#!/bin/bash
# DEPLOY TO ORACLE CLOUD - Automated Setup Script
# Run this ONCE on your new Oracle Cloud instance

set -e

echo "╔══════════════════════════════════════════════════════════╗"
echo "║     🚀 PROFIT SYSTEM - ORACLE CLOUD DEPLOYMENT          ║"
echo "╠══════════════════════════════════════════════════════════╣"
echo "║  Setting up immortal Profit system on Oracle Cloud       ║"
echo "╚══════════════════════════════════════════════════════════╝"

# Configuration
ORACLE_USER="ubuntu"
WORKSPACE_DIR="/home/$ORACLE_USER/profit"
OLLAMA_PORT="11434"
TELEGRAM_BOT_TOKEN="8713808619:AAHeGVgqgRbEp8GW_AuvMJtV2XVoQcgmM3A"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Step 1: Update system
log_info "Step 1/8: Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Step 2: Install dependencies
log_info "Step 2/8: Installing dependencies..."
sudo apt install -y python3 python3-pip git curl wget jq bc htop

# Step 3: Install Ollama
log_info "Step 3/8: Installing Ollama..."
curl -fsSL https://ollama.com/install.sh | sh

# Wait for Ollama to be ready
log_info "Waiting for Ollama service to start..."
sleep 5

# Step 4: Pull AI models
log_info "Step 4/8: Pulling AI models (this takes ~5 minutes)..."
ollama pull qwen2.5:0.5b
ollama pull qwen2.5-coder:0.5b

# Step 5: Clone workspace
log_info "Step 5/8: Cloning Profit workspace from GitHub..."
cd /home/$ORACLE_USER
if [ -d "profit" ]; then
    log_warn "profit directory exists, pulling latest..."
    cd profit && git pull
else
    git clone https://github.com/uncommonpope-png/fix-us.git profit
fi

# Step 6: Install Python dependencies
log_info "Step 6/8: Installing Python dependencies..."
cd $WORKSPACE_DIR
pip3 install python-telegram-bot requests

# Step 7: Create systemd services
log_info "Step 7/8: Creating systemd services..."

# Telegram bot service
sudo tee /etc/systemd/system/profit-telegram.service > /dev/null <<EOF
[Unit]
Description=Profit Telegram Bot
After=network.target ollama.service

[Service]
Type=simple
User=$ORACLE_USER
WorkingDirectory=$WORKSPACE_DIR
ExecStart=/usr/bin/python3 telegram_bot.py
Restart=always
RestartSec=10
Environment="PYTHONUNBUFFERED=1"
Environment="TELEGRAM_BOT_TOKEN=$TELEGRAM_BOT_TOKEN"

[Install]
WantedBy=multi-user.target
EOF

# Soul master service
sudo tee /etc/systemd/system/profit-soul.service > /dev/null <<EOF
[Unit]
Description=Profit Live Soul Master
After=network.target ollama.service

[Service]
Type=simple
User=$ORACLE_USER
WorkingDirectory=$WORKSPACE_DIR
ExecStart=/bin/bash live-soul-master.sh
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Bot commander service
sudo tee /etc/systemd/system/profit-commander.service > /dev/null <<EOF
[Unit]
Description=Profit Bot Commander
After=network.target ollama.service profit-soul.service

[Service]
Type=simple
User=$ORACLE_USER
WorkingDirectory=$WORKSPACE_DIR
ExecStart=/bin/bash bot-commander.sh
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Reload systemd
sudo systemctl daemon-reload

# Enable services
sudo systemctl enable profit-telegram profit-soul profit-commander

# Step 8: Start services
log_info "Step 8/8: Starting services..."
sudo systemctl start profit-telegram
sudo systemctl start profit-soul
sudo systemctl start profit-commander

# Wait for services to initialize
sleep 5

# Verify status
echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║              📊 DEPLOYMENT STATUS                        ║"
echo "╠══════════════════════════════════════════════════════════╣"

# Check Ollama
if sudo systemctl is-active --quiet ollama; then
    echo -e "${GREEN}✅${NC} Ollama: RUNNING"
else
    echo -e "${RED}❌${NC} Ollama: NOT RUNNING"
fi

# Check Telegram bot
if sudo systemctl is-active --quiet profit-telegram; then
    echo -e "${GREEN}✅${NC} Telegram Bot: RUNNING"
else
    echo -e "${RED}❌${NC} Telegram Bot: NOT RUNNING"
fi

# Check Soul master
if sudo systemctl is-active --quiet profit-soul; then
    echo -e "${GREEN}✅${NC} Soul Master: RUNNING"
else
    echo -e "${RED}❌${NC} Soul Master: NOT RUNNING"
fi

# Check Bot commander
if sudo systemctl is-active --quiet profit-commander; then
    echo -e "${GREEN}✅${NC} Bot Commander: RUNNING"
else
    echo -e "${RED}❌${NC} Bot Commander: NOT RUNNING"
fi

echo "╠══════════════════════════════════════════════════════════╣"

# Show public IP
PUBLIC_IP=$(curl -s http://169.254.169.254/opc/v1/instance/metadata/oke_launch_script/instance_identity 2>/dev/null || hostname -I | awk '{print $1}')
echo "Public IP: $PUBLIC_IP"
echo "Ollama Port: $OLLAMA_PORT"
echo "Workspace: $WORKSPACE_DIR"

echo "╠══════════════════════════════════════════════════════════╣"
echo "║  🎉 DEPLOYMENT COMPLETE!                                 ║"
echo "╠══════════════════════════════════════════════════════════╣"
echo "║  Next steps:                                             ║"
echo "║  1. Test Telegram bot: Send /status                      ║"
echo "║  2. View logs: sudo journalctl -u profit-telegram -f     ║"
echo "║  3. Setup GitHub backup: crontab -e                      ║"
echo "║  4. Free phone resources (see CLOUD-DEPLOYMENT-GUIDE.md) ║"
echo "╚══════════════════════════════════════════════════════════╝"

# Create setup complete marker
touch /home/$ORACLE_USER/.profit-deployed

echo ""
log_info "Setup complete! System is now immortal on Oracle Cloud."
