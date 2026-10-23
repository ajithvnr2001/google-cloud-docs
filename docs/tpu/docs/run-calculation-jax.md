---
url: https://docs.cloud.google.com/tpu/docs/run-calculation-jax/
title: Run a calculation on a Cloud TPU VM using JAX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:39.890985+00:00
---

# Run a calculation on a Cloud TPU VM using JAX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/run-calculation-jax/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Run a calculation on a Cloud TPU VM using JAX

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

This document provides a brief introduction to working with JAX and Cloud TPU.

**Note:** This example shows how to run code on a v5litepod-8 (v5e) TPU which is a single-host TPU. Single-host TPUs have only 1 TPU VM. To run code on TPUs with more than one TPU VM (for example, v5litepod-16 or larger), see [Run JAX code on Cloud TPU slices](https://docs.cloud.google.com/tpu/docs/jax-pods).

## Before you begin

Before running the commands in this document, you must create a Google Cloud account, install the Google Cloud CLI, and configure the `gcloud` command. For more information, see [Set up the Cloud TPU environment](https://docs.cloud.google.com/tpu/docs/setup-gcp-account).

### Required roles

To get the permissions that you need to create a TPU and connect to it using SSH, ask your administrator to grant you the following IAM roles on your project: 

  * [TPU Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#tpu.admin) (`roles/tpu.admin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Cloud TPU VM using `gcloud`

  1. Define some environment variables to make commands easier to use.
         
         export PROJECT_ID=your-project-id
         export TPU_NAME=your-tpu-name
         export ZONE=us-east5-a
         export ACCELERATOR_TYPE=v5litepod-8
         export RUNTIME_VERSION=v2-alpha-tpuv5-lite

#### Environment variable descriptions

     * `PROJECT_ID`: Your Google Cloud project ID. Use an existing project or [create a new one.](https://docs.cloud.google.com/tpu/docs/setup-gcp-account#set-up-project)
     * `TPU_NAME`: The name of the TPU.
     * `ZONE`: The zone in which to create the TPU VM. For more information about supported zones, see [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones). 
     * `ACCELERATOR_TYPE`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions). 
     * `RUNTIME_VERSION`: The Cloud TPU [software version](https://docs.cloud.google.com/tpu/docs/runtimes).
  2. Create your TPU VM by running the following command from a Cloud Shell or your computer terminal where the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) is installed.
         
         $ gcloud compute tpus tpu-vm create $TPU_NAME \
             --project=$PROJECT_ID \
             --zone=$ZONE \
             --accelerator-type=$ACCELERATOR_TYPE \
             --version=$RUNTIME_VERSION




## Connect to your Cloud TPU VM

Connect to your TPU VM over SSH by using the following command:
    
    
    $ gcloud compute tpus tpu-vm ssh $TPU_NAME \
        --project=$PROJECT_ID \
        --zone=$ZONE

If you fail to connect to a TPU VM using SSH, it might be because the TPU VM doesn't have an external IP address. To access a TPU VM without an external IP address, follow the instructions in [Connect to a TPU VM without a public IP address](https://docs.cloud.google.com/tpu/docs/tpu-iap).

## Install JAX on your Cloud TPU VM
    
    
    (vm)$ pip install jax[tpu] -f https://storage.googleapis.com/jax-releases/libtpu_releases.html

## System check

Verify that JAX can access the TPU and can run basic operations:

  1. Start the Python 3 interpreter:
         
         (vm)$ python3
         
         >>> import jax

  2. Display the number of TPU cores available:
         
         >>> jax.device_count()




The number of TPU cores is displayed. The number of cores displayed is dependent on the TPU version you are using. For more information, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).

### Perform a calculation
    
    
    >>> jax.numpy.add(1, 1)

The result of the numpy add is displayed:

Output from the command: 
    
    
    Array(2, dtype=int32, weak_type=True)

### Exit the Python interpreter
    
    
    >>> exit()

## Running JAX code on a TPU VM

You can now run any JAX code you want. The [Flax examples](https://github.com/google/flax/tree/master/examples) are a great place to start with running standard ML models in JAX. For example, to train a basic MNIST convolutional network:

  1. Install Flax examples dependencies:
         
         (vm)$ pip install --upgrade clu
         (vm)$ pip install tensorflow
         (vm)$ pip install tensorflow_datasets
         (vm)$ pip install tensorboard

  2. Install Flax:
         
         (vm)$ git clone https://github.com/google/flax.git
         (vm)$ pip install --user flax

  3. Run the Flax MNIST training script:
         
         (vm)$ cd flax/examples/mnist
         (vm)$ python3 main.py --workdir=/tmp/mnist \
             --config=configs/default.py \
             --config.learning_rate=0.05 \
             --config.num_epochs=5




The script downloads the dataset and starts training. The script output should look like this:
    
    
    I0214 18:00:50.660087 140369022753856 train.py:146] epoch:  1, train_loss: 0.2421, train_accuracy: 92.97, test_loss: 0.0615, test_accuracy: 97.88
    I0214 18:00:52.015867 140369022753856 train.py:146] epoch:  2, train_loss: 0.0594, train_accuracy: 98.16, test_loss: 0.0412, test_accuracy: 98.72
    I0214 18:00:53.377511 140369022753856 train.py:146] epoch:  3, train_loss: 0.0418, train_accuracy: 98.72, test_loss: 0.0296, test_accuracy: 99.04
    I0214 18:00:54.727168 140369022753856 train.py:146] epoch:  4, train_loss: 0.0305, train_accuracy: 99.06, test_loss: 0.0257, test_accuracy: 99.15
    I0214 18:00:56.082807 140369022753856 train.py:146] epoch:  5, train_loss: 0.0252, train_accuracy: 99.20, test_loss: 0.0263, test_accuracy: 99.18

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

When you are done with your TPU VM, follow these steps to clean up your resources.

  1. Disconnect from the Cloud TPU instance, if you have not already done so:
         
         (vm)$ exit

Your prompt should now be username@projectname, showing you are in the Cloud Shell.

  2. Delete your Cloud TPU:
         
         $ gcloud compute tpus tpu-vm delete $TPU_NAME \
             --project=$PROJECT_ID \
             --zone=$ZONE

  3. Verify the resources have been deleted by running the following command. Make sure your TPU is no longer listed. The deletion might take several minutes.
         
         $ gcloud compute tpus tpu-vm list \
             --zone=$ZONE




## Performance notes

Here are a few important details that are particularly relevant to using TPUs in JAX.

### Padding

One of the most common causes for slow performance on TPUs is introducing inadvertent padding:

  * Arrays in the Cloud TPU are tiled. This entails padding one of the dimensions to a multiple of 8, and a different dimension to a multiple of 128\. 
  * The matrix multiplication unit performs best with pairs of large matrices that minimize the need for padding.



### bfloat16 dtype

By default, matrix multiplication in JAX on TPUs uses [bfloat16](https://docs.cloud.google.com/tpu/docs/bfloat16) with float32 accumulation. This can be controlled with the precision argument on relevant `jax.numpy` function calls (matmul, dot, einsum, etc). In particular:

  * `precision=jax.lax.Precision.DEFAULT`: uses mixed bfloat16 precision (fastest)
  * `precision=jax.lax.Precision.HIGH`: uses multiple MXU passes to achieve higher precision
  * `precision=jax.lax.Precision.HIGHEST`: uses even more MXU passes to achieve full float32 precision



JAX also adds the bfloat16 dtype, which you can use to explicitly cast arrays to `bfloat16`. For example, `jax.numpy.array(x, dtype=jax.numpy.bfloat16)`.

## What's next

For more information about Cloud TPU, see:

  * [Run JAX code on TPU slices](https://docs.cloud.google.com/tpu/docs/jax-pods)
  * [Manage TPUs](https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm)
  * [Cloud TPU System architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
