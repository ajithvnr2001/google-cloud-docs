---
url: https://docs.cloud.google.com/tpu/docs/v5e-training/
title: Train a model using TPU v5e \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:52.775111+00:00
---

# Train a model using TPU v5e  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/v5e-training/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Train a model using TPU v5e

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

With a smaller 256-chip footprint per Pod, TPU v5e is optimized to be a high-value product for transformer, text-to-image, and Convolutional Neural Network (CNN) training, fine-tuning, and serving. For more information about using Cloud TPU v5e for serving, see [Inference using v5e](https://docs.cloud.google.com/tpu/docs/v5e-inference).

For more information about Cloud TPU v5e TPU hardware and configurations, see [TPU v5e](https://docs.cloud.google.com/tpu/docs/v5e).

## Get started

The following sections describe how to get started using TPU v5e.

### Request quota

You need quota to use TPU v5e for training. There are different quota types for on-demand TPUs, reserved TPUs, and TPU Spot VMs. There are separate quotas required if you're using your TPU v5e for [inference](https://docs.cloud.google.com/tpu/docs/v5e-inference). For more information about quotas, see [Quotas](https://docs.cloud.google.com/tpu/docs/quota). To request TPU v5e quota, contact [Cloud Sales](https://cloud.google.com/contact).

### Create a Google Cloud account and project

You need a Google Cloud account and project to use Cloud TPU. For more information, see [Set up a Cloud TPU environment](https://docs.cloud.google.com/tpu/docs/setup-gcp-account).

### Create a Cloud TPU

The best practice is to provision Cloud TPU v5es as [queued resources](https://docs.cloud.google.com/tpu/docs/queued-resources) using the `queued-resource create` command. For more information, see [Manage queued resources](https://docs.cloud.google.com/tpu/docs/queued-resources).

You can also use the Create Node API (`gcloud compute tpus tpu-vm create`) to provision Cloud TPU v5es. For more information, see [Manage TPU resources](https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm).

For more information about available v5e configurations for training, see [Cloud TPU v5e types for training](https://docs.cloud.google.com/tpu/docs/v5e#tpu-v5e-config).

## Framework setup

This section describes the general setup process for custom model training using JAX with TPU v5e. For PyTorch training options, see Train a model using PyTorch on Cloud TPU.

For inference setup instructions, see [v5e inference introduction](https://docs.cloud.google.com/tpu/docs/v5e-inference).

Define some environment variables:
    
    
    export PROJECT_ID=your_project_ID
    export ACCELERATOR_TYPE=v5litepod-16
    export ZONE=us-west4-a
    export TPU_NAME=your_tpu_name
    export QUEUED_RESOURCE_ID=your_queued_resource_id
    

### Setup for JAX

If you have slice shapes greater than 8 chips, you will have multiple VMs in one slice. In this case, you need to use the `--worker=all` flag to run the installation on all TPU VMs in a single step without using SSH to log into each separately:
    
    
    gcloud compute tpus tpu-vm ssh $TPU_NAME  \
       --project=$PROJECT_ID \
       --zone=$ZONE \
       --worker=all \
       --command='pip install -U "jax[tpu]" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html'
    

#### Command flag descriptions

  * `TPU_NAME`: The user-assigned text ID of the TPU which is created when the queued resource request is allocated.
  * `PROJECT_ID`: Google Cloud Project Name. Use an existing project or create a new one at [ Set up your Google Cloud project](https://docs.cloud.google.com/tpu/docs/setup-gcp-account#set-up-project)
  * `ZONE`: See the [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones) document for the supported zones.
  * `worker`: The TPU VM that has access to the underlying TPUs.



You can run the following command to check the number of devices (the outputs shown here were produced with a v5litepod-16 slice). This code tests that everything is installed correctly by checking that JAX sees the Cloud TPU TensorCores and can run basic operations:
    
    
    gcloud compute tpus tpu-vm ssh $TPU_NAME \
       --project=$PROJECT_ID \
       --zone=$ZONE \
       --worker=all \
       --command='python3 -c "import jax; print(jax.device_count()); print(jax.local_device_count())"'
    

The output will be similar to the following:
    
    
    SSH: Attempting to connect to worker 0...
    SSH: Attempting to connect to worker 1...
    SSH: Attempting to connect to worker 2...
    SSH: Attempting to connect to worker 3...
    16
    4
    16
    4
    16
    4
    16
    4
    

`jax.device_count()` shows the total number of chips in the given slice. `jax.local_device_count()` indicates the count of chips accessible by a single VM in this slice.
    
    
    # Check the number of chips in the given slice by summing the count of chips
    # from all VMs through the
    # jax.local_device_count() API call.
    gcloud compute tpus tpu-vm ssh $TPU_NAME \
       --project=$PROJECT_ID \
       --zone=$ZONE \
       --worker=all \
       --command='python3 -c "import jax; xs=jax.numpy.ones(jax.local_device_count()); print(jax.pmap(lambda x: jax.lax.psum(x, \"i\"), axis_name=\"i\")(xs))"'
    

The output will be similar to the following:
    
    
    SSH: Attempting to connect to worker 0...
    SSH: Attempting to connect to worker 1...
    SSH: Attempting to connect to worker 2...
    SSH: Attempting to connect to worker 3...
    [16. 16. 16. 16.]
    [16. 16. 16. 16.]
    [16. 16. 16. 16.]
    [16. 16. 16. 16.]
    

Try the JAX Tutorials in this document to get started with v5e training using JAX.

### Clean up

Delete your TPU and queued resource at the end of your session. To delete a queued resource, delete the slice and then the queued resource in 2 steps:
    
    
    gcloud compute tpus tpu-vm delete $TPU_NAME \
       --project=$PROJECT_ID \
       --zone=$ZONE \
       --quiet
    
    gcloud compute tpus queued-resources delete $QUEUED_RESOURCE_ID \
       --project=$PROJECT_ID \
       --zone=${ZONE} \
       --quiet
    

These two steps can also be used to remove queued resource requests that are in the `FAILED` state.

## JAX/FLAX examples

The following sections describe examples of how to train JAX and FLAX models on TPU v5e.

### Train ImageNet on v5e

This tutorial describes how to train ImageNet on v5e using fake input data. If you want to use real data, refer to the [README file on GitHub](https://github.com/google/flax/blob/main/examples/imagenet/README.md).

#### Set up

  1. Create environment variables:
         
         export PROJECT_ID=your-project-id
         export TPU_NAME=your-tpu-name
         export ZONE=us-west4-a
         export ACCELERATOR_TYPE=v5litepod-8
         export RUNTIME_VERSION=v2-alpha-tpuv5-lite
         export SERVICE_ACCOUNT=your-service-account
         export QUEUED_RESOURCE_ID=your-queued-resource-id

#### Environment variable descriptions

     * `PROJECT_ID`: Your Google Cloud project ID. Use an existing project or [create a new one.](https://docs.cloud.google.com/tpu/docs/setup-gcp-account#set-up-project)
     * `TPU_NAME`: The name of the TPU.
     * `ZONE`: The zone in which to create the TPU VM. For more information about supported zones, see [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones). 
     * `ACCELERATOR_TYPE`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions). 
     * `RUNTIME_VERSION`: The Cloud TPU [software version](https://docs.cloud.google.com/tpu/docs/runtimes).
     * `SERVICE_ACCOUNT`: The email address for your service account. You can find it by going to the [Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts) in the Google Cloud console. 

For example: `tpu-service-account@PROJECT_ID.iam.gserviceaccount.com`

     * `QUEUED_RESOURCE_ID`: The user-assigned text ID of the queued resource request.
  2. [Create a TPU resource:](https://docs.cloud.google.com/tpu/docs/queued-resources)
         
         gcloud compute tpus queued-resources create $QUEUED_RESOURCE_ID \
            --node-id=$TPU_NAME \
            --project=$PROJECT_ID \
            --zone=$ZONE \
            --accelerator-type=$ACCELERATOR_TYPE \
            --runtime-version=$RUNTIME_VERSION \
            --service-account=$SERVICE_ACCOUNT
         

**Note:** To use a reservation, add the `--reserved` flag. To use TPU Spot VMs, add the `--spot` flag.

You will be able to SSH to your TPU VM once your queued resource is in the `ACTIVE` state:
         
         gcloud compute tpus queued-resources describe $QUEUED_RESOURCE_ID  \
            --project=$PROJECT_ID \
            --zone=$ZONE
         

When the QueuedResource is in the `ACTIVE` state, the output will be similar to the following:
         
         state: ACTIVE
         

  3. Install newest version of JAX and jaxlib:
         
         gcloud compute tpus tpu-vm ssh $TPU_NAME \
            --project=$PROJECT_ID \
            --zone=$ZONE \
            --worker=all \
            --command='pip install -U "jax[tpu]" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html'
         

**Note:** If you see an error suggesting you use jax>=0.4.8, you can safely ignore the message.
  4. Clone the ImageNet model and install the corresponding requirements:
         
         gcloud compute tpus tpu-vm ssh $TPU_NAME \
            --project=$PROJECT_ID \
            --zone=$ZONE \
            --worker=all \
            --command="git clone https://github.com/coolkp/flax.git && cd flax && git checkout pmap-orbax-conversion && git pull"
         

  5. To generate fake data, the model needs information on the dimensions of the dataset. This can be gathered from the ImageNet dataset's metadata:
         
         gcloud compute tpus tpu-vm ssh $TPU_NAME \
            --project=$PROJECT_ID \
            --zone=$ZONE \
            --worker=all \
            --command="cd flax/examples/imagenet && pip install -r requirements-cloud-tpu.txt"
         




#### Train the model

Once all the previous steps are done, you can train the model.
    
    
    gcloud compute tpus tpu-vm ssh $TPU_NAME \
       --project=$PROJECT_ID \
       --zone=$ZONE \
       --worker=all \
       --command="cd flax/examples/imagenet && bash ../../tests/download_dataset_metadata.sh && JAX_PLATFORMS=tpu python imagenet_fake_data_benchmark.py"
    

#### Delete the TPU and queued resource

Delete your TPU and queued resource at the end of your session.
    
    
    gcloud compute tpus tpu-vm delete $TPU_NAME \
       --project=$PROJECT_ID \
       --zone=$ZONE \
       --quiet
    
    
    
    gcloud compute tpus queued-resources delete $QUEUED_RESOURCE_ID \
       --project=$PROJECT_ID \
       --zone=$ZONE \
       --quiet
    

### Hugging Face FLAX Models

[Hugging Face](https://huggingface.co/) models implemented in FLAX work out of the box on Cloud TPU v5e. This section provides instructions for running popular models.

#### Train ViT on Imagenette

This tutorial shows you how to train the [Vision Transformer](https://arxiv.org/abs/2010.11929) (ViT) model from HuggingFace using the Fast AI [Imagenette](https://github.com/fastai/imagenette) dataset on Cloud TPU v5e.

The ViT model was the first one that successfully trained a Transformer encoder on ImageNet with excellent results compared to convolutional networks. For more information, see [ViT overview](https://huggingface.co/docs/transformers/model_doc/vit).

#### Set up

  1. Create environment variables:
         
         export PROJECT_ID=your-project-id
         export TPU_NAME=your-tpu-name
         export ZONE=us-west4-a
         export ACCELERATOR_TYPE=v5litepod-16
         export RUNTIME_VERSION=v2-alpha-tpuv5-lite
         export SERVICE_ACCOUNT=your-service-account
         export QUEUED_RESOURCE_ID=your-queued-resource-id

#### Environment variable descriptions

     * `PROJECT_ID`: Your Google Cloud project ID. Use an existing project or [create a new one.](https://docs.cloud.google.com/tpu/docs/setup-gcp-account#set-up-project)
     * `TPU_NAME`: The name of the TPU.
     * `ZONE`: The zone in which to create the TPU VM. For more information about supported zones, see [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones). 
     * `ACCELERATOR_TYPE`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions). 
     * `RUNTIME_VERSION`: The Cloud TPU [software version](https://docs.cloud.google.com/tpu/docs/runtimes).
     * `SERVICE_ACCOUNT`: The email address for your service account. You can find it by going to the [Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts) in the Google Cloud console. 

For example: `tpu-service-account@PROJECT_ID.iam.gserviceaccount.com`

     * `QUEUED_RESOURCE_ID`: The user-assigned text ID of the queued resource request.
  2. [Create a TPU resource:](https://docs.cloud.google.com/tpu/docs/queued-resources)
         
         gcloud compute tpus queued-resources create $QUEUED_RESOURCE_ID \
            --node-id=$TPU_NAME \
            --project=$PROJECT_ID \
            --zone=$ZONE \
            --accelerator-type=$ACCELERATOR_TYPE \
            --runtime-version=$RUNTIME_VERSION \
            --service-account=$SERVICE_ACCOUNT
         

**Note:** To use a reservation, add the `--reserved` flag. To use TPU Spot VMs, add the `--spot` flag.

You will be able to SSH to your TPU VM once your queued resource is in state `ACTIVE`:
         
         gcloud compute tpus queued-resources describe $QUEUED_RESOURCE_ID  \
            --project=$PROJECT_ID \
            --zone=$ZONE
         

When the queued resource is in the `ACTIVE` state, the output will be similar to the following:
         
         state: ACTIVE
         

  3. Install JAX and its library:
         
         gcloud compute tpus tpu-vm ssh $TPU_NAME \
            --project=$PROJECT_ID \
            --zone=$ZONE \
            --worker=all \
            --command='pip install -U "jax[tpu]" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html'
         

  4. Download Hugging Face [repository](https://github.com/huggingface/transformers.git) and install requirements:
         
         gcloud compute tpus tpu-vm ssh $TPU_NAME \
            --project=$PROJECT_ID \
            --zone=$ZONE \
            --worker=all \
            --command='git clone https://github.com/huggingface/transformers.git && cd transformers && pip install . && pip install -r examples/flax/_tests_requirements.txt && pip install --upgrade huggingface-hub urllib3 zipp && pip install tensorflow==2.19 && sed -i "s/torchvision==0.12.0+cpu/torchvision==0.22.1/" examples/flax/vision/requirements.txt && pip install -r examples/flax/vision/requirements.txt && pip install tf-keras'
         

  5. Download the Imagenette dataset:
         
         gcloud compute tpus tpu-vm ssh $TPU_NAME \
            --project=$PROJECT_ID \
            --zone=$ZONE \
            --worker=all \
            --command='cd transformers && wget https://s3.amazonaws.com/fast-ai-imageclas/imagenette2.tgz && tar -xvzf imagenette2.tgz'
         




#### Train the model

Train the model with a pre-mapped buffer at 4GB.
    
    
    gcloud compute tpus tpu-vm ssh $TPU_NAME \
       --project=$PROJECT_ID \
       --zone=$ZONE \
       --worker=all \
       --command='cd transformers && JAX_PLATFORMS=tpu python3 examples/flax/vision/run_image_classification.py --train_dir "imagenette2/train" --validation_dir "imagenette2/val" --output_dir "./vit-imagenette" --learning_rate 1e-3 --preprocessing_num_workers 32 --per_device_train_batch_size 8 --per_device_eval_batch_size 8 --model_name_or_path google/vit-base-patch16-224-in21k --num_train_epochs 3'
    

#### Delete the TPU and queued resource

Delete your TPU and queued-resource at the end of your session.
    
    
    gcloud compute tpus tpu-vm delete $TPU_NAME \
       --project=$PROJECT_ID \
       --zone=$ZONE \
       --quiet
    
    gcloud compute tpus queued-resources delete $QUEUED_RESOURCE_ID \
       --project=$PROJECT_ID \
       --zone=$ZONE \
       --quiet
    

#### ViT benchmarking results

The training script was run on v5litepod-4, v5litepod-16, and v5litepod-64. The following table shows the throughputs with different accelerator types.

Accelerator type | v5litepod-4 | v5litepod-16 | v5litepod-64  
---|---|---|---  
Epoch | 3 | 3 | 3  
Global batch size | 32 | 128 | 512  
Throughput (examples/sec) | 263.40 | 429.34 | 470.71  
  
#### Train Diffusion on Pokémon

This tutorial shows you how to train the Stable Diffusion model from HuggingFace using the [Pokémon](https://huggingface.co/datasets/diffusers/pokemon-gpt4-captions) dataset on Cloud TPU v5e.

The Stable Diffusion model is a latent text-to-image model that generates photorealistic images from any text input. For more information, see the following resources:

  * [Stable Diffusion overview](https://huggingface.co/CompVis/stable-diffusion-v1-4)
  * [Stable Diffusion code source ](https://github.com/huggingface/diffusers/tree/main/examples/text_to_image)



#### Set up

  1. Set an environment variable for the name of your storage bucket:
         
         export GCS_BUCKET_NAME=your_bucket_name
         

  2. Set up a storage bucket for your model output:
         
         Google Cloud CLI storage buckets create gs://$GCS_BUCKET_NAME \
              --project=$PROJECT_ID \
              --location=$ZONE
         

  3. Create environment variables:
         
         export PROJECT_ID=your-project-id
         export TPU_NAME=your-tpu-name
         export ZONE=us-west1-c
         export ACCELERATOR_TYPE=v5litepod-16
         export RUNTIME_VERSION=v2-alpha-tpuv5-lite
         export SERVICE_ACCOUNT=your-service-account
         export QUEUED_RESOURCE_ID=your-queued-resource-id

#### Environment variable descriptions

     * `PROJECT_ID`: Your Google Cloud project ID. Use an existing project or [create a new one.](https://docs.cloud.google.com/tpu/docs/setup-gcp-account#set-up-project)
     * `TPU_NAME`: The name of the TPU.
     * `ZONE`: The zone in which to create the TPU VM. For more information about supported zones, see [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones). 
     * `ACCELERATOR_TYPE`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions). 
     * `RUNTIME_VERSION`: The Cloud TPU [software version](https://docs.cloud.google.com/tpu/docs/runtimes).
     * `SERVICE_ACCOUNT`: The email address for your service account. You can find it by going to the [Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts) in the Google Cloud console. 

For example: `tpu-service-account@PROJECT_ID.iam.gserviceaccount.com`

     * `QUEUED_RESOURCE_ID`: The user-assigned text ID of the queued resource request.
  4. [Create a TPU resource:](https://docs.cloud.google.com/tpu/docs/queued-resources)
         
         gcloud compute tpus queued-resources create $QUEUED_RESOURCE_ID \
            --node-id=$TPU_NAME \
            --project=$PROJECT_ID \
            --zone=$ZONE \
            --accelerator-type=$ACCELERATOR_TYPE \
            --runtime-version=$RUNTIME_VERSION \
            --service-account=$SERVICE_ACCOUNT
         

**Note:** To use a reservation, add the `--reserved` flag. To use TPU Spot VMs, add the `--spot` flag.

You will be able to SSH to your TPU VM once your queued resource is in the `ACTIVE` state:
         
         gcloud compute tpus queued-resources describe $QUEUED_RESOURCE_ID  \
            --project=$PROJECT_ID \
            --zone=$ZONE
         

When the queued resource is in the `ACTIVE` state, the output will be similar to the following:
         
         state: ACTIVE
         

  5. Install JAX and its library.
         
         gcloud compute tpus tpu-vm ssh $TPU_NAME \
            --project=$PROJECT_ID \
            --zone=$ZONE \
            --worker=all \
            --command='pip install "jax[tpu]==0.4.16" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html'
         

  6. Download the HuggingFace [repository](https://github.com/huggingface/diffusers) and install requirements.
         
         gcloud compute tpus tpu-vm ssh $TPU_NAME \
              --project=$PROJECT_ID \
              --zone=$ZONE \
              --worker=all \
              --command='git clone https://github.com/RissyRan/diffusers.git && cd diffusers && pip install . && pip install -U -r examples/text_to_image/requirements_flax.txt && pip install tensorflow==2.17.1 clu && pip install tensorboard==2.17.1'
         




#### Train the model

Train the model with a pre-mapped buffer at 4GB.
    
    
    gcloud compute tpus tpu-vm ssh $TPU_NAME --zone=$ZONE --project=$PROJECT_ID --worker=all --command="
        git clone https://github.com/google/maxdiffusion
        cd maxdiffusion
        pip3 install jax[tpu] -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
        pip3 install -r requirements.txt
        pip3 install .
        pip3 install gcsfs
        export LIBTPU_INIT_ARGS=''
        python -m src.maxdiffusion.train src/maxdiffusion/configs/base_2_base.yml run_name=my_run \
        jax_cache_dir=gs://${GCS_BUCKET_NAME} activations_dtype=bfloat16 weights_dtype=bfloat16 \
        per_device_batch_size=1 precision=DEFAULT dataset_save_location=gs://${GCS_BUCKET_NAME} \
        output_dir=gs://${GCS_BUCKET_NAME}/ attention=flash"
    

#### Clean up

Delete your TPU, queued resource, and Cloud Storage bucket at the end of your session.

  1. Delete your TPU:
         
         gcloud compute tpus tpu-vm delete $TPU_NAME \
             --project=$PROJECT_ID \
             --zone=$ZONE \
             --quiet
         

  2. Delete the queued resource:
         
         gcloud compute tpus queued-resources delete $QUEUED_RESOURCE_ID \
             --project=$PROJECT_ID \
             --zone=$ZONE \
             --quiet
         

  3. Delete the Cloud Storage bucket:
         
         gcloud storage rm -r gs://$GCS_BUCKET_NAME
         




#### Benchmarking results for diffusion

The training script ran on v5litepod-4, v5litepod-16, and v5litepod-64. The following table shows the throughputs.

Accelerator type | v5litepod-4 | v5litepod-16 | v5litepod-64  
---|---|---|---  
Train Step | 1500 | 1500 | 1500  
Global batch size | 32 | 64 | 128  
Throughput (examples/sec) | 36.53 | 43.71 | 49.36  
  
## Train a model using PyTorch on Cloud TPU

You can use [TorchTPU](https://github.com/google-pytorch/torch_tpu) directly to train your model or reuse the [TorchTitan](https://github.com/google-pytorch/torchtitan) reference library. For more information about the PyTorch ecosystem on Cloud TPU, see [PyTorch on Cloud TPU](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
