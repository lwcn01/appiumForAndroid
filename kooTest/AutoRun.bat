@echo off&title Appium

cls

color 06
@ ECHO.
@ ECHO.   ===============Appium==============
@ ECHO.

start cmd /k "appium --no-reset --log %~dp0Result\appium.log&&echo.&pause

start cmd /k "@ping -n 5 127.1 >nul 2>nul>nul&& python %~dp0Runner.py&&echo.&pause
