---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-rl-v6e-8-tpu-vm/
title: Run reinforcement learning training on a TPU VM by using MaxText \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:22.236423+00:00
---

# Run reinforcement learning training on a TPU VM by using MaxText  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-rl-v6e-8-tpu-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Run reinforcement learning training on a TPU VM by using MaxText Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial provides a step-by-step guide for running reinforcement learning (RL) training on a single `v6e-8` Tensor Processing Unit (TPU) virtual machine (VM) instance on Google Cloud by using MaxText, a high-performance JAX-based training stack for large language models (LLMs).

## Workload summary

Running this RL post-training workload on Cloud TPU involves the following components:

  * **Model:** Llama 3.1 8B Instruct (`llama3.1-8b-Instruct`), an open-weights LLM optimized for dialogue and instruction-following tasks. In this tutorial, the model weights are converted from Hugging Face format into MaxText-compatible format (`mt-format`) and prepared for distributed execution on a `v6e-8` TPU using JAX.

  * **Reinforcement Learning (RL) algorithm:** Group Relative Policy Optimization (GRPO), in which the workload executes a scalable post-training pipeline using MaxText's built-in RL trainer. GRPO eliminates the need for a separate value or critic model by evaluating a group of outputs generated for the same prompt, using relative rewards to optimize the actor policy efficiently.

  * **Dataset and template:** Grade School Math 8K (GSM8K), a high-quality dataset consisting of linguistically diverse grade-school math word problems. This workload uses it for generating rollouts, calculating rewards, and improving multi-step reasoning capabilities during the RL alignment phase.

  * **Infrastructure and framework:** A single Cloud TPU `v6e-8` node (`ct6e-standard-8t`) using MaxText (`maxtext[tpu-post-train]`), a high-performance training stack powered by JAX.




## Objectives

  * Set up a Cloud TPU VM instance.
  * Install MaxText and its dependencies.
  * Convert a Hugging Face model to MaxText format.
  * Run a RL Group Relative Policy Optimization (GRPO) workload on the TPU.
  * Convert the trained model back to Hugging Face format for serving.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Cloud TPU](https://cloud.google.com/tpu/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

**Important:** To complete this tutorial, you must have access to `v6e-8` TPUs. This tutorial assumes that you already have a reservation for these TPUs in your Google Cloud project to ensure that you have the capacity available when you need it. To learn more about your options for reserving Cloud TPU capacity for a future date and time, see [About Cloud TPU reservations](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations).

## Before you begin

  * You need a Hugging Face access token to use this tutorial. You can sign up for a free account at [Hugging Face](http://huggingface.co/login). After you have an account, generate an access token:

    1. On the [Welcome to Hugging Face](https://huggingface.co/welcome) page, click your account avatar and select **Access tokens**.
    2. On the **Access tokens** page, click **Create new token**.
    3. Select the **Read** token type and enter a name for your token.
    4. Your access token is displayed. Save the token in a safe place.



  * On the [Hugging Face website](https://huggingface.co/), accept the license agreement for the model that you plan to train. This tutorial uses the model `llama3.1-8b-Instruct`.



To get the permissions that you need to complete this tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * [TPU Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#tpu.admin) (`roles/tpu.admin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Compute Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.editor) (`roles/compute.editor`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up the environment

Set up your environment variables by running the following script:
    
    
    export PROJECT="YOUR_PROJECT_ID"
    export ZONE="YOUR_ZONE"
    export RESERVATION="YOUR_RESERVATION_NAME"
    export TPU_NAME="YOUR_TPU_NAME"

Replace the following:

  * YOUR_PROJECT_ID: your Google Cloud project ID
  * YOUR_ZONE: the zone that you want to use
  * YOUR_RESERVATION_NAME: your capacity reservation
  * YOUR_TPU_NAME: the name of your Cloud TPU VM instance



Authenticate with Google Cloud by running the following command:
    
    
    gcloud auth login
    

## Create your Cloud TPU VM

Create a Cloud TPU VM instance with 8 `v6e` TPU chips, bound to your capacity reservation.
    
    
    gcloud compute instances create "${TPU_NAME}" \
        --zone="${ZONE}" \
        --project="${PROJECT}" \
        --machine-type=ct6e-standard-8t \
        --image-project=ubuntu-os-accelerator-images \
        --image-family=ubuntu-accel-2204-amd64-tpu-v5e-v5p-v6e \
        --boot-disk-size=200GB \
        --maintenance-policy=TERMINATE \
        --instance-termination-action=DELETE \
        --provisioning-model=RESERVATION_BOUND \
        --reservation-affinity=specific \
        --reservation="${RESERVATION}"

After the VM instance has been created, connect to it by using SSH.
    
    
    gcloud compute ssh "${TPU_NAME}" --zone "${ZONE}" --project "${PROJECT}"

Complete the steps that follow within your TPU VM instance.

## Install MaxText

Update the system packages within the TPU VM instance.
    
    
    sudo apt update && sudo apt upgrade -y --fix-missing

Install Python 3.12, which MaxText requires, and its virtual environment package.
    
    
    sudo apt install -y build-essential cmake ninja-build

Use `uv` to speed up the installation of the Python package.
    
    
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source "${HOME}/.local/bin/env"

Create a virtual environment named `maxtext_venv` and activate it.
    
    
    uv python install 3.12
    uv venv --python 3.12 --seed maxtext_venv
    source maxtext_venv/bin/activate

Install MaxText and the dependencies that it requires for post-training tasks.
    
    
    UV_TORCH_BACKEND=cpu uv pip install "maxtext[tpu-post-train]==0.2.3" --resolution=lowest

Install the remaining required dependencies by running the following command:
    
    
    install_tpu_post_train_extra_deps

## Convert the model to MaxText format

To train the model in MaxText format, you must convert it from Hugging Face format to MaxText format.

Provide the following values:

  * Your Hugging Face access token
  * The name of the model that you want to use
  * The directory where you want to save the model in MaxText format
  * Options for loading and storage


    
    
    export HF_TOKEN="YOUR_HF_TOKEN"
    export MODEL_NAME='llama3.1-8b-Instruct'
    export MODEL_CHECKPOINT_DIRECTORY=/dev/shm/$MODEL_NAME/mt-format/
    export USE_PATHWAYS=0 # Set to 1 for Pathways, 0 for McJAX
    export LAZY_LOAD_TENSORS=False # True to use lazy load, False to use eager load.

Replace YOUR_HF_TOKEN with the Hugging Face access token that you previously created.

To convert the model from Hugging Face format to MaxText format, run the following script. This conversion takes about five minutes to complete.
    
    
    python3 -m maxtext.checkpoint_conversion.to_maxtext \
        model_name="${MODEL_NAME?}" \
        hf_access_token="${HF_TOKEN?}" \
        base_output_directory="${MODEL_CHECKPOINT_DIRECTORY?}" \
        scan_layers=True \
        use_multimodal=False \
        hardware=cpu \
        skip_jax_distributed_system=true \
        checkpoint_storage_use_zarr3=$((1 - USE_PATHWAYS)) \
        checkpoint_storage_use_ocdbt=$((1 - USE_PATHWAYS)) \
        --lazy_load_tensors="${LAZY_LOAD_TENSORS?}"

## Start the training workload

After the conversion process has completed, you can start the RL workload.

  1. Configure the RL workload training parameters.
         
         # -- MaxText configuration --
         export BASE_OUTPUT_DIRECTORY=/dev/shm/$MODEL_NAME/post-train/
         RUN_NAME=$(date +%Y-%m-%d-%H-%M-%S)
         export RUN_NAME
         export CHIPS_PER_VM=8
         export NUM_BATCHES=50
         export MAXTEXT_CKPT_PATH=$MODEL_CHECKPOINT_DIRECTORY/0/items
         export TPU_ACCELERATOR_TYPE=v6e-8
         export TPU_WORKER_ID=0
         TPU_NAME=$(hostname)
         export TPU_NAME
         export TPU_SKIP_MDS_QUERY=1
         export TPU_WORKER_HOSTNAMES=localhost
         export TPU_TOPOLOGY=2x4
         export TPU_CHIPS_PER_HOST_BOUNDS=2,4,1
         export TPU_HOST_BOUNDS=1,1,1

  2. Start the training job. This takes about 10 minutes on a `v6e-8` VM instance.
         
         python3 -m maxtext.trainers.post_train.rl.train_rl \
             model_name="${MODEL_NAME?}" \
             load_parameters_path="${MAXTEXT_CKPT_PATH?}" \
             run_name="${RUN_NAME?}" \
             base_output_directory="${BASE_OUTPUT_DIRECTORY?}" \
             chips_per_vm="${CHIPS_PER_VM?}" \
             num_batches="${NUM_BATCHES?}" \
             num_test_batches=10 \
             rollout_data_parallelism=1 \
             rollout_tensor_parallelism=-1




## Convert the trained model back into Hugging Face format

After the training workload has completed, convert the model back to Hugging Face format.

  1. Set the paths for export and the trained parameters.
         
         export HF_EXPORT=/dev/shm/$MODEL_NAME/hf-trained/
         export HF_MODEL_NAME=llama3.1-8b
         export POST_TRAIN_PATH=$BASE_OUTPUT_DIRECTORY/$RUN_NAME/checkpoints/actor/$NUM_BATCHES/model_params

  2. Run the conversion back to Hugging Face format.
         
         python3 -m maxtext.checkpoint_conversion.to_huggingface \
             model_name="${HF_MODEL_NAME?}" \
             load_parameters_path="${POST_TRAIN_PATH?}" \
             base_output_directory="${HF_EXPORT?}" \
             scan_layers=True \
             use_multimodal=False \
             weight_dtype=bfloat16




After the conversion has completed, your tuned model that's stored in `/dev/shm/$MODEL_NAME/hf-trained` is ready to use. Because you lose access to the contents of the `/dev/shm` folder when the VM reboots, you should move the tuned model to persistent storage or upload it to the Hugging Face Hub.

## Clean up

To avoid incurring additional charges, delete the resources created during this tutorial.

### Delete your TPU VM instance

Delete your Cloud TPU VM instance.
    
    
    gcloud compute instances delete "${TPU_NAME}" --zone="${ZONE}" --project="${PROJECT}" --quiet

## What's next

  * For more information about Cloud TPU, see [Introduction to Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu).
  * For architecture and configuration details for the `v6e-8` TPU, see [TPU v6e](https://docs.cloud.google.com/tpu/docs/v6e).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
