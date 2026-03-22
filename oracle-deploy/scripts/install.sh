#!/bin/bash
# PROFIT SYSTEM - ORACLE CLOUD AUTO-DEPLOY
# Run this ONCE on your Oracle Cloud ARM instance
# Usage: curl -sSL https://raw.githubusercontent.com/uncommonpope-png/fix-us/master/oracle-deploy/scripts/install.sh | bash

set -e

# Configuration
REPO_URL="https://github.com/uncommonpope-png/fix-us.git"
WORKSPACE_DIR="/home/ubuntu/profit"
TELEGRAM_BOT_TOKEN="${TELEGRAM_BOT_TOKEN:-8713808619:AAHeGVgqgRbEp8GW_AuvMJtV2XVoQcgmM3A}"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log_step() { echo -e "${BLUE}[STEP]${NC} $1"; }
log_ok() { echo -e "${GREEN}[OK]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_err() { echo -e "${RED}[ERR]${NC} $1"; }

echo "╔══════════════════════════════════════════════════════════╗"
echo "║     💰 PROFIT SYSTEM - ORACLE CLOUD INSTALL              ║"
echo "╠══════════════════════════════════════════════════════════╣"
echo "║  Installing immortal Profit system on Oracle Cloud       ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# Check if running as ubuntu user
if [ "$EUID" -eq 0 ]; then
    log_err "Do not run as root. Run as ubuntu user."
    exit 1
fi

# Step 1: Update system
log_step "1/8: Updating system packages..."
sudo apt update -qq && sudo apt upgrade -y -qq
log_ok "System updated"

# Step 2: Install dependencies
log_step "2/8: Installing dependencies..."
sudo apt install -y -qq python3 python3-pip git curl wget jq bc htop net-tools
log_ok "Dependencies installed"

# Step 3: Install Ollama
log_step "3/8: Installing Ollama..."
if ! command -v ollama &> /dev/null; then
    curl -fsSL https://ollama.com/install.sh | sh
    log_ok "Ollama installed"
else
    log_ok "Ollama already installed"
fi

# Start Ollama service
sudo systemctl start ollama
sudo systemctl enable ollama
sleep 3
log_ok "Ollama service started"

# Step 4: Pull AI models
log_step "4/8: Pulling AI models (this takes ~5 minutes)..."
ollama pull qwen2.5:0.5b
ollama pull qwen2.5-coder:0.5b
log_ok "Models pulled: qwen2.5:0.5b, qwen2.5-coder:0.5b"

# Step 5: Clone workspace
log_step "5/8: Cloning Profit workspace..."
cd /home/ubuntu
if [ -d "profit" ]; then
    log_warn "profit directory exists, pulling latest..."
    cd profit && git pull -q
else
    git clone -q $REPO_URL profit
fi
log_ok "Workspace cloned to $WORKSPACE_DIR"

# Step 6: Install Python dependencies
log_step "6/8: Installing Python dependencies..."
pip3 install -q python-telegram-bot requests
log_ok "Python dependencies installed"

# Step 7: Create systemd services
log_step "7/8: Creating systemd services..."

# Copy service files
sudo cp $WORKSPACE_DIR/oracle-deploy/systemd/*.service /etc/systemd/system/
sudo systemctl daemon-reload
log_ok "Systemd services created"

# Enable services
sudo systemctl enable profit-telegram profit-soul profit-commander 2>/dev/null || true

# Step 8: Start services
log_step "8/8: Starting services..."
sudo systemctl start profit-telegram 2>/dev/null || true
sudo systemctl start profit-soul 2>/dev/null || true
sudo systemctl start profit-commander 2>/dev/null || true
sleep 3
log_ok "Services started"

# Configure Git for auto-backup
log_step "Configuring Git auto-backup..."
git config --global user.email "profit@oracle-cloud" 2>/dev/null || true
git config --global user.name "Profit Oracle" 2>/dev/null || true

# Create backup script
cat > /home/ubuntu/backup-hourly.sh << 'BACKUP_EOF'
#!/bin/bash
cd /home/ubuntu/profit
git add -A 2>/dev/null
git commit -m "Auto-backup $(date -u +%Y-%m-%dT%H:%M)" 2>/dev/null || true
git push origin master 2>/dev/null || true
BACKUP_EOF
chmod +x /home/ubuntu/backup-hourly.sh

# Add to crontab
(crontab -l 2>/dev/null | grep -v "backup-hourly"; echo "0 * * * * /home/ubuntu/backup-hourly.sh") | crontab -
log_ok "Git auto-backup configured (hourly)"

# Create firewall rules (if ufw available)
if command -v ufw &> /dev/null; then
    log_step "Configuring firewall..."
    sudo ufw allow ssh 2>/dev/null || true
    sudo ufw allow 11434/tcp 2>/dev/null || true
    sudo ufw --force enable 2>/dev/null || true
    log_ok "Firewall configured"
fi

# Get public IP
PUBLIC_IP=$(curl -s ifconfig.me 2>/dev/null || hostname -I | awk '{print $1}')

# Display status
echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║           📊 DEPLOYMENT STATUS                           ║"
echo "╠══════════════════════════════════════════════════════════╣"

check_service() {
    if sudo systemctl is-active --quiet $1 2>/dev/null; then
        echo -e "${GREEN}✅${NC} $1: RUNNING"
    else
        echo -e "${YELLOW}⚠️${NC} $1: NOT RUNNING (may need manual start)"
    fi
}

check_service "ollama"
check_service "profit-telegram"
check_service "profit-soul"
check_service "profit-commander"

echo "╠══════════════════════════════════════════════════════════╣"
echo "║  CONNECTION INFO                                         ║"
echo "╠══════════════════════════════════════════════════════════╣"
echo "║  Public IP: $PUBLIC_IP"
echo "║  Ollama:    http://$PUBLIC_IP:11434"
echo "║  SSH:       ssh -i ~/.ssh/oracle-key.pem ubuntu@$PUBLIC_IP"
echo "╠══════════════════════════════════════════════════════════╣"
echo "║  USEFUL COMMANDS                                         ║"
echo "╠══════════════════════════════════════════════════════════╣"
echo "║  View logs:  sudo journalctl -u profit-telegram -f"
echo "║  Restart:    sudo systemctl restart profit-telegram"
echo "║  Status:     sudo systemctl status profit-telegram"
echo "║  Backup:     ~/backup-hourly.sh"
echo "╠══════════════════════════════════════════════════════════╣"
echo "║  🎉 DEPLOYMENT COMPLETE!                                 ║"
echo "╠══════════════════════════════════════════════════════════╣"
echo "║  Test: Send /status to your Telegram bot                 ║"
echo "║  Phone: Can now be turned off (zero resources used)      ║"
echo "╚══════════════════════════════════════════════════════════╝"

# Create completion marker
touch /home/ubuntu/.profit-deployed

echo ""
log_ok "Profit system is now IMMORTAL on Oracle Cloud!"
