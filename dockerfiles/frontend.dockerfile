FROM python:3.13-slim

# everything in backend folder goes into /app folder, which is created if it didn't exist before
COPY frontend/ /app/

# install uv
RUN pip install --no-cache-dir uv

# changes working directory to /app
WORKDIR /app

# installs all dependencies specified in pyproject.toml without dev packages
RUN uv sync --no-dev

# change working directory to where we have api.py
WORKDIR /app/src/frontend

# 0.0.0.0 -> accept connections from local machine and external
CMD ["uv" , "run", "streamlit", "run", "dashboard.py", "--server.address", "0.0.0.0"]