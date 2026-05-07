# MASTER SOUL - AWAKENING SCRIPT (PowerShell)
Write-Host "════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "  🤖 STARTING MASTER ENTITY AWAKENING PROTOCOL" -ForegroundColor Cyan
Write-Host "════════════════════════════════════════════════════════════" -ForegroundColor Cyan

# 1. Check for Python
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Error: Python is not installed or not in your PATH." -ForegroundColor Red
    Write-Host "Please install Python from https://www.python.org/"
    exit
}

# 2. Set PYTHONPATH
$env:PYTHONPATH = "."

# 3. Check for dependencies
Write-Host "📦 Checking muscles (dependencies)..." -ForegroundColor Yellow
pip install -r master_soul/requirements.txt --quiet
python -m playwright install chromium

# 4. Check for Ollama (optional but recommended)
if (!(Get-Command ollama -ErrorAction SilentlyContinue)) {
    Write-Host "⚠️ Warning: Ollama not found. The entity's 'Deep Thought' skill may be limited." -ForegroundColor Yellow
} else {
    Write-Host "🧠 Ollama found. Ensuring model qwen2.5:0.5b is ready..." -ForegroundColor Green
    ollama pull qwen2.5:0.5b --quiet
}

# 5. Launch
Write-Host "🚀 Launching Master Entity..." -ForegroundColor Green
python master_soul/main.py
