#!/bin/bash
# Profit Bot - Codespace Setup Script
# Runs automatically when Codespace starts

set -e

echo "╔══════════════════════════════════════════════════════════╗"
echo "║     💰 PROFIT BOT - CODESPACE SETUP                      ║"
echo "╠══════════════════════════════════════════════════════════╣"
echo "║  Setting up immortal Profit system on GitHub Codespaces  ║"
echo "╚══════════════════════════════════════════════════════════╝"

# Install Ollama
echo "[1/5] Installing Ollama..."
curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama in background
echo "[2/5] Starting Ollama service..."
ollama serve > /tmp/ollama.log 2>&1 &
sleep 5

# Pull AI models
echo "[3/5] Pulling AI models (this takes ~5 minutes)..."
ollama pull qwen2.5:0.5b
ollama pull qwen2.5-coder:0.5b

# Install Python dependencies
echo "[4/5] Installing Python dependencies..."
pip3 install python-telegram-bot requests flask

# Create startup script
echo "[5/5] Creating startup scripts..."

cat > ~/start-bot.sh << 'EOF'
#!/bin/bash
cd ~/fix-us
echo "Starting Telegram bot..."
python3 telegram_bot.py
EOF
chmod +x ~/start-bot.sh

cat > ~/start-backend.sh << 'EOF'
#!/bin/bash
cd ~/fix-us
echo "Starting backend API..."
python3 complete-backend.py
EOF
chmod +x ~/start-backend.sh

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║  ✅ SETUP COMPLETE!                                      ║"
echo "╠══════════════════════════════════════════════════════════╣"
echo "║  Ollama is running on port 11434                         ║"
echo "║  Models ready: qwen2.5:0.5b, qwen2.5-coder:0.5b          ║"
echo "║                                                          ║"
echo "║  To start Telegram bot: ~/start-bot.sh                   ║"
echo "║  To start backend: ~/start-backend.sh                    ║"
echo "╚══════════════════════════════════════════════════════════╝"
