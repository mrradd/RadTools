:: Outputs a file appended with the curernt date and time.

@echo off
for /f "delims=" %%a in ('powershell -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd'"') do set "mydate=%%a"

:: Extract hours and minutes
set Hour=%TIME:~0,2%
set Minute=%TIME:~3,2%

:: Fix leading space if the hour is a single digit (e.g., " 9:30")
if "%Hour:~0,1%"==" " set Hour=0%Hour:~1,1%

cd code_combiner
python code_combiner_tool.py C:\path\to\code\directory -o combined_code_%mydate%_%Hour%_%Minute%.txt