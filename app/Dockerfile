# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.9-slim AS builder
WORKDIR /app
COPY . /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

FROM gcr.io/distroless/python3:debug
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /app /app
WORKDIR /app
ENV PYTHONPATH=/usr/local/lib/python3.9/site-packages

ENTRYPOINT [ "/usr/bin/python3" ]
CMD ["app.py"]
