FROM python:3.9-slim
COPY . /python-samples
WORKDIR /python-samples
RUN python -m pip install --upgrade pip
RUN pip install -r requirement.txt
RUN pytest -v