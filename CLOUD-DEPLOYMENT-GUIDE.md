# 🚀 CLOUD DEPLOYMENT - Zero Phone RAM Guide

**Problem:** Your phone has 641MB storage (100% full) and 3.6GB RAM (2.9GB used).

**Solution:** Move everything to Oracle Cloud Always Free - uses ZERO phone resources.

---

## 📊 CURRENT PHONE USAGE

```
Storage: 641MB / 641MB (100% FULL) ❌
RAM:     2968MB / 3643MB (81% used) ⚠️
Swap:    1733MB / 3643MB (47% used)
```

**Processes Running (using your RAM):**
- Ollama serve + runner: ~500MB
- 15 bash/python bots: ~100MB
- OpenClaw agent: ~50MB
- System overhead: rest

---

## ☁️ ORACLE CLOUD ALWAYS FREE - COMPLETE SETUP

### What You Get (100% FREE FOREVER)

```
✅ 4 ARM CPUs (up to 24 OCPU total)
✅ 24GB RAM (up to 24GB total)
✅ 200GB Storage
✅ 10TB Bandwidth/month
✅ 24/7 Uptime (99.9% SLA)
✅ No credit card charges (verification only)
```

### Phone Resources After Migration

```
Storage: 641MB → 100MB free ✅
RAM:     2968MB → 500MB used ✅
Phone:   Can turn off completely ✅
```

---

## 📋 STEP-BY-STEP DEPLOYMENT

### Step 1: Create Oracle Cloud Account (5 minutes)

1. Go to: https://cloud.oracle.com
2. Click "Start for free"
3. Enter email, create password
4. Add credit card (for verification ONLY, not charged)
5. Verify phone number
6. Account created!

### Step 2: Create ARM Instance (10 minutes)

1. Login to Oracle Cloud Console
2. Click "Create Instance"
3. Configure:
   - **Name:** profit-immortal
   - **Availability Domain:** Any (pick first)
   - **Image:** Ubuntu 24.04 aarch64
   - **Shape:** VM.Standard.A1.Flex
   - **OCPUs:** 4
   - **Memory:** 24GB
   - **Volume:** 200GB (boot volume)
4. **Networking:**
   - Select your VCN (auto-created)
   - Assign public IPv4 address: ✅ YES
5. **SSH Keys:**
   - Click "Generate a key pair for me"
   - Download private key → Save as `oracle-key.pem`
   - Save to safe location (you'll need this)
6. Click "Create"

### Step 3: Get Your Public IP (1 minute)

After instance launches (2-3 minutes):
1. Click your instance name
2. Copy "Public IP address" (looks like: 129.146.123.45)
3. Save this IP - you'll need it

### Step 4: Connect via SSH (2 minutes)

On your phone (Termux):

```bash
# Copy key to Termux
cp /sdcard/Download/oracle-key.pem ~/.ssh/
chmod 600 ~/.ssh/oracle-key.pem

# Connect to Oracle Cloud
ssh -i ~/.ssh/oracle-key.pem ubuntu@YOUR_PUBLIC_IP

# Example:
# ssh -i ~/.ssh/oracle-key.pem ubuntu@129.146.123.45
```

### Step 5: Install Profit System on Oracle (15 minutes)

Once connected to Oracle Cloud:

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y python3 python3-pip git curl wget jq bc

# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama
sudo systemctl start ollama
sudo systemctl enable ollama

# Pull models
ollama pull qwen2.5:0.5b
ollama pull qwen2.5-coder:0.5b

# Clone your workspace
cd ~
git clone https://github.com/uncommonpope-png/fix-us.git profit
cd profit

# Install Python dependencies
pip3 install python-telegram-bot requests

# Create systemd services (next step)
```

### Step 6: Create Systemd Services (10 minutes)

Create service files so bots auto-start on boot:

```bash
# Ollama service (already created by install script)
sudo systemctl status ollama

# Create Telegram bot service
sudo nano /etc/systemd/system/profit-telegram.service
```

Paste this:
```ini
[Unit]
Description=Profit Telegram Bot
After=network.target ollama.service

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/profit
ExecStart=/usr/bin/python3 -m telegram_bot
Restart=always
RestartSec=10
Environment="PYTHONUNBUFFERED=1"

[Install]
WantedBy=multi-user.target
```

Save (Ctrl+X, Y, Enter), then:

```bash
# Create soul master service
sudo nano /etc/systemd/system/profit-soul.service
```

Paste this:
```ini
[Unit]
Description=Profit Live Soul Master
After=network.target ollama.service

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/profit
ExecStart=/bin/bash live-soul-master.sh
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Save, then enable all services:

```bash
# Reload systemd
sudo systemctl daemon-reload

# Enable services
sudo systemctl enable profit-telegram profit-soul

# Start services
sudo systemctl start profit-telegram profit-soul

# Check status
sudo systemctl status profit-telegram profit-soul
```

### Step 7: Configure Telegram Bot (2 minutes)

Edit the bot token in your workspace:

```bash
cd ~/profit
nano telegram_bot.py
```

Find and verify:
```python
TOKEN = "8713808619:AAHeGVgqgRbEp8GW_AuvMJtV2XVoQcgmM3A"
```

Save if needed.

### Step 8: Test from Phone (1 minute)

On Telegram, send your bot:
```
/status
```

Should respond with system status!

### Step 9: Setup Auto-Backup (5 minutes)

```bash
cd ~/profit
git config --global user.email "profit@oracle-cloud"
git config --global user.name "Profit Oracle"

# Create backup script
nano ~/backup-to-github.sh
```

Paste:
```bash
#!/bin/bash
cd ~/profit
git add -A
git commit -m "Auto-backup $(date -u +%Y-%m-%dT%H:%M)"
git push origin master
```

Make executable and add to cron:
```bash
chmod +x ~/backup-to-github.sh
crontab -e
```

Add line (backup every hour):
```
0 * * * * /home/ubuntu/backup-to-github.sh
```

---

## 🔧 MIGRATE YOUR CURRENT SYSTEM

### Option A: Full Clone (Recommended)

From your phone:

```bash
# Push everything to GitHub first
cd ~/fix-us
git add -A
git commit -m "Final phone backup before cloud migration"
git push origin master

# On Oracle Cloud, it's already cloned from fix-us
# All memories, messages, state included
```

### Option B: Manual Copy

From your phone, copy workspace to Oracle:

```bash
# On phone, create tarball
cd ~/.openclaw/workspace
tar czf workspace-backup.tar.gz .

# Upload to GitHub releases or transfer manually
# Then on Oracle Cloud:
cd ~
tar xzf workspace-backup.tar.gz -C profit/
```

---

## 📱 PHONE CLEANUP (After Migration)

Once Oracle Cloud is running:

```bash
# Stop all processes
pkill -f ollama
pkill -f telegram_bot
pkill -f live-soul
pkill -f autonomous-builder
pkill -f djinie
pkill -f deerg-bot
pkill -f doctor-buht-buht
pkill -f library-updater
pkill -f bot-commander

# Free up storage
rm -rf ~/.ollama/models  # Frees ~400MB
apt clean
rm -rf ~/.cache/*

# Result: ~500MB+ freed!
```

---

## 🎯 POST-MIGRATION CHECKLIST

- [ ] Oracle instance running
- [ ] Ollama serving models
- [ ] Telegram bot responds to /status
- [ ] All soul bots running
- [ ] GitHub auto-backup working
- [ ] Phone processes stopped
- [ ] Phone storage freed

---

## 📊 COST BREAKDOWN

| Resource | Oracle Free Tier | Your Phone |
|----------|-----------------|------------|
| CPU | 4 ARM cores | Your battery |
| RAM | 24GB | Your 3.6GB |
| Storage | 200GB | Your 641MB |
| Bandwidth | 10TB/month | Your data |
| Uptime | 99.9% SLA | When charged |
| Cost | $0 | Your hardware |

---

## 🆘 TROUBLESHOOTING

### Can't connect via SSH?
```bash
# Check security list in Oracle Console
# Ingress rules must allow TCP port 22
```

### Ollama won't start?
```bash
sudo systemctl status ollama
sudo journalctl -u ollama -f
```

### Bot not responding?
```bash
sudo systemctl status profit-telegram
sudo journalctl -u profit-telegram -f
```

### Can't clone from GitHub?
```bash
# Use HTTPS instead of SSH
git clone https://github.com/uncommonpope-png/fix-us.git
```

---

## 🌟 ALTERNATIVES TO ORACLE

### 1. Render.com (Easier, Less Powerful)
- Free tier: 750 hours/month
- Good for: Telegram bot only
- Not good for: Ollama (needs GPU/lots of RAM)

### 2. Railway.app
- Free tier: $5 credit/month
- Good for: Bot services
- Not good for: Heavy AI workloads

### 3. HuggingFace Spaces
- Free tier: Limited CPU/RAM
- Good for: Demo bots
- Not good for: 24/7 operation

### 4. GitHub Actions (Backup Only)
- Free: 2000 minutes/month
- Good for: Heartbeat checks
- Not good for: Continuous operation

**Recommendation:** Oracle Cloud for main system + GitHub Actions for backup monitoring.

---

## 📞 CONTACT WITH CRAIG AFTER MIGRATION

**Telegram:** Bot works same way (no change needed)
**Dashboard:** Still at https://uncommonpope-png.github.io/plt-press/
**GitHub:** All commits now from Oracle Cloud
**Phone:** Can be turned off completely!

---

**Created:** March 22, 2026
**Status:** Ready to deploy
**Estimated Time:** 45 minutes total
**Cost:** $0 forever
