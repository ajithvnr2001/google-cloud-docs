---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/kuberay-trillium/
title: Configure KubeRay with TPU Trillium \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:26:18.134927+00:00
---

# Configure KubeRay with TPU Trillium  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/kuberay-trillium/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Configure KubeRay with TPU Trillium Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial shows you how to configure KubeRay with TPU Trillium on Google Kubernetes Engine (GKE). Learn to set up both single-host and multi-host TPU configurations, including necessary environment variables and Pod specifications for [TPU Trillium](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#trillium-benefits).

This tutorial is for Platform admins and operators and Data and AI specialists who want to want to learn how to configure TPU Trillium initialization with KubeRay for single-host and multi-host node pools. This tutorial demonstrates how to run a script with Jax that verifies successful TPU initialization. This tutorial doesn't deploy a model.

Before you configure KubeRay in GKE, ensure that you are familiar with [Ray definitions and terminology in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview).

## Overview

This tutorial shows how to run a Python script with [Jax](https://github.com/google/jax) that verifies that TPU Trillium initialization with [KubeRay](https://github.com/ray-project/kuberay) was successful. Jax is a high-performance numerical computation library that supports machine learning workloads. [KubeRay](https://github.com/ray-project/kuberay) is a Kubernetes operator that provides a unified way to deploy, manage, and monitor Ray applications on Kubernetes.

Trillium TPUs (v6e) require specific environment variables and Pod specifications that differ from previous TPU generations. This tutorial provides the necessary configurations to successfully deploy a workload with KubeRay on Trillium TPUs.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure you have the [Ray CLI](https://docs.ray.io/en/latest/cluster/running-applications/job-submission/quickstart.html) (version 2.37.0) installed.



## Activate Cloud Shell

[Cloud Shell](https://docs.cloud.google.com/shell) comes preinstalled with the `gcloud`, `helm`, and `kubectl` command-line tools that are used in this tutorial.

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).
  2. At the top of the Google Cloud console window, click the **Activate Cloud Shell** ![Activate Shell Button](https://docs.cloud.google.com/static/kubernetes-engine/images/cloud-shell.png) button.

A Cloud Shell session opens inside a new frame in the Google Cloud console and displays a command-line prompt.

![Cloud Shell session](https://docs.cloud.google.com/static/shell/docs/images/new-console.png)




## Create a GKE cluster and node pool

You can configure KubeRay on TPUs in a GKE Autopilot or Standard cluster. We recommend that you use a Autopilot cluster for a fully managed Kubernetes experience. To choose the GKE mode of operation that's the best fit for your workloads, see [About GKE modes of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

### Autopilot

  1. In Cloud Shell, run the following command:
         
         gcloud container clusters create-auto CLUSTER_NAME \
             --enable-ray-operator \
             --release-channel=rapid \
             --location=LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: the name of the new cluster.
     * `LOCATION`: the region where your TPU Trillium capacity is available. For more information, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).

GKE creates an Autopilot cluster with the Ray operator addon enabled. The addon automatically installs the Ray TPU webhook in the cluster control plane.

  2. To communicate with your cluster, configure `kubectl` :
         
         gcloud container clusters get-credentials CLUSTER_NAME --location=LOCATION
         




### Standard

  1. In Cloud Shell, create a Standard cluster that enables the Ray operator addon by running the following command to :
         
         gcloud container clusters create CLUSTER_NAME \
           --location LOCATION \
           --addons=RayOperator \
           --cluster-version=1.33 \
           --machine-type=n1-standard-16
         

Replace the following:

     * `CLUSTER_NAME`: the name of the new cluster.
     * `LOCATION`: the region where your TPU Trillium capacity is available. For more information, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).

The cluster creation might take several minutes.

  2. To communicate with your cluster, configure `kubectl` :
         
         gcloud container clusters get-credentials CLUSTER_NAME --location=LOCATION
         

  3. You can create a [single-host](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#single-host) or a [multi-host](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#multi-host) TPU slice node pool:




### Single-host

In Cloud Shell, run the following command:
    
    
    gcloud container node-pools create v6e-4 \
        --location=us-central2-b \
        --cluster=CLUSTER_NAME \
        --machine-type=ct6e-standard-4t \
        --num-nodes=1 \
        --threads-per-core=1 \
        --tpu-topology=2x2
    

### Multi-host

In Cloud Shell, run the following command:
    
    
    gcloud container node-pools create v6e-16 \
        --location=us-central2-b \
        --cluster=CLUSTER_NAME \
        --machine-type=ct6e-standard-4t \
        --num-nodes=4 \
        --threads-per-core=1 \
        --tpu-topology=4x4
    

## Run a RayJob custom resource

By defining a RayJob manifest, you instruct KubeRay to do the following:

  * **Create a RayCluster:** the RayJob spec includes a `rayClusterSpec` which defines the Ray cluster configuration (head and worker groups) that you want.
  * **Run a specific Job:** the `entrypoint` field within the RayJob specifies the command or script to execute within the created Ray cluster. In this tutorial, the `entrypoint` is a Python script ([`tpu_list_devices.py`](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/gke-ray/tpu/tpu_list_devices.py)) designed to verify the TPU Trillium initialization.



To create a RayJob custom resource, complete the following steps:

### Single-host

  1. Create the following `ray-job.tpu-v6e-singlehost.yaml` manifest:
         
         apiVersion: ray.io/v1
         kind: RayJob
         metadata:
           name: v6e-4-job
         spec:
           entrypoint: python ai-ml/gke-ray/tpu/tpu_list_devices.py
           runtimeEnvYAML: |
             working_dir: "https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/archive/refs/heads/main.zip"
             pip:
               - jax[tpu]==0.4.33
               - -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
           rayClusterSpec:
             rayVersion: '2.43.0'
             headGroupSpec:
               rayStartParams: {}
               template:
                 spec:
                   containers:
                   -   name: ray-head
                       image: rayproject/ray:2.43.0-py310
                       ports:
                         - containerPort: 6379
                           name: gcs-server
                         - containerPort: 8265
                           name: dashboard
                         - containerPort: 10001
                           name: client
                       resources:
                         limits:
                           cpu: "8"
                           memory: 40G
                         requests:
                           cpu: "8"
                           memory: 40G
             workerGroupSpecs:
             -   replicas: 1
                 minReplicas: 1
                 maxReplicas: 1
                 numOfHosts: 1
                 groupName: tpu-group
                 rayStartParams: {}
                 template:
                   spec:
                     containers:
                     -   name: ray-worker
                         image: rayproject/ray:2.43.0-py310
                         resources:
                           limits:
                             cpu: "24"
                             google.com/tpu: "4"
                             memory: 200G
                           requests:
                             cpu: "24"
                             google.com/tpu: "4"
                             memory: 200G
                     nodeSelector:
                       cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                       cloud.google.com/gke-tpu-topology: 2x2

  2. Apply the manifest:
         
         kubectl apply -f ray-job.tpu-v6e-singlehost.yaml
         

  3. Verify that the RayJob is created and running:
         
         kubectl get rayjobs v6e-4-job
         

The output is similar to the following:
         
         NAME      JOB STATUS   DEPLOYMENT STATUS   RAY CLUSTER NAME       START TIME  END TIME   AGE
         v6e-4-job PENDING      Running             v6e-4-job-raycluster   2024-10-15T23:15:22Z  20s
         

  4. Print the output of the RayJob.
         
         kubectl logs -l=job-name=v6e-4-job
         

The output is similar to the following:
         
         2024-10-15 16:15:40,222 INFO cli.py:300 -- ray job stop v6e-4-job-hzq5q
         2024-10-15 16:15:40,246 INFO cli.py:307 -- Tailing logs until the job exits (disable with --no-wait):
         2024-10-15 16:15:40,112 INFO job_manager.py:528 -- Runtime env is setting up.
         2024-10-15 16:15:50,181 INFO worker.py:1461 -- Using address 10.84.1.25:6379 set in the environment variable RAY_ADDRESS
         2024-10-15 16:15:50,181 INFO worker.py:1601 -- Connecting to existing Ray cluster at address: 10.84.1.25:6379...
         2024-10-15 16:15:50,186 INFO worker.py:1777 -- Connected to Ray cluster. View the dashboard at 10.84.1.25:8265
         ['TPU cores:4']
         2024-10-15 16:16:12,349 SUCC cli.py:63 -- -------------------------------------
         2024-10-15 16:16:12,349 SUCC cli.py:64 -- Job 'v6e-4-job-hzq5q' succeeded
         2024-10-15 16:16:12,349 SUCC cli.py:65 -- -------------------------------------
         




### Multi-host

  1. Create the following `ray-job.tpu-v6e-multihost.yaml` manifest:
         
         apiVersion: ray.io/v1
         kind: RayJob
         metadata:
           name: v6e-16-job
         spec:
           entrypoint: python ai-ml/gke-ray/tpu/tpu_list_devices.py
           runtimeEnvYAML: |
             working_dir: "https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/archive/refs/heads/main.zip"
             pip:
               - jax[tpu]==0.4.33
               - -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
           rayClusterSpec:
             rayVersion: '2.43.0'
             headGroupSpec:
               rayStartParams: {}
               template:
                 spec:
                   containers:
                   -   name: ray-head
                       image: rayproject/ray:2.43.0-py310
                       ports:
                         - containerPort: 6379
                           name: gcs-server
                         - containerPort: 8265
                           name: dashboard
                         - containerPort: 10001
                           name: client
                       resources:
                         limits:
                           cpu: "8"
                           memory: 40G
                         requests:
                           cpu: "8"
                           memory: 40G
             workerGroupSpecs:
               - replicas: 1
                 minReplicas: 1
                 maxReplicas: 1
                 numOfHosts: 4
                 groupName: tpu-group
                 rayStartParams: {}
                 template:
                   spec:
                     containers:
                       - name: ray-worker
                         image: rayproject/ray:2.43.0-py310
                         resources:
                           limits:
                             cpu: "24"
                             google.com/tpu: "4"
                             memory: 200G
                           requests:
                             cpu: "24"
                             google.com/tpu: "4"
                             memory: 200G
                         env:
                         - name: NODE_IP
                           valueFrom:
                             fieldRef:
                               fieldPath: status.hostIP
                         - name: VBAR_CONTROL_SERVICE_URL
                           value: $(NODE_IP):8353
                         - name: JAX_PLATFORMS
                           value: tpu,cpu
                         - name: ENABLE_PJRT_COMPATIBILITY
                           value: "true"
                         ports:
                         - containerPort: 8081
                           name: mxla
                     nodeSelector:
                       cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                       cloud.google.com/gke-tpu-topology: 4x4

  2. Apply the manifest:
         
         kubectl apply -f ray-job.tpu-v6e-multihost.yaml
         

  3. Verify the v6e-16 RayJob is created and running:
         
         kubectl get rayjobs v6e-16-job
         

The output is similar to the following:
         
         NAME         JOB STATUS   DEPLOYMENT STATUS   RAY CLUSTER NAME              START TIME             END TIME   AGE
         v6e-16-job                Running             v6e-16-job-raycluster-qr6vk   2024-10-16T19:28:19Z              66s
         

  4. Print the output of the v6e-16 RayJob:
         
         kubectl logs -l=job-name=v6e-16-job
         

The output is similar to the following:
         
         2024-10-16 12:21:33,986 INFO cli.py:300 -- ray job stop v6e-16-job-z44s7
         2024-10-16 12:21:34,011 INFO cli.py:307 -- Tailing logs until the job exits (disable with --no-wait):
         2024-10-16 12:21:33,826 INFO job_manager.py:528 -- Runtime env is setting up.
         2024-10-16 12:21:46,327 INFO worker.py:1461 -- Using address 10.84.1.61:6379 set in the environment variable RAY_ADDRESS
         2024-10-16 12:21:46,327 INFO worker.py:1601 -- Connecting to existing Ray cluster at address: 10.84.1.61:6379...
         2024-10-16 12:21:46,333 INFO worker.py:1777 -- Connected to Ray cluster. View the dashboard at 10.84.1.61:8265
         ['TPU cores:16', 'TPU cores:16', 'TPU cores:16', 'TPU cores:16']
         2024-10-16 12:22:12,156 SUCC cli.py:63 -- ---------------------------------
         2024-10-16 12:22:12,156 SUCC cli.py:64 -- Job 'v6e-16-job-z44s7' succeeded
         2024-10-16 12:22:12,156 SUCC cli.py:65 -- ---------------------------------
         




## View the RayJob in the Ray Dashboard

Verify that GKE created the RayCluster service, and also connect to the RayCluster instance.

### Single-host

  1. Retrieve the name of the generated RayCluster for the RayJob:
         
         export RAYCLUSTER_NAME=$(kubectl get rayjob v6e-4-job -o jsonpath='{.status.rayClusterName}')
         

  2. Retrieve the name of the RayCluster head service:
         
         export HEAD_SVC=$(kubectl get svc -l ray.io/cluster=$RAYCLUSTER_NAME,ray.io/node-type=head -o jsonpath='{.items[0].metadata.name}')
         

  3. Connect to the Ray Dashboard by port-forwarding the head service:
         
         kubectl port-forward svc/$HEAD_SVC 8265:8265 2>&1 >/dev/null &
         

  4. Open a web browser and enter the following URL:
         
         http://localhost:8265/#/jobs
         

  5. View the RayJob status and relevant logs.




### Multi-host

  1. Retrieve the name of the generated RayCluster for the RayJob:
         
         export RAYCLUSTER_NAME=$(kubectl get rayjob v6e-16-job -o jsonpath='{.status.rayClusterName}')
         

  2. Retrieve the name of the RayCluster head service:
         
         export HEAD_SVC=$(kubectl get svc -l ray.io/cluster=$RAYCLUSTER_NAME,ray.io/node-type=head -o jsonpath='{.items[0].metadata.name}')
         

  3. Connect to the Ray Dashboard by port-forwarding the head service:
         
         kubectl port-forward svc/$HEAD_SVC 8265:8265 2>&1 >/dev/null &
         

  4. Open a web browser and enter the following URL:
         
         http://localhost:8265/#/jobs
         

  5. View the RayJob status and relevant logs.




Ray sets a `TPU-{accelerator}-Head` resource to identify the Ray worker node that corresponds to the `TPU_WORKER_ID=0` value. In the multi-host TPU group, the Ray node with `TPU_WORKER_ID=0` has `TPU-v6e-16-head: 1.0` set in its resources. This `TPU_WORKER_ID` environment variable is set by a mutating GKE webhook for KubeRay.

**Success:** You've successfully run a RayJob on a TPU slice node pool that runs TPU Trillium. The RayJob's completion indicates that Jax successfully initialized and the distributed TPU nodes are correctly enabled.

## Clean up

After you complete the tutorial, to prevent unwanted charges incurring on your account, delete the RayJob:

### Single-host
    
    
    kubectl delete rayjobs v6e-4-job
    

### Multi-host
    
    
    kubectl delete rayjobs v6e-16-job
    

## What's next

  * Learn about [Ray on Kubernetes](https://docs.ray.io/en/latest/cluster/kubernetes/index.html).
  * Learn how to [Serve vLLM on GKE with TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-vllm-tpu).
  * Learn how to [Serve SDXL on GKE with TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-sdxl-tpu).
  * Learn more [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
