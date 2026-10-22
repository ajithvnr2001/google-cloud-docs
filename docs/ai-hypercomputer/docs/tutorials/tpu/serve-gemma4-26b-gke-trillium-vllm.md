---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-gemma4-26b-gke-trillium-vllm/
title: Serve Gemma 4 26B on GKE with multi-host vLLM TorchTPU on Trillium TPUs \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:24.335591+00:00
---

# Serve Gemma 4 26B on GKE with multi-host vLLM TorchTPU on Trillium TPUs  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-gemma4-26b-gke-trillium-vllm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Serve Gemma 4 26B on GKE with multi-host vLLM TorchTPU on Trillium TPUs Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to deploy and serve the multimodal mixture of experts model [Gemma 4 26B (`google/gemma-4-26B-A4B-it`)](https://huggingface.co/google/gemma-4-26B-A4B-it) on Google Kubernetes Engine (GKE) using multi-host [Cloud TPU v6e (Trillium)](https://docs.cloud.google.com/tpu/docs/v6e) accelerators and [vLLM TorchTPU](https://github.com/vllm-project/vllm-torchtpu). Because the workload spans multiple TPU hosts in a `2x4` topology, you use the Kubernetes LeaderWorkerSet API and Ray to coordinate distributed tensor-parallel inference across eight TPU chips.

## Objectives

  * Set up your GKE cluster and multi-host TPU v6e node pool.
  * Deploy the multi-host vLLM server with LeaderWorkerSet.
  * Send text and multimodal inference requests.
  * Run a serving benchmark workload.
  * Clean up.



## Costs

In this document, you use the following billable components of Google Cloud:

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [Cloud TPU](https://docs.cloud.google.com/tpu/pricing)
  * [Compute Engine](https://docs.cloud.google.com/compute/all-pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

**Important:** To complete this tutorial, you must have access to `v6e-8` TPUs. This tutorial assumes that you already have a reservation for these TPUs in your Google Cloud project to ensure that you have the capacity available when you need it. To learn more about your options for reserving Cloud TPU capacity for a future date and time, see [About Cloud TPU reservations](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations).

## Before you begin

You need a Hugging Face access token to use this tutorial. You can sign up for a free account at [Hugging Face](http://huggingface.co/login). After you have an account, generate an access token:

  1. On the [Welcome to Hugging Face](https://huggingface.co/welcome) page, click your account avatar and select **Access tokens**.
  2. On the **Access tokens** page, click **Create new token**.
  3. Select the **Read** token type and enter a name for your token.
  4. Your access token is displayed. Save the token in a safe place.


  * [Install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the Google Cloud CLI, and install [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl). If you use Cloud Shell, both tools are preinstalled.



To get the permissions that you need to complete this tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
  * [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up your environment variables

Set up your environment variables:
    
    
    export PROJECT_ID="YOUR_PROJECT_ID"
    export RESERVATION_NAME="YOUR_RESERVATION_NAME"
    export REGION="YOUR_REGION"
    export ZONE="YOUR_ZONE"
    export CLUSTER_NAME="YOUR_CLUSTER_NAME"
    export HF_TOKEN="YOUR_HF_TOKEN"
    export NODE_POOL_NAME="tpuv6e-pool"
    export VLLM_IMAGE="vllm/vllm-torchtpu:v0.29.0"
    
    gcloud config set project "${PROJECT_ID}"
    gcloud config set billing/quota_project "${PROJECT_ID}"

Replace the following:

  * `YOUR_PROJECT_ID`: the ID of your Google Cloud project.
  * `YOUR_RESERVATION_NAME`: the name of your reservation.
  * `YOUR_REGION`: the region where you want to deploy your GKE cluster.
  * `YOUR_ZONE`: the zone where you want to deploy your TPU v6e node pool.
  * `YOUR_CLUSTER_NAME`: the name of your GKE cluster.
  * `YOUR_HF_TOKEN`: your Hugging Face access token.
  * `YOUR_VLLM_TPU_IMAGE`: the vLLM TPU image to use. For public images, refer to the [vLLM TorchTPU](https://github.com/vllm-project/vllm-torchtpu) repository.



## Create the GKE cluster

To create the GKE cluster and attach a multi-host TPU v6e node pool, complete the following steps:

  1. Create a regional GKE cluster that uses `e2-standard-4` nodes for the default node pool, and a TPU v6e node pool with two `ct6e-standard-4t` nodes arranged in a `2x4` topology (eight TPU chips total). The default GKE machine type (`e2-medium`) doesn't provide enough CPU resources for the LeaderWorkerSet controller, so this tutorial specifies `e2-standard-4`:
         
         gcloud container clusters create "${CLUSTER_NAME}" \
             --project="${PROJECT_ID}" \
             --location="${REGION}" \
             --machine-type=e2-standard-4 \
         
         gcloud container node-pools create "${NODE_POOL_NAME}" \
             --project="${PROJECT_ID}" \
             --location="${REGION}" \
             --cluster="${CLUSTER_NAME}" \
             --node-locations="${ZONE}" \
             --machine-type=ct6e-standard-4t \
             --tpu-topology=2x4 \
             --num-nodes=2 \
             --disk-size=500 \
             --reservation-affinity=specific \
             --reservation="${RESERVATION_NAME}"

Instead of using a specific reservation, you can also create the node pool using Spot capacity or Flex-start VMs by passing the following flags:

     * **Spot VMs** : replace the `--reservation-affinity` and `--reservation` flags with `--spot` to use Spot capacity. Instances that use Spot capacity might take time to be created after the node pool is created, and they might be preempted during workload runs. If your Pods take time to be created, or workloads stop in the middle of running, this could be the cause.
     * **Flex-start VMs** : Pass `--flex-start` to provision the node pool using the [Flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws) consumption option. For more information, see [Run a small batch workload with TPUs and Flex-start VMs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dws-flex-start-training-tpu).
  2. Configure `kubectl` credentials to communicate with your cluster:
         
         gcloud container clusters get-credentials "${CLUSTER_NAME}" \
             --project="${PROJECT_ID}" \
             --location="${REGION}"




## Configure credentials and install LeaderWorkerSet

To prepare your cluster for the multi-host deployment, complete the following steps:

  1. Export your Hugging Face token and create a Kubernetes Secret named `hf-secret`:
         
         kubectl create secret generic hf-secret \
             --from-literal=hf_api_token="${HF_TOKEN}" \
             --dry-run=client -o yaml | kubectl apply -f -

  2. Install the LeaderWorkerSet CustomResourceDefinition and controller on your cluster:
         
         kubectl apply --server-side -k "github.com/kubernetes-sigs/lws/config/default?ref=main"
         echo "Waiting for LWS controller to be ready..."
         kubectl wait --for=condition=Available --timeout=300s deployment/lws-controller-manager -n lws-system




## Deploy the multi-host vLLM server

The workload manifest (`gemma4-26b-multihost-v6e-2x4.yaml`) defines two resources:

  * A LeaderWorkerSet resource (`vllm-tpu-gemma4-26b`) with `size: 2` (one leader Pod and one worker Pod) scheduled across the two `ct6e-standard-4t` nodes in the `2x4` TPU slice. Each Pod runs an InitContainer that prefetches the `google/gemma-4-26B-A4B-it` model weights from Hugging Face into an in-memory volume before starting Ray and the vLLM OpenAI API server with the `--tensor-parallel-size=8`, `--kv-cache-dtype=fp8`, `--max-model-len=5248`, and `--max-num-seqs=128` flags.
  * A ClusterIP Service (`vllm-service`) that exposes port `8000` on the leader Pod.



To deploy and monitor the workload, complete the following steps:

  1. Fetch the LeaderWorkerSet manifest from GitHub:
         
         curl -LO https://raw.githubusercontent.com/GoogleCloudSamples/AIHypercomputerSamples/main/tpu/inference/gemma-4-26b/gemma4-26b-multihost-v6e-2x4.yaml

Alternatively, create a file named `gemma4-26b-multihost-v6e-2x4.yaml` with the following contents:
         
         apiVersion: leaderworkerset.x-k8s.io/v1
         kind: LeaderWorkerSet
         metadata:
           name: vllm-tpu-gemma4-26b
         spec:
           replicas: 1
           leaderWorkerTemplate:
             # One pod per TPU host: a 2x4 v6e slice has 2 ct6e-standard-4t hosts.
             size: 2
             restartPolicy: RecreateGroupOnPodRestart
             leaderTemplate:
               metadata:
                 labels:
                   role: leader
               spec:
                 # Download the model into the pod-local cache before vLLM starts, so the
                 # serving ranks can run offline and never hit Hugging Face during init.
                 initContainers:
                 - name: prefetch-model
                   image: $VLLM_IMAGE
                   command: ["hf", "download", "google/gemma-4-26B-A4B-it"]
                   env:
                   - name: HF_TOKEN
                     valueFrom:
                       secretKeyRef:
                         name: hf-secret
                         key: hf_api_token
                   - name: HF_HOME
                     value: "/data/huggingface_cache"
                   volumeMounts:
                   - name: model-cache
                     mountPath: /data
                 containers:
                 - name: vllm-leader
                   image: $VLLM_IMAGE
                   command:
                     - sh
                     - -c
                     - |
                       set -e
                       mkdir -p "${TMPDIR}"
                       ray start --head --port=6379
                       echo "Waiting for all 8 TPU chips to join the Ray cluster..."
                       until ray status 2>/dev/null | grep -E -q "8(\.0)? TPU"; do
                         sleep 5
                       done
                       vllm serve google/gemma-4-26B-A4B-it \
                         --tensor-parallel-size 8 \
                         --distributed-executor-backend ray \
                         --host 0.0.0.0 \
                         --port 8000 \
                         --max-model-len 5248 \
                         --max-num-seqs 128 \
                         --max-num-batched-tokens 4096 \
                         --kv-cache-dtype fp8 \
                         --gpu-memory-utilization 0.85 \
                         --disable-chunked-mm-input
                   resources:
                     requests:
                       cpu: "128"
                       memory: "384Gi"
                       google.com/tpu: 4
                     limits:
                       cpu: "170"
                       memory: "650Gi"
                       google.com/tpu: 4
                   ports:
                   - containerPort: 8000
                   - containerPort: 6379
                   env:
                   - name: TPU_MULTIHOST_BACKEND
                     value: "ray"
                   - name: VLLM_ENGINE_READY_TIMEOUT_S
                     value: "3600"
                   # Same cache the init container populated; offline mode guarantees no
                   # Hugging Face requests from the serving ranks.
                   - name: HF_HOME
                     value: "/data/huggingface_cache"
                   - name: HF_HUB_OFFLINE
                     value: "1"
                   - name: TMPDIR
                     value: "/data/tmp"
                   volumeMounts:
                   - mountPath: /dev/shm
                     name: dshm
                   - mountPath: /data
                     name: model-cache
                   # Model loading and compilation can take a long time; allow up to 60 minutes.
                   startupProbe:
                     httpGet:
                       path: /health
                       port: 8000
                     periodSeconds: 10
                     failureThreshold: 360
                   livenessProbe:
                     httpGet:
                       path: /health
                       port: 8000
                     periodSeconds: 10
                   readinessProbe:
                     httpGet:
                       path: /health
                       port: 8000
                     periodSeconds: 5
                 nodeSelector:
                   topology.kubernetes.io/zone: "$ZONE"
                   cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                   cloud.google.com/gke-tpu-topology: 2x4
                   cloud.google.com/reservation-name: $RESERVATION_NAME
                 volumes:
                 - name: dshm
                   emptyDir:
                     medium: Memory
                     sizeLimit: 32Gi
                 - name: model-cache
                   emptyDir:
                     medium: Memory
                     sizeLimit: 350Gi
             workerTemplate:
               spec:
                 # Each pod has its own cache, so the worker downloads the model too.
                 initContainers:
                 - name: prefetch-model
                   image: $VLLM_IMAGE
                   command: ["hf", "download", "google/gemma-4-26B-A4B-it"]
                   env:
                   - name: HF_TOKEN
                     valueFrom:
                       secretKeyRef:
                         name: hf-secret
                         key: hf_api_token
                   - name: HF_HOME
                     value: "/data/huggingface_cache"
                   volumeMounts:
                   - name: model-cache
                     mountPath: /data
                 containers:
                 - name: vllm-worker
                   image: $VLLM_IMAGE
                   command:
                     - sh
                     - -c
                     - |
                       set -e
                       mkdir -p "${TMPDIR}"
                       echo "Waiting for the Ray head at ${LWS_LEADER_ADDRESS}:6379..."
                       until ray status --address="${LWS_LEADER_ADDRESS}:6379" 2>/dev/null | grep -q "node_"; do
                         sleep 3
                       done
                       ray start --address="${LWS_LEADER_ADDRESS}:6379" --block
                   resources:
                     requests:
                       cpu: "128"
                       memory: "384Gi"
                       google.com/tpu: 4
                     limits:
                       cpu: "170"
                       memory: "650Gi"
                       google.com/tpu: 4
                   env:
                   - name: TPU_MULTIHOST_BACKEND
                     value: "ray"
                   - name: VLLM_ENGINE_READY_TIMEOUT_S
                     value: "3600"
                   - name: HF_HOME
                     value: "/data/huggingface_cache"
                   - name: HF_HUB_OFFLINE
                     value: "1"
                   - name: TMPDIR
                     value: "/data/tmp"
                   volumeMounts:
                   - mountPath: /dev/shm
                     name: dshm
                   - mountPath: /data
                     name: model-cache
                 nodeSelector:
                   topology.kubernetes.io/zone: "$ZONE"
                   cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                   cloud.google.com/gke-tpu-topology: 2x4
                   cloud.google.com/reservation-name: $RESERVATION_NAME
                 volumes:
                 - name: dshm
                   emptyDir:
                     medium: Memory
                     sizeLimit: 32Gi
                 - name: model-cache
                   emptyDir:
                     medium: Memory
                     sizeLimit: 350Gi
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: vllm-service
         spec:
           selector:
             leaderworkerset.sigs.k8s.io/name: vllm-tpu-gemma4-26b
             role: leader
           type: ClusterIP
           ports:
             - protocol: TCP
               port: 8000
               targetPort: 8000

  2. Apply the LeaderWorkerSet manifest:
         
         MANIFEST="gemma4-26b-multihost-v6e-2x4.yaml"
         echo "Applying LeaderWorkerSet (retrying if webhook is not fully ready)..."
         MAX_ATTEMPTS=12
         attempt=1
         until envsubst '$RESERVATION_NAME $ZONE $VLLM_IMAGE' < "${MANIFEST}" | kubectl apply -f -; do
           if [ "${attempt}" -ge "${MAX_ATTEMPTS}" ]; then
             echo "Error: failed to apply ${MANIFEST} after ${MAX_ATTEMPTS} attempts." >&2
             exit 1
           fi
           echo "Webhook not ready yet, retrying in 5 seconds (attempt ${attempt}/${MAX_ATTEMPTS})..."
           attempt=$((attempt + 1))
           sleep 5
         done

  3. Monitor the leader Pod status and logs until application startup completes:
         
         LIMIT=60
         count=0
         until kubectl get pod -l role=leader -o name | grep -q "vllm-tpu"; do
           if [ "${count}" -ge "${LIMIT}" ]; then
             echo "Error: timeout waiting for leader pod to be created." >&2
             exit 1
           fi
           echo "Waiting for leader pod to be created..."
           sleep 5
           count=$((count + 1))
         done
         
         # Wait up to 20 minutes for the pod to start running (TPU nodes take a while to boot)
         echo "Waiting for pod to be scheduled and running..."
         if ! kubectl wait --for=jsonpath='{.status.phase}'=Running --timeout=1200s pod -l role=leader; then
           echo "Pod failed to start running within 20 minutes! Here are the events:" >&2
           kubectl describe pod -l role=leader
           exit 1
         fi
         
         echo "Pod is running. Streaming logs while waiting for it to become Ready (this includes model download)..."
         # Stream logs in the background so the user can see what's happening
         kubectl logs -f -l role=leader &
         LOG_PID=$!
         trap 'kill "${LOG_PID}" 2>/dev/null || true' EXIT
         
         if ! kubectl wait --for=condition=Ready --timeout=3600s pod -l role=leader; then
           echo "Pod failed to become Ready within 60 minutes!" >&2
           kubectl describe pod -l role=leader
           exit 1
         fi
         
         echo "Pod is Ready!"

Initial service startup takes approximately 9 minutes while the Pods prefetch the model weights, form the two-node Ray cluster across all eight TPU chips, and compile the model. Wait until the logs report `Application startup complete` before sending traffic.

  4. In a second terminal session, forward local port `8000` to `vllm-service`:
         
         kubectl port-forward service/vllm-service 8000:8000

Leave port forwarding running in this terminal session.




## Send inference requests

Return to your first terminal session and test the deployed model with both text and multimodal chat completion requests:

  1. Send a text chat completion request to the `/v1/chat/completions` endpoint:
         
         curl http://localhost:8000/v1/chat/completions \
             -H "Content-Type: application/json" \
             -d '{
                 "model": "google/gemma-4-26B-A4B-it",
                 "messages": [{"role": "user", "content": "Explain Mixture of Experts in 2 sentences."}],
                 "max_tokens": 128
             }'

  2. Send a multimodal request containing both an image URL and a text prompt:
         
         curl http://localhost:8000/v1/chat/completions \
             -H "Content-Type: application/json" \
             -d '{
                 "model": "google/gemma-4-26B-A4B-it",
                 "messages": [
                     {
                         "role": "user",
                         "content": [
                             {
                                 "type": "image_url",
                                 "image_url": {
                                     "url": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?auto=format&fit=crop&w=800&q=80"
                                 }
                             },
                             {
                                 "type": "text",
                                 "text": "Describe the image above"
                             }
                         ]
                     }
                 ],
                 "max_tokens": 300,
                 "temperature": 0.0,
                 "top_p": 1.0
             }'




## Run a benchmark workload

To benchmark the deployed model, run the following command:
    
    
    kubectl exec vllm-tpu-gemma4-26b-0 -- vllm bench serve \
      --backend openai-chat \
      --endpoint /v1/chat/completions \
      --model google/gemma-4-26B-A4B-it \
      --host localhost \
      --port 8000 \
      --dataset-name random \
      --num-prompts 250 \
      --random-input-len 1024 \
      --random-output-len 1024 \
      --max-concurrency 128

## Clean up

To avoid incurring additional ongoing charges to your Google Cloud account for the resources used in this tutorial, delete the Kubernetes workloads, the TPU node pool, and the GKE cluster:

  1. Delete the vLLM server deployment and the Hugging Face secret:
         
         envsubst '$RESERVATION_NAME $ZONE $VLLM_IMAGE' < gemma4-26b-multihost-v6e-2x4.yaml | kubectl delete -f - --ignore-not-found || true
         kubectl delete secret hf-secret --ignore-not-found || true

  2. Delete the TPU v6e node pool and the GKE cluster:
         
         gcloud container node-pools delete "${NODE_POOL_NAME}" \
             --cluster="${CLUSTER_NAME}" \
             --location="${REGION}" \
             --project="${PROJECT_ID}" \
             --quiet || true
         
         gcloud container clusters delete "${CLUSTER_NAME}" \
             --location="${REGION}" \
             --project="${PROJECT_ID}" \
             --quiet

  3. Return to your second terminal session and stop port forwarding.




## What's next

  * Learn more about [vLLM TorchTPU](https://github.com/vllm-project/vllm-torchtpu).
  * Learn more about [Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
