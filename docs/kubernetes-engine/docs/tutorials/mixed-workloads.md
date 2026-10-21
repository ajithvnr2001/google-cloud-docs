---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/mixed-workloads/
title: Optimize GKE resource utilization for mixed AI/ML training and inference workloads \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:27.906151+00:00
---

# Optimize GKE resource utilization for mixed AI/ML training and inference workloads  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/mixed-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Optimize GKE resource utilization for mixed AI/ML training and inference workloads Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode) [ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This tutorial shows you how to efficiently share accelerator resources between training- and inference-serving workloads within a single Google Kubernetes Engine (GKE) cluster. By distributing your mixed workloads across a single cluster, you improve resource utilization, simplify cluster management, reduce issues from accelerator quantity limitations, and enhance overall cost-effectiveness.

In this tutorial, you create a high-priority serving Deployment using the [Gemma 2](https://huggingface.co/google/gemma-2-9b-it) large language model (LLM) for inference and the [Hugging Face TGI](https://huggingface.co/docs/text-generation-inference/en/index) (Text Generation Interface) serving framework, along with a low-priority LLM fine-tuning Job. Both workloads run on a single cluster that uses NVIDIA L4 GPUs. You use [Kueue](https://kueue.sigs.k8s.io/), an open source Kubernetes-native Job queueing system, to manage and schedule your workloads. Kueue lets you prioritize serving tasks and preempt lower-priority training Jobs to optimize resource utilization. As serving demands decrease, you reallocate the freed-up accelerators to resume training Jobs. You use Kueue and priority classes to manage resource quotas throughout the process.

This tutorial is intended for Machine learning (ML) engineers, Platform admins and operators, and Data and AI specialists who want to train and host a machine learning (ML) model on a GKE cluster, and who also want to reduce costs and management overhead, especially when dealing with a limited number of accelerators. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/anthos/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with the following:

  * [Current GPU version availability](https://docs.cloud.google.com/compute/docs/gpus)
  * [GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus)



## Objectives

By the end of this guide, you should be able to perform the following steps:

  * Configure a high-priority serving Deployment.
  * Set up lower-priority training Jobs.
  * Implement preemption strategies to address varying demand.
  * Manage resource allocation between training and serving tasks using Kueue.



## Before you begin

  * Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Enable the required APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,artifactregistry.googleapis.com,iam.googleapis.com)

  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Enable the required APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,artifactregistry.googleapis.com,iam.googleapis.com)

  * Make sure that you have the following role or roles on the project: `roles/container.admin`, `roles/iam.serviceAccountAdmin`

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
  * Ensure your project has sufficient quota for L4 GPUs. To learn more, see [About GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus#gpu-quota) and [Allocation quotas](https://docs.cloud.google.com/compute/resource-usage#gpu_quota).



## Prepare the environment

In this section, you provision the resources that you need to deploy TGI and the model for your inference and training workloads.

### Get access to the model

To get access to the Gemma models for deployment to GKE, you must first sign the license consent agreement, then generate a Hugging Face access token.

  1. **Sign the license consent agreement**. Access the [model consent page](https://www.kaggle.com/models/google/gemma), verify consent using your Hugging Face account, and accept the model terms.
  2. **Generate an access token**. To access the model through Hugging Face, you need a [Hugging Face token](https://huggingface.co/docs/hub/security-tokens). Follow these steps to generate a new token if you don't have one already:

     1. Click **Your Profile > Settings > Access Tokens**.
     2. Select **New Token**.
     3. Specify a Name of your choice and a Role of at least `Read`.
     4. Select **Generate a token**.
     5. Copy the generated token to your clipboard.



### Launch Cloud Shell

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell) to manage resources hosted on Google Cloud. Cloud Shell comes preinstalled with the software you need for this tutorial, including [`kubectl`](https://kubernetes.io/docs/reference/kubectl/), [ gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), and [Terraform](https://docs.cloud.google.com/docs/terraform).

To set up your environment with Cloud Shell, follow these steps:

  1. In the Google Cloud console, launch a Cloud Shell session by clicking ![Cloud Shell activation icon](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg)**Activate Cloud Shell** in the [Google Cloud console](http://console.cloud.google.com). This launches a session in the bottom pane of Google Cloud console.

  2. Set the default environment variables:
         
         gcloud config set project PROJECT_ID
         export PROJECT_ID=$(gcloud config get project)
         

Replace PROJECT_ID with your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  3. Clone the sample code from GitHub. In Cloud Shell, run the following commands:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/
         cd kubernetes-engine-samples/ai-ml/mix-train-and-inference
         export EXAMPLE_HOME=$(pwd)
         




### Create a GKE cluster

You can use an Autopilot or Standard cluster for your mixed workloads. We recommend that you use an Autopilot cluster for a fully managed Kubernetes experience. To choose the GKE mode of operation that's the best fit for your workloads, see [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

### Autopilot

  1. Set the default environment variables in Cloud Shell:
         
         export HF_TOKEN=HF_TOKEN
         export REGION=REGION
         export CLUSTER_NAME="llm-cluster"
         export PROJECT_NUMBER=$(gcloud projects list \
             --filter="$(gcloud config get-value project)" \
             --format="value(PROJECT_NUMBER)")
         export MODEL_BUCKET="model-bucket-$PROJECT_ID"
         

Replace the following values:

     * HF_TOKEN: the Hugging Face token you generated earlier.
     * REGION: a region that supports the accelerator type you want to use, for example, `us-central1` for the L4 GPU.

You can adjust the MODEL_BUCKET variable—this represents the Cloud Storage bucket where you store your trained model weights.

  2. Create an Autopilot cluster:
         
         gcloud container clusters create-auto ${CLUSTER_NAME} \
             --project=${PROJECT_ID} \
             --location=${REGION} \
             --release-channel=rapid
         

  3. Create the Cloud Storage bucket for the fine-tuning job:
         
         gcloud storage buckets create gs://${MODEL_BUCKET} \
             --location ${REGION} \
             --uniform-bucket-level-access
         

  4. To grant access to the Cloud Storage bucket, run this command:
         
         gcloud storage buckets add-iam-policy-binding "gs://$MODEL_BUCKET" \
             --role=roles/storage.objectAdmin \
             --member=principal://iam.googleapis.com/projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/$PROJECT_ID.svc.id.goog/subject/ns/llm/sa/default \
             --condition=None
         

  5. To get authentication credentials for the cluster, run this command:
         
         gcloud container clusters get-credentials llm-cluster \
             --location=$REGION \
             --project=$PROJECT_ID
         

  6. Create a namespace for your Deployments. In Cloud Shell, run the following command:
         
         kubectl create ns llm
         




### Standard

  1. Set the default environment variables in Cloud Shell:
         
         export HF_TOKEN=HF_TOKEN
         export REGION=REGION
         export CLUSTER_NAME="llm-cluster"
         export GPU_POOL_MACHINE_TYPE="g2-standard-24"
         export GPU_POOL_ACCELERATOR_TYPE="nvidia-l4"
         export PROJECT_NUMBER=$(gcloud projects list \
             --filter="$(gcloud config get-value project)" \
             --format="value(PROJECT_NUMBER)")
         export MODEL_BUCKET="model-bucket-$PROJECT_ID"
         

Replace the following values:

     * HF_TOKEN: the Hugging Face token you generated earlier.
     * REGION: the region that supports the accelerator type you want to use, for example, `us-central1` for the L4 GPU.

You can adjust these variables:

     * GPU_POOL_MACHINE_TYPE: the node pool machine series that you want to use in your selected region. This value depends on the accelerator type you selected. To learn more, see [Limitations of using GPUs on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#limitations). For example, this tutorial uses `g2-standard-24` with two GPUs attached per node. For the most up-to-date list of available GPUs, see [GPUs for Compute Workloads](https://docs.cloud.google.com/compute/docs/gpus#gpus_for_compute_workloads).
     * GPU_POOL_ACCELERATOR_TYPE: the accelerator type that's supported in your selected region. For example, this tutorial uses `nvidia-l4`. For the latest list of available GPUs, see [GPUs for Compute Workloads](https://docs.cloud.google.com/compute/docs/gpus#gpus_for_compute_workloads).
     * MODEL_BUCKET: the Cloud Storage bucket where you store your trained model weights.
  2. Create a Standard cluster:
         
         gcloud container clusters create ${CLUSTER_NAME} \
             --project=${PROJECT_ID} \
             --location=${REGION} \
             --workload-pool=${PROJECT_ID}.svc.id.goog \
             --release-channel=rapid \
             --machine-type=e2-standard-4 \
             --addons GcsFuseCsiDriver \
             --num-nodes=1
         

  3. Create the GPU node pool for inference and fine-tuning workloads:
         
         gcloud container node-pools create gpupool \
             --accelerator type=${GPU_POOL_ACCELERATOR_TYPE},count=2,gpu-driver-version=latest \
             --project=${PROJECT_ID} \
             --location=${REGION} \
             --node-locations=${REGION}-a \
             --cluster=${CLUSTER_NAME} \
             --machine-type=${GPU_POOL_MACHINE_TYPE} \
             --num-nodes=3
         

  4. Create the Cloud Storage bucket for the fine-tuning job:
         
         gcloud storage buckets create gs://${MODEL_BUCKET} \
             --location ${REGION} \
             --uniform-bucket-level-access
         

  5. To grant access to the Cloud Storage bucket, run this command:
         
         gcloud storage buckets add-iam-policy-binding "gs://$MODEL_BUCKET" \
             --role=roles/storage.objectAdmin \
             --member=principal://iam.googleapis.com/projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/$PROJECT_ID.svc.id.goog/subject/ns/llm/sa/default \
             --condition=None
         

  6. To get authentication credentials for the cluster, run this command:
         
         gcloud container clusters get-credentials llm-cluster \
             --location=$REGION \
             --project=$PROJECT_ID
         

  7. Create a namespace for your Deployments. In Cloud Shell, run the following command:
         
         kubectl create ns llm
         




### Create a Kubernetes Secret for Hugging Face credentials

To create a Kubernetes Secret that contains the Hugging Face token, run the following command:
    
    
    kubectl create secret generic hf-secret \
        --from-literal=hf_api_token=$HF_TOKEN \
        --dry-run=client -o yaml | kubectl apply --namespace=llm --filename=-
    

## Configure Kueue

In this tutorial, Kueue is the central resource manager, enabling efficient sharing of GPUs between your training and serving workloads. Kueue achieves this by defining resource requirements ("flavors"), prioritizing workloads through queues (with serving tasks prioritized over training), and dynamically allocating resources based on demand and priority. This tutorial uses the [Workload](https://kueue.sigs.k8s.io/docs/concepts/workload/) resource type to group the inference and fine-tuning workloads, respectively.

Kueue's preemption feature ensures that high-priority serving workloads always have the necessary resources by pausing or evicting lower-priority training Jobs when resources are scarce.

To control the inference server Deployment with Kueue, you enable `pod` integration and configure `managedJobsNamespaceSelector` to exclude the `kube-system` and `kueue-system` namespaces.

  1. In the `/kueue` directory, view the code in `kustomization.yaml`. This manifest installs the Kueue resource manager with custom configurations.
         
         apiVersion: kustomize.config.k8s.io/v1beta1
         kind: Kustomization
         resources:
         - https://github.com/kubernetes-sigs/kueue/releases/download/v0.12.3/manifests.yaml
         patches:
         - path: patch.yaml
           target:
             version: v1
             kind: ConfigMap
             name: kueue-manager-config
         

  2. In the `/kueue` directory, view the code in `patch.yaml`. This ConfigMap customizes Kueue to exclude management of Pods in the `kube-system` and `kueue-system` namespaces.
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: kueue-manager-config
         data:
           controller_manager_config.yaml: |
             apiVersion: config.kueue.x-k8s.io/v1beta1
             kind: Configuration
             health:
               healthProbeBindAddress: :8081
             metrics:
               bindAddress: :8080
             # enableClusterQueueResources: true
             webhook:
               port: 9443
             leaderElection:
               leaderElect: true
               resourceName: c1f6bfd2.kueue.x-k8s.io
             controller:
               groupKindConcurrency:
                 Job.batch: 5
                 Pod: 5
                 Workload.kueue.x-k8s.io: 5
                 LocalQueue.kueue.x-k8s.io: 1
                 ClusterQueue.kueue.x-k8s.io: 1
                 ResourceFlavor.kueue.x-k8s.io: 1
             clientConnection:
               qps: 50
               burst: 100
             #pprofBindAddress: :8083
             #waitForPodsReady:
             #  enable: false
             #  timeout: 5m
             #  blockAdmission: false
             #  requeuingStrategy:
             #    timestamp: Eviction
             #    backoffLimitCount: null # null indicates infinite requeuing
             #    backoffBaseSeconds: 60
             #    backoffMaxSeconds: 3600
             #manageJobsWithoutQueueName: true
             managedJobsNamespaceSelector:
               matchExpressions:
                 - key: kubernetes.io/metadata.name
                   operator: NotIn
                   values: [ kube-system, kueue-system ]
             #internalCertManagement:
             #  enable: false
             #  webhookServiceName: ""
             #  webhookSecretName: ""
             integrations:
               frameworks:
               - "batch/job"
               - "kubeflow.org/mpijob"
               - "ray.io/rayjob"
               - "ray.io/raycluster"
               - "jobset.x-k8s.io/jobset"
               - "kubeflow.org/paddlejob"
               - "kubeflow.org/pytorchjob"
               - "kubeflow.org/tfjob"
               - "kubeflow.org/xgboostjob"
               - "kubeflow.org/jaxjob"
               - "workload.codeflare.dev/appwrapper"
               - "pod"
             #  - "deployment" # requires enabling pod integration
             #  - "statefulset" # requires enabling pod integration
             #  - "leaderworkerset.x-k8s.io/leaderworkerset" # requires enabling pod integration
             #  externalFrameworks:
             #  - "Foo.v1.example.com"
             #fairSharing:
             #  enable: true
             #  preemptionStrategies: [LessThanOrEqualToFinalShare, LessThanInitialShare]
             #admissionFairSharing:
             #  usageHalfLifeTime: "168h" # 7 days
             #  usageSamplingInterval: "5m"
             #  resourceWeights: # optional, defaults to 1 for all resources if not specified
             #    cpu: 0    # if you want to completely ignore cpu usage
             #    memory: 0 # ignore completely memory usage
             #    example.com/gpu: 100 # and you care only about GPUs usage
             #resources:
             #  excludeResourcePrefixes: []
             #  transformations:
             #  - input: nvidia.com/mig-4g.5gb
             #    strategy: Replace | Retain
             #    outputs:
             #      example.com/accelerator-memory: 5Gi
             #      example.com/accelerator-gpc: 4
             #objectRetentionPolicies:
             #  workloads:
             #    afterFinished: null # null indicates infinite retention, 0s means no retention at all
             #    afterDeactivatedByKueue: null # null indicates infinite retention, 0s means no retention at all
         

  3. In Cloud Shell, run the following command to install Kueue:
         
         cd ${EXAMPLE_HOME}
         kubectl kustomize kueue |kubectl apply --server-side --filename=-
         

Wait until the Kueue Pods are ready:
         
         watch kubectl --namespace=kueue-system get pods
         

The output should look similar to the following:
         
         NAME                                        READY   STATUS    RESTARTS   AGE
         kueue-controller-manager-bdc956fc4-vhcmx    1/1     Running   0          3m15s
         

  4. In the `/workloads` directory, view the `flavors.yaml`, `cluster-queue.yaml`, and `local-queue.yaml` files. These manifests specify how Kueue manages resource quotas:

### ResourceFlavor

This manifest defines a default [ResourceFlavor](https://kueue.sigs.k8s.io/docs/concepts/resource_flavor/) in Kueue for resource management.
         
         apiVersion: kueue.x-k8s.io/v1beta1
         kind: ResourceFlavor
         metadata:
           name: default-flavor
         

### ClusterQueue

This manifest sets up a Kueue [ClusterQueue](https://kueue.sigs.k8s.io/docs/concepts/cluster_queue/) with resource limits for CPU, memory, and GPU.

This tutorial uses nodes with two Nvidia L4 GPUs attached, with the corresponding node type of `g2-standard-24`, offering 24 vCPU and 96 GB RAM. The example code shows how to limit your workload's resource usage to a maximum of six GPUs.

The `preemption` field in the ClusterQueue configuration references the PriorityClasses to determine which Pods can be preempted when resources are scarce.
         
         apiVersion: kueue.x-k8s.io/v1beta1
         kind: ClusterQueue
         metadata:
           name: "cluster-queue"
         spec:
           namespaceSelector: {} # match all.
           preemption:
             reclaimWithinCohort: LowerPriority
             withinClusterQueue: LowerPriority
           resourceGroups:
           - coveredResources: [ "cpu", "memory", "nvidia.com/gpu", "ephemeral-storage" ]
             flavors:
             - name: default-flavor
               resources:
               - name: "cpu"
                 nominalQuota: 72
               - name: "memory"
                 nominalQuota: 288Gi
               - name: "nvidia.com/gpu"
                 nominalQuota: 6
               - name: "ephemeral-storage"
                 nominalQuota: 200Gi
         

### LocalQueue

This manifest creates a Kueue [LocalQueue](https://kueue.sigs.k8s.io/docs/concepts/local_queue/) named `lq` in the `llm` namespace.
         
         apiVersion: kueue.x-k8s.io/v1beta1
         kind: LocalQueue
         metadata:
           namespace: llm # LocalQueue under llm namespace 
           name: lq
         spec:
           clusterQueue: cluster-queue # Point to the ClusterQueue
         

  5. View the `default-priorityclass.yaml`, `low-priorityclass.yaml`, and `high-priorityclass.yaml` files. These manifests define the [PriorityClass](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass) objects for Kubernetes scheduling.

### Default priority
         
         apiVersion: scheduling.k8s.io/v1
         kind: PriorityClass
         metadata:
           name: default-priority-nonpreempting
         value: 10
         preemptionPolicy: Never
         globalDefault: true
         description: "This priority class will not cause other pods to be preempted."
         

### Low priority
         
         apiVersion: scheduling.k8s.io/v1
         kind: PriorityClass
         metadata:
           name: low-priority-preempting
         value: 20
         preemptionPolicy: PreemptLowerPriority
         globalDefault: false
         description: "This priority class will cause pods with lower priority to be preempted."
         

### High priority
         
         apiVersion: scheduling.k8s.io/v1
         kind: PriorityClass
         metadata:
           name: high-priority-preempting
         value: 30
         preemptionPolicy: PreemptLowerPriority
         globalDefault: false
         description: "This high priority class will cause other pods to be preempted."
         

  6. Create the Kueue and Kubernetes objects by running these commands to apply the corresponding manifests.
         
         cd ${EXAMPLE_HOME}/workloads
         kubectl apply --filename=flavors.yaml
         kubectl apply --filename=default-priorityclass.yaml
         kubectl apply --filename=high-priorityclass.yaml
         kubectl apply --filename=low-priorityclass.yaml
         kubectl apply --filename=cluster-queue.yaml
         kubectl apply --filename=local-queue.yaml --namespace=llm
         




## Deploy the TGI inference server

In this section, you deploy the TGI container to serve the Gemma 2 model.

  1. In the `/workloads` directory, view the `tgi-gemma-2-9b-it-hp.yaml` file. This manifest defines a Kubernetes Deployment to deploy the TGI serving runtime and `gemma-2-9B-it` model. A _Deployment_ is a Kubernetes API object that lets you run multiple replicas of Pods that are distributed among the nodes in a cluster..

The Deployment prioritizes inference tasks and uses two GPUs for the model. It uses [tensor parallelism](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/llm-optimization#tensor-parallelism), by setting the `NUM_SHARD` environment variable, to fit the model into GPU memory.
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: tgi-gemma-deployment
           labels:
             app: gemma-server
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: gemma-server
           template:
             metadata:
               labels:
                 app: gemma-server
                 ai.gke.io/model: gemma-2-9b-it
                 ai.gke.io/inference-server: text-generation-inference
                 examples.ai.gke.io/source: user-guide
                 kueue.x-k8s.io/queue-name: lq
             spec:
               priorityClassName: high-priority-preempting
               containers:
               - name: inference-server
                 image: us-docker.pkg.dev/deeplearning-platform-release/gcr.io/huggingface-text-generation-inference-cu121.2-1.ubuntu2204.py310
                 resources:
                   requests:
                     cpu: "4"
                     memory: "30Gi"
                     ephemeral-storage: "30Gi"
                     nvidia.com/gpu: "2"
                   limits:
                     cpu: "4"
                     memory: "30Gi"
                     ephemeral-storage: "30Gi"
                     nvidia.com/gpu: "2"
                 env:
                 - name: AIP_HTTP_PORT
                   value: '8000'
                 - name: NUM_SHARD
                   value: '2'
                 - name: MODEL_ID
                   value: google/gemma-2-9b-it
                 - name: HUGGING_FACE_HUB_TOKEN
                   valueFrom:
                     secretKeyRef:
                       name: hf-secret
                       key: hf_api_token
                 volumeMounts:
                 - mountPath: /dev/shm
                   name: dshm
               volumes:
               - name: dshm
                 emptyDir:
                   medium: Memory
               nodeSelector:
                 cloud.google.com/gke-accelerator: "nvidia-l4"
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: llm-service
         spec:
           selector:
             app: gemma-server
           type: ClusterIP
           ports:
           - protocol: TCP
             port: 8000
             targetPort: 8000
         

  2. Apply the manifest by running the following command:
         
         kubectl apply --filename=tgi-gemma-2-9b-it-hp.yaml --namespace=llm
         

The deployment operation will take a few minutes to complete.

  3. To check if GKE successfully created the Deployment, run the following command:
         
         kubectl --namespace=llm get deployment
         

The output should look similar to the following:
         
         NAME                   READY   UP-TO-DATE   AVAILABLE   AGE
         tgi-gemma-deployment   1/1     1            1           5m13s
         




## Verify Kueue quota management

In this section, you confirm that Kueue is correctly enforcing the GPU quota for your Deployment.

  1. To check if Kueue is aware of your Deployment, run this command to retrieve the status of the Workload objects:
         
         kubectl --namespace=llm get workloads
         

The output should look similar to the following:
         
         NAME                                              QUEUE   RESERVED IN     ADMITTED   FINISHED   AGE
         pod-tgi-gemma-deployment-6bf9ffdc9b-zcfrh-84f19   lq      cluster-queue   True                  8m23s
         

  2. To test overriding the quota limits, scale the Deployment to four replicas:
         
         kubectl scale --replicas=4 deployment/tgi-gemma-deployment --namespace=llm
         

  3. Run the following command to see the number of replicas that GKE deploys:
         
         kubectl get workloads --namespace=llm
         

The output should look similar to the following:
         
         NAME                                              QUEUE   RESERVED IN     ADMITTED   FINISHED   AGE
         pod-tgi-gemma-deployment-6cb95cc7f5-5thgr-3f7d4   lq      cluster-queue   True                  14s
         pod-tgi-gemma-deployment-6cb95cc7f5-cbxg2-d9fe7   lq      cluster-queue   True                  5m41s
         pod-tgi-gemma-deployment-6cb95cc7f5-tznkl-80f6b   lq                                            13s
         pod-tgi-gemma-deployment-6cb95cc7f5-wd4q9-e4302   lq      cluster-queue   True                  13s
         

The output shows that only three Pods are admitted due to the resource quota that Kueue enforces.

  4. Run the following to display the Pods in the `llm` namespace:
         
         kubectl get pod --namespace=llm
         

The output should look similar to the following:
         
         NAME                                    READY   STATUS            RESTARTS   AGE
         tgi-gemma-deployment-7649884d64-6j256   1/1     Running           0          4m45s
         tgi-gemma-deployment-7649884d64-drpvc   0/1     SchedulingGated   0          7s
         tgi-gemma-deployment-7649884d64-thdkq   0/1     Pending           0          7s
         tgi-gemma-deployment-7649884d64-znvpb   0/1     Pending           0          7s
         

  5. Now, scale down the Deployment back to 1. This step is required before deploying the fine-tuning job, otherwise it won't get admitted due to the inference job having priority.
         
         kubectl scale --replicas=1 deployment/tgi-gemma-deployment --namespace=llm
         




### Explanation of the behavior

The scaling example results in only three replicas (despite scaling to four) because of the GPU quota limit that you set in the ClusterQueue configuration. The ClusterQueue's `spec.resourceGroups` section defines a nominalQuota of "6" for `nvidia.com/gpu`. The Deployment specifies that each Pod requires "2" GPUs. Therefore, the ClusterQueue can only accommodate a maximum of three replicas of the Deployment at a time (since 3 replicas * 2 GPUs per replica = 6 GPUs, which is the total quota).

When you attempt to scale to four replicas, Kueue recognizes that this action would exceed the GPU quota and it prevents the fourth replica from being scheduled. This is indicated by the `SchedulingGated` status of the fourth Pod. This behavior demonstrates Kueue's resource quota enforcement.

## Deploy the training Job

In this section, you deploy a lower-priority fine-tuning Job for a Gemma 2 model that requires four GPUs across two Pods. A Job controller in Kubernetes creates one or more Pods and helps ensure that they successfully execute a specific task.

This Job will use the remaining GPU quota in the ClusterQueue. The Job uses a prebuilt image and saves checkpoints to allow restarting from intermediate results.

The fine-tuning Job uses the [`b-mc2/sql-create-context`](https://huggingface.co/datasets/b-mc2/sql-create-context) dataset. The source for the fine-tuning job can be found in the [repository](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/mix-train-and-inference/src).

  1. View the `fine-tune-l4.yaml` file. This manifest defines the fine-tuning Job.
         
         apiVersion: v1
         kind: Service
         metadata:
           name: headless-svc-l4
         spec:
           clusterIP: None # clusterIP must be None to create a headless service
           selector:
             job-name: finetune-gemma-l4 # must match Job name
         ---
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: finetune-gemma-l4
           labels:
             kueue.x-k8s.io/queue-name: lq
         spec:
           backoffLimit: 4
           completions: 2
           parallelism: 2
           completionMode: Indexed
           suspend: true # Set to true to allow Kueue to control the Job when it starts
           template:
             metadata:
               labels:
                 app: finetune-job
               annotations:
                 gke-gcsfuse/volumes: "true"
                 gke-gcsfuse/memory-limit: "35Gi"
             spec:
               priorityClassName: low-priority-preempting
               containers:
               - name: gpu-job
                 imagePullPolicy: Always
                 image: us-docker.pkg.dev/google-samples/containers/gke/gemma-fine-tuning:v1.1.0
                 ports:
                 - containerPort: 29500
                 resources:
                   requests:
                     nvidia.com/gpu: "2"
                   limits:
                     nvidia.com/gpu: "2"
                 command:
                 - bash
                 - -c
                 - |
                   accelerate launch \
                   --config_file fsdp_config.yaml \
                   --debug \
                   --main_process_ip finetune-gemma-l4-0.headless-svc-l4 \
                   --main_process_port 29500 \
                   --machine_rank ${JOB_COMPLETION_INDEX} \
                   --num_processes 4 \
                   --num_machines 2 \
                   fine_tune.py
                 env:
                 - name: "EXPERIMENT"
                   value: "finetune-experiment"
                 - name: MODEL_NAME
                   value: "google/gemma-2-2b"
                 - name: NEW_MODEL
                   value: "gemma-ft"
                 - name: MODEL_PATH
                   value: "/model-data/model-gemma2/experiment"
                 - name: DATASET_NAME
                   value: "b-mc2/sql-create-context"
                 - name: DATASET_LIMIT
                   value: "5000"
                 - name: EPOCHS
                   value: "1"
                 - name: GRADIENT_ACCUMULATION_STEPS
                   value: "2"
                 - name: CHECKPOINT_SAVE_STEPS
                   value: "10"
                 - name: HF_TOKEN
                   valueFrom:
                     secretKeyRef:
                       name: hf-secret
                       key: hf_api_token
                 volumeMounts:
                 - mountPath: /dev/shm
                   name: dshm
                 - name: gcs-fuse-csi-ephemeral
                   mountPath: /model-data
                   readOnly: false
               nodeSelector:
                 cloud.google.com/gke-accelerator: nvidia-l4
               restartPolicy: OnFailure
               serviceAccountName: default
               subdomain: headless-svc-l4
               terminationGracePeriodSeconds: 60
               volumes:
               - name: dshm
                 emptyDir:
                   medium: Memory
               - name: gcs-fuse-csi-ephemeral
                 csi:
                   driver: gcsfuse.csi.storage.gke.io
                   volumeAttributes:
                     bucketName: <MODEL_BUCKET>
                     mountOptions: "implicit-dirs"
                     gcsfuseLoggingSeverity: warning
         

  2. Apply the manifest to create the fine-tuning Job:
         
         cd ${EXAMPLE_HOME}/workloads
         
         sed -e "s/<MODEL_BUCKET>/$MODEL_BUCKET/g" \
             -e "s/<PROJECT_ID>/$PROJECT_ID/g" \
             -e "s/<REGION>/$REGION/g" \
             fine-tune-l4.yaml |kubectl apply --filename=- --namespace=llm
         

  3. Verify that your Deployments are running. To check the status of the Workload objects, run the following command:
         
         kubectl get workloads --namespace=llm
         

The output should look similar to the following:
         
         NAME                                              QUEUE   RESERVED IN     ADMITTED   FINISHED   AGE
         job-finetune-gemma-l4-3316f                       lq      cluster-queue   True                  29m
         pod-tgi-gemma-deployment-6cb95cc7f5-cbxg2-d9fe7   lq      cluster-queue   True                  68m
         

Next, view the Pods in the `llm` namespace by running this command:
         
         kubectl get pod --namespace=llm
         

The output should look similar to the following:
         
         NAME                                    READY   STATUS    RESTARTS   AGE
         finetune-gemma-l4-0-vcxpz               2/2     Running   0          31m
         finetune-gemma-l4-1-9ppt9               2/2     Running   0          31m
         tgi-gemma-deployment-6cb95cc7f5-cbxg2   1/1     Running   0          70m
         

The output shows that Kueue admits both your fine-tune Job and inference server Pods to run, reserving the correct resources based on your specified quota limits.

  4. View the output logs to verify that your fine-tuning Job saves checkpoints to the Cloud Storage bucket. The fine-tuning Job takes around 10 minutes before it starts saving the first checkpoint.
         
         kubectl logs --namespace=llm --follow --selector=app=finetune-job
         

The output for the first saved checkpoint looks similar to the following:
         
         {"name": "finetune", "thread": 133763559483200, "threadName": "MainThread", "processName": "MainProcess", "process": 33, "message": "Fine tuning started", "timestamp": 1731002351.0016131, "level": "INFO", "runtime": 451579.89835739136}
         …
         {"name": "accelerate.utils.fsdp_utils", "thread": 136658669348672, "threadName": "MainThread", "processName": "MainProcess", "process": 32, "message": "Saving model to /model-data/model-gemma2/experiment/checkpoint-10/pytorch_model_fsdp_0", "timestamp": 1731002386.1763802, "level": "INFO", "runtime": 486753.8924217224}
         




## Test Kueue preemption and dynamic allocation on your mixed workload

In this section, you simulate a scenario where the inference server's load increases, requiring it to scale up. This scenario demonstrates how Kueue prioritizes the high-priority inference server by suspending and preempting the lower-priority fine-tuning Job when resources are constrained.

  1. Run the following command to scale the inference server's replicas to two:
         
         kubectl scale --replicas=2 deployment/tgi-gemma-deployment --namespace=llm
         

  2. Check the status of the Workload objects:
         
         kubectl get workloads --namespace=llm
         

The output looks similar to the following:
         
         NAME                                              QUEUE   RESERVED IN     ADMITTED   FINISHED   AGE
         job-finetune-gemma-l4-3316f                       lq                      False                 32m
         pod-tgi-gemma-deployment-6cb95cc7f5-cbxg2-d9fe7   lq      cluster-queue   True                  70m
         pod-tgi-gemma-deployment-6cb95cc7f5-p49sh-167de   lq      cluster-queue   True                  14s
         

The output shows that the fine-tuning Job is no longer admitted because the increased inference server replicas are using the available GPU quota.

  3. Check the status of the fine-tune Job:
         
         kubectl get job --namespace=llm
         

The output looks similar to the following, indicating that the fine-tune Job status is now suspended:
         
         NAME                STATUS      COMPLETIONS   DURATION   AGE
         finetune-gemma-l4   Suspended   0/2                      33m
         

  4. Run the following command to inspect your Pods:
         
         kubectl get pod --namespace=llm
         

The output looks similar to the following, indicating that Kueue terminated the fine-tune Job Pods to free resources for the higher priority inference server Deployment.
         
         NAME                                    READY   STATUS              RESTARTS   AGE
         tgi-gemma-deployment-6cb95cc7f5-cbxg2   1/1     Running             0          72m
         tgi-gemma-deployment-6cb95cc7f5-p49sh   0/1     ContainerCreating   0          91s
         

  5. Next, test the scenario where the inference server load decreases and its Pods scale down. Run the following command:
         
         kubectl scale --replicas=1 deployment/tgi-gemma-deployment --namespace=llm
         

Run the following command to display the Workload objects:
         
         kubectl get workloads --namespace=llm
         

The output looks similar to the following, indicating that one of the inference server Deployments is terminated, and the fine-tune Job is re-admitted.
         
         NAME                                              QUEUE   RESERVED IN     ADMITTED   FINISHED   AGE
         job-finetune-gemma-l4-3316f                       lq      cluster-queue   True                  37m
         pod-tgi-gemma-deployment-6cb95cc7f5-cbxg2-d9fe7   lq      cluster-queue   True                  75m
         

  6. Run this command to display the Jobs:
         
         kubectl get job --namespace=llm
         

The output looks similar to the following, indicating that the fine-tune Job is running again, resuming from the latest available checkpoint.
         
         NAME                STATUS    COMPLETIONS   DURATION   AGE
         finetune-gemma-l4   Running   0/2           2m11s      38m
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the deployed resources

To avoid incurring charges to your Google Cloud account for the resources that you created in this guide, run the following commands:
    
    
    gcloud storage rm --recursive gs://${MODEL_BUCKET}
    gcloud container clusters delete ${CLUSTER_NAME} --location ${REGION}
    

## What's next

  * [Learn the best practices for autoscaling LLM inference workloads with GPUs on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling).
  * [Learn the best practices for optimizing LLM inference serving with GPUs on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/llm-optimization#tensor-parallelism).
  * [Learn best practices for running batch workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/batch-platform-on-gke).
  * [Learn best practices for optimizing AI/ML workload prioritization on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/optimize-ai-utilization).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
