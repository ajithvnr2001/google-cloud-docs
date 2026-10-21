---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning/
title: Configure node pool auto-creation \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:58.987532+00:00
---

# Configure node pool auto-creation  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Configure node pool auto-creation Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can reduce the amount of manual infrastructure management in Google Kubernetes Engine (GKE) Standard clusters by letting GKE automatically create node pools for pending Pods. This document shows you how to enable node pool auto-creation for clusters and workloads, set default values for auto-created nodes, and trigger auto-creation for some common use cases.

This document is for cluster administrators, operators, and developers who manage infrastructure in, and deploy workloads to, Standard clusters. For more information about how node pool auto-creation works and the different enablement methods (such as ComputeClasses and cluster-level node auto-provisioning), see [About node pool auto-creation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning).

## Limitations

Node pool auto-creation has the following limitations:

  * All of the limitations of the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#limitations) also apply to node pool auto-creation.
  * Clusters that have more than 200 total node pools might have increased latency during autoscaling. Any configuration that triggers the creation of a new node pool, such as [workload separation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-separation) or the use of multiple ComputeClasses, increases this number. For more information about cluster limits, see [limits and best practices](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-clusters#limits-best-practices-large-scale-clusters) in "Planning large clusters".
  * Any resource limits that you set for the cluster when you enable node auto-provisioning also apply to the node pools that GKE creates for ComputeClasses.
  * The following settings aren't supported by ComputeClasses: 
    * Surge upgrades or blue-green upgrades.
    * Node integrity and secure boot.
  * To enable node pool auto-creation for a [ComputeClass](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) in GKE versions earlier than 1.33.3-gke.1136000, you must also enable cluster-level node auto-provisioning. This limitation doesn't apply in GKE version 1.33.3-gke.1136000 and later.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Requirements

You can enable node pool auto-creation for your entire cluster in any GKE version by using the node auto-provisioning feature. If you want to use a ComputeClass to enable node pool auto-creation at the workload level, and you don't want to enable node auto-provisioning, your cluster must be at GKE version 1.33.3-gke.1136000 or later.

To trigger node pool auto-creation for specific node configurations, you must meet the corresponding version requirements. For more information about version support for various configurations, see [GKE release notes (new features)](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-new-features) or the documentation for your use case.

## Enable workload-level auto-creation

You can enable node pool auto-creation for specific workloads in the cluster by using a ComputeClass. The `nodePoolAutoCreation` field in a ComputeClass specification controls whether GKE can create new node pools for Pods that select that ComputeClass. In GKE version 1.33.3-gke.1136000 and later, you can enable node pool auto-creation for a ComputeClass even if the cluster doesn't have node auto-provisioning enabled. In versions earlier than 1.33.3-gke.1136000, you must also enable cluster-level node auto-provisioning.

To enable node pool auto-creation for a ComputeClass, follow these steps:

  1. Use a new or existing Standard cluster with version 1.33.3-gke.1136000 or later.

You can optionally [create a new Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster).

  2. If your cluster doesn't meet the requirements in the preceding step, enable cluster-level node auto-provisioning.

  3. Save the following example ComputeClass as a YAML file:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: COMPUTE_CLASS
         spec:
           priorities:
           -  machineFamily: n4
           -  machineFamily: n2
           whenUnsatisfiable: ScaleUpAnyway
           **nodePoolAutoCreation :
             enabled: true**
         

Replace `COMPUTE_CLASS` with a name for the new ComputeClass. For more information about the available fields in ComputeClasses, see the [ComputeClass CustomResourceDefinition](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass).

  4. Apply the ComputeClass manifest to the cluster:
         
         kubectl apply -f PATH_TO_COMPUTECLASS_MANIFEST
         

Replace `PATH_TO_COMPUTECLASS_MANIFEST` with the path to the ComputeClass manifest file. 

  5. Save the following example Deployment, which selects a ComputeClass, as `helloweb-deploy.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: helloweb
           labels:
             app: hello
         spec:
           selector:
             matchLabels:
               app: hello
           template:
             metadata:
               labels:
                 app: hello
             spec:
               nodeSelector:
                 # Replace with the name of a compute class
                 cloud.google.com/compute-class: COMPUTE_CLASS 
               containers:
               - name: hello-app
                 image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
                 ports:
                 - containerPort: 8080
                 resources:
                   requests:
                     cpu: "250m"
                     memory: "1Gi"

  6. Create the Deployment in the cluster:
         
         kubectl apply -f helloweb-deploy.yaml
         

  7. To verify that GKE created a new node pool for your Pod, get a list of the node pools in your cluster:
         
         gcloud container node-pools list \
             --cluster=CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `CONTROL_PLANE_LOCATION`: the region or zone of the cluster control plane, such as `us-central1` or `us-central1-a`.



## Enable cluster-level node auto-provisioning

To enable node pool auto-creation for your entire GKE cluster, use the _node auto-provisioning_ setting. Node auto-provisioning lets GKE create new node pools for pending workloads across the cluster based on the configuration in the Pod specification or in a ComputeClass. You can enable node auto-provisioning for new or existing clusters.

Before you enable node auto-provisioning, plan the size of the primary IPv4 address range of your VPC subnet. GKE uses this IP address range as the primary node IP address range. Depending on the size and scale of your cluster, the default node IP address range might not have enough IP addresses to assign to new nodes. If you update the size of the node IP address range after you create your cluster, you must update the [GKE cluster firewall rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules) to allow traffic from the new IP addresses.

To get auto-created node pools in GKE versions earlier than 1.33.3-gke.1136000, you must do the steps in this section. You can also enable node auto-provisioning for an existing cluster by editing the cluster configuration in the Google Cloud console.

**Caution:** If you enable node auto-provisioning for an existing cluster, pending workloads that have compatible node selectors or ComputeClass configurations might trigger node pool auto-creation. Validate your existing workload specifications to minimize the risk of unintended autoscaling.

To enable node auto-provisioning when you create a new cluster, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. On the **Cluster basics** page, specify a name and a location for your new cluster.

  3. In the navigation pane, click **Advanced settings**.

  4. In the **Node autoprovisioning** row, click _edit_ **Edit configuration**.

  5. Select the **Enable node auto-provisioning** checkbox. A **Limits** section appears.

  6. Specify limits for CPU and memory.

  7. Click **Save**.

  8. Click **Create**.




###  gcloud 
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --enable-autoprovisioning \
        --min-cpu=MINIMUM_CPU \
        --min-memory=MINIMUM_MEMORY \
        --max-cpu=MAXIMUM_CPU \
        --max-memory=MAXIMUM_MEMORY \
        --autoprovisioning-scopes=https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/devstorage.read_only
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster to enable node auto-provisioning.
  * `CONTROL_PLANE_LOCATION`: the region or zone of the cluster control plane, such as `us-central1` or `us-central1-a`.
  * `MINIMUM_CPU`: the minimum number of cores in the cluster.
  * `MINIMUM_MEMORY`: the minimum memory capacity, in GiB, in the cluster.
  * `MAXIMUM_CPU`: the maximum number of cores in the cluster. This limit applies to the sum of CPU cores across all of the new and existing nodes in the cluster, including manually created node pools.
  * `MAXIMUM_MEMORY`: the maximum memory capacity, in GiB, in the cluster. This limit applies to the sum of memory capacity across all of the new and existing node pools in the cluster, including manually created node pools.



### Configure settings with a node auto-provisioning configuration file

You can configure resource limits and node configuration settings for node auto-provisioning by using a YAML configuration file. The configuration file lets you declaratively specify default values for auto-created node pools and lets you perform advanced configuration, such as enabling node auto-repair. This file isn't related to ComputeClasses, which are Kubernetes custom resources. Instead, the configuration file exists as a more extensible alternative to using command-line flags to specify settings for node auto-provisioning. For more information, see [Cluster-level default settings with a configuration file](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning#cluster-level-default).

To create and use a configuration file, follow these steps:

  1. In a text editor, create a YAML file in a path that the Google Cloud CLI can access.
  2. Add the configurations that you want to set or modify, such as in the following example:
         
         resourceLimits:
           - resourceType: 'cpu'
             minimum: 4
             maximum: 10
           - resourceType: 'memory'
             maximum: 64
           - resourceType: 'nvidia-tesla-t4'
             maximum: 4
         management:
           autoRepair: true
           autoUpgrade: true
         shieldedInstanceConfig:
           enableSecureBoot: true
           enableIntegrityMonitoring: true
         

This example has the following settings for node auto-provisioning:

     * `resourceLimits`: sets resource limits for CPU, memory capacity, and NVIDIA T4 GPUs in the cluster. These limits apply to the sum of the resource capacity in the cluster, including in manually created node pools.
     * `management`: enables node auto-repair and node auto-upgrade for all new auto-created node pools in the cluster.
     * `shieldedInstanceConfig`: enables secure boot and node integrity monitoring for all new auto-created node pools in the cluster.
  3. Provide the configuration file to GKE by specifying the `--autoprovisioning-config-file` flag and the `--enable-autoprovisioning` flag for a new or existing cluster:
         
         gcloud container clusters create CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --enable-autoprovisioning \
             **--autoprovisioning-config-file =PATH_TO_CONFIGURATION_FILE**
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `PATH_TO_CONFIGURATION_FILE`: the path to the configuration file. 



After you apply the configuration file to the cluster, GKE uses the settings in the file for new auto-created node pools in the cluster. These settings don't apply to existing node pools that GKE created in the cluster.

### Configure resource limits for node auto-provisioning

When you use cluster-level node auto-provisioning, you must configure limits for the total amount of resources that your cluster can have across all of its node pools. To enable node auto-provisioning for a cluster, you must specify limits for CPU and memory capacity in the cluster. Additionally, to use other types of attached resources like GPUs and TPUs, you must specify limits for those resources. These limits are required only if you enable the node auto-provisioning setting for your cluster. If you use only ComputeClasses to get auto-created node pools, you don't need to configure resource limits.

You can alternatively configure resource limits that target subsets of nodes, such as nodes that are created for a ComputeClass or nodes that use a specific machine family. For more information, see [Configure granular resource limits](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-capacity-quotas).

You can add or modify resource limits for node pool auto-creation by using one of the following methods:

  * The Google Cloud console
  * gcloud CLI flags
  * The cluster-level configuration file



To configure resource limits for an existing cluster, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster. The **Cluster details** page opens.

  3. Click the **Details** tab.

  4. In the **Automation** section, in the **Node auto-provisioning** row, click edit **Edit**. The **Edit node auto-provisioning** pane opens.

  5. Select the **Enable node auto-provisioning** checkbox.

  6. In the **Limits** section, specify minimum and maximum values for CPU and memory capacity in the cluster.

  7. To configure limits for another resource, like GPUs or TPUs, do the following:

     1. Click **Add resource**.
     2. From the **Resource type** drop-down list, select the GPU model or TPU machine type, such as **NVIDIA A100 80GB** or **ct5p**.
     3. Specify minimum and maximum values for the resource.
  8. Optional: In the **Node pool locations** section, select specific zones for GKE to create nodes in. For example, if you plan to run GPU workloads, select zones that have high availability for your selected GPU type.

  9. Click **Save changes**.




###  gcloud 

Run one of the following commands:

  * Specify CPU and memory resource limits:
        
        gcloud container clusters update CLUSTER_NAME \
            --location=CONTROL_PLANE_LOCATION \
            --enable-autoprovisioning \
            **--min-cpu =MINIMUM_CPU \
            --min-memory=MINIMUM_MEMORY \
            --max-cpu=MAXIMUM_CPU \
            --max-memory=MAXIMUM_MEMORY**
        

Replace the following:

    * `MINIMUM_CPU`: the minimum number of cores in the cluster.
    * `MINIMUM_MEMORY`: the minimum memory capacity, in GiB, in the cluster.
    * `MAXIMUM_CPU`: the maximum number of cores in the cluster. This limit applies to the sum of CPU cores across all of the node pools in the cluster, including manually created node pools.
    * `MAXIMUM_MEMORY`: the maximum memory capacity, in GiB, in the cluster. This limit applies to the sum of memory capacity across all of the node pools in the cluster, including manually created node pools.
  * Specify GPU resource limits:
        
        gcloud container clusters update CLUSTER_NAME \
            --location=CONTROL_PLANE_LOCATION \
            --enable-autoprovisioning \
            --min-cpu=MINIMUM_CPU \
            --min-memory=MINIMUM_MEMORY \
            --max-cpu=MAXIMUM_CPU \
            --max-memory=MAXIMUM_MEMORY \
            **--min-accelerator =type=GPU_TYPE,count=MINIMUM_GPU_COUNT \
            --max-accelerator=type=GPU_TYPE,count=MAXIMUM_GPU_COUNT**
        

Replace the following:

    * `GPU_TYPE`: the type of GPU to set a limit for, such as `nvidia-l4`.
    * `MINIMUM_GPU_COUNT`: the minimum number of GPUs of the specified type that the cluster can have.
    * `MAXIMUM_GPU_COUNT`: the maximum number of GPUs of the specified type that the cluster can have.
  * Specify TPU resource limits:
        
        gcloud container clusters update CLUSTER_NAME \
            --location=CONTROL_PLANE_LOCATION \
            --enable-autoprovisioning \
            --min-cpu=MINIMUM_CPU \
            --min-memory=MINIMUM_MEMORY \
            --max-cpu=MAXIMUM_CPU \
            --max-memory=MAXIMUM_MEMORY \
            **--min-accelerator =type=TPU_TYPE,count=MINIMUM_TPU_COUNT \
            --max-accelerator=type=TPU_TYPE,count=MAXIMUM_TPU_COUNT**
        

Replace the following:

    * `TPU_TYPE`: the type of TPU to set a limit for. The following values are supported: 
      * `tpu-v4-podslice`: TPU v4.
      * `tpu-v5-lite-podslice`: TPU v5e with machine types that start with `ct5lp-`.
      * `tpu-v5p-slice`: TPU v5e with machine types that start with `ct5p-`.
      * `tpu-v6e-slice`: TPU Trillium.
    * `MINIMUM_TPU_COUNT`: the minimum number of TPU chips of the specified type that the cluster can have. If the value that you specify is larger than the number of TPU chips in a multi-host TPU slice, your TPU slice might not scale down.
    * `MAXIMUM_TPU_COUNT`: the maximum number of TPU chips of the specified type that the cluster can have. For multi-host TPU slices, specify a value that's greater than the number of chips in each slice so that GKE can scale the slice atomically. The number of chips in a slice is the product of the TPU topology. For example, if the topology is `2x2x2`, the number of chips in the slice is `8`, which means that the value of MAXIMUM_TPU_COUNT must be greater than `8`.



### Configuration file

  1. In your configuration file, specify one of the following sets of fields in the `resourceLimits` field:

     * Specify CPU and memory resource limits:
           
           resourceLimits:
             - resourceType: 'cpu'
               minimum: MINIMUM_CPU
               maximum: MAXIMUM_CPU
             - resourceType: 'memory'
               minimum: MINIMUM_MEMORY
               maximum: MAXIMUM_MEMORY
           

Replace the following:

       * `MINIMUM_CPU`: the minimum number of cores in the cluster.
       * `MINIMUM_MEMORY`: the minimum memory capacity, in GiB, in the cluster.
       * `MAXIMUM_CPU`: the maximum number of cores in the cluster. This limit applies to the sum of CPU cores across all of the node pools in the cluster, including manually created node pools.
       * `MAXIMUM_MEMORY`: the maximum memory capacity, in GiB, in the cluster. This limit applies to the sum of memory capacity across all of the node pools in the cluster, including manually created node pools.
     * Specify GPU resource limits:
           
           resourceLimits:
             - resourceType: 'cpu'
               minimum: MINIMUM_CPU
               maximum: MAXIMUM_CPU
             - resourceType: 'memory'
               minimum: MINIMUM_MEMORY
               maximum: MAXIMUM_MEMORY
             **- resourceType: 'GPU1_TYPE'
               minimum: MINIMUM_GPU1_COUNT
               maximum: MAXIMUM_GPU1_COUNT
             - resourceType: 'GPU2_TYPE'
               minimum: MINIMUM_GPU2_COUNT
               maximum: MAXIMUM_GPU2_COUNT**
           

Replace the following:

       * `GPU1_TYPE`,`GPU2_TYPE`: the types of GPUs to set limits for, such as `nvidia-l4`.
       * `MINIMUM_GPU1_COUNT`,`MINIMUM_GPU2_COUNT`: the minimum number of GPUs of the specified types that the cluster can have.
       * `MAXIMUM_GPU1_COUNT`,`MAXIMUM_GPU2_COUNT`: the maximum number of GPUs of the specified types that the cluster can have.
     * Specify TPU resource limits:
           
           resourceLimits:
             - resourceType: 'cpu'
               minimum: MINIMUM_CPU
               maximum: MAXIMUM_CPU
             - resourceType: 'memory'
               minimum: MINIMUM_MEMORY
               maximum: MAXIMUM_MEMORY
             **- resourceType: 'TPU1_TYPE'
               minimum: MINIMUM_TPU1_COUNT
               maximum: MAXIMUM_TPU1_COUNT
             - resourceType: 'TPU2_TYPE'
               minimum: MINIMUM_TPU2_COUNT
               maximum: MAXIMUM_TPU2_COUNT**
           

Replace the following:

       * `TPU1_TYPE`,`TPU2_TYPE`: the types of TPUs to set limits for. The following values are supported: 
         * `tpu-v4-podslice`: TPU v4.
         * `tpu-v5-lite-podslice`: TPU v5e with machine types that start with `ct5lp-`.
         * `tpu-v5p-slice`: TPU v5e with machine types that start with `ct5p-`.
         * `tpu-v6e-slice`: TPU Trillium.
       * `MINIMUM_TPU1_COUNT`,`MINIMUM_TPU2_COUNT`: the minimum number of TPU chips of the specified type that the cluster can have. If the value that you specify is larger than the number of TPU chips in a multi-host TPU slice, your TPU slice might not scale down.
       * `MAXIMUM_TPU1_COUNT`,`MAXIMUM_TPU2_COUNT`: the maximum number of TPU chips of the specified type that the cluster can have. For multi-host TPU slices, specify a value that's greater than the number of chips in each slice so that GKE can scale the slice atomically. The number of chips in a slice is the product of the TPU topology. For example, if the topology for `TPU1_TYPE` is `2x2x2`, the number of chips in the slice is `8`, which means that the value of `MAXIMUM_TPU1_COUNT` must be greater than `8`.
  2. Provide the configuration file to GKE by specifying the `--autoprovisioning-config-file` flag and the `--enable-autoprovisioning` flag for a new or existing cluster:
         
         gcloud container clusters create CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --enable-autoprovisioning \
             **--autoprovisioning-config-file =PATH_TO_CONFIGURATION_FILE**
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `PATH_TO_CONFIGURATION_FILE`: the path to the configuration file. 



### Mark existing node pools as auto-created

After you enable cluster-level node auto-provisioning, you can mark any existing node pools in the cluster as auto-created. GKE manages scaling in these node pools, including deleting the node pools when they're empty. You can mark manually created node pools as auto-created to let GKE manage the node pools for you.

If you disable auto-provisioning for your cluster, GKE stops managing all existing auto-created node pools in the cluster. If you re-enable auto-provisioning for the cluster later, GKE doesn't automatically resume the management of those existing node pools. You must mark those existing node pools as auto-created.

To mark an existing node pool as auto-created, run the following command:
    
    
    gcloud container node-pools update NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --enable-autoprovisioning
    

Replace `NODE_POOL_NAME` with the name of the node pool.

## Configure default settings for auto-created node pools

GKE uses your ComputeClasses and Pod specifications to determine the types of nodes that can optimally run your pending Pods. You can optionally configure default settings that GKE applies to auto-created node pools, such as a custom Identity and Access Management (IAM) service account for the nodes or custom boot disk configurations. These default settings override any corresponding default values that Google sets for your clusters. For example, you can set an Ubuntu node image as the default for auto-created node pools, which overrides the GKE default Container-Optimized OS node image.

You can configure default settings at the cluster level by using node auto-provisioning or at the workload level in ComputeClasses. Before you configure a setting at one of these levels, consider the following:

  * The cluster-level settings apply to any auto-created node pool in the cluster, and the ComputeClass settings apply only to workloads that use that ComputeClass.
  * If you specify the same default setting in a ComputeClass and at the cluster level, GKE uses the ComputeClass setting for workloads that use the ComputeClass.
  * Any default values that you configure apply only to _new_ auto-created node pools. Existing node pools aren't affected.



The following sections show you how to configure specific default settings.

### Set the default node image

Select one of the following options:

### ComputeClass

  1. In a ComputeClass manifest, use the [`nodePoolConfig.imageType`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#nodepoolconfig) field. This field is available in GKE version 1.32.4-gke.1198000 and later.
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: COMPUTE_CLASS
         spec:
           priorities:
           - machineFamily: n4
           - machineFamily: n4d
           **nodePoolConfig :
             imageType: IMAGE_TYPE**
           whenUnsatisfiable: ScaleUpAnyway
           nodePoolAutoCreation:
             enabled: true
         

Replace `IMAGE_TYPE` with a value for the [node image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images), which can be one of the following:

     * `cos_containerd`: Container-Optimized OS with containerd.
     * `ubuntu_containerd`: Ubuntu with containerd.
  2. Apply the ComputeClass manifest to the cluster:
         
         kubectl apply -f PATH_TO_COMPUTECLASS_MANIFEST
         

Replace `PATH_TO_COMPUTECLASS_MANIFEST` with the path to the ComputeClass manifest file. 




###  gcloud 

To set the default node image on the command-line, use the [\--`autoprovisioning-image-type`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update#--autoprovisioning-image-type) flag:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --enable-autoprovisioning \
        **--autoprovisioning-image-type =IMAGE_TYPE**
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `IMAGE_TYPE`: the [node image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images), which can be one of the following: 
    * `cos_containerd`: Container-Optimized OS with containerd.
    * `ubuntu_containerd`: Ubuntu with containerd.



To set the default node image in a configuration file, follow these steps:

  1. In your configuration file, specify the `imageType` field:
         
         imageType: 'IMAGE_TYPE'
         

If your configuration file has other settings, don't modify those settings. Any modifications or removals in the configuration file also modify the corresponding cluster-level settings. 

  2. Provide the configuration file to GKE by specifying the `--autoprovisioning-config-file` flag and the `--enable-autoprovisioning` flag for a new or existing cluster:
         
         gcloud container clusters create CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --enable-autoprovisioning \
             **--autoprovisioning-config-file =PATH_TO_CONFIGURATION_FILE**
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `PATH_TO_CONFIGURATION_FILE`: the path to the configuration file. 



### Set the default IAM service account for nodes

GKE nodes use an [IAM service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#default-gke-service-agent) for system tasks like logging and monitoring. To change the IAM service account for auto-created node pools, select one of the following options:

### ComputeClass

  1. In a Computeclass manifest, use the [`nodePoolConfig.serviceAccount`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#nodepoolconfig) field. This field is available in GKE version 1.31.4-gke.1072000 and later.
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: COMPUTE_CLASS
         spec:
           priorities:
           - machineFamily: n4
           - machineFamily: n4d
           **nodePoolConfig :
             serviceAccount: SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com**
           whenUnsatisfiable: ScaleUpAnyway
           nodePoolAutoCreation:
             enabled: true
         

Replace the following:

     * `SERVICE_ACCOUNT_NAME`: the name of the IAM service account, like `my-node-account`.
     * `PROJECT_ID`: the project ID of the service account project.
  2. Apply the ComputeClass manifest to the cluster:
         
         kubectl apply -f PATH_TO_COMPUTECLASS_MANIFEST
         

Replace `PATH_TO_COMPUTECLASS_MANIFEST` with the path to the ComputeClass manifest file. 




###  gcloud 

When you use the gcloud CLI to configure a default service account for auto-created node pools, you must also specify [access scopes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-scopes#standard-scopes) that the node pools require to function correctly.

To set the default service account and access scopes on the command-line, use the [\--`autoprovisioning-service-account`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update#--autoprovisioning-service-account) and the [\--`autoprovisioning-scopes`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update#--autoprovisioning-scopes) flags:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --enable-autoprovisioning \
        **--autoprovisioning-service-account =SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
        --autoprovisioning-scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/trace.append**
    

Replace the following:

  * `SERVICE_ACCOUNT_NAME`: the name of the IAM service account, like `my-node-account`.
  * `PROJECT_ID`: the project ID of the service account project.



To set the default service account and access scopes in a configuration file, follow these steps:

  1. In your configuration file, specify the `serviceAccount` and `scopes` fields:
         
         serviceAccount: SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com
         scopes: https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/trace.append
         

If your configuration file has other settings, don't modify those settings. Any modifications or removals in the configuration file also modify the corresponding cluster-level settings. 

  2. Provide the configuration file to GKE by specifying the `--autoprovisioning-config-file` flag and the `--enable-autoprovisioning` flag for a new or existing cluster:
         
         gcloud container clusters create CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --enable-autoprovisioning \
             **--autoprovisioning-config-file =PATH_TO_CONFIGURATION_FILE**
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `PATH_TO_CONFIGURATION_FILE`: the path to the configuration file. 



### Set the default zones for auto-created nodes

By default, GKE auto-creates nodes in the following zones, depending on the type of cluster:

  * **Regional clusters** : GKE creates nodes in three random zones in the cluster region.
  * **Zonal clusters** : GKE creates nodes in the same zone as the cluster control plane.



You can manually specify a list of zones where GKE auto-creates nodes. These zones must be in the same region as the cluster control plane. For example, if you have a zonal cluster with the control plane in `us-central1-a`, you can specify any zones in the `us-central1` region for GKE to auto-create nodes. If you modify the default zones for auto-created nodes in an existing cluster, the changes apply only to new node pools that GKE creates.

To specify the default zones for auto-created nodes, select one of the following options:

### ComputeClass

  1. In a ComputeClass manifest, use the [`spec.priorityDefaults.location.zones`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#priorityDefaults) field. This field is available in GKE version 1.33.1-gke.1545000 and later.
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: COMPUTE_CLASS
         spec:
           **priorityDefaults :
             location:
               zones: ['ZONE1','ZONE2','...']**
           priorities:
           - machineFamily: n4
           - machineFamily: n4d
           whenUnsatisfiable: ScaleUpAnyway
           nodePoolAutoCreation:
             enabled: true
         

Replace `ZONE1,ZONE2,...` with a comma-separated list of the default zones for auto-created nodes, such as '`us-central1-a','us-central1-b', 'us-central1-f'`. GKE uses these zones if specific rules in the `spec.priorities` field don't include an explicit list of zones. 

Optional: If you are provisioning TPU VMs, use an [AI zone](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones), like `us-central1-ai1a`. AI zones are specialized locations that are optimized for AI/ML workloads within Google Cloud regions.

  2. Apply the ComputeClass manifest to the cluster:
         
         kubectl apply -f PATH_TO_COMPUTECLASS_MANIFEST
         

Replace `PATH_TO_COMPUTECLASS_MANIFEST` with the path to the ComputeClass manifest file. 




###  gcloud 

To set the default zones for node pool auto-creation on the command-line, use the [\--`autoprovisioning-locations`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update#--autoprovisioning-locations) flag:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --enable-autoprovisioning \
        **--autoprovisioning-locations =ZONE1,ZONE2,...**
    

Replace `ZONE1,ZONE2,...` with a comma-separated list of the default zones for auto-created nodes, such as '`us-central1-a','us-central1-b', 'us-central1-f'`.

To set the default zones for node pool auto-creation by using a configuration file, follow these steps:

  1. Specify the `autoprovisioningLocations` field in the configuration file:
         
         autoprovisioningLocations:
         - ZONE1
         - ZONE2
         

Replace `ZONE1`,`ZONE2` with the default zones for auto-created nodes, such as '`us-central1-a`' and '`us-central1-b`'.

If your configuration file has other settings, don't modify those settings. Any modifications or removals in the configuration file also modify the corresponding cluster-level settings. 

  2. Provide the configuration file to GKE by specifying the `--autoprovisioning-config-file` flag and the `--enable-autoprovisioning` flag for a new or existing cluster:
         
         gcloud container clusters create CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --enable-autoprovisioning \
             **--autoprovisioning-config-file =PATH_TO_CONFIGURATION_FILE**
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `PATH_TO_CONFIGURATION_FILE`: the path to the configuration file. 



### Set customer-managed encryption keys for boot disk encryption

You can specify a [customer managed encryption key (CMEK)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek) in Cloud Key Management Service that GKE uses to encrypt the boot disks of nodes in auto-created node pools. You must [create the key](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek) before you use it with node pool auto-creation. To set a CMEK for your node boot disks, select one of the following options:

### ComputeClass

In ComputeClasses, you must specify the key in every priority rule in the `spec.priorities` field in the ComputeClass.

  1. In a ComputeClass manifest, use the [`priorities.storage.bootDiskKMSKey`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#storage) field:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: COMPUTE_CLASS
         spec:
           priorities:
           - machineFamily: n4
             **storage :
               bootDiskKMSKey: projects/KEY_PROJECT_ID/locations/KEY_LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME**
           - machineFamily: n4d
             **storage :
               bootDiskKMSKey: projects/KEY_PROJECT_ID/locations/KEY_LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME**
           whenUnsatisfiable: ScaleUpAnyway
           nodePoolAutoCreation:
             enabled: true
         

Replace the following:

     * `KEY_PROJECT_ID`: the project ID of the project that has the key.
     * `KEY_LOCATION`: the location of the key ring.
     * `KEY_RING`: the name of the key ring that contains the key.
     * `KEY_NAME`: the name of the key.
  2. Apply the ComputeClass manifest to the cluster:
         
         kubectl apply -f PATH_TO_COMPUTECLASS_MANIFEST
         

Replace `PATH_TO_COMPUTECLASS_MANIFEST` with the path to the ComputeClass manifest file. 




###  gcloud 

  1. Specify the `bootDiskKmsKey` field in the configuration file:
         
         bootDiskKmsKey: projects/KEY_PROJECT_ID/locations/KEY_LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME
         

Replace the following:

     * `KEY_PROJECT_ID`: the project ID of the project that has the key.
     * `KEY_LOCATION`: the location of the key ring.
     * `KEY_RING`: the name of the key ring that contains the key.
     * `KEY_NAME`: the name of the key.

If your configuration file has other settings, don't modify those settings. Any modifications or removals in the configuration file also modify the corresponding cluster-level settings. 

  2. Provide the configuration file to GKE by specifying the `--autoprovisioning-config-file` flag and the `--enable-autoprovisioning` flag for a new or existing cluster:
         
         gcloud container clusters create CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --enable-autoprovisioning \
             **--autoprovisioning-config-file =PATH_TO_CONFIGURATION_FILE**
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `PATH_TO_CONFIGURATION_FILE`: the path to the configuration file. 



### Configure node integrity and secure boot

You can enable [secure boot and integrity monitoring](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes) for auto-created node pools only by using the node auto-provisioning configuration file.

  1. Specify the `shieldedInstanceConfig` field in the configuration file:
         
         shieldedInstanceConfig:
           enableSecureBoot: true
           enableIntegrityMonitoring: true
         

If your configuration file has other settings, don't modify those settings. Any modifications or removals in the configuration file also modify the corresponding cluster-level settings. 

  2. Provide the configuration file to GKE by specifying the `--autoprovisioning-config-file` flag and the `--enable-autoprovisioning` flag for a new or existing cluster:
         
         gcloud container clusters create CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --enable-autoprovisioning \
             **--autoprovisioning-config-file =PATH_TO_CONFIGURATION_FILE**
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `PATH_TO_CONFIGURATION_FILE`: the path to the configuration file. 



### Configure node auto-repair and auto-upgrade

You can modify settings for [node auto-repairs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair) and [node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades) in auto-created node pools. These features are enabled by default in all GKE clusters and node pools. We recommend that you keep these features enabled to improve reliability and stability in your clusters.

**Warning:** Disabling auto-upgrades when the cluster is enrolled in a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) can result in GKE failing to create new node pools.

To change node auto-repair and node auto-upgrade settings, select one of the following options:

### ComputeClass

  1. In a ComputeClass manifest, use the `autoRepair` field and the `autoUpgrade` field in the [`spec.nodePoolConfig`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#nodepoolconfig) field. These fields are available in GKE version 1.34.0-gke.2201000 and later.
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: COMPUTE_CLASS
         spec:
           **nodePoolConfig :
             autoRepair: true
             autoUpgrade: true**
           priorities:
           - machineFamily: n4
           - machineFamily: n4d
           whenUnsatisfiable: ScaleUpAnyway
           nodePoolAutoCreation:
             enabled: true
         

  2. Apply the ComputeClass manifest to the cluster:
         
         kubectl apply -f PATH_TO_COMPUTECLASS_MANIFEST
         

Replace `PATH_TO_COMPUTECLASS_MANIFEST` with the path to the ComputeClass manifest file. 




###  gcloud 

  * To enable auto-repair and auto-upgrade settings on the command-line, use the [`--enable-autoprovisioning-autorepair`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update#--enable-autoprovisioning-autorepair) and the [`--enable-autoprovisioning-autoupgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update#--enable-autoprovisioning-autoupgrade) flags:
        
        gcloud container clusters update CLUSTER_NAME \
            --location=CONTROL_PLANE_LOCATION \
            --enable-autoprovisioning \
            **--enable-autoprovisioning-autorepair \
            --enable-autoprovisioning-autoupgrade**
        

  * To disable auto-repair and auto-upgrade settings on the command-line, use the `--no-enable-autoprovisioning-autorepair` and the `--no-enable-autoprovisioning-autoupgrade` flags:
        
        gcloud container clusters update CLUSTER_NAME \
            --location=CONTROL_PLANE_LOCATION \
            --enable-autoprovisioning \
            **--no-enable-autoprovisioning-autorepair \
            --no-enable-autoprovisioning-autoupgrade**
        

  * To modify settings for node auto-repair and auto-upgrade by using a configuration file, follow these steps:

    1. Specify the `management.autoRepair` and the `management.autoUpgrade` fields in the configuration file:
           
           management:
             autoRepair: true
             autoUpgrade: true
           

If your configuration file has other settings, don't modify those settings. Any modifications or removals in the configuration file also modify the corresponding cluster-level settings. 

    2. Provide the configuration file to GKE by specifying the `--autoprovisioning-config-file` flag and the `--enable-autoprovisioning` flag for a new or existing cluster:
           
           gcloud container clusters create CLUSTER_NAME \
               --location=CONTROL_PLANE_LOCATION \
               --enable-autoprovisioning \
               **--autoprovisioning-config-file =PATH_TO_CONFIGURATION_FILE**
           

Replace the following:

       * `CLUSTER_NAME`: the name of the cluster.
       * `PATH_TO_CONFIGURATION_FILE`: the path to the configuration file. 



### Configure surge upgrade settings

You can specify [surge upgrade settings](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge) in auto-created node pools. Surge upgrades are the default GKE [node upgrade strategy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies). To change surge upgrade settings, you must configure cluster-level node auto-provisioning.

  * To specify surge upgrade settings on the command line, use the [`--autoprovisioning-max-surge-upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update#--autoprovisioning-max-surge-upgrade) and the [`--autoprovisioning-max-unavailable-upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update#--autoprovisioning-max-unavailable-upgrade) flags:
        
        gcloud container clusters update CLUSTER_NAME \
            --location=CONTROL_PLANE_LOCATION \
            --enable-autoprovisioning \
            **--autoprovisioning-max-surge-upgrade =MAX_SURGE \
            --autoprovisioning-max-unavailable-upgrade=MAX_UNAVAILABLE**
        

Replace the following:

    * `MAX_SURGE`: the maximum number of nodes that can be added to the node pool during upgrades.
    * `MAX_UNAVAILABLE`: the maximum number of nodes in the node pool that can be simultaneously unavailable during upgrades.
  * To specify surge upgrade settings by using a configuration file, follow these steps:

    1. Specify the `upgradeSettings.maxSurgeUpgrade` and the `upgradeSettings.maxUnavailableUpgrade` fields in the configuration file:
           
           upgradeSettings:
             maxSurgeUpgrade: MAX_SURGE
             maxUnavailableUpgrade: MAX_UNAVAILABLE
           

If your configuration file has other settings, don't modify those settings. Any modifications or removals in the configuration file also modify the corresponding cluster-level settings. 

    2. Provide the configuration file to GKE by specifying the `--autoprovisioning-config-file` flag and the `--enable-autoprovisioning` flag for a new or existing cluster:
           
           gcloud container clusters create CLUSTER_NAME \
               --location=CONTROL_PLANE_LOCATION \
               --enable-autoprovisioning \
               **--autoprovisioning-config-file =PATH_TO_CONFIGURATION_FILE**
           

Replace the following:

       * `CLUSTER_NAME`: the name of the cluster.
       * `PATH_TO_CONFIGURATION_FILE`: the path to the configuration file. 



The surge upgrade settings that you specify apply only if your cluster uses surge upgrades to upgrade auto-created node pools. To switch your node upgrade strategy to surge upgrades for new auto-created node pools, run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --enable-autoprovisioning \
        **--enable-autoprovisioning-surge-upgrade**
    

When you switch the upgrade strategy, GKE uses any settings that you previously configured for that upgrade strategy.

### Use blue-green upgrades for new auto-created node pools

You can switch your node upgrade strategy to [blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#blue-green-upgrade-strategy) for all new auto-created node pools and tune the default settings for blue-green upgrades. To change your upgrade strategy, you must configure cluster-level node auto-provisioning. Any changes that you make apply only to new auto-created node pools. You can also [update existing auto-created node pools to use blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pool-upgrade-strategies#update-node-pool-blue-green). You can't use [autoscaled blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#autoscaled-blue-green-upgrade-strategy) ([Preview](https://cloud.google.com/products#product-launch-stages)) with auto-created node pools.

  * To use blue-green upgrades and the GKE default settings for new auto-created node pools, run the following command:
        
        gcloud container clusters update CLUSTER_NAME \
            --location=CONTROL_PLANE_LOCATION
            --enable-autoprovisioning \
            **--enable-autoprovisioning-blue-green-upgrade**
        

  * To use blue-green upgrades and configure your own default settings for new auto-created node pools, run the following command:
        
        gcloud container clusters update CLUSTER_NAME \
            --location=CONTROL_PLANE_LOCATION \
            --enable-autoprovisioning \
            **--enable-autoprovisioning-blue-green-upgrade \
            --autoprovisioning-node-pool-soak-duration=NODE_POOL_SOAK_DURATION \
            --autoprovisioning-standard-rollout-policy=batch-node-count=BATCH_NODE_COUNT,batch-soak-duration=BATCH_SOAK_DURATION**
        

Replace the following:

    * `NODE_POOL_SOAK_DURATION`: the duration, in seconds, that GKE waits after draining all of the node batches in the blue pool before deleting the blue pool. The default value is `3600`.
    * `BATCH_NODE_COUNT`: the number of nodes to drain in a batch during the blue pool drain phase. The default value is `1`. If you specify a value of `0`, GKE skips the blue pool drain phase.
    * `BATCH_SOAK_DURATION`: the duration, in seconds, that GKE waits to start a batch drain operation after the previous drain operation completes. The default value is `0`.



### Configure custom node boot disks

To specify the type and size of the boot disks that GKE attaches to each node VM in an auto-created node pool, select one of the following options:

### ComputeClass

  1. Use the `bootDiskType` and the `bootDiskSize` fields in the [`spec.priorities.storage`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#storage) field in a ComputeClass:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: COMPUTE_CLASS
         spec:
           priorities:
           - machineType: n4-standard-16
             **storage :
               bootDiskType: BOOT_DISK_TYPE
               bootDiskSize: BOOT_DISK_SIZE**
           - machineType: n4d-standard-16
             **storage :
               bootDiskType: BOOT_DISK_TYPE
               bootDiskSize: BOOT_DISK_SIZE**
           whenUnsatisfiable: ScaleUpAnyway
           nodePoolAutoCreation:
             enabled: true
         

**Note:** To configure the `bootDiskSize` setting in a ComputeClass without specifying values for the `machineType` or `GPU` fields, you must use GKE version 1.34.1-gke.1431000 and later.

Replace the following:

     * `BOOT_DISK_TYPE`: the disk type to use as the node boot disk. The value that you specify must be supported by the Compute Engine machine type that GKE uses for that priority rule. The value must be one of the following: 
       * `pd-balanced`: balanced Persistent Disk.
       * `pd-standard`: standard Persistent Disk.
       * `pd-ssd`: performance (SSD) Persistent Disk.
       * `hyperdisk-balanced`: Google Cloud Hyperdisk Balanced.
     * `BOOT_DISK_SIZE`: the size, in GiB, of the node boot disk. The minimum value is `10`.
  2. Apply the ComputeClass manifest to the cluster:
         
         kubectl apply -f PATH_TO_COMPUTECLASS_MANIFEST
         

Replace `PATH_TO_COMPUTECLASS_MANIFEST` with the path to the ComputeClass manifest file. 




###  gcloud 

  1. In your configuration file, specify the `diskSizeGb` and the `diskType` fields:
         
         diskSizeGb: BOOT_DISK_SIZE
         diskType: BOOT_DISK_TYPE
         

Replace the following:

     * `BOOT_DISK_TYPE`: the disk type to use as the node boot disk. The value that you specify must be supported by the Compute Engine machine type that GKE uses for that priority rule. The value must be one of the following: 
       * `pd-balanced`: balanced Persistent Disk.
       * `pd-standard`: standard Persistent Disk.
       * `pd-ssd`: performance (SSD) Persistent Disk.
       * `hyperdisk-balanced`: Google Cloud Hyperdisk Balanced.
     * `BOOT_DISK_SIZE`: the size, in GiB, of the node boot disk. The minimum value is `10`.

If your configuration file has other settings, don't modify those settings. Any modifications or removals in the configuration file also modify the corresponding cluster-level settings. 

  2. Provide the configuration file to GKE by specifying the `--autoprovisioning-config-file` flag and the `--enable-autoprovisioning` flag for a new or existing cluster:
         
         gcloud container clusters create CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --enable-autoprovisioning \
             **--autoprovisioning-config-file =PATH_TO_CONFIGURATION_FILE**
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `PATH_TO_CONFIGURATION_FILE`: the path to the configuration file. 



GKE reserves a portion of the node boot disk for system functionality and for ephemeral storage. For more information, see [Ephemeral storage backed by node boot disk](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes#ephemeral_storage_backed_by_node_boot_disk).

## Configure auto-created node pools for common scenarios

The following sections show you how to request auto-created node pools for certain common GKE use cases. For more information about additional use cases and supported configurations, see the documentation for your specific use case.

### Select a machine series or machine type

To select a [supported Compute Engine machine series or machine type](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning#supported_machine_types), select one of the following options:

### ComputeClass

  1. In a ComputeClass manifest, specify either of the following fields in the `spec.priorities` field. You can specify both of these fields in the same ComputeClass manifest, but not in the same priority rule.

     * To select a machine series, specify the `machineFamily` field in a priority rule:
           
           apiVersion: cloud.google.com/v1
           kind: ComputeClass
           metadata:
             name: COMPUTE_CLASS
           spec:
             priorities:
             **- machineFamily: MACHINE_SERIES**
             whenUnsatisfiable: ScaleUpAnyway
             nodePoolAutoCreation:
               enabled: true
           

Replace `MACHINE_SERIES` with a Compute Engine machine series, such as `n4`.

     * To select a machine type, specify the `machineType` field in a priority rule:
           
           apiVersion: cloud.google.com/v1
           kind: ComputeClass
           metadata:
             name: COMPUTE_CLASS
           spec:
             priorities:
             **- machineType: MACHINE_TYPE**
             whenUnsatisfiable: ScaleUpAnyway
             nodePoolAutoCreation:
               enabled: true
           

Replace `MACHINE_TYPE` with a Compute Engine machine type, such as `c4-standard-96`. In GKE version 1.33.2-gke.1111000 and later, you can also specify [custom machine types](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#create) in this field.

You can't specify the `machineFamily` field and the `machineType` field in the same priority rule.

  2. Apply the ComputeClass manifest to the cluster:
         
         kubectl apply -f PATH_TO_COMPUTECLASS_MANIFEST
         

Replace `PATH_TO_COMPUTECLASS_MANIFEST` with the path to the ComputeClass manifest file. 

  3. [Select the ComputeClass in a workload](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-attributes-compute-classes).




### Pod specification

  1. In a Pod manifest, select one of the following node labels:

     * To select a machine series, use the `cloud.google.com/machine-family` node label:
           
           apiVersion: v1
           kind: Pod
           metadata:
             name: machine-series-pod
           spec:
             nodeSelector:
               **cloud.google.com/machine-family : MACHINE_SERIES**
             containers:
             - name: hello-app
               image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
           

Replace `MACHINE_SERIES` with a Compute Engine machine series, such as `n4`.

     * To select a predefined machine type, use the `cloud.google.com/machine-family` and the `node.kubernetes.io/instance-type` node labels:
           
           apiVersion: v1
           kind: Pod
           metadata:
             name: machine-series-pod
           spec:
             nodeSelector:
               **cloud.google.com/machine-family : MACHINE_SERIES
               node.kubernetes.io/instance-type: MACHINE_TYPE**
             containers:
             - name: hello-app
               image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
           

Replace `MACHINE_TYPE` with a Compute Engine machine type in the specified machine series. For example, if you specify `n4` for `MACHINE_SERIES`, you can specify `n4-standard-80` for `MACHINE_TYPE`.

In GKE version 1.33.2-gke.1111000, you can also specify [custom machine types](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#create) in this field.

  2. Create the Pod:
         
         kubectl apply -f PATH_TO_POD_MANIFEST
         

Replace `PATH_TO_POD_MANIFEST` with the path to the Pod manifest.




### Select GPUs

To request GPUs for auto-created node pools, select one of the following options:

### ComputeClass

  1. In a ComputeClass manifest, specify the [`spec.priorities.gpu`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#gpu) field:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: COMPUTE_CLASS
         spec:
           priorities:
           **- gpu:
               type: GPU_TYPE
               count: GPU_COUNT
               driverVersion: DRIVER_VERSION**
           whenUnsatisfiable: DoNotScaleUp
           nodePoolAutoCreation:
             enabled: true
         

Replace the following:

     * `GPU_TYPE`: the [type of GPU](https://docs.cloud.google.com/compute/docs/gpus) to attach, such as `nvidia-l4`.
     * `GPU_COUNT`: the number of GPUs to attach to each node. This value must be at least `1`.
     * `DRIVER_VERSION`: the GPU driver version to install. This value must be `default` or `latest`. This field requires GKE version 1.31.1-gke.1858000 or later.
  2. Apply the ComputeClass manifest to the cluster:
         
         kubectl apply -f PATH_TO_COMPUTECLASS_MANIFEST
         

Replace `PATH_TO_COMPUTECLASS_MANIFEST` with the path to the ComputeClass manifest file. 

  3. Select the ComputeClass in a GPU workload, like in the following example:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: my-gpu-pod
         spec:
           nodeSelector:
             **cloud.google.com/compute-class : nvidia-l4-class**
           containers:
           - name: my-gpu-container
             image: nvidia/cuda:11.0.3-runtime-ubuntu20.04
             command: ["/bin/bash", "-c", "--"]
             args: ["while true; do sleep 600; done;"]
             **resources :
               limits:
               nvidia.com/gpu: 1**
         




### Pod specification

To select GPUs in your Pod specifications, you must configure cluster-level node auto-provisioning and set resource limits for that GPU type. To configure GPU resource limits and select GPUs in your Pods, follow these steps:

  1. Configure cluster-level resource limits for the GPUs that you want to use, as described in the Configure resource limits for node pool auto-creation section.
  2. Select GPUs by using node labels in the Pod specification:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: my-gpu-pod
         spec:
           nodeSelector:
             **cloud.google.com/gke-accelerator : GPU_TYPE
             cloud.google.com/gke-accelerator-count: GPU_COUNT
             cloud.google.com/gke-gpu-driver-version: DRIVER_VERSION**
           containers:
           - name: my-gpu-container
             image: nvidia/cuda:11.0.3-runtime-ubuntu20.04
             command: ["/bin/bash", "-c", "--"]
             args: ["while true; do sleep 600; done;"]
             **resources :
               limits:
               nvidia.com/gpu: GPU_QUANTITY**
         

Replace the following:

     * `GPU_TYPE`: the [type of GPU](https://docs.cloud.google.com/compute/docs/gpus) to attach, such as `nvidia-l4`.
     * `GPU_COUNT`: the number of GPUs to attach to each node. This value must be at least `1`.
     * `DRIVER_VERSION`: the GPU driver version to install. This value must be `default` or `latest`. In GKE version 1.32.2-gke.1297000 and later, GKE automatically installs the `default` driver version. This node label requires GKE version 1.29.2-gke.1108000 or later. For more information, see [Installing drivers using node auto-provisioning with GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#installing_node_auto_provisioning).
     * `GPU_QUANTITY`: the number of GPUs to attach to the Pod. This value must be less than or equal to the value of `GPU_COUNT`.



### Select TPUs

You can request TPUs in ComputeClasses or Pod specifications. This section assumes that you're familiar with [Cloud TPU selection](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning#tpus), and that you know the TPU type, topology, and count that you want to use. The steps that you follow depend on how you select TPUs:

  * **ComputeClasses** : see [Provision TPUs by using custom compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#custom-compute-classes).
  * **Pod specification** : 
    1. Configure cluster-level resource limits for the TPUs that you want to use, as described in the Configure resource limits for node pool auto-creation section.
    2. Configure selectors and resource requests in your Pod specifications, as described in [Run your workload on TPU slice nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#run).



### Limit the run time of auto-created nodes

You can specify a maximum duration after which GKE terminates the auto-created nodes. [Compute Engine restrictions](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime#restrictions) apply to this time limit.

Select one of the following options:

### ComputeClass

  1. In a ComputeClass manifest, use the [`spec.priorities.maxRunDurationSeconds`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#priorities) field. This field is available in GKE version 1.32.1-gke.1159000 and later.
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: COMPUTE_CLASS
         spec:
           priorities:
           - machine-family: n4
             **maxRunDurationSeconds : MAX_RUN_DURATION**
           whenUnsatisfiable: DoNotScaleUp
           nodePoolAutoCreation:
             enabled: true
         

Replace `MAX_RUN_DURATION` with the time, in seconds, that auto-created nodes can run before GKE terminates the nodes.

  2. Apply the ComputeClass manifest to the cluster:
         
         kubectl apply -f PATH_TO_COMPUTECLASS_MANIFEST
         

Replace `PATH_TO_COMPUTECLASS_MANIFEST` with the path to the ComputeClass manifest file. 

  3. [Select the ComputeClass in a workload](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-attributes-compute-classes).




### Pod specification

  1. In your Pod manifest, use a node selector for the `cloud.google.com/gke-max-run-duration-seconds` node label. This node label is available in GKE version 1.31.2-gke.1518000 and later.
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: machine-series-pod
         spec:
           nodeSelector:
             cloud.google.com/machine-family: n4
             **cloud.google.com/gke-max-run-duration-seconds : MAX_RUN_DURATION**
           containers:
           - name: hello-app
             image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
         

Replace `MAX_RUN_DURATION` with the time, in seconds, that auto-created nodes can run before GKE terminates the nodes.

  2. Create the Pod:
         
         kubectl apply -f PATH_TO_POD_MANIFEST
         

Replace `PATH_TO_POD_MANIFEST` with the path to the Pod manifest.




### Specify a minimum CPU platform

Node auto-provisioning supports creating node pools with a [minimum CPU platform](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/min-cpu-platform) specified. You can specify the minimum CPU platform at the workload level (recommended) or at the cluster level.

## Disable node pool auto-creation

The following sections show you how to disable node pool auto-creation for specific node pools or for the entire cluster. You can also disable node pool auto-creation in a ComputeClass by specifying a value of `false` in the `nodePoolAutoCreation.enabled` field of the ComputeClass. However, we don't recommend that you disable auto-creation for ComputeClasses, because auto-creation is a primary benefit of ComputeClasses that lets you use features like active migration and fallback priorities.

### Disable auto-creation for specific node pools

You can stop GKE from managing the nodes in existing auto-created node pools. This action has the following effects:

  * The cluster autoscaler stops creating or deleting nodes in that node pool. If you want GKE to autoscale the nodes, you can separately [enable the cluster autoscaler for that node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler#enable_autoscaling).
  * GKE doesn't delete the node pool when the number of nodes is zero.
  * GKE continues to place pending Pods on existing nodes in that node pool that have availability. If node auto-provisioning is still enabled for the cluster, GKE can also create new node pools for pending Pods as needed.



To disable auto-creation for a specific node pool, run the following command:
    
    
    gcloud container node-pools update NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --no-enable-autoprovisioning
    

### Disable node auto-provisioning for the cluster

You can disable node pool auto-creation for your entire cluster by disabling the node auto-provisioning cluster setting. This action has the following effects:

  * The cluster autoscaler stops creating and deleting nodes in existing auto-created node pools. Any manually created node pools that use the cluster autoscaler aren't affected.
  * GKE doesn't automatically create new node pools for pending workloads. Monitor your cluster to avoid stuck Pods.
  * If the cluster meets the following requirements, GKE continues to create new node pools for ComputeClasses that enable auto-creation:

    * Uses GKE version 1.33.3-gke.1136000 or later.

If the cluster doesn't meet these requirements, GKE doesn't create new node pools for ComputeClasses that enable auto-creation.




If you re-enable the cluster-level node auto-provisioning setting later, GKE doesn't re-enable node pool auto-creation on existing node pools. You must mark individual node pools as auto-created.

To disable the cluster-level node auto-provisioning setting, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Kubernetes clusters** page:

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster to modify. The **Cluster details** page opens.

  3. Click the **Details** tab.

  4. In the **Automation** section, in the **Node auto-provisioning** row, click **Edit**. The **Edit node auto-provisioning** pane appears.

  5. Clear the **Enable node auto-provisioning** checkbox.

  6. Click **Save changes**.




###  gcloud 
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --no-enable-autoprovisioning
    

## What's next

  * [Learn more about cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).
  * [Learn more about node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools).
  * [Learn more about node upgrade strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
