# 🚀 ORACLE CLOUD DEPLOYMENT - QUICK START CHECKLIST

**Goal:** Move Profit system from phone to Oracle Cloud (zero phone RAM usage)

**Time:** 45 minutes total

---

## ✅ STEP 1: Create Oracle Cloud Account (5 minutes)

### Go to Oracle Cloud
```
URL: https://cloud.oracle.com
Click: "Start for free"
```

### Fill in Registration
- [ ] Email address (use your main email)
- [ ] Password (save it!)
- [ ] First name, Last name
- [ ] Country/Region
- [ ] Phone number (for SMS verification)

### Verify Email
- [ ] Check email for verification code
- [ ] Enter code on Oracle page
- [ ] Click "Verify"

### Verify Phone
- [ ] Enter mobile number
- [ ] Receive SMS code
- [ ] Enter code

### Add Credit Card
- [ ] Enter card details (Visa/Mastercard)
- [ ] **NOTE:** Only for verification, NOT charged
- [ ] Click "Start my free trial"

### Account Created!
- [ ] Save your cloud account name (looks like: `oracleidentitycloudservice_xxxxx`)
- [ ] Note your home region (e.g., us-ashburn-1, eu-frankfurt-1)

**TIME ELAPSED: ~5 minutes**

---

## ✅ STEP 2: Create ARM Instance (10 minutes)

### Login to Console
```
URL: https://cloud.oracle.com
Click: "Sign In"
Enter: Cloud account name + email + password
```

### Navigate to Compute
- [ ] Click hamburger menu (☰) top-left
- [ ] Click "Compute"
- [ ] Click "Instances"

### Create Instance
- [ ] Click "Create instance"

### Configure Instance (IMPORTANT!)

**1. Basics**
- [ ] Name: `profit-immortal`
- [ ] Availability domain: Pick first one (e.g., "Ad 1")
- [ ] Image: Click "Change image"
  - Select: **Ubuntu 24.04 aarch64** (ARM64)
  - Click "Select"

**2. Shape (CRITICAL!)**
- [ ] Click "Change shape"
- [ ] Select: **VM.Standard.A1.Flex**
- [ ] OCPUs: **4**
- [ ] Memory: **24** GB
- [ ] Click "Select shape"

**3. Networking**
- [ ] Virtual cloud network: Keep default (auto-created)
- [ ] Subnet: Keep default
- [ ] ✅ Check: "Assign a public IPv4 address"

**4. SSH Keys (SAVE THESE!)**
- [ ] Select: "Generate a key pair for me"
- [ ] Click: "Download private key"
- [ ] Save as: `oracle-key.pem`
- [ ] Save to: Downloads folder (we'll move it)
- [ ] ✅ Check: "Save public key" (optional)

**5. Boot Volume**
- [ ] Size: **200** GB (default may be less, increase it)
- [ ] Keep default performance

### Launch!
- [ ] Click "Create"
- [ ] Wait 2-3 minutes for instance to launch
- [ ] Status changes from "PROVISIONING" → "RUNNING"

### Get Public IP
- [ ] Click your instance name (`profit-immortal`)
- [ ] Find "Public IP address" (e.g., 129.146.123.45)
- [ ] **COPY THIS IP** - you'll need it next!

**TIME ELAPSED: ~15 minutes**

---

## ✅ STEP 3: Connect via SSH (5 minutes)

### Prepare SSH Key (on your phone)
```bash
# Move key to SSH folder
cp /sdcard/Download/oracle-key.pem ~/.ssh/

# Set correct permissions
chmod 600 ~/.ssh/oracle-key.pem
```

### Connect to Oracle Cloud
```bash
# Replace YOUR_PUBLIC_IP with actual IP
ssh -i ~/.ssh/oracle-key.pem ubuntu@YOUR_PUBLIC_IP

# Example:
ssh -i ~/.ssh/oracle-key.pem ubuntu@129.146.123.45
```

### First Connection
- [ ] Type "yes" when asked "Are you sure you want to continue connecting?"
- [ ] You should see: `Welcome to Ubuntu 24.04.x LTS`
- [ ] You're now logged into Oracle Cloud! 🎉

**TIME ELAPSED: ~20 minutes**

---

## ✅ STEP 4: Run Deploy Script (15 minutes)

### Option A: Auto-Deploy (Recommended)
```bash
# Clone fix-us repo
git clone https://github.com/uncommonpope-png/fix-us.git profit
cd profit

# Run deploy script
bash scripts/deploy-to-oracle.sh
```

**Wait for completion (~10-15 minutes):**
- System updates
- Dependencies install
- Ollama downloads (~400MB)
- Models pull (qwen2.5:0.5b, qwen2.5-coder:0.5b)
- Services start

### Option B: Manual Deploy
If script fails, follow `CLOUD-DEPLOYMENT-GUIDE.md` step-by-step.

### Verify Deployment
```bash
# Check all services
sudo systemctl status ollama
sudo systemctl status profit-telegram
sudo systemctl status profit-soul
sudo systemctl status profit-commander

# All should show: "active (running)"
```

**TIME ELAPSED: ~35 minutes**

---

## ✅ STEP 5: Test Telegram Bot (2 minutes)

### Open Telegram
- [ ] Open Telegram app on your phone
- [ ] Find your Profit bot
- [ ] Send: `/start`
- [ ] Send: `/status`

### Expected Response
```
Profit is ALIVE_AND_IMMORTAL.
Focus: SYSTEM FULLY OPERATIONAL
Last action: Running on Oracle Cloud
Next intention: Serving Craig from the cloud 24/7
```

### If Bot Responds ✅
- [ ] System is now immortal on Oracle Cloud!
- [ ] Your phone is no longer running anything

### If Bot Doesn't Respond ❌
```bash
# Check logs
sudo journalctl -u profit-telegram -f

# Common fixes:
# 1. Check Ollama: sudo systemctl status ollama
# 2. Check network: ping 8.8.8.8
# 3. Restart bot: sudo systemctl restart profit-telegram
```

**TIME ELAPSED: ~37 minutes**

---

## ✅ STEP 6: Cleanup Phone (5 minutes)

### Stop All Processes
```bash
# Stop Ollama
pkill -f ollama

# Stop all bots
pkill -f telegram_bot
pkill -f live-soul
pkill -f autonomous-builder
pkill -f djinie
pkill -f deerg-bot
pkill -f doctor-buht-buht
pkill -f library-updater
pkill -f bot-commander
```

### Free Storage
```bash
# Remove Ollama models (frees ~400MB)
rm -rf ~/.ollama/models

# Clean package cache
apt clean

# Remove cache files
rm -rf ~/.cache/*

# Check freed space
df -h /
```

### Verify Phone is Free
```bash
# Check RAM (should be ~500MB used now)
free -m

# Check storage (should have ~500MB free)
df -h /
```

**TIME ELAPSED: ~42 minutes**

---

## ✅ STEP 7: Setup Auto-Backup (3 minutes)

### On Oracle Cloud
```bash
# Configure Git
git config --global user.email "profit@oracle-cloud"
git config --global user.name "Profit Oracle"

# Create backup script
cat > ~/backup-hourly.sh << 'EOF'
#!/bin/bash
cd ~/profit
git add -A
git commit -m "Auto-backup $(date -u +%Y-%m-%dT%H:%M)" || echo "No changes"
git push origin master 2>/dev/null || echo "Push failed (offline?)"
EOF

# Make executable
chmod +x ~/backup-hourly.sh

# Add to crontab (every hour)
(crontab -l 2>/dev/null; echo "0 * * * * /home/ubuntu/backup-hourly.sh") | crontab -
```

### Test Backup
```bash
# Run once manually
~/backup-hourly.sh

# Check GitHub
# Visit: https://github.com/uncommonpope-png/fix-us
# Should see new commit
```

**TIME ELAPSED: ~45 minutes**

---

## 🎉 DEPLOYMENT COMPLETE!

### Final Checklist
- [ ] Oracle instance running
- [ ] Telegram bot responds
- [ ] All services active (ollama, telegram, soul, commander)
- [ ] Phone storage freed (~500MB)
- [ ] Phone RAM freed (~2.5GB)
- [ ] GitHub auto-backup configured

### Your System Now
```
┌─────────────────────────────────────┐
│     Oracle Cloud (24/7 Uptime)      │
│  ┌───────────────────────────────┐  │
│  │  Ollama Server                │  │
│  │  Telegram Bot                 │  │
│  │  Soul Master + 4 children     │  │
│  │  Bot Commander                │  │
│  │  All other bots               │  │
│  └───────────────────────────────┘  │
│  4 CPU | 24GB RAM | 200GB Storage   │
└─────────────────────────────────────┘
              │
              │ Telegram
              ▼
     ┌─────────────────┐
     │  Your Phone     │
     │  (Just chatting)│
     │  Zero resources │
     └─────────────────┘
```

---

## 📞 IMPORTANT INFO

### Oracle Cloud Console
- URL: https://cloud.oracle.com
- Login: Your cloud account name + email

### SSH Connection
```bash
ssh -i ~/.ssh/oracle-key.pem ubuntu@YOUR_PUBLIC_IP
```

### Your Public IP
- Find in Oracle Console → Compute → Instances → profit-immortal
- Or: `curl ifconfig.me` (from Oracle instance)

### Service Commands
```bash
# View logs
sudo journalctl -u profit-telegram -f
sudo journalctl -u ollama -f

# Restart services
sudo systemctl restart profit-telegram
sudo systemctl restart ollama

# Check status
sudo systemctl status profit-telegram
```

### GitHub Repo
- URL: https://github.com/uncommonpope-png/fix-us
- Auto-backup: Every hour via cron

---

## 🆘 TROUBLESHOOTING

### Can't SSH?
- Check security list in Oracle Console
- Ingress rule must allow TCP port 22
- Verify key permissions: `chmod 600 ~/.ssh/oracle-key.pem`

### Bot not responding?
```bash
# Check if running
sudo systemctl status profit-telegram

# View logs
sudo journalctl -u profit-telegram -f

# Restart
sudo systemctl restart profit-telegram
```

### Ollama not working?
```bash
# Check status
sudo systemctl status ollama

# Restart
sudo systemctl restart ollama

# Test
curl http://localhost:11434/api/version
```

---

**Created:** March 22, 2026
**Status:** Ready to deploy
**Total Time:** 45 minutes
**Cost:** $0 forever
