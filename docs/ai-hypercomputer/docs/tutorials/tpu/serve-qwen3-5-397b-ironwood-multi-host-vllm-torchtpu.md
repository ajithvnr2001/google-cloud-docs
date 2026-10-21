---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-qwen3-5-397b-ironwood-multi-host-vllm-torchtpu/
title: Serve Qwen3.5-397B on GKE with multi-host vLLM TorchTPU on TPU7x accelerators \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:26:26.958605+00:00
---

# Serve Qwen3.5-397B on GKE with multi-host vLLM TorchTPU on TPU7x accelerators  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-qwen3-5-397b-ironwood-multi-host-vllm-torchtpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Serve Qwen3.5-397B on GKE with multi-host vLLM TorchTPU on TPU7x accelerators Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to deploy and serve [Qwen3.5-397B (`Qwen/Qwen3.5-397B-A17B-FP8`)](https://huggingface.co/Qwen/Qwen3.5-397B-A17B-FP8), a Mixture-of-Experts model, on Google Kubernetes Engine (GKE). The deployment uses multi-host [TPU7x (Ironwood)](https://docs.cloud.google.com/tpu/docs/tpu7x) accelerators and the [vLLM TPU serving framework](https://github.com/vllm-project/tpu-inference) with TorchTPU (`torchtpu`) and prefill-decode (PD) disaggregation.

In this configuration, you provision two multi-host `tpu7x-standard-4t` node pools, each arranged in a `2x2x2` topology (eight TPU7x chips across two nodes per node pool, for a total of 16 TPU7x chips). You use the Kubernetes JobSet API and Ray to run disaggregated multi-host prefill and decode servers on separate TPU7x slices with data parallelism and expert parallelism enabled, and route requests through a disaggregation proxy.

## Objectives

  * Set up your GKE cluster and multi-host TPU7x node pools.
  * Stage the model weights in a Cloud Storage bucket.
  * Deploy the multi-host vLLM TorchTPU prefill, decode, and proxy servers with JobSet.
  * Run a serving benchmark workload and analyze the results.
  * Clean up.



## Costs

In this document, you use the following billable components of Google Cloud:

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [Cloud TPU](https://docs.cloud.google.com/tpu/pricing)
  * [Cloud Storage](https://docs.cloud.google.com/storage/pricing)
  * [Compute Engine](https://docs.cloud.google.com/compute/all-pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  * You need a Hugging Face access token to use this tutorial. You can sign up for a free account at [Hugging Face](http://huggingface.co/login). After you have an account, generate an access token:

    1. On the [Welcome to Hugging Face](https://huggingface.co/welcome) page, click your account avatar and select **Access tokens**.
    2. On the **Access tokens** page, click **Create new token**.
    3. Select the **Read** token type and enter a name for your token.
    4. Your access token is displayed. Save the token in a safe place.



  * Enable the Kubernetes Engine API in your Google Cloud project:

[Enable Kubernetes Engine API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  * [Install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the Google Cloud CLI, and install [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl). If you use Cloud Shell, both tools are preinstalled.

  * Ensure that your project has sufficient [SSD quota and external IP address quota](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#additional-quotas) in the region where your TPU capacity is located:

    1. In the Google Cloud console, go to the **Quotas & System Limits** page.

[Go to Quotas & System Limits](https://console.cloud.google.com/iam-admin/quotas)

    2. Filter by **Persistent Disk SSD (GB)** and verify that you have sufficient available SSD quota in your target region.

    3. Filter by **In-use regional external IPv4 addresses** and verify that you have sufficient IP address quota in your target region.


**Important:** To complete this tutorial, you must have quota for TPU7x (Ironwood) TPUs in your Google Cloud project. TPU quota is [region- and zone-specific](https://docs.cloud.google.com/tpu/docs/regions-zones), so make sure that you create your resources in a region and zone where TPU7x capacity is available. This tutorial uses Spot capacity, but you can also use a reservation or Flex-start VMs if available. To learn more about reserving Cloud TPU capacity, see [About Cloud TPU reservations](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations).

To get the permissions that you need to complete this tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
  * [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up your environment variables

  1. Set up your authentication:
         
         gcloud auth login
         gcloud auth application-default login

  2. Export the environment variables that you use throughout this tutorial:
         
         export PROJECT_ID="YOUR_PROJECT_ID"
         export REGION="YOUR_REGION"
         export ZONE="YOUR_ZONE"
         export CLUSTER_NAME="YOUR_CLUSTER_NAME"
         export MACHINE_TYPE="tpu7x-standard-4t"
         export WORKLOAD_POLICY_NAME="${CLUSTER_NAME}-policy"
         export NODE_POOL_NAME_0="np-0"
         export NODE_POOL_NAME_1="np-1"
         export RESERVATION_NAME="YOUR_RESERVATION_NAME"
         export GCS_BUCKET="YOUR_GCS_BUCKET"
         export HF_TOKEN="YOUR_HF_TOKEN"
         export VLLM_IMAGE="vllm/vllm-torchtpu:v0.29.0@sha256:3976ccc1a69ffd361e0a7d2831fe317f6b685636014f426321a39ae02f8da0dc"
         
         gcloud config set project "${PROJECT_ID}"
         gcloud config set billing/quota_project "${PROJECT_ID}"

Replace the following:

     * `YOUR_PROJECT_ID`: the ID of your Google Cloud project.
     * `YOUR_REGION`: the region where you want to deploy your cluster, such as `us-central1`.
     * `YOUR_ZONE`: the zone where you want to deploy your TPU7x node pools, such as `us-central1-c`.
     * `YOUR_CLUSTER_NAME`: the name of your GKE cluster.
     * `YOUR_RESERVATION_NAME`: the name of your TPU reservation, if you're using a reservation.
     * `YOUR_GCS_BUCKET`: the name of the Cloud Storage bucket that you use to stage the model weights.
     * `YOUR_HF_TOKEN`: your Hugging Face access token.
     * `YOUR_VLLM_IMAGE`: the vLLM TorchTPU image to use. For public images, refer to the [vLLM TorchTPU](https://github.com/vllm-project/vllm-torchtpu) repository.



## Create the GKE cluster

To create a GKE cluster in Standard mode and attach two multi-host TPU7x node pools for prefill and decode disaggregation, complete the following steps:

  1. Create a regional GKE cluster with Workload Identity Federation for GKE enabled:
         
         gcloud container clusters create "${CLUSTER_NAME}" \
             --project="${PROJECT_ID}" \
             --location="${REGION}" \
             --node-locations="${ZONE}" \
             --machine-type="e2-standard-4" \
             --workload-pool="${PROJECT_ID}.svc.id.goog"

The output is similar to the following:
         
         NAME     LOCATION       MASTER_VERSION      MASTER_IP      MACHINE_TYPE   NODE_VERSION        NUM_NODES  STATUS   STACK_TYPE
         asq-v7x  us-central1    1.35.7-gke.1027000  35.226.172.84  e2-standard-4  1.35.7-gke.1027000  3          RUNNING  IPV4
         

  2. Create a high-throughput workload placement policy with a `2x2x2` accelerator topology, which is required for multi-host TPU7x node pools:
         
         gcloud compute resource-policies create workload-policy "${WORKLOAD_POLICY_NAME}" \
             --type=HIGH_THROUGHPUT \
             --accelerator-topology=2x2x2 \
             --project="${PROJECT_ID}" \
             --region="${REGION}"

  3. Create two multi-host TPU7x node pools (`np-0` and `np-1`), each containing two `tpu7x-standard-4t` nodes (eight TPU7x chips in a `2x2x2` topology per node pool, for a total of 16 TPU7x chips):
         
         gcloud container node-pools create "${NODE_POOL_NAME_0}" \
             --cluster="${CLUSTER_NAME}" \
             --machine-type="${MACHINE_TYPE}" \
             --placement-policy="${WORKLOAD_POLICY_NAME}" \
             --location="${REGION}" \
             --node-locations="${ZONE}" \
             --project="${PROJECT_ID}" \
             --num-nodes=2 \
             --spot
         
         gcloud container node-pools create "${NODE_POOL_NAME_1}" \
             --cluster="${CLUSTER_NAME}" \
             --machine-type="${MACHINE_TYPE}" \
             --placement-policy="${WORKLOAD_POLICY_NAME}" \
             --location="${REGION}" \
             --node-locations="${ZONE}" \
             --project="${PROJECT_ID}" \
             --num-nodes=2 \
             --spot

This tutorial uses Spot capacity (`--spot`). Instances using Spot capacity might take time to be created after the node pool is created, and they might be preempted during workload runs. You can also create the node pools using a reservation or Flex-start VMs by passing the following flags:

     * **Specific reservation** : replace the `--spot` flag with the `--reservation-affinity=specific` and `--reservation=RESERVATION_NAME` flags, where `RESERVATION_NAME` is the name of the reservation that GKE uses when creating the node pool. To learn more about TPU reservations, see [About Cloud TPU reservations](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations).
     * **Flex-start VMs** : replace the `--spot` and `--num-nodes=2` flags with the `--flex-start`, `--reservation-affinity=none`, `--enable-autoscaling`, `--num-nodes=0`, `--min-nodes=0`, and `--max-nodes=2` flags to provision the node pool using the [Flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws) consumption option. For more information, see [Run a small batch workload with TPUs and Flex-start VMs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dws-flex-start-training-tpu).

The output for each node pool is similar to the following:
    
    NAME  MACHINE_TYPE       DISK_SIZE_GB  NODE_VERSION
    np-0  tpu7x-standard-4t  100           1.35.7-gke.1027000
    

  4. Configure `kubectl` credentials to communicate with your cluster:
         
         gcloud container clusters get-credentials "${CLUSTER_NAME}" \
             --location="${REGION}" \
             --project="${PROJECT_ID}"




## Stage the model weights in Cloud Storage

Stage the model weights in a Cloud Storage bucket for your workload runs:

  1. Create a Cloud Storage bucket with uniform bucket-level access:
         
         gcloud storage buckets create "gs://${GCS_BUCKET}" \
             --project="${PROJECT_ID}" \
             --location="${REGION}" \
             --uniform-bucket-level-access

  2. Grant Identity and Access Management (IAM) permissions on the bucket to your default Compute Engine service account and the default Kubernetes service account:
         
         PROJECT_NUMBER=$(gcloud projects describe "${PROJECT_ID}" --format="value(projectNumber)")
         
         gcloud storage buckets add-iam-policy-binding "gs://${GCS_BUCKET}" \
             --member="serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
             --role="roles/storage.objectAdmin"
         
         gcloud storage buckets add-iam-policy-binding "gs://${GCS_BUCKET}" \
             --member="principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${PROJECT_ID}.svc.id.goog/subject/ns/default/sa/default" \
             --role="roles/storage.admin"

  3. Create a Kubernetes secret named `hf-secret` to store your Hugging Face access token:
         
         kubectl create secret generic hf-secret \
             --from-literal=hf_api_token="${HF_TOKEN}" \
             --dry-run=client -o yaml | kubectl apply -f -

  4. Fetch the `download_model.yaml` config:
         
         curl -O https://raw.githubusercontent.com/GoogleCloudSamples/AIHypercomputerSamples/main/tpu/inference/qwen3-5-397b-multihost/download_model.yaml

Alternatively, you can choose to create a file named `download_model.yaml` with the following content:
         
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: download-qwen35
           namespace: default
         spec:
           backoffLimit: 1
           template:
             spec:
               restartPolicy: OnFailure
               # Schedule onto a TPU node (requests 0 TPUs so it can run alongside or before workloads)
               nodeSelector:
                 cloud.google.com/gke-tpu-accelerator: tpu7x
               tolerations:
               - operator: Exists
               containers:
               - name: model-downloader
                 image: gcr.io/google.com/cloudsdktool/google-cloud-cli:slim
                 env:
                 - name: HF_TOKEN
                   valueFrom:
                     secretKeyRef:
                       name: hf-secret
                       key: hf_api_token
                 # Enable high-performance concurrent chunked downloads in huggingface_hub
                 - name: HF_XET_HIGH_PERFORMANCE
                   value: "1"
                 # Place Hugging Face cache on the staging volume so the 100GB boot disk never fills up
                 - name: HF_HOME
                   value: "/local-ssd/hf-cache"
                 command: ["/bin/bash", "-c"]
                 args:
                 - |
                   set -euo pipefail
         
                   echo "=== 1. Installing huggingface_hub ==="
                   pip3 install --break-system-packages -q -U "huggingface_hub"
         
                   echo "=== 2. Downloading Qwen/Qwen3.5-397B-A17B-FP8 to Local Staging Volume ==="
                   hf download Qwen/Qwen3.5-397B-A17B-FP8 --local-dir /local-ssd/Qwen/Qwen3.5-397B-A17B-FP8
                   rm -rf /local-ssd/Qwen/Qwen3.5-397B-A17B-FP8/.cache
         
                   echo "=== 3. Uploading from Local Staging Volume to GCS ==="
                   gcloud config set storage/parallel_composite_upload_compatibility_check False
                   gcloud storage cp -r /local-ssd/Qwen gs://${GCS_BUCKET}/
         
                   echo "=== 4. Cleaning up Local Staging Volume ==="
                   rm -rf /local-ssd/Qwen /local-ssd/hf-cache
                 resources:
                   requests:
                     cpu: "64"
                     memory: "128Gi"
                 volumeMounts:
                 - name: local-ssd
                   mountPath: /local-ssd
               volumes:
               - name: local-ssd
                 # If the TPU node pool was created with --ephemeral-storage-local-ssd, use `emptyDir: {}`.
                 # On standard tpu7x-standard-4t / ct6e-standard-4t node pools without Local SSDs attached,
                 # `emptyDir: {}` uses the 100GB boot disk; use `medium: Memory` (RAM disk) instead:
                 emptyDir:
                   medium: Memory
                   sizeLimit: 450Gi

  5. Download the model weights to the staging volume and transfer them to your Cloud Storage bucket:
         
         envsubst '$GCS_BUCKET' < download_model.yaml | kubectl apply -f -

This step takes approximately 30 to 40 minutes to complete.

  6. After the job finishes, verify that all 163 `.safetensors` shards are in your Cloud Storage bucket:
         
         gcloud storage ls "gs://${GCS_BUCKET}/Qwen/Qwen3.5-397B-A17B-FP8/*.safetensors" | wc -l

  7. Delete the completed staging Job:
         
         kubectl delete job download-qwen35

  8. Wait until the Pod starts and monitor the download Job logs:
         
         kubectl wait --for=condition=Ready pod -l job-name=download-qwen35 --timeout=120s
         kubectl logs -f job/download-qwen35




## Deploy the multi-host vLLM TorchTPU server

The workload manifest (`v7x_qwen3_5_server_multihost_slice.yaml`) defines a Kubernetes JobSet resource (`vllm-qwen3-5-397b-pd-disagg-v7x`) with three replicated jobs that coordinate disaggregated prefill and decode serving across the two `2x2x2` TPU7x node pools:

  * **Prefill server (`prefill`)**: runs two replicas across one `2x2x2` TPU7x node pool (two `tpu7x-standard-4t` nodes with four dual-core chips per host, for 16 TPU cores total). The Pods form a two-node Ray cluster and launch vLLM TorchTPU on port `8000` for `Qwen/Qwen3.5-397B-A17B-FP8` with `--data-parallel-size=16`, `--tensor-parallel-size=1`, `--enable-expert-parallel`, `--load-format=runai_streamer`, and `TPURaidenConnector` configured as `kv_producer`.
  * **Decode server (`decode`)**: runs two replicas across the second `2x2x2` TPU7x node pool (16 TPU cores total), using Pod affinity and anti-affinity rules on `cloud.google.com/gke-nodepool` to isolate prefill and decode onto separate node pools. The Pods form a two-node Ray cluster and launch vLLM TorchTPU on port `7200` with TPURaidenConnector configured as `kv_consumer`.
  * **Disaggregation proxy (`proxy`)**: runs `toy_proxy_server.py` on port `10000` to coordinate request routing and KV cache transfer between the prefill server (port `8000`) and the decode server (port `7200`).



To deploy and monitor the disaggregated vLLM servers, complete the following steps:

  1. Install the Kubernetes JobSet CustomResourceDefinition and controller on your cluster:
         
         kubectl apply --server-side -f https://github.com/kubernetes-sigs/jobset/releases/download/v0.12.0/manifests.yaml
         kubectl wait --for=condition=Available --timeout=300s deployment/jobset-controller-manager -n jobset-system

  2. Fetch the server manifest:
         
         curl -O https://raw.githubusercontent.com/GoogleCloudSamples/AIHypercomputerSamples/main/tpu/inference/qwen3-5-397b-multihost/v7x_qwen3_5_server_multihost_slice.yaml

Alternatively, you can create a file named `v7x_qwen3_5_server_multihost_slice.yaml` with the following content:
         
         apiVersion: jobset.x-k8s.io/v1alpha2
         kind: JobSet
         metadata:
           name: vllm-qwen3-5-397b-pd-disagg-v7x
         spec:
           failurePolicy:
             restartStrategy: BlockingRecreate
             maxRestarts: 5
           ttlSecondsAfterFinished: 86400
           network:
             enableDNSHostnames: true
           replicatedJobs:
           # ---------------------------------------------------------
           # PREFILL SERVERS (2 Replicas, 1 Node each = 4 dual-core chips / 8 TPU devices per host = 16 TPU devices on 2x2x2 v7x slice)
           # ---------------------------------------------------------
           - name: prefill
             replicas: 2
             template:
               spec:
                 parallelism: 1
                 completions: 1
                 backoffLimit: 0
                 template:
                   metadata:
                     labels:
                       app: vllm-tpu-prefill
                   spec:
                     dnsPolicy: ClusterFirstWithHostNet
                     nodeSelector:
                       cloud.google.com/gke-tpu-topology: 2x2x2
                       cloud.google.com/gke-tpu-accelerator: tpu7x
                     tolerations:
                     - key: "google.com/tpu"
                       operator: "Exists"
                       effect: "NoSchedule"
                     - key: "cloud.google.com/gke-spot"
                       operator: "Equal"
                       value: "true"
                       effect: "NoSchedule"
                     affinity:
                       podAntiAffinity:
                         requiredDuringSchedulingIgnoredDuringExecution:
                         - labelSelector:
                             matchExpressions:
                             - key: app
                               operator: In
                               values:
                               - vllm-tpu-decode
                           topologyKey: "cloud.google.com/gke-nodepool"
                       podAffinity:
                         requiredDuringSchedulingIgnoredDuringExecution:
                         - labelSelector:
                             matchExpressions:
                             - key: app
                               operator: In
                               values:
                               - vllm-tpu-prefill
                           topologyKey: "cloud.google.com/gke-nodepool"
                     initContainers:
                     - name: tpu-node-setup
                       image: busybox
                       securityContext:
                         privileged: true
                       command:
                       - /bin/sh
                       - -c
                       args:
                       - |
                         sysctl -w vm.max_map_count=8388608
                         if [ -f /sys/module/vfio_iommu_type1/parameters/dma_entry_limit ]; then
                           echo 2000000 > /sys/module/vfio_iommu_type1/parameters/dma_entry_limit
                         fi
                     containers:
                     - name: vllm-tpu-prefill
                       image: ${VLLM_IMAGE}
                       imagePullPolicy: IfNotPresent
                       command:
                       - /bin/bash
                       - -c
                       args:
                         - |
                           set -e
                           export TPU_WORKER_ID=$JOBSET_JOB_INDEX
                           unset TPU_VISIBLE_CHIPS
         
                           echo "=== Installing runai-model-streamer[gcs] and pre-caching metadata from GCS on $HOSTNAME ==="
                           pip install -q "runai-model-streamer[gcs]==0.16.1"
                           python3 -c "from vllm.transformers_utils.runai_utils import ObjectStorageModel; uri = 'gs://${GCS_BUCKET}/Qwen/Qwen3.5-397B-A17B-FP8'; m = ObjectStorageModel(uri); m.pull_files(uri, ignore_pattern=['*.pt', '*.safetensors', '*.bin', '*.tensors', '*.pth']); print('Pulled metadata/tokenizer to', m.dir)"
         
                           HEAD_ADDR="${JS_NAME}-prefill-0-0.${JS_NAME}"
         
                           if [ "$JOBSET_JOB_INDEX" = "0" ]; then
                             echo "=== Node 0: Starting Ray Head on $HOSTNAME (port 6379, IP $POD_IP) ==="
                             ray start --head --port=6379 --node-ip-address=$POD_IP --resources='{"TPU": 8}' --block &
         
                             echo "Waiting for worker node to join Ray cluster (expecting 16.0 TPU total across 2 nodes)..."
                             until ray status 2>/dev/null | grep -E -q "16(\.0)? TPU"; do
                               echo "Waiting for worker to connect to Ray Head..."
                               sleep 2
                             done
                             echo "Worker joined! Ray cluster status:"
                             ray status
         
                             echo "=== Starting vLLM Prefill Server (Qwen3.5 397B FP8, DP=16, TP=1, Port 8000) ==="
                             PREFILL_ARGS=(
                               gs://${GCS_BUCKET}/Qwen/Qwen3.5-397B-A17B-FP8
                               --served-model-name=Qwen/Qwen3.5-397B-A17B-FP8
                               --api-server-count=1
                               --load-format=runai_streamer
                               --enable-ep-weight-filter
                               --tensor-parallel-size=1
                               --data-parallel-size=16
                               --data-parallel-size-local=8
                               --data-parallel-backend=ray
                               --data-parallel-address=$POD_IP
                               --distributed-executor-backend=ray
                               --enable-expert-parallel
                               --max-model-len=18432
                               --max-num-batched-tokens=8192
                               --max-num-seqs=64
                               --num-gpu-blocks-override=256
                               --host=0.0.0.0
                               --port=8000
                               --async-scheduling
                               --no-enable-prefix-caching
                               --kv-cache-dtype=fp8
                               --attention-backend=CUSTOM
                               --block-size=1024
                               --return-tokens-as-token-ids
                               --compilation-config '{"backend":"vllm_torchtpu.compilation.tpu_compiler.TpuCompilerAdaptor","compile_sizes":[4096,8192],"inductor_compile_config":{"enable_auto_functionalized_v2":false,"size_asserts":false,"alignment_asserts":false,"scalar_asserts":false}}'
                               --kv-transfer-config '{"kv_connector":"TPURaidenConnector","kv_connector_module_path":"vllm_torchtpu.distributed.kv_transfer.tpu_connector","kv_role":"kv_producer","kv_port":14579}'
                             )
                             exec vllm serve "${PREFILL_ARGS[@]}"
                           else
                             echo "=== Node 1: Starting Ray Worker on $HOSTNAME (IP $POD_IP) ==="
                             until timeout 1 bash -c "cat < /dev/null > /dev/tcp/${HEAD_ADDR}/6379" 2>/dev/null; do
                               echo "Waiting for Ray head at ${HEAD_ADDR}:6379..."
                               sleep 2
                             done
                             echo "Ray head is reachable! Starting Ray worker..."
                             sleep 3
                             exec ray start --address="${HEAD_ADDR}:6379" --node-ip-address=$POD_IP --resources='{"TPU": 8}' --block
                           fi
         
                       env:
                       - name: JS_NAME
                         valueFrom:
                           fieldRef:
                             fieldPath: metadata.labels['jobset.sigs.k8s.io/jobset-name']
                       - name: JOBSET_JOB_INDEX
                         valueFrom:
                           fieldRef:
                             fieldPath: metadata.labels['jobset.sigs.k8s.io/job-index']
                       - name: POD_IP
                         valueFrom:
                           fieldRef:
                             fieldPath: status.podIP
                       - name: TPU_MULTIHOST_BACKEND
                         value: "ray"
                       - name: RAY_EXPERIMENTAL_NOSET_TPU_VISIBLE_CHIPS
                         value: "1"
                       - name: RAY_ADDRESS
                         value: "127.0.0.1:6379"
                       - name: VLLM_ENGINE_READY_TIMEOUT_S
                         value: "14400"
                       - name: SKIP_MEGASCALE_PJRT_CLIENT
                         value: "true"
                       - name: USE_MOE_FUSED_EP_KERNEL
                         value: "1"
                       - name: ONEHOT_MOE_PERMUTE_THRESHOLD
                         value: "2048"
                       - name: LIBTPU_INIT_ARGS
                         value: "--xla_tpu_use_minor_sharding_for_major_trivial_input=true --xla_tpu_enable_sparse_core_collective_offload_reduce_scatter=false --xla_tpu_ars_combiner_threshold_in_bytes=0 --xla_tpu_enable_async_collective_merger=false --xla_tpu_enable_diagnostic_coordinator=false --xla_enable_async_all_gather=true --xla_tpu_enable_sparse_core_collective_offload_all_gather=true --xla_tpu_sparse_core_all_gather_offload_min_size_in_bytes=262144"
                       # Raiden KV-transfer configuration (Prefill / Producer)
                       - name: TPU_KV_RESHARD_TRANSPORT
                         value: "raiden"
                       - name: TPU_RAIDEN_RESHARD_IMPL
                         value: "store"
                       - name: TPU_RAIDEN_ADVERTISE_HOST
                         valueFrom:
                           fieldRef:
                             fieldPath: status.podIP
                       - name: TPU_USE_RAIDEN_KV_CACHE_MANAGER
                         value: "1"
                       - name: TPU_RAIDEN_QWEN35_ADMISSION
                         value: "1"
                       - name: TPU_RAIDEN_TRANSFER_PARALLELISM
                         value: "1"
                       volumeMounts:
                       - name: dshm
                         mountPath: /dev/shm
                       securityContext:
                         privileged: true
                         capabilities:
                           add:
                           - IPC_LOCK
                       ports:
                       - name: http
                         containerPort: 8000
                       - name: ray-gcs
                         containerPort: 6379
                       resources:
                         limits:
                           google.com/tpu: "4"
                         requests:
                           google.com/tpu: "4"
                     volumes:
                     - name: dshm
                       emptyDir:
                         medium: Memory
         
           # ---------------------------------------------------------
           # DECODE SERVERS (2 Replicas, 1 Node each = 4 dual-core chips / 8 TPU devices per host = 16 TPU devices on 2x2x2 v7x slice)
           # ---------------------------------------------------------
           - name: decode
             replicas: 2
             template:
               spec:
                 parallelism: 1
                 completions: 1
                 backoffLimit: 0
                 template:
                   metadata:
                     labels:
                       app: vllm-tpu-decode
                   spec:
                     dnsPolicy: ClusterFirstWithHostNet
                     nodeSelector:
                       cloud.google.com/gke-tpu-topology: 2x2x2
                       cloud.google.com/gke-tpu-accelerator: tpu7x
                     tolerations:
                     - key: "google.com/tpu"
                       operator: "Exists"
                       effect: "NoSchedule"
                     - key: "cloud.google.com/gke-spot"
                       operator: "Equal"
                       value: "true"
                       effect: "NoSchedule"
                     affinity:
                       podAntiAffinity:
                         requiredDuringSchedulingIgnoredDuringExecution:
                         - labelSelector:
                             matchExpressions:
                             - key: app
                               operator: In
                               values:
                               - vllm-tpu-prefill
                           topologyKey: "cloud.google.com/gke-nodepool"
                       podAffinity:
                         requiredDuringSchedulingIgnoredDuringExecution:
                         - labelSelector:
                             matchExpressions:
                             - key: app
                               operator: In
                               values:
                               - vllm-tpu-decode
                           topologyKey: "cloud.google.com/gke-nodepool"
                     initContainers:
                     - name: tpu-node-setup
                       image: busybox
                       securityContext:
                         privileged: true
                       command:
                       - /bin/sh
                       - -c
                       args:
                       - |
                         sysctl -w vm.max_map_count=8388608
                         if [ -f /sys/module/vfio_iommu_type1/parameters/dma_entry_limit ]; then
                           echo 2000000 > /sys/module/vfio_iommu_type1/parameters/dma_entry_limit
                         fi
                     containers:
                     - name: vllm-tpu-decode
                       image: ${VLLM_IMAGE}
                       imagePullPolicy: IfNotPresent
                       command:
                       - /bin/bash
                       - -c
                       args:
                         - |
                           set -e
                           export TPU_WORKER_ID=$JOBSET_JOB_INDEX
                           unset TPU_VISIBLE_CHIPS
         
                           echo "=== Installing runai-model-streamer[gcs] and pre-caching metadata from GCS on $HOSTNAME ==="
                           pip install -q "runai-model-streamer[gcs]==0.16.1"
                           python3 -c "from vllm.transformers_utils.runai_utils import ObjectStorageModel; uri = 'gs://${GCS_BUCKET}/Qwen/Qwen3.5-397B-A17B-FP8'; m = ObjectStorageModel(uri); m.pull_files(uri, ignore_pattern=['*.pt', '*.safetensors', '*.bin', '*.tensors', '*.pth']); print('Pulled metadata/tokenizer to', m.dir)"
         
                           HEAD_ADDR="${JS_NAME}-decode-0-0.${JS_NAME}"
         
                           if [ "$JOBSET_JOB_INDEX" = "0" ]; then
                             echo "=== Node 0: Starting Ray Head on $HOSTNAME (port 6379, IP $POD_IP) ==="
                             ray start --head --port=6379 --node-ip-address=$POD_IP --resources='{"TPU": 8}' --block &
         
                             echo "Waiting for worker node to join Ray cluster (expecting 16.0 TPU total across 2 nodes)..."
                             until ray status 2>/dev/null | grep -E -q "16(\.0)? TPU"; do
                               echo "Waiting for worker to connect to Ray Head..."
                               sleep 2
                             done
                             echo "Worker joined! Ray cluster status:"
                             ray status
         
                             echo "=== Starting vLLM Decode Server (Qwen3.5 397B FP8, DP=16, TP=1, Port 7200) ==="
                             DECODE_ARGS=(
                               gs://${GCS_BUCKET}/Qwen/Qwen3.5-397B-A17B-FP8
                               --served-model-name=Qwen/Qwen3.5-397B-A17B-FP8
                               --api-server-count=1
                               --load-format=runai_streamer
                               --enable-ep-weight-filter
                               --tensor-parallel-size=1
                               --data-parallel-size=16
                               --data-parallel-size-local=8
                               --data-parallel-backend=ray
                               --data-parallel-address=$POD_IP
                               --distributed-executor-backend=ray
                               --enable-expert-parallel
                               --max-model-len=18432
                               --max-num-batched-tokens=2048
                               --max-num-seqs=64
                               --num-gpu-blocks-override=256
                               --host=0.0.0.0
                               --port=7200
                               --async-scheduling
                               --no-enable-prefix-caching
                               --kv-cache-dtype=fp8
                               --attention-backend=CUSTOM
                               --block-size=8192
                               --compilation-config '{"backend":"vllm_torchtpu.compilation.tpu_compiler.TpuCompilerAdaptor","compile_sizes":[8,16,32,64,2048],"inductor_compile_config":{"enable_auto_functionalized_v2":false,"size_asserts":false,"alignment_asserts":false,"scalar_asserts":false}}'
                               --kv-transfer-config '{"kv_connector":"TPURaidenConnector","kv_connector_module_path":"vllm_torchtpu.distributed.kv_transfer.tpu_connector","kv_role":"kv_consumer","kv_port":14579}'
                             )
                             exec vllm serve "${DECODE_ARGS[@]}"
                           else
                             echo "=== Node 1: Starting Ray Worker on $HOSTNAME (IP $POD_IP) ==="
                             until timeout 1 bash -c "cat < /dev/null > /dev/tcp/${HEAD_ADDR}/6379" 2>/dev/null; do
                               echo "Waiting for Ray head at ${HEAD_ADDR}:6379..."
                               sleep 2
                             done
                             echo "Ray head is reachable! Starting Ray worker..."
                             sleep 3
                             exec ray start --address="${HEAD_ADDR}:6379" --node-ip-address=$POD_IP --resources='{"TPU": 8}' --block
                           fi
         
                       env:
                       - name: JS_NAME
                         valueFrom:
                           fieldRef:
                             fieldPath: metadata.labels['jobset.sigs.k8s.io/jobset-name']
                       - name: JOBSET_JOB_INDEX
                         valueFrom:
                           fieldRef:
                             fieldPath: metadata.labels['jobset.sigs.k8s.io/job-index']
                       - name: POD_IP
                         valueFrom:
                           fieldRef:
                             fieldPath: status.podIP
                       - name: TPU_MULTIHOST_BACKEND
                         value: "ray"
                       - name: RAY_EXPERIMENTAL_NOSET_TPU_VISIBLE_CHIPS
                         value: "1"
                       - name: RAY_ADDRESS
                         value: "127.0.0.1:6379"
                       - name: VLLM_ENGINE_READY_TIMEOUT_S
                         value: "14400"
                       - name: SKIP_MEGASCALE_PJRT_CLIENT
                         value: "true"
                       - name: USE_MOE_FUSED_EP_KERNEL
                         value: "1"
                       - name: ONEHOT_MOE_PERMUTE_THRESHOLD
                         value: "2048"
                       - name: RAGGED_GATHER_REDUCE_VERSION
                         value: "v3"
                       - name: USE_BATCHED_RPA_LONGCTX
                         value: "1"
                       - name: LIBTPU_INIT_ARGS
                         value: "--xla_tpu_use_minor_sharding_for_major_trivial_input=true --xla_tpu_enable_sparse_core_collective_offload_reduce_scatter=false --xla_tpu_ars_combiner_threshold_in_bytes=0 --xla_tpu_enable_async_collective_merger=false --xla_tpu_enable_diagnostic_coordinator=false --xla_enable_async_all_gather=true --xla_tpu_enable_sparse_core_collective_offload_all_gather=true --xla_tpu_sparse_core_all_gather_offload_min_size_in_bytes=262144"
                       # Raiden KV-transfer configuration (Decode / Consumer)
                       - name: TPU_KV_RESHARD_TRANSPORT
                         value: "raiden"
                       - name: TPU_RAIDEN_RESHARD_IMPL
                         value: "store"
                       - name: TPU_RAIDEN_ADVERTISE_HOST
                         valueFrom:
                           fieldRef:
                             fieldPath: status.podIP
                       - name: TPU_USE_RAIDEN_KV_CACHE_MANAGER
                         value: "1"
                       - name: TPU_RAIDEN_QWEN35_ADMISSION
                         value: "1"
                       - name: TPU_RAIDEN_TRANSFER_PARALLELISM
                         value: "1"
                       volumeMounts:
                       - name: dshm
                         mountPath: /dev/shm
                       securityContext:
                         privileged: true
                         capabilities:
                           add:
                           - IPC_LOCK
                       ports:
                       - name: http
                         containerPort: 7200
                       - name: ray-gcs
                         containerPort: 6379
                       resources:
                         limits:
                           google.com/tpu: "4"
                         requests:
                           google.com/tpu: "4"
                     volumes:
                     - name: dshm
                       emptyDir:
                         medium: Memory
         
           # ---------------------------------------------------------
           # DISAGGREGATION PROXY (Coordinates Prefill -> Decode)
           # ---------------------------------------------------------
           - name: proxy
             replicas: 1
             template:
               spec:
                 parallelism: 1
                 completions: 1
                 backoffLimit: 2
                 template:
                   spec:
                     containers:
                     - name: vllm-tpu-proxy
                       image: ${VLLM_IMAGE}
                       imagePullPolicy: IfNotPresent
                       command:
                       - /bin/bash
                       - -c
                       args:
                       - |
                         set -e
                         exec python3 /root/torchtpu-vllm/examples/disagg/toy_proxy_server.py \
                           --host 0.0.0.0 \
                           --port 10000 \
                           --prefiller-host "${JS_NAME}-prefill-0-0.${JS_NAME}" \
                           --prefiller-port 8000 \
                           --decoder-host "${JS_NAME}-decode-0-0.${JS_NAME}" \
                           --decoder-port 7200
                       env:
                       - name: JS_NAME
                         valueFrom:
                           fieldRef:
                             fieldPath: metadata.labels['jobset.sigs.k8s.io/jobset-name']
                       ports:
                       - name: http
                         containerPort: 10000
                       resources:
                         requests: { cpu: "2", memory: "4Gi" }
                         limits: { cpu: "8", memory: "16Gi" }

  3. Substitute your Cloud Storage bucket name into `v7x_qwen3_5_server_multihost_slice.yaml` and apply the manifest:
         
         envsubst '${GCS_BUCKET} ${VLLM_IMAGE}' < "v7x_qwen3_5_server_multihost_slice.yaml" | kubectl apply -f -

This configuration uses one `2x2x2` TPU7x slice (two nodes) for prefill and one `2x2x2` TPU7x slice (two nodes) for decode. To scale the number of nodes in either pool, update the `replicas` field (`replicas: NUM_NODES`).

  4. Monitor the prefill and decode Pod logs until application startup completes:
         
         # Prefill logs
         kubectl logs -l jobset.sigs.k8s.io/replicatedjob-name=prefill -f --tail=-1
         
         # Decode logs
         kubectl logs -l jobset.sigs.k8s.io/replicatedjob-name=decode -f --tail=-1

Initial model loading and compilation take approximately 30 to 45 minutes on the first run.

If you're using preemptible capacity such as Spot or Flex-start VMs, it might take longer after node pool creation for your TPU slice nodes to be created, and they can be preempted during workload runs. For more details, see [Preemptible VM instances](https://docs.cloud.google.com/compute/docs/instances/preemptible#preemption). To check whether your TPU slice nodes have been created, see [Check the node's status and conditions](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/node-notready#check-node-status-conditions).

Wait until both the prefill and decode server logs report `Application startup complete` before running the benchmark:
         
         (APIServer pid=1) INFO:     Started server process [1]
         (APIServer pid=1) INFO:     Waiting for application startup.
         (APIServer pid=1) INFO:     Application startup complete.
         




## Run a benchmark workload

To benchmark the deployed Qwen3.5-397B model using an 8,192-token input and 1,024-token output (`8k/1k`) workload against the disaggregation proxy, complete the following steps:

  1. Fetch the benchmark manifest:
         
         curl -O https://raw.githubusercontent.com/GoogleCloudSamples/AIHypercomputerSamples/main/tpu/inference/qwen3-5-397b-multihost/v7x_qwen3_5_benchmark_multihost_slice.yaml

Alternatively, you can create a file named `v7x_qwen3_5_benchmark_multihost_slice.yaml` with the following content:
         
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: vllm-qwen3-5-397b-pd-disagg-v7x-tester
         spec:
           parallelism: 1
           completions: 1
           backoffLimit: 0
           template:
             spec:
               restartPolicy: Never
               containers:
               - name: vllm-test
                 image: ${VLLM_IMAGE}
                 imagePullPolicy: IfNotPresent
                 resources:
                   requests: { cpu: "1", memory: "4Gi" }
                   limits: { cpu: "4", memory: "8Gi" }
                 command:
                 - /bin/bash
                 - -c
                 args:
                 - |
                   set -e
                   PREFILLER_DNS="${JS_NAME}-prefill-0-0.${JS_NAME}"
                   DECODER_DNS="${JS_NAME}-decode-0-0.${JS_NAME}"
                   PROXY_DNS="${JS_NAME}-proxy-0-0.${JS_NAME}"
                   MODEL="Qwen/Qwen3.5-397B-A17B-FP8"
         
                   echo 'import torch; torch.utils.rename_privateuse1_backend("tpu")' > /tmp/sitecustomize.py
                   export PYTHONPATH="/tmp:${PYTHONPATH:-}"
         
                   wait_for() {
                     local name="$1" url="$2" timeout=18000 elapsed=0
                     echo "Waiting for $name ($url)..."
                     until curl -sf "$url" > /dev/null; do
                       [ "$elapsed" -ge "$timeout" ] && { echo "ERROR: $name timeout" >&2; exit 1; }
                       sleep 10; elapsed=$((elapsed + 10))
                     done
                     echo "$name is up after ${elapsed}s!"
                   }
                   wait_for prefill "http://$PREFILLER_DNS:8000/health"
                   wait_for decode  "http://$DECODER_DNS:7200/health"
                   wait_for proxy   "http://$PROXY_DNS:10000/healthcheck"
         
                   echo "=== BENCHMARK: 8K/1K c=128 n=1280 ==="
                   BENCH_ARGS=(
                     --backend openai-chat
                     --base-url "http://$PROXY_DNS:10000" --endpoint /v1/chat/completions
                     --model "$MODEL" --dataset-name random
                     --random-input-len 8192 --random-output-len 1024
                     --ignore-eos
                     --max-concurrency 128 --num-prompts 1280
                   )
                   if vllm bench serve "${BENCH_ARGS[@]}"; then
                     echo "=== BENCHMARK COMPLETED SUCCESSFULLY ==="
                   else
                     echo "ERROR: BENCHMARK FAILED"
                     exit 1
                   fi
                 env:
                 - name: JS_NAME
                   value: "vllm-qwen3-5-397b-pd-disagg-v7x"

  2. Apply the benchmark Job manifest and wait for the benchmark Pod to be ready:
         
         envsubst '${VLLM_IMAGE}' < v7x_qwen3_5_benchmark_multihost_slice.yaml | kubectl apply -f -

  3. Monitor the benchmark Job logs:
         
         kubectl wait --for=condition=Ready pod -l job-name=vllm-qwen3-5-397b-pd-disagg-v7x-tester --timeout=300s
         kubectl logs -f job/vllm-qwen3-5-397b-pd-disagg-v7x-tester




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, delete the Kubernetes workloads, the TPU7x node pools, the GKE cluster, and your Cloud Storage bucket:

  1. Delete the Kubernetes workloads:
         
         kubectl delete -f v7x_qwen3_5_server_multihost_slice.yaml --ignore-not-found || true
         kubectl delete secret hf-secret --ignore-not-found || true

  2. Delete the TPU7x node pools, the workload placement policy, and the GKE cluster:
         
         gcloud container node-pools delete "${NODE_POOL_NAME_0}" \
             --cluster="${CLUSTER_NAME}" \
             --location="${REGION}" \
             --project="${PROJECT_ID}" \
             --quiet || true
         
         gcloud container node-pools delete "${NODE_POOL_NAME_1}" \
             --cluster="${CLUSTER_NAME}" \
             --location="${REGION}" \
             --project="${PROJECT_ID}" \
             --quiet || true
         
         gcloud container clusters delete "${CLUSTER_NAME}" \
             --location="${REGION}" \
             --project="${PROJECT_ID}" \
             --quiet || true
         
         gcloud compute resource-policies delete "${WORKLOAD_POLICY_NAME}" \
             --region="${REGION}" \
             --project="${PROJECT_ID}" \
             --quiet || true

  3. Optionally, delete the Cloud Storage bucket that stores the staged model weights:
         
         gcloud storage rm --recursive "gs://${GCS_BUCKET}" --project="${PROJECT_ID}" --quiet || true




## What's next

  * Learn more about [vLLM on Cloud TPU](https://github.com/vllm-project/tpu-inference).
  * Learn more about [TPU7x (Ironwood)](https://docs.cloud.google.com/tpu/docs/tpu7x).
  * Learn more about [Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
