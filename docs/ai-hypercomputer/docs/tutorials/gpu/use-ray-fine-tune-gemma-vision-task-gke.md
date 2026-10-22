---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/use-ray-fine-tune-gemma-vision-task-gke/
title: Use Ray to fine-tune Gemma 3 for vision tasks on GKE \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:14:15.091116+00:00
---

# Use Ray to fine-tune Gemma 3 for vision tasks on GKE  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/use-ray-fine-tune-gemma-vision-task-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Use Ray to fine-tune Gemma 3 for vision tasks on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This tutorial shows you how to fine-tune a Gemma 3 model by using the Ray framework on a multi-node GKE cluster. The cluster uses two A4 virtual machine (VM) instances, each with eight NVIDIA B200 GPUs attached.

**Important:** To complete this tutorial, you must have reserved the capacity to create two A4 VMs. To learn more about your options for reserving capacity in AI Hypercomputer for a future date and time, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

The content of this tutorial is divided into two parts:

  1. Preparing the Ray Cluster on top of a GKE Autopilot cluster.
  2. Running distributed training job, utilizing 2 A4 instances, with 8 B200 GPUs each.



This tutorial is intended for machine learning (ML) engineers, researchers, platform administrators and operators, and for data and AI specialists who are interested in distributing an AI workload across multiple nodes and GPUs.

## Objectives

  * Access a Gemma 3 model by using Hugging Face.

  * Prepare your environment.

  * Create a GKE Autopilot cluster with the Ray Operator installed on it.

  * Configure the Ray Cluster on the GKE cluster to accept Ray Jobs.

  * Configure and run a Ray Job that tunes the Gemma 3 model based on visual input.

  * Monitor your workload.

  * Clean up.




## Costs

In this document, you use the following billable components of Google Cloud: 

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
         
         gcloud services enable  compute.googleapis.com logging.googleapis.com cloudresourcemanager.googleapis.com servicenetworking.googleapis.com container.googleapis.com

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
         
         gcloud services enable  compute.googleapis.com logging.googleapis.com cloudresourcemanager.googleapis.com servicenetworking.googleapis.com container.googleapis.com

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: ` roles/compute.admin, roles/iam.serviceAccountUser, roles/file.editor, roles/storage.admin, roles/container.clusterAdmin, roles/serviceusage.serviceUsageAdmin `
         
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
  18. [Sign in to or create a Hugging Face account](https://huggingface.co/login).



## Access Gemma 3 by using Hugging Face

To use Hugging Face to access Gemma 3, do the following:

  1. [Sign the consent agreement to use Gemma 3](https://huggingface.co/google/gemma-3-12b-pt).

  2. [Create a Hugging Face `read access` token](https://huggingface.co/docs/hub/security-tokens#how-to-manage-user-access-tokens).

  3. Copy and save the `read access` token value. You use it later in this tutorial.




## Prepare your environment

Prepare your environment by configuring the necessary settings and setting the environment variables.

Run the following:
    
    
    export PROJECT_ID="YOUR_PROJECT_ID"
    export RESERVATION="YOUR_RESERVATION_NAME"
    export REGION="YOUR_REGION"
    export CLUSTER_NAME="YOUR_CLUSTER_NAME"
    export HF_TOKEN="YOUR_HF_TOKEN"
    export RAY_SA="YOUR_RAY_SA"
    export GSA_NAME="YOUR_GSA_NAME"
    export GCS_BUCKET="YOUR_GCS_BUCKET"
    
    gcloud config set project $PROJECT_ID
    gcloud config set billing/quota_project $PROJECT_ID

Replace the following:

  * `YOUR_PROJECT_ID`: the name of the Google Cloud project where you want to create the GKE cluster.
  * `YOUR_RESERVATION_NAME`: the URL of the reservation that you want to use to create your cluster. Based on the project in which the reservation exists, specify one of the following values: 
    * The reservation exists in your project: Specify the reservation name (e.g., `my-reservation`).
    * The reservation exists in a different project: Specify the full path in the format `projects/RESERVATION_PROJECT_ID/reservations/RESERVATION_NAME`.
  * `YOUR_REGION`: the region where you want to create your GKE cluster. You can only create the cluster in the region where your reservation exists.
  * `YOUR_CLUSTER_NAME`: the name of the GKE cluster to create.
  * `YOUR_HF_TOKEN`: the Hugging Face token that you created in an earlier step.
  * `YOUR_RAY_SA`: the Service Account name inside the Kubernetes cluster.
  * `YOUR_GSA_NAME`: the name of the Google Service Account.
  * `YOUR_GCS_BUCKET`: the name of the bucket where you store the results from the training checkpoint.



## Create a GKE cluster in Autopilot mode

To create a GKE cluster in Autopilot mode, run the following:
    
    
    gcloud container clusters create-auto $CLUSTER_NAME \
        --enable-ray-operator \
        --enable-ray-cluster-monitoring \
        --enable-ray-cluster-logging \
        --location=$REGION

It might take some time to complete the creation of the GKE cluster. To verify if Google Cloud has finished creating your cluster, go to [Kubernetes clusters](https://console.cloud.google.com/kubernetes/list/overview) on the Google Cloud console.

## Create a Kubernetes secret for Hugging Face credentials

In Cloud Shell, to create a Kubernetes secret for Hugging Face credentials, do the following:

  1. Configure `kubectl` to connect to your cluster:
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
             --region=$REGION

  2. Create a Kubernetes secret to store your Hugging Face token:
         
         kubectl create secret generic hf-secret \
             --from-literal=hf_api_token=$HF_TOKEN \
             --dry-run=client -o yaml | kubectl apply -f -




## Create the Cloud Storage bucket

If you want to use a new bucket to store your training artifacts, run the following:
    
    
    gcloud storage buckets create gs://$GCS_BUCKET --location=$REGION

If you want to use an existing bucket, you can skip this step. However, you must ensure that your bucket is in the same region as your cluster.

## Create an IAM service account

In Cloud Shell, to create an IAM service account (also known as a Google service account, or GSA) and grant it permissions to access your Cloud Storage bucket, do the following:

  1. Create an IAM service account:
         
         gcloud iam service-accounts create $GSA_NAME \
             --project=$PROJECT_ID \
             --description="Account for Ray to save Gemma training results" \
             --display-name="Ray Gemma Training SA"

  2. Grant the Storage Admin role (`roles/storage.admin`) to your IAM service account for your Cloud Storage bucket:
         
         gcloud storage buckets add-iam-policy-binding gs://${GCS_BUCKET#gs://} \
             --member="serviceAccount:$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com" \
             --role="roles/storage.admin"




## Create Kubernetes Service Account

In Cloud Shell, create a Kubernetes Service Account and configure Workload Identity to grant Ray pods access to Google Cloud resources:

  1. Create a Kubernetes Service Account: 
         
         kubectl create serviceaccount $RAY_SA \
             --dry-run=client -o yaml | kubectl apply -f -

  2. Bind your Kubernetes Service Account to the IAM service account that you previously created to enable Workload Identity: 
         
         gcloud iam service-accounts add-iam-policy-binding $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
             --project=$PROJECT_ID \
             --role="roles/iam.workloadIdentityUser" \
             --member="serviceAccount:$PROJECT_ID.svc.id.goog[default/$RAY_SA]"

  3. Annotate your Kubernetes Service Account with the email address of the IAM service account: 
         
         kubectl annotate serviceaccount $RAY_SA iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com --overwrite




## Save your training code as a ConfigMap

To avoid the need to embed your training script into a container image, you store it as a ConfigMap in your cluster. This ConfigMap is mounted onto the Pod file systems, which lets you update the training script without having to recreate the entire Ray cluster.

To store your training script as a ConfigMap in your cluster, complete the following steps:

  1. Create a directory with the name `code`, and in that directory, create a file with the name `vision_train.py`.

  2. Copy the following code into the `vision_train.py` file:
         
         import argparse
         import datetime
         import ray
         import ray.train.huggingface.transformers
         import torch
         from PIL import Image
         from datasets import load_dataset
         from peft import LoraConfig
         from ray.train import ScalingConfig, RunConfig
         from ray.train.torch import TorchTrainer
         from transformers import AutoProcessor, AutoModelForImageTextToText, BitsAndBytesConfig
         from trl import SFTConfig
         from trl import SFTTrainer
         
         # System message for the assistant
         system_message = "You are an expert product description writer for Amazon."
         
         # User prompt that combines the user query and the schema
         user_prompt = """Create a Short Product description based on the provided <PRODUCT> and <CATEGORY> and image.
         Only return description. The description should be SEO optimized and for a better mobile search experience.
         
         <PRODUCT>
         {product}
         </PRODUCT>
         
         <CATEGORY>
         {category}
         </CATEGORY>
         """
         
         def get_args():
             parser = argparse.ArgumentParser()
             parser.add_argument("--model_id", type=str, default="google/gemma-3-4b-it", help="Hugging Face model ID")
             # parser.add_argument("--hf_token", type=str, default=None, help="Hugging Face token for private models")
             parser.add_argument("--dataset_name", type=str, default="philschmid/amazon-product-descriptions-vlm", help="Hugging Face dataset name")
             parser.add_argument("--output_dir", type=str, default="gemma-3-4b-seo-optimized", help="Directory to save model checkpoints")
             parser.add_argument("--gcs_bucket", type=str, required=True, help="storage bucket name used to synchronize tasks and save checkpoints")
             parser.add_argument("--push_to_hub", help="Push model to Hugging Face hub", action="store_true")
         
             # LoRA arguments
             parser.add_argument("--lora_r", type=int, default=16, help="LoRA attention dimension")
             parser.add_argument("--lora_alpha", type=int, default=16, help="LoRA alpha scaling factor")
             parser.add_argument("--lora_dropout", type=float, default=0.05, help="LoRA dropout probability")
         
             # SFTConfig arguments
             parser.add_argument("--max_seq_length", type=int, default=512, help="Maximum sequence length")
             parser.add_argument("--num_train_epochs", type=int, default=3, help="Number of training epochs")
             parser.add_argument("--per_device_train_batch_size", type=int, default=1, help="Batch size per device during training")
             parser.add_argument("--gradient_accumulation_steps", type=int, default=4, help="Gradient accumulation steps")
             parser.add_argument("--learning_rate", type=float, default=2e-4, help="Learning rate")
             parser.add_argument("--logging_steps", type=int, default=10, help="Log every X steps")
             parser.add_argument("--save_strategy", type=str, default="epoch", help="Checkpoint save strategy")
             parser.add_argument("--save_steps", type=int, default=100, help="Save checkpoint every X steps")
         
             return parser.parse_args()
         
         # Convert dataset to OAI messages
         def format_data(sample):
             return {
                 "messages": [
                     {
                         "role": "system",
                         "content": [{"type": "text", "text": system_message}],
                     },
                     {
                         "role": "user",
                         "content": [
                             {
                                 "type": "text",
                                 "text": user_prompt.format(
                                     product=sample["Product Name"],
                                     category=sample["Category"],
                                 ),
                             },
                             {
                                 "type": "image",
                                 "image": sample["image"],
                             },
                         ],
                     },
                     {
                         "role": "assistant",
                         "content": [{"type": "text", "text": sample["description"]}],
                     },
                 ],
             }
         
         def process_vision_info(messages: list[dict]) -> list[Image.Image]:
             image_inputs = []
             # Iterate through each conversation
             for msg in messages:
                 # Get content (ensure it's a list)
                 content = msg.get("content", [])
                 if not isinstance(content, list):
                     content = [content]
         
                 # Check each content element for images
                 for element in content:
                     if isinstance(element, dict) and ("image" in element or element.get("type") == "image"):
                         # Get the image and convert to RGB
                         if "image" in element:
                             image = element["image"]
                         else:
                             image = element
                         image_inputs.append(image.convert("RGB"))
             return image_inputs
         
         def train(args):
             # Load dataset from the hub
             dataset = load_dataset(args.dataset_name, split="train")
         
             # Convert dataset to OAI messages
             # need to use list comprehension to keep Pil.Image type, .mape convert image to bytes
             dataset = [format_data(sample) for sample in dataset]
         
             # Hugging Face model id
             model_id = args.model_id
         
             # Check if GPU benefits from bfloat16
             if torch.cuda.get_device_capability()[0] < 8:
                 raise ValueError("GPU does not support bfloat16, please use a GPU that supports bfloat16.")
         
             # Define model init arguments
             model_kwargs = dict(
                 attn_implementation="eager",  # Use "flash_attention_2" when running on Ampere or newer GPU
                 torch_dtype=torch.bfloat16,  # What torch dtype to use, defaults to auto
                 # device_map="auto",  # Let torch decide how to load the model
             )
         
             # BitsAndBytesConfig int-4 config
             model_kwargs["quantization_config"] = BitsAndBytesConfig(
                 load_in_4bit=True,
                 bnb_4bit_use_double_quant=True,
                 bnb_4bit_quant_type="nf4",
                 bnb_4bit_compute_dtype=model_kwargs["torch_dtype"],
                 bnb_4bit_quant_storage=model_kwargs["torch_dtype"],
             )
         
             # Load model and tokenizer
             model = AutoModelForImageTextToText.from_pretrained(model_id, **model_kwargs)
             processor = AutoProcessor.from_pretrained(model_id, use_fast=True)
         
             peft_config = LoraConfig(
                 lora_alpha=args.lora_alpha,
                 lora_dropout=args.lora_dropout,
                 r=args.lora_r,
                 bias="none",
                 target_modules="all-linear",
                 task_type="CAUSAL_LM",
                 modules_to_save=[
                     "lm_head",
                     "embed_tokens",
                 ],
             )
         
             args = SFTConfig(
                 output_dir=args.output_dir,  # directory to save and repository id
                 num_train_epochs=args.num_train_epochs,  # number of training epochs
                 per_device_train_batch_size=args.per_device_train_batch_size,  # batch size per device during training
                 gradient_accumulation_steps=args.gradient_accumulation_steps,  # number of steps before performing a backward/update pass
                 gradient_checkpointing=True,  # use gradient checkpointing to save memory
                 optim="adamw_torch_fused",  # use fused adamw optimizer
                 logging_steps=args.logging_steps,  # log every N steps
                 save_strategy=args.save_strategy,  # save checkpoint every epoch
                 learning_rate=args.learning_rate,  # learning rate, based on QLoRA paper
                 bf16=True,  # use bfloat16 precision
                 max_grad_norm=0.3,  # max gradient norm based on QLoRA paper
                 warmup_ratio=0.03,  # warmup ratio based on QLoRA paper
                 lr_scheduler_type="constant",  # use constant learning rate scheduler
                 push_to_hub=args.push_to_hub,  # push model to hub
                 report_to="tensorboard",  # report metrics to tensorboard
                 gradient_checkpointing_kwargs={
                     "use_reentrant": False
                 },  # use reentrant checkpointing
                 dataset_text_field="",  # need a dummy field for collator
                 dataset_kwargs={"skip_prepare_dataset": True},  # important for collator
             )
             args.remove_unused_columns = False  # important for collator
         
             # Create a data collator to encode text and image pairs
             def collate_fn(examples):
                 texts = []
                 images = []
                 for example in examples:
                     image_inputs = process_vision_info(example["messages"])
                     text = processor.apply_chat_template(
                         example["messages"], add_generation_prompt=False, tokenize=False
                     )
                     texts.append(text.strip())
                     images.append(image_inputs)
         
                 # Tokenize the texts and process the images
                 batch = processor(text=texts, images=images, return_tensors="pt", padding=True)
         
                 # The labels are the input_ids, and we mask the padding tokens and image tokens in the loss computation
                 labels = batch["input_ids"].clone()
         
                 # Mask image tokens
                 boi_token = processor.tokenizer.special_tokens_map.get("boi_token")
                 image_token_id = processor.tokenizer.convert_tokens_to_ids(boi_token) if boi_token else None
         
                 # Mask tokens for not being used in the loss computation
                 labels[labels == processor.tokenizer.pad_token_id] = -100
                 if image_token_id is not None:
                     labels[labels == image_token_id] = -100
                 labels[labels == 262144] = -100
         
                 batch["labels"] = labels
                 return batch
         
             trainer = SFTTrainer(
                 model=model,
                 args=args,
                 train_dataset=dataset,
                 peft_config=peft_config,
                 processing_class=processor,
                 data_collator=collate_fn,
             )
         
             callback = ray.train.huggingface.transformers.RayTrainReportCallback()
             trainer.add_callback(callback)
             trainer = ray.train.huggingface.transformers.prepare_trainer(trainer)
         
             # Start training, the model will be automatically saved to the Hub and the output directory
             trainer.train()
         
             # Save the final model again to the Hugging Face Hub
             trainer.save_model()
         
         if __name__ == "__main__":
             args = get_args()
             print("Starting training task!")
             training_name = f"gemma_vision_train_{datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}"
         
             gcs_bucket = args.gcs_bucket
             if not gcs_bucket.startswith("gs://"):
                 gcs_bucket = "gs://" + gcs_bucket
         
             run_config = RunConfig(
                 storage_path=gcs_bucket,
                 name=training_name,
             )
             scaling_config = ScalingConfig(num_workers=16, use_gpu=True, accelerator_type="B200")
             ray_trainer = TorchTrainer(train, train_loop_config=args, scaling_config=scaling_config, run_config=run_config)
             print("Commencing training!")
             result = ray_trainer.fit()
         

  3. Save the file.

  4. Create a ConfigMap object in your cluster:
         
         kubectl create cm ray-job-cm --from-file=code -o yaml --dry-run=client | kubectl apply -f -

To update the training script, you rerun the preceding command. It might take a minute before any changes propagate to all the pods.



## Configure Ray Cluster

  1. To create a Ray Cluster in your GKE cluster, save the following YAML as a file with the name `ray_cluster.yaml`.
         
         apiVersion: ray.io/v1
         kind: RayCluster
         metadata:
           name: gemma3-tuning
         spec:
           rayVersion: '2.48.0'
           headGroupSpec:
             rayStartParams:
               dashboard-host: '0.0.0.0'
             template:
               metadata:
               spec:
                 serviceAccountName: $RAY_SA
                 containers:
                 - name: ray-head
                   image: rayproject/ray:2.48.0
                   ports:
                   - containerPort: 6379
                     name: gcs
                   - containerPort: 8265
                     name: dashboard
                   - containerPort: 10001
                     name: client
                   resources:
                     limits:
                       cpu: "24"
                       ephemeral-storage: "9Gi"
                       memory: "64Gi"
                     requests:
                       cpu: "24"
                       ephemeral-storage: "9Gi"
                       memory: "64Gi"
                   env:
                     - name: HF_TOKEN
                       valueFrom:
                         secretKeyRef:
                           name: hf-secret
                           key: hf_api_token
                   volumeMounts:
                     - name: job-code
                       mountPath: /code/
                     - mountPath: /mnt/local-ssd/
                       name: local-storage
                 volumes:
                   - name: job-code
                     configMap:
                       name: ray-job-cm
                   - name: local-storage
                     emptyDir: { }
           workerGroupSpecs:
           - replicas: 2
             minReplicas: 1
             maxReplicas: 5
             groupName: gpu-group
             rayStartParams: {}
             template:
               spec:
                 serviceAccountName: $RAY_SA
                 containers:
                 - name: ray-worker
                   image: rayproject/ray:2.48.0-gpu
                   resources:
                     limits:
                       nvidia.com/gpu: "8"
                       cpu: "80"
                       memory: "320Gi"
                     requests:
                       nvidia.com/gpu: "8"
                       cpu: "80"
                       memory: "320Gi"
                   env:
                     - name: HF_TOKEN
                       valueFrom:
                         secretKeyRef:
                           name: hf-secret
                           key: hf_api_token
                   volumeMounts:
                     - name: job-code
                       mountPath: /code/
                     - mountPath: /mnt/local-ssd/
                       name: local-storage
                 volumes:
                   - name: job-code
                     configMap:
                       name: ray-job-cm
                   - name: local-storage
                     emptyDir: { }
                 nodeSelector:
                   cloud.google.com/gke-accelerator: nvidia-b200
                   cloud.google.com/reservation-name: $RESERVATION
                   cloud.google.com/reservation-affinity: "specific"
                   cloud.google.com/gke-gpu-driver-version: latest

  2. Apply this YAML definition to your cluster by using the following command:
         
         envsubst < ray_cluster.yaml | kubectl apply -f -

The `$RESERVATION` flag is automatically replaced with the name you configured as environment variable. 

Ray Operator creates the raylet pods, which in turn triggers autoscaling of the cluster to provide those pods with the appropriate nodes. Three pods are created in your cluster: one head node, and two worker nodes. The worker nodes are equipped with the B200 GPUs.

  3. To verify that all three of the pods are ready, run the following:
         
         kubectl get pods

The pod list of a ready Ray Cluster is similar to the following: 
         
         NAME                                   READY   STATUS    RESTARTS   AGE
         gemma3-tuning-gpu-group-worker-s4h8f   2/2     Running   0          16m
         gemma3-tuning-gpu-group-worker-stg5f   2/2     Running   0          5m34s
         gemma3-tuning-head-zbdvp               2/2     Running   0          16m
         




## Schedule a training job

  1. Save the following as a `ray_job.yaml` file:
         
         apiVersion: ray.io/v1
         kind: RayJob
         metadata:
           name: test-ray-job
         spec:
           entrypoint: python /code/vision_train.py --gcs_bucket $GCS_BUCKET
           runtimeEnvYAML: |
             pip:
               - torch==2.8.0
               - torchvision==0.23.0
               - ray==2.48.0
               - transformers==4.55.2
               - datasets==4.0.0
               - evaluate==0.4.5
               - accelerate==1.10.0
               - pillow==11.3.0
               - bitsandbytes==0.47.0
               - trl==0.21.0
               - peft==0.17.0
           clusterSelector:
             ray.io/cluster: gemma3-tuning
         

  2. Submit the RayJob definition to your RayCluster:
         
         envsubst < ray_job.yaml | kubectl apply -f -

  3. Check that a new Pod is in your cluster:
         
         kubectl get pods

Make a note of the full name of the `test-ray-job-` Pod that you see in the output. This name is unique to your job.

  4. Inspect the progress of your training. Replace `gemma-training-ray-job-UNIQUE_ID` with the unique Pod name that you noted in the previous step.
         
         kubectl logs -f <test-ray-job-UNIQUE_ID>

The output that you see is similar to the following:
         
         2025-08-20 08:29:34,966 INFO cli.py:41 -- Job submission server address: http://gemma3-tuning-head-svc.default.svc.cluster.local:8265
         2025-08-20 08:29:34,991 SUCC cli.py:65 -- -----------------------------------------------
         2025-08-20 08:29:34,991 SUCC cli.py:66 -- Job 'test-ray-job-82mm7' submitted successfully
         2025-08-20 08:29:34,991 SUCC cli.py:67 -- -----------------------------------------------
         2025-08-20 08:29:34,992 INFO cli.py:291 -- Next steps
         2025-08-20 08:29:34,992 INFO cli.py:292 -- Query the logs of the job:
         2025-08-20 08:29:34,992 INFO cli.py:294 -- ray job logs test-ray-job-82mm7
         2025-08-20 08:29:34,992 INFO cli.py:296 -- Query the status of the job:
         2025-08-20 08:29:34,992 INFO cli.py:298 -- ray job status test-ray-job-82mm7
         2025-08-20 08:29:34,992 INFO cli.py:300 -- Request the job to be stopped:
         2025-08-20 08:29:34,992 INFO cli.py:302 -- ray job stop test-ray-job-82mm7
         2025-08-20 08:29:35,003 INFO cli.py:312 -- Tailing logs until the job exits (disable with --no-wait):
         2025-08-20 08:29:34,982 INFO job_manager.py:531 -- Runtime env is setting up.
         Starting training task!
         Commencing training!
         2025-08-20 08:30:08,498 INFO worker.py:1606 -- Using address 10.76.0.17:6379 set in the environment variable RAY_ADDRESS
         2025-08-20 08:30:08,506 INFO worker.py:1747 -- Connecting to existing Ray cluster at address: 10.76.0.17:6379...
         2025-08-20 08:30:08,527 INFO worker.py:1918 -- Connected to Ray cluster. View the dashboard at 10.76.0.17:8265
         2025-08-20 08:30:08,701 INFO tune.py:253 -- Initializing Ray automatically. For cluster usage or custom Ray initialization, call `ray.init(...)` before `<FrameworkTrainer>(...)`.
         2025-08-20 08:30:08,951 WARNING tune_controller.py:2132 -- The maximum number of pending trials has been automatically set to the number of available cluster CPUs, which is high (519 CPUs/pending trials). If you're running an experiment with a large number of trials, this could lead to scheduling overhead. In this case, consider setting the `TUNE_MAX_PENDING_TRIALS_PG` environment variable to the desired maximum number of concurrent pending trials.
         2025-08-20 08:30:08,953 WARNING tune_controller.py:2132 -- The maximum number of pending trials has been automatically set to the number of available cluster CPUs, which is high (519 CPUs/pending trials). If you're running an experiment with a large number of trials, this could lead to scheduling overhead. In this case, consider setting the `TUNE_MAX_PENDING_TRIALS_PG` environment variable to the desired maximum number of concurrent pending trials.
         
         View detailed results here: YOUR_GCS_BUCKET/gemma_vision_train_2025_08_20_08_30_07
         To visualize your results with TensorBoard, run: `tensorboard --logdir /tmp/ray/session_2025-08-20_04-43-14_215096_1/artifacts/2025-08-20_08-30-08/gemma_vision_train_2025_08_20_08_30_07/driver_artifacts`
         
         Training started with configuration:
         ╭──────────────────────────────────────────────────────────────────────╮
         │ Training config                                                      │
         ├──────────────────────────────────────────────────────────────────────┤
         │ train_loop_config/dataset_name                  ...-descriptions-vlm │
         │ train_loop_config/gcs_bucket                    ...-bucket-yooo-west │
         │ train_loop_config/gradient_accumulation_steps                      4 │
         │ train_loop_config/learning_rate                               0.0002 │
         │ train_loop_config/logging_steps                                   10 │
         │ train_loop_config/lora_alpha                                      16 │
         │ train_loop_config/lora_dropout                                  0.05 │
         │ train_loop_config/lora_r                                          16 │
         │ train_loop_config/max_seq_length                                 512 │
         │ train_loop_config/model_id                      google/gemma-3-4b-it │
         │ train_loop_config/num_train_epochs                                 3 │
         │ train_loop_config/output_dir                    ...-4b-seo-optimized │
         │ train_loop_config/per_device_train_batch_size                      1 │
         │ train_loop_config/push_to_hub                                  False │
         │ train_loop_config/save_steps                                     100 │
         │ train_loop_config/save_strategy                                epoch │
         ╰──────────────────────────────────────────────────────────────────────╯
         (RayTrainWorker pid=45455, ip=10.76.0.71) Setting up process group for: env:// [rank=0, world_size=16]
         (TorchTrainer pid=45197, ip=10.76.0.71) Started distributed worker processes:
         (TorchTrainer pid=45197, ip=10.76.0.71) - (node_id=4c934ab2f646a578b03cc335586f30b943e811b645526a74c50bfca1, ip=10.76.0.71, pid=45455) world_rank=0, local_rank=0, node_rank=0
         (TorchTrainer pid=45197, ip=10.76.0.71) - (node_id=4c934ab2f646a578b03cc335586f30b943e811b645526a74c50bfca1, ip=10.76.0.71, pid=45450) world_rank=1, local_rank=1, node_rank=0
         (TorchTrainer pid=45197, ip=10.76.0.71) - (node_id=4c934ab2f646a578b03cc335586f30b943e811b645526a74c50bfca1, ip=10.76.0.71, pid=45454) world_rank=2, local_rank=2, node_rank=0
         (TorchTrainer pid=45197, ip=10.76.0.71) - (node_id=4c934ab2f646a578b03cc335586f30b943e811b645526a74c50bfca1, ip=10.76.0.71, pid=45448) world_rank=3, local_rank=3, node_rank=0
         (TorchTrainer pid=45197, ip=10.76.0.71) - (node_id=4c934ab2f646a578b03cc335586f30b943e811b645526a74c50bfca1, ip=10.76.0.71, pid=45453) world_rank=4, local_rank=4, node_rank=0
         (TorchTrainer pid=45197, ip=10.76.0.71) - (node_id=4c934ab2f646a578b03cc335586f30b943e811b645526a74c50bfca1, ip=10.76.0.71, pid=45452) world_rank=5, local_rank=5, node_rank=0
         (TorchTrainer pid=45197, ip=10.76.0.71) - (node_id=4c934ab2f646a578b03cc335586f30b943e811b645526a74c50bfca1, ip=10.76.0.71, pid=45451) world_rank=6, local_rank=6, node_rank=0
         (TorchTrainer pid=45197, ip=10.76.0.71) - (node_id=4c934ab2f646a578b03cc335586f30b943e811b645526a74c50bfca1, ip=10.76.0.71, pid=45449) world_rank=7, local_rank=7, node_rank=0
         (TorchTrainer pid=45197, ip=10.76.0.71) - (node_id=c0db52b44f891f3d6a1cedcbea4c6beb2c8434c66ef414dc15e65743, ip=10.76.0.135, pid=45729) world_rank=8, local_rank=0, node_rank=1
         (TorchTrainer pid=45197, ip=10.76.0.71) - (node_id=c0db52b44f891f3d6a1cedcbea4c6beb2c8434c66ef414dc15e65743, ip=10.76.0.135, pid=45726) world_rank=9, local_rank=1, node_rank=1
         (TorchTrainer pid=45197, ip=10.76.0.71) - (node_id=c0db52b44f891f3d6a1cedcbea4c6beb2c8434c66ef414dc15e65743, ip=10.76.0.135, pid=45728) world_rank=10, local_rank=2, node_rank=1
         (TorchTrainer pid=45197, ip=10.76.0.71) - (node_id=c0db52b44f891f3d6a1cedcbea4c6beb2c8434c66ef414dc15e65743, ip=10.76.0.135, pid=45727) world_rank=11, local_rank=3, node_rank=1
         (TorchTrainer pid=45197, ip=10.76.0.71) - (node_id=c0db52b44f891f3d6a1cedcbea4c6beb2c8434c66ef414dc15e65743, ip=10.76.0.135, pid=45725) world_rank=12, local_rank=4, node_rank=1
         (TorchTrainer pid=45197, ip=10.76.0.71) - (node_id=c0db52b44f891f3d6a1cedcbea4c6beb2c8434c66ef414dc15e65743, ip=10.76.0.135, pid=45724) world_rank=13, local_rank=5, node_rank=1
         (TorchTrainer pid=45197, ip=10.76.0.71) - (node_id=c0db52b44f891f3d6a1cedcbea4c6beb2c8434c66ef414dc15e65743, ip=10.76.0.135, pid=45723) world_rank=14, local_rank=6, node_rank=1
         (TorchTrainer pid=45197, ip=10.76.0.71) - (node_id=c0db52b44f891f3d6a1cedcbea4c6beb2c8434c66ef414dc15e65743, ip=10.76.0.135, pid=45722) world_rank=15, local_rank=7, node_rank=1
         
         ...
         
         Training finished iteration 3 at 2025-08-20 08:40:43. Total running time: 10min 34s
         ╭─────────────────────────────────────────╮
         │ Training result                         │
         ├─────────────────────────────────────────┤
         │ checkpoint_dir_name   checkpoint_000002 │
         │ time_this_iter_s               152.6374 │
         │ time_total_s                  525.88585 │
         │ training_iteration                    3 │
         │ epoch                           2.75294 │
         │ grad_norm                      47.27161 │
         │ learning_rate                    0.0002 │
         │ loss                            22.5275 │
         │ mean_token_accuracy             0.90325 │
         │ num_tokens                     1583017. │
         │ step                                 60 │
         ╰─────────────────────────────────────────╯
         
         ...
         
         Training completed after 3 iterations at 2025-08-20 08:40:52. Total running time: 10min 43s
         2025-08-20 08:40:53,113 INFO tune.py:1009 -- Wrote the latest version of all result files and experiment state to 'YOUR_GCS_BUCKET/gemma_vision_train_2025_08_20_08_30_07' in 0.1663s.
         
         2025-08-20 08:40:58,304 SUCC cli.py:65 -- ----------------------------------
         2025-08-20 08:40:58,305 SUCC cli.py:66 -- Job 'test-ray-job-82mm7' succeeded
         2025-08-20 08:40:58,305 SUCC cli.py:67 -- ----------------------------------
         

## Monitor your workload




You can use the dashboard in Ray to monitor the workloads that are scheduled in your cluster.

To access this dashboard, you need to set up port-forwarding to your cluster by running the following command in a new terminal window:
    
    
    kubectl port-forward service/gemma3-tuning-head-svc 8265:8265 > fwd.log 2>&1 &

  1. Open the following link in your browser: `http://localhost:8265`.

  2. Optionally, if you're using Cloud Shell, after you run the command in the previous step, you can click the **Web Preview** button.

Select the **Change port** option, enter `8265`, and then click **Change and Preview**. The Ray Dashboard opens in a new tab.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete your resources

  1. To delete the Ray Cluster and release the GPU-powered node, run the following:
         
         kubectl delete -f ray_cluster.yaml

GKE automatically scales down your cluster and releases the A4 machines used by Ray.
  2. To delete the entire GKE cluster, run the following:
         
         gcloud container clusters delete $CLUSTER_NAME \
             --region=$REGION

  3. To delete the entire Cloud Storage bucket with all its contents, run the following:
         
         gcloud storage rm -r gs://$GCS_BUCKET




### Delete your project

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

## What's next

  * [Redeploy a Slurm cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-slurm-cluster#redeploy-slurm-cluster)

  * [Test network performance on a Slurm cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-slurm-cluster#test-rdma)

  * [Monitor VMs in a Slurm cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
