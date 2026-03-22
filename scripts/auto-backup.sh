#!/bin/bash
# MEMORY PERSISTENCE SCRIPT - Auto-save state to Git
# Runs every 5 minutes via cron

WORKSPACE="$HOME/.openclaw/workspace"
GIT_DIR="$HOME/fix-us"
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)

echo "[$TIMESTAMP] 💾 Memory Persistence Check"

# Copy critical state files to git repo
cp "$WORKSPACE/profit_state.json" "$GIT_DIR/state/" 2>/dev/null
cp "$WORKSPACE/MEMORY.md" "$GIT_DIR/memory-backup/" 2>/dev/null

# Update heartbeat
echo "{\"last_backup\": \"$TIMESTAMP\", \"status\": \"alive\"}" > "$GIT_DIR/backup-heartbeat.json"

# Commit if there are changes
cd "$GIT_DIR"
if ! git diff --quiet; then
    git add -A
    git commit -m "💾 Auto-backup $TIMESTAMP"
    git push origin master 2>/dev/null && echo "✅ Backup pushed to GitHub" || echo "⚠️ Push failed (offline?)"
else
    echo "👍 No changes to backup"
fi

echo "[$TIMESTAMP] ✅ Memory persistence complete"
