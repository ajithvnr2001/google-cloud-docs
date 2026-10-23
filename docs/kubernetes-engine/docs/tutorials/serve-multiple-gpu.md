---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-multiple-gpu/
title: Serve an LLM with multiple GPUs in GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:21.402518+00:00
---

# Serve an LLM with multiple GPUs in GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-multiple-gpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Serve an LLM with multiple GPUs in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial demonstrates how to deploy and serve a large language model (LLM) using multiple GPUs on GKE for efficient and scalable inference. You create a GKE cluster that uses multiple L4 GPUs and you prepare infrastructure to serve any of the following models:

  * [Llama 3 70b](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct)
  * [Mixtral 8x7b](https://mistral.ai/news/mixtral-of-experts/)
  * [Falcon 40b](https://falconllm.tii.ae/falcon-40b.html)



Depending on the data format of the model, the required number of GPUs varies. In this tutorial, each model uses two L4 GPUs. To learn more, see Calculating the amount of GPUs.

This tutorial is intended for Machine learning (ML) engineers, Platform admins and operators, and for Data and AI specialists who are interested in using Kubernetes container orchestration capabilities for serving LLMs. To learn more about common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/anthos/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with the following:

  * [Autopilot mode and Standard mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)
  * [Current GPU version availability](https://docs.cloud.google.com/compute/docs/gpus)
  * [GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus)



## Objectives

In this tutorial, you:

  1. Create a cluster and node pools.
  2. Prepare your workload.
  3. Deploy your workload.
  4. Interact with the LLM interface.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Some models have additional requirements. Ensure you meet these requirements:

    * To access models from Hugging Face, use a [HuggingFace token](https://huggingface.co/docs/hub/security-tokens).
    * For the Mixtral 8x7b model - accept the conditions for the [Mistral Mixtral model](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1).
    * For the Llama 3 70b model - make sure you have an active license for the [Meta Llama models](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct).
**Warning:** Getting access and approval for the Llama model might take up to three days.



## Prepare your environment

  1. In the Google Cloud console, start a Cloud Shell instance:   
[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Set the default environment variables:
         
         gcloud config set project PROJECT_ID
         gcloud config set billing/quota_project PROJECT_ID
         export PROJECT_ID=$(gcloud config get project)
         export CONTROL_PLANE_LOCATION=us-central1
         

Replace the PROJECT_ID with your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

**Note:** If your Cloud Shell instance disconnects throughout the tutorial execution, repeat the preceding step.



### Create a GKE cluster and node pool

You can serve LLMs on GPUs in a GKE Autopilot or Standard cluster. We recommend that you use a Autopilot cluster for a fully managed Kubernetes experience. To choose the GKE mode of operation that's the best fit for your workloads, see [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

### Autopilot

  1. In Cloud Shell, run the following command:
         
         gcloud container clusters create-auto l4-demo \
           --project=${PROJECT_ID} \
           --location=${CONTROL_PLANE_LOCATION} \
           --release-channel=rapid
         

GKE creates an Autopilot cluster with CPU and GPU nodes as requested by the deployed workloads.

  2. Configure `kubectl` to communicate with your cluster:
         
         gcloud container clusters get-credentials l4-demo --location=${CONTROL_PLANE_LOCATION}
         




### Standard

  1. In Cloud Shell, run the following command to create a Standard cluster that uses [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity):
         
         gcloud container clusters create l4-demo \
           --location ${CONTROL_PLANE_LOCATION} \
           --workload-pool ${PROJECT_ID}.svc.id.goog \
           --enable-image-streaming \
           --node-locations=${CONTROL_PLANE_LOCATION}-a \
           --workload-pool=${PROJECT_ID}.svc.id.goog \
           --machine-type n2d-standard-4 \
           --num-nodes 1 --min-nodes 1 --max-nodes 5 \
           --release-channel=rapid
         

**Note:** The `--node-locations` flag might have to be adjusted based on which region you choose. Check which [zones the L4 GPUs](https://docs.cloud.google.com/compute/docs/gpus#nvidia_l4_vws_gpus) are available if you change the `us-central1` region.

The cluster creation might take several minutes.

  2. Run the following command to create a [node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) for your cluster:
         
         gcloud container node-pools create g2-standard-24 --cluster l4-demo \
           --location ${CONTROL_PLANE_LOCATION} \
           --accelerator type=nvidia-l4,count=2,gpu-driver-version=latest \
           --machine-type g2-standard-24 \
           --enable-autoscaling --enable-image-streaming \
           --num-nodes=0 --min-nodes=0 --max-nodes=3 \
           --node-locations ${CONTROL_PLANE_LOCATION}-a,${CONTROL_PLANE_LOCATION}-c \
           --spot
         

GKE creates the following resources for the LLM:

     * A public Standard cluster.
     * A node pool with `g2-standard-24` machine type scaled down to 0 nodes. You aren't charged for any GPUs until you launch Pods that request GPUs. This node pool provisions [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/spot-vms), which are priced lower than the default standard Compute Engine VMs and provide no guarantee of availability. You can remove the `--spot` flag from this command, and the `cloud.google.com/gke-spot` node selector in the `text-generation-inference.yaml` config to use on-demand VMs.
  3. Configure `kubectl` to communicate with your cluster:
         
         gcloud container clusters get-credentials l4-demo --location=${CONTROL_PLANE_LOCATION}
         




## Prepare your workload

This section shows how to set up your workload depending on the model you want to use. This tutorial uses Kubernetes Deployments to deploy the model. A _Deployment_ is a Kubernetes API object that lets you run multiple replicas of Pods that are distributed among the nodes in a cluster..

### Llama 3 70b

  1. Set the default environment variables:
         
         export HF_TOKEN=HUGGING_FACE_TOKEN
         

Replace the `HUGGING_FACE_TOKEN` with your HuggingFace token.

  2. Create a [Kubernetes secret](https://kubernetes.io/docs/concepts/configuration/secret/) for the HuggingFace token:
         
         kubectl create secret generic l4-demo \
             --from-literal=HUGGING_FACE_TOKEN=${HF_TOKEN} \
             --dry-run=client -o yaml | kubectl apply -f -
         

  3. Create the following `text-generation-inference.yaml` Deployment manifest:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: llm
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: llm
           template:
             metadata:
               labels:
                 app: llm
             spec:
               containers:
               - name: llm
                 image: us-docker.pkg.dev/deeplearning-platform-release/gcr.io/huggingface-text-generation-inference-cu121.2-1.ubuntu2204.py310
                 resources:
                   requests:
                     cpu: "10"
                     memory: "60Gi"
                     nvidia.com/gpu: "2"
                   limits:
                     cpu: "10"
                     memory: "60Gi"
                     nvidia.com/gpu: "2"
                 env:
                 - name: MODEL_ID
                   value: meta-llama/Meta-Llama-3-70B-Instruct
                 - name: NUM_SHARD
                   value: "2"
                 - name: MAX_INPUT_TOKENS
                   value: "2048"
                 - name: PORT
                   value: "8080"
                 - name: QUANTIZE
                   value: bitsandbytes-nf4
                 - name: HUGGING_FACE_HUB_TOKEN
                   valueFrom:
                     secretKeyRef:
                       name: l4-demo
                       key: HUGGING_FACE_TOKEN
                 volumeMounts:
                   - mountPath: /dev/shm
                     name: dshm
                   # mountPath is set to /tmp as it's the path where the HUGGINGFACE_HUB_CACHE environment
                   # variable in the TGI DLCs is set to instead of the default /data set within the TGI default image.
                   # i.e. where the downloaded model from the Hub will be stored
                   - mountPath: /tmp
                     name: ephemeral-volume
               volumes:
                 - name: dshm
                   emptyDir:
                       medium: Memory
                 - name: ephemeral-volume
                   ephemeral:
                     volumeClaimTemplate:
                       metadata:
                         labels:
                           type: ephemeral
                       spec:
                         accessModes: ["ReadWriteOnce"]
                         storageClassName: "premium-rwo"
                         resources:
                           requests:
                             storage: 150Gi
               nodeSelector:
                 cloud.google.com/gke-accelerator: "nvidia-l4"
                 cloud.google.com/gke-spot: "true"

In this manifest:

     * `NUM_SHARD` must be `2` because the model requires two NVIDIA L4 GPUs.
     * `QUANTIZE` is set to `bitsandbytes-nf4` which means that the model is loaded in 4 bit instead of 32 bits. This allows GKE to reduce the amount of GPU memory needed and improves the inference speed. However, the model accuracy can decrease. To learn how to calculate the GPUs to request, see Calculating the amount of GPUs.
  4. Apply the manifest:
         
         kubectl apply -f text-generation-inference.yaml
         

The output is similar to the following:
         
         deployment.apps/llm created
         

  5. Verify the status of the model:
         
         kubectl get deploy
         

The output is similar to the following:
         
         NAME          READY   UP-TO-DATE   AVAILABLE   AGE
         llm           1/1     1            1           20m
         

  6. View the logs from the running deployment:
         
         kubectl logs -l app=llm
         

The output is similar to the following:
         
         {"timestamp":"2024-03-09T05:08:14.751646Z","level":"INFO","message":"Warming up model","target":"text_generation_router","filename":"router/src/main.rs","line_number":291}
         {"timestamp":"2024-03-09T05:08:19.961136Z","level":"INFO","message":"Setting max batch total tokens to 133696","target":"text_generation_router","filename":"router/src/main.rs","line_number":328}
         {"timestamp":"2024-03-09T05:08:19.961164Z","level":"INFO","message":"Connected","target":"text_generation_router","filename":"router/src/main.rs","line_number":329}
         {"timestamp":"2024-03-09T05:08:19.961171Z","level":"WARN","message":"Invalid hostname, defaulting to 0.0.0.0","target":"text_generation_router","filename":"router/src/main.rs","line_number":343}
         




### Mixtral 8x7b

  1. Set the default environment variables:
         
         export HF_TOKEN=HUGGING_FACE_TOKEN
         

Replace the `HUGGING_FACE_TOKEN` with your HuggingFace token.

  2. Create a [Kubernetes secret](https://kubernetes.io/docs/concepts/configuration/secret/) for the HuggingFace token:
         
         kubectl create secret generic l4-demo \
             --from-literal=HUGGING_FACE_TOKEN=${HF_TOKEN} \
             --dry-run=client -o yaml | kubectl apply -f -
         

  3. Create the following `text-generation-inference.yaml` Deployment manifest:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: llm
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: llm
           template:
             metadata:
               labels:
                 app: llm
             spec:
               containers:
               - name: llm
                 image: us-docker.pkg.dev/deeplearning-platform-release/gcr.io/huggingface-text-generation-inference-cu124.2-3.ubuntu2204.py311
                 resources:
                   requests:
                     cpu: "5"
                     memory: "40Gi"
                     nvidia.com/gpu: "2"
                   limits:
                     cpu: "5"
                     memory: "40Gi"
                     nvidia.com/gpu: "2"
                 env:
                 - name: MODEL_ID
                   value: mistralai/Mixtral-8x7B-Instruct-v0.1
                 - name: NUM_SHARD
                   value: "2"
                 - name: PORT
                   value: "8080"
                 - name: QUANTIZE
                   value: bitsandbytes-nf4
                 - name: HUGGING_FACE_HUB_TOKEN
                   valueFrom:
                     secretKeyRef:
                       name: l4-demo
                       key: HUGGING_FACE_TOKEN          
                 volumeMounts:
                   - mountPath: /dev/shm
                     name: dshm
                   # mountPath is set to /tmp as it's the path where the HF_HOME environment
                   # variable in the TGI DLCs is set to instead of the default /data set within the TGI default image.
                   # i.e. where the downloaded model from the Hub will be stored
                   - mountPath: /tmp
                     name: ephemeral-volume
               volumes:
                 - name: dshm
                   emptyDir:
                       medium: Memory
                 - name: ephemeral-volume
                   ephemeral:
                     volumeClaimTemplate:
                       metadata:
                         labels:
                           type: ephemeral
                       spec:
                         accessModes: ["ReadWriteOnce"]
                         storageClassName: "premium-rwo"
                         resources:
                           requests:
                             storage: 100Gi
               nodeSelector:
                 cloud.google.com/gke-accelerator: "nvidia-l4"
                 cloud.google.com/gke-spot: "true"

In this manifest:

     * `NUM_SHARD` must be `2` because the model requires two NVIDIA L4 GPUs.
     * `QUANTIZE` is set to `bitsandbytes-nf4` which means that the model is loaded in 4 bit instead of 32 bits. This allows GKE to reduce the amount of GPU memory needed and improves the inference speed. However, this may reduce model accuracy. To learn how to calculate the GPUs to request, see Calculating the amount of GPUs.
  4. Apply the manifest:
         
         kubectl apply -f text-generation-inference.yaml
         

The output is similar to the following:
         
         deployment.apps/llm created
         

  5. Verify the status of the model:
         
         watch kubectl get deploy
         

When the Deployment is ready, the output is similar to the following:
         
         NAME          READY   UP-TO-DATE   AVAILABLE   AGE
         llm           1/1     1            1           10m
         

To exit the watch, type `CTRL + C`.

  6. View the logs from the running deployment:
         
         kubectl logs -l app=llm
         

The output is similar to the following:
         
         {"timestamp":"2024-03-09T05:08:14.751646Z","level":"INFO","message":"Warming up model","target":"text_generation_router","filename":"router/src/main.rs","line_number":291}
         {"timestamp":"2024-03-09T05:08:19.961136Z","level":"INFO","message":"Setting max batch total tokens to 133696","target":"text_generation_router","filename":"router/src/main.rs","line_number":328}
         {"timestamp":"2024-03-09T05:08:19.961164Z","level":"INFO","message":"Connected","target":"text_generation_router","filename":"router/src/main.rs","line_number":329}
         {"timestamp":"2024-03-09T05:08:19.961171Z","level":"WARN","message":"Invalid hostname, defaulting to 0.0.0.0","target":"text_generation_router","filename":"router/src/main.rs","line_number":343}
         




### Falcon 40b

  1. Create the following `text-generation-inference.yaml` Deployment manifest:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: llm
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: llm
           template:
             metadata:
               labels:
                 app: llm
             spec:
               containers:
               - name: llm
                 image: us-docker.pkg.dev/deeplearning-platform-release/gcr.io/huggingface-text-generation-inference-cu121.1-4.ubuntu2204.py310
                 resources:
                   requests:
                     cpu: "10"
                     memory: "60Gi"
                     nvidia.com/gpu: "2"
                   limits:
                     cpu: "10"
                     memory: "60Gi"
                     nvidia.com/gpu: "2"
                 env:
                 - name: MODEL_ID
                   value: tiiuae/falcon-40b-instruct
                 - name: NUM_SHARD
                   value: "2"
                 - name: PORT
                   value: "8080"
                 - name: QUANTIZE
                   value: bitsandbytes-nf4
                 volumeMounts:
                   - mountPath: /dev/shm
                     name: dshm
                   # mountPath is set to /data as it's the path where the HUGGINGFACE_HUB_CACHE environment
                   # variable points to in the TGI container image i.e. where the downloaded model from the Hub will be
                   # stored
                   - mountPath: /data
                     name: ephemeral-volume
               volumes:
                 - name: dshm
                   emptyDir:
                       medium: Memory
                 - name: ephemeral-volume
                   ephemeral:
                     volumeClaimTemplate:
                       metadata:
                         labels:
                           type: ephemeral
                       spec:
                         accessModes: ["ReadWriteOnce"]
                         storageClassName: "premium-rwo"
                         resources:
                           requests:
                             storage: 175Gi
               nodeSelector:
                 cloud.google.com/gke-accelerator: "nvidia-l4"
                 cloud.google.com/gke-spot: "true"

In this manifest:

     * `NUM_SHARD` must be `2` because the model requires two NVIDIA L4 GPUs.
     * `QUANTIZE` is set to `bitsandbytes-nf4` which means that the model is loaded in 4 bit instead of 32 bits. This allows GKE to reduce the amount of GPU memory needed and improves the inference speed. However, the model accuracy can decrease. To learn how to calculate the GPUs to request, see Calculating the amount of GPUs.
  2. Apply the manifest:
         
         kubectl apply -f text-generation-inference.yaml
         

The output is similar to the following:
         
         deployment.apps/llm created
         

  3. Verify the status of the model:
         
         watch kubectl get deploy
         

When the deployment is ready, the output is similar to the following:
         
         NAME          READY   UP-TO-DATE   AVAILABLE   AGE
         llm           1/1     1            1           10m
         

To exit the watch, type `CTRL + C`.

  4. View the logs from the running deployment:
         
         kubectl logs -l app=llm
         

The output is similar to the following:
         
         {"timestamp":"2024-03-09T05:08:14.751646Z","level":"INFO","message":"Warming up model","target":"text_generation_router","filename":"router/src/main.rs","line_number":291}
         {"timestamp":"2024-03-09T05:08:19.961136Z","level":"INFO","message":"Setting max batch total tokens to 133696","target":"text_generation_router","filename":"router/src/main.rs","line_number":328}
         {"timestamp":"2024-03-09T05:08:19.961164Z","level":"INFO","message":"Connected","target":"text_generation_router","filename":"router/src/main.rs","line_number":329}
         {"timestamp":"2024-03-09T05:08:19.961171Z","level":"WARN","message":"Invalid hostname, defaulting to 0.0.0.0","target":"text_generation_router","filename":"router/src/main.rs","line_number":343}
         




### Create a Service of type ClusterIP

Expose your Pods internally within the cluster so they can be discovered and accessed by other applications.

  1. Create the following `llm-service.yaml` manifest:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: llm-service
         spec:
           selector:
             app: llm
           type: ClusterIP
           ports:
             - protocol: TCP
               port: 80
               targetPort: 8080
         

  2. Apply the manifest:
         
         kubectl apply -f llm-service.yaml
         




## Deploy a chat interface

Use [Gradio](https://www.gradio.app/docs/interface) to build a web application that lets you interact with your model. Gradio is a Python library that has a ChatInterface wrapper that creates user interfaces for chatbots.

### Llama 3 70b

  1. Create a file named `gradio.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: gradio
           labels:
             app: gradio
         spec:
           strategy:
             type: Recreate
           replicas: 1
           selector:
             matchLabels:
               app: gradio
           template:
             metadata:
               labels:
                 app: gradio
             spec:
               containers:
               - name: gradio
                 image: us-docker.pkg.dev/google-samples/containers/gke/gradio-app:v1.0.4
                 resources:
                   requests:
                     cpu: "512m"
                     memory: "512Mi"
                   limits:
                     cpu: "1"
                     memory: "512Mi"
                 env:
                 - name: CONTEXT_PATH
                   value: "/generate"
                 - name: HOST
                   value: "http://llm-service"
                 - name: LLM_ENGINE
                   value: "tgi"
                 - name: MODEL_ID
                   value: "meta-llama/Meta-Llama-3-70B-Instruct"
                 - name: USER_PROMPT
                   value: "<|begin_of_text|><|start_header_id|>user<|end_header_id|> prompt <|eot_id|><|start_header_id|>assistant<|end_header_id|>"
                 - name: SYSTEM_PROMPT
                   value: "prompt <|eot_id|>"
                 ports:
                 - containerPort: 7860
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: gradio-service
         spec:
           type: LoadBalancer
           selector:
             app: gradio
           ports:
           - port: 80
             targetPort: 7860
         

  2. Apply the manifest:
         
         kubectl apply -f gradio.yaml
         

  3. Find the external IP address of the Service:
         
         kubectl get svc
         

The output is similar to the following:
         
         NAME             TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)        AGE
         gradio-service   LoadBalancer   10.24.29.197   34.172.115.35   80:30952/TCP   125m
         

  4. Copy the external IP address from the `EXTERNAL-IP` column.

  5. View the model interface from your web browser by using the external IP address with the exposed port:
         
         http://EXTERNAL_IP
         




### Mixtral 8x7b

  1. Create a file named `gradio.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: gradio
           labels:
             app: gradio
         spec:
           strategy:
             type: Recreate
           replicas: 1
           selector:
             matchLabels:
               app: gradio
           template:
             metadata:
               labels:
                 app: gradio
             spec:
               containers:
               - name: gradio
                 image: us-docker.pkg.dev/google-samples/containers/gke/gradio-app:v1.0.4
                 resources:
                   requests:
                     cpu: "512m"
                     memory: "512Mi"
                   limits:
                     cpu: "1"
                     memory: "512Mi"
                 env:
                 - name: CONTEXT_PATH
                   value: "/generate"
                 - name: HOST
                   value: "http://llm-service"
                 - name: LLM_ENGINE
                   value: "tgi"
                 - name: MODEL_ID
                   value: "mixtral-8x7b"
                 - name: USER_PROMPT
                   value: "[INST] prompt [/INST]"
                 - name: SYSTEM_PROMPT
                   value: "prompt"
                 ports:
                 - containerPort: 7860
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: gradio-service
         spec:
           type: LoadBalancer
           selector:
             app: gradio
           ports:
           - port: 80
             targetPort: 7860
         

  2. Apply the manifest:
         
         kubectl apply -f gradio.yaml
         

  3. Find the external IP address of the Service:
         
         kubectl get svc
         

The output is similar to the following:
         
         NAME             TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)        AGE
         gradio-service   LoadBalancer   10.24.29.197   34.172.115.35   80:30952/TCP   125m
         

  4. Copy the external IP address from the `EXTERNAL-IP` column.

  5. View the model interface from your web browser by using the external IP address with the exposed port:
         
         http://EXTERNAL_IP
         




### Falcon 40b

  1. Create a file named `gradio.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: gradio
           labels:
             app: gradio
         spec:
           strategy:
             type: Recreate
           replicas: 1
           selector:
             matchLabels:
               app: gradio
           template:
             metadata:
               labels:
                 app: gradio
             spec:
               containers:
               - name: gradio
                 image: us-docker.pkg.dev/google-samples/containers/gke/gradio-app:v1.0.4
                 resources:
                   requests:
                     cpu: "512m"
                     memory: "512Mi"
                   limits:
                     cpu: "1"
                     memory: "512Mi"
                 env:
                 - name: CONTEXT_PATH
                   value: "/generate"
                 - name: HOST
                   value: "http://llm-service"
                 - name: LLM_ENGINE
                   value: "tgi"
                 - name: MODEL_ID
                   value: "falcon-40b-instruct"
                 - name: USER_PROMPT
                   value: "User: prompt"
                 - name: SYSTEM_PROMPT
                   value: "Assistant: prompt"
                 ports:
                 - containerPort: 7860
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: gradio-service
         spec:
           type: LoadBalancer
           selector:
             app: gradio
           ports:
           - port: 80
             targetPort: 7860
         

  2. Apply the manifest:
         
         kubectl apply -f gradio.yaml
         

  3. Find the external IP address of the Service:
         
         kubectl get svc
         

The output is similar to the following:
         
         NAME             TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)        AGE
         gradio-service   LoadBalancer   10.24.29.197   34.172.115.35   80:30952/TCP   125m
         

  4. Copy the external IP address from the `EXTERNAL-IP` column.

  5. View the model interface from your web browser by using the external IP address with the exposed port:
         
         http://EXTERNAL_IP
         




**Success:** At this point, you have deployed an LLM using L4 GPUs in GKE.

## Calculate the amount of GPUs

The amount of GPUs depends on the value of the `QUANTIZE` flag. In this tutorial, `QUANTIZE` is set to `bitsandbytes-nf4`, which means that the model is loaded in 4 bits.

A 70 billion parameter model would require a minimum of 40 GB of GPU memory which equals to 70 billion times 4 bits (70 billion x 4 bits= 35 GB) and considers a 5 GB of overhead. In this case, a single L4 GPU wouldn't have enough memory. Therefore, the examples in this tutorial use _two_ L4 GPU of memory (2 x 24 = 48 GB). This configuration is sufficient for running Falcon 40b or Llama 3 70b in L4 GPUs.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the cluster

To avoid incurring charges to your Google Cloud account for the resources that you created in this guide, delete the GKE cluster:
    
    
    gcloud container clusters delete l4-demo --location ${CONTROL_PLANE_LOCATION}
    

## What's next

  * [Learn more about G2 VMs with NVIDIA L4 GPUs](https://cloud.google.com/blog/products/compute/introducing-g2-vms-with-nvidia-l4-gpus)
  * [Train a model with GPUs on GKE Standard mode](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/train-model-gpus-standard)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
