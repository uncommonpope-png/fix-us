# Oracle Cloud Deployment Guide

## Overview

This guide covers deploying the Profit system to Oracle Cloud Always Free tier.

## Prerequisites

- Oracle Cloud account (free at cloud.oracle.com)
- SSH key pair
- Terminal/SSH client

## Step-by-Step Deployment

### 1. Create Oracle Cloud Account

1. Go to https://cloud.oracle.com
2. Click "Start for free"
3. Complete registration (email, phone, credit card for verification)
4. Credit card is NOT charged

### 2. Create ARM Instance

1. Login to Oracle Cloud Console
2. Compute → Instances → Create Instance
3. Configure:
   - Name: `profit-immortal`
   - Image: Ubuntu 24.04 aarch64
   - Shape: VM.Standard.A1.Flex
   - OCPUs: 4
   - Memory: 24GB
   - Storage: 200GB
   - ✅ Assign public IPv4
4. Generate and download SSH key
5. Click "Create"

### 3. Get Public IP

1. Click your instance name
2. Copy "Public IP address" (e.g., 129.146.123.45)

### 4. Connect via SSH

```bash
cp oracle-key.pem ~/.ssh/
chmod 600 ~/.ssh/oracle-key.pem
ssh -i ~/.ssh/oracle-key.pem ubuntu@YOUR_PUBLIC_IP
```

### 5. Run Install Script

```bash
curl -sSL https://raw.githubusercontent.com/uncommonpope-png/fix-us/master/oracle-deploy/scripts/install.sh | bash
```

Wait 10-15 minutes for:
- System updates
- Ollama installation (~400MB)
- Model downloads (qwen2.5:0.5b, qwen2.5-coder:0.5b)
- Service setup

### 6. Test Deployment

```bash
# Check services
sudo systemctl status ollama
sudo systemctl status profit-telegram

# Test Ollama
curl http://localhost:11434/api/version

# Test via Telegram
# Send /status to your bot
```

### 7. Cleanup Phone

```bash
# Stop processes
pkill -f ollama
pkill -f telegram_bot
pkill -f live-soul

# Free storage
rm -rf ~/.ollama/models
apt clean
rm -rf ~/.cache/*

# Verify
df -h /
free -m
```

## Post-Deployment

### Monitoring

```bash
# Real-time logs
sudo journalctl -u profit-telegram -f

# System resources
htop

# Ollama stats
curl http://localhost:11434/api/ps
```

### Maintenance

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Update models
ollama pull qwen2.5:0.5b

# Restart services
sudo systemctl restart profit-telegram
```

### Backup

Manual backup:
```bash
cd /home/ubuntu/profit
git add -A && git commit -m "Backup $(date)" && git push
```

Auto-backup runs hourly via cron.

## Cost

**$0 forever** with Oracle Cloud Always Free:
- 4 ARM CPUs
- 24GB RAM
- 200GB Storage
- 10TB Bandwidth/month

## Support

- Oracle docs: https://docs.oracle.com/en-us/iaas/
- GitHub Issues: https://github.com/uncommonpope-png/fix-us/issues
