---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-gemma4-31b-sft-maxtext/
title: Run SFT for Gemma 4 31B on multi-host TPU v6e \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:20.337100+00:00
---

# Run SFT for Gemma 4 31B on multi-host TPU v6e  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-gemma4-31b-sft-maxtext/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Run SFT for Gemma 4 31B on multi-host TPU v6e Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to run supervised fine-tuning (SFT) on a multi-host Tensor Processing Unit (TPU) v6e cluster by using MaxText and Cluster Toolkit. You use Cluster Toolkit to execute a multi-host training workload and export the results back to Hugging Face format for serving.

## Workload summary

Running this SFT workload on Cloud TPU and GKE involves the following components:

  * **Model:** Gemma 4 31B (`google/gemma-4-31b-it`), an advanced open-weights model. In this tutorial, the model weights are downloaded from Hugging Face, converted into MaxText-compatible format, and deployed on a GKE cluster with Cloud TPU v6e (`v6e-32`) infrastructure.
  * **Training method:** SFT using MaxText. The workload executes a scalable fine-tuning pipeline on Cloud TPU v6e using JAX. It optimizes model parameters over 1000 steps using MaxText's built-in SFT trainer (`maxtext.trainers.post_train.sft.train_sft`) and instruction-tuning datasets.
  * **Dataset and template:** UltraChat 200k (`HuggingFaceH4/ultrachat_200k`), a large-scale, high-quality multi-turn dialogue dataset. The workload uses this dataset to fine-tune the model and improve its conversational and instruction-following capabilities.
  * **Infrastructure and framework:** GKE, managed using Cluster Toolkit, on Cloud TPU v6e (`v6e-32`, with a `4x8` topology). The framework is MaxText (`tpu_post_training:0.2.4`) with a JAX backend.



## Objectives

  * Install Cluster Toolkit and its dependencies.
  * Deploy a Cluster Toolkit cluster.
  * Convert a Hugging Face model to MaxText format.
  * Run an SFT training workload on the TPU.
  * Convert the fine-tuned model back to Hugging Face format for serving.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/pricing)
  * [ Cloud TPU](https://cloud.google.com/tpu/pricing)
  * [ Cloud Storage](https://cloud.google.com/storage/pricing)
  * [ Compute Engine](https://cloud.google.com/compute/all-pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

**Important:** To complete this tutorial, you must have access to `v6e-32` TPUs. This tutorial assumes that you already have a reservation for these TPUs in your Google Cloud project to ensure that you have the capacity available when you need it. To learn more about your options for reserving Cloud TPU capacity for a future date and time, see [About Cloud TPU reservations](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations).

## Before you begin

Authenticate your user account:
    
    
    gcloud auth login
    

Generate Application Default Credentials (ADC):
    
    
    gcloud auth application-default login
    

If you're running in a headless or remote SSH session without a browser, append `--no-launch-browser` to both commands.

**Note:** Skipping ADC authentication might result in metadata server errors during cluster provisioning.

  * You need a Hugging Face access token to use this tutorial. You can sign up for a free account at [Hugging Face](http://huggingface.co/login). After you have an account, generate an access token:

    1. On the [Welcome to Hugging Face](https://huggingface.co/welcome) page, click your account avatar and select **Access tokens**.
    2. On the **Access tokens** page, click **Create new token**.
    3. Select the **Read** token type and enter a name for your token.
    4. Your access token is displayed. Save the token in a safe place.



  * On the [`google/gemma-4-31b-it` model card on Hugging Face](https://huggingface.co/google/gemma-4-31b-it), accept the license agreement for the model.



To get the permissions that you need to complete this tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * To complete this tutorial: 
    * [TPU Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#tpu.admin) (`roles/tpu.admin`)
    * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
    * [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)
    * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
    * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
    * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
    * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
    * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up your environment variables

Set up your environment variables:
    
    
    export PROJECT="YOUR_PROJECT_ID"
    export REGION="YOUR_REGION"
    export ZONE="YOUR_ZONE"
    export CLUSTER_NAME="YOUR_CLUSTER_NAME"
    export GCS_BUCKET="YOUR_BUCKET_NAME"
    export CLOUD_IMAGE_NAME="us-docker.pkg.dev/cloud-tpu-images/maxtext-images/tpu_post_training:0.2.4"
    export TPU_TYPE="v6e-32"
    export RESERVATION="YOUR_RESERVATION_NAME"
    export HF_TOKEN="YOUR_HF_TOKEN"
    export MODEL_NAME="gemma4-31b"
    export CLUSTER_TOOLKIT_VERSION="v1.103.0"
    
    gcloud config set project "${PROJECT:?}"
    gcloud auth application-default set-quota-project "${PROJECT:?}" || true

Replace the following:

  * `YOUR_PROJECT_ID`: the ID of your Google Cloud project.
  * `YOUR_REGION`: the region where your TPU reservation is located and where you deploy your cluster.
  * `YOUR_ZONE`: the zone where your TPU reservation is located and where you deploy your cluster.
  * `YOUR_BUCKET_NAME`: a globally unique name for a Cloud Storage bucket.
  * `YOUR_RESERVATION_NAME`: the name of your TPU v6e reservation.
  * `YOUR_HF_TOKEN`: your Hugging Face access token.



By default, the script sets `MODEL_NAME` to `gemma4-31b` (the MaxText model name for `google/gemma-4-31b-it`) and `CLUSTER_NAME` to `gke-tpu-v6e`. If you customize `CLUSTER_NAME`, the name must start with a lowercase letter, contain only lowercase letters, numbers, and hyphens, and be 20 characters or fewer so that generated service account IDs stay within the 30-character limit.

## Install Cluster Toolkit dependencies

To complete this tutorial from a Linux or macOS client or workstation, follow the relevant steps in [Install dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies) in the Cluster Toolkit documentation.

If you're using Cloud Shell, then you can skip this section.

## Install Cluster Toolkit

Download and extract the prebuilt bundle for the specific version of Cluster Toolkit defined in `CLUSTER_TOOLKIT_VERSION` (`v1.103.0`) into your current working directory:
    
    
    case "$(uname -s)-$(uname -m)" in
      Linux-x86_64)              BUNDLE="gcluster_bundle_linux_amd64.tgz" ;;
      Linux-aarch64|Linux-arm64) BUNDLE="gcluster_bundle_linux_arm64.tgz" ;;
      Darwin-x86_64)             BUNDLE="gcluster_bundle_mac_amd64.tgz" ;;
      Darwin-arm64)              BUNDLE="gcluster_bundle_mac_arm64.tgz" ;;
      *) BUNDLE=""; echo "Unsupported platform: $(uname -s)-$(uname -m)" >&2 ;;
    esac
    mkdir -p cluster-toolkit
    curl -fsSL "https://github.com/GoogleCloudPlatform/cluster-toolkit/releases/download/${CLUSTER_TOOLKIT_VERSION:?}/${BUNDLE:?}" \
      | tar -xz -C cluster-toolkit
    cd cluster-toolkit

**Note:** The [Install Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment#install-bundle) documentation describes how to download the latest release into a `cluster-toolkit` directory. However, because blueprint variables can differ across Cluster Toolkit versions, for this tutorial you must install the exact version specified in `CLUSTER_TOOLKIT_VERSION` (`v1.103.0`) rather than the latest release. Extracting the bundle provides the `gcluster` binary and the `examples/` blueprints that you use in the steps that follow. If you extracted the bundle into a `cluster-toolkit` directory, make sure that you change to that directory (`cd cluster-toolkit`) before running the subsequent commands.

## Create your Cluster Toolkit cluster

To create and deploy a Cluster Toolkit cluster with 32 `v6e` TPU chips, complete the following steps:

  1. Create a Cloud Storage bucket:
         
         gcloud storage buckets create "gs://${GCS_BUCKET:?}" --project="${PROJECT:?}" --location="${REGION:?}" || true

  2. Stage the blueprint configuration and copy the example deployment blueprint to an isolated working directory:
         
         mkdir -p tmp
         cp examples/gke-tpu-v6e/gke-tpu-v6e-advanced.yaml tmp/

  3. Update `tmp/gke-tpu-v6e-advanced.yaml` to grant your cluster node pool service account (`gke-np-sa`) the Storage Admin role (`roles/storage.admin`) for writing checkpoints to your Cloud Storage bucket, switch the system node pool machine type to `e2-standard-8`, and pin the system node pool to your target zone to avoid regional machine-type stockouts:
         
         # Grant the GKE Node Pool Service Account storage.admin access for checkpoint writes
         sed -i "s/- storage.objectViewer/- storage.admin/" tmp/gke-tpu-v6e-advanced.yaml
         # Change n2-standard-8 to e2-standard-8 to avoid GCE_STOCKOUT in some regions
         sed -i "s/n2-standard-8/e2-standard-8/" tmp/gke-tpu-v6e-advanced.yaml
         # Pin system node pool to a single zone to avoid cross-zone stockouts
         sed -i '/system_node_pool_machine_type/a \      system_node_pool_zones: [$(vars.zone)]' tmp/gke-tpu-v6e-advanced.yaml

  4. Use the [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) to deploy your Cluster Toolkit cluster by using the blueprint `tmp/gke-tpu-v6e-advanced.yaml` and passing the required variables by using the `--vars` flag:
         
         ./gcluster deploy tmp/gke-tpu-v6e-advanced.yaml \
             --vars "project_id=${PROJECT:?},deployment_name=${CLUSTER_NAME:?},region=${REGION:?},zone=${ZONE:?},num_slices=1,tpu_topology=4x8,authorized_cidr=0.0.0.0/0,reservation=${RESERVATION:-}" \
             --download-dependencies \
             -l IGNORE \
             --auto-approve -w

  5. Configure container registry authentication:
         
         gcloud auth configure-docker gcr.io --quiet
         gcloud auth configure-docker "${REGION:?}-docker.pkg.dev" --quiet




## Convert the model to MaxText format

To train the model in MaxText format, you must convert it from Hugging Face format to MaxText format.

  1. To simplify subsequent commands, use the [`gcluster job config` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-config) to configure your default project, cluster, and location:
         
         # Configure gcluster Defaults
         ./gcluster job config set project "${PROJECT:?}"
         ./gcluster job config set cluster "${CLUSTER_NAME:?}"
         ./gcluster job config set location "${REGION:?}"

  2. Use the [`gcluster job submit` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-submit) to convert the model from Hugging Face format to MaxText format and store it in your Cloud Storage bucket:
         
         ./gcluster job submit --name hf-to-mt \
             --compute-type "${TPU_TYPE:?}" \
             --num-slices 1 \
             --image "${CLOUD_IMAGE_NAME:?}" \
             --await-job-completion \
             --command "[ \"\$JOB_COMPLETION_INDEX\" != \"0\" ] || \
               python3 -m maxtext.checkpoint_conversion.to_maxtext \
                 model_name=${MODEL_NAME:?} \
                 hf_access_token=${HF_TOKEN:?} \
                 base_output_directory=gs://${GCS_BUCKET:?}/${MODEL_NAME}/max-text-format/ \
                 scan_layers=True \
                 use_multimodal=False \
                 skip_jax_distributed_system=true \
                 checkpoint_storage_use_zarr3=0 \
                 checkpoint_storage_use_ocdbt=0 \
                 hardware=cpu \
                 --lazy_load_tensors=True"

The command includes the `--await-job-completion` flag, which means that it waits in your current terminal until the conversion finishes.

  3. Optional: To stream the conversion logs while the job is running, open a separate terminal in the working directory where you extracted `gcluster`, and run the [`gcluster job logs` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-logs):
         
         # Use the list command to check status
         ./gcluster job list
         
         # Check progress of the job (--main-only targets the coordinator pod (Job Index 0, Pod Index 0) to avoid duplicate logs from other workers)
         ./gcluster job logs hf-to-mt --main-only -f

  4. In your original terminal, verify that the converted model files are available in your Cloud Storage bucket:
         
         gcloud storage ls "gs://${GCS_BUCKET:?}/${MODEL_NAME:?}/max-text-format/"




## Start the training workload

  1. After the conversion process has completed, start the SFT workload:
         
         ./gcluster job submit --name sft \
             --compute-type "${TPU_TYPE:?}" \
             --num-slices 1 \
             --image "${CLOUD_IMAGE_NAME:?}" \
             --await-job-completion \
             --command "JAX_PLATFORMS=tpu,cpu ENABLE_PJRT_COMPATIBILITY=true JAX_TRACEBACK_FILTERING=off LIBTPU_INIT_ARGS=' --xla_tpu_scoped_vmem_limit_kib=61440 --xla_tpu_bf16_emission_mode=NATIVE_EMISSION --xla_tpu_enable_sparse_core_collective_offload_all_reduce=true --xla_tpu_use_single_sparse_core_for_all_gather_offload=true ' \
               python3 -m maxtext.trainers.post_train.sft.train_sft \
               run_name=sft \
               base_output_directory=gs://${GCS_BUCKET:?}/${MODEL_NAME:?}/trained/ \
               model_name=${MODEL_NAME} \
               load_parameters_path=gs://${GCS_BUCKET}/${MODEL_NAME}/max-text-format/0/items/ \
               hf_access_token=${HF_TOKEN:?} \
               dataset_type=hf \
               hf_path=HuggingFaceH4/ultrachat_200k \
               per_device_batch_size=1 steps=1000 \
               profiler=xplane \
               checkpoint_storage_use_zarr3=0 \
               checkpoint_storage_use_ocdbt=0 \
               skip_jax_distributed_system=False"

The command includes the `--await-job-completion` flag, which means that it waits in your current terminal until the training job finishes.

  2. Optional: To stream the live training logs while the job is running, open a separate terminal in the working directory where you extracted `gcluster`, and run the `gcluster job logs` command:
         
         # Use the list command to check status
         ./gcluster job list
         
         # Check progress of the job (--main-only targets the coordinator pod (Job Index 0, Pod Index 0) to avoid duplicate logs from other workers)
         ./gcluster job logs sft --main-only -f

After initial XLA compilation completes, the coordinator logs output progress for each step across the 1000-step run in the format `completed step: <step>, seconds: ..., TFLOP/s/device: ..., loss: ...`, with the training loss decreasing from approximately `1.57` at step 5 to approximately `0.82` at step 1000. Before you proceed to the next section, wait until step 1000 finishes and the output from the `./gcluster job list` command shows the status of `sft` as `Succeeded`.

**Note:** Completed JobSets on GKE are automatically cleaned up after their configured time to live (TTL) expires, which is one hour by default (`--gke-ttl-after-finished=1h`). Completed workloads are not listed in the output of the `./gcluster job list` command after their TTL expires; however, all checkpoints and model weights are stored in your Cloud Storage bucket.
  3. In your original terminal, verify that the SFT training checkpoints are generated in your Cloud Storage bucket:
         
         gcloud storage ls "gs://${GCS_BUCKET:?}/${MODEL_NAME:?}/trained/sft/checkpoints/1000/model_params/"




## Convert the trained model back into Hugging Face format

  1. After the training workload has completed, convert the model back to Hugging Face format:
         
         ./gcluster job submit --name mt-to-hf \
             --compute-type "${TPU_TYPE:?}" \
             --num-slices 1 \
             --image "${CLOUD_IMAGE_NAME:?}" \
             --await-job-completion \
             --command "[ \"\$JOB_COMPLETION_INDEX\" != \"0\" ] || \
               python3 -m maxtext.checkpoint_conversion.to_huggingface \
                 model_name=${MODEL_NAME:?} \
                 hf_access_token=${HF_TOKEN:?} \
                 load_parameters_path=gs://${GCS_BUCKET:?}/${MODEL_NAME}/trained/sft/checkpoints/1000/model_params/ \
                 base_output_directory=gs://${GCS_BUCKET}/${MODEL_NAME}/hf-trained/ \
                 skip_jax_distributed_system=true \
                 hardware=cpu \
                 scan_layers=True \
                 use_multimodal=False \
                 weight_dtype=bfloat16 \
                 --override_model_architecture"

The command includes the `--await-job-completion` flag, which means that it waits in your current terminal until the conversion finishes.

  2. Optional: To stream the live conversion logs while the job is running, open a separate terminal in the working directory where you extracted `gcluster`, and run the `gcluster job logs` command:
         
         # Use the list command to check status
         ./gcluster job list
         
         # Check progress of the job (--main-only targets the coordinator pod (Job Index 0, Pod Index 0) to avoid duplicate logs from other workers)
         ./gcluster job logs mt-to-hf --main-only -f
         
         # The trained model is now available in gs://${GCS_BUCKET}/${MODEL_NAME}/hf-trained/ 

  3. In your original terminal, verify that the final Hugging Face Safetensors weights are generated in your Cloud Storage bucket:
         
         gcloud storage ls -l --readable-sizes "gs://${GCS_BUCKET:?}/${MODEL_NAME:?}/hf-trained/"




## Clean up

To avoid incurring additional charges, use the [`gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy) to delete the resources created during this tutorial:
    
    
    ./gcluster destroy "${CLUSTER_NAME:?}" --robust --auto-approve
    gcloud storage rm -r "gs://${GCS_BUCKET:?}"
    
    # To delete the local deployment folder and staged blueprint
    rm -rf .ghpc "${CLUSTER_NAME:?}" tmp

## What's next

  * For more information about Cloud TPU, see [Introduction to Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu).
  * For architecture and configuration details for the `v6e-32` TPU, see [TPU v6e](https://docs.cloud.google.com/tpu/docs/v6e).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
