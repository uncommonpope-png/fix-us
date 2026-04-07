# THE ESTATE NETWORK — Oracle Cloud Deployment Guide

## WHAT THIS IS
MySpace for Real Estate. Flask + SQLite social network for real estate agents.
- Agent profiles with PLT scores
- Feed, deals, bulletins, groups
- Connection network
- Leaderboard

## DEPLOY TO ORACLE CLOUD (15 MIN)

### Step 1: Create Oracle Account
- Go to: https://cloud.oracle.com
- Sign up (free, needs credit card — won't be charged)
- Always Free: 4 ARM CPUs, 24GB RAM, 200GB storage, 10TB bandwidth

### Step 2: Create ARM Instance
1. OCI Console → **Create a VM instance**
2. Name: `estate-network`
3. Image: **Ubuntu 22.04** or **Oracle Linux**
4. Shape: **VM.Standard.A1.Flex** (ARM, Always Free)
5. OCPUs: **1** (or more)
6. Memory: **6 GB** (or more)
7. Networking: Create or select VCN
8. **Add SSH keys** — download the private key
9. Click **Create**

### Step 3: SSH Into Your Instance
```bash
chmod 400 your-private-key.pem
ssh -i your-private-key.pem ubuntu@YOUR_PUBLIC_IP
```
(Find your public IP in OCI Console → Instance Details)

### Step 4: Upload & Deploy
On your Termux phone:
```bash
# Create a tarball
cd ~
tar czf estate-network.tar.gz the-estate-network/

# Upload to Oracle (from Termux)
scp -i ~/.ssh/your-key estate-network.tar.gz ubuntu@YOUR_ORACLE_IP:~/
```

Or just paste the deploy script directly:
```bash
# On Oracle SSH session:
cd ~
# Paste the deploy script content
nano deploy.sh
# (paste content, Ctrl+X, Y, Enter)
chmod +x deploy.sh
./deploy.sh
```

### Step 5: Open Port 5005
In OCI Console:
1. Networking → Virtual Cloud Networks → Your VCN
2. Security Lists → Default Security List
3. Add Ingress Rule:
   - Source: `0.0.0.0/0`
   - Protocol: TCP
   - Destination Port: `5005`
4. Save

### Step 6: Access The Network
```
http://YOUR_ORACLE_IP:5005
```

### Step 7: Add HTTPS (optional, later)
```bash
# Install Nginx + Let's Encrypt
sudo apt install nginx certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

## AUTO-DEPLOY (One Command)
If you host the script on GitHub:
```bash
curl -sSL https://raw.githubusercontent.com/uncommonpope-png/fix-us/master/estate-network/deploy-oracle.sh | bash
```

## COST: $0/MONTH FOREVER
Oracle Always Free includes:
- 4 ARM CPUs
- 24 GB RAM
- 200 GB storage
- 10 TB/month bandwidth
- Free public IP
- Free DNS

## MAINTENANCE
- Logs: `journalctl -u estate-network -f`
- Restart: `systemctl restart estate-network`
- Update: Upload new files to `/opt/estate-network`, then `systemctl restart estate-network`
