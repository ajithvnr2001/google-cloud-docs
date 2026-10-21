---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-qwen3-5-397b-ironwood-vllm-torchtpu/
title: Serve Qwen3.5-397B on GKE with vLLM TorchTPU on TPU7x accelerators \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:26:38.158048+00:00
---

# Serve Qwen3.5-397B on GKE with vLLM TorchTPU on TPU7x accelerators  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-qwen3-5-397b-ironwood-vllm-torchtpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Serve Qwen3.5-397B on GKE with vLLM TorchTPU on TPU7x accelerators Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to deploy and serve the mixture of experts model [Qwen3.5-397B (`Qwen/Qwen3.5-397B-A17B-FP8`)](https://huggingface.co/Qwen/Qwen3.5-397B-A17B-FP8) on Google Kubernetes Engine (GKE) using a single-host [TPU7x (Ironwood)](https://docs.cloud.google.com/tpu/docs/tpu7x) accelerator and the [vLLM TPU serving framework](https://github.com/vllm-project/vllm-torchtpu) with TorchTPU (`torchtpu`). Because Qwen3.5-397B requires a minimum of four TPU7x chips, you can run the workload on a single `tpu7x-standard-4t` node in a `2x2x1` topology with data parallelism and expert parallelism enabled.

## Objectives

  * Set up your GKE cluster and single-host TPU7x node pool.
  * Deploy the single-host vLLM TorchTPU server on GKE.
  * Send an inference request to the vLLM TorchTPU server.
  * Run a serving benchmark workload.
  * Clean up.



## Costs

In this document, you use the following billable components of Google Cloud:

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [Cloud TPU](https://docs.cloud.google.com/tpu/pricing)
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

[Enable the Kubernetes Engine API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  * Enable the Artifact Registry API in your Google Cloud project:

[Enable the Artifact Registry API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com)

  * [Install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the Google Cloud CLI, and install [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl). If you use Cloud Shell, both tools are preinstalled.

  * Ensure that your project has sufficient [SSD quota and external IP address quota](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#additional-quotas) in the region where your TPU capacity is located:

    1. In the Google Cloud console, go to the **Quotas & System Limits** page.

[Go to Quotas & System Limits](https://console.cloud.google.com/iam-admin/quotas)

    2. Filter by **Persistent Disk SSD (GB)** and verify that you have at least 1,500 GB of available quota for the model cache volume.

    3. Filter by **In-use regional external IPv4 addresses** and verify that you have sufficient IP address quota in your target region.


**Important:** To complete this tutorial, you must have quota for `TPU7x` TPUs in your Google Cloud project. This tutorial uses a TPU7x reservation, but you can also use Spot capacity or Flex-start VMs if available. To learn more about reserving Cloud TPU capacity, see [About Cloud TPU reservations](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations).

To get the permissions that you need to complete this tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
  * [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up your environment variables

Set up your authentication:
    
    
    gcloud auth login
    gcloud auth application-default login

Set up your environment variables:
    
    
    export PROJECT_ID="YOUR_PROJECT_ID"
    export REGION="YOUR_REGION"
    export ZONE="YOUR_ZONE"
    export CLUSTER_NAME="YOUR_CLUSTER_NAME"
    export MACHINE_TYPE="tpu7x-standard-4t"
    export NODE_POOL_NAME="np-0"
    export RESERVATION_NAME="YOUR_RESERVATION_NAME"
    export HF_TOKEN="YOUR_HF_TOKEN"
    export NETWORK="YOUR_NETWORK_NAME"
    export SUBNETWORK="YOUR_SUBNETWORK_NAME"
    export VLLM_IMAGE="YOUR_VLLM_TPU_IMAGE"
    
    gcloud config set project "${PROJECT_ID}"
    gcloud config set billing/quota_project "${PROJECT_ID}"

Replace the following:

  * `YOUR_PROJECT_ID`: the ID of your Google Cloud project.
  * `YOUR_REGION`: the region where you want to deploy your cluster, such as `us-central1`.
  * `YOUR_ZONE`: the zone where you want to deploy your TPU7x node pool, such as `us-central1-c`.
  * `YOUR_CLUSTER_NAME`: the name of your GKE cluster, such as `tpu7x-tutorial-cluster`.
  * `YOUR_RESERVATION_NAME`: if you're using a reservation, the name of your TPU7x reservation.
  * `YOUR_HF_TOKEN`: your Hugging Face access token.
  * `YOUR_NETWORK_NAME`: the name of your Google Cloud network. If you [created a custom network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks), then specify that network. Otherwise, specify `default`.
  * `YOUR_SUBNETWORK_NAME`: the name of your Google Cloud subnetwork. If you created a custom subnetwork, then specify that subnetwork. Otherwise, specify `default`.
  * `YOUR_VLLM_TPU_IMAGE`: the vLLM TorchTPU image to use. For public images, refer to the [vLLM TorchTPU](https://github.com/vllm-project/vllm-torchtpu) repository.



## Create the GKE cluster

To create a GKE cluster in Standard mode and attach a single-host TPU7x node pool, complete the following steps:

  1. Create a regional GKE cluster:
         
         gcloud container clusters create "${CLUSTER_NAME}" \
             --project="${PROJECT_ID}" \
             --location="${REGION}" \
             --node-locations="${ZONE}" \
             --network="${NETWORK}" \
             --subnetwork="${SUBNETWORK}"

The output is similar to the following:
         
         NAME                    LOCATION       MASTER_VERSION      MASTER_IP      MACHINE_TYPE    NODE_VERSION        NUM_NODES  STATUS
         tpu7x-tutorial-cluster  us-central1    1.35.7-gke.1027000  34.63.222.246  n2-standard-16  1.35.7-gke.1027000  3          RUNNING
         

  2. Create a single-host TPU7x node pool with one `tpu7x-standard-4t` node (four TPU7x chips in a `2x2x1` topology) using your reservation:
         
         gcloud container node-pools create "${NODE_POOL_NAME}" \
             --cluster="${CLUSTER_NAME}" \
             --machine-type="${MACHINE_TYPE}" \
             --location="${REGION}" \
             --node-locations="${ZONE}" \
             --project="${PROJECT_ID}" \
             --num-nodes=1 \
             --reservation-affinity=specific \
             --reservation="${RESERVATION_NAME}"

Instead of using a specific reservation, you can also create the node pool using Spot capacity or Flex-start VMs by passing the following flags:

     * **Spot VMs** : replace the `--reservation-affinity` and `--reservation` flags with `--spot` to use Spot capacity. Instances using Spot capacity might take time to be created after the node pool is created, and they might be preempted during workload runs. If your Pods take time to be created, or workloads stop in the middle of running, this could be the cause.
     * **Flex-start VMs** : pass the `--flex-start` flag to provision the node pool using the [Flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws) consumption option. For more information, see [Run a small batch workload with TPUs and Flex-start VMs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dws-flex-start-training-tpu).

The output is similar to the following:
    
    NAME  MACHINE_TYPE       DISK_SIZE_GB  NODE_VERSION
    np-0  tpu7x-standard-4t  100           1.35.7-gke.1027000
    

  3. Configure `kubectl` credentials to communicate with your cluster:
         
         gcloud container clusters get-credentials "${CLUSTER_NAME}" \
             --location="${REGION}" \
             --project="${PROJECT_ID}"




## Configure credentials

Create a Kubernetes Secret named `hf-secret` to store your Hugging Face access token:
    
    
    kubectl create secret generic hf-secret \
        --from-literal=hf_api_token="${HF_TOKEN}" \
        --dry-run=client -o yaml | kubectl apply -f -

## Deploy the vLLM TorchTPU server

The workload manifest (`qwen3_5_server.yaml`) defines the following resources:

  * A StorageClass (`hyperdisk-balanced-qwen3-5`) and a 1,500 GiB PersistentVolumeClaim (`hd-claim-qwen3-5`) backed by Google Cloud Hyperdisk Balanced storage to store the downloaded model weights, XLA compilation cache, and PyTorch compile cache.
  * A Deployment (`vllm-qwen3-5`) scheduled on a single TPU7x node with a `2x2x1` topology (`google.com/tpu: '4'`). The container runs `vllm serve` for `Qwen/Qwen3.5-397B-A17B-FP8` with `--data-parallel-size=8`, `--tensor-parallel-size=1`, `--enable-expert-parallel`, `--kv-cache-dtype=fp8`, `--max-model-len=9236`, and `--max-num-seqs=64`.
  * A `ClusterIP` Service (`vllm-qwen3-5-service`) that exposes port `8000`.



To deploy and monitor the workload, complete the following steps:

  1. Fetch the server manifest:
         
         curl -O https://raw.githubusercontent.com/GoogleCloudSamples/AIHypercomputerSamples/refs/heads/main/tpu/inference/qwen3-5-397b/qwen3_5_server.yaml

Alternately, you can choose to create a file named `qwen3_5_server.yaml` with the following content:
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: hyperdisk-balanced-qwen3-5
         provisioner: pd.csi.storage.gke.io
         parameters:
           type: hyperdisk-balanced
         reclaimPolicy: Delete
         volumeBindingMode: WaitForFirstConsumer
         allowVolumeExpansion: true
         ---
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: hd-claim-qwen3-5
           namespace: default
         spec:
           storageClassName: hyperdisk-balanced-qwen3-5
           accessModes:
             - ReadWriteOnce
           resources:
             requests:
               storage: 1500Gi
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: vllm-qwen3-5
           namespace: default
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: vllm-qwen3-5
           template:
             metadata:
               labels:
                 app: vllm-qwen3-5
             spec:
               nodeSelector:
                 cloud.google.com/gke-tpu-accelerator: tpu7x
                 cloud.google.com/gke-tpu-topology: 2x2x1
               tolerations:
               - key: "cloud.google.com/gke-spot"
                 operator: "Equal"
                 value: "true"
                 effect: "NoSchedule"
               containers:
               - name: vllm-tpu
                 image: $VLLM_IMAGE
                 command: ["vllm", "serve"]
                 args:
                 - --host=0.0.0.0
                 - --port=8000
                 - --model=Qwen/Qwen3.5-397B-A17B-FP8
                 - --tokenizer=Qwen/Qwen3.5-397B-A17B-FP8
                 - --max-model-len=9236
                 - --max-num-batched-tokens=1024
                 - --max-num-seqs=64
                 - --no-enable-prefix-caching
                 - --gpu-memory-utilization=0.9
                 - --data-parallel-size=8
                 - --tensor-parallel-size=1
                 - --async-scheduling
                 - --language-model-only
                 - --enable-auto-tool-choice
                 - --tool-call-parser=qwen3_coder
                 - --reasoning-parser=qwen3
                 - '--limit-mm-per-prompt={"image": 0, "video": 0}'
                 - --kv-cache-dtype=fp8
                 - --enable-expert-parallel
                 - --download-dir=/data
                 - --block-size=128
                 env:
                 - name: MODEL_IMPL_TYPE
                   value: "vllm"
                 - name: DP_SCHED_ENABLED
                   value: "1"
                 - name: ONEHOT_MOE_PERMUTE_THRESHOLD
                   value: "32768"
                 - name: VLLM_ENGINE_READY_TIMEOUT_S
                   value: "9600"
                 - name: VLLM_ENGINE_ITERATION_TIMEOUT_S
                   value: "1800"
                 - name: USE_MOE_SPARSE_CORE
                   value: "1"
                 - name: TPU_MOE_SKIP_PADDED_TOKENS
                   value: "1"
                 - name: VLLM_CACHE_ROOT
                   value: "/data/vllm_cache"
                 - name: VLLM_TORCH_COMPILE_CACHE_DIR
                   value: "/data/torch_compile_cache"
                 - name: XLA_CACHE_DIR
                   value: "/data/xla_cache"
                 - name: HF_HOME
                   value: /data
                 - name: HF_TOKEN
                   valueFrom:
                     secretKeyRef:
                       name: hf-secret
                       key: hf_api_token
                 ports:
                 - containerPort: 8000
                 resources:
                   limits:
                     google.com/tpu: '4'
                   requests:
                     google.com/tpu: '4'
                 readinessProbe:
                   tcpSocket:
                     port: 8000
                   initialDelaySeconds: 15
                   periodSeconds: 10
                 volumeMounts:
                 - mountPath: "/data"
                   name: data-volume
                 - mountPath: /dev/shm
                   name: dshm
               volumes:
               - emptyDir:
                   medium: Memory
                 name: dshm
               - name: data-volume
                 persistentVolumeClaim:
                   claimName: hd-claim-qwen3-5
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: vllm-qwen3-5-service
           namespace: default
         spec:
           selector:
             app: vllm-qwen3-5
           type: ClusterIP
           ports:
           - name: http
             protocol: TCP
             port: 8000
             targetPort: 8000

  2. Apply the vLLM TorchTPU server manifest to your cluster:
         
         envsubst '$VLLM_IMAGE' < "qwen3_5_server.yaml" | kubectl apply -f -

  3. Monitor the server deployment logs until application startup completes:
         
         kubectl wait --for=jsonpath='{.status.phase}'=Running pod -l app=vllm-qwen3-5 --timeout=900s
         kubectl logs deployment/vllm-qwen3-5 -c vllm-tpu -f

Initial service startup might take approximately 20 to 30 minutes while the Pod downloads the model weights and compiles the model.

If you're using preemptive capacity like Spot or Flex-start, it might take longer after node pool creation for your TPU slice nodes to be created, and they can be preempted during workload runs. If your Pods are taking longer than expected to start, or your workloads stop in the middle, this could be the cause. For more information, see [Preemption of Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot#preemption). To check if your TPU slice nodes have been created, see [Check the node's status and conditions](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/node-notready#check-node-status-conditions).

Wait until the logs report `Application startup complete` before you send traffic:
         
         (APIServer pid=1) INFO:     Started server process [1]
         (APIServer pid=1) INFO:     Waiting for application startup.
         (APIServer pid=1) INFO:     Application startup complete.
         

  4. Open a second terminal session.

  5. In your second terminal session, forward local port `8000` to `vllm-qwen3-5-service`:
         
         kubectl port-forward service/vllm-qwen3-5-service 8000:8000

Leave port forwarding running in this terminal session.




## Send inference requests

Return to your first terminal session and send a chat completion request to the `/v1/chat/completions` endpoint:
    
    
    curl http://localhost:8000/v1/chat/completions \
        -H "Content-Type: application/json" \
        -d '{
            "model": "Qwen/Qwen3.5-397B-A17B-FP8",
            "messages": [
                {"role": "user", "content": "Hello! Tell me a joke."}
            ],
            "max_tokens": 512,
            "temperature": 0.7
        }' | jq .

## Run a benchmark workload

To benchmark the deployed Qwen3.5 397B model using an 8,192-token input and 1,024-token output (8k/1k) workload with the [InferenceX benchmark suite](https://github.com/SemiAnalysisAI/InferenceX), complete the following steps:

  1. Fetch the benchmark manifest:
         
         curl -O https://raw.githubusercontent.com/GoogleCloudSamples/AIHypercomputerSamples/refs/heads/main/tpu/inference/qwen3-5-397b/qwen3_5-benchmark-8k1k.yaml

Alternately, create a file named `qwen3_5-benchmark-8k1k.yaml` with the following content:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: qwen3-5-bench-8k1k
           namespace: default
         spec:
           restartPolicy: OnFailure
           terminationGracePeriodSeconds: 60
           containers:
           - name: vllm-bench
             image: $VLLM_IMAGE
             command: ["/bin/bash", "-c"]
             args:
             - |
               while ! curl http://vllm-qwen3-5-service:8000/ping; do sleep 30 && echo 'Waiting for server...'; done
               apt-get update && apt-get install -y git && \
               git clone https://github.com/SemiAnalysisAI/InferenceX.git /ubench/inferencex && \
               cd /ubench/inferencex && \
               git checkout 89ce6098ef2bc4576a735c43f39c7d972b091cfc && \
               python3 /ubench/inferencex/utils/bench_serving/benchmark_serving.py \
                 --backend=vllm \
                 --percentile-metrics='ttft,tpot,itl,e2el' \
                 --host=vllm-qwen3-5-service \
                 --port=8000 \
                 --model=Qwen/Qwen3.5-397B-A17B-FP8 \
                 --tokenizer=Qwen/Qwen3.5-397B-A17B-FP8 \
                 --dataset-name=random \
                 --random-input-len=8192 \
                 --random-output-len=1024 \
                 --random-range-ratio=1.0 \
                 --num-prompts=2560 \
                 --num-warmups=512 \
                 --max-concurrency=256 \
                 --ignore-eos
             env:
             - name: HUGGING_FACE_HUB_TOKEN
               valueFrom:
                 secretKeyRef:
                   key: hf_api_token
                   name: hf-secret

  2. Apply the benchmark Pod manifest:
         
         envsubst '$VLLM_IMAGE' < "qwen3_5-benchmark-8k1k.yaml" | kubectl apply -f -

  3. Monitor the benchmark logs:
         
         kubectl logs -f qwen3-5-bench-8k1k

The benchmark takes approximately 25 to 30 minutes to complete.




## Clean up

To avoid incurring additional ongoing charges to your Google Cloud account for the resources used in this tutorial, delete the Kubernetes workloads, the TPU node pool, and the GKE cluster:

  1. Delete the vLLM TorchTPU server Deployment, Service, PersistentVolumeClaim, and benchmark Pod:
         
         kubectl delete -f qwen3_5_server.yaml --ignore-not-found || true
         kubectl delete secret hf-secret --ignore-not-found || true

  2. Delete the TPU7x node pool and the GKE cluster:
         
         gcloud container node-pools delete "${NODE_POOL_NAME}" \
             --cluster="${CLUSTER_NAME}" \
             --location="${REGION}" \
             --project="${PROJECT_ID}" \
             --quiet || true
         
         gcloud container clusters delete "${CLUSTER_NAME}" \
             --location="${REGION}" \
             --project="${PROJECT_ID}" \
             --quiet || true




## What's next

  * Learn more about [vLLM on Cloud TPU](https://github.com/vllm-project/vllm-torchtpu).
  * Learn more about [TPU7x (Ironwood)](https://docs.cloud.google.com/tpu/docs/tpu7x).
  * Learn more about [Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
