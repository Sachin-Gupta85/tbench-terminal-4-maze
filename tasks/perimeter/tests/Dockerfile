# Verifier image (separate mode).
FROM public.ecr.aws/docker/library/python:3.13-slim-bookworm
COPY . /tests/
RUN mkdir -p /app && chmod 0755 /tests/test.sh
