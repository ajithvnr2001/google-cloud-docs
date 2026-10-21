---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/spot-vms/
title: Run fault-tolerant workloads at lower costs with Spot VMs \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:59.372133+00:00
---

# Run fault-tolerant workloads at lower costs with Spot VMs  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/spot-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Run fault-tolerant workloads at lower costs with Spot VMs Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to run fault-tolerant, stateless, or batch workloads at lower costs by using Spot VMs in your Google Kubernetes Engine (GKE) clusters and node pools.

## Overview

Spot VMs are Compute Engine [virtual machines (VMs)](https://docs.cloud.google.com/compute/docs/instances) that are priced lower than the default standard VMs and provide no guarantee of availability. Spot VMs offer the same [machine types](https://docs.cloud.google.com/compute/docs/machine-types) and options as standard Compute Engine VMs. Compute Engine can reclaim Spot VMs at any time due to system events, such as when the resources are needed for standard VMs.

To learn more about Spot VMs in GKE, see [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms).

Spot VMs replace the need to use [preemptible VMs](https://docs.cloud.google.com/compute/docs/instances/preemptible) to run stateless, batch, or fault-tolerant workloads. In contrast to preemptible VMs, which expire after 24 hours, Spot VMs have no expiration time. Spot VMs are terminated when Compute Engine requires the resources to run standard VMs.

**Note:** GKE continues to support using preemptible VMs in your clusters and node pools.

Spot VMs are also supported on GKE Autopilot clusters through [Spot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-spot-pods). With Spot Pods, Autopilot automatically schedules and manages workloads on Spot VMs.

## Limitations

  * Spot VMs don't support Windows Server node pools.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * [View the availability of Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-vm-availability) before provisioning resources to help reduce your chances of encountering resource availability errors.



## Provision Spot VMs in GKE

You can provision Spot VMs by creating a cluster that uses Spot VMs for the default node pool. Or, you can create a node pool that uses Spot VMs.

Use either the Google Cloud console or Google Cloud CLI to set the parameters for the graceful shutdown of Spot VMs. For more information about the ability to set the graceful shutdown parameters, see [Termination and graceful shutdown of Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms#termination-graceful-shutdown).

### Create a cluster with Spot VMs

You can create a new cluster using Spot VMs with the Google Cloud CLI or the Google Cloud console.

### Console

To create a new cluster with a node pool using Spot VMs, perform the following steps:

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. From the navigation menu, in the **Node pools** section, click the name of the node pool you want to configure.

  3. For **Provisioning model** , select **Spot VMs**.

  4. Optional: to configure the graceful termination period for Pods running on nodes in this node pool, select a value for the **Shutdown grace period** drop-down and, if applicable, enter a value for the **Critical pods shutdown grace period (seconds)** field. The values, if configured, are stored in the [node system configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#spot-graceful-termination), where you can later update them, if needed. For more information, see [Termination and graceful shutdown of Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms#termination-graceful-shutdown).

  5. Configure the cluster as needed, and then click **Create**.




### gcloud

Create a new cluster which uses Spot VMs in the default node pool instead of standard VMs:
    
    
    gcloud container clusters create CLUSTER_NAME \
        **--spot**
        [--system-config-from-file=SYSTEM_CONFIG_PATH]
    
    

Replace `CLUSTER_NAME` with the name of your new cluster.

Optionally, if you want to set the parameters for graceful shutdown for the default node pool, replace `SYSTEM_CONFIG_PATH` with the path to the file containing your `kubelet` configuration. For more information, see [Graceful termination of Spot VMs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#spot-graceful-termination). You can also update these parameters after node pool creation, however, GKE must [re-create the nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#update-config-of-existing-node-pool) to make the changes.

### Create a node pool with Spot VMs

You can create new node pools using Spot VMs with the gcloud CLI or Google Cloud console. You can only enable Spot VMs on new node pools. You cannot enable or disable Spot VMs on existing node pools.

### Console

To create a new node pool using Spot VMs, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Click the **Nodes** tab.

  4. Click add_box **Create user-managed node pool**.

  5. From the navigation menu, click **Nodes**.

  6. For **Provisioning model** , select **Spot VMs**.

  7. Optional: to configure the graceful termination period for Pods running on nodes in this node pool, select a value for the **Shutdown grace period** drop-down and, if applicable, enter a value for the **Critical pods shutdown grace period (seconds)** field. The values, if configured, are stored in the [node system configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#spot-graceful-termination), where you can later update them, if needed. For more information, see [Termination and graceful shutdown of Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms#termination-graceful-shutdown).

  8. Configure the node pool as needed, and then click **Create node pool**.




### gcloud

Create a new node pool using Spot VMs:
    
    
    gcloud container node-pools create POOL_NAME \
        --cluster=CLUSTER_NAME \
        **--spot**
        [--system-config-from-file=SYSTEM_CONFIG_PATH]
    

Replace the following:

  * `POOL_NAME`: the name of the new node pool.
  * `CLUSTER_NAME`: the name of your cluster.



Optionally, if you want to set the parameters for graceful shutdown, replace `SYSTEM_CONFIG_PATH` with the path to the file containing your `kubelet` configuration. For more information, see [Graceful termination of Spot VMs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#spot-graceful-termination). You can also update these parameters after node pool creation, however, GKE must [re-create the nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#update-config-of-existing-node-pool) to make the changes.

## Schedule workloads on Spot VMs

GKE adds the `cloud.google.com/gke-spot=true` and `cloud.google.com/gke-provisioning=spot` (for nodes running GKE version 1.25.5-gke.2500 or later) [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) to nodes that use Spot VMs. You can filter for this label in your Pod spec using either the [`nodeSelector`](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) field in your Pod spec or [node affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity).

In the following example, you create a cluster with two node pools, one of which uses Spot VMs. Then, you deploy a stateless `nginx` application onto the Spot VMs, using a `nodeSelector` to control where GKE places the Pods.

  1. Create a new cluster with the default node pool using standard VMs:
         
         gcloud container clusters create CLUSTER_NAME
         

Replace `CLUSTER_NAME` with the name of your new cluster.

  2. Get credentials for the cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME
         

  3. Create a node pool using Spot VMs:
         
         gcloud container node-pools create POOL_NAME \
            **--cluster =CLUSTER_NAME** \
             --num-nodes=1 \
             --spot
         

Replace the following:

     * `POOL_NAME`: the name of the new node pool.
     * `CLUSTER_NAME`: the name of your cluster.
  4. Save the following manifest as a file named `pi-app.yaml`:
         
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: pi
         spec:
           template:
             metadata:
               labels:
                 app: pi
             spec:
               nodeSelector:
                 cloud.google.com/gke-spot: "true"
               terminationGracePeriodSeconds: 25
               containers:
               - name: pi
                 image: perl:5.34.0
                 command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
               restartPolicy: Never
           backoffLimit: 4
         

In this manifest, the `nodeSelector` field tells GKE to only schedule Pods on nodes that use Spot VMs.

  5. Apply the manifest to your cluster:
         
         kubectl apply -f pi-app.yaml
         

  6. Describe the Pod:
         
         kubectl describe pod pi
         

The output is similar to the following:
         
         Name:         pi-kjbr9
         Namespace:    default
         Priority:     0
         **Node:         gke-cluster-2-spot-pool-fb434072-44ct**
         ...
         Labels:       app=pi
                       job-name=pi
         Status:       Succeeded
         ...
         Controlled By:  Job/pi
         Containers:
         ...
         Conditions:
           Type              Status
           Initialized       True 
           Ready             False 
           ContainersReady   False 
           PodScheduled      True 
         Volumes:
         ...
         Node-Selectors:              cloud.google.com/gke-spot=true
         Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                                     node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
         Events:
           Type    Reason     Age    From               Message
           ----    ------     ----   ----               -------
           Normal  Scheduled  4m3s   default-scheduler  Successfully assigned default/pi-kjbr9 to gke-cluster-2-spot-pool-fb434072-44ct
           Normal  Pulling    4m2s   kubelet            Pulling image "perl:5.34.0"
           Normal  Pulled     3m43s  kubelet            Successfully pulled image "perl:5.34.0" in 18.481761978s
           Normal  Created    3m43s  kubelet            Created container pi
           Normal  Started    3m43s  kubelet            Started container pi
         

The `Node` field shows that GKE only schedules your Pods on nodes that use Spot VMs.




## Use taints and tolerations for Spot VMs

As a best practice, create clusters with at least one node pool without Spot VMs where you can place system workloads like DNS. You can use [node taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) and the corresponding [tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) to tell GKE to avoid placing certain workloads on Spot VMs.

  1. To create a node pool with nodes that use Spot VMs and have node taints, use the `--node-taints` flag when creating the node pool:
         
         gcloud container node-pools create POOL_NAME \
             **--cluster =CLUSTER_NAME** \
             **--node-taints =cloud.google.com/gke-spot="true":NoSchedule** \
             --spot
         

  2. To add the corresponding toleration to the Pods that you want to schedule to Spot VMs, modify your deployments and add the following to your Pod specification:
         
         tolerations:
         - key: cloud.google.com/gke-spot
           operator: Equal
           value: "true"
           effect: NoSchedule
         

GKE only schedules Pods with this toleration onto the Spot VMs with the added node taint.




## What's next

  * [Learn how to run a GKE application on Spot VMs with on-demand nodes as fallback](https://cloud.google.com/blog/topics/developers-practitioners/running-gke-application-spot-nodes-demand-nodes-fallback).
  * [Learn more about Spot VMs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms).
  * [Take a tutorial about deploying a batch workload using Spot VMs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/batch-ml-workload).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
