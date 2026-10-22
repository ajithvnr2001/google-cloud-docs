---
url: https://docs.cloud.google.com/tpu/docs/run-in-container/
title: Run TPU workloads in a Docker container \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:57:28.971522+00:00
---

# Run TPU workloads in a Docker container  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/run-in-container/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Run TPU workloads in a Docker container

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

[Docker containers](https://www.docker.com/resources/what-container/) make configuring applications easier by combining your code and all needed dependencies in one distributable package. You can run Docker containers within TPU VMs to simplify configuring and sharing your Cloud TPU applications. This document describes how to set up a Docker container for each ML framework supported by Cloud TPU.

**Important:** You can run a maximum of 256 Docker pods on a TPU VM.

## Train a PyTorch model in a Docker container

[PyTorch on Cloud TPU](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu) describes the PyTorch libraries for TPU and links to documentation for getting the Python packages and Docker images. You can use [TorchTPU](https://torchtpu.readthedocs.io/en/latest/) directly (see [Get started on GKE](https://torchtpu.readthedocs.io/en/latest/get_started_on_gke/) for the public release container image) or use the [TorchTitan](https://github.com/google-pytorch/torchtitan) reference library to build and run containerized training workloads.

## Train a JAX model in a Docker container

Before running the following commands, create the following environment variables:
    
    
    export PROJECT_ID=your-project-id
    export TPU_NAME=your-tpu-name
    export ZONE=us-west4-a
    export ACCELERATOR_TYPE=v5litepod-8
    export RUNTIME_VERSION=v2-alpha-tpuv5-lite

#### Environment variable descriptions

  * `PROJECT_ID`: Your Google Cloud project ID. Use an existing project or [create a new one.](https://docs.cloud.google.com/tpu/docs/setup-gcp-account#set-up-project)
  * `TPU_NAME`: The name of the TPU.
  * `ZONE`: The zone in which to create the TPU VM. For more information about supported zones, see [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones). 
  * `ACCELERATOR_TYPE`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions). 
  * `RUNTIME_VERSION`: The Cloud TPU [software version](https://docs.cloud.google.com/tpu/docs/runtimes).



### TPU device

  1. Create the TPU VM
         
         gcloud compute tpus tpu-vm create $TPU_NAME \
         --zone=$ZONE \
         --accelerator-type=$ACCELERATOR_TYPE \
         --version=$RUNTIME_VERSION
         

  2. Connect to the TPU VM using SSH
         
         gcloud compute tpus tpu-vm ssh $TPU_NAME --zone=$ZONE
         

  3. Start Docker daemon in TPU VM
         
         sudo systemctl start docker
         

  4. Start Docker container
         
         sudo docker run --net=host -ti --rm --name your-container-name \
         --privileged us-central1-docker.pkg.dev/tpu-pytorch-releases/docker/xla:r2.6.0_3.10_tpuvm_cxx11 \
         bash
         

  5. Install JAX
         
         pip install jax[tpu]
         

  6. Install FLAX
         
         pip install --upgrade clu
         git clone https://github.com/google/flax.git
         pip install --user -e flax
         

  7. Install `tensorflow` and `tensorflow-datasets` packages
         
         pip install tensorflow
         pip install tensorflow-datasets
         

  8. Run the FLAX MNIST training script
         
         cd flax/examples/mnist
         python3 main.py --workdir=/tmp/mnist \
         --config=configs/default.py \
         --config.learning_rate=0.05 \
         --config.num_epochs=5
         




When the training script completes, clean up the resources.

  1. Type `exit` to exit from the Docker container
  2. Type `exit` to exit from the TPU VM
  3. Delete the TPU VM
         
         gcloud compute tpus tpu-vm delete $TPU_NAME --zone=$ZONE
         




### TPU slice

When you run JAX code on a TPU slice, you must run your JAX code on all TPU workers at the same time. One way to do this is to use the `gcloud compute tpus tpu-vm ssh` command with the `--worker=all` and `--command` flags. The following procedure shows you how to create a Docker image to make setting up each TPU worker easier.

  1. Create a file named `Dockerfile` in your current directory and paste the following text
         
         FROM python:3.10
         RUN pip install jax[tpu]
         RUN pip install --upgrade clu
         RUN git clone https://github.com/google/flax.git
         RUN pip install --user -e flax
         RUN pip install tensorflow
         RUN pip install tensorflow-datasets
         WORKDIR ./flax/examples/mnist
         

  2. Prepare an Artifact Registry
         
         gcloud artifacts repositories create your-repo \
         --repository-format=docker \
         --location=europe-west4 --description="Docker repository" \
         --project=$PROJECT_ID
         
         gcloud artifacts repositories list \
         --project=$PROJECT_ID
         
         gcloud auth configure-docker europe-west4-docker.pkg.dev
         

  3. Build the Docker image
         
         docker build -t your-image-name .
         

  4. Add a tag to your Docker image before pushing it to the Artifact Registry. For more information on working with Artifact Registry, see [Work with container images](https://docs.cloud.google.com/artifact-registry/docs/docker).
         
         docker tag your-image-name europe-west4-docker.pkg.dev/$PROJECT_ID/your-repo/your-image-name:your-tag
         

  5. Push your Docker image to the Artifact Registry
         
         docker push europe-west4-docker.pkg.dev/$PROJECT_ID/your-repo/your-image-name:your-tag
         

  6. Create a TPU VM
         
         gcloud compute tpus tpu-vm create $TPU_NAME \
         --zone=$ZONE \
         --accelerator-type=$ACCELERATOR_TYPE \
         --version=$RUNTIME_VERSION
         

  7. Pull the Docker image from the Artifact Registry on all TPU workers
         
         gcloud compute tpus tpu-vm ssh $TPU_NAME --worker=all \
         --zone=$ZONE \
         --command='sudo usermod -a -G docker ${USER}'
         
         
         gcloud compute tpus tpu-vm ssh $TPU_NAME --worker=all \
         --zone=$ZONE \
         --command="gcloud auth configure-docker europe-west4-docker.pkg.dev --quiet"
         
         
         gcloud compute tpus tpu-vm ssh $TPU_NAME --worker=all \
         --zone=$ZONE \
         --command="docker pull europe-west4-docker.pkg.dev/$PROJECT_ID/your-repo/your-image-name:your-tag"
         

  8. Run the container on all TPU workers
         
         gcloud compute tpus tpu-vm ssh $TPU_NAME --worker=all \
         --zone=$ZONE \
         --command="docker run -ti -d --privileged --net=host --name your-container-name europe-west4-docker.pkg.dev/$PROJECT_ID/your-repo/your-image-name:your-tag bash"
         

  9. Run the training script on all TPU workers
         
         gcloud compute tpus tpu-vm ssh $TPU_NAME --worker=all \
         --zone=$ZONE \
         --command="docker exec --privileged your-container-name python3 main.py --workdir=/tmp/mnist \
         --config=configs/default.py \
         --config.learning_rate=0.05 \
         --config.num_epochs=5"
         




When the training script completes, clean up the resources.

  1. Shut down the container on all workers
         
         gcloud compute tpus tpu-vm ssh $TPU_NAME --worker=all \
         --zone=$ZONE \
         --command="docker kill your-container-name"
         

  2. Delete the TPU VM
         
         gcloud compute tpus tpu-vm delete $TPU_NAME \
         --zone=$ZONE
         




## What's next

  * [Cloud TPU tutorials](https://docs.cloud.google.com/tpu/docs/tutorials)
  * [Manage TPUs](https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm)
  * [Cloud TPU architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm)
  * [Run JAX code on TPU slices](https://docs.cloud.google.com/tpu/docs/jax-pods)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
