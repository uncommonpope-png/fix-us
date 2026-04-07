#!/bin/bash
# NEO-KEMET CONTINUOUS EXPANSION DAEMON
# Runs in background, expands code every 30 minutes

LOG_FILE="$HOME/fix-us/neo-kemet/expansion.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

log "🚀 Starting Neo-Kemet Expansion Daemon..."

while true; do
    log "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    log "🔄 Expansion cycle starting..."
    
    # Run expansion script
    bash "$HOME/fix-us/neo-kemet/auto-expand.sh" 2>> "$LOG_FILE"
    
    log "⏳ Sleeping for 30 minutes..."
    sleep 1800
done
