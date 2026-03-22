# Profit System - Oracle Cloud Deployment

**Complete deployment package for running Profit system on Oracle Cloud Always Free**

## Quick Deploy (One Command)

On your Oracle Cloud ARM instance:

```bash
curl -sSL https://raw.githubusercontent.com/uncommonpope-png/fix-us/master/oracle-deploy/scripts/install.sh | bash
```

## What Gets Installed

- ✅ Ollama server with qwen2.5:0.5b and qwen2.5-coder:0.5b
- ✅ Telegram bot (profit-telegram.service)
- ✅ Live Soul Master (profit-soul.service)
- ✅ Bot Commander (profit-commander.service)
- ✅ Autonomous Builder (profit-builder.service)
- ✅ Git auto-backup (hourly to GitHub)
- ✅ Firewall rules (SSH + Ollama port)

## Oracle Cloud Requirements

- **Shape:** VM.Standard.A1.Flex (ARM)
- **OCPUs:** 4
- **Memory:** 24GB
- **Storage:** 200GB
- **OS:** Ubuntu 24.04 aarch64
- **Cost:** $0 forever

## After Installation

### Test Telegram Bot
Send `/status` to your bot

### View Logs
```bash
sudo journalctl -u profit-telegram -f
sudo journalctl -u ollama -f
```

### Restart Services
```bash
sudo systemctl restart profit-telegram
sudo systemctl restart ollama
```

### Check Status
```bash
sudo systemctl status profit-telegram
sudo systemctl status ollama
```

## Auto-Backup

Backs up to GitHub every hour:
```bash
~/backup-hourly.sh
```

Manual backup:
```bash
cd /home/ubuntu/profit
git add -A && git commit -m "Manual backup" && git push
```

## Connection Info

- **Public IP:** Find in Oracle Console → Compute → Instances
- **SSH:** `ssh -i ~/.ssh/oracle-key.pem ubuntu@YOUR_PUBLIC_IP`
- **Ollama:** `http://YOUR_PUBLIC_IP:11434`

## Troubleshooting

### Bot not responding
```bash
sudo systemctl status profit-telegram
sudo journalctl -u profit-telegram -f
sudo systemctl restart profit-telegram
```

### Ollama not working
```bash
sudo systemctl status ollama
sudo systemctl restart ollama
curl http://localhost:11434/api/version
```

### Can't SSH
- Check Oracle Console → Security Lists
- Ensure port 22 (SSH) is allowed
- Verify key: `chmod 600 ~/.ssh/oracle-key.pem`

## Files Structure

```
oracle-deploy/
├── scripts/
│   └── install.sh          # Main install script
├── systemd/
│   ├── profit-telegram.service
│   ├── profit-soul.service
│   ├── profit-commander.service
│   └── profit-builder.service
├── config/
│   └── (future configs)
└── docs/
    └── (future docs)
```

## Phone Cleanup (After Deploy)

Stop local processes and free resources:
```bash
pkill -f ollama
pkill -f telegram_bot
pkill -f live-soul
rm -rf ~/.ollama/models
apt clean
```

Frees ~500MB storage, ~2.5GB RAM.

---

**Created:** March 22, 2026
**Version:** 1.0.0
**Status:** Production Ready
