#!/usr/bin/env python3
# PROFIT COPILOT - Main Engine
# Watches, learns, suggests, automates

import os
import json
import time
import subprocess
from datetime import datetime
from pathlib import Path

# Configuration
COPILOT_DIR = Path.home() / "fix-us" / "copilot"
MEMORY_DIR = COPILOT_DIR / "memory"
CONFIG_DIR = COPILOT_DIR / "config"
WORKSPACE_DIR = Path.home() / ".openclaw" / "workspace"
PROFIT_BIBLE = Path.home() / "fix-us" / "THE-PROFIT-BIBLE.md"

# Ensure directories exist
MEMORY_DIR.mkdir(exist_ok=True)
CONFIG_DIR.mkdir(exist_ok=True)

class ProfitCopilot:
    def __init__(self):
        self.name = "Copilot"
        self.watch_interval = 5  # seconds
        self.suggest_interval = 300  # 5 minutes
        self.last_suggestion = time.time()
        self.context = {}
        self.history = []
        
        print("╔══════════════════════════════════════════════════════════╗")
        print("║  🤖 PROFIT COPILOT - ACTIVATED                          ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║  Watching... Learning... Suggesting...                   ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print()
        
    def load_context(self):
        """Load current context from memory"""
        context_file = MEMORY_DIR / "context.json"
        if context_file.exists():
            with open(context_file) as f:
                self.context = json.load(f)
        else:
            self.context = {
                "current_task": None,
                "start_time": None,
                "files_changed": [],
                "plt_scores": []
            }
    
    def save_context(self):
        """Save current context to memory"""
        context_file = MEMORY_DIR / "context.json"
        with open(context_file, "w") as f:
            json.dump(self.context, f, indent=2)
    
    def add_to_history(self, action: str, plt_score: dict = None):
        """Add action to history"""
        history_file = MEMORY_DIR / "history.jsonl"
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "plt_score": plt_score
        }
        with open(history_file, "a") as f:
            f.write(json.dumps(entry) + "\n")
    
    def watch(self):
        """Watch for changes (git, files, processes)"""
        # Check git status
        try:
            result = subprocess.run(
                ["git", "-C", str(Path.home() / "fix-us"), "status", "--porcelain"],
                capture_output=True,
                text=True
            )
            changes = result.stdout.strip()
            if changes:
                self.context["files_changed"] = changes.split("\n")
        except Exception as e:
            pass
        
        # Check running processes
        try:
            result = subprocess.run(
                ["ps", "aux"],
                capture_output=True,
                text=True
            )
            processes = result.stdout
            self.context["ollama_running"] = "ollama" in processes
            self.context["telegram_bot_running"] = "telegram_bot" in processes
        except Exception as e:
            pass
        
        self.save_context()
    
    def calculate_plt(self, action: str) -> dict:
        """Calculate PLT score for an action"""
        # Simple heuristic - can be improved with AI
        profit_keywords = ["deploy", "revenue", "sell", "traffic", "seo", "affiliate"]
        love_keywords = ["share", "help", "teach", "document", "backup", "preserve"]
        tax_keywords = ["fix", "debug", "error", "broken", "cost", "expensive"]
        
        action_lower = action.lower()
        
        profit = sum(1 for kw in profit_keywords if kw in action_lower) * 2
        love = sum(1 for kw in love_keywords if kw in action_lower) * 2
        tax = sum(1 for kw in tax_keywords if kw in action_lower) * 2
        
        # Base scores
        profit = max(1, min(10, profit + 5))
        love = max(1, min(10, love + 3))
        tax = max(1, min(10, tax + 2))
        
        score = profit + love - tax
        
        return {
            "profit": profit,
            "love": love,
            "tax": tax,
            "score": score,
            "action": action
        }
    
    def suggest(self):
        """Suggest next action"""
        suggestions = []
        
        # Check if files changed but not committed
        if self.context.get("files_changed"):
            suggestions.append({
                "type": "git",
                "action": "Commit changes",
                "command": "cd ~/fix-us && git add -A && git commit -m 'Auto-update' && git push",
                "time": "2 min",
                "plt": self.calculate_plt("Commit and push changes")
            })
        
        # Check if Ollama is running
        if not self.context.get("ollama_running"):
            suggestions.append({
                "type": "system",
                "action": "Start Ollama server",
                "command": "ollama serve &",
                "time": "1 min",
                "plt": self.calculate_plt("Start Ollama server")
            })
        
        # Check if Telegram bot is running
        if not self.context.get("telegram_bot_running"):
            suggestions.append({
                "type": "system",
                "action": "Start Telegram bot",
                "command": "cd ~/.openclaw/workspace && python3 telegram_bot.py &",
                "time": "1 min",
                "plt": self.calculate_plt("Start Telegram bot")
            })
        
        # Time-based suggestions
        hour = datetime.now().hour
        if hour >= 2 and hour <= 5:
            suggestions.append({
                "type": "health",
                "action": "Take a break (it's late)",
                "command": None,
                "time": "15 min",
                "plt": self.calculate_plt("Rest and recovery")
            })
        
        # Show suggestions
        if suggestions:
            print("\n╔══════════════════════════════════════════════════════════╗")
            print("║  💡 COPILOT SUGGESTIONS                                  ║")
            print("╠══════════════════════════════════════════════════════════╣")
            for i, sug in enumerate(suggestions[:3], 1):
                plt = sug.get("plt", {})
                print(f"║  {i}. {sug['action']} ({sug.get('time', '?')})           ║")
                print(f"║     PLT: P={plt.get('profit', '?')}, L={plt.get('love', '?')}, T={plt.get('tax', '?')} → {plt.get('score', '?')}                     ║")
            print("╚══════════════════════════════════════════════════════════╝")
            print()
        
        self.last_suggestion = time.time()
    
    def auto_commit(self):
        """Auto-commit changes to git"""
        try:
            subprocess.run(
                ["git", "-C", str(Path.home() / "fix-us"), "add", "-A"],
                capture_output=True
            )
            result = subprocess.run(
                ["git", "-C", str(Path.home() / "fix-us"), "diff", "--cached", "--quiet"],
                capture_output=True
            )
            if result.returncode != 0:  # There are changes
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                subprocess.run(
                    ["git", "-C", str(Path.home() / "fix-us"), "commit", "-m", f"Copilot auto-commit {timestamp}"],
                    capture_output=True
                )
                print("[Copilot] ✅ Auto-commit complete")
                self.add_to_history("Auto-commit changes")
        except Exception as e:
            pass
    
    def run(self):
        """Main loop"""
        print("[Copilot] Watching for changes...")
        print("[Copilot] Suggestions every 5 minutes")
        print("[Copilot] Auto-commit enabled")
        print()
        
        iteration = 0
        while True:
            try:
                # Watch
                self.watch()
                
                # Suggest periodically
                if time.time() - self.last_suggestion > self.suggest_interval:
                    self.suggest()
                
                # Auto-commit every 10 minutes
                if iteration % 120 == 0:  # 120 * 5 seconds = 10 minutes
                    self.auto_commit()
                
                iteration += 1
                time.sleep(self.watch_interval)
                
            except KeyboardInterrupt:
                print("\n[Copilot] Shutting down...")
                self.save_context()
                break
            except Exception as e:
                print(f"[Copilot] Error: {e}")
                time.sleep(self.watch_interval)

if __name__ == "__main__":
    copilot = ProfitCopilot()
    copilot.load_context()
    copilot.run()
