@echo off
echo Starting YouTube Converter...
start "" "http://127.0.0.1:5000"
py "%~dp0app.py"
pause
