#!/bin/bash
# PROFIT COPILOT - Quick Start Script

set -e

echo "╔══════════════════════════════════════════════════════════╗"
echo "║  🤖 PROFIT COPILOT - INSTALLER                          ║"
echo "╠══════════════════════════════════════════════════════════╣"
echo "║  Setting up your AI wingman...                           ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

COPILOT_DIR="$HOME/fix-us/copilot"

# Install dependencies
echo "[1/3] Installing Python dependencies..."
pip3 install -q requests python-telegram-bot

# Create memory directory
echo "[2/3] Creating memory directories..."
mkdir -p $COPILOT_DIR/memory
mkdir -p $COPILOT_DIR/config

# Create default config
cat > $COPILOT_DIR/config/settings.json << 'EOF'
{
  "name": "Copilot",
  "watch_interval": 5,
  "suggest_interval": 300,
  "auto_commit": true,
  "auto_deploy": false,
  "plt_scoring": true,
  "memory_updates": true,
  "telegram_notifications": true
}
EOF

echo "[3/3] Setup complete!"
echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║  ✅ COPILOT READY                                        ║"
echo "╠══════════════════════════════════════════════════════════╣"
echo "║  To run:                                                 ║"
echo "║    python3 ~/fix-us/copilot/scripts/copilot.py           ║"
echo "║                                                          ║"
echo "║  To run in background:                                   ║"
echo "║    nohup python3 ~/fix-us/copilot/scripts/copilot.py >   ║"
echo "║      ~/copilot.log 2>&1 &                                ║"
echo "╚══════════════════════════════════════════════════════════╝"
