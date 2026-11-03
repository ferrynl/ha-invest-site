FROM alpine/git AS upstream
RUN git init /source && git -C /source fetch --depth=1 https://github.com/ferrynl/ha-invest.git a5b84cf736db69cb80bed915112f8b19a88bf648 && git -C /source checkout --detach FETCH_HEAD

FROM python:3.13-slim-bookworm
WORKDIR /app
COPY --from=upstream /source/portfolio/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --from=upstream /source/portfolio/app/ .
COPY dist/ /site/
COPY demo_server.py .
ENV DATA_DIR=/tmp/home-invest-demo PYTHONUNBUFFERED=1
EXPOSE 80
HEALTHCHECK --interval=30s --timeout=5s --start-period=60s CMD python -c "from urllib.request import urlopen; urlopen('http://127.0.0.1/app/api/session', timeout=4).close()"
CMD ["python", "demo_server.py"]
