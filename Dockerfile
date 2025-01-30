FROM python:3.12.8-alpine3.21@sha256:ba13ef990f6e5d13014e9e8d04c02a8fdb0fe53d6dccf6e19147f316e6cc3a84

LABEL description="Fat Secret Platform" maintainer="s.asekrea@innopolis.university"

# prevents Python from writing compiled Python files to the disk --> reduces image size
ENV PYTHONDONTWRITEBYTECODE=1

# logs and output are shown in real-time on terminal --> easier to debug
ENV PYTHONUNBUFFERED=1



# Create a non-root user
RUN addgroup -S app_group && adduser -S app_user -G app_group

WORKDIR /fatsecret_platform

COPY requirements.txt /fatsecret_platform/requirements.txt

RUN pip install --no-cache-dir --upgrade pip==25.0 \
    && pip install --no-cache-dir --upgrade -r /fatsecret_platform/requirements.txt

COPY . /fatsecret_platform

RUN chown -R app_user:app_group /fatsecret_platform/

# Switch to the non-root user
USER app_user

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]


