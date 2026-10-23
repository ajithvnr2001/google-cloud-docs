---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/analyzing-cpu-performance-using-pmu/
title: Analyze CPU performance using the PMU \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:25.717931+00:00
---

# Analyze CPU performance using the PMU  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/analyzing-cpu-performance-using-pmu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Analyze CPU performance using the PMU Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to analyze the CPU performance of your Google Kubernetes Engine (GKE) cluster nodes using [Performance Monitoring Unit (PMU)](https://docs.cloud.google.com/compute/docs/pmu-overview) events.

This page is intended for cluster admins who have performance-sensitive workloads and want to examine the CPU execution of their workloads on their GKE nodes during development, debugging, benchmarking, and continuous monitoring.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Requirements and limitations

When enabling PMU events, be aware of the following requirements and limitations:

  * Your cluster must be Standard mode.
  * If your cluster has node auto-provisioning enabled, any node pools created through auto-provisioning cannot enable PMU events. If you enable node auto provisioning after enabling PMU events, existing node pools are not impacted.
  * Cluster node pools must run a machine series that supports PMU. For more information about the supported machine types, see [Supported machine series and CPU platforms](https://docs.cloud.google.com/compute/docs/pmu-overview#supported-series).



## Create a GKE cluster

Create a cluster with PMU events enabled for the default node pool:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=COMPUTE_LOCATION \
        --performance-monitoring-unit=PMU_LEVEL \
        --machine-type=MACHINE_TYPE
    

Replace the following:

  * `CLUSTER_NAME`: the name of the new cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the new cluster.
  * `PMU_LEVEL`: the type of PMU events to collect. For more information, see [How the PMU works](https://docs.cloud.google.com/compute/docs/pmu-overview#how-pmu-works) in the Compute Engine documentation. Supported values are as follows: 
    * `architectural`: enables architectural PMU events related to non-last-level cache (LLC) events.
    * `standard`: includes architectural events and enables core PMU events, including L2 cache events.
    * `enhanced`: includes standard events and enables any local events outside the CPU core and LLC PMU events. This option is only available with VMs that have a specific number of vCPUs. For more information, see [Limitations](https://docs.cloud.google.com/compute/docs/pmu-overview#limitations) in the Compute Engine documentation.
  * `MACHINE_TYPE`: the Compute Engine machine type for your nodes. For a list of supported machine types, see [Supported machine series and CPU platforms](https://docs.cloud.google.com/compute/docs/pmu-overview#supported-series) in the Compute Engine documentation.



You can also create a new node pool for an existing cluster using the [`gcloud container node-pools create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create) command.

## Connect to the cluster

Configure `kubectl` to communicate with the cluster:
    
    
    gcloud container clusters get-credentials CLUSTER_NAME \
        --location=COMPUTE_LOCATION
    

## Verify the PMU is enabled

Verify your cluster nodes have PMU enabled by examining the kernel messages.

  1. Get a list of nodes in the cluster:
         
         kubectl get nodes
         

The output is similar to the following:
         
         NAME                                  STATUS   ROLES    AGE     VERSION
         gke-c1-default-pool-44be3e13-prr1     Ready    <none>   5d23h   v1.27.13-gke.1070000
         gke-c1-default-pool-7abc4a17-9dlg     Ready    <none>   2d21h   v1.27.13-gke.1070000
         gke-c1-default-pool-ed969ef6-4gzp     Ready    <none>   5d      v1.27.13-gke.1070000
         

Record the name of one of the nodes.

  2. Get the Compute Engine location of the node:
         
         gcloud compute instances list --filter=NODE_NAME
         

Replace `NODE_NAME` with the name of a node from the previous step.

The output is similar to the following:
         
         NAME                               ZONE           MACHINE_TYPE  PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP    STATUS
         gke-c1-default-pool-44be3e13-prr1  us-central1-c  c4-standard-4     true         10.128.0.67  34.170.44.164  RUNNING
         

Record the name of the Compute Engine `ZONE`. In this example, it's `us-central1-c`.

  3. Use SSH to connect to the cluster node:
         
         gcloud compute ssh NODE_NAME \
             --zone=COMPUTE_ZONE
         

Replace `COMPUTE_ZONE` with the name of the Compute Engine zone from the previous step.

  4. Examine the kernel messages:
         
         sudo dmesg |grep -A10 -i "Performance"
         

The output is similar to the following:
         
         [    0.307634] Performance Events: generic architected perfmon, full-
         width counters, Intel PMU driver.
         # Several lines omitted
         

This output indicates the PMU driver is initialized.




## What's next

  * Learn how to [Choose a minimum CPU platform](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/min-cpu-platform)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
