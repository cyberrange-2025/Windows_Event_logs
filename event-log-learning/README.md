# 🛡️ Windows Event Log Monitoring (For Learning Use Only)

This repository is created **strictly for educational and learning purposes**, demonstrating how to collect, convert, analyze, and visualize Windows Event Logs using PowerShell, Python, and GitHub automation.

...

# Logon Sessions
Get-WinEvent -FilterHashtable @{LogName='System'; Id=6005}     # Log service started
Get-WinEvent -FilterHashtable @{LogName='System'; Id=6006}     # Log service stopped