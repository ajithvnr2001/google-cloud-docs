---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-with-gke-inference-gateway/
title: Serve an LLM with GKE Inference Gateway \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:42:38.358267+00:00
---

# Serve an LLM with GKE Inference Gateway  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-with-gke-inference-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Serve an LLM with GKE Inference Gateway Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial describes how to deploy a large language model (LLM) on Google Kubernetes Engine (GKE) with the GKE Inference Gateway. The tutorial includes steps for cluster setup, model deployment, GKE Inference Gateway configuration, and handling LLM requests.

This tutorial is for Machine learning (ML) engineers, Platform admins and operators, and Data and AI specialists who want to deploy and manage LLM applications on GKE with GKE Inference Gateway.

Before you read this page, familiarize yourself with the following:

  * [About model inference on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/inference)
  * [Run best practice inference with GKE Inference Quickstart recipes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart)
  * [Autopilot mode and Standard mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)
  * [GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus)



## Background

This section describes the key technologies used in this tutorial. For more information about model serving concepts and terminology, and how GKE generative AI capabilities can enhance and support your model serving performance, see [About model inference on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/inference).

## vLLM

vLLM is a highly optimized open source LLM serving framework that increases serving throughput on GPUs. Key features include the following:

  * Optimized transformer implementation with [PagedAttention](https://docs.vllm.ai/en/latest/design/kernel/paged_attention.html#vllm-paged-attention)
  * Continuous batching that improves the overall serving throughput
  * Tensor parallelism and distributed serving across multiple GPUs



To learn more, refer to the [vLLM documentation](https://docs.vllm.ai/en/latest/).

### GKE Inference Gateway

GKE Inference Gateway enhances the capabilities of GKE for serving LLMs. It optimizes inference workloads with features such as the following:

  * Inference-optimized load balancing based on load metrics.
  * Support for dense multi-workload serving of LoRA adapters.
  * Model-aware routing for simplified operations.



For more information, see [About GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway).

## Objectives

  1. Get access to the model.
  2. Prepare your environment.
  3. Create and configure Google Cloud resources.
  4. Install the `InferenceObjective` and `InferencePool` CRDs.
  5. Deploy the model server.
  6. Configure observability for your Inference Gateway.



## Before you begin

  * Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Enable the required API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Enable the required API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  * Make sure that you have the following role or roles on the project: roles/container.admin, roles/iam.serviceAccountAdmin 

#### Check for the roles

    1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
    2. Select the project. 
    3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

    4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

    1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
    2. Select the project. 
    3. Click person_add **Grant access**. 
    4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

    5. Click **Select a role** , then search for the role. 
    6. To grant additional roles, click add **Add another role** and add each additional role. 
    7. Click **Save**. 


  * Create a [Hugging Face](https://huggingface.co/) account, if you don't already have one.
  * Ensure your project has sufficient quota for H100 GPUs. To learn more, see [Plan GPU quota](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus#gpu-quota) and [Allocation quotas](https://docs.cloud.google.com/compute/resource-usage#gpu_quota).



## Get access to the model

To deploy the `Llama3.1` model to GKE, sign the license consent agreement and generate a Hugging Face access token.

### Sign the license consent agreement

You must sign the consent agreement to use the `Llama3.1` model. Follow these instructions:

  1. Access consent page and verify consent for using your Hugging Face account.
  2. Accept the model terms.



### Generate an access token

To access the model through Hugging Face, you need a [Hugging Face token](https://huggingface.co/docs/hub/security-tokens).

Follow these steps to generate a new token if you don't have one already:

  1. Click **Your Profile > Settings > Access Tokens**.
  2. Select **New Token**.
  3. Specify a name of your choice and a role of at least `Read`.
  4. Select **Generate a token**.
  5. Copy the generated token to your clipboard.



## Prepare your environment

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell) to manage resources hosted on Google Cloud. Cloud Shell comes preinstalled with the software you need for this tutorial, including [`kubectl`](https://kubernetes.io/docs/reference/kubectl/) and [ gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

To set up your environment with Cloud Shell, perform the following steps:

  1. In the Google Cloud console, launch a Cloud Shell session by clicking ![Cloud Shell activation icon](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg)**Activate Cloud Shell** in the [Google Cloud console](http://console.cloud.google.com). This launches a session in the bottom pane of Google Cloud console.

  2. Set the default environment variables:
         
         gcloud config set project PROJECT_ID
         gcloud config set billing/quota_project PROJECT_ID
         export PROJECT_ID=$(gcloud config get project)
         export REGION=REGION
         export CLUSTER_NAME=CLUSTER_NAME
         export HF_TOKEN=HF_TOKEN
         

Replace the following values:

     * `PROJECT_ID`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * `REGION`: a region that supports the accelerator type you want to use, for example, `us-central1` for H100 GPU.
     * `CLUSTER_NAME`: the name of your cluster.
     * `HF_TOKEN`: the Hugging Face token you generated earlier.



## Create and configure Google Cloud resources

**Note:** You might need to create a capacity reservation to use some accelerators. For more information about reserving and consuming reserved resources, see [Consuming reserved zonal resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations).

### Create a GKE cluster and node pool

Serve LLMs on GPUs in a GKE Autopilot or Standard cluster. We recommend that you use a Autopilot cluster for a fully managed Kubernetes experience. To choose the GKE mode of operation that's the best fit for your workloads, see [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

### Autopilot

In Cloud Shell, run the following command:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --project=PROJECT_ID \
        --location=CONTROL_PLANE_LOCATION \
        --release-channel=rapid
    

Replace the following values:

  * `PROJECT_ID`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region that supports the accelerator type you want to use, for example, `us-central1` for H100 GPU.
  * `CLUSTER_NAME`: the name of your cluster.



GKE creates an Autopilot cluster with CPU and GPU nodes as requested by the deployed workloads.

### Standard

  1. In Cloud Shell, run the following command to create a Standard cluster:
         
         gcloud container clusters create CLUSTER_NAME \
             --project=PROJECT_ID \
             --location=CONTROL_PLANE_LOCATION \
             --workload-pool=PROJECT_ID.svc.id.goog \
             --release-channel=rapid \
             --num-nodes=1 \
             --enable-managed-prometheus \
             --monitoring=SYSTEM,DCGM \
             --gateway-api=standard
         

Replace the following values:

     * `PROJECT_ID`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region that supports the accelerator type you want to use, for example, `us-central1` for H100 GPU.
     * `CLUSTER_NAME`: the name of your cluster.

The cluster creation might take several minutes.

  2. To create a [node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) with the appropriate disk size for running `Llama-3.1-8B-Instruct` model, run the following command:
         
         gcloud container node-pools create gpupool \
             --accelerator type=nvidia-h100-80gb,count=2,gpu-driver-version=latest \
             --project=PROJECT_ID \
             --location=CONTROL_PLANE_LOCATION \
             --node-locations=CONTROL_PLANE_LOCATION-a \
             --cluster=CLUSTER_NAME \
             --machine-type=a3-highgpu-2g \
             --num-nodes=1 \
             --disk-type="pd-balanced"
         

GKE creates a single node pool containing a H100 GPU.




### Set up authorization to scrape metrics

To set up authorization to scrape metrics, create the `inference-gateway-sa-metrics-reader-secret` secret.

  1. Save the following manifest as `metrics-auth.yaml`:
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRole
         metadata:
           name: inference-gateway-metrics-reader
         rules:
         - nonResourceURLs:
           - /metrics
           verbs:
           - get
         ---
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: inference-gateway-sa-metrics-reader
           namespace: default
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRoleBinding
         metadata:
           name: inference-gateway-sa-metrics-reader-role-binding
           namespace: default
         subjects:
         - kind: ServiceAccount
           name: inference-gateway-sa-metrics-reader
           namespace: default
         roleRef:
           kind: ClusterRole
           name: inference-gateway-metrics-reader
           apiGroup: rbac.authorization.k8s.io
         ---
         apiVersion: v1
         kind: Secret
         metadata:
           name: inference-gateway-sa-metrics-reader-secret
           namespace: default
           annotations:
             kubernetes.io/service-account.name: inference-gateway-sa-metrics-reader
         type: kubernetes.io/service-account-token
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRole
         metadata:
           name: inference-gateway-sa-metrics-reader-secret-read
         rules:
         - resources:
           - secrets
           apiGroups:
           - ""
           verbs:
           - get
           - list
           - watch
           resourceNames:
           - inference-gateway-sa-metrics-reader-secret
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRoleBinding
         metadata:
           name: gmp-system:collector:inference-gateway-sa-metrics-reader-secret-read
           namespace: default
         roleRef:
           name: inference-gateway-sa-metrics-reader-secret-read
           kind: ClusterRole
           apiGroup: rbac.authorization.k8s.io
         subjects:
         - name: collector
           namespace: gmp-system
           kind: ServiceAccount

  2. Apply the manifest:
         
         kubectl apply -f metrics-auth.yaml
         




### Create a Kubernetes secret for Hugging Face credentials

In Cloud Shell, do the following:

  1. Configure `kubectl` so it can communicate with your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=REGION
         

Replace the following values:

     * `REGION`: a region that supports the accelerator type you want to use, for example, `us-central1` for L4 GPU.
     * `CLUSTER_NAME`: the name of your cluster.
  2. Create a Kubernetes Secret that contains the Hugging Face token:
         
         kubectl create secret generic hf-secret \
             --from-literal=hf_api_token=${HF_TOKEN} \
             --dry-run=client -o yaml | kubectl apply -f -
         

Replace `HF_TOKEN` with the Hugging Face token you generated earlier.




## Install the `InferenceObjective` and `InferencePool` CRDs

In this section, you install the necessary Custom Resource Definitions (CRDs) for GKE Inference Gateway.

CRDs extend the Kubernetes API. This lets you define new resource types. To use GKE Inference Gateway, install the `InferencePool` and `InferenceObjective` CRDs in your GKE cluster by running the following command:
    
    
    kubectl apply -f https://github.com/kubernetes-sigs/gateway-api-inference-extension/releases/download/v1.0.0/manifests.yaml
    

## Deploy the model server

This example deploys a `Llama3.1` model using a vLLM model server. The deployment is labeled as `app:vllm-llama3.1-8b-instruct`. This deployment also uses two LoRA adapters named `food-review` and `cad-fabricator` from Hugging Face. You can update this deployment with your own model server and model container, serving port, and deployment name. You can optionally configure LoRA adapters in the deployment, or deploy the base model.

**Note:** We don't recommend using base models like Llama 3 8B for production chatbots due to safety concerns. For more information about best practices, see [System instructions for safety](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/safety-system-instructions).

  1. To deploy on a `nvidia-h100-80gb` accelerator type, save the following manifest as `vllm-llama3.1-8b-instruct.yaml`. This manifest defines a Kubernetes Deployment with your model and model server:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: vllm-llama3.1-8b-instruct
         spec:
           replicas: 3
           selector:
             matchLabels:
               app: vllm-llama3.1-8b-instruct
           template:
             metadata:
               labels:
                 app: vllm-llama3.1-8b-instruct
             spec:
               containers:
                 - name: vllm
                   image: "vllm/vllm-openai:v0.13.0"
                   imagePullPolicy: Always
                   command: ["python3", "-m", "vllm.entrypoints.openai.api_server"]
                   args:
                   - "--model"
                   - "meta-llama/Llama-3.1-8B-Instruct"
                   - "--tensor-parallel-size"
                   - "1"
                   - "--port"
                   - "8000"
                   - "--enable-lora"
                   - "--max-loras"
                   - "2"
                   - "--max-cpu-loras"
                   - "12"
                   - "--compilation-config"
                   - '{"cudagraph_specialize_lora": "False"}' # As workaround for https://github.com/vllm-project/vllm/issues/29049
                   env:
                     - name: PORT
                       value: "8000"
                     - name: HUGGING_FACE_HUB_TOKEN
                       valueFrom:
                         secretKeyRef:
                           name: hf-secret
                           key: hf_api_token
                     - name: VLLM_ALLOW_RUNTIME_LORA_UPDATING
                       value: "true"
                   ports:
                     - containerPort: 8000
                       name: http
                       protocol: TCP
                   lifecycle:
                     preStop:
                       # vLLM stops accepting connections when it receives SIGTERM, so we need to sleep
                       # to give upstream gateways a chance to take us out of rotation. The time we wait
                       # is dependent on the time it takes for all upstreams to completely remove us from
                       # rotation. Older or simpler load balancers might take upwards of 30s, but we expect
                       # our deployment to run behind a modern gateway like Envoy which is designed to
                       # probe for readiness aggressively.
                       sleep:
                         # Upstream gateway probers for health should be set on a low period, such as 5s,
                         # and the shorter we can tighten that bound the faster that we release
                         # accelerators during controlled shutdowns. However, we should expect variance,
                         # as load balancers may have internal delays, and we don't want to drop requests
                         # normally, so we're often aiming to set this value to a p99 propagation latency
                         # of readiness -> load balancer taking backend out of rotation, not the average.
                         #
                         # This value is generally stable and must often be experimentally determined on
                         # for a given load balancer and health check period. We set the value here to
                         # the highest value we observe on a supported load balancer, and we recommend
                         # tuning this value down and verifying no requests are dropped.
                         #
                         # If this value is updated, be sure to update terminationGracePeriodSeconds.
                         #
                         seconds: 30
                       #
                       # IMPORTANT: preStop.sleep is beta as of Kubernetes 1.30 - for older versions
                       # replace with this exec action.
                       #exec:
                       #  command:
                       #  - /usr/bin/sleep
                       #  - 30
                   livenessProbe:
                     httpGet:
                       path: /health
                       port: http
                       scheme: HTTP
                     # vLLM's health check is simple, so we can more aggressively probe it.  Liveness
                     # check endpoints should always be suitable for aggressive probing.
                     periodSeconds: 1
                     successThreshold: 1
                     # vLLM has a very simple health implementation, which means that any failure is
                     # likely significant. However, any liveness triggered restart requires the very
                     # large core model to be reloaded, and so we should bias towards ensuring the
                     # server is definitely unhealthy vs immediately restarting. Use 5 attempts as
                     # evidence of a serious problem.
                     failureThreshold: 5
                     timeoutSeconds: 1
                   readinessProbe:
                     httpGet:
                       path: /health
                       port: http
                       scheme: HTTP
                     # vLLM's health check is simple, so we can more aggressively probe it.  Readiness
                     # check endpoints should always be suitable for aggressive probing, but may be
                     # slightly more expensive than readiness probes.
                     periodSeconds: 1
                     successThreshold: 1
                     # vLLM has a very simple health implementation, which means that any failure is
                     # likely significant,
                     failureThreshold: 1
                     timeoutSeconds: 1
                   # We set a startup probe so that we don't begin directing traffic or checking
                   # liveness to this instance until the model is loaded.
                   startupProbe:
                     # Failure threshold is when we believe startup will not happen at all, and is set
                     # to the maximum possible time we believe loading a model will take. In our
                     # default configuration we are downloading a model from HuggingFace, which may
                     # take a long time, then the model must load into the accelerator. We choose
                     # 10 minutes as a reasonable maximum startup time before giving up and attempting
                     # to restart the pod.
                     #
                     # IMPORTANT: If the core model takes more than 10 minutes to load, pods will crash
                     # loop forever. Be sure to set this appropriately.
                     failureThreshold: 600
                     # Set delay to start low so that if the base model changes to something smaller
                     # or an optimization is deployed, we don't wait unnecessarily.
                     initialDelaySeconds: 2
                     # As a startup probe, this stops running and so we can more aggressively probe
                     # even a moderately complex startup - this is a very important workload.
                     periodSeconds: 1
                     httpGet:
                       # vLLM does not start the OpenAI server (and hence make /health available)
                       # until models are loaded. This may not be true for all model servers.
                       path: /health
                       port: http
                       scheme: HTTP
         
                   resources:
                     limits:
                       nvidia.com/gpu: 1
                     requests:
                       nvidia.com/gpu: 1
                   volumeMounts:
                     - mountPath: /data
                       name: data
                     - mountPath: /dev/shm
                       name: shm
                     - name: adapters
                       mountPath: "/adapters"
               # This is the second container in the Pod, a sidecar to the vLLM container.
               # It watches the ConfigMap and downloads LoRA adapters.
                 - name: lora-adapter-syncer
                   image: us-central1-docker.pkg.dev/k8s-staging-images/gateway-api-inference-extension/lora-syncer:main
                   imagePullPolicy: Always
                   env:
                     - name: DYNAMIC_LORA_ROLLOUT_CONFIG
                       value: "/config/configmap.yaml"
                   volumeMounts: # DO NOT USE subPath, dynamic configmap updates don't work on subPaths
                   - name: config-volume
                     mountPath: /config
               restartPolicy: Always
         
               # vLLM allows VLLM_PORT to be specified as an environment variable, but a user might
               # create a 'vllm' service in their namespace. That auto-injects VLLM_PORT in docker
               # compatible form as `tcp://<IP>:<PORT>` instead of the numeric value vLLM accepts
               # causing CrashLoopBackoff. Set service environment injection off by default.
               enableServiceLinks: false
         
               # Generally, the termination grace period needs to last longer than the slowest request
               # we expect to serve plus any extra time spent waiting for load balancers to take the
               # model server out of rotation.
               #
               # An easy starting point is the p99 or max request latency measured for your workload,
               # although LLM request latencies vary significantly if clients send longer inputs or
               # trigger longer outputs. Since steady state p99 will be higher than the latency
               # to drain a server, you may wish to slightly this value either experimentally or
               # via the calculation below.
               #
               # For most models you can derive an upper bound for the maximum drain latency as
               # follows:
               #
               #   1. Identify the maximum context length the model was trained on, or the maximum
               #      allowed length of output tokens configured on vLLM (llama2-7b was trained to
               #      4k context length, while llama3-8b was trained to 128k).
               #   2. Output tokens are the more compute intensive to calculate and the accelerator
               #      will have a maximum concurrency (batch size) - the time per output token at
               #      maximum batch with no prompt tokens being processed is the slowest an output
               #      token can be generated (for this model it would be about 10ms TPOT at a max
               #      batch size around 50, or 100 tokens/sec)
               #   3. Calculate the worst case request duration if a request starts immediately
               #      before the server stops accepting new connections - generally when it receives
               #      SIGTERM (for this model that is about 4096 / 100 ~ 40s)
               #   4. If there are any requests generating prompt tokens that will delay when those
               #      output tokens start, and prompt token generation is roughly 6x faster than
               #      compute-bound output token generation, so add 40% to the time from above (40s +
               #      16s = 56s)
               #
               # Thus we think it will take us at worst about 56s to complete the longest possible
               # request the model is likely to receive at maximum concurrency (highest latency)
               # once requests stop being sent.
               #
               # NOTE: This number will be lower than steady state p99 latency since we stop       receiving
               #       new requests which require continuous prompt token computation.
                   # NOTE: The max timeout for backend connections from gateway to model servers should
               #       be configured based on steady state p99 latency, not drain p99 latency
               #
               #   5. Add the time the pod takes in its preStop hook to allow the load balancers to
               #      stop sending us new requests (56s + 30s = 86s).
               #
               # Because the termination grace period controls when the Kubelet forcibly terminates a
               # stuck or hung process (a possibility due to a GPU crash), there is operational safety
               # in keeping the value roughly proportional to the time to finish serving. There is also
               # value in adding a bit of extra time to deal with unexpectedly long workloads.
               #
               #   6. Add a 50% safety buffer to this time (86s * 1.5 ≈ 130s).
               #
               # One additional source of drain latency is that some workloads may run close to
               # saturation and have queued requests on each server. Since traffic in excess of the
               # max sustainable QPS will result in timeouts as the queues grow, we assume that failure
               # to drain in time due to excess queues at the time of shutdown is an expected failure
               # mode of server overload. If your workload occasionally experiences high queue depths
               # due to periodic traffic, consider increasing the safety margin above to account for
               # time to drain queued requests.
               terminationGracePeriodSeconds: 130
               nodeSelector:
                 cloud.google.com/gke-accelerator: "nvidia-h100-80gb"
               volumes:
                 - name: data
                   emptyDir: {}
                 - name: shm
                   emptyDir:
                     medium: Memory
                 - name: adapters
                   emptyDir: {}
                 - name: config-volume
                   configMap:
                     name: vllm-llama3.1-8b-adapters
         ---
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: vllm-llama3.1-8b-adapters
         data:
           configmap.yaml: |
               vLLMLoRAConfig:
                 name: vllm-llama3.1-8b-instruct
                 port: 8000
                 defaultBaseModel: meta-llama/Llama-3.1-8B-Instruct
                 ensureExist:
                   models:
                   - id: food-review
                     source: Kawon/llama3.1-food-finetune_v14_r8
                   - id: cad-fabricator
                     source: redcathode/fabricator
         ---
         kind: HealthCheckPolicy
         apiVersion: networking.gke.io/v1
         metadata:
           name: health-check-policy
           namespace: default
         spec:
           targetRef:
             group: "inference.networking.k8s.io"
             kind: InferencePool
             name: vllm-llama3.1-8b-instruct
           default:
             config:
               type: HTTP
               httpHealthCheck:
                   requestPath: /health
                   port: 8000
         

  2. Apply the manifest to your cluster:
         
         kubectl apply -f vllm-llama3.1-8b-instruct.yaml
         




## Create an `InferencePool` resource

The `InferencePool` Kubernetes custom resource defines a group of Pods with a common base LLM and compute configuration.

The `InferencePool` custom resource includes the following key fields:

  * `selector`: specifies which Pods belong to this pool. The labels in this selector must exactly match the labels applied to your model server Pods.
  * `targetPort`: defines the ports used by the model server within the Pods.



The `InferencePool` resource enables GKE Inference Gateway to route traffic to your model server Pods.

**Note:** The Pods that the `InferencePool` resource selects must already be running.

To create an `InferencePool` using Helm, perform the following steps:
    
    
    helm install vllm-llama3.1-8b-instruct \
      --set inferencePool.modelServers.matchLabels.app=vllm-llama3.1-8b-instruct \
      --set provider.name=gke \
      --set healthCheckPolicy.create=false \
      --version v1.0.0 \
      oci://registry.k8s.io/gateway-api-inference-extension/charts/inferencepool
    

Change the following field to match your Deployment:

  * `inferencePool.modelServers.matchLabels.app`: the key of the label used to select your model server Pods.



This command creates an `InferencePool` object that logically represents your model server deployment and references the model endpoint services within the Pods that the `Selector` selects.

## Create an `InferenceObjective` resource with a serving criticality

The `InferenceObjective` custom resource defines the serving parameters for a model, including its priority. You must create `InferenceObjective` resources to define which models are served on an `InferencePool`. These resources can reference base models or LoRA adapters supported by the model servers in the `InferencePool`.

The `metadata.name` field specifies the model's name, the `priority` field sets its serving criticality, and the `poolRef` field links to the `InferencePool` where the model is served.

To create an `InferenceObjective`, perform the following steps:

  1. Save the following sample manifest as `inferenceobjective.yaml`:
         
         apiVersion: inference.networking.x-k8s.io/v1alpha2
         kind: InferenceObjective
         metadata:
           name: MODEL_NAME
         spec:
           priority: VALUE
           poolRef:
             name: INFERENCE_POOL_NAME
             kind: "InferencePool"
         

Replace the following:

     * `MODEL_NAME`: the name of your base model or LoRA adapter. For example, `food-review`.
     * `VALUE`: the priority for the inference objective. This is an integer where a higher value indicates a more critical request. For example, `10`.
     * `INFERENCE_POOL_NAME`: the name of the `InferencePool` you created in the previous step. For example, `vllm-llama3.1-8b-instruct`.
  2. Apply the sample manifest to your cluster:
         
         kubectl apply -f inferenceobjective.yaml
         




The following example creates two `InferenceObjective` objects. The first configures the `food-review` LoRA model on the `vllm-llama3.1-8b-instruct` `InferencePool` with a priority of `10`. The second configures the `llama3-base-model` to be served with a higher priority of `20`.
    
    
    apiVersion: inference.networking.k8s.io/v1alpha1
    kind: InferenceObjective
    metadata:
      name: food-review
    spec:
      priority: 10
      poolRef:
        name: vllm-llama3.1-8b-instruct
        kind: "InferencePool"
    ---
    apiVersion: inference.networking.k8s.io/v1alpha1
    kind: InferenceObjective
    metadata:
      name: llama3-base-model
    spec:
      priority: 20
      poolRef:
        name: vllm-llama3.1-8b-instruct
        kind: "InferencePool"
    

## Create the Gateway

The Gateway resource acts as the entry point for external traffic into your Kubernetes cluster. It defines the listeners that accept incoming connections.

GKE Inference Gateway supports the `gke-l7-rilb` and `gke-l7-regional-external-managed` Gateway Class. For more information, see the GKE documentation on [Gateway Classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#gatewayclass).

**Note:** The `gke-l7-regional-external-managed` GatewayClass requires a proxy-only subnet. For more information, see [create the proxy-only subnet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#configure_a_proxy-only_subnet).

To create a Gateway, perform the following steps:

  1. Save the following sample manifest as `gateway.yaml`:
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: Gateway
         metadata:
           name: GATEWAY_NAME
         spec:
           gatewayClassName: gke-l7-regional-external-managed
           listeners:
             - protocol: HTTP # Or HTTPS for production
               port: 80 # Or 443 for HTTPS
               name: http
         

Replace `GATEWAY_NAME` with a unique name for your Gateway resource. For example, `inference-gateway`.

  2. Apply the manifest to your cluster:
         
         kubectl apply -f gateway.yaml
         




## Create the `HTTPRoute` resource

In this section, you create an `HTTPRoute` resource to define how the Gateway routes incoming HTTP requests to your `InferencePool`.

The HTTPRoute resource defines how the GKE Gateway routes incoming HTTP requests to backend services, which is your `InferencePool`. It specifies matching rules (for example, headers, or paths) and the backend to which traffic should be forwarded.

To create an HTTPRoute, perform the following steps:

  1. Save the following sample manifest as `httproute.yaml`:
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: HTTPRoute
         metadata:
           name: HTTPROUTE_NAME
         spec:
           parentRefs:
           - name: GATEWAY_NAME
           rules:
           - matches:
             - path:
                 type: PathPrefix
                 value: PATH_PREFIX
             backendRefs:
             - name: INFERENCE_POOL_NAME
               group: inference.networking.k8s.io
               kind: InferencePool
         

Replace the following:

     * `HTTPROUTE_NAME`: a unique name for your `HTTPRoute` resource. For example, `my-route`.
     * `GATEWAY_NAME`: the name of the `Gateway` resource that you created. For example, `inference-gateway`.
     * `PATH_PREFIX`: the path prefix that you use to match incoming requests. For example, `/` to match all.
     * `INFERENCE_POOL_NAME`: the name of the `InferencePool` resource that you want to route traffic to. For example, `vllm-llama3.1-8b-instruct`.
  2. Apply the manifest to your cluster:
         
         kubectl apply -f httproute.yaml
         

**Note:** To configure Cross-Origin Resource Sharing (CORS) for your inference endpoints by using a `CORS` filter in the `HTTPRoute`, see [Configure Cross-Origin Resource Sharing (CORS)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#configure-cors).



## Send an inference request

After you have configured GKE Inference Gateway, you can send inference requests to your deployed model.

To send inference requests, perform the following steps:

  * Retrieve the Gateway endpoint.
  * Construct a properly formatted JSON request.
  * Use `curl` to send the request to the `/v1/completions` endpoint.



This lets you generate text based on your input prompt and specified parameters.

  1. To get the Gateway endpoint, run the following command:
         
         IP=$(kubectl get gateway/GATEWAY_NAME -o jsonpath='{.status.addresses[0].value}')
         PORT=80
         

Replace `GATEWAY_NAME` with the name of your Gateway resource.

  2. To send a request to the `/v1/completions` endpoint using `curl`, run the following command:
         
         curl -i -X POST http://${IP}:${PORT}/v1/completions \
         -H "Content-Type: application/json" \
         -d '{
             "model": "MODEL_NAME",
             "prompt": "PROMPT_TEXT",
             "max_tokens": MAX_TOKENS,
             "temperature": "TEMPERATURE"
         }'
         

Replace the following:

     * `MODEL_NAME`: the name of the model or LoRA adapter to use.
     * `PROMPT_TEXT`: the input prompt for the model.
     * `MAX_TOKENS`: the maximum number of tokens to generate in the response.
     * `TEMPERATURE`: controls the randomness of the output. Use the value `0` for deterministic output, or a higher number for more creative output.



Keep the following in mind:

  * **Request body** : the request body can include additional parameters like `stop` and `top_p`. Refer to the [OpenAI API specification](https://platform.openai.com/docs/api-reference/completions) for a complete list of options.
  * **Error handling** : implement proper error handling in your client code to handle potential errors in the response. For example, check the HTTP status code in the `curl` response. A non-200 status code generally indicates an error.
  * **Authentication and authorization** : for production deployments, secure your API endpoint with authentication and authorization mechanisms. Include the appropriate headers (for example, `Authorization`) in your requests.



## Configure observability for your Inference Gateway

GKE Inference Gateway provides observability into the health, performance, and behavior of your inference workloads. This helps you to identify and resolve issues, optimize resource utilization, and ensure the reliability of your applications. You can view these observability metrics in Cloud Monitoring through the [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

To configure observability for GKE Inference Gateway, see [Configure observability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-gke-inference-gateway-configurations#observability).

## Delete the deployed resources

To avoid incurring charges to your Google Cloud account for the resources that you created from this guide, run the following command:
    
    
    gcloud container clusters delete CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION
    

Replace the following values:

  * `CONTROL_PLANE_LOCATION`: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.
  * `CLUSTER_NAME`: the name of your cluster.



## What's next

  * Read about [GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway).
  * Read about [Deploying GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-gke-inference-gateway).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
