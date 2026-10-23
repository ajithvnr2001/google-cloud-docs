---
url: https://docs.cloud.google.com/kubernetes-engine/security/secure-modules-cos/
title: Configure secure kernel module loading \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:17.910938+00:00
---

# Configure secure kernel module loading  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/security/secure-modules-cos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Configure secure kernel module loading Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Google Kubernetes Engine (GKE) secure kernel module loading lets you run workloads that require signed, out-of-tree (OOT) kernel modules on secure, Container-Optimized OS images. Secure kernel module loading helps enhance the security posture of your clusters and node pools by giving you more control over loading modules on CPU, TPU, or GPU nodes with signature verification.

## How secure kernel module loading works

By default, GKE nodes use different Container-Optimized OS images with different security configurations, depending on the node type:

  * **CPU and TPU nodes** : use a Container-Optimized OS image with [Linux Security Module (LSM) Loadpin](https://docs.kernel.org/admin-guide/LSM/LoadPin.html) enabled. Loadpin restricts any OOT kernel module loading. This setting is secure, but prevents loading OOT modules.
  * **GPU nodes** : use a Container-Optimized OS image with Loadpin disabled. This setting allows loading OOT modules, such as installation of NVIDIA drivers, but is less secure by default.



You enable secure kernel module loading by using the `NodeKernelModuleLoading.Policy` setting in the `LinuxNodeConfig` for a node pool or by passing the `--enable-kernel-module-signature-enforcement` flag when creating or updating a cluster or node pool. When you set the policy to `ENFORCE_SIGNED_MODULES`, Loadpin is enabled but configured to allow kernel module loading from outside the root file system. Modules must be signed and the system permits only Google-signed modules.

## When to use secure kernel module loading

Use secure kernel module loading when you need to load Google-signed OOT kernel modules, such as custom drivers or file systems like Lustre, on any GKE node type. This feature lets you use these modules without reducing the security posture of the node. For example, you can load a required driver on a CPU node without needing to use the less restrictive GPU image type.

## Requirements and limitations

When you enable secure kernel module loading on your node pools, the following requirements and limitations apply:

  * **Supported modules** : only Google-signed OOT modules are allowed.
  * **cgroup v2** : the node pool must use cgroup v2. The Kubernetes Engine API rejects requests to enable this policy on node pools that use cgroup v1. For more information, see the [Kubernetes cgroup documentation](https://kubernetes.io/docs/concepts/architecture/cgroups/).
  * **GKE version** : this feature is available for CPU and TPU nodes in GKE cluster versions 1.34.1-gke.2364000 and later. For GPU nodes, this feature is available in versions 1.36.0-gke.1585000 and later.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Configure the secure kernel module loading policy

You can configure the secure kernel module loading policy on individual clusters or as a node pool setting. The available policies are:

  * `ENFORCE_SIGNED_MODULES`: enforces that any out-of-tree kernel modules are signed by Google. This policy requires the node pool to use cgroup v2.
  * `DO_NOT_ENFORCE_SIGNED_MODULES`: allows any kernel module, signed or unsigned, to be loaded. This is the default behavior.



If you don't specify a policy, GKE uses the default behavior, which does not enforce signed modules.

### Enable secure kernel module loading on a cluster

To enable secure kernel module loading a cluster, complete one of the following steps:

  * To enable on a new cluster, run the following command:

###  Standard 
        
        gcloud container clusters create CLUSTER_NAME \
           --location=LOCATION \
           --project=PROJECT_ID \
           --enable-kernel-module-signature-enforcement
        

###  Autopilot 
        
        gcloud container clusters create-auto CLUSTER_NAME \
           --location=LOCATION \
           --project=PROJECT_ID \
           --enable-kernel-module-signature-enforcement
        

Replace the following:

    * `CLUSTER_NAME`: the name of your new cluster.
    * `LOCATION`: the region or zone for the cluster.
    * `PROJECT_ID`: your project ID.
  * To enable on an existing cluster, run the following command:
        
        gcloud container clusters update CLUSTER_NAME \
             --location=LOCATION \
             --project=PROJECT_ID \
             --enable-kernel-module-signature-enforcement
        

Replace the following:

    * `CLUSTER_NAME`: the name of your cluster.
    * `LOCATION`: the region or zone for the cluster.
    * `PROJECT_ID`: your project ID.

When you update an existing cluster, nodes are re-created at the next available opportunity, unless prevented by a maintenance window.




### Enable secure kernel module loading on a node pool

To enable secure kernel module loading on a node pool, complete one of the following steps:

  * To enable on a new node pool, run the following command:
        
        gcloud container node-pools create NODEPOOL_NAME \
             --cluster=CLUSTER_NAME \
             --location=LOCATION \
             --project=PROJECT_ID \
             --enable-kernel-module-signature-enforcement
        

Replace the following:

    * `NODEPOOL_NAME`: the name of your new node pool.
    * `CLUSTER_NAME`: the name of your cluster.
    * `LOCATION`: the region or zone for the cluster.
    * `PROJECT_ID`: your project ID.
  * To enable on an existing node pool, run the following command:
        
        gcloud container node-pools update NODEPOOL_NAME \
             --cluster=CLUSTER_NAME \
             --location=LOCATION \
             --project=PROJECT_ID \
             --enable-kernel-module-signature-enforcement
        

Replace the following:

    * `NODEPOOL_NAME`: the name of the node pool to update.
    * `CLUSTER_NAME`: the name of your cluster.
    * `LOCATION`: the region or zone for the cluster.
    * `PROJECT_ID`: your project ID.



## Confirm the secure kernel module policy is set

To confirm that a policy is set for a cluster, run the following command:
    
    
    gcloud container node-pools describe NODEPOOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=LOCATION \
        --project=PROJECT_ID
    

In the output, check the `linuxNodeConfig` section. The `kernelModuleLoading` field shows the current policy:
    
    
    ...
    config:
      linuxNodeConfig:
        kernelModuleLoading:
          policy: ENFORCE_SIGNED_MODULES
        cgroupMode: CGROUP_MODE_V2
    

## Disable secure kernel module loading

To disable secure kernel module loading, complete one of the following steps:

  * To disable on a cluster, run the following command:
        
        gcloud container clusters update CLUSTER_NAME \
             --location=LOCATION \
             --project=PROJECT_ID \
             --no-enable-kernel-module-signature-enforcement
        

  * To disable on an existing node pool, run the following command:
        
        gcloud container node-pools update NODEPOOL_NAME \
             --cluster=CLUSTER_NAME \
             --location=LOCATION \
             --project=PROJECT_ID \
             --no-enable-kernel-module-signature-enforcement
        




## What's next

  * Learn how to [harden your cluster's security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
