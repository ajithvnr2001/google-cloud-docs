---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-sft-v6e-8-tpu-vm-maxtext/
title: Run supervised fine-tuning on a TPU VM by using MaxText \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:11.239189+00:00
---

# Run supervised fine-tuning on a TPU VM by using MaxText  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-sft-v6e-8-tpu-vm-maxtext/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Run supervised fine-tuning on a TPU VM by using MaxText Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial provides a step-by-step guide for running supervised fine-tuning (SFT) on a single `v6e-8` Tensor Processing Unit (TPU) virtual machine (VM) instance on Google Cloud by using MaxText, a high-performance JAX-based training stack for large language models (LLMs).

## Workload summary

Running this SFT workload on a Cloud TPU VM involves the following components:

  * **Model:** Gemma 3 4B (`gemma3-4b`), an open-weights lightweight language model. In this tutorial, the model weights are converted from Hugging Face format into MaxText-compatible format (`mt-format`) and prepared for execution on a single Cloud TPU `v6e-8` VM using JAX.
  * **Training method:** SFT using MaxText. The workload executes a fine-tuning pipeline on a single Cloud TPU `v6e-8` instance using JAX. It optimizes model parameters over 1000 steps using MaxText's built-in SFT trainer (`maxtext.trainers.post_train.sft.train_sft`) and dialogue-focused instruction-tuning datasets.
  * **Dataset and template:** UltraChat 200k (`HuggingFaceH4/ultrachat_200k`), a large-scale, high-quality multi-turn dialogue dataset (`train_sft` split with `messages` column). It is used to fine-tune the model and improve its conversational and instruction-following capabilities.
  * **Infrastructure and framework:** a single Cloud TPU `v6e-8` VM instance (`ct6e-standard-8t`). The framework is MaxText (`maxtext[tpu-post-train]`) powered by JAX.



## Objectives

  * Set up a Cloud TPU VM instance.
  * Install MaxText and its dependencies.
  * Convert a Hugging Face model to MaxText format.
  * Run an SFT training workload on the TPU.
  * Convert the fine-tuned model back to Hugging Face format for serving.



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



  * On the [Hugging Face website](https://huggingface.co/), accept the license agreement for the model that you plan to train. This tutorial uses the model `gemma3-4b`.



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
    export NAME="YOUR_TPU_NAME"
    export NETWORK="default"

Replace the following:

  * YOUR_PROJECT_ID: your Google Cloud project ID
  * YOUR_ZONE: the zone that you want to use
  * YOUR_RESERVATION_NAME: your capacity reservation
  * YOUR_TPU_NAME: the name of your Cloud TPU VM instance



Authenticate with Google Cloud by running the following command:
    
    
    gcloud auth login
    

## Create your Cloud TPU VM

Create a Cloud TPU VM instance with 8 `v6e` TPU chips, bound to your capacity reservation.
    
    
    gcloud compute instances create "${NAME}" \
        --zone="${ZONE}" \
        --project="${PROJECT}" \
        --network="${NETWORK}" \
        --tags="${NAME}" \
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
    
    
    gcloud compute ssh "${NAME}" --zone "${ZONE}" --project "${PROJECT}"

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
    
    
    UV_TORCH_BACKEND=cpu uv pip install "maxtext[tpu-post-train]==0.2.2" --resolution=lowest

Install the remaining required dependencies by running the following command:
    
    
    install_tpu_post_train_extra_deps

## Convert the model to MaxText format

To train the model in MaxText format, you must convert it from Hugging Face format to MaxText format.

Specify your environment variables, such as your Hugging Face access token, the name of the model that you want to use, and the directory where you want to save the model in MaxText format.
    
    
    export HF_TOKEN="YOUR_HF_TOKEN"
    export MODEL_NAME='gemma3-4b'
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

After the conversion process has completed, you can start the SFT workload.

  1. Configure the SFT workload training parameters.
         
         # -- MaxText configuration --
         export BASE_OUTPUT_DIRECTORY=/dev/shm/$MODEL_NAME/post-train/
         RUN_NAME=$(date +%Y-%m-%d-%H-%M-%S)
         export RUN_NAME
         export STEPS=1000
         export PER_DEVICE_BATCH_SIZE=1
         
         # -- Dataset configuration --
         export DATASET_NAME="HuggingFaceH4/ultrachat_200k"
         export TRAIN_SPLIT="train_sft"
         export TRAIN_DATA_COLUMNS="['messages']"
         
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
         
         python3 -m maxtext.trainers.post_train.sft.train_sft \
             run_name="${RUN_NAME?}" \
             base_output_directory="${BASE_OUTPUT_DIRECTORY?}" \
             model_name="${MODEL_NAME?}" \
             load_parameters_path="${MAXTEXT_CKPT_PATH?}" \
             per_device_batch_size="${PER_DEVICE_BATCH_SIZE?}" \
             steps="${STEPS?}" \
             hf_path="${DATASET_NAME?}" \
             train_split="${TRAIN_SPLIT?}" \
             train_data_columns="${TRAIN_DATA_COLUMNS?}" \
             profiler=xplane




## Convert the trained model back into Hugging Face format

After the training workload has completed, convert the model back to Hugging Face format.

  1. Set the paths for export and the trained parameters.
         
         export HF_EXPORT=/dev/shm/$MODEL_NAME/hf-trained/
         export POST_TRAIN_PATH=$BASE_OUTPUT_DIRECTORY/$RUN_NAME/checkpoints/$STEPS/model_params

  2. Run the conversion back to Hugging Face format.
         
         python3 -m maxtext.checkpoint_conversion.to_huggingface \
             model_name="${MODEL_NAME}" \
             load_parameters_path="${POST_TRAIN_PATH}" \
             base_output_directory="${HF_EXPORT}" \
             scan_layers=True \
             use_multimodal=False \
             weight_dtype=bfloat16




After the conversion has completed, your tuned model stored in `/dev/shm/gemma3-4b/hf-trained` is ready to be used. Because you lose access to the contents of the `/dev/shm` folder when the VM reboots, you should move the tuned model to persistent storage or upload it to the Hugging Face Hub.

## Clean up

To avoid incurring additional charges, delete the resources created during this tutorial.

### Delete your TPU VM instance

Exit your Cloud TPU VM instance, and then delete it.
    
    
    # 1. Delete TPU instance
    echo "Deleting TPU instance: ${NAME}..."
    gcloud compute instances delete "${NAME}" \
        --zone="${ZONE}" \
        --project="${PROJECT}" \
        --quiet || true
    
    # 2. Delete IAP firewall rule
    echo "Deleting firewall rule: ${FIREWALL_RULE_NAME}..."
    gcloud compute firewall-rules delete "${FIREWALL_RULE_NAME}" \
        --project="${PROJECT}" \
        --quiet || true

## What's next

  * For more information about Cloud TPU, see [Introduction to Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu).
  * For architecture and configuration details for the `v6e-8` TPU, see [TPU v6e](https://docs.cloud.google.com/tpu/docs/v6e).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
