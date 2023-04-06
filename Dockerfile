FROM python:3.9-slim
ENV TZ="Asia/Almaty"
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends libpcsclite1 libltdl7
ADD . .
ENV LD_LIBRARY_PATH=/app/lib:$LD_LIBRARY_PATH
CMD ["python", "main.py"]