---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gemma3-finetune-a4-gke-multi-host-cluster/
title: Fine-tune Gemma 3 on a multi-host A4 GKE cluster \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:28:09.401833+00:00
---

# Fine-tune Gemma 3 on a multi-host A4 GKE cluster  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gemma3-finetune-a4-gke-multi-host-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Fine-tune Gemma 3 on a multi-host A4 GKE cluster Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to fine-tune a [Gemma 3](https://ai.google.dev/gemma/docs/core) large language model (LLM) on a multi-host GKE Autopilot cluster on Google Cloud. This cluster uses two A4 virtual machine (VM) instances with a total of 16 NVIDIA B200 GPUs.

The two main processes described in this tutorial are as follows:

  1. Deploy a high-performance, multi-host GKE cluster by using GKE Autopilot. As part of this deployment, you create a custom VM image with the necessary software pre-installed.
  2. After the cluster is deployed, you run a distributed fine-tuning job by using the set of scripts that accompany this tutorial. The job leverages the [Hugging Face Accelerate library](https://huggingface.co/docs/accelerate/en/usage_guides/fsdp).

**Important:** To complete this tutorial, you must have reserved the capacity to create an A4 VM. To learn more about your options for reserving capacity in AI Hypercomputer for a future date and time, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

This tutorial is intended for machine learning (ML) engineers, researchers, platform administrators and operators, and for data and AI specialists who are interested in deploying GKE clusters on Google Cloud to train LLMs.

## Objectives

  * Access the Gemma 3 model by using Hugging Face.

  * Prepare your environment.

  * Create and deploy an A4 GKE cluster.

  * Fine-tune the Gemma 3 model by using the Hugging Face Accelerate library with fully sharded data parallel (FSDP).

  * Monitor your job.

  * Clean up.




## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Compute Engine](https://cloud.google.com/compute/vm-instance-pricing)
  * [ Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine)
  * [ Filestore](https://docs.cloud.google.com/filestore/pricing)
  * [ Cloud Storage](https://docs.cloud.google.com/storage/pricing)
  * [ Cloud Logging](https://docs.cloud.google.com/stackdriver/pricing#logging-pricing-summary)



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

  7. Enable the required APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com container.googleapis.com file.googleapis.com logging.googleapis.com cloudresourcemanager.googleapis.com servicenetworking.googleapis.com

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

  13. Enable the required APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com container.googleapis.com file.googleapis.com logging.googleapis.com cloudresourcemanager.googleapis.com servicenetworking.googleapis.com

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: ` roles/compute.admin, roles/iam.serviceAccountUser, roles/cloudbuild.builds.editor, roles/artifactregistry.admin, roles/storage.admin, roles/serviceusage.serviceUsageAdmin `
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.
  15. Enable the default service account for your Google Cloud project: 
         
         export PROJECT_NUMBER="$(gcloud projects describe "PROJECT_ID" --format "value(project_number)")"
           gcloud iam service-accounts enable "${PROJECT_NUMBER}-compute@developer.gserviceaccount.com \
             --project=PROJECT_ID

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



## Access Gemma 3 by using Hugging Face

To use Hugging Face to access Gemma 3, do the following:

  1. [Sign in to Hugging Face](https://huggingface.co/google/gemma-3-27b-it)
  2. [Create a Hugging Face `write` access token](https://huggingface.co/docs/hub/security-tokens#how-to-manage-user-access-tokens).  
Click **Your Profile > Settings > Access tokens > +Create new token**.
  3. Copy and save the `write access` token value. You use it later in this tutorial.



## Prepare your environment

To prepare your environment, set the following:
    
    
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

  * PROJECT_ID: the name of the Google Cloud project where you want to create the GKE cluster.

  * CLUSTER_NAME: the name of the GKE cluster to create.

  * CLUSTER_REGION: the region where you want to create your GKE cluster. You can only create the cluster in the region where your reservation exists.

  * RESERVATION: the identifier for your reserved capacity.

  * HF_TOKEN: the Hugging Face access token that you created in the previous section.

  * ARTIFACT_REPO_LOCATION: the location where you want to create your Artifact Registry repository.

  * NUM_NODES: the number of nodes that you want the GKE cluster to have.

  * NETWORK: the network to use.




## Create a multi-host GKE cluster in Autopilot mode

Create a multi-host GKE cluster in Autopilot mode:
    
    
    gcloud container clusters create-auto "${CLUSTER_NAME}" \
        --project="${PROJECT_ID}" \
        --location="${CLUSTER_REGION}" \
        --release-channel=rapid

Creating the GKE cluster might take some time to complete. To verify that Google Cloud has finished creating your cluster, go to [Kubernetes clusters](https://console.cloud.google.com/kubernetes/list/overview) on the Google Cloud console.

## Get credentials for your GKE cluster

Configure `kubectl` to communicate with the newly-created GKE cluster by running the following command:
    
    
    gcloud container clusters get-credentials "${CLUSTER_NAME}" \
        --location="${CLUSTER_REGION}"

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
           args: [ 'build', '-t', '$_ARTIFACT_REPO_LOCATION-docker.pkg.dev/$PROJECT_ID/gemma/finetune-gemma-multihost-gpu:1.0.0', '.' ]
         images:
         - '$_ARTIFACT_REPO_LOCATION-docker.pkg.dev/$PROJECT_ID/gemma/finetune-gemma-multihost-gpu:1.0.0'

  3. Create a `Dockerfile` file to define the environment and install the dependencies required to complete the fine-tuning job:
         
         FROM nvidia/cuda:12.8.1-cudnn-devel-ubuntu24.04
         RUN apt-get update && \
             apt-get -y install python3 python3-dev gcc python3-pip python3-venv git curl vim
         RUN python3 -m venv /opt/venv
         ENV PATH="/opt/venv/bin:/usr/local/nvidia/bin:$PATH"
         ENV LD_LIBRARY_PATH="/usr/local/nvidia/lib64:$LD_LIBRARY_PATH"
         RUN pip3 install setuptools wheel packaging ninja
         RUN pip3 install torch torchvision torchaudio  --index-url https://download.pytorch.org/whl/cu128
         
         RUN pip3 install \
             transformers==4.53.3 \
             datasets==4.0.0 \
             accelerate==1.9.0 \
             evaluate==0.4.5 \
             bitsandbytes==0.46.1 \
             trl==0.19.1 \
             peft==0.16.0 \
             tensorboard==2.20.0 \
             protobuf==6.31.1 \
             sentencepiece==0.2.0
         COPY finetune.py /finetune.py
         COPY accel_fsdp_gemma3_config.yaml /accel_fsdp_gemma3_config.yaml
         CMD accelerate launch --config_file accel_fsdp_gemma3_config.yaml finetune.py

**Note:** This tutorial doesn't use the latest versions of NVIDIA and Pytorch dependencies. If you need newer dependencies, then see the [NVIDIA documentation](https://developer.nvidia.com/cuda-gpus) and the [Pytorch documentation](https://pytorch.org/get-started/locally/#linux-pip).
  4. Create the `accel_fsdp_gemma3_config.yaml` file. This configuration file directs Hugging Face Accelerate to split the tuning job across multiple GPUs.
         
         compute_environment: LOCAL_MACHINE
         debug: false
         distributed_type: FSDP
         downcast_bf16: 'no'
         enable_cpu_affinity: false
         fsdp_config:
           fsdp_activation_checkpointing: false
           fsdp_auto_wrap_policy: TRANSFORMER_BASED_WRAP
           fsdp_cpu_ram_efficient_loading: true
           fsdp_offload_params: false
           fsdp_reshard_after_forward: true
           fsdp_state_dict_type: FULL_STATE_DICT
           fsdp_transformer_layer_cls_to_wrap: Gemma3DecoderLayer
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

  5. Create the `finetune.yaml` file:
         
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
                           --config_file accel_fsdp_gemma3_config.yaml \
                           --num_machines ${NUM_NODES} \
                           --num_processes ${NUM_PROCESSES} \
                           --machine_rank ${JOB_COMPLETION_INDEX} \
                           --main_process_ip finetune-jobset-workers-0-0.finetune-jobset.default.svc.cluster.local \
                           --main_process_port 29500 \
                           finetune.py \
                           --model_id google/gemma-3-12b-pt \
                           --output_dir gemma-12b-text-to-sql \
                           --per_device_train_batch_size 8 \
                           --gradient_accumulation_steps 8 \
                           --num_train_epochs 3 \
                           --learning_rate 1e-5 \
                           --save_strategy steps \
                           --save_steps 100
                       resources:
                         limits:
                           nvidia.com/gpu: "8"
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

  6. Create the `finetune.py` file:
         
         import torch
         import argparse
         import subprocess
         from datasets import load_dataset
         from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, AutoConfig
         from peft import LoraConfig, prepare_model_for_kbit_training, get_peft_model
         from trl import SFTTrainer, SFTConfig
         from huggingface_hub import login
         
         def get_args():
             def str2bool(v):
                 if isinstance(v, bool):
                     return v
                 return v.lower() in ("yes", "true", "t", "1")
         
             parser = argparse.ArgumentParser()
             parser.add_argument("--model_id", type=str, default="google/gemma-3-12b-pt", help="Hugging Face model ID")
             parser.add_argument("--hf_token", type=str, default=None, help="Hugging Face token for private models")
             parser.add_argument("--trust_remote", type=str2bool, default=False, help="Trust remote code when loading tokenizer")
             parser.add_argument("--use_fast", type=str2bool, default=True, help="Determines if a fast Rust-based tokenizer should be used")
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
             parser.add_argument("--push_to_hub", action='store_true', help="Push model back up to HF")
             parser.add_argument("--hub_private_repo", type=str2bool, default=True, help="Push to a private repo")
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
             tokenizer = AutoTokenizer.from_pretrained(args.model_id, trust_remote_code=args.trust_remote, use_fast=args.use_fast)
             tokenizer.pad_token = tokenizer.eos_token
             gemma_chat_template = (
                 "{{ bos_token }}"
                 "{% if messages[0]['role'] == 'system' %}{{ messages[0]['content'] }}{% endif %}"
                 "{% for message in messages %}"
                 "{% if message['role'] == 'user' %}<start_of_turn>user\n{{ message['content'] }}<end_of_turn>\n{% elif message['role'] == 'assistant' %}<start_of_turn>model\n{{ message['content'] }}<end_of_turn>\n{% endif %}"
                 "{% endfor %}"
             )
             tokenizer.chat_template = gemma_chat_template
             # --- 4. Define the Formatting Function ---
             def formatting_func(example):
                 system_message = "You are a text to SQL query translator. Users will ask you questions in English and you will generate a SQL query based on the provided SCHEMA."
                 user_prompt = "Given the <USER_QUERY> and the <SCHEMA>, generate the corresponding SQL command to retrieve the desired data, considering the query's syntax, semantics, and schema constraints.\n\n<SCHEMA>\n{context}\n</SCHEMA>\n\n<USER_QUERY>\n{question}\n</USER_QUERY>\n"
         
                 messages = [
                     {"role": "user", "content": user_prompt.format(question=example["sql_prompt"], context=example["sql_context"])},
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
                 attn_implementation="eager",
                 torch_dtype=torch_dtype_obj,
             )
         
             model = prepare_model_for_kbit_training(model)
             peft_config = LoraConfig(
                 lora_alpha=args.lora_alpha,
                 lora_dropout=args.lora_dropout,
                 r=args.lora_r,
                 bias="none",
                 target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
                 task_type="CAUSAL_LM",
             )
             print("Applying PEFT configuration...")
             model = get_peft_model(model, peft_config)
             model.print_trainable_parameters()
             # --- 6. Configure Training Arguments ---
             training_args = SFTConfig(
                 output_dir=args.output_dir,
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
                 push_to_hub=args.push_to_hub,
                 hub_private_repo=args.hub_private_repo,
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
             trainer.save_model(args.output_dir)
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

  2. Install the JobSet custom resource definitions (CRDs) required for orchestrating multi-host workloads.
         
         kubectl apply --server-side -f https://github.com/kubernetes-sigs/jobset/releases/download/v0.12.0/manifests.yaml

JobSet is a Kubernetes extension used to manage groups of related jobs. For more information about JobSet, see the external [JobSet documentation](https://jobset.sigs.k8s.io/docs/overview/).

  3. In the `llm-finetuning-gemma` directory that you created in an earlier step, run the following command to create the fine-tuning image and push it to Artifact Registry.
         
         gcloud builds submit . --substitutions=_ARTIFACT_REPO_LOCATION="${ARTIFACT_REPO_LOCATION}"

  4. Export the image URL. You use it at a later step in this tutorial:
         
         export IMAGE_URL="${ARTIFACT_REPO_LOCATION}-docker.pkg.dev/${PROJECT_ID}/gemma/finetune-gemma-gpu:1.0.0"




## Start your fine-tuning workload

To start your fine-tuning workload, do the following:

  1. Apply the finetune manifest to create the fine-tuning job:
         
         envsubst '${RESERVATION} ${IMAGE_URL} ${NUM_NODES}' < finetune.yaml | kubectl apply -f -

Because you're using clusters in GKE Autopilot mode, it might take a few minutes to start your GPU enabled node.

  2. Monitor the job by running the following command:
         
         watch kubectl get pods

  3. Check the logs from the primary worker pod by running the following command:
         
         kubectl logs -l "job-name=finetune-jobset-workers-0" -f

The job resource downloads the model data then fine-tunes the model across all eight of the GPUs. The download takes around five minutes to complete. After the download is complete, the fine-tuning process takes approximately two hours and 30 minutes to complete.




## Monitor your workload

You can monitor the use of the GPUs in your GKE cluster to verify that your fine-tuning job is efficiently running. To do so, open the following link in your browser:
    
    
    echo "https://console.cloud.google.com/kubernetes/clusters/details/${CLUSTER_REGION}/${CLUSTER_NAME}/observability?mods=monitoring_api_prod&project=${PROJECT_ID}&pageState=("timeRange":("duration":"PT1H"),"nav":("section":"gpu"),"groupBy":("groupByType":"namespacesTop5"))"

When you monitor your workload, you can see the following:

  * **GPUs usage** : for a healthy fine-tuning job, you can expect to see the usage of all of your 8 GPUs rise and stabilize to a high level throughout your training.
  * **Job duration** : the job should take approximately 10 minutes to complete on the specified A4 cluster.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete your resources

  1. To delete your JobSet, run the following command:
         
         kubectl delete jobset finetune-jobset

  2. To delete your GKE cluster, run the following command:
         
         gcloud container clusters delete "${CLUSTER_NAME}" \
             --region="${CLUSTER_REGION}"

  3. To delete your Artifact Registry repository, run the following command:
         
         gcloud artifacts repositories delete gemma \
             --location="${ARTIFACT_REPO_LOCATION}" \
             --quiet




### Delete your project

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

## What's next

  * [Manage AI-optimized GKE clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters)

  * [Learn about recommended storage services for AI and ML workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/storage)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
