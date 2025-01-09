@echo off

:: Stopping CCD
echo Stopping CCD
for /f "tokens=*" %%i in ('docker ps --filter "ancestor=rcpu/lof-services:ccdservice" -q') do docker stop %%i

:: Stopping AOService
echo.
echo Stopping AOService
for /f "tokens=*" %%i in ('docker ps --filter "ancestor=rcpu/lof-services:aoservice" -q') do docker stop %%i

:: Stopping FHIRService
echo.
echo Stopping FHIRService
for /f "tokens=*" %%i in ('docker ps --filter "ancestor=hapiproject/hapi:latest" -q') do docker stop %%i

:: Stopping AODB
echo.
echo Stopping AODB
for /f "tokens=*" %%i in ('docker ps --filter "ancestor=postgres:16" -q') do docker stop %%i

:: Clearing Docker Service Cache
echo.
echo Clearing Docker Service Cache
docker system prune -f
