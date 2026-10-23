---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/quickstarts/ray-gpu-cluster/
title: Quickstart: Deploy GPU-accelerated Ray for AI workloads on GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:43.590791+00:00
---

# Quickstart: Deploy GPU-accelerated Ray for AI workloads on GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/quickstarts/ray-gpu-cluster/




Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy GPU-accelerated Ray for AI workloads on GKE

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to set up and run a GPU-enabled [Ray](https://docs.ray.io/en/latest/ray-overview/index.html) cluster on Google Kubernetes Engine (GKE) to scale your AI/ML workloads.

## Why use Ray?

Using Ray on GKE, facilitated by [KubeRay](https://docs.ray.io/en/latest/cluster/kubernetes/index.html), lets you scale Python and AI applications. Ray handles the application scaling, and GKE manages the underlying servers and resources.

This combination makes it easier to manage resources, automatically adjust capacity, ensure reliability, and deploy your applications across various environments. By connecting your distributed Ray applications with your existing cloud infrastructure and tools on GKE, you can simplify operations and provision a robust, scalable platform for complex tasks by using standard Kubernetes methods.

For more information, see the blog post [Why GKE for your Ray AI workloads](https://cloud.google.com/blog/products/containers-kubernetes/the-benefits-of-using-gke-for-running-ray-ai-workloads).

## Before you begin

Before you start, make sure you have performed the following tasks:

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the GKE API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. Configure the gcloud CLI to use your federated identity.

For more information, see [ Sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. **Install`kubectl`**: `kubectl` is the primary command line tool for interacting with GKE clusters. If you use Cloud Shell, `kubectl` is already installed. Otherwise, install it in your terminal by running the `gcloud components install kubectl` command. 

To verify your installation, run this command: `kubectl version --client`

  8. **Install Ray** : we highly recommend that you create and enter a Python virtual environment (`venv`) before you install Ray so that you can isolate its dependencies. 
     1. [Install Python](https://docs.cloud.google.com/python/docs/setup#installing_python).
     2. [Create and activate a new virtual environment](https://docs.cloud.google.com/python/docs/setup#installing_and_using_virtualenv).
     3. Install the latest stable version of Ray by running this command inside your virtual environment: `pip install -U "ray[default]"`.
     4. To verify your installation, run this command: `ray --version`. Note the Ray version (for example, 2.44.1) in the output.
  9. Ensure your Google Cloud project has sufficient quota for L4 GPUs. For more information, see [About GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus) and [Allocation quotas](https://docs.cloud.google.com/compute/resource-usage#gpu_quota).



## Create a GKE cluster

You can deploy your workload in a GKE Autopilot or Standard cluster. We recommend that you use an Autopilot cluster for a fully managed Kubernetes experience. To choose the GKE mode of operation that's the best fit for your workloads, see [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

### Autopilot

In [Autopilot mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview), Google manages your cluster configuration, including scaling, security, and other preconfigured settings. Autopilot clusters are optimized to run most production workloads and provision compute resources based on your Kubernetes manifests.

  1. In the terminal, run the following [`gcloud container clusters create-auto`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto) command:
         
         gcloud container clusters create-auto my-ray-enabled-cluster \
             --enable-ray-operator \
             --enable-ray-cluster-monitoring \
             --enable-ray-cluster-logging \
             --location=us-central1
         

This Google Cloud CLI command creates an Autopilot cluster named `my-ray-enabled-cluster`, with these settings:

     * `--enable-ray-operator`: installs the Ray Operator on the cluster, which simplifies managing Ray clusters within Kubernetes.
     * `--enable-ray-cluster-monitoring`: sets up integration with Cloud Monitoring for Ray cluster metrics.
     * `--enable-ray-cluster-logging`: configures integration with Cloud Logging to collect logs from your Ray cluster.
     * `--location=us-central1`: specifies the geographical region where the GKE cluster will be created. Be aware that accelerator availability and supported types vary by location. For more information, see [GPU regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).

Autopilot clusters automatically [provisions and scales nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning) (including GPU-enabled ones that use compute classes) based on workload demands, optimizing both utilization and cost. This automatic provisioning and scaling of resources in Autopilot clusters simplifies resource management, and lets you focus on your models instead of infrastructure.

If you use a GKE Standard cluster, the flags and settings for enabling Ray might be different. For more information, see [Enable the Ray Operator on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/enable-ray-on-gke).

  2. Configure `kubectl` to communicate with your cluster:
         
         gcloud container clusters get-credentials my-ray-enabled-cluster \
             --location=us-central1
         




### Standard

In [Standard mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode#why-standard), you have more control over the underlying infrastructure of your GKE cluster. You manage node pools, node sizes, and other configurations directly, allowing for greater customization. Standard clusters are suitable for workloads that need specific configurations or tight control over resources.

  1. In the terminal, run the following [`gcloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create) command:
         
         gcloud container clusters create my-ray-enabled-cluster \
             --addons=RayOperator \
             --enable-ray-cluster-monitoring \
             --enable-ray-cluster-logging \
             --location=us-central1 \
             --enable-autoprovisioning \
             --max-cpu=10 \
             --max-memory=64
         

This Google Cloud CLI command creates an Standard cluster named `my-ray-enabled-cluster`, with these settings:

     * `--addons=RayOperator`: installs the Ray Operator on the cluster, which simplifies managing Ray clusters within Kubernetes.
     * `--enable-ray-cluster-monitoring`: sets up integration with Cloud Monitoring for Ray cluster metrics.
     * `--enable-ray-cluster-logging`: configures integration with Cloud Logging to collect logs from your Ray cluster.
     * `--location=us-central1`: specifies the geographical region where the GKE cluster will be created. Be aware that accelerator availability and supported types vary by location. For more information, see [GPU regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).
     * `--enable-autoprovisioning`: automatically creates and deletes [node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) and scale nodes within those pools based on your workload's demands.
     * `--max-cpu`: maximum number of cores to which the cluster can scale.
     * `--max-memory`: maximum number of gigabytes of memory to which the cluster can scale.
  2. Configure `kubectl` to communicate with your cluster:
         
         gcloud container clusters get-credentials my-ray-enabled-cluster \
             --location=us-central1
         




## Install the KubeRay `kubectl ray` plugin

The `kubectl ray` plugin simplifies common Ray on Kubernetes workflows. For the latest installation instructions, see the [KubeRay documentation](https://docs.ray.io/en/latest/cluster/kubernetes/user-guides/kubectl-plugin.html).

  1. Go to the [releases page](https://github.com/ray-project/kuberay/releases/tag/v1.3.2) and download the binary for your platform. For example, to install `kubectl ray` plugin version 1.3.2 on Linux amd64, run the following commands:
         
         curl -LO https://github.com/ray-project/kuberay/releases/download/v1.3.2/kubectl-ray_v1.3.2_linux_amd64.tar.gz
         tar -xvf kubectl-ray_v1.3.2_linux_amd64.tar.gz
         cp kubectl-ray ~/.local/bin
         

Replace `~/.local/bin` with the directory in your `PATH`.

  2. Verify your installation:
         
         kubectl ray version
         

If you see a warning like `KubeRay operator installation cannot be found: no KubeRay operator deployments found in any namespace.`, you can safely ignore it. If the installation was successful, the output is the version of the `kubectl ray` plugin.




## Create the custom compute class in your cluster

A [custom compute class](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) in GKE lets you define specific hardware requirements, like the GPU type and count, by priority. GKE uses this priority when provisioning nodes for your workloads.

To create the example custom compute class for this guide, follow these steps:

  1. Save the following compute class specification as `nvidia-l4-compute-class.yaml`:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: gpu-compute-class
         spec:
           priorities:
           - gpu:
               type: nvidia-l4
               count: 1
             spot: true
           - gpu:
               type: nvidia-l4
               count: 1
             spot: false
           nodePoolAutoCreation:
             enabled: true
           whenUnsatisfiable: DoNotScaleUp
         

  2. Create the compute class by by running this command:
         
         kubectl apply -f nvidia-l4-compute-class.yaml
         

**What happens after you apply the custom compute class?** After applying the compute class YAML file, GKE will automatically provision nodes with one NVIDIA L4 GPU when your Ray cluster requests them. It will prioritize Spot VMs as defined in your manifest. The `whenUnsatisfiable: DoNotScaleUp` setting instructs GKE to not create nodes that don't meet the specified requirements.




## Create and verify the Ray cluster

You can now create your [Ray cluster](https://docs.ray.io/en/latest/cluster/key-concepts.html#ray-cluster) on your GKE cluster.

  1. **Create the Ray cluster**. Use the `kubectl ray create cluster` command to define and create your Ray cluster. This command simplifies the process by handling the underlying Kubernetes resource creation.
         
         kubectl ray create cluster my-ray-cluster \
               --worker-replicas=1 \
               --worker-cpu=2 \
               --worker-memory=4Gi \
               --worker-gpu=1 \
               --worker-node-selectors="cloud.google.com/compute-class=gpu-compute-class"
         

The `kubectl ray create cluster` command uses the KubeRay plugin to translate your specifications into a [RayCluster](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview#raycluster) custom resource definition and sends it to the Kubernetes API to create the RayCluster object. This object acts as a blueprint, telling the Ray Operator how to provision and manage the actual Ray cluster components (head and worker nodes) within GKE. By default, GKE schedules the head Pod on a node from the E2 machine series.

The example command uses these settings:

     * `kubectl ray create cluster my-ray-cluster`: specifies the name of the Ray cluster you want to create.
     * `--worker-node-selectors`: tells Kubernetes to schedule worker Pods on nodes that are labeled with `cloud.google.com/compute-class=gpu-compute-class`.
**Important:** For best results, use the `--ray-version` flag with the `kubectl ray create cluster` command to match your local Ray and Python versions with the corresponding versions in the Ray cluster. Keeping versions closely aligned generally improves stability.
  2. **Verify the Ray cluster status**. Use these commands to verify that your Ray cluster is up and running.

     * Check the RayCluster resource by running this command:
           
           kubectl ray get cluster
           

This command lists all the Ray clusters in your Kubernetes namespace. You should see `my-ray-cluster` listed. It might take a few minutes for the cluster to initialize.

     * Check the Kubernetes Pods by running this command:
           
           kubectl get pods
           

This command lists all the Pods that are running in your Kubernetes namespace. You should see Pods related to your Ray cluster:

       * A Pod for the Ray head node, with a name like `my-ray-cluster-head-0`.
       * One or more Pods for the Ray worker nodes, with names like `my-ray-cluster-worker-group-0-xxxxx`. The number of worker Pods depends on the initial configuration of your Ray cluster and any autoscaling that might have occurred.



## Submit a Ray job

After your Ray cluster is ready, you can submit a Ray job to your running Ray cluster on GKE.

To do this, use the `kubectl ray session` command to start an interactive session, and the `ray job submit` command to start job execution.

  1. **Start a Ray interactive session**. To establish a local connection to your Ray cluster, run this command:
         
         kubectl ray session my-ray-cluster
         

This command initiates port forwarding between your local machine and the Ray head node in your GKE cluster. Note that your terminal will be occupied while this session is active; to proceed, open a separate terminal instance.

  2. **Create the sample code to run**. Save the following example code to a file named `sample_code.py`.

**Tip:** For training and deploying your actual AI/ML models in production, you would substitute this basic example with Python code that utilizes libraries such as PyTorch or TensorFlow. For a more comprehensive PyTorch training example, see [pytorch-mnist/train.py](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/gke-ray/raytrain/pytorch-mnist/train.py).
         
         import ray
           import os
           import requests
         
           ray.init()
         
           @ray.remote
           class Counter:
               def __init__(self):
                   # Used to verify runtimeEnv
                   self.name = os.getenv("counter_name")
                   assert self.name == "test_counter"
                   self.counter = 0
         
               def inc(self):
                   self.counter += 1
         
               def get_counter(self):
                   return "{} got {}".format(self.name, self.counter)
         
           counter = Counter.remote()
         
           for _ in range(5):
                   ray.get(counter.inc.remote())
                   print(ray.get(counter.get_counter.remote()))
         
           # Verify that the correct runtime env was used for the job.
           assert requests.__version__ == "2.26.0"
         

  3. **Open a new terminal and submit the Ray job**.

     1. Open a new terminal on your local machine. If you created a virtual environment for your Ray installation, ensure you activate it in this new terminal as well.
     2. Navigate to the directory where you saved the `sample_code.py` file.
     3. Run the following command:
            
            ray job submit \
                  --working-dir=. \
                  --runtime-env-json='{"pip": ["requests==2.26.0"], "env_vars": {"counter_name": "test_counter"}}' \
                  --address http://localhost:8265 python sample_code.py
            

The example command uses these settings:

        * `--working-dir=.`: specifies the current directory as the working directory to be made available to the Ray job on the cluster. Ideally, this directory contains just the application source code you want to run on Ray. In our example, this is the `sample_code.py` file.
        * `--runtime-env-json='{"pip": ["requests==2.26.0"], "env_vars": {"counter_name": "test_counter"}}'`: defines the runtime environment for the job. It specifies the required Python library version (`requests==2.26.0`) and sets an environment variable (`counter_name`) for the job's execution.
  4. **View the Ray job**. You can monitor the job in one of these ways:

     * **Ray dashboard** : open your web browser and go to `http://localhost:8265`. This URL opens the Ray dashboard, where you can see information about your running job, including its status, logs, and resource usage.
     * **Metrics Explorer** : use the prebuilt metrics dashboards in the Google Cloud console. For more information, see [Collect and view logs and metrics for Ray clusters on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/collect-view-logs-metrics).
  5. **Terminate the Ray session**. After you finish interacting with the Ray cluster or monitoring your job, you can terminate the interactive session by pressing `Ctrl+C` in the terminal where you ran the `kubectl ray session` command.


**Success:** Congratulations on deploying your first Ray job on GKE!

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

If you deployed the quickstart in a new Google Cloud project, and if you no longer need the project, delete it by completing the following steps:

  1. In the Google Cloud console, go to the [Manage resources page](https://console.cloud.google.com/iam-admin/projects).
  2. In the project list, select the project that you want to delete, and then click **Delete**.
  3. In the dialog, enter the project ID, and the click **Shut down** to delete the project.



If you did not create a new Google Cloud project, and if you no longer need the GKE cluster, you can delete it by running this command:
    
    
    gcloud container clusters delete my-ray-enabled-cluster \
        --location=us-central1
    

## What's next

  * **Explore additional examples, best practices, and tools for Ray on GKE:** For more information, see the [ai-on-gke GitHub](https://github.com/GoogleCloudPlatform/ai-on-gke/tree/main/ray-on-gke) repository.
  * **Learn more about using accelerators on GKE** : Use [GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus) for parallel processing in machine learning and data analytics tasks. Use [TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus) for accelerating large-scale deep learning model training and inference.
  * **Learn more about the Ray Operator** : For more information about how to use the Ray Operator to manage Ray Deployments, including Ray jobs, see [About Ray on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview).
  * **Utilize Kueue for job queuing:** Discover how Kueue, a Kubernetes-native job queuing system, can help manage and prioritize your AI/ML workloads, which can improve resource utilization. For more information, see [Optimize GKE resource utilization for mixed AI/ML training and inference workloads](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/mixed-workloads). 



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
