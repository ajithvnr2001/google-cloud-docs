---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-confidential-nodes/
title: Encrypt GPU workload data in use with Confidential GKE Nodes \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:02.019176+00:00
---

# Encrypt GPU workload data in use with Confidential GKE Nodes  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-confidential-nodes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Encrypt GPU workload data in use with Confidential GKE Nodes Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can encrypt GPU workload data in-use by running the workloads on encrypted Confidential Google Kubernetes Engine Nodes. This page shows Security engineers and Operators how to improve security for the data in accelerated workloads, such as AI/ML tasks. You should be familiar with the following concepts:

  * [Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes)
  * [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview)
  * [GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus)



## About running GPU workloads on Confidential GKE Nodes

You can request Confidential GKE Nodes for your GPU workloads by using one of the following methods:

  * Automatically provision Confidential GKE Nodes for your GPU workloads by using GKE _ComputeClasses_. You can use this method in Autopilot clusters and in Standard clusters. For more information, see the Use ComputeClasses to run GPU workloads on Confidential GKE Nodes section.
  * Manually configure Confidential GKE Nodes for your Standard clusters or node pools. For more information, see the Manually configure Confidential GKE Nodes in GKE Standard section.



## Limitations

Autopilot mode supports only NVIDIA H100 (80 GB) GPUs with Confidential GKE Nodes.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Requirements

Regardless of the Confidential GKE Nodes configuration method that you choose, you must meet all of the following requirements:

  * The nodes must be in a zone that supports NVIDIA Confidential Computing. For more information, see [View supported zones](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-zones).
  * The nodes must use a supported machine type, Confidential Computing technology, and GPU. For more information, see [Supported configurations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#machine-type-cpu-zone).
  * You must have preemptible quota for the GPUs that you want to use in your node locations. For example, if you use NVIDIA H100 (80 GB) GPUs, then you must have quota for `compute.googleapis.com/preemptible_nvidia_h100_gpus`. For more information about managing your quota, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).



In addition to these requirements, you must meet specific conditions depending on the Confidential GKE Nodes configuration method that you choose, as described in the following table:

Configuration method | Requirements | Limitations  
---|---|---  
ComputeClasses | 

  * Use Spot VMs or [flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws) ([Preview](https://cloud.google.com/products#product-launch-stages)).
  * Use GKE version 1.33.3-gke.1392000 or later.

| 

  * You can't use flex-start with queued provisioning with ComputeClasses.
  * You can't use GPU sharing features like time-sharing or multi-instance GPUs.

  
Manual configuration in Standard mode | 

  * Use Spot VMs, preemptible VMs, flex-start ([Preview](https://cloud.google.com/products#product-launch-stages)), or flex-start with queued provisioning.
  * Use one of the following GKE versions: 
    * **Manual GPU driver installation** : 1.32.2-gke.1297000 or later.
    * **Automatic GPU driver installation** : 1.33.3-gke.1392000 or later. **Caution** : For automatic driver installation, versions earlier than 1.33.3-gke.1392000 might cause workload disruptions because of driver incompatibilities.
    * **Flex-start with queued provisioning** : 1.32.2-gke.1652000 or later.

| 

  * You can't use flex-start ([Preview](https://cloud.google.com/products#product-launch-stages)) if you enable Confidential GKE Nodes for the entire cluster.
  * You can't use GPU sharing features like time-sharing or multi-instance GPUs.

  
  
### Required roles

To get the permissions that you need to create Confidential GKE Nodes, ask your administrator to grant you the following IAM roles on the Google Cloud project: 

  * Create Confidential GKE Nodes: [Kubernetes Engine Cluster Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterAdmin) (`roles/container.clusterAdmin`) 
  * Deploy GPU workloads: [Kubernetes Engine Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.developer) (`roles/container.developer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Use ComputeClasses to run confidential GPU workloads

You can define your Confidential GKE Nodes configuration in a [ComputeClass](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes). ComputeClasses are Kubernetes custom resources that let you declaratively set node configurations for GKE autoscaling and scheduling. You can follow the steps in this section in any Autopilot or Standard cluster that runs GKE version 1.33.3-gke.1392000 or later.

To use a ComputeClass to run GPU workloads on Confidential GKE Nodes, follow these steps:

  1. Save the following ComputeClass manifest as a YAML file:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: COMPUTECLASS_NAME
         spec:
           **nodePoolConfig :
             confidentialNodeType: CONFIDENTIAL_COMPUTE_TECHNOLOGY
           priorityDefaults:
             location:
               zones: ['ZONE1','ZONE2']
           priorities:
           - gpu:
               type: GPU_TYPE
               count: GPU_COUNT
               driverVersion: default
             spot: true**
           activeMigration:
             optimizeRulePriority: true
           nodePoolAutoCreation:
             enabled: true
           whenUnsatisfiable: DoNotScaleUp
         

Replace the following:

     * `COMPUTECLASS_NAME`: a name for the ComputeClass.
     * `CONFIDENTIAL_COMPUTE_TECHNOLOGY`: the Confidential Computing technology to use, such as `TDX`. Choose a technology that's supported by the GPU that you want to use.

     * `ZONE1,ZONE2`: a comma-separated list of zones to create nodes in, such as `['us-central1-a','us-central1-b']`. Specify zones that support the Confidential Computing technology and machine type that you want to use. For more information, see [View supported zones](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-zones).

     * `GPU_TYPE`: the GPU type to use, such as `nvidia-h100-80gb`.

     * `GPU_COUNT`: the number of GPUs to attach to each node. Specify a value that's supported by Confidential VM for the GPU type. For example, if you choose the `nvidia-h100-80gb` GPU type, then you must specify a value of `1` in this field.

  2. Create the ComputeClass:
         
         kubectl apply -f PATH_TO_MANIFEST
         

Replace `PATH_TO_MANIFEST` with the path to the ComputeClass manifest file.

  3. To run your GPU workload on Confidential GKE Nodes, select the ComputeClass in the workload manifest. For example, save the following Deployment manifest, which selects a ComputeClass and GPUs, as a YAML file:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: confidential-gpu-deployment
           labels:
             app: conf-gpu
         spec:
           selector:
             matchLabels:
               app: conf-gpu
           replicas: 1
           template:
             metadata:
               labels:
                 app: conf-gpu
             spec:
               nodeSelector:
                 cloud.google.com/compute-class: COMPUTECLASS_NAME
               containers:
               - name: example-app
                 image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
                 resources:
                   limits:
                     cpu: "4"
                     memory: "16Gi"
                     nvidia.com/gpu: GPU_REQUEST
                   requests:
                     cpu: "4"
                     memory: "16Gi"
         

Replace the following:

     * `COMPUTECLASS_NAME`: the name of the ComputeClass that you created.
     * `GPU_REQUEST`: the number of GPUs to use in the container. Specify a value that's less than or equal to the value that you specified in the `gpu.count` field of the ComputeClass.
  4. Create the Deployment:
         
         kubectl apply -f PATH_TO_DEPLOYMENT_MANIFEST
         

Replace `PATH_TO_DEPLOYMENT_MANIFEST` with the path to the Deployment manifest.




When you create your GPU workload, GKE uses the configuration in the ComputeClass to create Confidential GKE Nodes with attached GPUs.

## Manually configure Confidential GKE Nodes in GKE Standard

You can run GPU workloads on Confidential GKE Nodes in Standard mode clusters or node pools.

### Enable Confidential GKE Nodes in new Standard clusters

You can enable Confidential GKE Nodes for your entire Standard cluster, so that every GPU node pool that you create uses the same Confidential Computing technology. When you create a new Standard mode cluster that uses Confidential GKE Nodes for GPU workloads, ensure that you specify the following cluster settings:

  * **Location** : a region or a zone that supports NVIDIA Confidential Computing. For more information, see [View supported zones](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-zones).
  * **Confidential Computing type** : a Confidential Computing technology that supports GPUs. For more information, see [Supported configurations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#machine-type-cpu-zone).
  * **Cluster version** : one of the following versions, depending on how you want to install your GPU drivers:

    * **Manual GPU driver installation** : 1.32.2-gke.1297000 or later.
    * **Automatic GPU driver installation** : 1.33.3-gke.1392000 or later.



You can optionally configure GPUs for the default node pool that GKE creates in your cluster. However, we recommend that you use a separate node pool for your GPUs, so that at least one node pool in the cluster can run any workload.

For more information, see [Enable Confidential GKE Nodes on Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes#enabling_in_a_new_cluster).

### Use Confidential GKE Nodes with GPUs in Standard node pools

If your cluster doesn't have Confidential GKE Nodes enabled, you can enable Confidential GKE Nodes in specific new or existing GPU node pools. The control plane and node pools must meet the requirements in the Availability section. When you configure the node pool, you can choose to install GPU drivers automatically or manually.

  * To create a new GPU node pool that uses Confidential GKE Nodes, select one of the following options:

###  Console 

    1. In the Google Cloud console, go to the **Kubernetes clusters** page:

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list)

    2. Click the name of the Standard mode cluster to modify.

    3. Click the **Nodes** tab.

    4. Click add_box **Create user-managed node pool**. The **Add a node pool** page opens.

    5. On the **Node pool details** pane, do the following:

       1. Select **Specify node locations**.
       2. Select only the supported zones that are listed in the Availability section.
       3. Ensure that the control plane version is one of the versions that's listed in the Availability section.
    6. In the navigation menu, click **Nodes**.

    7. On the **Configure node settings** pane, do the following:

       1. In the **Machine configuration** section, click **GPUs**.
       2. In the **GPU type** menu, select a GPU type that's supported by Confidential Computing.
       3. In the **Number of GPUs** menu, select the number of GPUs to attach to each node. Select a value that's supported by the GPU type that you chose. For example, if you chose NVIDIA H100 (80 GB) GPUs, select **1**.
       4. Ensure that **Enable GPU sharing** isn't selected.
       5. In the **GPU Driver installation** section, select one of the following options:

          * **Google-managed** : GKE automatically installs a driver. If you select this option, in the **Version** drop-down list, select one of the following driver versions:

            * **Default** : install the default driver version for the node GKE version. Requires GKE version 1.33.3-gke.1392000 or later.
            * **Latest** : install the latest driver version for the node GKE version. Requires GKE version 1.33.3-gke.1392000 or later.
**Caution:** if you select the **Google-managed** option, control plane version upgrades immediately trigger node re-creation in node pools that use Confidential GKE Nodes. GKE re-creates the nodes using the node upgrade strategy, regardless of active maintenance policies. Before you upgrade your control plane, ensure that your confidential GPU workloads are ready to handle potential disruptions.
          * **User-managed** : skip automatic driver installation. If you select this option, you **must** manually install a compatible GPU driver. Requires 1.32.2-gke.1297000 or later.

       6. In the **Machine type** section, ensure that the machine type is a GPU machine type that's supported by Confidential VM for your selected GPU type.

       7. Select **Enable nodes on spot VMs** or [configure Flex-start VMs with queued provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest#create-node-pool).

    8. When you're ready to create the node pool, click **Create**.

###  gcloud 

You can create GPU node pools that run Confidential GKE Nodes on Spot VMs or by using _Flex-start VMs with queued provisioning_.

    * Create a GPU node pool that runs Confidential GKE Nodes on Spot VMs:
          
          gcloud container node-pools create NODE_POOL_NAME \
              --cluster=CLUSTER_NAME \
              --confidential-node-type=CONFIDENTIAL_COMPUTE_TECHNOLOGY \
              --location=LOCATION \
              --node-locations=NODE_LOCATION1,NODE_LOCATION2,... \
              --spot \
              --accelerator=type=GPU_TYPE,count=GPU_COUNT,gpu-driver-version=DRIVER_VERSION \
              --machine-type=MACHINE_TYPE
          

Replace the following:

      * `NODE_POOL_NAME`: a name for your new node pool.
      * `CLUSTER_NAME`: the name of your existing cluster.
      * `CONFIDENTIAL_COMPUTE_TECHNOLOGY`: the Confidential Computing technology to use, such as `TDX`. Choose a technology that's supported by the GPU that you want to use.
      * `LOCATION`: the location for your new node pool. The location must support using GPUs in Confidential GKE Nodes.
      * `NODE_LOCATION1,NODE_LOCATION2,...`: a comma-separated list of zones to run the nodes in. Specify zones that support the Confidential Computing technology and machine type that you want to use. For more information, see [View supported zones](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-zones).
      * `GPU_TYPE`: the GPU type to use, such as `nvidia-h100-80gb`.
      * `GPU_COUNT`: the number of GPUs to attach to each node. Specify a value that's supported by Confidential VM for the GPU type. For example, if you choose the `nvidia-h100-80gb` GPU type, then you must specify a value of `1` in this field.

      * `DRIVER_VERSION`: the GPU driver version to install. Specify one of the following values:

        * `default`: install the default driver version for the node GKE version. Requires GKE version 1.33.3-gke.1392000 or later.
        * `latest`: install the latest driver version for the node GKE version. Requires GKE version 1.33.3-gke.1392000 or later.
        * `disabled`: skip automatic driver installation. If you specify this value, you **must** manually install a compatible GPU driver. Requires 1.32.2-gke.1297000 or later.
**Caution:** if you specify `default` or `latest`, control plane version upgrades immediately trigger node re-creation in node pools that use Confidential GKE Nodes, regardless of active maintenance policies. Before you upgrade your control plane, ensure that your confidential GPU workloads are ready to handle potential disruptions.
      * `MACHINE_TYPE`: the machine type to use for the nodes. Specify a GPU machine type that's supported by Confidential VM for your selected GPU type.
    * Create a GPU node pool that runs Confidential GKE Nodes by using Flex-start VMs with queued provisioning:
          
          gcloud container node-pools create NODE_POOL_NAME \
              --cluster=CLUSTER_NAME \
              --node-locations=NODE_LOCATION1,NODE_LOCATION2,... \
              --machine-type=MACHINE_TYPE \
              --confidential-node-type=CONFIDENTIAL_COMPUTE_TECHNOLOGY \
              --location=LOCATION \
              **--flex-start --enable-queued-provisioning \
              --enable-autoscaling --num-nodes=0 --total-max-nodes=TOTAL_MAX_NODES \**
              --location-policy=ANY --no-enable-autorepair \
              --accelerator=type=GPU_TYPE,count=GPU_COUNT,gpu-driver-version=DRIVER_VERSION
          

Replace `TOTAL_MAX_NODES` with the maximum number of nodes that the node pool can automatically scale to.

For more information about the configuration options in flex-start with queued provisioning, see [Run a large-scale workload with flex-start with queued provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest).

  * To update your existing node pools to use Confidential Computing, see [Update an existing node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes#update-existing-node-pool).




#### Manually install GPU drivers that support Confidential GKE Nodes

If you didn't enable automatic driver installation when you created or updated your node pools, you must manually install a GPU driver that supports Confidential GKE Nodes.

This change requires recreating the nodes, which can cause disruption to your running workloads. For details about this specific change, find the corresponding row in the [manual changes that recreate the nodes using a node upgrade strategy without respecting maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manual-changes-strategy-but-no-respect-policies) table. To learn more about node updates, see [Planning for node update disruptions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#plan-node-disruption).

**Caution:** GKE immediately begins recreating the nodes for this change using the node upgrade strategy, regardless of active maintenance policies. GKE depends on [resource availability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota) for the change. Disabling node auto-upgrades [doesn't prevent this change](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable-only-versions). Ensure that your workloads running on the nodes are prepared for disruption before you initiate this change.

For instructions, see the "COS" tab in [Manually install NVIDIA GPU drivers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#installing_drivers).

## Troubleshoot

For troubleshooting information, see [Troubleshoot GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/gpus#confidential-nodes-gpus).

## What's next

  * [Verify that your GPU nodes use Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes#verifying_that_are_enabled)
  * [Deploy a workload on your GPU nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#multiple_gpus)
  * [Learn about the methods to run large-scale workloads with GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws#methods)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
