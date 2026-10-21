---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gemma4-finetune-a4-gke-cluster/
title: Fine-tune Gemma 4 on an A4 GKE cluster \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:41.350968+00:00
---

# Fine-tune Gemma 4 on an A4 GKE cluster  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gemma4-finetune-a4-gke-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Fine-tune Gemma 4 on an A4 GKE cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This tutorial shows you how to fine-tune a [Gemma 4](https://ai.google.dev/gemma/docs/core) large language model (LLM) on a single-host, multi-GPU Google Kubernetes Engine (GKE) cluster on Google Cloud. This cluster uses a single A4 virtual machine (VM) instance with 8 NVIDIA B200 GPUs attached.

The two main processes described in this tutorial are as follows:

  1. Deploy a high-performance GKE cluster by using GKE Autopilot. As part of this deployment, you use Cloud Build to build a custom container image with the necessary software pre-installed.
  2. After the cluster is deployed, you run a fine-tuning job that uses Fully Sharded Data Parallel (FSDP) to shard the model across all eight GPUs of a single A4 (`a4-highgpu-8g`) node. The job uses the set of scripts that accompany this tutorial and leverages the [Hugging Face Accelerate library](https://huggingface.co/docs/accelerate/en/usage_guides/fsdp).

**Important:** To complete this tutorial, you must have reserved the capacity to create an A4 VM. To learn more about your options for reserving capacity in AI Hypercomputer for a future date and time, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

This tutorial is intended for machine learning (ML) engineers, researchers, platform administrators and operators, and for data and AI specialists who are interested in deploying GKE clusters on Google Cloud to train LLMs.

## Objectives

  * Access the Gemma 4 model by using Hugging Face.

  * Prepare your environment.

  * Create and deploy an A4 GKE cluster.

  * Fine-tune the Gemma 4 model by using the Hugging Face Accelerate library with fully sharded data parallel (FSDP).

  * Monitor your job.

  * Clean up.




## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Compute Engine](https://cloud.google.com/compute/vm-instance-pricing)
  * [ Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine)
  * [ Artifact Registry](https://docs.cloud.google.com/artifact-registry/pricing)
  * [ Cloud Build](https://docs.cloud.google.com/build/pricing)
  * [ Cloud Storage](https://docs.cloud.google.com/storage/pricing)
  * [ Cloud Logging](https://docs.cloud.google.com/stackdriver/pricing#logging-pricing-summary)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Enable the required APIs, if any are not already enabled:

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com container.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com logging.googleapis.com cloudresourcemanager.googleapis.com servicenetworking.googleapis.com

  2. Enable the default service account for your Google Cloud project:
         
         export PROJECT_NUMBER="$(gcloud projects describe "YOUR_PROJECT_ID" --format "value(project_number)")"
         gcloud iam service-accounts enable "${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
             --project=YOUR_PROJECT_ID

  3. Grant the roles that the default service account needs to run the fine-tuning workload:
         
         ROLES=("roles/artifactregistry.writer"
                "roles/cloudbuild.builds.builder"
                "roles/logging.logWriter"
                "roles/monitoring.metricWriter"
                "roles/monitoring.viewer"
                "roles/stackdriver.resourceMetadata.writer"
                "roles/storage.objectViewer")
         for role in "${ROLES[@]}"; do
           gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
               --member="serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
               --role="${role}" 1>/dev/null
         done
         unset ROLES

To verify that the roles were granted, run the following command:
         
         gcloud projects get-iam-policy YOUR_PROJECT_ID \
             --flatten="bindings[].members" \
             --filter="bindings.members:serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
             --format="table(bindings.role)"

**Note:** This step grants only the predefined roles that this tutorial requires. Granting a basic role such as Editor (`roles/editor`) gives the service account many more permissions than it needs, and your organization's policies might block the grant. For more information, see [Best practices for working with service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts).
  4. Create local authentication credentials for your user account:
         
         gcloud auth application-default login

**Note:** If you use a local shell and an external identity provider (IdP), and you encounter an authentication error after running the preceding command, then [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).
  5. Enable OS Login for your project:
         
         gcloud compute project-info add-metadata \
             --metadata=enable-oslogin=TRUE \
             --project=YOUR_PROJECT_ID




To get the permissions that you need to complete this tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
  * [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
  * [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`)
  * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Access Gemma 4 by using Hugging Face

To use Hugging Face to access Gemma 4, do the following:

  1. [Sign in to Hugging Face](https://huggingface.co/google/gemma-4-31B-it)
  2. [Create a Hugging Face `write` access token](https://huggingface.co/docs/hub/security-tokens#how-to-manage-user-access-tokens).  
Click **Your Profile > Settings > Access tokens > +Create new token**
  3. Copy and save the `write access` token value. You use it later in this tutorial.



## Prepare your environment

To prepare your environment, set the following:
    
    
    export PROJECT_ID="YOUR_PROJECT_ID"
    export CLUSTER_NAME="YOUR_CLUSTER_NAME"
    export CLUSTER_REGION="YOUR_REGION"
    export RESERVATION="YOUR_RESERVATION_NAME"
    export HF_TOKEN="YOUR_HF_TOKEN"
    export ARTIFACT_REPO_LOCATION="YOUR_ARTIFACT_REGISTRY_LOCATION"
    
    gcloud config set project "${PROJECT_ID}"
    gcloud config set billing/quota_project "${PROJECT_ID}"

Replace the following:

  * YOUR_PROJECT_ID: the ID of the Google Cloud project where you want to create the GKE cluster.

  * YOUR_CLUSTER_NAME: the name of the GKE cluster to create.

  * YOUR_REGION: the region where you want to create your GKE cluster. You can only create the cluster in the region where your reservation exists.

  * YOUR_RESERVATION_NAME: the identifier for your reserved capacity.

  * YOUR_HF_TOKEN: the Hugging Face access token that you created in the previous section.

  * YOUR_ARTIFACT_REGISTRY_LOCATION: the Google Cloud region where you want to create your Artifact Registry repository. To minimize image pull latency, we recommend that you use the same region that you used for YOUR_REGION.




## Create a GKE cluster in Autopilot mode

To create a GKE cluster in Autopilot mode, run the following command:
    
    
    gcloud container clusters create-auto "${CLUSTER_NAME}" \
        --project="${PROJECT_ID}" \
        --location="${CLUSTER_REGION}"

Creating the GKE cluster might take some time to complete. To verify that Google Cloud has finished creating your cluster, go to [Kubernetes clusters](https://console.cloud.google.com/kubernetes/list/overview) on the Google Cloud console.

## Create a Kubernetes secret for Hugging Face credentials

To create a Kubernetes secret for Hugging Face credentials, follow these steps:

  1. Configure `kubectl` to communicate with your GKE cluster:
         
         gcloud container clusters get-credentials "${CLUSTER_NAME}" \
             --location="${CLUSTER_REGION}"

  2. Create a Kubernetes secret to store your Hugging Face token:
         
         kubectl create secret generic hf-secret \
             --from-literal=hf_api_token="${HF_TOKEN}" \
             --dry-run=client -o yaml | kubectl apply -f -




## Prepare your workload

To prepare your workload, you do the following:

  1. Create workload scripts.

  2. Use Docker and Cloud Build to create a fine-tuning container.




### Create workload scripts

To create the scripts that your fine-tuning workload uses, do the following:

  1. Create a directory for the workload scripts. Use this directory as your working directory.
         
         mkdir llm-finetuning-gemma
         cd llm-finetuning-gemma

  2. Create the `cloudbuild.yaml` file to use Google Cloud Build. This file creates your workload container and stores it in Artifact Registry:
         
         steps:
         - name: 'gcr.io/cloud-builders/docker'
           args:
           - 'build'
           - '-t'
           - '$_ARTIFACT_REPO_LOCATION-docker.pkg.dev/$PROJECT_ID/gemma/finetune-gemma-gpu:2.0.0'
           - '.'
         images:
         - '$_ARTIFACT_REPO_LOCATION-docker.pkg.dev/$PROJECT_ID/gemma/finetune-gemma-gpu:2.0.0'
         options:
           logging: CLOUD_LOGGING_ONLY

  3. Create a `Dockerfile` file to execute the fine-tuning job:
         
         FROM nvidia/cuda:12.8.1-cudnn-devel-ubuntu24.04
         RUN apt-get update && \
             apt-get -y install python3 python3-dev gcc python3-pip \
                 python3-venv git curl vim && \
             rm -rf /var/lib/apt/lists/*
         RUN python3 -m venv /opt/venv
         ENV PATH="/opt/venv/bin:/usr/local/nvidia/bin:$PATH"
         ENV LD_LIBRARY_PATH="/usr/local/nvidia/lib64:$LD_LIBRARY_PATH"
         RUN pip3 install setuptools wheel packaging ninja
         RUN pip3 install torch torchvision torchaudio \
             --index-url https://download.pytorch.org/whl/cu128
         RUN pip3 install \
             "transformers>=4.53.3" \
             "datasets>=4.0.0" \
             "accelerate>=1.9.0" \
             evaluate==0.4.5 \
             bitsandbytes==0.46.1 \
             "trl>=0.19.1" \
             "peft>=0.16.0" \
             tensorboard==2.20.0 \
             protobuf==6.31.1 \
             sentencepiece==0.2.0
         COPY finetune.py /finetune.py
         COPY accel_fsdp_gemma4_config.yaml /accel_fsdp_gemma4_config.yaml
         CMD accelerate launch --config_file accel_fsdp_gemma4_config.yaml finetune.py

**Note:** This tutorial doesn't use the latest versions of NVIDIA and Pytorch dependencies. If you need newer dependencies, then see the [NVIDIA documentation](https://developer.nvidia.com/cuda-gpus) and the [Pytorch documentation](https://pytorch.org/get-started/locally/#linux-pip).
  4. Create the `accel_fsdp_gemma4_config.yaml` file. This configuration file directs Hugging Face Accelerate to split the tuning job across the eight local GPUs on your single host by using FSDP:
         
         compute_environment: LOCAL_MACHINE
         debug: false
         distributed_type: FSDP
         downcast_bf16: 'no'
         enable_cpu_affinity: false
         fsdp_config:
           fsdp_activation_checkpointing: false
           fsdp_auto_wrap_policy: TRANSFORMER_BASED_WRAP
           fsdp_cpu_ram_efficient_loading: false
           fsdp_offload_params: false
           fsdp_reshard_after_forward: true
           fsdp_state_dict_type: FULL_STATE_DICT
           fsdp_transformer_layer_cls_to_wrap: Gemma4TextDecoderLayer
           fsdp_version: 2
         machine_rank: 0
         main_training_function: main
         mixed_precision: bf16
         num_machines: 1
         num_processes: 8
         rdzv_backend: static
         same_network: true
         tpu_env: []
         tpu_use_cluster: false
         tpu_use_sudo: false
         use_cpu: false

  5. Create the `finetune.yaml` file:
         
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: finetune-job
           namespace: default
         spec:
           backoffLimit: 2
           template:
             metadata:
               annotations:
                 kubectl.kubernetes.io/default-container: finetuner
             spec:
               terminationGracePeriodSeconds: 600
               containers:
               - name: finetuner
                 image: $IMAGE_URL
                 command: ["accelerate","launch"]
                 args:
                 - "--config_file"
                 - "accel_fsdp_gemma4_config.yaml"
                 - "finetune.py"
                 - "--model_id"
                 - "google/gemma-4-31B-it"
                 - "--output_dir"
                 - "gemma-31b-text-to-sql"
                 - "--per_device_train_batch_size"
                 - "2"
                 - "--gradient_accumulation_steps"
                 - "32"
                 - "--num_train_epochs"
                 - "3"
                 - "--learning_rate"
                 - "1e-5"
                 - "--save_strategy"
                 - "steps"
                 - "--save_steps"
                 - "20"
                 - "--push_to_hub"
                 resources:
                   limits:
                     nvidia.com/gpu: "8"
                     memory: "1200Gi"
                     ephemeral-storage: "350Gi"
                   requests:
                     nvidia.com/gpu: "8"
                     memory: "1200Gi"
                     ephemeral-storage: "350Gi"
                 env:
                 - name: HF_TOKEN
                   valueFrom:
                     secretKeyRef:
                       name: hf-secret
                       key: hf_api_token
                 volumeMounts:
                 - mountPath: /dev/shm
                   name: dshm
               volumes:
               - name: dshm
                 emptyDir:
                   medium: Memory
                   sizeLimit: 64Gi
               nodeSelector:
                 cloud.google.com/gke-accelerator: nvidia-b200
                 cloud.google.com/reservation-name: $RESERVATION
                 cloud.google.com/reservation-affinity: "specific"
                 cloud.google.com/gke-gpu-driver-version: latest
               restartPolicy: OnFailure

  6. Create the `finetune.py` file:
         
         import torch
         import argparse
         import subprocess
         from datasets import load_dataset
         from transformers import (
             AutoTokenizer,
             AutoModelForCausalLM,
             BitsAndBytesConfig,
             AutoConfig,
         )
         from peft import LoraConfig
         from trl import SFTTrainer, SFTConfig
         from huggingface_hub import login
         
         def get_args():
             parser = argparse.ArgumentParser()
             parser.add_argument(
                 "--model_id", type=str, default="google/gemma-4-31b-it",
                 help="Hugging Face model ID")
             parser.add_argument(
                 "--hf_token", type=str, default=None,
                 help="Hugging Face token for private models")
             parser.add_argument(
                 "--trust_remote", type=lambda x: str(x).lower() == "true",
                 default=False,
                 help="Trust remote code when loading tokenizer")
             parser.add_argument(
                 "--use_fast", type=lambda x: str(x).lower() == "true",
                 default=True,
                 help="Determines if a fast Rust-based tokenizer should be used")
             parser.add_argument(
                 "--dataset_name", type=str,
                 default="philschmid/gretel-synthetic-text-to-sql",
                 help="Hugging Face dataset name")
             parser.add_argument(
                 "--output_dir", type=str, default="gemma-31b-text-to-sql",
                 help="Directory to save model checkpoints")
         
             # LoRA arguments
             parser.add_argument(
                 "--lora_r", type=int, default=16,
                 help="LoRA attention dimension")
             parser.add_argument(
                 "--lora_alpha", type=int, default=32,
                 help="LoRA alpha scaling factor")
             parser.add_argument(
                 "--lora_dropout", type=float, default=0.05,
                 help="LoRA dropout probability")
             # SFTConfig arguments
             parser.add_argument(
                 "--max_length", type=int, default=1024,
                 help="Maximum sequence length")
             parser.add_argument(
                 "--num_train_epochs", type=int, default=3,
                 help="Number of training epochs")
             parser.add_argument(
                 "--per_device_train_batch_size", type=int, default=2,
                 help="Batch size per device during training")
             parser.add_argument(
                 "--gradient_accumulation_steps", type=int, default=32,
                 help="Gradient accumulation steps")
             parser.add_argument(
                 "--learning_rate", type=float, default=1e-5,
                 help="Learning rate")
             parser.add_argument(
                 "--logging_steps", type=int, default=10,
                 help="Log every X steps")
             parser.add_argument(
                 "--save_strategy", type=str, default="steps",
                 help="Checkpoint save strategy")
             parser.add_argument(
                 "--save_steps", type=int, default=100,
                 help="Save checkpoint every X steps")
             parser.add_argument(
                 "--push_to_hub", action='store_true',
                 help="Push model back up to HF")
             parser.add_argument(
                 "--hub_private_repo", type=lambda x: str(x).lower() == "true",
                 default=True,
                 help="Push to a private repo")
             return parser.parse_args()
         
         def main():
             args = get_args()
             # --- 1. Setup and Login ---
             if args.hf_token:
                 login(args.hf_token)
             # --- 2. Create and prepare the fine-tuning dataset ---
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
             tokenizer = AutoTokenizer.from_pretrained(
                 args.model_id,
                 trust_remote_code=args.trust_remote,
                 use_fast=args.use_fast,
             )
             if tokenizer.pad_token is None:
                 tokenizer.pad_token = tokenizer.eos_token
             # --- 4. Define the Formatting Function ---
             def formatting_func(example):
                 system_message = (
                     "You are a text to SQL query translator. Users will ask you "
                     "questions in English and you will generate a SQL query based "
                     "on the provided SCHEMA."
                 )
                 user_prompt = (
                     "Given the <USER_QUERY> and the <SCHEMA>, generate the "
                     "corresponding SQL command to retrieve the desired data, "
                     "considering the query's syntax, semantics, and schema "
                     "constraints.\n\n<SCHEMA>\n{context}\n</SCHEMA>\n\n"
                     "<USER_QUERY>\n{question}\n</USER_QUERY>\n"
                 )
         
                 messages = [
                     {"role": "system", "content": system_message},
                     {
                         "role": "user",
                         "content": user_prompt.format(
                             question=example["sql_prompt"],
                             context=example["sql_context"],
                         ),
                     },
                     {"role": "assistant", "content": example["sql"]}
                 ]
                 return tokenizer.apply_chat_template(messages, tokenize=False)
             # --- 5. Load Model and Apply PEFT ---
             config = AutoConfig.from_pretrained(args.model_id)
             config.use_cache = False
             print("Loading base model...")
             model = AutoModelForCausalLM.from_pretrained(
                 args.model_id,
                 config=config,
                 attn_implementation="sdpa",
                 torch_dtype=torch_dtype_obj,
             )
         
             peft_config = LoraConfig(
                 lora_alpha=args.lora_alpha,
                 lora_dropout=args.lora_dropout,
                 r=args.lora_r,
                 bias="none",
                 # Train only the text decoder projections; skip vision/audio modules.
                 target_modules=[
                     "q_proj", "k_proj", "v_proj", "o_proj",
                     "gate_proj", "up_proj", "down_proj",
                 ],
                 exclude_modules=(
                     r".*(vision_tower|audio_tower|embed_vision|embed_audio).*"),
                 task_type="CAUSAL_LM",
             )
             # --- 6. Configure Training Arguments ---
             training_args = SFTConfig(
                 output_dir=args.output_dir,
                 max_length=args.max_length,
                 num_train_epochs=args.num_train_epochs,
                 per_device_train_batch_size=args.per_device_train_batch_size,
                 gradient_accumulation_steps=args.gradient_accumulation_steps,
                 learning_rate=args.learning_rate,
                 logging_steps=args.logging_steps,
                 save_strategy=args.save_strategy,
                 save_steps=args.save_steps,
                 packing=False,
                 label_names=["domain"],
                 gradient_checkpointing=True,
                 gradient_checkpointing_kwargs={"use_reentrant": False},
                 optim="adamw_torch",
                 fp16=True if torch_dtype_obj == torch.float16 else False,
                 bf16=True if torch_dtype_obj == torch.bfloat16 else False,
                 max_grad_norm=0.3,
                 warmup_steps=0.03,
                 lr_scheduler_type="constant",
                 push_to_hub=args.push_to_hub,
                 hub_private_repo=args.hub_private_repo,
                 report_to="tensorboard",
             )
             # --- 7. Create Trainer and Start Training ---
             trainer = SFTTrainer(
                 model=model,
                 args=training_args,
                 peft_config=peft_config,
                 train_dataset=dataset["train"],
                 eval_dataset=dataset["test"],
                 processing_class=tokenizer,
                 formatting_func=formatting_func,
             )
             print("Starting training...")
             trainer.train()
             print("Training finished.")
             # --- 8. Save the final model ---
             print(f"Saving final model to {args.output_dir}")
             if trainer.is_fsdp_enabled:
                 trainer.accelerator.state.fsdp_plugin.set_state_dict_type(
                     "FULL_STATE_DICT")
             trainer.save_model(args.output_dir)
             if torch.distributed.is_initialized():
                 torch.distributed.destroy_process_group()
         
         if __name__ == "__main__":
             main()




### Use Docker and Cloud Build to create a fine-tuning container

  1. Create an Artifact Registry Docker Repository:
         
         gcloud artifacts repositories create gemma \
             --repository-format=docker \
             --location="${ARTIFACT_REPO_LOCATION}" \
             --description="Repository for Gemma fine tuning workload containers" || true

  2. In the `llm-finetuning-gemma` directory that you created in an earlier step, run the following command to create the fine-tuning image and push it to Artifact Registry.
         
         gcloud builds submit . \
             --substitutions=_ARTIFACT_REPO_LOCATION="${ARTIFACT_REPO_LOCATION}"

**Note:** Building and pushing the image might take 20 minutes or more. To view the build progress, open the link that the command provides with the output `Logs are available at`.
  3. Export the image URL. You use it at a later step in this tutorial:
         
         IMAGE_REGISTRY="${ARTIFACT_REPO_LOCATION}-docker.pkg.dev/${PROJECT_ID}"
         export IMAGE_URL="${IMAGE_REGISTRY}/gemma/finetune-gemma-gpu:2.0.0"




## Start your fine-tuning workload

To start your fine-tuning workload, do the following:

  1. Apply the finetune manifest to create the fine-tuning job:
         
         envsubst < finetune.yaml | kubectl apply -f -

Because you're using clusters in GKE Autopilot mode, it might take a few minutes to start your GPU enabled node.

  2. Monitor the job by running the following command:
         
         watch kubectl get pods

  3. After the pods are running, check the logs of the job:
         
         kubectl logs job.batch/finetune-job -f

The job resource downloads the model data then fine-tunes the model across all eight of the GPUs. The download takes around five minutes to complete. After the download is complete, the fine-tuning process takes approximately 45 minutes to complete. The job saves a checkpoint every 20 steps and pushes the fine-tuned Low-Rank Adaptation (LoRA) adapter to a private Hugging Face repository named `gemma-31b-text-to-sql`.

  4. After the job completes, get the URL of your fine-tuned model on Hugging Face, and then open the URL in your browser:
         
         HF_USERNAME=$(curl -s -H "Authorization: Bearer ${HF_TOKEN}" \
             https://huggingface.co/api/whoami-v2 | jq -r .name)
         echo "https://huggingface.co/${HF_USERNAME}/gemma-31b-text-to-sql"




## Monitor your workload

You can monitor the use of the GPUs in your GKE cluster to verify that your fine-tuning job is efficiently running. To do so, open the following link in your browser:
    
    
    echo "https://console.cloud.google.com/kubernetes/clusters/details/${CLUSTER_REGION}/${CLUSTER_NAME}/observability?mods=monitoring_api_prod&project=${PROJECT_ID}&pageState=(\"timeRange\":(\"duration\":\"PT1H\"),\"nav\":(\"section\":\"gpu\"),\"groupBy\":(\"groupByType\":\"namespacesTop5\"))"

When you monitor your workload, you can see the following:

  * **GPUs usage** : for a healthy fine-tuning job, you can expect to see the usage of all of your 8 GPUs rise and stabilize to a high level throughout your training.
  * **Job duration** : the job should take approximately 45 minutes to complete on the specified A4 cluster.



## Clean up

To avoid incurring additional charges, delete the resources created during this tutorial.

### Delete your resources

  1. To delete your fine-tuning job, run the following command:
         
         kubectl delete job finetune-job

  2. To delete your GKE cluster, run the following command:
         
         gcloud container clusters delete "${CLUSTER_NAME}" \
             --region="${CLUSTER_REGION}"

  3. To delete your Artifact Registry repository, run the following command:
         
         gcloud artifacts repositories delete gemma \
             --location="${ARTIFACT_REPO_LOCATION}"




## What's next

  * [Manage AI-optimized GKE clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters)

  * [Learn about recommended storage services for AI and ML workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/storage)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
