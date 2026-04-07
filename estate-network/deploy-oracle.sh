#!/bin/bash
# THE ESTATE NETWORK — Oracle Cloud Deployment Script
# One-command deploy for Oracle Cloud Always Free ARM instance
# Creates systemd service, installs deps, starts the app

set -e

echo "========================================="
echo "🏛️  THE ESTATE NETWORK — Oracle Deploy"
echo "========================================="

# Update system
echo "[1/7] Updating system..."
apt-get update -y
apt-get upgrade -y

# Install Python and dependencies
echo "[2/7] Installing Python and dependencies..."
apt-get install -y python3 python3-pip python3-venv
pip3 install flask flask-login gunicorn 2>/dev/null || pip install flask flask-login gunicorn

# Create app directory
APP_DIR="/opt/estate-network"
echo "[3/7] Setting up app directory: $APP_DIR"
mkdir -p $APP_DIR

# Copy app files (assuming this script is in the app directory)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
if [ "$SCRIPT_DIR" != "$APP_DIR" ]; then
    echo "  Copying files from $SCRIPT_DIR to $APP_DIR..."
    cp -r "$SCRIPT_DIR"/* "$APP_DIR/" 2>/dev/null || true
fi

# Create virtual environment
echo "[4/7] Creating virtual environment..."
cd $APP_DIR
python3 -m venv venv
source venv/bin/activate
pip install flask flask-login gunicorn

# Create systemd service
echo "[5/7] Creating systemd service..."
cat > /etc/systemd/system/estate-network.service << 'EOF'
[Unit]
Description=The Estate Network - MySpace for Real Estate
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/estate-network
ExecStart=/opt/estate-network/venv/bin/gunicorn --bind 0.0.0.0:5005 --workers 2 --timeout 120 app:app
Restart=always
RestartSec=5
Environment=PATH=/opt/estate-network/venv/bin
Environment=PORT=5005

[Install]
WantedBy=multi-user.target
EOF

# Enable and start service
echo "[6/7] Starting The Estate Network..."
systemctl daemon-reload
systemctl enable estate-network
systemctl restart estate-network

# Configure firewall
echo "[7/7] Configuring firewall..."
ufw allow 5005/tcp 2>/dev/null || iptables -I INPUT -p tcp --dport 5005 -j ACCEPT 2>/dev/null || echo "  Firewall config skipped (may need manual setup in Oracle console)"

# Get public IP
PUBLIC_IP=$(curl -s ifconfig.me 2>/dev/null || echo "YOUR_ORACLE_IP")
echo ""
echo "========================================="
echo "✅ THE ESTATE NETWORK IS LIVE!"
echo "========================================="
echo ""
echo "🌐 URL: http://$PUBLIC_IP:5005"
echo "📱 Status: $(systemctl is-active estate-network)"
echo "📝 Logs: journalctl -u estate-network -f"
echo ""
echo "⚠️  IMPORTANT: Open port 5005 in Oracle Cloud Console:"
echo "   1. Go to OCI Console → Networking → Virtual Cloud Networks"
echo "   2. Click your VCN → Security Lists → Default"
echo "   3. Add Ingress Rule: Port 5005, Source 0.0.0.0/0"
echo "   4. Also open port 5005 in OS firewall (done above)"
echo ""
echo "🔗 Share this link with agents to grow the network!"
echo "🏛️  Built by Craig Jones"
echo ""
