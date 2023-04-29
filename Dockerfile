FROM python:3.8-slim

ENV PYTHONFAULTHANDLER=1 \
     PYTHONUNBUFFERED=1 \
     PYTHONDONTWRITEBYTECODE=1 \
     PIP_DISABLE_PIP_VERSION_CHECK=on \
     TELEGRAM_BOT_TOKEN="" \
     TELEGRAM_USER_IDS="" \
     CLAUDE_SECRET_KEY="" \
     BARD_SECRET_KEY=""

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt --no-cache-dir

CMD ["python", "bot.py"]
