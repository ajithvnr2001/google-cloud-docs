---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gemma4-finetune-a4-gke-multi-host-cluster/
title: Fine-tune Gemma 4 on a multi-host A4 GKE cluster \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:28:10.434091+00:00
---

# Fine-tune Gemma 4 on a multi-host A4 GKE cluster  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gemma4-finetune-a4-gke-multi-host-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Fine-tune Gemma 4 on a multi-host A4 GKE cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This tutorial shows you how to fine-tune a [Gemma 4](https://ai.google.dev/gemma/docs/core) 31B large language model (`google/gemma-4-31b-it`) on a multi-host, multi-GPU Google Kubernetes Engine (GKE) Autopilot cluster on Google Cloud. This cluster uses two A4 (`a4-highgpu-8g`) virtual machine (VM) instances with a total of 16 NVIDIA B200 GPUs.

The three main processes described in this tutorial are as follows:

  1. Deploy a multi-host GKE cluster in Autopilot mode.
  2. Build a custom container image with the required fine-tuning dependencies by using Cloud Build.
  3. Orchestrate a distributed multi-host fine-tuning workload across all 16 GPUs by using Kubernetes [JobSet](https://jobset.sigs.k8s.io/docs/overview/) and the [Hugging Face Accelerate library](https://huggingface.co/docs/accelerate/en/usage_guides/fsdp) with Fully Sharded Data Parallel v2 (FSDP v2), pushing checkpoints to Hugging Face Hub.

**Important:** To complete this tutorial, you must have reserved the capacity to create two A4 VMs. To learn more about your options for reserving capacity in AI Hypercomputer for a future date and time, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

This tutorial is intended for machine learning (ML) engineers, researchers, platform administrators and operators, and data and AI specialists who deploy GKE clusters on Google Cloud to fine-tune LLMs across multiple hosts.

## Objectives

  * Access the Gemma 4 model by using Hugging Face.

  * Prepare your environment.

  * Create and deploy a multi-host A4 GKE cluster.

  * Fine-tune the Gemma 4 31B model across 16 GPUs by using Kubernetes `JobSet` and Hugging Face Accelerate with FSDP v2.

  * Monitor your job.

  * View the fine-tuned adapter weights on Hugging Face Hub.

  * Clean up.




## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Compute Engine](https://cloud.google.com/compute/vm-instance-pricing)
  * [ Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine)
  * [ Artifact Registry](https://docs.cloud.google.com/artifact-registry/pricing)
  * [ Cloud Build](https://docs.cloud.google.com/build/pricing)
  * [ Cloud Storage](https://docs.cloud.google.com/storage/pricing)
  * [ Cloud Logging](https://docs.cloud.google.com/stackdriver/pricing#logging-pricing-summary)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

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

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the Google Cloud CLI, and [install `kubectl`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl). If you use Cloud Shell, both tools are preinstalled.

  2. Enable the required APIs, if any aren't already enabled:

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com container.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com logging.googleapis.com cloudresourcemanager.googleapis.com servicenetworking.googleapis.com

  3. Enable the default Compute Engine service account for your Google Cloud project:
         
         export PROJECT_NUMBER="$(gcloud projects describe "YOUR_PROJECT_ID" --format "value(project_number)")"
         gcloud iam service-accounts enable "${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
             --project=YOUR_PROJECT_ID

  4. Grant the least-privilege IAM roles that the default Compute Engine service account needs to build the container image and run the fine-tuning workload:
         
         ROLES=(
           "roles/artifactregistry.writer"
           "roles/cloudbuild.builds.builder"
           "roles/logging.logWriter"
           "roles/monitoring.metricWriter"
           "roles/monitoring.viewer"
           "roles/stackdriver.resourceMetadata.writer"
           "roles/storage.objectViewer"
         )
         for role in "${ROLES[@]}"; do
           gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
               --member="serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
               --role="${role}" 1>/dev/null
         done
         unset ROLES

**Note:** This step grants only the predefined roles that this tutorial requires. Granting a basic role such as Editor (`roles/editor`) gives the service account many more permissions than it needs, and your organization's policies might block the grant. For more information, see [Best practices for working with service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts).
  5. Verify that the roles were granted to the default Compute Engine service account:
         
         echo "Displaying roles for ${PROJECT_NUMBER}-compute@developer.gserviceaccount.com:"
         gcloud projects get-iam-policy YOUR_PROJECT_ID \
             --flatten="bindings[].members" \
             --filter="bindings.members:serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
             --format="table(bindings.role)"

  6. Create local authentication credentials for your user account:
         
         gcloud auth application-default login

**Note:** If you use a local shell and an external identity provider (IdP), and you encounter an authentication error after running the preceding command, then [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).
  7. Enable OS Login for your project:
         
         gcloud compute project-info add-metadata \
             --metadata=enable-oslogin=TRUE \
             --project=YOUR_PROJECT_ID




## Access Gemma 4 by using Hugging Face

To use Hugging Face to access Gemma 4, complete the following steps:

  1. Sign in to Hugging Face and [accept the Gemma 4 license agreement](https://huggingface.co/google/gemma-4-31b-it).
  2. [Create a Hugging Face `write` access token](https://huggingface.co/docs/hub/security-tokens#how-to-manage-user-access-tokens).  
Click **Your Profile > Settings > Access tokens > +Create new token**.
  3. Copy and save the `write` access token value. You use this token to download the base model and push fine-tuned adapter checkpoints to Hugging Face Hub before GKE scales down the GPU nodes.



## Prepare your environment

To prepare your environment, set the following environment variables:
    
    
    export PROJECT_ID="YOUR_PROJECT_ID"
    export CLUSTER_NAME="YOUR_CLUSTER_NAME"
    export CLUSTER_REGION="YOUR_REGION"
    export RESERVATION="YOUR_RESERVATION_NAME"
    export HF_TOKEN="YOUR_HF_TOKEN"
    export ARTIFACT_REPO_LOCATION="YOUR_ARTIFACT_REGISTRY_LOCATION"
    export NUM_NODES="YOUR_NUMBER_OF_NODES"
    
    gcloud config set project "${PROJECT_ID}"
    gcloud config set billing/quota_project "${PROJECT_ID}"

Replace the following:

  * YOUR_PROJECT_ID: the ID of the Google Cloud project where you want to create the GKE cluster.

  * YOUR_CLUSTER_NAME: the name of the GKE cluster to create. This name must be 40 characters or less and be composed of lowercase alphanumeric characters and hyphens.

  * YOUR_REGION: the region where you want to create your GKE cluster. You can only create the cluster in the region where your reservation exists.

  * YOUR_RESERVATION_NAME: the identifier for your reserved capacity.

  * YOUR_HF_TOKEN: the Hugging Face `write` access token that you created in the previous section.

  * YOUR_ARTIFACT_REGISTRY_LOCATION: the Google Cloud region (for example, `us-central1`) where you want to create your Artifact Registry repository. To minimize image pull latency, use the same region that you specified for YOUR_REGION.

  * YOUR_NUMBER_OF_NODES: the number of A4 VM nodes in your fine-tuning job. For this multi-host tutorial with 16 NVIDIA B200 GPUs across two `a4-highgpu-8g` instances, set this value to `2`.




## Create a multi-host GKE cluster in Autopilot mode

Create a multi-host GKE cluster in Autopilot mode:
    
    
    gcloud container clusters create-auto "${CLUSTER_NAME}" \
        --project="${PROJECT_ID}" \
        --location="${CLUSTER_REGION}"

Creating the GKE cluster might take several minutes to complete. To verify that Google Cloud has finished creating your cluster, go to [Kubernetes clusters](https://console.cloud.google.com/kubernetes/list/overview) on the Google Cloud console.

## Configure kubectl to communicate with your GKE cluster

Configure `kubectl` to communicate with your GKE cluster:
    
    
    gcloud container clusters get-credentials "${CLUSTER_NAME}" \
        --location="${CLUSTER_REGION}"

## Create a Kubernetes secret for Hugging Face credentials

Create a Kubernetes secret to store your Hugging Face token:
    
    
    kubectl create secret generic hf-secret \
        --from-literal=hf_api_token="${HF_TOKEN}" \
        --dry-run=client -o yaml | kubectl apply -f -

## Prepare your workload

To prepare your workload, you do the following:

  1. Create workload scripts.

  2. Use Docker and Cloud Build to create a fine-tuning container.




### Create workload scripts

To create the configuration files and scripts that your fine-tuning workload uses, complete the following steps:

  1. Create a directory for the workload scripts. Use this directory as your working directory.
         
         mkdir llm-finetuning-gemma
         cd llm-finetuning-gemma

  2. Create the `cloudbuild.yaml` file to build your workload container image with Cloud Build and push it to Artifact Registry:
         
         steps:
         - name: 'gcr.io/cloud-builders/docker'
           args:
           - 'build'
           - '-t'
           - '$_ARTIFACT_REPO_LOCATION-docker.pkg.dev/$PROJECT_ID/gemma/finetune-gemma-multihost-gpu:2.0.0'
           - '.'
         images:
         - '$_ARTIFACT_REPO_LOCATION-docker.pkg.dev/$PROJECT_ID/gemma/finetune-gemma-multihost-gpu:2.0.0'
         options:
           logging: CLOUD_LOGGING_ONLY

  3. Create a `Dockerfile` file to define the environment and install the dependencies required to complete the fine-tuning job:
         
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
             "transformers>=5.5.0" \
             trl==0.29.1 \
             peft==0.18.1 \
             accelerate==1.13.0 \
             bitsandbytes==0.49.2 \
             datasets==4.8.4 \
             evaluate==0.4.5 \
             tensorboard==2.20.0 \
             protobuf==6.31.1 \
             sentencepiece==0.2.0
         WORKDIR /workspace
         COPY finetune.py /workspace/finetune.py
         COPY accel_fsdp_gemma4_config.yaml /workspace/accel_fsdp_gemma4_config.yaml
         CMD ["accelerate", "launch", "--config_file", "/workspace/accel_fsdp_gemma4_config.yaml", "/workspace/finetune.py"]

**Note:** This tutorial uses pinned library versions validated with Gemma 4 and FSDP v2 on NVIDIA B200 GPUs. If you need later versions, see the [NVIDIA documentation](https://developer.nvidia.com/cuda-gpus) and the [PyTorch documentation](https://pytorch.org/get-started/locally/#linux-pip).
  4. Create the `accel_fsdp_gemma4_config.yaml` file. This configuration directs Hugging Face Accelerate to shard `Gemma4TextDecoderLayer` across 16 GPUs on two hosts by using FSDP v2:
         
         compute_environment: LOCAL_MACHINE
         debug: false
         distributed_type: FSDP
         downcast_bf16: 'no'
         enable_cpu_affinity: false
         fsdp_config:
           fsdp_activation_checkpointing: false
           fsdp_auto_wrap_policy: TRANSFORMER_BASED_WRAP
           fsdp_cpu_ram_efficient_loading: false
           fsdp_offload_params: true
           fsdp_reshard_after_forward: true
           fsdp_state_dict_type: FULL_STATE_DICT
           fsdp_transformer_layer_cls_to_wrap: Gemma4TextDecoderLayer
           fsdp_version: 2
         machine_rank: 0
         main_training_function: main
         mixed_precision: bf16
         num_machines: 2
         num_processes: 16
         rdzv_backend: static
         same_network: true
         tpu_env: []
         tpu_use_cluster: false
         tpu_use_sudo: false
         use_cpu: false

  5. Create the `finetune.yaml` Kubernetes `JobSet` manifest:
         
         apiVersion: resource.k8s.io/v1
         kind: ResourceClaimTemplate
         metadata:
           name: mrdma
         spec:
           spec:
             devices:
               requests:
               - name: mrdma
                 exactly:
                   deviceClassName: mrdma.google.com
         ---
         apiVersion: jobset.x-k8s.io/v1alpha2
         kind: JobSet
         metadata:
           name: finetune-jobset
           namespace: default
         spec:
           failurePolicy:
             maxRestarts: 2
           replicatedJobs:
           - name: workers
             replicas: 1
             template:
               spec:
                 parallelism: ${NUM_NODES}
                 completions: ${NUM_NODES}
                 backoffLimit: 0
                 template:
                   metadata:
                     annotations:
                       kubectl.kubernetes.io/default-container: finetuner
                   spec:
                     terminationGracePeriodSeconds: 600
                     restartPolicy: OnFailure
                     nodeSelector:
                       cloud.google.com/compute-class: "Accelerator"
                       cloud.google.com/gke-accelerator: "nvidia-b200"
                       cloud.google.com/reservation-name: ${RESERVATION}
                       cloud.google.com/reservation-affinity: "specific"
                       cloud.google.com/gke-gpu-driver-version: latest
                     containers:
                     - name: finetuner
                       image: $IMAGE_URL
                       command: ["bash", "-c"]
                       args:
                       - |
                         NUM_PROCESSES=$(( ${NUM_NODES} * 8 ))
                         accelerate launch \
                           --config_file /workspace/accel_fsdp_gemma4_config.yaml \
                           --num_machines ${NUM_NODES} \
                           --num_processes ${NUM_PROCESSES} \
                           --machine_rank ${JOB_COMPLETION_INDEX} \
                           --main_process_ip finetune-jobset-workers-0-0.finetune-jobset.default.svc.cluster.local \
                           --main_process_port 29500 \
                           /workspace/finetune.py \
                           --base_model google/gemma-4-31b-it \
                           --new_model gemma-31b-text-to-sql \
                           --per_device_train_batch_size 4 \
                           --gradient_accumulation_steps 4 \
                           --num_train_epochs 3 \
                           --learning_rate 1e-5 \
                           --save_strategy steps \
                           --save_steps 15 \
                           --push_to_hub
                       resources:
                         limits:
                           nvidia.com/gpu: "8"
                           memory: "1000Gi"
                           ephemeral-storage: "350Gi"
                         requests:
                           nvidia.com/gpu: "8"
                           memory: "1000Gi"
                           ephemeral-storage: "350Gi"
                       env:
                       - name: HF_TOKEN
                         valueFrom:
                           secretKeyRef:
                             name: hf-secret
                             key: hf_api_token
                       - name: NUM_NODES
                         value: "${NUM_NODES}"
                       volumeMounts:
                       - mountPath: /dev/shm
                         name: dshm
                     volumes:
                     - name: dshm
                       emptyDir:
                         medium: Memory
                         sizeLimit: 64Gi

  6. Create the `finetune.py` supervised fine-tuning script:
         
         import argparse
         import torch
         from datasets import load_dataset
         from huggingface_hub import login
         from peft import LoraConfig
         from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer
         from trl import SFTConfig, SFTTrainer
         
         
         def get_args():
             def str2bool(v):
                 if isinstance(v, bool):
                     return v
                 return v.lower() in ("yes", "true", "t", "1")
         
             parser = argparse.ArgumentParser()
             parser.add_argument(
                 "--base_model",
                 "--model_id",
                 dest="base_model",
                 type=str,
                 default="google/gemma-4-31b-it",
                 help="Hugging Face model ID",
             )
             parser.add_argument(
                 "--hf_token",
                 type=str,
                 default=None,
                 help="Hugging Face token for gated models and Hub uploads",
             )
             parser.add_argument(
                 "--trust_remote",
                 type=str2bool,
                 default=False,
                 help="Trust remote code when loading tokenizer",
             )
             parser.add_argument(
                 "--use_fast",
                 type=str2bool,
                 default=True,
                 help="Determines if a fast Rust-based tokenizer should be used",
             )
             parser.add_argument(
                 "--dataset_name",
                 type=str,
                 default="philschmid/gretel-synthetic-text-to-sql",
                 help="Hugging Face dataset name",
             )
             parser.add_argument(
                 "--new_model",
                 "--output_dir",
                 dest="new_model",
                 type=str,
                 default="gemma-31b-text-to-sql",
                 help="Directory and repository name to save model checkpoints",
             )
         
             # LoRA arguments
             parser.add_argument(
                 "--lora_r", type=int, default=16, help="LoRA attention dimension"
             )
             parser.add_argument(
                 "--lora_alpha", type=int, default=32, help="LoRA alpha scaling factor"
             )
             parser.add_argument(
                 "--lora_dropout",
                 type=float,
                 default=0.05,
                 help="LoRA dropout probability",
             )
             # SFTConfig arguments
             parser.add_argument(
                 "--max_length",
                 type=int,
                 default=1024,
                 help="Maximum sequence length",
             )
             parser.add_argument(
                 "--num_train_epochs",
                 type=int,
                 default=3,
                 help="Number of training epochs",
             )
             parser.add_argument(
                 "--per_device_train_batch_size",
                 type=int,
                 default=4,
                 help="Batch size per device during training",
             )
             parser.add_argument(
                 "--gradient_accumulation_steps",
                 type=int,
                 default=4,
                 help="Gradient accumulation steps",
             )
             parser.add_argument(
                 "--learning_rate", type=float, default=1e-5, help="Learning rate"
             )
             parser.add_argument(
                 "--logging_steps", type=int, default=10, help="Log every X steps"
             )
             parser.add_argument(
                 "--save_strategy",
                 type=str,
                 default="steps",
                 help="Checkpoint save strategy",
             )
             parser.add_argument(
                 "--save_steps",
                 type=int,
                 default=15,
                 help="Save checkpoint every X steps",
             )
             parser.add_argument(
                 "--push_to_hub",
                 action="store_true",
                 help="Push model back up to Hugging Face Hub",
             )
             parser.add_argument(
                 "--hub_private_repo",
                 type=str2bool,
                 default=True,
                 help="Push to a private repository on Hugging Face Hub",
             )
             return parser.parse_args()
         
         
         def main():
             args = get_args()
             # --- 1. Setup and Login ---
             if args.hf_token:
                 login(args.hf_token)
             # --- 2. Create and prepare the fine-tuning dataset ---
             dataset = load_dataset(args.dataset_name, split="train")
             dataset = dataset.shuffle().select(range(12500))
             dataset = dataset.train_test_split(test_size=2500 / 12500)
             # --- 3. Configure Model and Tokenizer ---
             if torch.cuda.is_available() and torch.cuda.get_device_capability()[0] >= 8:
                 torch_dtype_obj = torch.bfloat16
             else:
                 torch_dtype_obj = torch.float16
             tokenizer = AutoTokenizer.from_pretrained(
                 args.base_model,
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
                     {"role": "assistant", "content": example["sql"]},
                 ]
                 return tokenizer.apply_chat_template(messages, tokenize=False)
         
             # --- 5. Load Model and Configure LoRA ---
             config = AutoConfig.from_pretrained(args.base_model)
             config.use_cache = False
             print("Loading base model...")
             model = AutoModelForCausalLM.from_pretrained(
                 args.base_model,
                 config=config,
                 attn_implementation="sdpa",
                 torch_dtype=torch_dtype_obj,
             )
         
             peft_config = LoraConfig(
                 lora_alpha=args.lora_alpha,
                 lora_dropout=args.lora_dropout,
                 r=args.lora_r,
                 bias="none",
                 target_modules=[
                     "q_proj",
                     "k_proj",
                     "v_proj",
                     "o_proj",
                     "gate_proj",
                     "up_proj",
                     "down_proj",
                 ],
                 exclude_modules=r".*(vision_tower|embed_vision|audio_tower|embed_audio).*",
                 task_type="CAUSAL_LM",
             )
             # --- 6. Configure Training Arguments ---
             training_args = SFTConfig(
                 output_dir=args.new_model,
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
                 fp16=torch_dtype_obj == torch.float16,
                 bf16=torch_dtype_obj == torch.bfloat16,
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
             print(f"Saving final model to {args.new_model}")
             if trainer.is_fsdp_enabled:
                 trainer.accelerator.state.fsdp_plugin.set_state_dict_type(
                     "FULL_STATE_DICT"
                 )
             trainer.save_model(args.new_model)
             if torch.distributed.is_initialized():
                 torch.distributed.destroy_process_group()
         
         
         if __name__ == "__main__":
             main()




### Use Docker and Cloud Build to create a fine-tuning container

  1. Create an Artifact Registry Docker repository:
         
         gcloud artifacts repositories create gemma \
             --repository-format=docker \
             --location="${ARTIFACT_REPO_LOCATION}" \
             --description="Repository for Gemma fine tuning workload containers" || true

  2. Install the `JobSet` custom resource definitions (CRDs) required for orchestrating multi-host workloads:
         
         kubectl apply --server-side \
             -f https://github.com/kubernetes-sigs/jobset/releases/download/v0.12.0/manifests.yaml

  3. In the `llm-finetuning-gemma` directory that you created in an earlier step, submit the container build to Cloud Build:
         
         gcloud builds submit . \
             --substitutions=_ARTIFACT_REPO_LOCATION="${ARTIFACT_REPO_LOCATION}"

**Note:** Building and pushing the CUDA and PyTorch container image takes approximately 20 minutes to complete. Because `cloudbuild.yaml` sets `logging: CLOUD_LOGGING_ONLY`, the command outputs a link (`Logs are available at [...]`) that you can open in the Google Cloud console to monitor real-time build progress.
  4. Export the multi-host container image URL. You use it at a later step in this tutorial, when you deploy the `JobSet` manifest:
         
         IMAGE_REGISTRY="${ARTIFACT_REPO_LOCATION}-docker.pkg.dev/${PROJECT_ID}"
         export IMAGE_URL="${IMAGE_REGISTRY}/gemma/finetune-gemma-multihost-gpu:2.0.0"




## Start your fine-tuning workload

To deploy and monitor your distributed fine-tuning workload, complete the following steps:

  1. Substitute environment variables into the fine-tuning manifest to create the fine-tuning job:
         
         envsubst '${RESERVATION} ${IMAGE_URL} ${NUM_NODES}' < finetune.yaml \
             | kubectl apply -f -

Because your cluster runs in GKE Autopilot mode, it might take a few minutes to provision the two GPU-enabled A4 nodes and pull the container image.

  2. Watch the worker pods until both pods transition to the `Running` status:
         
         watch kubectl get pods

  3. After the worker pods transition to `Running`, stream the training logs:
         
         kubectl logs -l "job-name=finetune-jobset-workers-0" -f

**Note:** `kubectl logs` only outputs training logs after the worker pods enter the `Running` state. Each worker downloads the Gemma 4 31B model weights (this takes approximately five minutes) and then runs distributed FSDP v2 fine-tuning across all 16 GPUs. Checkpoints are saved every 15 steps and uploaded automatically to your private Hugging Face Hub repository at `https://huggingface.co/YOUR_HF_USERNAME/gemma-31b-text-to-sql`.



## Monitor your workload

You can monitor GPU utilization across your GKE cluster to verify that all 16 GPUs across both A4 hosts are actively processing training steps. Generate and open the observability link in your browser:
    
    
    echo "https://console.cloud.google.com/kubernetes/clusters/details/${CLUSTER_REGION}/${CLUSTER_NAME}/observability?mods=monitoring_api_prod&project=${PROJECT_ID}&pageState=(\"timeRange\":(\"duration\":\"PT1H\"),\"nav\":(\"section\":\"gpu\"),\"groupBy\":(\"groupByType\":\"namespacesTop5\"))"

When you monitor your workload, expect the following behavior:

  * **GPU utilization** : For a healthy distributed fine-tuning job, you can expect to see GPU utilization across all 16 NVIDIA B200 GPUs rise and stabilize near 95%–100% during training steps.
  * **Job duration** : Across two `a4-highgpu-8g` nodes (16 B200 GPUs), the 3-epoch fine-tuning job takes approximately 2 and a half hours to complete.



## View your fine-tuned adapter weights

When training finishes, view your fine-tuned LoRA adapter weights and checkpoints on Hugging Face Hub at `https://huggingface.co/YOUR_HF_USERNAME/gemma-31b-text-to-sql`.

## Clean up

To avoid incurring additional charges, delete the resources created during this tutorial.

### Delete your resources

  1. Delete the fine-tuning `JobSet`:
         
         kubectl delete jobset finetune-jobset

  2. Delete your GKE cluster:
         
         gcloud container clusters delete "${CLUSTER_NAME}" \
             --region="${CLUSTER_REGION}"

  3. Delete your Artifact Registry repository:
         
         gcloud artifacts repositories delete gemma \
             --location="${ARTIFACT_REPO_LOCATION}" \
             --quiet




## What's next

  * [Manage AI-optimized GKE clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters)

  * [Learn about recommended storage services for AI and ML workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/storage)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
