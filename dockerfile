FROM python:3.9

WORKDIR /app

COPY jogo_da_velha.py .

CMD ["python", "jogo_da_velha.py"]