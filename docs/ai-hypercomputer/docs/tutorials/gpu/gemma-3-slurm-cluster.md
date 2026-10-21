---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gemma-3-slurm-cluster/
title: Fine-tune Gemma 3 on an A4 Slurm cluster \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:28:11.777431+00:00
---

# Fine-tune Gemma 3 on an A4 Slurm cluster  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gemma-3-slurm-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Fine-tune Gemma 3 on an A4 Slurm cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This tutorial shows you how to fine-tune the [Gemma 3](https://ai.google.dev/gemma/docs/core) large language model (LLM) on a multi-node Slurm cluster that uses two A4 virtual machine (VM) instances. As part of this tutorial, you do the following:

  * Create a custom image.

  * Configure an RDMA network.

  * Run a distributed fine-tuning job. For efficient multi-node training, you use the [Hugging Face Accelerate library with Fully Sharded Data Parallel (FSDP)](https://huggingface.co/docs/accelerate/en/usage_guides/fsdp).


**Important:** To complete this tutorial, you must have reserved the capacity to create two A4 VMs. To learn more about your options for reserving capacity in AI Hypercomputer for a future date and time, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

This tutorial is intended for machine learning (ML) engineers, platform administrators and operators, and for data and AI specialists who are interested in using Slurm job scheduling capabilities to handle fine-tuning workloads.

## Objectives

  1. Access Gemma 3 by using Hugging Face.

  2. Prepare your environment.

  3. Create an A4 Slurm cluster.

  4. Prepare your workload.

  5. Run a fine-tuning job.

  6. Monitor your job.

  7. Clean up.




## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Compute Engine](https://cloud.google.com/compute/gpus-pricing)
  * [ Google Kubernetes Engine (GKE) Enterprise edition](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [ Filestore](https://docs.cloud.google.com/filestore#pricing)
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

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: ` roles/compute.admin, roles/iam.serviceAccountUser, roles/file.editor, roles/storage.admin, roles/serviceusage.serviceUsageAdmin `
         
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

**Note** : If you use a local shell and an external identity provider (IdP), and you encounter an authentication error after running the preceding command, then [sign in to the Google Cloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 
  18. Enable OS Login for your project: 
         
         gcloud compute project-info add-metadata --metadata=enable-oslogin=TRUE

  19. [Sign in to or create a Hugging Face account](https://huggingface.co/login).



## Access Gemma 3 by using Hugging Face

To use Hugging Face to access Gemma 3, follow these steps:

  1. [Sign the consent agreement to use Gemma 3 12B](https://huggingface.co/google/gemma-3-12b-pt).

  2. [Create a Hugging Face `read` access token](https://huggingface.co/docs/hub/security-tokens#how-to-manage-user-access-tokens). Click **Your Profile > Settings > Access tokens > +Create new token**

  3. Copy and save the `read` access token value. You use it later in this tutorial.




## Install Cluster Toolkit

For more information about using the [`gcluster` CLI](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster) and managing clusters, see the [Cluster Toolkit overview](https://docs.cloud.google.com/cluster-toolkit/docs/overview).

  1. Prepare the Cluster Toolkit version:
         
         # Find all available releases at: https://github.com/GoogleCloudPlatform/cluster-toolkit/releases
         # Set the desired version TAG (e.g., v1.97.0)
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
         export ZONE="YOUR_ZONE"
         export REGION="YOUR_REGION"
         export RESERVATION_URL="YOUR_RESERVATION_NAME"
         export CLUSTER_NAME="YOUR_CLUSTER_NAME"
         export BUCKET_NAME="YOUR_GCS_BUCKET"
         export HF_TOKEN="YOUR_HF_TOKEN"
         
         gcloud config set project "${PROJECT_ID}"
         gcloud config set billing/quota_project "${PROJECT_ID}"

Replace the following:

     * `YOUR_PROJECT_ID`: the ID of the Google Cloud project where you want to create your Cloud Storage bucket.

     * `YOUR_ZONE`: the zone where your reservation exists.

     * `YOUR_REGION`: the region where your reservation exists.

     * `YOUR_RESERVATION_NAME`: the URL or the name of the reservation that you want to use to create your Slurm cluster.

     * `YOUR_CLUSTER_NAME`: the name of the Slurm cluster that you want to create.

     * `YOUR_GCS_BUCKET`: a name for your Cloud Storage bucket that follows [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).

     * `YOUR_HF_TOKEN`: the Hugging Face access token that you created in the previous section.

  2. Create a Cloud Storage bucket:
         
         gcloud storage buckets create "gs://${BUCKET_NAME}" \
           --project="${PROJECT_ID}"




## Create an A4 Slurm cluster

To create an A4 Slurm cluster, follow these steps:

  1. Create the `a4high-slurm-deployment.yaml` file:
         
         MANIFEST_PATH="${CLUSTER_TOOLKIT_PATH}/examples/machine-learning/a4-highgpu-8g"
         cat <<EOF > "${MANIFEST_PATH}/a4high-slurm-deployment.yaml"
         terraform_backend_defaults:
           type: gcs
           configuration:
             bucket: ${BUCKET_NAME}
         
         vars:
           deployment_name: ${CLUSTER_NAME}
           project_id: ${PROJECT_ID}
           region: ${REGION}
           zone: ${ZONE}
           a4h_cluster_size: 2
           a4h_reservation_name: ${RESERVATION_URL}
         EOF

  2. Prepare the manifests:

     1. Use the [`gcluster create` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-create) to create the Terraform manifests:
            
            gcluster create \
              -d "${MANIFEST_PATH}/a4high-slurm-deployment.yaml" \
              "${MANIFEST_PATH}/a4high-slurm-blueprint.yaml"

     2. Patch the manifests:
            
            echo "[$(date)] Patching Filestore deletion protection in ${CLUSTER_NAME}..."
            sed -i '/deletion_protection = {/,/}/ { s/enabled = true/enabled = false/; /reason  = "Avoid data loss"/d; }' "${CLUSTER_NAME}/cluster-env/main.tf"

  3. Deploy the cluster:
         
         gcluster deploy "${CLUSTER_NAME}" --auto-approve

The [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) is a two-phase process, which is as follows:

     * The first phase builds a custom image with all software pre-installed, which can take up to 45 minutes to complete.

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

To create the scripts that your fine-tuning workload will use, follow these steps:

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
         
         # Default configuration for a 2-node, 8-GPU-per-node (16 total GPUs) FSDP training job.
         
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
           fsdp_state_dict_type: "FULL_STATE_DICT"
           fsdp_transformer_layer_cls_to_wrap: "Gemma3DecoderLayer"
           fsdp_use_orig_params: true
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
         
         #!/bin/bash
         #SBATCH --job-name=gemma3-finetune
         #SBATCH --nodes=2
         #SBATCH --ntasks-per-node=1 # 1 task per node
         #SBATCH --gpus-per-node=8   # 8 GPUs per node
         #SBATCH --partition=a4high
         #SBATCH --output=slurm-%j.out
         #SBATCH --error=slurm-%j.err
         
         set -e
         echo "--- Slurm Job Started ---"
         
         # --- STAGE 1: Copy Environment to Local SSD on all nodes ---
         srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 bash -c '
           echo "Setting up local environment on $(hostname)..."
           LOCAL_VENV="/mnt/localssd/venv_job_${SLURM_JOB_ID}"
           LOCAL_CACHE="/mnt/localssd/hf_cache_job_${SLURM_JOB_ID}"
           rsync -a --info=progress2 ~/./.venv/ ${LOCAL_VENV}/
           mkdir -p ${LOCAL_CACHE}
           echo "Setup on $(hostname) complete."
         '
         
         # --- STAGE 2: Run the Training Job using the Local Environment ---
         echo "--- Starting Training ---"
         
         LOCAL_VENV="/mnt/localssd/venv_job_${SLURM_JOB_ID}"
         LOCAL_CACHE="/mnt/localssd/hf_cache_job_${SLURM_JOB_ID}"
         LOCAL_OUTPUT_DIR="/mnt/localssd/outputs_${SLURM_JOB_ID}"
         mkdir -p ${LOCAL_OUTPUT_DIR}
         
         # This is the main training command.
         srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 bash -c '
           # Ensure nccl-gib is at version 1.1.2-1
           INSTALLED_VERSION=$(dpkg-query -W -f="\${Version}" nccl-gib 2>/dev/null || echo "not_installed")
           if [ "${INSTALLED_VERSION}" != "1.1.2-1" ]; then
             echo "Upgrading nccl-gib to 1.1.2-1..."
             sudo apt-get update && sudo apt-get install -y --allow-change-held-packages nccl-gib=1.1.2-1
           fi
         
           source '"${LOCAL_VENV}"'/bin/activate
         
           export HF_HOME='"${LOCAL_CACHE}"'
           export HF_DATASETS_CACHE='"${LOCAL_CACHE}"'
         
           if [ -f /usr/local/gib/scripts/set_nccl_env.sh ]; then
             echo "Sourcing set_nccl_env.sh"
             source /usr/local/gib/scripts/set_nccl_env.sh
           fi
           export LD_LIBRARY_PATH=/usr/local/gib/lib64:${LD_LIBRARY_PATH:-}
         
           export MASTER_ADDR=$(scontrol show hostnames "$SLURM_JOB_NODELIST" | head -n 1)
           export MASTER_PORT=29500
         
           # Use accelerate launch to properly run the distributed FSDP job
           accelerate launch \
             --config_file ~/accelerate_config.yaml \
             --machine_rank $SLURM_NODEID \
             --main_process_ip $MASTER_ADDR \
             --main_process_port $MASTER_PORT \
             --num_machines $SLURM_NNODES \
             --num_processes $((SLURM_NNODES * 8)) \
             ~/train.py \
             --model_id google/gemma-3-12b-pt \
             --output_dir '"${LOCAL_OUTPUT_DIR}"' \
             --per_device_train_batch_size 1 \
             --gradient_accumulation_steps 8 \
             --num_train_epochs 3 \
             --learning_rate 1e-5 \
             --save_strategy steps \
             --save_steps 100
         '
         
         # --- STAGE 3: Copy Final Model from Local SSD to Home Directory ---
         echo "--- Copying final model from local SSD to /home ---"
         # This command runs only on the first node of the job allocation
         # and copies the final model back to the persistent shared directory.
         srun --nodes=1 --ntasks=1 --ntasks-per-node=1 bash -c "
           rsync -a --info=progress2 ${LOCAL_OUTPUT_DIR}/ ~/gemma-12b-text-to-sql-finetuned/
         "
         
         echo "--- Slurm Job Finished ---"

  4. To specify the dependencies for your fine-tuning job, create the `requirements.txt` file with the following content:
         
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

**Note:** This tutorial doesn't use the latest versions of NVIDIA and Pytorch dependencies. If you need newer dependencies, then see the [NVIDIA documentation](https://developer.nvidia.com/cuda-gpus) and the [Pytorch documentation](https://pytorch.org/get-started/locally/#linux-pip).
  5. To specify the instructions for your job, create the `train.py` file with the following content:
         
         import torch
         import argparse
         from datasets import load_dataset
         from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, AutoConfig
         from peft import LoraConfig, prepare_model_for_kbit_training, get_peft_model
         from trl import SFTTrainer, SFTConfig
         from huggingface_hub import login
         
         
         def get_args():
             parser = argparse.ArgumentParser()
             parser.add_argument("--model_id", type=str, default="google/gemma-3-12b-pt", help="Hugging Face model ID")
             parser.add_argument("--hf_token", type=str, default=None, help="Hugging Face token for private models")
             parser.add_argument("--dataset_name", type=str, default="philschmid/gretel-synthetic-text-to-sql", help="Hugging Face dataset name")
             parser.add_argument("--output_dir", type=str, default="gemma-12b-text-to-sql", help="Directory to save model checkpoints")
         
             # LoRA arguments
             parser.add_argument("--lora_r", type=int, default=16, help="LoRA attention dimension")
             parser.add_argument("--lora_alpha", type=int, default=16, help="LoRA alpha scaling factor")
             parser.add_argument("--lora_dropout", type=float, default=0.05, help="LoRA dropout probability")
         
             # SFTConfig arguments
             parser.add_argument("--max_seq_length", type=int, default=512, help="Maximum sequence length")
             parser.add_argument("--num_train_epochs", type=int, default=3, help="Number of training epochs")
             parser.add_argument("--per_device_train_batch_size", type=int, default=8, help="Batch size per device during training")
             parser.add_argument("--gradient_accumulation_steps", type=int, default=1, help="Gradient accumulation steps")
             parser.add_argument("--learning_rate", type=float, default=1e-5, help="Learning rate")
             parser.add_argument("--logging_steps", type=int, default=10, help="Log every X steps")
             parser.add_argument("--save_strategy", type=str, default="steps", help="Checkpoint save strategy")
             parser.add_argument("--save_steps", type=int, default=100, help="Save checkpoint every X steps")
         
             return parser.parse_args()
         
         def main():
             args = get_args()
         
             # --- 1. Setup and Login ---
             if args.hf_token:
                 login(args.hf_token)
         
             # --- 2. Create and prepare the fine-tuning dataset ---
             # The SFTTrainer will use the `formatting_func` to apply the chat template.
             dataset = load_dataset(args.dataset_name, split="train")
             dataset = dataset.shuffle().select(range(12500))
             dataset = dataset.train_test_split(test_size=2500/12500)
         
             # --- 3. Configure Model and Tokenizer ---
             if torch.cuda.is_available() and torch.cuda.get_device_capability()[0] >= 8:
                 torch_dtype_obj = torch.bfloat16
                 torch_dtype_str = "bfloat16"
             else:
                 torch_dtype_obj = torch.float16
                 torch_dtype_str = "float16"
         
             tokenizer = AutoTokenizer.from_pretrained(args.model_id)
             tokenizer.pad_token = tokenizer.eos_token
         
             gemma_chat_template = (
                 "{% for message in messages %}"
                 "{% if message['role'] == 'user' %}"
                 "{{ '<start_of_turn>user\n' + message['content'] + '<end_of_turn>\n' }}"
                 "{% elif message['role'] == 'assistant' %}"
                 "{{ '<start_of_turn>model\n' + message['content'] + '<end_of_turn>\n' }}"
                 "{% endif %}"
                 "{% endfor %}"
                 "{% if add_generation_prompt %}"
                 "{{ '<start_of_turn>model\n' }}"
                 "{% endif %}"
             )
             tokenizer.chat_template = gemma_chat_template
         
             # --- 4. Define the Formatting Function ---
             # This function will be used by the SFTTrainer to format each sample
             # from the dataset into the correct chat template format.
             def formatting_func(example):
                 # The create_conversation logic is now implicitly handled by this.
                 # We need to construct the messages list here.
                 system_message = "You are a text to SQL query translator. Users will ask you questions in English and you will generate a SQL query based on the provided SCHEMA."
                 user_prompt = "Given the <USER_QUERY> and the <SCHEMA>, generate the corresponding SQL command to retrieve the desired data, considering the query's syntax, semantics, and schema constraints.\n\n<SCHEMA>\n{context}\n</SCHEMA>\n\n<USER_QUERY>\n{question}\n</USER_QUERY>\n"
         
                 messages = [
                     {"role": "system", "content": system_message},
                     {"role": "user", "content": user_prompt.format(question=example["sql_prompt"], context=example["sql_context"])},
                     {"role": "assistant", "content": example["sql"]}
                 ]
                 return tokenizer.apply_chat_template(messages, tokenize=False)
         
             # --- 5. Load Quantized Model and Apply PEFT ---
         
             # Define the quantization configuration
             config = AutoConfig.from_pretrained(args.model_id)
             config.use_cache = False
         
             # Load the base model in native precision
             print("Loading base model...")
             model = AutoModelForCausalLM.from_pretrained(
                 args.model_id,
                 config=config,
                 attn_implementation="sdpa",
                 torch_dtype=torch_dtype_obj,
             )
         
             # Configure LoRA.
             peft_config = LoraConfig(
                 lora_alpha=args.lora_alpha,
                 lora_dropout=args.lora_dropout,
                 r=args.lora_r,
                 bias="none",
                 target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
                 task_type="CAUSAL_LM",
             )
         
             # Apply the PEFT config to the model
             print("Applying PEFT configuration...")
             model = get_peft_model(model, peft_config)
             model.print_trainable_parameters()
         
             # --- 6. Configure Training Arguments ---
             training_args = SFTConfig(
                 output_dir=args.output_dir,
                 ddp_timeout=300.0,
                 max_seq_length=args.max_seq_length,
                 num_train_epochs=args.num_train_epochs,
                 per_device_train_batch_size=args.per_device_train_batch_size,
                 gradient_accumulation_steps=args.gradient_accumulation_steps,
                 learning_rate=args.learning_rate,
                 logging_steps=args.logging_steps,
                 save_strategy=args.save_strategy,
                 save_steps=args.save_steps,
                 packing=False,
                 gradient_checkpointing=True,
                 gradient_checkpointing_kwargs={"use_reentrant": False},
                 optim="adamw_torch",
                 fp16=True if torch_dtype_obj == torch.float16 else False,
                 bf16=True if torch_dtype_obj == torch.bfloat16 else False,
                 max_grad_norm=0.3,
                 warmup_ratio=0.03,
                 lr_scheduler_type="constant",
                 push_to_hub=False,
                 report_to="tensorboard",
                 dataset_kwargs={
                     "add_special_tokens": False,
                     "append_concat_token": True,
                 }
             )
         
             # --- 7. Create Trainer and Start Training ---
             trainer = SFTTrainer(
                 model=model,
                 args=training_args,
                 train_dataset=dataset["train"],
                 eval_dataset=dataset["test"],
                 formatting_func=formatting_func,
             )
         
             print("Starting training...")
             trainer.train()
             print("Training finished.")
         
             # --- 8. Save the final model ---
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

  2. Upload your scripts to the login node's home directory:
         
         gcloud compute scp \
           --project="${PROJECT_ID}" \
           --zone="${ZONE}" \
           --tunnel-through-iap \
           ./install_environment.sh \
           ./requirements.txt \
           ./submit.slurm \
           ./accelerate_config.yaml \
           ./train.py \
           "${LOGIN_NODE}":~/




### Connect to the Slurm cluster

Connect to the login node, and propagate your Hugging Face token to the new session:
    
    
    gcloud compute ssh "${LOGIN_NODE}" \
        --project="${PROJECT_ID}" \
        --tunnel-through-iap \
        --zone="${ZONE}" \
        -- -t "export HF_TOKEN='${HF_TOKEN}'; bash -l"

### Install frameworks and tools

After connecting to the login node, set up a Python virtual environment with the required dependencies:
    
    
    chmod +x install_environment.sh
    ./install_environment.sh

## Start your fine-tuning workload

To start your fine-tuning workload, follow these steps:

  1. Submit the job to the Slurm scheduler and collect the Job ID:
         
         JOB_ID="$(sbatch submit.slurm 2>&1 \
           | tee /dev/tty \
           | grep -oP 'Submitted batch job \K\d+')"

  2. On the login node in your Slurm cluster, you can monitor the job's progress by checking the output files created in your `home` directory:
         
         tail -f "slurm-${JOB_ID}.out" "slurm-${JOB_ID}.err"

If your job successfully starts, then the `.err` file shows a progress bar that updates as your job progresses.




## Monitor your workload

You can monitor the use of the GPUs in your Slurm cluster to verify that your fine-tuning job is efficiently running. To do so, open the following link in your browser:
    
    
    https://console.cloud.google.com/monitoring/metrics-explorer?project=PROJECT_ID&pageState=%7B%22xyChart%22%3A%7B%22dataSets%22%3A%5B%7B%22timeSeriesFilter%22%3A%7B%22filter%22%3A%22metric.type%3D%5C%22agent.googleapis.com%2Fgpu%2Futilization%5C%22%20resource.type%3D%5C%22gce_instance%5C%22%22%2C%22perSeriesAligner%22%3A%22ALIGN_MEAN%22%7D%2C%22plotType%22%3A%22LINE%22%7D%5D%7D%7D
    

When you monitor your workload, you can see the following:

  * **GPU usage** : for a healthy fine-tuning job, you can expect to see the usage of all your 16 GPUs (eight GPUs for each VM in the cluster) rise and stabilize to a specific level throughout your training.

  * **Job duration** : the job should take approximately one hour to complete.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete your Slurm cluster

To delete your Slurm cluster, run the [`gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy):
    
    
    gcluster destroy "${CLUSTER_NAME}" --auto-approve

If you need to delete all VPC networks, firewall rules, routers, IPs, and subnets associated with the project, do the following:
    
    
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

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
