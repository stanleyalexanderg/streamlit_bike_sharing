## Setup Environment - Anaconda
conda create --name bike_analysis_env python=3.9
conda activate bike_analysis_env
pip install -r requirements.txt

## Setup Environment - Shell/Terminal (Without Anaconda)
mkdir bike_analysis_project
cd bike_analysis_project
pipenv install
pipenv shell
pip install -r requirements.txt

## Run Streamlit App
streamlit run Dashboard/dashboard.py
