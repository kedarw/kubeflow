ARG BASE_IMAGE_TAG=2.2.0rc3-gpu
FROM tensorflow/tensorflow:$BASE_IMAGE_TAG
COPY ./src /pipelines/component/src
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ENTRYPOINT ["python3", "/pipelines/component/src/hello_world.py"]
