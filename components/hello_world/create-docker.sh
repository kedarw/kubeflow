#!/bin/bash -e
image_name=gcr.io/citric-snow-274005/hello_world
image_tag=latest

full_image_name=${image_name}:${image_tag}
base_image_tag=2.2.0rc3-gpu

cd "$(dirname "$0")"

docker build --build-arg BASE_IMAGE_TAG=${base_image_tag} -t "${full_image_name}" .
docker push "$full_image_name"
