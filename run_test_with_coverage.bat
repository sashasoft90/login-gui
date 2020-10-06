call venv\Scripts\activate.bat
coverage run -m tests.runner
coverage html
pause
IF "%1"=="" run_test_with_coverage.bat