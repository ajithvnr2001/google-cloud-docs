---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/train-qwen2-a4-slurm-cluster/
title: Train Qwen2 on an A4 Slurm cluster \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:22.261194+00:00
---

# Train Qwen2 on an A4 Slurm cluster  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/train-qwen2-a4-slurm-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Train Qwen2 on an A4 Slurm cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This tutorial shows you how to train a large language model (LLM) on a multi-node, multi-GPU Slurm cluster on Google Cloud. The model that you use in this tutorial is based on a Qwen2 1.5 billion parameter model. The Slurm cluster uses two a4-highgpu-8g virtual machines (VMs), which each have 8 NVIDIA B200 GPUs.

The two main processes described in this tutorial are as follows:

  1. Deploy a production-grade, high-performance Slurm cluster using the Google Cloud Cluster Toolkit. As part of this deployment, you create a custom VM image with the necessary software pre-installed. You also set up a shared Filestore instance, and configure high-speed RDMA networking.
  2. After the cluster is deployed, you run a distributed pre-training job by using the set of scripts that accompany this tutorial. The job leverages the [Hugging Face Accelerate library.](https://huggingface.co/docs/accelerate/en/usage_guides/fsdp)

**Important:** To complete this tutorial, you must have reserved the capacity to create two A4 VMs. To learn more about your options for reserving capacity in AI Hypercomputer for a future date and time, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

This tutorial is intended for machine learning (ML) engineers, researchers, platform administrators and operators, and for data and AI specialists who are interested in deploying high-performance Slurm clusters on Google Cloud to train LLMs.

## Objectives

  * Access the Qwen2 model by using Hugging Face.
  * Prepare your environment.
  * Create and deploy a production-grade A4 Slurm cluster.
  * Train the Qwen2 model by using the [Accelerate](https://huggingface.co/docs/accelerate/en/index) library .
  * Monitor your job.
  * Clean up.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Compute Engine](https://cloud.google.com/compute/gpus-pricing)
  * [ Filestore](https://docs.cloud.google.com/filestore/pricing)
  * [ Cloud Storage](https://docs.cloud.google.com/storage/pricing)
  * [ Cloud Logging](https://docs.cloud.google.com/logging#pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the required API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com file.googleapis.com logging.googleapis.com cloudresourcemanager.googleapis.com servicenetworking.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the required API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com file.googleapis.com logging.googleapis.com cloudresourcemanager.googleapis.com servicenetworking.googleapis.com

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: ` roles/compute.admin, roles/iam.serviceAccountUser, roles/file.editor, roles/storage.admin, roles/serviceusage.serviceUsageAdmin, roles/compute.osAdminLogin, roles/iap.tunnelResourceAccessor `
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.
  15. Enable the default service account for your Google Cloud project: 
         
         gcloud iam service-accounts enable PROJECT_NUMBER-compute@developer.gserviceaccount.com \
             --project=PROJECT_ID

Replace PROJECT_NUMBER with your project number. To review your project number, see [ Get an existing project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#get_an_existing_project). 

  16. Grant the Editor role (`roles/editor`) to the default service account: 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
             --role=roles/editor

  17. Create local authentication credentials for your user account: 
         
         gcloud auth application-default login

**Note** : If you use a local shell and an external identity provider (IdP), and you encounter an authentication error after running the preceding command, then [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 
  18. Enable OS Login for your project: 
         
         gcloud compute project-info add-metadata --metadata=enable-oslogin=TRUE

  19. [Sign in to or create a Hugging Face account](https://huggingface.co/login).



## Access Qwen2 by using Hugging Face

To use Hugging Face to access Qwen2, do the following:

  1. [Sign the consent agreement to use Qwen 2 1.5B](https://huggingface.co/Qwen/Qwen2-1.5B).

  2. [Create a `read` access token](https://huggingface.co/docs/hub/security-tokens#how-to-manage-user-access-tokens).




## Install Cluster Toolkit

Cluster Toolkit is an open-source tool that simplifies deploying high performance computing (HPC), artificial intelligence (AI), and machine learning (ML) workloads on Google Cloud. For more information about using the [`gcluster` CLI](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster) and managing clusters, see the [Cluster Toolkit overview](https://docs.cloud.google.com/cluster-toolkit/docs/overview).

  1. Prepare the Cluster Toolkit version:
         
         export CLUSTER_TOOLKIT_TAG=v1.97.0
         
         # Detect OS (linux or mac)
         case "$(uname -s)" in
           Linux*)     OS="linux" ;;
           Darwin*)    OS="mac" ;;
           *)          echo "Error: Unsupported operating system: $(uname -s)" >&2; exit 1 ;;
         esac
         
         # Detect Architecture (amd64 or arm64)
         case "$(uname -m)" in
           x86_64)     ARCH="amd64" ;;
           aarch64|arm64) ARCH="arm64" ;;
           *)          echo "Error: Unsupported architecture: $(uname -m)" >&2; exit 1 ;;
         esac

  2. Download the release:
         
         # Download and extract the platform-specific bundle
         curl -LO "https://github.com/GoogleCloudPlatform/cluster-toolkit/releases/download/${CLUSTER_TOOLKIT_TAG}/gcluster_bundle_${OS}_${ARCH}.zip"
         unzip "gcluster_bundle_${OS}_${ARCH}.zip" -d cluster-toolkit/
         rm -f "gcluster_bundle_${OS}_${ARCH}.zip"

  3. Define the `gcluster` path:
         
         export CLUSTER_TOOLKIT_PATH="$(pwd)/cluster-toolkit"
         export PATH="${CLUSTER_TOOLKIT_PATH}:${PATH}"
         gcluster --version




## Prepare your environment

To prepare your environment, follow these steps:

  1. Set the default environment variables: 
         
         export PROJECT_ID="YOUR_PROJECT_ID"
         export CLUSTER_NAME="YOUR_CLUSTER_NAME"
         export ZONE="YOUR_ZONE"
         export REGION="YOUR_REGION"
         export RESERVATION_URL="YOUR_RESERVATION_NAME"
         export GCS_BUCKET="YOUR_GCS_BUCKET"
         export HF_TOKEN="YOUR_HF_TOKEN"
         
         gcloud config set project "${PROJECT_ID}"
         gcloud config set billing/quota_project "${PROJECT_ID}"

Replace the following:

     * `YOUR_PROJECT_ID`: the name of the Google Cloud project where you want to create the GKE cluster.
     * `YOUR_CLUSTER_NAME`: the name of the Slurm cluster that you want to create.
     * `YOUR_ZONE`: the zone where your reservation exists.
     * `YOUR_REGION,`: the region where your reservation exists.
     * `RESERVATION_NAME`: the URL or the name of the reservation that you want to use to create your Slurm cluster.
     * `YOUR_GCS_BUCKET`: the name of the bucket where you store the results from the training checkpoint. Before you create it, familiarize yourself with [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).
     * `YOUR_HF_TOKEN`: the Hugging Face token that you created in an earlier step.
  2. Create a Cloud Storage bucket:
         
         gcloud storage buckets create "gs://${GCS_BUCKET}" \
           --project="${PROJECT_ID}"




## Create an A4 Slurm cluster

To create an A4 Slurm cluster, follow these steps:

  1. Create the `a4high-slurm-deployment.yaml` file:
         
         MANIFEST_PATH="${CLUSTER_TOOLKIT_PATH}/examples/machine-learning/a4-highgpu-8g"
         cat <<EOF > "${MANIFEST_PATH}/a4high-slurm-deployment.yaml"
         terraform_backend_defaults:
           type: gcs
           configuration:
             bucket: ${GCS_BUCKET}
         
         vars:
           deployment_name: ${CLUSTER_NAME}
           project_id: ${PROJECT_ID}
           region: ${REGION}
           zone: ${ZONE}
           a4h_cluster_size: 2
           a4h_reservation_name: ${RESERVATION_URL}
         EOF

  2. Use the [`gcluster create` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-create) to create the Terraform manifests:
         
         gcluster create \
           -d "${MANIFEST_PATH}/a4high-slurm-deployment.yaml" \
           "${MANIFEST_PATH}/a4high-slurm-blueprint.yaml" \
           -o "${CLUSTER_NAME}"

  3. Patch the manifests:
         
         sed -i '/deletion_protection = {/,/}/ { s/enabled = true/enabled = false/; /reason  = "Avoid data loss"/d; }' "${CLUSTER_NAME}/${CLUSTER_NAME}/cluster-env/main.tf"

  4. Deploy the cluster:
         
         gcluster deploy "${CLUSTER_NAME}/${CLUSTER_NAME}" --auto-approve

The [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) is a two-phase process, which is as follows:

     * The first phase builds a custom image with all software pre-installed, which can take up to 50 minutes to complete.

     * The second phase deploys the cluster by using that custom image. This process generally takes less time to complete than the first phase.

If the first phase succeeds but the second phase fails, then you can try to deploy the Slurm cluster again by skipping the first phase:
    
    gcluster deploy "${CLUSTER_NAME}" --auto-approve --skip "image" -w




## Prepare your workload

To prepare your workload, follow these steps:

  1. Create workload scripts.

  2. Upload scripts to the Slurm cluster.

  3. Connect to the Slurm cluster.

  4. Install frameworks and tools.




### Create workload scripts

To create the scripts that your training workload will use, follow these steps:

  1. To set up the Python virtual environment, create the `install_environment.sh` file with the following content:
         
         #!/bin/bash
         # This script should be run ONCE on the login node to set up the
         # shared Python virtual environment.
         
         set -e
         echo "--- Creating Python virtual environment in /home ---"
         python3 -m venv ~/.venv
         echo "--- Activating virtual environment ---"
         source ~/.venv/bin/activate
         
         echo "--- Installing build dependencies ---"
         pip install --upgrade pip wheel packaging
         
         echo "--- Installing PyTorch for CUDA 12.8 ---"
         pip install torch --index-url https://download.pytorch.org/whl/cu128
         
         echo "--- Installing application requirements ---"
         pip install -r requirements.txt
         
         echo "--- Environment setup complete. You can now submit jobs with sbatch. ---"

  2. To specify the configurations for your fine-tuning job, create the `accelerate_config.yaml` file with the following content:
         
         compute_environment: "LOCAL_MACHINE"
         distributed_type: "FSDP"
         downcast_bf16: "no"
         fsdp_config:
           fsdp_auto_wrap_policy: "TRANSFORMER_BASED_WRAP"
           fsdp_backward_prefetch: "BACKWARD_PRE"
           fsdp_cpu_ram_efficient_loading: true
           fsdp_forward_prefetch: false
           fsdp_offload_params: false
           fsdp_sharding_strategy: "FULL_SHARD"
           fsdp_state_dict_type: "SHARDED_STATE_DICT"
           fsdp_transformer_layer_cls_to_wrap: "Qwen2DecoderLayer"
         machine_rank: 0
         main_training_function: "main"
         mixed_precision: "bf16"
         num_machines: 2
         num_processes: 16
         rdzv_backend: "static"
         same_network: true
         tpu_env: []
         use_cpu: false

  3. To specify the tasks for the jobs to run on your Slurm cluster, create the `submit.slurm` file with the following content:
         
         #SBATCH --job-name=qwen2-pretrain-smollm-fineweb
         #SBATCH --nodes=2
         #SBATCH --ntasks-per-node=1  # 1 main srun task on the node that manages accelerate
         #SBATCH --gpus-per-node=8    # access to all 8 GPUs on the node
         #SBATCH --partition=a4high
         #SBATCH --output=logs/slurm-%j.out
         #SBATCH --error=logs/slurm-%j.err
         
         set -euo pipefail
         echo "--- Slurm Job Started ---"
         
         # --- STAGE 1: Setup environment and pre-process data on each node's local SSD ---
         srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 --gpu-bind=none bash -c '
           set -e
           echo "Setting up local environment on $(hostname)..."
           LOCAL_VENV="/mnt/localssd/venv_job_${SLURM_JOB_ID}"
           LOCAL_CACHE="/mnt/localssd/hf_cache_job_${SLURM_JOB_ID}"
           PROCESSED_DATA_DIR="/mnt/localssd/processed_data_${SLURM_JOB_ID}"
           LOCAL_TMP="/mnt/localssd/tmp_job_${SLURM_JOB_ID}"
         
           rsync -a --info=progress2 ~/.venv/ ${LOCAL_VENV}/
           mkdir -p ${LOCAL_CACHE} ${PROCESSED_DATA_DIR} ${LOCAL_TMP}
         
           echo "Pre-processing data on $(hostname)..."
           source ${LOCAL_VENV}/bin/activate
           export TMPDIR="${LOCAL_TMP}"
           export TEMP="${LOCAL_TMP}"
           export TMP="${LOCAL_TMP}"
           export HF_HOME="${LOCAL_CACHE}"
           export HF_DATASETS_CACHE="${LOCAL_CACHE}"
           export HF_MODULES_CACHE="${LOCAL_CACHE}/modules"
           export HF_METRICS_CACHE="${LOCAL_CACHE}/metrics"
         
           python "${HOME}/preprocess_data.py" \
             --dataset_name "HuggingFaceFW/fineweb-edu" \
             --dataset_config "CC-MAIN-2024-10" \
             --tokenizer_id "Qwen/Qwen2-1.5B" \
             --max_seq_length 1024 \
             --output_path ${PROCESSED_DATA_DIR}
         
           echo "Setup on $(hostname) complete."
         '
         
         # --- STAGE 2: Run the Training Job using the Local Environment ---
         echo "--- Starting Training ---"
         
         LOCAL_VENV="/mnt/localssd/venv_job_${SLURM_JOB_ID}"
         PROCESSED_DATA_DIR="/mnt/localssd/processed_data_${SLURM_JOB_ID}"
         LOCAL_OUTPUT_DIR="/mnt/localssd/outputs_${SLURM_JOB_ID}"
         
         export MASTER_ADDR=$(scontrol show hostnames "$SLURM_JOB_NODELIST" | head -n 1)
         export MASTER_PORT=29505
         
         # Network and initialization debugging configurations
         export NCCL_DEBUG=INFO
         export NCCL_DEBUG_SUBSYS=INIT,COLL
         export TORCH_DISTRIBUTED_DEBUG=INFO
         export NCCL_IB_DISABLE=0
         
         # Launching with full GPU access enabled for accelerate
         srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 --gpu-bind=none bash -c "
           mkdir -p ${LOCAL_OUTPUT_DIR}
           source ${LOCAL_VENV}/bin/activate
         
           # Reset the forced Slurm isolation to expose all 8 GPUs to the processes
           unset CUDA_VISIBLE_DEVICES
         
           # Retrieve the default network device.
           DETECTED_IFACE=\$(ip route show | grep default | awk '{print \$5}' | head -n 1)
           echo \"[INFO] Automatically detected cluster network interface: \$DETECTED_IFACE\"
         
           # Dynamic injection of the detected interface into the network configuration
           export NCCL_SOCKET_IFNAME=\"\${DETECTED_IFACE},gpu*\"
           export TP_SOCKET_IFNAME=\"\${DETECTED_IFACE}\"
           export GLOO_SOCKET_IFNAME=\"\${DETECTED_IFACE}\"
         
           accelerate launch \
             --config_file ~/accelerate_config.yaml \
             --num_machines \$SLURM_NNODES \
             --num_processes \$((SLURM_NNODES * 8)) \
             --machine_rank \$SLURM_NODEID \
             --main_process_ip \$MASTER_ADDR \
             --main_process_port \$MASTER_PORT \
             train.py \
               --model_config_id 'Qwen/Qwen2-1.5B' \
               --preprocessed_data_path ${PROCESSED_DATA_DIR} \
               --output_dir ${LOCAL_OUTPUT_DIR} \
               --per_device_train_batch_size 4 \
               --gradient_accumulation_steps 4 \
               --max_steps 10000 \
               --learning_rate 5e-5 \
               --save_strategy steps \
               --save_steps 500 \
               --logging_steps 1
         "
         
         # --- STAGE 3: Copy Final Model from Local SSD to Home Directory ---
         echo "--- Copying final model from local SSD to /home ---"
         mkdir -p ~/qwen2-from-scratch-on-smollm-fineweb/
         
         srun --nodes=1 --ntasks=1 --ntasks-per-node=1 bash -c "
           rsync -a --info=progress2 ${LOCAL_OUTPUT_DIR}/ ~/qwen2-from-scratch-on-smollm-fineweb/
         "
         
         echo "--- Slurm Job Finished ---"

  4. To specify the dependencies for your fine-tuning job, create a `requirements.txt` file with the following content:
         
         # Hugging Face Libraries (Pinned to recent, stable versions for reproducibility)
         transformers==4.53.3
         datasets==4.0.0
         accelerate==1.9.0
         evaluate==0.4.5
         bitsandbytes==0.46.1
         trl==0.19.1
         peft==0.16.0
         
         # Other dependencies
         tensorboard==2.20.0
         protobuf==6.31.1
         sentencepiece==0.2.0

Note: This tutorial doesn't use the latest versions of NVIDIA and Pytorch dependencies. If you need newer dependencies, then see the [NVIDIA documentation](https://developer.nvidia.com/cuda-gpus) and the [Pytorch documentation](https://pytorch.org/get-started/locally/#linux-pip).
  5. To download, tokenize, and preprocess the dataset into a format that's ready for training, create a `preprocess_data.py` file with the following content:
         
         import argparse
         from datasets import load_dataset
         from transformers import AutoTokenizer
         import os
         from itertools import chain
         
         def get_args():
            parser = argparse.ArgumentParser(description="Download and preprocess a dataset.")
            parser.add_argument("--dataset_name", type=str, required=True)
            parser.add_argument("--dataset_config", type=str, required=True)
            parser.add_argument("--tokenizer_id", type=str, required=True)
            parser.add_argument("--max_seq_length", type=int, required=True)
            parser.add_argument("--output_path", type=str, required=True, help="Path to save the processed dataset.")
            return parser.parse_args()
         
         def main():
            args = get_args()
         
            if os.path.exists(args.output_path) and os.listdir(args.output_path):
                print(f"Processed dataset already exists at {args.output_path}. Skipping.")
                return
         
            # 1. Load tokenizer
            tokenizer = AutoTokenizer.from_pretrained(args.tokenizer_id)
         
            # 2. Load raw dataset
            print(f"Loading raw dataset {args.dataset_name}...")
            raw_dataset = load_dataset(args.dataset_name, name=args.dataset_config, split="train")
         
            # 3. Tokenize
            def tokenize_function(examples):
                return tokenizer(examples["text"])
         
            num_proc = os.cpu_count()
            print(f"Tokenizing dataset using {num_proc} processes...")
            print("Tokenizing dataset...")
            tokenized_dataset = raw_dataset.map(
                tokenize_function,
                batched=True,
                remove_columns=raw_dataset.column_names,
                desc="Running tokenizer on dataset",
                num_proc=num_proc,
            )
         
            # 4. Group texts
            def group_texts(examples):
                concatenated_examples = {k: list(chain.from_iterable(examples[k])) for k in examples.keys()}
                total_length = len(concatenated_examples[list(examples.keys())[0]])
                if total_length >= args.max_seq_length:
                    total_length = (total_length // args.max_seq_length) * args.max_seq_length
                result = {
                    k: [t[i : i + args.max_seq_length] for i in range(0, total_length, args.max_seq_length)]
                    for k, t in concatenated_examples.items()
                }
                result["labels"] = result["input_ids"].copy()
                return result
         
            print("Grouping texts...")
            lm_dataset = tokenized_dataset.map(
                group_texts,
                batched=True,
                desc=f"Grouping texts in chunks of {args.max_seq_length}",
                num_proc=num_proc,
            )
         
            # 5. Save to disk
            print(f"Saving processed dataset to {args.output_path}...")
            lm_dataset.save_to_disk(args.output_path)
            print("Preprocessing complete.")
         
         if __name__ == "__main__":
            main()

  6. To specify the instructions for your job, create a `train.py` file with the following content:
         
         import torch
         import argparse
         from datasets import load_dataset, load_from_disk
         import os
         from transformers import (
             AutoConfig,
             AutoTokenizer,
             AutoModelForCausalLM,
             Trainer,
             TrainingArguments,
             DataCollatorForLanguageModeling,
         )
         from huggingface_hub import login
         
         def get_args():
             parser = argparse.ArgumentParser()
             parser.add_argument("--model_config_id", type=str, default="Qwen/Qwen2-1.5B", help="Hugging Face model config to use for architecture.")
             # Data arguments - used if preprocessed data is not available
             parser.add_argument("--dataset_name", type=str, default="HuggingFaceFW/fineweb-edu", help="Hugging Face dataset for pre-training.")
             parser.add_argument("--dataset_config", type=str, default="CC-MAIN-2024-10", help="Config for the fineweb-edu dataset, e.g., 'CC-MAIN-2024-10'.")
             parser.add_argument("--preprocessed_data_path", type=str, default=None, help="Path to a preprocessed dataset on disk. If provided, skips download and processing.")
             # General arguments
             parser.add_argument("--hf_token", type=str, default=None, help="Hugging Face token for private models/tokenizers")
             parser.add_argument("--output_dir", type=str, default="qwen2-from-scratch-on-smollm-fineweb", help="Directory to save model checkpoints")
         
             # TrainingArguments
             parser.add_argument("--max_seq_length", type=int, default=1024, help="Maximum sequence length")
             parser.add_argument("--num_train_epochs", type=int, default=1, help="Number of training epochs")
             parser.add_argument("--max_steps", type=int, default=-1, help="If set to a positive number, it overrides num_train_epochs.")
             parser.add_argument("--per_device_train_batch_size", type=int, default=4, help="Batch size per device during training")
             parser.add_argument("--gradient_accumulation_steps", type=int, default=4, help="Gradient accumulation steps")
             parser.add_argument("--learning_rate", type=float, default=5e-5, help="Learning rate")
             parser.add_argument("--logging_steps", type=int, default=10, help="Log every X steps")
             parser.add_argument("--save_strategy", type=str, default="steps", help="Checkpoint save strategy")
             parser.add_argument("--save_steps", type=int, default=500, help="Save checkpoint every X steps")
         
             return parser.parse_args()
         
         def main():
             args = get_args()
         
             # --- 1. Setup and Login ---
             if args.hf_token:
                 login(args.hf_token)
         
             # --- 2. Load Tokenizer ---
             # We load the tokenizer from the specified config ID to ensure compatibility
             # with the model architecture (e.g., special tokens).
             tokenizer = AutoTokenizer.from_pretrained(args.model_config_id)
         
             # --- 3. Initialize Model from Scratch ---
             print(f"Initializing a new model from {args.model_config_id} configuration...")
             config = AutoConfig.from_pretrained(args.model_config_id)
             model = AutoModelForCausalLM.from_config(config)
         
             print(f"Model has {model.num_parameters():,} parameters.")
         
             # --- 4. Load or Create and prepare the training dataset ---
             if args.preprocessed_data_path and os.path.exists(args.preprocessed_data_path):
                 print(f"Loading preprocessed dataset from {args.preprocessed_data_path}...")
         
                 # Synchronization of distributed processes
                 local_rank = int(os.environ.get("LOCAL_RANK", -1))
                 if local_rank != -1:
                     # Introducing a minimal time offset per GPU to avoid I/O collisions.
                     import time
                     time.sleep(local_rank * 0.2)
         
                 lm_dataset = load_from_disk(args.preprocessed_data_path, keep_in_memory=False)
         
             else:
                 print("No preprocessed dataset found, starting from raw data...")
                 raw_dataset = load_dataset(args.dataset_name, name=args.dataset_config, split="train")
         
                 # Tokenization function
                 def tokenize_function(examples):
                     return tokenizer(examples["text"])
         
                 tokenized_dataset = raw_dataset.map(
                     tokenize_function,
                     batched=True,
                     remove_columns=raw_dataset.column_names,
                     desc="Running tokenizer on dataset",
                 )
         
                 # Main data processing function that will concatenate all texts from our dataset
                 # and generate chunks of max_seq_length.
                 def group_texts(examples):
                     # Concatenate all texts.
                     concatenated_examples = {k: [item for sublist in examples[k] for item in sublist] for k in examples.keys()}
                     total_length = len(concatenated_examples[list(examples.keys())[0]])
                     # We drop the small remainder.
                     if total_length >= args.max_seq_length:
                         total_length = (total_length // args.max_seq_length) * args.max_seq_length
                     # Split by chunks of max_len.
                     result = {
                         k: [t[i : i + args.max_seq_length] for i in range(0, total_length, args.max_seq_length)]
                         for k, t in concatenated_examples.items()
                     }
                     result["labels"] = result["input_ids"].copy()
                     return result
         
                 lm_dataset = tokenized_dataset.map(
                     group_texts,
                     batched=True,
                     desc=f"Grouping texts in chunks of {args.max_seq_length}",
                 )
         
         
             # --- 5. Configure Training Arguments ---
             # Check for bfloat16 support
             use_bf16 = torch.cuda.is_available() and torch.cuda.is_bf16_supported()
         
             training_args = TrainingArguments(
                 output_dir=args.output_dir,
                 num_train_epochs=args.num_train_epochs,
                 max_steps=args.max_steps,
                 per_device_train_batch_size=args.per_device_train_batch_size,
                 gradient_accumulation_steps=args.gradient_accumulation_steps,
                 learning_rate=args.learning_rate,
                 logging_steps=args.logging_steps,
                 save_strategy=args.save_strategy,
                 save_steps=args.save_steps,
                 save_total_limit=2, # Optional: Limit the number of checkpoints
                 bf16=use_bf16,
                 fp16=not use_bf16,
                 optim="adamw_torch",
                 lr_scheduler_type="cosine",
                 warmup_ratio=0.03,
                 report_to="tensorboard",
                 gradient_checkpointing=True,
                 # Required for gradient checkpointing with some parallelization strategies
                 gradient_checkpointing_kwargs={"use_reentrant": False},
             )
         
             # --- 6. Create Trainer and Start Training ---
             # Data collator will take care of creating batches for causal language modeling
             data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
         
             trainer = Trainer(
                 model=model,
                 args=training_args,
                 train_dataset=lm_dataset,
                 # eval_dataset=... # Optional: if you have a validation set
                 tokenizer=tokenizer,
                 data_collator=data_collator,
             )
         
             print("Starting training from scratch...")
             trainer.train()
             print("Training finished.")
         
             # --- 7. Save the final model ---
             print(f"Saving final model to {args.output_dir}")
             trainer.save_model()
         
         if __name__ == "__main__":
             main()




### Upload scripts to the Slurm cluster

To upload the scripts that you created in the previous section to the Slurm cluster, follow these steps:

  1. Set the `LOGIN_NODE` variable by retrieving the name of the login node for your cluster:
         
         LOGIN_NODE="$(gcloud compute instances list \
                         --project="${PROJECT_ID}" \
                         --filter="labels.ghpc_deployment='${CLUSTER_NAME}' AND labels.slurm_instance_role='login'" \
                         --format="value(name)" | head -n 1)"

The `LOGIN_NODE` variable stores a value similar to `${CLUSTER_NAME}-login-001`.

  2. Create a firewall rule:
         
         # Identify the VPC network used by the Slurm cluster's login node
         VPC_NETWORK_URI=$(gcloud compute instances describe "${LOGIN_NODE}" \
           --project="${PROJECT_ID}" \
           --zone="${ZONE}" \
           --format="value(networkInterfaces[0].network)")
         CLUSTER_NETWORK=$(basename "${VPC_NETWORK_URI}")
         
         # Create the IAP firewall rule to allow SSH access to the login node
         gcloud compute firewall-rules create "allow-ssh-from-iap-${CLUSTER_NETWORK}" \
           --project="${PROJECT_ID}" \
           --network="${CLUSTER_NETWORK}" \
           --direction=INGRESS \
           --action=allow \
           --rules=tcp:22 \
           --source-ranges=35.235.240.0/20 \
           --description="Allow SSH ingress from Google Cloud Identity-Aware Proxy (IAP)"

  3. Upload your scripts to the login node's home directory:
         
         gcloud compute scp \
           --project="${PROJECT_ID}" \
           --zone="${ZONE}" \
           --tunnel-through-iap \
           ./install_environment.sh \
           ./requirements.txt \
           ./submit.slurm \
           ./accelerate_config.yaml \
           ./train.py \
           ./preprocess_data.py \
           "${LOGIN_NODE}":~/




### Connect to the Slurm cluster

Connect to the Slurm cluster by connecting to the login node through SSH:
    
    
    gcloud compute ssh "${LOGIN_NODE}" \
        --project="${PROJECT_ID}" \
        --tunnel-through-iap \
        --zone="${ZONE}"
        -- -t "export HF_TOKEN='${HF_TOKEN}'; bash -l"

### Install frameworks and tools

After you connect to the login node, install frameworks and tools by doing the following:

  1. Set up a Python virtual environment with all the required dependencies:
         
         chmod +x install_environment.sh
         ./install_environment.sh




## Start your pre-training your workload

To start your training your workload, do the following:

  1. Submit the job to the Slurm scheduler:
         
         sbatch submit.slurm

  2. On the login node in your Slurm cluster, you can monitor the job's progress by checking the output files created in your `home` directory:
         
         tail -f ~/logs/slurm-1.err # (or .out, depending on where the script is currently sending logs)

If your job successfully starts, then the `.err` file shows a progress bar that updates as your job progresses.




## Monitor your workload

You can monitor the use of the GPUs in your Slurm cluster to verify that your fine-tuning job is efficiently running. To do so, open the following link in your browser:
    
    
    https://console.cloud.google.com/monitoring/metrics-explorer?project=PROJECT_ID&pageState=%7B%22xyChart%22%3A%7B%22dataSets%22%3A%5B%7B%22timeSeriesFilter%22%3A%7B%22filter%22%3A%22metric.type%3D%5C%22agent.googleapis.com%2Fgpu%2Futilization%5C%22%20resource.type%3D%5C%22gce_instance%5C%22%22%2C%22perSeriesAligner%22%3A%22ALIGN_MEAN%22%7D%2C%22plotType%22%3A%22LINE%22%7D%5D%7D%7D
    

Alternately, you can enter the command directly in the terminal:
    
    
    open "https://console.cloud.google.com/monitoring/metrics-explorer?project=${PROJECT_ID}&pageState=%7B%22xyChart%22%3A%7B%22dataSets%22%3A%5B%7B%22timeSeriesFilter%22%3A%7B%22filter%22%3A%22metric.type%3D%5C%22agent.googleapis.com%2Fgpu%2Futilization%5C%22%20resource.type%3D%5C%22gce_instance%5C%22%22%2C%22perSeriesAligner%22%3A%22ALIGN_MEAN%22%7D%2C%22plotType%22%3A%22LINE%22%7D%5D%7D%7D"

When you monitor your workload, you can see the following:

  * **GPUs usage** : for a healthy fine-tuning job, you can expect to see the usage of all your 16 GPUs (eight GPUs for each VM in the cluster) rise and stabilize to a specific level throughout your training. TEST

  * **Job duration** : the job should take approximately one hour to complete.




## Download your model

After you have successfully run your job, your trained model is saved in the `~/qwen2-from-scratch-on-smollm-fineweb/` directory on the login node. Because this persistent shared directory is mounted across all of the nodes in your cluster, your model checkpoints remain available even after the job completes or the compute nodes are deallocated.

You can download the saved model from the login node to your local machine by using the `gcloud compute scp` command, as shown in the following example:
    
    
    # From your local machine
    gcloud compute scp --project="${PROJECT_ID}" --zone="${ZONE}" --tunnel-through-iap \
      "${LOGIN_NODE}":~/qwen2-from-scratch-on-smollm-fineweb/ ./qwen2-trained-model/ --recurse

After you download your model, you can do the following:

  * **Load the model for inference** : Use the Hugging Face Transformers framework to load the `qwen2-trained-model/` directory and perform inference with your newly trained Qwen2 model.
  * **Additional fine-tuning** : Use the saved checkpoint as a starting point for additional fine-tuning on a more specific dataset.
  * **Push the model to the Hugging Face Hub** : Share your trained model by pushing it to the Hugging Face Hub.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete your resources

  1. To delete your Slurm cluster, run the [`gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy):
         
         ./gcluster destroy "${CLUSTER_NAME}" --auto-approve

  2. To delete your Cloud Storage bucket, follow these steps:
         
         gcloud storage buckets delete "gs://${GCS_BUCKET}" --quiet || true

  3. To delete a [Packer](https://developer.hashicorp.com/packer/docs) image, open your web browser, navigate to the following page, search for your specific image, and click Delete. 
         
         http://console.cloud.google.com/compute/images

  4. To delete all VPC networks, firewall rules, routers, IPs, and subnets associated with the project, do the following:
         
         echo "========================================================================="
         echo " STARTING AUTOMATED NETWORK CLEANUP FOR CLUSTER: ${CLUSTER_NAME}"
         echo "========================================================================="
         
         echo "Discovering all VPC networks linked to the cluster..."
         NETWORKS=$(gcloud compute networks list --project="${PROJECT_ID}" --format="value(name)" | grep "^${CLUSTER_NAME}" || true)
         
         if [ -z "${NETWORKS}" ]; then
             echo "No VPC networks found starting with ${CLUSTER_NAME}. Everything is already clean!"
             exit 0
         fi
         
         echo "Found the following networks to process:"
         echo "${NETWORKS}"
         echo "-------------------------------------------------------------------------"
         
         echo "=== 1. Wiping Global Firewall Rules ==="
         FIREWALL_RULES=$(gcloud compute firewall-rules list \
             --project="${PROJECT_ID}" \
             --filter="network ~ ^${CLUSTER_NAME} OR name ~ ^${CLUSTER_NAME}" \
             --format="value(name)" || echo "")
         
         if [ -n "${FIREWALL_RULES}" ]; then
             echo "Deleting matching firewall rules:"
             echo "${FIREWALL_RULES}"
             echo "${FIREWALL_RULES}" | xargs -r gcloud compute firewall-rules delete --project="${PROJECT_ID}" --quiet
         else
             echo "No matching firewall rules found."
         fi
         
         echo "=== 2. Tearing Down Network-Specific Infrastructure ==="
         echo "${NETWORKS}" | while read -r net_name; do
             [ -z "${net_name}" ] && continue
             echo "Processing resources for network: ${net_name}"
         
             ROUTERS=$(gcloud compute routers list \
                 --project="${PROJECT_ID}" \
                 --regions="${REGION}" \
                 --filter="network=${net_name}" \
                 --format="value(name)" || echo "")
         
             if [ -n "${ROUTERS}" ]; then
                 echo "  -> Deleting routers: ${ROUTERS}"
                 echo "${ROUTERS}" | xargs -r gcloud compute routers delete --region="${REGION}" --project="${PROJECT_ID}" --quiet
             fi
         
             IPS=$(gcloud compute addresses list \
                 --project="${PROJECT_ID}" \
                 --regions="${REGION}" \
                 --filter="name ~ ^${net_name}" \
                 --format="value(name)" || echo "")
         
             if [ -n "${IPS}" ]; then
                 echo "  -> Deleting IP reservations: ${IPS}"
                 echo "${IPS}" | xargs -r gcloud compute addresses delete --region="${REGION}" --project="${PROJECT_ID}" --quiet
             fi
         
             SUBNETS=$(gcloud compute networks subnets list \
                 --project="${PROJECT_ID}" \
                 --regions="${REGION}" \
                 --filter="network=${net_name}" \
                 --format="value(name)" || echo "")
         
             if [ -n "${SUBNETS}" ]; then
                 echo "  -> Deleting subnetworks:"
                 echo "${SUBNETS}"
                 echo "${SUBNETS}" | xargs -r gcloud compute networks subnets delete --region="${REGION}" --project="${PROJECT_ID}" --quiet
             fi
         done
         
         echo "-------------------------------------------------------------------------"
         echo "Waiting 15 seconds for Google Cloud API dependencies to unlock..."
         sleep 15
         
         echo "=== 3. Final VPC Networks Destruction ==="
         echo "${NETWORKS}" | while read -r net_name; do
             [ -z "${net_name}" ] && continue
             echo "Deleting core VPC network: ${net_name}..."
             gcloud compute networks delete "${net_name}" --project="${PROJECT_ID}" --quiet || \
             echo "Warning: Could not delete ${net_name} yet. If a lock occurred, please rerun in 1 minute."
         done
         
         echo "========================================================================="
         echo " SUCCESS: All network resources for cluster ${CLUSTER_NAME} have been wiped!"
         echo "========================================================================="




### Delete your project

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

## What's next

  * [Redeploy a Slurm cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-fully-managed-slurm-cluster#redeploy-slurm-cluster)

  * [Test network performance on a Slurm cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-slurm)

  * [Monitor VMs in a Slurm cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor)

  * [Learn about recommended storage services for AI and ML workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/storage)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
