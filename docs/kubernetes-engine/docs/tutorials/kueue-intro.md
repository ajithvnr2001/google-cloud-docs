---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/kueue-intro/
title: Deploy a batch system using Kueue \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:14.337434+00:00
---

# Deploy a batch system using Kueue  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/kueue-intro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Deploy a batch system using Kueue Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial shows you how to optimize available resources by scheduling [Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/) on Google Kubernetes Engine (GKE) with [Kueue](https://kueue.sigs.k8s.io). In this tutorial, you learn to use Kueue to effectively manage and schedule batch jobs, improve resource utilization, and simplify workload management. You set up a shared cluster for two tenant teams where each team has its own namespace and each team creates Jobs that share global resources. You also configure Kueue to schedule the Jobs based on resource quotas that you define.

This tutorial is for Cloud architects and Platform engineers who are interested in implementing a batch system using GKE. To learn more about common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/anthos/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with the following:

  * [Autopilot mode and Standard mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)
  * [GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus)



## Background

Jobs are applications that run to completion, such as machine learning, rendering, simulation, analytics, CI/CD, and similar workloads.

Kueue is a cloud-native Job scheduler that works with the default Kubernetes scheduler, the Job controller, and the cluster autoscaler to provide an end-to-end batch system. Kueue implements Job queueing, deciding when Jobs should wait and when they should start, based on quotas and a hierarchy for sharing resources fairly among teams.

Kueue has the following characteristics:

  * It is optimized for cloud architectures, where resources are heterogeneous, interchangeable, and scalable.
  * It provides a set of APIs to manage elastic quotas and manage Job queueing.
  * It does not re-implement existing capabilities such as autoscaling, pod scheduling, or Job lifecycle management.
  * Kueue has built-in support for the Kubernetes`batch/v1.Job` API.
  * It can integrate with other job APIs.



Kueue refers to jobs defined with any API as Workloads, to avoid the confusion with the specific Kubernetes Job API.

## Objectives

  1. Create a GKE cluster
  2. Create the [ResourceFlavor](https://kueue.sigs.k8s.io/docs/concepts/resource_flavor/)
  3. Create the [ClusterQueue](https://kueue.sigs.k8s.io/docs/concepts/cluster_queue/)
  4. Create the [LocalQueue](https://kueue.sigs.k8s.io/docs/concepts/local_queue/)
  5. Create Jobs and observe the admitted workloads



## Costs

This tutorial uses the following billable components of Google Cloud: 

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing)



Use the [Pricing Calculator](https://cloud.google.com/products/calculator) to generate a cost estimate based on your projected usage.

When you finish this tutorial, avoid continued billing by deleting the resources you created. For more information, see Clean up.

## Before you begin

### Set up your project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, click **Create project** to begin creating a new Google Cloud project.

**Roles required to create a project**

To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the GKE API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  5. In the Google Cloud console, on the project selector page, click **Create project** to begin creating a new Google Cloud project.

**Roles required to create a project**

To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the GKE API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)




### Set defaults for the Google Cloud CLI

  1. In the Google Cloud console, start a Cloud Shell instance:   
[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Download the source code for this sample app:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples
         cd kubernetes-engine-samples/batch/kueue-intro
         

  3. Set the default environment variables:
         
         gcloud config set project PROJECT_ID
         gcloud config set compute/region CONTROL_PLANE_LOCATION
         

Replace the following values:

     * PROJECT_ID: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * CONTROL_PLANE_LOCATION: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.



## Create a GKE cluster

  1. Create a GKE Autopilot cluster named `kueue-autopilot`:
         
         gcloud container clusters create-auto kueue-autopilot \
           --release-channel "rapid" --location CONTROL_PLANE_LOCATION
         

Autopilot clusters are fully managed, and have built-in autoscaling. Learn more about [GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview).

Kueue also supports Standard GKE with Node Auto-provisioning and regular autoscaled node pools.

**Note:** Autopilot cluster creation can take up to five minutes to complete.

The outcome is similar to the following once the cluster is created:
         
         NAME: kueue-autopilot
           LOCATION: us-central1
           MASTER_VERSION: 1.26.2-gke.1000
           MASTER_IP: 35.193.173.228
           MACHINE_TYPE: e2-medium
           NODE_VERSION: 1.26.2-gke.1000
           NUM_NODES: 3
           **STATUS: RUNNING**
         

Where the `STATUS` is `RUNNING` for the `kueue-autopilot`.

  2. Get authentication credentials for the cluster:
         
         gcloud container clusters get-credentials kueue-autopilot
         

  3. Install Kueue on the cluster:
         
         VERSION=VERSION
         kubectl apply --server-side -f \
           https://github.com/kubernetes-sigs/kueue/releases/download/$VERSION/manifests.yaml
         

Replace VERSION with the latest version of Kueue. For more information about Kueue versions, see [Kueue releases](https://github.com/kubernetes-sigs/kueue/releases).

  4. Wait until the Kueue Pods are ready:
         
         watch kubectl -n kueue-system get pods
         

The output should be similar to the following before you can continue:
         
         NAME                                        READY   STATUS    RESTARTS   AGE
         kueue-controller-manager-66d8bb946b-wr2l2   2/2     Running   0          3m36s
         

**Note:** This step may take up to three minutes.
  5. Create two new namespaces called `team-a` and `team-b`:
         
         kubectl create namespace team-a
         kubectl create namespace team-b
         




## Create the ResourceFlavor

A ResourceFlavor is an object that represents the variations in the nodes available in your cluster by associating them with node labels and taints. For example, you can use ResourceFlavors to represent VMs with different provisioning guarantees (for example, spot versus on-demand), architectures (for example, x86 versus ARM CPUs), brands and models (for example, Nvidia A100 versus T4 GPUs).

In this tutorial, the `kueue-autopilot` cluster has homogeneous resources. As a result, create a single ResourceFlavor for CPU, memory, ephemeral-storage, and GPUs, with no labels or taints.
    
    
    apiVersion: kueue.x-k8s.io/v1beta1
    kind: ResourceFlavor
    metadata:
      name: default-flavor # This ResourceFlavor will be used for all the resources

Deploy the ResourceFlavor: 
    
    
    kubectl apply -f flavors.yaml
    

## Create the ClusterQueue

A ClusterQueue is a cluster-scoped object that manages a pool of resources such as CPU, memory, GPU. It manages the ResourceFlavors, and limits the usage and dictates the order in which workloads are admitted.
    
    
    apiVersion: kueue.x-k8s.io/v1beta1
    kind: ClusterQueue
    metadata:
      name: cluster-queue
    spec:
      namespaceSelector: {} # Available to all namespaces
      queueingStrategy: BestEffortFIFO # Default queueing strategy
      resourceGroups:
      - coveredResources: ["cpu", "memory", "nvidia.com/gpu", "ephemeral-storage"]
        flavors:
        - name: "default-flavor"
          resources:
          - name: "cpu"
            nominalQuota: 10
          - name: "memory"
            nominalQuota: 10Gi
          - name: "nvidia.com/gpu"
            nominalQuota: 10
          - name: "ephemeral-storage"
            nominalQuota: 10Gi

Deploy the ClusterQueue:
    
    
    kubectl apply -f cluster-queue.yaml
    

The order of consumption is determined by `.spec.queueingStrategy`, where there are two configurations:

  * BestEffortFIFO

    * The default queueing strategy configuration.
    * The workload admission follows the first in first out (FIFO) rule, but if there is not enough quota to admit the workload at the head of the queue, the next one in line is tried.
  * StrictFIFO

    * Guarantees FIFO semantics.
    * Workload at the head of the queue can block queueing until the workload can be admitted.



In `cluster-queue.yaml`, you create a new ClusterQueue called `cluster-queue`. This ClusterQueue manages four resources, `cpu`, `memory`, `nvidia.com/gpu` and `ephemeral-storage` with the flavor created in `flavors.yaml`. The quota is consumed by the requests in the workload Pod specs.

Each flavor includes usage limits represented as `.spec.resourceGroups[].flavors[].resources[].nominalQuota`. In this case, the ClusterQueue admits workloads if and only if:

  * The sum of the CPU requests is less than or equal to 10
  * The sum of the memory requests is less than or equal to 10Gi
  * The sum of GPU requests is less than or equal to 10
  * The sum of the storage used is less than or equal to 10Gi



## Create the LocalQueue

A LocalQueue is a namespaced object that accepts workloads from users in the namespace. LocalQueues from different namespaces can point to the same ClusterQueue where they can share the resources' quota. In this case, LocalQueue from namespace `team-a` and `team-b` points to the same ClusterQueue `cluster-queue` under `.spec.clusterQueue`.
    
    
    apiVersion: kueue.x-k8s.io/v1beta1
    kind: LocalQueue
    metadata:
      namespace: team-a # LocalQueue under team-a namespace
      name: lq-team-a
    spec:
      clusterQueue: cluster-queue # Point to the ClusterQueue
    ---
    apiVersion: kueue.x-k8s.io/v1beta1
    kind: LocalQueue
    metadata:
      namespace: team-b # LocalQueue under team-b namespace
      name: lq-team-b
    spec:
      clusterQueue: cluster-queue # Point to the ClusterQueue

Each team sends their workloads to the LocalQueue in their own namespace. Which are then allocated resources by the ClusterQueue.

Deploy the LocalQueues:
    
    
    kubectl apply -f local-queue.yaml
    

## Create Jobs and observe the admitted workloads

In this section, you create Kubernetes Jobs in the namespace `team-a`. A Job controller in Kubernetes creates one or more Pods and helps ensure that they successfully execute a specific task.

The Job in the namespace `team-a` has the following attributes:

  * It points to the `lq-team-a` LocalQueue.
  * It requests GPU resources by setting the `nodeSelector` field to `nvidia-tesla-t4`.
  * It is composed of three Pods that sleep for 10 seconds in parallel. Jobs are cleaned up after 60 seconds according to the value defined in the `ttlSecondsAfterFinished` field.
  * It requires 1,500 milliCPU, 1536 Mi of memory, 1,536 Mi of ephemeral storage, and three GPUs since there are three Pods.


    
    
    apiVersion: batch/v1
    kind: Job
    metadata:
      namespace: team-a # Job under team-a namespace
      generateName: sample-job-team-a-
      labels:
        kueue.x-k8s.io/queue-name: lq-team-a # Point to the LocalQueue
    spec:
      ttlSecondsAfterFinished: 60 # Job will be deleted after 60 seconds
      parallelism: 3 # This Job will have 3 replicas running at the same time
      completions: 3 # This Job requires 3 completions
      suspend: true # Set to true to allow Kueue to control the Job when it starts
      template:
        spec:
          nodeSelector:
            cloud.google.com/gke-accelerator: "nvidia-tesla-t4" # Specify the GPU hardware
          containers:
          - name: dummy-job
            image: gcr.io/k8s-staging-perf-tests/sleep:latest
            args: ["10s"] # Sleep for 10 seconds
            resources:
              requests:
                cpu: "500m"
                memory: "512Mi"
                ephemeral-storage: "512Mi"
                nvidia.com/gpu: "1"
              limits:
                cpu: "500m"
                memory: "512Mi"
                ephemeral-storage: "512Mi"
                nvidia.com/gpu: "1"
          restartPolicy: Never

Jobs are also created under the file [`job-team-b.yaml`](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/batch/kueue-intro/job-team-b.yaml) where its namespace belongs to `team-b`, with requests to represent different teams with different needs.

To learn more, see [deploying GPU workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus).

  1. In a new terminal, observe the status of the ClusterQueue that refreshes every two seconds:
         
         watch -n 2 kubectl get clusterqueue cluster-queue -o wide
         

  2. In a new terminal, observe the status of the nodes:
         
         watch -n 2 kubectl get nodes -o wide
         

  3. In a new terminal, create Jobs to LocalQueue from namespace `team-a` and `team-b` every 10 seconds:
         
         ./create_jobs.sh job-team-a.yaml job-team-b.yaml 10
         

  4. Observe the Jobs being queued up, admitted in the ClusterQueue, and nodes being brought up with GKE Autopilot.

**Note:** It is normal to see a warning for the Pods with message `Unschedulable` while Nodes are scaling up.
  5. Obtain a Job from namespace `team-a`:
         
         kubectl -n team-a get jobs
         

The outcome is similar to the following:
         
         NAME                      COMPLETIONS   DURATION   AGE
         sample-job-team-b-t6jnr   3/3           21s        3m27s
         sample-job-team-a-tm7kc   0/3                      2m27s
         sample-job-team-a-vjtnw   3/3           30s        3m50s
         sample-job-team-b-vn6rp   0/3                      40s
         sample-job-team-a-z86h2   0/3                      2m15s
         sample-job-team-b-zfwj8   0/3                      28s
         sample-job-team-a-zjkbj   0/3                      4s
         sample-job-team-a-zzvjg   3/3           83s        4m50s
         

  6. Copy a Job name from the previous step and observe the admission status and events for the Job.
         
         kubectl -n team-a describe job JOB_NAME
         

  7. When the pending Jobs start increasing from the ClusterQueue, end the script by pressing `CTRL + C` on the running script.

  8. Once all Jobs are completed, notice the nodes being scaled down.

**Note:** The scale down process can take up to two minutes.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the individual resource

  1. Delete the Kueue quota system:
         
         kubectl delete -n team-a localqueue lq-team-a
         kubectl delete -n team-b localqueue lq-team-b
         kubectl delete clusterqueue cluster-queue
         kubectl delete resourceflavor default-flavor
         

  2. Delete the Kueue manifest:
         
         VERSION=VERSION
         kubectl delete -f \
           https://github.com/kubernetes-sigs/kueue/releases/download/$VERSION/manifests.yaml
         

  3. Delete the cluster:
         
         gcloud container clusters delete kueue-autopilot --location=CONTROL_PLANE_LOCATION
         




## What's next

  * Check out the [GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview).

  * Learn more about [Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/).

  * [Learn more about Kueue](https://kueue.sigs.k8s.io/)

  * Learn how to [Setup Kueue for quota sharing between namespaces](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/kueue-cohort)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
