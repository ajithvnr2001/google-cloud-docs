---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/fsdp-mixtral-8x7b/
title: Use FSDP to fine-tune Mixtral-8x7B on an A4 Slurm cluster \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:55:09.064098+00:00
---

# Use FSDP to fine-tune Mixtral-8x7B on an A4 Slurm cluster  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/fsdp-mixtral-8x7b/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Use FSDP to fine-tune Mixtral-8x7B on an A4 Slurm cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This tutorial shows you how to fine-tune a [`mistralai/Mixtral-8x7B-v0.1`](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1) model on a multi-node, multi-GPU Slurm cluster on Google Cloud. The cluster uses two `a4-highgpu-8g` virtual machine (VM) instances, which each have 8 NVIDIA B200 GPUs.

The two main processes described in this tutorial are as follows:

  1. Deploy a production-grade, high-performance Slurm cluster by using the Google Cloud Cluster Toolkit. As part of this deployment, you create a custom VM image with the necessary software pre-installed. You also set up a shared Lustre file system and configure high-speed networking.
  2. After the cluster is deployed, you run a distributed fine-tuning job by using the set of scripts that accompany this tutorial. The job leverages PyTorch Fully Sharded Data Parallel (FSDP), which you access through the Hugging Face [Transformer Reinforcement Learning](https://github.com/huggingface/trl) [(TRL)](https://github.com/huggingface/trl) library.

**Important:** To complete this tutorial, you must have reserved the capacity to create two A4 VMs. To learn more about your options for reserving capacity in AI Hypercomputer for a future date and time, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

This tutorial is intended for machine learning (ML) engineers, researchers, platform administrators and operators, and data and AI specialists who are interested in distributing an AI workload across multiple nodes and GPUs.

## Objectives

  * Access Mixtral by using Hugging Face
  * Install Cluster Toolkit
  * Prepare your environment
  * Create and deploy a production-grade A4 High-GPU Slurm cluster.
  * Configure a multi-node environment for distributed training with FSDP.
  * Fine-tune the Mixtral model by using the Hugging Face `trl.SFTTrainer` class.
  * Stage data to local SSDs.
  * Monitor your job.
  * Clean up.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Compute Engine](https://cloud.google.com/compute/all-pricing)
  * [ Cloud Storage](https://docs.cloud.google.com/storage/pricing)
  * [ Cloud Logging](https://docs.cloud.google.com/logging#pricing)
  * [ Google Cloud Managed Lustre](https://docs.cloud.google.com/managed-lustre#pricing)



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
         
         gcloud services enable compute.googleapis.com file.googleapis.com logging.googleapis.com cloudresourcemanager.googleapis.com servicenetworking.googleapis.com lustre.googleapis.com

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
         
         gcloud services enable compute.googleapis.com file.googleapis.com logging.googleapis.com cloudresourcemanager.googleapis.com servicenetworking.googleapis.com lustre.googleapis.com

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
  20. [ Install the dependencies that you need to use the Cluster Toolkit](https://cloud.google.com/cluster-toolkit/docs/setup/install-dependencies).



## Access Mixtral by using Hugging Face

To use Hugging Face to access Mixtral, do the following:

  1. [Sign in to Hugging Face and explore the Mixtral model](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1).
  2. [Create a Hugging Face `read` access token](https://huggingface.co/docs/hub/security-tokens#how-to-manage-user-access-tokens).
  3. Copy and save the token value. You use it later in this tutorial.



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
         export ZONE="YOUR_ZONE"
         export REGION="YOUR_REGION"
         export RESERVATION_NAME="YOUR_RESERVATION_NAME"
         export DEPLOYMENT_NAME="YOUR_CLUSTER_NAME"
         export BUCKET_NAME="YOUR_GCS_BUCKET"
         export HF_TOKEN="YOUR_HF_TOKEN"

Replace the following:

     * `YOUR_PROJECT_ID`: the name of the Google Cloud project where you want to create your Slurm cluster.
     * `YOUR_ZONE`: the zone where your reservation exists.
     * `YOUR_REGION`: the region where your reservation exists.
     * `YOUR_RESERVATION_NAME`: the URL or the name of the reservation that you want to use to create your Slurm cluster.
     * `YOUR_CLUSTER_NAME`: the name of your deployment. Use a short name containing only letters and numbers (for example, `a4high`). This name is also assigned to the Slurm cluster created by the deployment.
     * `YOUR_GCS_BUCKET`: the name of the bucket where you store the results from the training checkpoint. Specify an existing bucket or create a new one. Before you create it, familiarize yourself with [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).
     * `YOUR_HF_TOKEN`: the Hugging Face token that you created in an earlier step.
  2. Create a Cloud Storage bucket:
         
         gcloud storage buckets create "gs://${BUCKET_NAME}" \
           --project="${PROJECT_ID}"




## Create an A4 Slurm cluster

To create an A4 Slurm cluster, do the following:

  1. Overwrite the `a4high-slurm-deployment.yaml` file in the `examples/machine-learning/a4-highgpu-8g` directory with your environment variables by running the following command:
         
         MANIFEST_PATH="${CLUSTER_TOOLKIT_PATH}/examples/machine-learning/a4-highgpu-8g"
         cat <<EOF > "${MANIFEST_PATH}/a4high-slurm-deployment.yaml"
         terraform_backend_defaults:
           type: gcs
           configuration:
             bucket: ${BUCKET_NAME}
         
         vars:
           deployment_name: ${DEPLOYMENT_NAME}
           project_id: ${PROJECT_ID}
           region: ${REGION}
           zone: ${ZONE}
           a4h_cluster_size: 2
           a4h_reservation_name: ${RESERVATION_NAME}
         EOF

  2. Open the `a4high-slurm-blueprint.yaml` file in the `examples/machine-learning/a4-highgpu-8g` directory, and edit it to use Managed Lustre for the shared `/home` directory as follows:

     * Remove the default `homefs` module block with `source: modules/file-system/filestore`.
     * Enable the `lustrefs` (`homefs` block with `remote_mount: lustrefs`) and `private-service-access` modules.
     * In the `vars` block, configure the following: 
       1. Change the value for `install_managed_lustre` in `/var/tmp/slurm_vars.json` to `true`.
       2. Set `per_unit_storage_throughput` parameter to `500`.
       3. Set `lustre_size_gib` parameter to `36000`.
       4. Uncomment `lustre_instance_id: lustre-instance`.
       5. Comment out or remove unused `filestore_ip_range`.
  3. Deploy the cluster:
         
         ./gcluster deploy \
           -d "${MANIFEST_PATH}/a4high-slurm-deployment.yaml" \
           "${MANIFEST_PATH}/a4high-slurm-blueprint.yaml" \
           --auto-approve

The [`./gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) starts a two-phase process, which is as follows:

     * The first phase builds a custom image with all software pre-installed, which can take up to 35 minutes to complete.
     * The second phase deploys the cluster by using that custom image. This process should complete more quickly than the first phase.



## Prepare your workload

To prepare your workload, follow these steps:

  1. Create workload scripts.

  2. Upload scripts to the Slurm cluster.

  3. Connect to the Slurm cluster .

  4. Install frameworks and tools.




## Create workload scripts

To create the scripts that your fine-tuning workload will use, follow these steps:

  1. To set up the Python virtual environment, create the `install_environment.sh` file with the following content:
         
         #!/bin/bash
         # This script sets a reliable environment for FSDP training.
         # It is meant to be run on a compute node.
         set -e
         
         # --- 1. Create the Python virtual environment ---
         VENV_PATH="$HOME/.venv/venv-fsdp"
         if [ ! -d "$VENV_PATH" ]; then
           echo "--- Creating Python virtual environment at $VENV_PATH ---"
           python3 -m venv $VENV_PATH
         else
           echo "--- Virtual environment already exists at $VENV_PATH ---"
         fi
         
         source $VENV_PATH/bin/activate
         
         # --- 2. Install Dependencies ---
         echo "--- [STEP 2.1] Upgrading build toolchain ---"
         pip install --upgrade pip wheel packaging
         
         echo "--- [STEP 2.2] Installing PyTorch Nightly ---"
         pip install --force-reinstall --pre torch --index-url https://download.pytorch.org/whl/nightly/cu128
         
         echo "--- [STEP 2.3] Installing application dependencies ---"
         if [ -f "requirements-fsdp.txt" ]; then
             pip install -r requirements-fsdp.txt
         else
             echo "ERROR: requirements-fsdp.txt not found!"
             exit 1
         fi
         
         # --- [STEP 2.4] Build Flash Attention from Source ---
         echo "--- Building flash-attn from source... This will take a while. ---"
         # Bypass PyTorch CUDA version mismatch check for extension builds
         python3 -c "
         import torch.utils.cpp_extension as ce
         p = ce.__file__
         content = open(p).read().replace('raise RuntimeError(CUDA_MISMATCH_MESSAGE', 'pass # raise RuntimeError')
         open(p, 'w').write(content)
         "
         
         # Use all available CPU cores to speed up the build
         MAX_JOBS=$(nproc) pip install flash-attn --no-build-isolation
         
         # --- 3. Download the Model ---
         echo "--- [STEP 2.5] Downloading Mixtral model ---"
         if [ -z "$HF_TOKEN" ]; then
           echo "ERROR: The HF_TOKEN environment variable is not set."; exit 1;
         fi
         pip install huggingface_hub[cli]
         
         # Execute the CLI using its full, explicit path
         $VENV_PATH/bin/hf download mistralai/Mixtral-8x7B-v0.1 --local-dir ~/Mixtral-8x7B-v0.1 --token $HF_TOKEN
         
         echo "--- Environment setup complete. ---"

**Note:** This tutorial doesn't use the latest versions of NVIDIA and PyTorch dependencies. If you need newer dependencies, then see the [NVIDIA documentation](https://developer.nvidia.com/cuda-gpus) and the [Pytorch documentation](https://pytorch.org/get-started/locally/#linux-pip).
  2. To specify the Python dependencies for the training script, create a `requirements-fsdp.txt` file with the following content:
         
         transformers==4.55.0
         datasets==4.0.0
         peft==0.16.0
         accelerate==1.9.0
         trl==0.21.0
         
         # Other dependencies
         sentencepiece==0.2.0
         protobuf==6.31.1

  3. Specify `train-mixtral.py` as the main training script:
         
         import torch
         from torch.distributed.fsdp import MixedPrecision
         from datasets import load_dataset
         import shutil
         import os
         import torch.distributed as dist
         
         from peft import LoraConfig, PeftModel, get_peft_model
         from transformers import (
             AutoModelForCausalLM,
             AutoTokenizer,
             TrainingArguments,
             HfArgumentParser,
         )
         
         from torch.distributed import get_rank, get_world_size
         
         from transformers.models.mixtral.modeling_mixtral import MixtralDecoderLayer
         from trl import SFTTrainer
         from dataclasses import dataclass, field
         from typing import Optional
         
         @dataclass
         class ScriptArguments:
             model_id: str = field(default="mistralai/Mixtral-8x7B-v0.1", metadata={"help": "Hugging Face model ID from the Hub"})
             dataset_name: str = field(default="philschmid/gretel-synthetic-text-to-sql", metadata={"help": "Dataset from the Hub"})
             run_inference_after_training: bool = field(default=False, metadata={"help": "Run sample inference on rank 0 after training"})
             dataset_subset_size: Optional[int] = field(default=None, metadata={"help": "Number of samples to use from the dataset for training. If None, uses the full dataset."})
         
         @dataclass
         class PeftArguments:
             lora_r: int = field(default=16, metadata={"help": "LoRA attention dimension"})
             lora_alpha: int = field(default=32, metadata={"help": "LoRA alpha scaling factor"})
             lora_dropout: float = field(default=0.05, metadata={"help": "LoRA dropout probability"})
         
         @dataclass
         class SftTrainingArguments(TrainingArguments):
             max_length: Optional[int] = field(default=2048, metadata={"help": "The maximum sequence length for SFTTrainer"})
             packing: Optional[bool] = field(default=False, metadata={"help": "Enable packing for SFTTrainer"})
             ddp_find_unused_parameters: Optional[bool] = field(default=False, metadata={"help": "When using FSDP activation checkpointing, this must be set to False for Mixtral"})
         
         def formatting_prompts_func(example):
             system_message = "You are a text to SQL query translator. Users will ask you questions in English and you will generate a SQL query based on the provided SCHEMA."
             user_prompt = f"### SCHEMA:\n{example['sql_context']}\n\n### USER QUERY:\n{example['sql_prompt']}"
             response = f"\n\n### SQL QUERY:\n{example['sql']}"
             return f"{system_message}\n\n{user_prompt}{response}"
         
         def main():
             parser = HfArgumentParser((ScriptArguments, PeftArguments, SftTrainingArguments))
             script_args, peft_args, training_args = parser.parse_args_into_dataclasses()
         
             training_args.gradient_checkpointing = True
             training_args.gradient_checkpointing_kwargs = {"use_reentrant": True}
         
             training_args.optim = "adamw_torch_fused"
         
             bf16_policy = MixedPrecision(
                 param_dtype=torch.bfloat16,
                 reduce_dtype=torch.bfloat16,
                 buffer_dtype=torch.bfloat16,
             )
         
             training_args.fsdp = "full_shard"
             training_args.fsdp_config = {
                 "fsdp_auto_wrap_policy": "TRANSFORMER_BASED_WRAP",
                 "fsdp_transformer_layer_cls_to_wrap": [MixtralDecoderLayer],
                 "fsdp_state_dict_type": "SHARDED_STATE_DICT",
                 "fsdp_offload_params": False,
                 "fsdp_forward_prefetch": True,
                 "fsdp_mixed_precision_policy": bf16_policy
             }
         
             tokenizer = AutoTokenizer.from_pretrained(script_args.model_id, trust_remote_code=True)
         
             tokenizer.pad_token = tokenizer.eos_token
             tokenizer.padding_side = "right"
         
             model = AutoModelForCausalLM.from_pretrained(
                 script_args.model_id,
                 torch_dtype=torch.bfloat16,
                 trust_remote_code=True,
                 attn_implementation="flash_attention_2",
             )
         
             peft_config = LoraConfig(
                 r=peft_args.lora_r,
                 lora_alpha=peft_args.lora_alpha,
                 lora_dropout=peft_args.lora_dropout,
                 bias="none",
                 task_type="CAUSAL_LM",
                 target_modules=["q_proj", "v_proj", "k_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
             )
         
             model = get_peft_model(model, peft_config)
         
             data_splits = load_dataset(script_args.dataset_name)
         
             dataset = data_splits["train"]
             eval_dataset = data_splits["test"]
         
             if script_args.dataset_subset_size is not None:
                 dataset = dataset.select(range(script_args.dataset_subset_size))
         
             dataset = dataset.shuffle(seed=training_args.seed)
         
             trainer = SFTTrainer(
                 model=model,
                 args=training_args,
                 train_dataset=dataset,
                 eval_dataset=eval_dataset,
                 formatting_func=formatting_prompts_func,
                 processing_class=tokenizer,
             )
         
             trainer.train()
         
             dist.barrier()
             if trainer.is_world_process_zero():
                 best_model_path = trainer.state.best_model_checkpoint
         
                 final_model_dir = os.path.join(training_args.output_dir, "final_best_model")
                 print(f"Copying best model to: {final_model_dir}")
         
                 if os.path.exists(final_model_dir):
                     shutil.rmtree(final_model_dir)
                 shutil.copytree(best_model_path, final_model_dir)
         
                 if script_args.run_inference_after_training:
                     del model, trainer
                     torch.cuda.empty_cache()
                     run_post_training_inference(script_args, final_model_dir, tokenizer)
         
         def run_post_training_inference(script_args, best_model_path, tokenizer):
             print("\n" + "="*50)
             print("=== RUNNING POST-TRAINING INFERENCE TEST ===")
             print("="*50 + "\n")
         
             base_model = AutoModelForCausalLM.from_pretrained(
                 script_args.model_id,
                 torch_dtype=torch.bfloat16,
                 trust_remote_code=True,
                 device_map="auto"
             )
             model = PeftModel.from_pretrained(base_model, best_model_path)
             model = model.merge_and_unload()
             model.eval()
         
             # Define the test case
             schema = "CREATE TABLE artists (Name TEXT, Country TEXT, Genre TEXT)"
             system_message = "You are a text to SQL query translator. Users will ask you questions in English and you will generate a SQL query based on the provided SCHEMA."
             question = "Show me all artists from the Country just north of the USA."
         
             prompt = f"{system_message}\n\n### SCHEMA:\n{schema}\n\n### USER QUERY:\n{question}\n\n### SQL QUERY:\n"
         
             print(f"Test Prompt:\n{prompt}")
         
             inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
         
             print("\n--- Generating SQL... ---")
             outputs = model.generate(
                 **inputs,
                 max_new_tokens=100,
                 pad_token_id=tokenizer.eos_token_id,
                 do_sample=False,
                 temperature=None,
                 top_p=None,
             )
         
             generated_sql = tokenizer.decode(outputs[0], skip_special_tokens=True)[len(prompt):].strip()
         
             print(f"\n--- Generated SQL Query ---")
             print(generated_sql)
             print("\n" + "="*50)
             print("=== INFERENCE TEST COMPLETE ===")
             print("="*50 + "\n")
         
         if __name__ == "__main__":
             main()

  4. To specify the tasks for the jobs to run on your Slurm cluster, create the `train-mixtral.sh` file with the following content:
         
         #!/bin/bash
         #SBATCH --job-name=mixtral-fsdp
         #SBATCH --nodes=2
         #SBATCH --ntasks-per-node=8
         #SBATCH --gpus-per-node=8
         #SBATCH --partition=a4high
         #SBATCH --output=mixtral-%j.out
         #SBATCH --error=mixtral-%j.err
         
         set -e
         set -x
         
         echo "--- Slurm Job Started ---"
         
         # --- Define Paths ---
         LOCAL_SSD_PATH="/mnt/localssd/job_${SLURM_JOB_ID}"
         VENV_PATH="${HOME}/.venv/venv-fsdp"
         MODEL_PATH="${HOME}/Mixtral-8x7B-v0.1"
         
         # --- STAGE 1: Stage Data to Local SSD on Each Node ---
         srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 bash -c "
         echo '--- Staging on node: $(hostname) ---'
         mkdir -p ${LOCAL_SSD_PATH}
         
         echo 'Copying virtual environment...'
         rsync -a -q ${VENV_PATH}/ ${LOCAL_SSD_PATH}/venv/
         
         echo 'Copying model weights...'
         rsync -a ${MODEL_PATH}/ ${LOCAL_SSD_PATH}/model/
         
         mkdir -p ${LOCAL_SSD_PATH}/hf_cache
         
         echo '--- Staging on $(hostname) complete ---'
         "
         echo "--- Staging complete on all nodes ---"
         
         # --- STAGE 2: Run the Training Job ---
         echo "--- Launching Distributed Training with GIB NCCL Plugin ---"
         nodes=( $( scontrol show hostnames "$SLURM_JOB_NODELIST" ) )
         head_node=${nodes[0]}
         head_node_ip=$(srun --nodes=1 --ntasks=1 -w "$head_node" hostname --ip-address)
         
         export MASTER_ADDR=$head_node_ip
         export MASTER_PORT=29500
         
         export NCCL_SOCKET_IFNAME=enp0s19
         
         export NCCL_NET=gIB
         
         # export NCCL_DEBUG=INFO # Un-comment to diagnose NCCL issues if needed
         
         srun --cpu-bind=none --accel-bind=g bash -c '
         # Activate the environment from the local copy
         source '${LOCAL_SSD_PATH}'/venv/bin/activate
         
         # Point Hugging Face cache to the local SSD
         export HF_HOME='${LOCAL_SSD_PATH}'/hf_cache
         
         export RANK=$SLURM_PROCID
         export WORLD_SIZE=$SLURM_NTASKS
         export LOCAL_RANK=$SLURM_LOCALID
         
         export LD_LIBRARY_PATH=/usr/local/gib/lib64:$LD_LIBRARY_PATH
         source /usr/local/gib/scripts/set_nccl_env.sh
         
         # --- Launch the training ---
         python \
             '${SLURM_SUBMIT_DIR}'/train-mixtral.py \
             --model_id="'${LOCAL_SSD_PATH}'/model/" \
             --output_dir="${HOME}/outputs/mixtral_job_${SLURM_JOB_ID}" \
             --dataset_name="philschmid/gretel-synthetic-text-to-sql" \
             --seed=900913 \
             --bf16=True \
             --num_train_epochs=3 \
             --per_device_train_batch_size=32 \
             --gradient_accumulation_steps=4 \
             --learning_rate=4e-5 \
             --logging_steps=3 \
             --lora_r=32 \
             --lora_alpha=32 \
             --lora_dropout=0.05 \
             --eval_strategy=steps \
             --eval_steps=10 \
             --save_strategy=steps \
             --save_steps=10 \
             --load_best_model_at_end=False \
             --metric_for_best_model=eval_loss \
             --run_inference_after_training \
             --dataset_subset_size=67000
         '
         
         # --- STAGE 3: Cleanup ---
         echo "--- Cleaning up local SSD on all nodes ---"
         srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 bash -c "rm -rf ${LOCAL_SSD_PATH}"
         
         echo "--- Slurm Job Finished ---"




### Upload the scripts to your Slurm cluster

To upload the scripts that you created in the previous section to the Slurm cluster, follow these steps:

  1. Set the `LOGIN_NODE` variable by retrieving the name of the login node for your cluster:
         
         LOGIN_NODE="$(gcloud compute instances list \
                         --project="${PROJECT_ID}" \
                         --filter="labels.ghpc_deployment='${DEPLOYMENT_NAME}' AND labels.slurm_instance_role='login'" \
                         --format="value(name)" | head -n 1)"

The `LOGIN_NODE` variable stores a value similar to `${DEPLOYMENT_NAME}-login-001`.

  2. Create a firewall rule:
         
         gcloud compute firewall-rules create allow-ssh-ingress-from-iap \
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
           ./requirements-fsdp.txt \
           ./train-mixtral.py \
           ./train-mixtral.sh \
           "${LOGIN_NODE}":~/




### Connect to the Slurm cluster

Connect to the Slurm cluster by connecting to the login node through SSH:
    
    
    gcloud compute ssh "${LOGIN_NODE}" \
        --project="${PROJECT_ID}" \
        --tunnel-through-iap \
        --zone="${ZONE}"
        -- -t "export HF_TOKEN='${HF_TOKEN}'; bash -l"

### Install frameworks and tools

After you connect to the login node, install the required frameworks and tools by running the installation script on a compute node:
    
    
    # On the login node
    srun \
      --job-name=env-setup \
      --nodes=1 \
      --ntasks=1 \
      --gpus-per-node=1 \
      --partition=a4high \
      bash ./install_environment.sh

This command sets up the virtual environment, installs all dependencies, and downloads the Mixtral model weights into `~/Mixtral-8x7B-v0.1`. This process can take over 30 minutes to complete.

Running this step via `srun` delegates the installation script from the login node to an allocated compute node, allowing the script to access GPU drivers during compilation.

## Start your fine-tuning workload

To start your training workload, do the following:

  1. Submit the job to the Slurm scheduler:
         
         # On the login node
         sbatch train-mixtral.sh




## Monitor your workload

To monitor the progress of your fine-tuning job, use the following methods:

  1. On the login node in your Slurm cluster, you can monitor the job's progress by checking the output files created in your `home` directory:
         
         # On the login node:
         tail -f mixtral-*.out mixtral-*.err

If your job successfully starts, then the `.err` file shows a progress bar that updates as your job progresses.

The job has two main phases:

     * Copying the large base model to the local SSD of each compute node.
     * The training job, which begins once the copying of the model is complete.

The whole job takes about 60 minutes to run.

  2. You can also monitor the use of the GPUs in your Slurm cluster to verify that your fine-tuning job is efficiently running. To do so, open the following link in your browser:
         
         https://console.cloud.google.com/monitoring/metrics-explorer?project=YOUR_PROJECT_ID&pageState=%7B%22xyChart%22%3A%7B%22dataSets%22%3A%5B%7B%22timeSeriesFilter%22%3A%7B%22filter%22%3A%22metric.type%3D%5C%22agent.googleapis.com%2Fgpu%2Futilization%5C%22%20resource.type%3D%5C%22gce_instance%5C%22%22%2C%22perSeriesAligner%22%3A%22ALIGN_MEAN%22%7D%2C%22plotType%22%3A%22LINE%22%7D%5D%7D%7D
         

Alternately, you can enter the command directly in the terminal:
         
         open "https://console.cloud.google.com/monitoring/metrics-explorer?project=${PROJECT_ID}&pageState=%7B%22xyChart%22%3A%7B%22dataSets%22%3A%5B%7B%22timeSeriesFilter%22%3A%7B%22filter%22%3A%22metric.type%3D%5C%22agent.googleapis.com%2Fgpu%2Futilization%5C%22%20resource.type%3D%5C%22gce_instance%5C%22%22%2C%22perSeriesAligner%22%3A%22ALIGN_MEAN%22%7D%2C%22plotType%22%3A%22LINE%22%7D%5D%7D%7D"

When you monitor your workload, you can see the following:

     * **GPU usage** : for a healthy fine-tuning job, you can expect to see the usage of all your 16 GPUs (eight GPUs for each VM in the cluster) rise and stabilize to a specific level throughout your training.

     * **Job duration** : the job should take approximately one hour to complete. 




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the resources

Run the following commands to delete the resources that you created in this tutorial:

  1. To delete your Slurm cluster, go to the `cluster-toolkit` directory and run the [`gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy):
         
         ./gcluster destroy "${DEPLOYMENT_NAME}" --auto-approve --robust

  2. Delete your bucket:
         
         gcloud storage rm --recursive "gs://${BUCKET_NAME}" --quiet || true

  3. To delete a [Packer](https://developer.hashicorp.com/packer/docs) image, open your web browser, navigate to the following page, search for your specific image, and click Delete.
         
         http://console.cloud.google.com/compute/images




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
  * [Create a serving endpoint](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-multiple-gpu): Once you have your fine-tuned model, you can deploy it to a serving endpoint using Google Kubernetes Engine (GKE) or Vertex AI to make it accessible for inference.
  * [Learn about recommended storage services for AI and ML workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/storage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
