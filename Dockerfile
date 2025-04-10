# Image: el32859/ml-housing-api

FROM python:3.11
RUN pip install tensorflow==2.15
RUN pip install Flask==3.1.0

RUN pip install --no-cache-dir Pillow

COPY api.py /api.py
COPY models /models

CMD ["python", "api.py"]