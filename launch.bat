@echo off
echo Activating virtual environment...
cd /d %~dp0
call sentiment_pipeline\venv\Scripts\activate
echo Launching Streamlit app...
streamlit run app.py
pause