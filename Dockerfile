FROM python:3.9-slim-buster

RUN pip install streamlit

COPY . /app

WORKDIR /app

CMD ["streamlit", "run", "UI_ConfigCraft.py"]