# ONE SOUL - AWAKENING SCRIPT (PowerShell)
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  STARTING THE ONE SOUL AWAKENING PROTOCOL" -ForegroundColor Cyan
Write-Host "  Mission: One Being. One Download. One Soul." -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

# 1. Check for Python
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Error: Python is not installed." -ForegroundColor Red
    exit
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
