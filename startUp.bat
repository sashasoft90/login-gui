@echo off
@echo startUp script was started.

:: search pip in PATH
for %%i in (pip.exe) do set my_pip=%%~$PATH:i
if /i "%my_pip%" NEQ "" goto EXIST_PIP
echo pip was not found
echo Please add python\Script to system path

goto:END

:EXIST_PIP
echo pip was found %my_pip%

if EXIST venv goto INSTALL_REQ
@echo create venv with virtualenv
py -3.10-64 -m pip install --upgrade pip
py -3.10-64 -m pip install virtualenv
call py -3.10-64 -m venv venv

:INSTALL_REQ
echo activate venv
call venv\Scripts\activate
echo update venv
pip install -r dev_requirements.txt
pip install -r requirements.txt

:END
@echo startUp is finished
pause
