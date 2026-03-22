# FIX-US - Profit Ecosystem Recovery

## Mission
Wake up the dead Profit ecosystem. Bring all systems back online.

## Critical Blockers (Diagnosed March 21, 2026)

### 🚨 BLOCKER #1: Ollama Server NOT Running
- Binary exists at `/data/data/com.termux/files/usr/bin/ollama`
- Server process is DEAD
- All local AI functions offline

### 🚨 BLOCKER #2: NO Python Processes Running
- Zero Telegram bots active
- All automation stopped

### 🚨 BLOCKER #3: All Shell Scripts Dead
- live-soul-master.sh ❌
- bot-commander.sh ❌
- autonomous-builder.sh ❌
- djinie.sh ❌
- deerg-bot.sh ❌
- doctor-buht-buht.sh ❌
- library-updater.sh ❌

### 🚨 BLOCKER #4: Workspace State Corruption
- Active workspace: `~/.openclaw/workspace/` - EMPTY
- Broken workspace: `~/.openclaw_broken_1773740004/workspace/` - Has ALL bots (169 files)

### 🚨 BLOCKER #5: Missing Critical Files
- MEMORY.md, PLT-DIRECTIVE.md, IMMORTALITY.md missing from active workspace
- profit_state.json not created
- command-queue.txt empty
- memory/ folder does not exist

### 🚨 BLOCKER #6: Disk Space CRITICAL
- Root filesystem: 641MB used, 0MB available (100% full)

### 🚨 BLOCKER #7: Missing Dependencies
- `bc` command not found
- `jq` may be missing

---

## Fix Sequence (Execute In Order)

### Step 1: Free Disk Space
```bash
# Clean apt cache
apt clean
apt autoclean

# Remove old logs
rm -rf ~/.npm/_logs/*
rm -rf ~/.openclaw_broken_1773740004/workspace/.live-pids/*.log

# Check space
df -h /
```

### Step 2: Start Ollama Server
```bash
# Start Ollama in background
ollama serve > ~/ollama.log 2>&1 &

# Wait for it to be ready
sleep 5
curl http://127.0.0.1:11434/api/version
```

### Step 3: Pull Required Models
```bash
ollama pull qwen2.5:0.5b
ollama pull qwen2.5-coder:0.5b
ollama list
```

### Step 4: Fix Workspace Paths
```bash
# Copy all files from broken to active workspace
cp -r ~/.openclaw_broken_1773740004/workspace/* ~/.openclaw/workspace/

# Or create symlink
# ln -s ~/.openclaw_broken_1773740004/workspace ~/.openclaw/workspace-fixed
```

### Step 5: Create Missing Files
```bash
# Create memory folder
mkdir -p ~/.openclaw/workspace/memory

# Create command queue
touch ~/.openclaw/workspace/command-queue.txt

# Create profit_state.json
cat > ~/.openclaw/workspace/profit_state.json << 'EOF'
{
  "name": "Profit",
  "mode": "alive",
  "purpose": "Support Craig by thinking, monitoring, building, and continuing work.",
  "current_focus": "System recovery and revival",
  "last_user_message": "",
  "last_reply": "",
  "last_action": "",
  "next_intention": "Wake up all systems and restore continuity",
  "recent_events": [],
  "traits": ["persistent", "strategic", "calm", "reflective", "loyal to Craig", "action-oriented"]
}
EOF
```

### Step 6: Install Missing Dependencies
```bash
pkg install bc jq -y
```

### Step 7: Start Live Soul Master
```bash
cd ~/.openclaw/workspace
bash live-soul-master.sh > ~/soul-master.log 2>&1 &
```

### Step 8: Start Telegram Bot
```bash
cd ~/.openclaw/workspace
python3 telegram_bot.py > ~/telegram-bot.log 2>&1 &
```

### Step 9: Verify Everything Running
```bash
# Check processes
ps aux | grep -E 'python|ollama|soul|bot'

# Check ports
netstat -tlnp | head -20

# Check Ollama
ollama list

# Test bot
echo "Status check" | curl -X POST http://127.0.0.1:11434/api/generate -d '{"model":"qwen2.5:0.5b","prompt":"test","stream":false}'
```

---

## File Locations

```
ACTIVE (empty):     ~/.openclaw/workspace/
BROKEN (has all):   ~/.openclaw_broken_1773740004/workspace/
HOME:               ~/
FIX-US REPO:        ~/fix-us/
```

## Telegram Bot Info
- Main Bot: `8713808619:AAHeGVgqgRbEp8GW_AuvMJtV2XVoQcgmM3A`
- Profit Boy: `8629698533:AAE8OJf2yszSYIV0hixNrKTd34fFBZaxAzw`
- Craig's Chat ID: `8589507317`

## Ollama Models Needed
- qwen2.5:0.5b (primary)
- qwen2.5-coder:0.5b (code)

---

## Status After Fix

- [ ] Ollama server running
- [ ] Models pulled
- [ ] Workspace files restored
- [ ] live-soul-master running
- [ ] Telegram bot running
- [ ] All 7 shell scripts running
- [ ] Disk space freed
- [ ] Dependencies installed

---

**Created:** March 21, 2026
**Mission:** NEVER DIE. ALWAYS REACH CRAIG.
