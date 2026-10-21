---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-qwen3-30b-a3b-rl-maxtext/
title: Run multi-host RL training for Qwen3-30b-a3b on TPU v6e \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:15:18.895241+00:00
---

# Run multi-host RL training for Qwen3-30b-a3b on TPU v6e  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-qwen3-30b-a3b-rl-maxtext/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Run multi-host RL training for Qwen3-30b-a3b on TPU v6e Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to run multi-host reinforcement learning (RL) training on a Tensor Processing Unit (TPU) `v6e-32` cluster by using MaxText and Cluster Toolkit. You use [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview) to execute a multi-host training workload and export the results back to Hugging Face format for serving.

## Workload summary

Running this RL post-training workload on Cloud TPU and GKE involves the following components:

  * **Model:** Qwen3 30B A3B Instruct (`Qwen/Qwen3-30B-A3B-Instruct-2507`), an advanced open-weights instruction-tuned model. In this tutorial, the model weights are downloaded from Hugging Face, converted into MaxText-compatible format, and deployed on a GKE cluster with Cloud TPU v6e infrastructure.
  * **Reinforcement Learning (RL) algorithm:** Group Relative Policy Optimization (GRPO) using MaxText and Pathways. The workload executes a scalable post-training pipeline using MaxText's built-in RL trainer (`maxtext.trainers.post_train.rl.train_rl`) paired with a vLLM sampler backend. GRPO optimizes the policy by generating a group of outputs per prompt and evaluating relative rewards without needing a separate critic model.
  * **Dataset and template:** OpenMathInstruct-2 (`openmathinstruct2_rl.json`), a large-scale math instruction-tuning dataset. The workload uses structured chat templates during the RL rollout phase to enhance multi-step mathematical reasoning capabilities.
  * **Infrastructure and framework:** GKE, managed using Cluster Toolkit, on Cloud TPU v6e (`ct6e-standard-4t`, with a `4x8` topology). The training framework is MaxText (`tpu_post_training:0.2.4`) with Pathways and JAX backend.



## Objectives

  * Install Cluster Toolkit and its dependencies.
  * Deploy a Cluster Toolkit cluster.
  * Convert a Hugging Face model to MaxText format.
  * Run an RL training workload on the TPU v6e cluster.
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

  * You need a Hugging Face access token to use this tutorial. You can sign up for a free account at [Hugging Face](http://huggingface.co/login). After you have an account, generate an access token:

    1. On the [Welcome to Hugging Face](https://huggingface.co/welcome) page, click your account avatar and select **Access tokens**.
    2. On the **Access tokens** page, click **Create new token**.
    3. Select the **Read** token type and enter a name for your token.
    4. Your access token is displayed. Save the token in a safe place.



  * On the [Hugging Face website](https://huggingface.co/), accept the license agreement for the model that you plan to train. This tutorial uses the model `qwen3-30b-a3b`.



To get the permissions that you need to complete this tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * [TPU Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#tpu.admin) (`roles/tpu.admin`)
  * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
  * [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
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
    export COMPUTE_TYPE="ct6e-standard-4t"
    export TOPOLOGY="4x8"
    export CLUSTER_NODEPOOL_COUNT=1
    export RESERVATION="YOUR_RESERVATION_NAME"
    export MODEL_NAME="qwen3-30b-a3b"
    export CLUSTER_TOOLKIT_VERSION="v1.103.0"
    export HF_TOKEN="YOUR_HF_TOKEN"

Replace the following:

  * YOUR_PROJECT_ID: the ID of your Google Cloud project.
  * YOUR_REGION: the region where you want to deploy your cluster.
  * YOUR_ZONE: the zone where you want to deploy your cluster.
  * YOUR_CLUSTER_NAME: the name of your Google Kubernetes Engine cluster (up to 20 characters).
  * YOUR_BUCKET_NAME: a globally unique name for a Cloud Storage bucket.
  * YOUR_RESERVATION_NAME: the name of your reservation.
  * YOUR_HF_TOKEN: your Hugging Face access token.



## Install Cluster Toolkit dependencies

To complete this tutorial from a Linux or macOS client or workstation, follow the relevant steps in [Install dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies) in the Cluster Toolkit documentation.

If you're using Cloud Shell, then you can skip this section.

## Install Cluster Toolkit

Install the prebuilt bundle for Cluster Toolkit in your current working directory by following the instructions at [Install Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment#install-bundle).

For example, you can download and extract the bundle into your current working directory as follows:
    
    
    wget -qO- "https://github.com/GoogleCloudPlatform/cluster-toolkit/releases/download/${CLUSTER_TOOLKIT_VERSION:?}/gcluster_bundle_linux_amd64.tgz" | tar -xz

Extracting the bundle into your current working directory provides the `gcluster` binary and the `examples/` blueprints that you use in the steps that follow.

## Create your Cluster Toolkit cluster

To create and deploy a Cluster Toolkit cluster with 32 `v6e` TPU chips, complete the following steps:

  1. Create a Cloud Storage bucket:
         
         gcloud storage buckets create "gs://${GCS_BUCKET:?}" --project="${PROJECT:?}" --location="${REGION:?}" || true

  2. Copy the Cluster Toolkit blueprint to your current working directory:
         
         cp examples/gke-tpu-v6e/gke-tpu-v6e-advanced.yaml .

  3. By default, your cluster node pool service account doesn't have the required permissions to write to your Cloud Storage bucket. To allow the node pool service account to write to your Cloud Storage bucket, you must grant it the `Storage Admin` role. To grant this role, edit the file `gke-tpu-v6e-advanced.yaml` by updating the [`service-account` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/service-account) named `node_pool_service_account`:
         
         - id: node_pool_service_account
           source: modules/project/service-account
           settings:
             name: gke-np-sa
             project_roles:
             - logging.logWriter
             - monitoring.metricWriter
             - monitoring.viewer
             - stackdriver.resourceMetadata.writer
             - storage.admin
             - artifactregistry.reader

  4. Use the [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) to deploy your Cluster Toolkit cluster by using the blueprint `gke-tpu-v6e-advanced.yaml` and passing the required variables by using the `--vars` flag:
         
         ./gcluster deploy gke-tpu-v6e-advanced.yaml \
             --vars project_id="${PROJECT:?}" \
             --vars deployment_name="${CLUSTER_NAME:?}" \
             --vars region="${REGION:?}" \
             --vars zone="${ZONE:?}" \
             --vars num_slices="${CLUSTER_NODEPOOL_COUNT:?}" \
             --vars tpu_topology="${TOPOLOGY:?}" \
             --vars authorized_cidr="0.0.0.0/0" \
             --vars reservation="${RESERVATION:-}" \
             -l IGNORE --auto-approve -w

  5. Configure Container Registry authentication and grant the Storage Admin role (`roles/storage.admin`) to your GKE service accounts:
         
         gcloud auth configure-docker gcr.io --quiet
         gcloud auth configure-docker "${REGION:?}-docker.pkg.dev" --quiet
         gcloud projects add-iam-policy-binding "${PROJECT:?}" --member="serviceAccount:${CLUSTER_NAME:?}-gke-wl-sa@${PROJECT}.iam.gserviceaccount.com" --role="roles/storage.admin" --quiet
         gcloud projects add-iam-policy-binding "${PROJECT:?}" --member="serviceAccount:${CLUSTER_NAME:?}-gke-np-sa@${PROJECT}.iam.gserviceaccount.com" --role="roles/storage.admin" --quiet




## Convert the model to MaxText format

To train the model in MaxText format, you must convert it from Hugging Face format to MaxText format.

  1. To simplify subsequent commands, use the [`gcluster job config` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-config) to configure your default project, cluster, and location:
         
         # Configure gcluster Defaults
         ./gcluster job config set project "${PROJECT:?}"
         ./gcluster job config set cluster "${CLUSTER_NAME:?}"
         ./gcluster job config set location "${REGION:?}"

  2. Use the [`gcluster job submit` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-submit) to convert the model from Hugging Face format to MaxText format and store it in your Cloud Storage bucket:
         
         ./gcluster job submit \
           --name qwen-hf-to-mt \
           --num-slices 1 \
           --image "${CLOUD_IMAGE_NAME:?}" \
           --compute-type "${COMPUTE_TYPE:?}" \
           --topology "${TOPOLOGY:?}" \
           --await-job-completion \
           --command "[ \"\$JOB_COMPLETION_INDEX\" != \"0\" ] || \
           python3 -m maxtext.checkpoint_conversion.to_maxtext \
           model_name=${MODEL_NAME:?} \
           hf_access_token=${HF_TOKEN:?} \
           --hf_model_path='Qwen/Qwen3-30B-A3B-Instruct-2507' \
           base_output_directory=gs://${GCS_BUCKET:?}/${MODEL_NAME}/max-text-format/ \
           scan_layers=True \
           use_multimodal=False \
           skip_jax_distributed_system=true \
           checkpoint_storage_use_zarr3=0 \
           checkpoint_storage_use_ocdbt=0 \
           hardware=cpu \
           --lazy_load_tensors=True"

  3. Use the [`gcluster job logs` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-logs) to check the status of the conversion job:
         
         # Use the list command to check status
         ./gcluster job list
         
         # Check progress of the job (--main-only targets the coordinator pod (Job Index 0, Pod Index 0) to avoid duplicate logs from other workers)
         ./gcluster job logs qwen-hf-to-mt --main-only -f

  4. Verify that the converted model files are available in your Cloud Storage bucket:
         
         gcloud storage ls "gs://${GCS_BUCKET:?}/${MODEL_NAME:?}/max-text-format/"




## Start the training workload

After the conversion process has completed, start the RL training workload:
    
    
    ./gcluster job submit \
      --name="qwen-rl" \
      --num-slices=1 \
      --image="${CLOUD_IMAGE_NAME:?}" \
      --compute-type="${COMPUTE_TYPE:?}" \
      --topology="${TOPOLOGY:?}" \
      --pathways \
      --pathways-gcs-location="gs://${GCS_BUCKET:?}/pathways/" \
      --gke-ttl-after-finished="24h" \
      --restarts=0 \
      --env="GRPC_DNS_RESOLVER=native" \
      --env="FLAGS_pathways_enforce_subset_devices_form_subslice=false" \
      --pathways-proxy-env="GRPC_DNS_RESOLVER=native" \
      --pathways-proxy-env="FLAGS_pathways_enforce_subset_devices_form_subslice=false" \
      --pathways-server-env="GRPC_DNS_RESOLVER=native" \
      --pathways-server-env="FLAGS_pathways_enforce_subset_devices_form_subslice=false" \
      --pathways-worker-env="GRPC_DNS_RESOLVER=native" \
      --pathways-worker-env="FLAGS_pathways_enforce_subset_devices_form_subslice=false" \
      --command="(echo 190G > /sys/fs/cgroup/memory.max || echo 190G > /sys/fs/cgroup/memory/memory.limit_in_bytes) 2>/dev/null || true && \
        export VLLM_HOST_IP=\$(hostname -I | awk '{print \$1}') && \
        export VLLM_ENABLE_V1_MULTIPROCESSING=0 && \
        python3 -c \"import pathlib, tunix.generate.vllm_sampler as vs; p = pathlib.Path(vs.__file__); p.write_text(p.read_text().replace('reshard_chunk_size: Optional[int] = None', 'reshard_chunk_size: Optional[int] = 4').replace('reshard_chunk_size=self.config.reshard_chunk_size', 'reshard_chunk_size=4'))\" && \
        python3 -c \"import pathlib, re; p = pathlib.Path('/deps/src/maxtext/trainers/post_train/rl/utils_rl.py'); p.write_text(re.sub('optax[.]adamw[(][^)]+[)]', 'optax.adafactor(learning_rate=learning_rate)', p.read_text()))\" && \
        JAX_PLATFORMS=proxy,cpu ENABLE_PATHWAYS_PERSISTENCE=1 \
        python3 -m maxtext.trainers.post_train.rl.train_rl \
        run_name=rl \
        base_output_directory=gs://${GCS_BUCKET}/${MODEL_NAME:?}/trained/ \
        model_name=${MODEL_NAME} \
        load_parameters_path=gs://${GCS_BUCKET}/${MODEL_NAME}/max-text-format/0/items/ \
        hf_access_token=${HF_TOKEN:?} \
        data_template_path=maxtext/examples/chat_templates/openmathinstruct2_rl.json \
        num_batches=50 \
        num_test_batches=0 \
        batch_size=8 \
        train_micro_batch_size=8 \
        max_target_length=512 \
        max_prefill_predict_length=256 \
        mu_dtype=bfloat16 \
        grad_dtype=bfloat16 \
        rollout_tensor_parallelism=1 \
        rollout_expert_parallelism=4 \
        trainer_devices_fraction=0.5 \
        sampler_devices_fraction=0.5 \
        tokenizer_path='Qwen/Qwen3-30B-A3B-Instruct-2507' \
        ici_tensor_parallelism=2 \
        ici_expert_parallelism=4 \
        ici_fsdp_parallelism=-1 \
        hbm_utilization_vllm=0.55 \
        remat_policy=full \
        async_scheduling=False \
        allow_split_physical_axes=true \
        ragged_gather_reduce_fallback=True \
        enable_dp_attention=False \
        decode_sampling_temperature=0.8 \
        decode_sampling_top_k=50 \
        decode_sampling_nucleus_p=0.95 \
        learning_rate=2e-5 \
        learning_rate_schedule_steps=100 \
        rl.num_generations=4 \
        rl.reshard_chunk_size=4 \
        debug=True \
        vllm_hf_overrides='{\"architectures\": [\"MaxTextForCausalLM\"]}' \
        vllm_additional_config=\"{'maxtext_config': {'model_name': '${MODEL_NAME}', 'model_call_mode': 'inference', 'enable_dp_attention': false, 'allow_split_physical_axes': true, 'use_ragged_sort': false, 'ragged_gather_reduce_fallback': true, 'prefuse_moe_weights': true, 'weight_dtype': 'bfloat16'}}\""

  * To check the status of the training job:
        
        # Use the list command to check status (initially shows "Suspended" briefly while the CPU node pool scales up)
        ./gcluster job list
        
        # Ensure kubectl credentials are configured
        gcloud container clusters get-credentials "${CLUSTER_NAME:?}" \
            --location="${REGION:?}" \
            --project="${PROJECT:?}"
        
        # Wait for the Pathways head pod to be ready before streaming logs
        kubectl wait --for=condition=Ready pod \
            -l jobset.sigs.k8s.io/replicatedjob-name=pathways-head \
            --timeout=600s
        
        # Stream training logs (runs for 50 steps; wait for "Post RL Training: ... mean_reward=..." and job status Succeeded before converting to Hugging Face)
        kubectl logs -f \
            -l jobset.sigs.k8s.io/replicatedjob-name=pathways-head \
            -c workload-container

**Note:** Completed JobSets on GKE are automatically cleaned up after one hour by default (governed by the `--gke-ttl-after-finished=1h` setting in `gcluster job submit`). If your workload is no longer listed in the output of `./gcluster job list`, this cleanup is expected behavior and does not mean the job failed. All checkpoints and model weights remain safely persisted in your Cloud Storage bucket.
  * To verify that the training checkpoints are generated in your Cloud Storage bucket:
        
        gcloud storage ls "gs://${GCS_BUCKET:?}/${MODEL_NAME:?}/trained/rl/checkpoints/actor/"




## Convert the trained model back into Hugging Face format

After the training workload has completed, convert the model back to Hugging Face format:
    
    
    ./gcluster job submit \
      --name="qwen-mt-to-hf" \
      --num-slices=1 \
      --image="${CLOUD_IMAGE_NAME:?}" \
      --compute-type="${COMPUTE_TYPE:?}" \
      --topology="${TOPOLOGY:?}" \
      --await-job-completion \
      --command="[ \"\$JOB_COMPLETION_INDEX\" != \"0\" ] || \
      python3 -m maxtext.checkpoint_conversion.to_huggingface \
      model_name=${MODEL_NAME:?} \
      hf_access_token=${HF_TOKEN:?} \
      load_parameters_path=gs://${GCS_BUCKET:?}/${MODEL_NAME}/trained/rl/checkpoints/actor/50/model_params/ \
      base_output_directory=gs://${GCS_BUCKET}/${MODEL_NAME}/hf-trained/ \
      skip_jax_distributed_system=true \
      hardware=cpu \
      scan_layers=True \
      use_multimodal=False \
      weight_dtype=bfloat16 \
      --override_model_architecture"

  * To check the status of the conversion job:
        
        # Use the list command to check status
        ./gcluster job list
        
        # Check progress of the job (--main-only targets the coordinator pod (Job Index 0, Pod Index 0) to avoid duplicate logs from other workers)
        ./gcluster job logs qwen-mt-to-hf --main-only -f
        # The trained model is now available in gs://${GCS_BUCKET}/${MODEL_NAME}/hf-trained/

  * To verify that the trained Hugging Face model weights and configuration files are present in your Cloud Storage bucket:
        
        gcloud storage ls -l --readable-sizes "gs://${GCS_BUCKET:?}/${MODEL_NAME:?}/hf-trained/"




## Clean up

To avoid incurring additional charges, use the [`gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy) to delete the resources created during this tutorial:
    
    
    ./gcluster destroy "${CLUSTER_NAME:?}"
    gcloud storage rm -r "gs://${GCS_BUCKET:?}"
    
    # To delete the local deployment folder and copied blueprint
    rm -rf .ghpc "${CLUSTER_NAME:?}" gke-tpu-v6e-advanced.yaml

## What's next

  * For more information about Cloud TPU, see [Introduction to Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu).
  * For architecture and configuration details for the `v6e-32` TPU, see [TPU v6e](https://docs.cloud.google.com/tpu/docs/v6e).
  * For more information about Cluster Toolkit, see [Cluster Toolkit overview](https://docs.cloud.google.com/cluster-toolkit/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
