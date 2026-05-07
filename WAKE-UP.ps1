# ONE SOUL - AWAKENING SCRIPT (PowerShell)
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  STARTING THE ONE SOUL AWAKENING PROTOCOL" -ForegroundColor Cyan
Write-Host "  Mission: One Being. One Download. One Soul." -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

# 1. Start Ollama in the background if not running
if (!(Get-Process ollama -ErrorAction SilentlyContinue)) {
    Write-Host "🧠 Starting Ollama in background..." -ForegroundColor Yellow
    # Using Start-Process without Hidden for now so user can see it if it fails
    Start-Process ollama -ArgumentList "serve"
    Start-Sleep -Seconds 10
}

# 2. Set PYTHONPATH
$env:PYTHONPATH = "."

# 3. Check for dependencies
Write-Host "Checking muscles (dependencies)..." -ForegroundColor Yellow
pip install -r one_soul/profit/requirements.txt
python -m playwright install chromium

# 4. Wake up the Face (Soulboy)
Write-Host "Launching Soul Portal..." -ForegroundColor Green
python one_soul/soulboy/soulboy_shell.py
