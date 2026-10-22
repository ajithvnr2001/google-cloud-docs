---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/fsdp-llama4/
title: Use FSDP to fine-tune Llama 4 on an A4 Slurm cluster \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:13.108606+00:00
---

# Use FSDP to fine-tune Llama 4 on an A4 Slurm cluster  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/fsdp-llama4/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Use FSDP to fine-tune Llama 4 on an A4 Slurm cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This tutorial shows you how to fine-tune a `Llama-4-Scout-17` large language model (LLM) on a multi-node, multi-GPU Slurm cluster on Google Cloud. The cluster uses two A4 virtual machine (VM) instances which each have 8 NVIDIA B200 GPUs.

The two main processes described in this tutorial are as follows:

  1. Deploy a production-grade, high-performance Slurm cluster by using the Cluster Toolkit. As part of this deployment, you create a custom VM image with the necessary software pre-installed. You also configure high-speed RDMA networking and create a Cloud Storage bucket to host your Terraform state.
  2. After the cluster is deployed, you run a distributed fine-tuning job by using the set of scripts that accompany this tutorial. The job leverages PyTorch Fully Sharded Data Parallel (FSDP), which you access through the Hugging Face [Transformer Reinforcement Learning library](https://github.com/huggingface/trl).

**Important:** To complete this tutorial, you must have reserved the capacity to create two A4 VMs. To learn more about your options for reserving capacity in AI Hypercomputer for a future date and time, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

This tutorial is intended for machine learning (ML) engineers, platform administrators and operators, and for data and AI specialists who are interested in using Slurm job scheduling capabilities to handle fine-tuning workloads.

## Objectives

  * Access Llama 4 by using Hugging Face.

  * Prepare your environment.

  * Create and deploy a production-grade A4 High-GPU Slurm cluster.

  * Configure a multi-node environment for distributed training with FSDP.

  * Fine-tune the Llama 4 model by using Hugging Face `trl.SFTTrainer`.

  * Stage data to local SSDs.

  * Monitor your job.

  * Clean up.




## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Compute Engine](https://cloud.google.com/compute/all-pricing)
  * [ Cloud Logging](https://docs.cloud.google.com/logging#pricing)
  * [ Cloud Storage](https://docs.cloud.google.com/storage/pricing)



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
         
         gcloud services enable compute.googleapis.com logging.googleapis.com cloudresourcemanager.googleapis.com servicenetworking.googleapis.com

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
         
         gcloud services enable compute.googleapis.com logging.googleapis.com cloudresourcemanager.googleapis.com servicenetworking.googleapis.com

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: ` roles/compute.admin, roles/iam.serviceAccountUser, roles/file.editor, roles/storage.admin, roles/serviceusage.serviceUsageAdmin `
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.
  15. Enable the default service account for your Google Cloud project: 
         
         gcloud iam service-accounts enable PROJECT_NUMBER-compute@developer.gserviceaccount.com   
             --project=PROJECT_ID

Replace PROJECT_NUMBER with your project number. To review your project number, see [ Get an existing project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#get_an_existing_project). 

  16. Grant the Editor role (`roles/editor`) to the default service account: 
         
         gcloud projects add-iam-policy-binding PROJECT_ID   
             --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com"   
             --role=roles/editor

  17. Create local authentication credentials for your user account: 
         
         gcloud auth application-default login

**Note** : If you use a local shell and an external identity provider (IdP), and you encounter an authentication error after running the preceding command, then [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 
  18. Enable OS Login for your project: 
         
         gcloud compute project-info add-metadata --metadata=enable-oslogin=TRUE

  19. [Sign in to or create a Hugging Face account](https://huggingface.co/login).
  20. [ Install the dependencies that you need to use the Cluster Toolkit](https://cloud.google.com/cluster-toolkit/docs/setup/install-dependencies).



## Access Llama 4 by using Hugging Face

To use Hugging Face to access Llama 4, do the following:

  1. [Sign the consent agreement to use Llama 4](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct).

  2. [Create a Hugging Face `read` access token](https://huggingface.co/docs/hub/security-tokens#how-to-manage-user-access-tokens).

Click **Your Profile > Settings > Access tokens > +Create new token**

  3. Copy and save the `read access` token value. You use it later in this tutorial.




## Prepare your environment

To prepare your environment, follow these steps:

  1. Clone the Cluster Toolkit GitHub repository:
         
         git clone https://github.com/GoogleCloudPlatform/cluster-toolkit.git
         

  2. Create a Cloud Storage bucket to host your Terraform state:
         
         gcloud storage buckets create gs://BUCKET_NAME \
             --project=PROJECT_ID
         

Replace the following:

     * `BUCKET_NAME`: a name for your Cloud Storage bucket that follows [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).

     * `PROJECT_ID`: the ID of the Google Cloud project where you want to create your Cloud Storage bucket.




## Create an A4 Slurm cluster

To create an A4 Slurm cluster, follow these steps:

  1. Go to the `cluster-toolkit` directory:
         
         cd cluster-toolkit
         

  2. If it's your first time using Cluster Toolkit, then build the [`gcluster` binary](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster):
         
         make
         

  3. Go to the `examples/machine-learning/a4-highgpu-8g` directory:
         
         cd examples/machine-learning/a4-highgpu-8g/
         

  4. Open the `a4high-slurm-deployment.yaml` file, and then edit it as follows:
         
         terraform_backend_defaults:
           type: gcs
           configuration:
             bucket: BUCKET_NAME
         
         vars:
           deployment_name: a4-high
           project_id: PROJECT_ID
           region: REGION
           zone: ZONE
           a4h_cluster_size: 2
           a4h_reservation_name: RESERVATION_URL
         

Replace the following:

     * `BUCKET_NAME`: the name of the Cloud Storage bucket that you created in the previous section.

     * `PROJECT_ID`: the ID of the Google Cloud project where your bucket exists and where you want to create your Slurm cluster.

     * `REGION`: the region where your reservation exists.

     * `ZONE`: the zone where your reservation exists.

     * `RESERVATION_URL`: the URL of the reservation that you want to use to create your Slurm cluster. Based on the project in which the reservation exists, specify one of the following values:

       * The reservation exists in your project: `RESERVATION_NAME`

       * The reservation exists in a different project, and your project can use the reservation: `projects/RESERVATION_PROJECT_ID/reservations/RESERVATION_NAME`

  5. Deploy the cluster:
         
         ./gcluster deploy -d examples/machine-learning/a4-highgpu-8g/a4high-slurm-deployment.yaml examples/machine-learning/a4-highgpu-8g/a4high-slurm-blueprint.yaml --auto-approve
         

The [`./gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) is a two-phase process, which is as follows:

     * The first phase builds a custom image with all software pre-installed, which can take up to 35 minutes to complete.

     * The second phase deploys the cluster by using that custom image. This process should complete more quickly than the first phase.

If the first phase succeeds but the second phase fails, then you can try to deploy the Slurm cluster again by skipping the first phase:
    
    ./gcluster deploy -d examples/machine-learning/a4-highgpu-8g/a4high-slurm-deployment.yaml examples/machine-learning/a4-highgpu-8g/a4high-slurm-blueprint.yaml --auto-approve --skip "image" -w
    




## Prepare your workload

To prepare your workload, you do the following:

  1. Create workload scripts.

  2. Upload scripts to the Slurm cluster.

  3. Connect to the Slurm cluster.

  4. Install frameworks and tools.




## Create workload scripts

To create the scripts that your fine-tuning workload will use, follow these steps:

  1. To set up the Python virtual environment, create the `install_environment.sh` file with the following content:
         
         #!/bin/bash
         # This script sets up a consistent environment for FSDP training.
         # It is meant to be run once on the login node of your Slurm cluster
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
         pip install --force-reinstall --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu128
         
         echo "--- [STEP 2.3] Installing application dependencies ---"
         if [ -f "requirements-fsdp.txt" ]; then
             pip install -r requirements-fsdp.txt
         else
             echo "ERROR: requirements-fsdp.txt not found!"
             exit 1
         fi
         
         # --- 3. Download the Model ---
         echo "--- [STEP 2.4] Downloading Llama4 model ---"
         if [ -z "$HF_TOKEN" ]; then
           echo "ERROR: The HF_TOKEN environment variable is not set."; exit 1;
         fi
         pip install huggingface_hub[cli]
         
         # Execute the CLI using its full, explicit path
         $VENV_PATH/bin/huggingface-cli download meta-llama/Llama-4-Scout-17B-16E-Instruct --local-dir ~/Llama-4-Scout-17B-16E-Instruct --token $HF_TOKEN
         
         echo "--- Environment setup complete. ---"
         

This script sets up a reliable Python virtual environment, installs a PyTorch nightly build, and downloads the Llama 4 model.

**Note:** This tutorial doesn't use the latest versions of NVIDIA and Pytorch dependencies. If you need newer dependencies, then see the [NVIDIA documentation](https://developer.nvidia.com/cuda-gpus) and the [Pytorch documentation](https://pytorch.org/get-started/locally/#linux-pip).
  2. To specify the Python dependencies for the training script, create a `requirements-fsdp.txt`file with the following content:
         
         transformers==4.55.0
         datasets==4.0.0
         peft==0.16.0
         accelerate==1.9.0
         trl==0.21.0
         
         # Other dependencies
         sentencepiece==0.2.0
         

  3. Specify `llama4-train-distributed.py` as the main training script:
         
         import torch
         from datasets import load_dataset
         from peft import LoraConfig, PeftModel
         from transformers import (
             AutoModelForCausalLM,
             AutoTokenizer,
             TrainingArguments,
             HfArgumentParser,
         )
         
         from torch.distributed import get_rank, get_world_size
         
         from transformers.models.llama4.modeling_llama4 import Llama4TextDecoderLayer
         from trl import SFTTrainer
         from dataclasses import dataclass, field
         from typing import Optional
         
         @dataclass
         class ScriptArguments:
             model_id: str = field(metadata={"help": "Hugging Face model ID from the Hub"})
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
             ddp_find_unused_parameters: Optional[bool] = field(default=True, metadata={"help": "When using FSDP activation checkpointing, this must be set to True"})
         
         def formatting_prompts_func(example):
             system_message = "You are a text to SQL query translator. Users will ask you questions in English and you will generate a SQL query based on the provided SCHEMA."
             user_prompt = f"### SCHEMA:\n{example['sql_context']}\n\n### USER QUERY:\n{example['sql_prompt']}"
             response = f"\n\n### SQL QUERY:\n{example['sql']}"
             return f"{system_message}\n\n{user_prompt}{response}"
         
         def main():
             parser = HfArgumentParser((ScriptArguments, PeftArguments, SftTrainingArguments))
             script_args, peft_args, training_args = parser.parse_args_into_dataclasses()
         
             training_args.gradient_checkpointing = True
             training_args.gradient_checkpointing_kwargs = {"use_reentrant": False}
         
             training_args.optim = "adamw_torch_fused"
         
             training_args.fsdp = "full_shard"
             training_args.fsdp_config = {
                 "fsdp_auto_wrap_policy": "TRANSFORMER_BASED_WRAP",
                 "fsdp_transformer_layer_cls_to_wrap": [Llama4TextDecoderLayer],
                 "fsdp_state_dict_type": "FULL_STATE_DICT",
                 "fsdp_offload_params": False,
                 "fsdp_forward_prefetch": True,
             }
         
             tokenizer = AutoTokenizer.from_pretrained(script_args.model_id, trust_remote_code=True)
         
             model = AutoModelForCausalLM.from_pretrained(
                 script_args.model_id,
                 torch_dtype=torch.bfloat16,
                 trust_remote_code=True,
                 attn_implementation="sdpa",
             )
         
             peft_config = LoraConfig(
                 r=peft_args.lora_r,
                 lora_alpha=peft_args.lora_alpha,
                 lora_dropout=peft_args.lora_dropout,
                 bias="none",
                 task_type="CAUSAL_LM",
                 target_modules=["q_proj", "v_proj", "k_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
             )
             rank = get_rank()
             world_size = get_world_size()
         
             dataset = load_dataset(script_args.dataset_name, split="train")
         
             if script_args.dataset_subset_size is not None:
                 dataset = dataset.select(range(script_args.dataset_subset_size))
             else:
                 print(f"Using the full dataset with {len(dataset)} samples.")
         
             dataset = dataset.shuffle(seed=training_args.seed)
             print(f"Dataset shuffled with seed: {training_args.seed}.")
         
             if world_size > 1:
                 print(f"Sharding dataset for Rank {rank} of {world_size}.")
                 dataset = dataset.shard(num_shards=world_size, index=rank)
         
             print("Initializing SFTTrainer...")
             trainer = SFTTrainer(
                 model=model,
                 args=training_args,
                 train_dataset=dataset,
                 peft_config=peft_config,
                 formatting_func=formatting_prompts_func,
                 processing_class=tokenizer,
             )
         
             trainer.train()
         
             trainer.save_model(training_args.output_dir)
         
             if script_args.run_inference_after_training and trainer.is_world_process_zero():
                 del model
                 del trainer
                 torch.cuda.empty_cache()
                 run_post_training_inference(script_args, training_args, tokenizer)
         
         def run_post_training_inference(script_args, training_args, tokenizer):
             """
             Loads the fine-tuned PEFT adapter from the local output directory and runs inference.
             This should only be called on rank 0 after training is complete.
             """
             print("\n" + "="*50)
             print("=== RUNNING POST-TRAINING INFERENCE TEST ===")
             print("="*50 + "\n")
         
             # Load the base model and merge the adapter.
             base_model = AutoModelForCausalLM.from_pretrained(
                 script_args.model_id,
                 torch_dtype=torch.bfloat16,
                 trust_remote_code=True,
                 device_map="auto"
             )
             # Load the PEFT adapter and merge it into the base model
             model = PeftModel.from_pretrained(base_model, training_args.output_dir)
             model = model.merge_and_unload() # Merge weights for faster inference
             model.eval()
         
             # Define the test case
             schema = "CREATE TABLE artists (Name TEXT, Country TEXT, Genre TEXT)"
             system_message = "You are a text to SQL query translator. Users will ask you questions in English and you will generate a SQL query based on the provided SCHEMA."
             question = "Show me all artists from the Country just north of the USA."
         
             # This must match the formatting_func exactly
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
         

This script utilizes the TRL Supervised Fine-Tuning (SFT) Trainer to manage FSDP training loops, Low-Rank Adaptation (LoRA) configuration, and data formatting.

  4. To specify the tasks for the jobs to run on your Slurm cluster, create the `submit.slurm` file with the following content:
         
         #!/bin/bash
         #SBATCH --job-name=llama4-fsdp-fixed
         #SBATCH --nodes=2
         #SBATCH --ntasks-per-node=8
         #SBATCH --gpus-per-node=8
         #SBATCH --partition=a4high
         #SBATCH --output=llama4-%j.out
         #SBATCH --error=llama4-%j.err
         
         set -e
         set -x
         
         echo "--- Slurm Job Started ---"
         echo "Job ID: $SLURM_JOB_ID"
         echo "Node List: $SLURM_JOB_NODELIST"
         
         # --- Define Paths ---
         LOCAL_SSD_PATH="/mnt/localssd/job_${SLURM_JOB_ID}"
         VENV_PATH="${HOME}/.venv/venv-fsdp"
         MODEL_PATH="${HOME}/Llama-4-Scout-17B-16E-Instruct"
         
         # --- STAGE 1: Stage Data to Local SSD on Each Node ---
         srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 bash -c "
           echo '--- Staging on node: $(hostname) ---'
         
           mkdir -p ${LOCAL_SSD_PATH}
         
           echo 'Copying virtual environment...'
           rsync -a -q ${VENV_PATH}/ ${LOCAL_SSD_PATH}/venv/
         
           echo 'Copying model weights...'
           rsync -a --info=progress2 ${MODEL_PATH}/ ${LOCAL_SSD_PATH}/model/
         
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
             '${SLURM_SUBMIT_DIR}'/llama4-train-distributed.py \
               --model_id="'${LOCAL_SSD_PATH}'/model/" \
               --output_dir="'${LOCAL_SSD_PATH}'/outputs/" \
               --dataset_name="philschmid/gretel-synthetic-text-to-sql" \
               --seed=900913 \
               --bf16=True \
               --num_train_epochs=1 \
               --per_device_train_batch_size=2 \
               --gradient_accumulation_steps=4 \
               --learning_rate=2e-5 \
               --logging_steps=10 \
               --lora_r=16 \
               --lora_alpha=32 \
               --lora_dropout=0.05 \
               --run_inference_after_training
         '
         
         # --- STAGE 3: Copy Final Results Back to Persistent Storage ---
         echo "--- Copying final results from local SSD to shared storage ---"
         PERSISTENT_OUTPUT_DIR="${HOME}/outputs/llama4_job_${SLURM_JOB_ID}"
         mkdir -p "$PERSISTENT_OUTPUT_DIR"
         
         # Only copy from the head node where trl has combined the results
         srun --nodes=1 --ntasks=1 -w "$head_node" \
           rsync -a --info=progress2 "${LOCAL_SSD_PATH}/outputs/" "${PERSISTENT_OUTPUT_DIR}/"
         
         # --- STAGE 4: Cleanup ---
         echo "--- Cleaning up local SSD on all nodes ---"
         srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 bash -c "rm -rf ${LOCAL_SSD_PATH}"
         
         echo "--- Slurm Job Finished ---"
         




### Upload scripts to the Slurm cluster

To upload the scripts that you created in the previous section to the Slurm cluster, follow these steps:

  1. To identify your login node, list all A4 VMs in your project:
         
         gcloud compute instances list --filter="machineType:a4-highgpu-8g"
         

The name of the login node is similar to `a4-high-login-001`.

  2. Upload your scripts to the login node's home directory:
         
         gcloud compute scp --project="$PROJECT_ID" --zone="$ZONE" --tunnel-through-iap \
           ./install_environment.sh \
           ./requirements-fsdp.txt \
           ./llama4-train-distributed.py \
           ./submit.slurm \
           "${LOGIN_NODE_NAME}":~/
         

Replace `LOGIN_NODE_NAME` with the name of the login node.




### Connect to the Slurm cluster

Connect to the Slurm cluster by connecting to the login node through SSH:
    
    
    gcloud compute ssh LOGIN_NODE_NAME \
        --project=PROJECT_ID \
        --tunnel-through-iap \
        --zone=ZONE
    

### Install frameworks and tools

After you connect to the login node, install frameworks and tools by doing the following:

  1. Export your Hugging Face token:
         
         # On the login node
         export HF_TOKEN="hf_..." # Replace with your token
         

  2. Run the installation script:
         
         # On the login node
         chmod +x install_environment.sh
         ./install_environment.sh
         

This command sets up a virtual environment with all the required dependencies, and downloads the model weights into the `~/Llama-4-Scout-17B-16E-Instruct` file.

Because the model download is very large (~200 GB), this process takes around 30 minutes, depending on network conditions.




## Start your fine-tuning workload

To start training your workload, do the following:

  1. Submit the job to the Slurm scheduler:
         
         sbatch submit.slurm
         

  2. On the login node in your Slurm cluster, you can monitor the job's progress by checking the output files created in your `home` directory:
         
         # On the login node
         tail -f llama4-*.out
         

If your job successfully starts, then the `.err` file shows a progress bar that updates as your job progresses.

This job should take a bit over an hour to complete on the Slurm Cluster. The job has two main phases:

     * Copying the large base model to the local SSD of each compute node.
     * The training job, which begins once the copying of the model is complete. This job takes about 35 minutes to run.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete your project

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

### Delete your Slurm cluster

To delete your Slurm cluster, follow these steps:

  1. Go to the `cluster-toolkit` directory.

  2. Use the [`gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy) to destroy the Terraform file and all created resources:
         
         ./gcluster destroy a4-high --auto-approve
         




## What's next

  * [Redeploy a Slurm cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-fully-managed-slurm-cluster#redeploy-slurm-cluster)

  * [Test network performance on a Slurm cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-slurm)

  * [Monitor VMs in a Slurm cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
