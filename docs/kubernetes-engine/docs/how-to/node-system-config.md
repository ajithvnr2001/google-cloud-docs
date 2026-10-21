---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config/
title: Customizing node system configuration \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:27:27.283311+00:00
---

# Customizing node system configuration  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Customizing node system configuration Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to customize your Google Kubernetes Engine (GKE) node configuration by using a configuration file called a _node system configuration_.

A node system configuration is a configuration file that provides a way to adjust a limited set of system settings. In your node pool, you can use a node system configuration to specify custom settings for the [`kubelet`](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/) Kubernetes node agent and for [`sysctl`](https://en.wikipedia.org/wiki/Sysctl) low-level Linux kernel configurations.

**Caution:** Changing the `kubelet` or `sysctl` settings can lead to unintended behavior that might negatively affect the health of your workloads and nodes. Extensively test any `kubelet` or `sysctl` changes before you deploy them on production workloads.

This document details the available configurations for a node system configuration and how to apply them to your GKE Standard node pools. Note that because GKE Autopilot clusters have a more managed node environment, their direct node system configuration options are limited compared to GKE Standard node pools.

## Why use node system configurations

Node system configurations offer the following benefits:

  * **Performance tuning:** optimize network stack performance, memory management, CPU scheduling, or I/O behavior for demanding applications like AI training or serving, databases, high-traffic web servers, or latency-sensitive services.
  * **Security hardening:** apply specific kernel-level security settings or restrict certain system behaviors to reduce the attack surface.
  * **Resource management:** fine-tune how `kubelet` manages PIDs, disk space, image garbage collection, or CPU and memory resources.
  * **Workload compatibility:** help ensure that the node environment meets specific prerequisites for specialized software or older applications that require particular kernel settings.



## Other options for customizing node configurations

You can also customize your node configuration by using other methods:

  * **Runtime configuration file** : to customize a containerd container runtime on your GKE nodes, you can use a different file called a _runtime configuration file_. For more information, see [Customize containerd configuration in GKE nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration).
  * **ComputeClass** : you can specify node attributes in your GKE ComputeClass specification. You can use ComputeClasses, in both GKE Autopilot mode and Standard mode, in GKE version 1.32.1-gke.1729000 and later. For more information, see [Customize the node system configuration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#customize-node-system-config).
  * **DaemonSets** : you can also use DaemonSets to customize nodes. For more information, see [Automatically bootstrapping GKE nodes with DaemonSets](https://docs.cloud.google.com/solutions/automatically-bootstrapping-gke-nodes-with-daemonsets).



Node system configurations are _not_ supported in Windows Server nodes.

## Before you begin

Before you begin, make sure to do the following:

  * **Install command-line tools** : 
    * If you use the gcloud CLI examples in this document, ensure that you install and configure the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).
    * If you use the Terraform examples, ensure that you install and configure [Terraform](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/install-cli).
  * **Grant permissions** : you need appropriate IAM permissions to create and update GKE clusters and node pools, such as `container.clusterAdmin` or a different role with equivalent permissions.
  * **Plan for potential workload disruption** : custom node configurations are applied at the node pool level. Changes typically trigger a rolling update of the nodes in the pool, which involves [re-creating the nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manual-changes-strategy-but-no-respect-policies). Plan for potential workload disruption and use Pod Disruption Budgets (PDBs) where appropriate.
  * **Back up and test all changes:** always test configuration changes in a staging or development environment before you apply them to production. Incorrect settings can lead to node instability or workload failures.
  * **Review GKE default settings:** GKE node images come with optimized default configurations. Only customize parameters if you have a specific need and understand the impact of your changes.



## Add a node system configuration

You can customize your node system configuration by using either a ComputeClass or a configuration file.

### Use a ComputeClass for node system configuration

You can use a custom ComputeClass to customize certain parameters in the `kubelet` and the Linux kernel. This method is available in GKE version 1.32.1-gke.1729000 and later.

To use a ComputeClass to customize your node system configuration, do the following:

  1. Create a ComputeClass that includes the `spec.nodePoolAutoCreation.enabled: true` field-value pair and specify the system configurations in the `priorityDefaults` field.
  2. Deploy a workload that selects the ComputeClass.



#### Create the ComputeClass

Write your ComputeClass configuration in YAML. Use the `nodeSystemConfig` field inside the `priorityDefaults` specification to set system configurations across all priorities.

The following example `ComputeClass` configures the static CPU manager policy and custom kernel parameters:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: custom-sysconfig
    spec:
      nodePoolAutoCreation:
        enabled: true
      priorityDefaults:
        nodeSystemConfig:
          kubeletConfig:
            cpuManagerPolicy: static
          linuxNodeConfig:
            sysctls:
              net.core.somaxconn: 2048
      priorities:
      - machineFamily: n4
    

Apply the ComputeClass:
    
    
    kubectl apply -f custom-sysconfig.yaml
    

#### Deploy a workload that selects the ComputeClass

In your Pod specification, add a node selector for the ComputeClass name:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-app
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: my-app
      template:
        metadata:
          labels:
            app: my-app
        spec:
          nodeSelector:
            cloud.google.com/compute-class: custom-sysconfig
          containers:
          - name: app-container
            image: nginx
    

Apply the workload:
    
    
    kubectl apply -f my-app.yaml
    

For more information, see [Customize the node system configuration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#customize-node-system-config).

### Use a configuration file for node system configuration

When you use a node system configuration file, you use a YAML file that contains the configuration parameters for the `kubelet` and the Linux kernel. Although node system configurations are also available in GKE Autopilot mode, the steps in this document show you how to create and use a configuration file for GKE Standard mode.

To use a node system configuration file in GKE Standard mode, do the following:

  1. Create a configuration file. This file contains your `kubelet` and `sysctl` configurations.
  2. Add the configuration when you create a cluster, or when you create or update a node pool.



#### Create a configuration file

Write your node system configuration in YAML. The following example adds configurations for the `kubelet` and `sysctl` options:
    
    
    kubeletConfig:
      cpuManagerPolicy: static
      allowedUnsafeSysctls:
        - 'kernel.shm*'
        - 'kernel.msg*'
        - 'kernel.sem'
        - 'fs.mqueue.*'
        - 'net.*'
    linuxConfig:
      sysctl:
        net.core.somaxconn: '2048'
        net.ipv4.tcp_rmem: '4096 87380 6291456'
    

In this example, the following applies:

  * The `cpuManagerPolicy: static` field configures the `kubelet` to use the [static CPU management policy](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/#static-policy).
  * The `net.core.somaxconn: '2048'` field limits the `socket listen()` backlog to 2,048 bytes.
  * The `net.ipv4.tcp_rmem: '4096 87380 6291456'` field sets the minimum, default, and maximum value of the TCP socket receive buffer to 4,096 bytes, 87,380 bytes, and 6,291,456 bytes, respectively.



If you want to add configurations only for the `kubelet` or `sysctl`, include only that section in your node system configuration. For example, to add a `kubelet` configuration, create the following file:
    
    
    kubeletConfig:
      cpuManagerPolicy: static
    

For a complete list of the fields that you can add to your node system configuration, see the Kubelet configuration options and Sysctl configuration options sections.

#### Add the configuration to a Standard node pool

After you create the node system configuration, add the [`--system-config-from-file`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/node-pools/create#--system-config-from-file) flag by using the Google Cloud CLI. You can add this flag when you create a cluster, or when you create or update a node pool. You can't add a node system configuration by using the Google Cloud console.

#### Create a cluster with the node system configuration

You can add a node system configuration during cluster creation by using the gcloud CLI or Terraform. The following instructions apply the node system configuration to the default node pool:

###  gcloud CLI 
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=LOCATION \
        --system-config-from-file=SYSTEM_CONFIG_PATH
    

Replace the following:

  * `CLUSTER_NAME`: the name for your cluster
  * `LOCATION`: the compute zone or region of the cluster
  * `SYSTEM_CONFIG_PATH`: the path to the file that contains your `kubelet` and `sysctl` configurations



After you apply a node system configuration, the default node pool of the cluster uses the settings that you defined.

### Terraform

To create a regional cluster with a customized node system configuration by using Terraform, refer to the following example:
    
    
    resource "google_container_cluster" "default" {
      name     = "gke-standard-regional-cluster"
      location = "us-central1"
    
      initial_node_count = 1
    
      node_config {
        # Kubelet configuration
        kubelet_config {
          cpu_manager_policy = "static"
        }
    
        linux_node_config {
          # Sysctl configuration
          sysctls = {
            "net.core.netdev_max_backlog" = "10000"
          }
    
          # Linux cgroup mode configuration
          cgroup_mode = "CGROUP_MODE_V2"
    
          # Linux huge page configuration
          hugepages_config {
            hugepage_size_2m = "1024"
          }
        }
      }
    }

For more information about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

#### Create a new node pool with the node system configuration

You can add a node system configuration when you use the gcloud CLI or Terraform to create a new node pool.

The following instructions apply the node system configuration to a new node pool:

###  gcloud CLI 
    
    
    gcloud container node-pools create POOL_NAME \
         --cluster CLUSTER_NAME \
         --location=LOCATION \
         --system-config-from-file=SYSTEM_CONFIG_PATH
    
    

Replace the following:

  * `POOL_NAME`: the name for your node pool
  * `CLUSTER_NAME`: the name of the cluster that you want to add a node pool to
  * `LOCATION`: the compute zone or region of the cluster
  * `SYSTEM_CONFIG_PATH`: the path to the file that contains your `kubelet` and `sysctl` configurations



### Terraform

To create a node pool with a customized node system configuration by using Terraform, refer to the following example:
    
    
    resource "google_container_node_pool" "default" {
      name    = "gke-standard-regional-node-pool"
      cluster = google_container_cluster.default.name
    
      node_config {
        # Kubelet configuration
        kubelet_config {
          cpu_manager_policy = "static"
        }
    
        linux_node_config {
          # Sysctl configuration
          sysctls = {
            "net.core.netdev_max_backlog" = "10000"
          }
    
          # Linux cgroup mode configuration
          cgroup_mode = "CGROUP_MODE_V2"
    
          # Linux huge page configuration
          hugepages_config {
            hugepage_size_2m = "1024"
          }
        }
      }
    }

For more information about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

#### Update the node system configuration for an existing node pool

You can set or update the node system configuration for an existing node pool. For more information specifically about updating an existing configuration, see Edit by updating an existing node pool.

Run the following command to update the existing node pool:
    
    
       gcloud container node-pools update POOL_NAME \
          --cluster=CLUSTER_NAME \
          --location=LOCATION \
          --system-config-from-file=SYSTEM_CONFIG_PATH
    

Replace the following:

  * `POOL_NAME`: the name of the node pool that you want to update
  * `CLUSTER_NAME`: the name of the cluster that you want to update
  * `LOCATION`: the compute zone or region of the cluster
  * `SYSTEM_CONFIG_PATH`: the path to the file that contains your `kubelet` and `sysctl` configurations



This change requires re-creating the nodes, which can cause disruption to your running workloads. For more information about this specific change, find the corresponding row in the [manual changes that re-create the nodes using a node upgrade strategy without respecting maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manual-changes-strategy-but-no-respect-policies) table.

For more information about node updates, see [Planning for node update disruptions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#plan-node-disruption).

**Caution:** GKE immediately begins re-creating the nodes for this change by using the node upgrade strategy, regardless of active maintenance policies. GKE depends on [resource availability for the change](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota). Disabling node auto-upgrades [doesn't prevent this change](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable-only-versions).

## Edit a node system configuration

You can edit a node system configuration depending on whether you are using ComputeClasses or a configuration file.

### For ComputeClasses

To edit the node system configuration when using ComputeClasses, choose one of the following methods:

#### Method 1: Update the existing ComputeClass

If you update the `nodeSystemConfig` in an existing ComputeClass, GKE applies the updated configuration to _newly created nodes only_. Existing nodes are not automatically updated.

To migrate your workloads to nodes with the new configuration, you can do one of the following:

  * Configure [active migration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#active-migration) in your ComputeClass.
  * To trigger a scale-up of new nodes, manually restart or re-create your workloads.



To update the ComputeClass, edit the YAML file and apply it:
    
    
    kubectl apply -f custom-sysconfig.yaml
    

#### Method 2: Create a new ComputeClass

To help ensure that your workloads migrate to new nodes with the updated configuration, do the following:

  1. Create a new ComputeClass with a different name and the updated configuration.
  2. Update the node selector in your workload specifications to reference the new ComputeClass.
  3. Apply the updated workload specifications. The cluster autoscaler will provision new nodes with the new configuration and eventually scale down the old nodes.
  4. Delete the old ComputeClass object.



### For configuration files

To edit a node system configuration when using a configuration file, you can create a new node pool with the configuration that you want, or update the node system configuration of an existing node pool.

#### Edit by creating a node pool

To edit a node system configuration by creating a node pool, do the following:

  1. Create a configuration file with the configuration that you want.
  2. Add the configuration to a new node pool.
  3. Migrate your workloads to the new node pool.
  4. [Delete the old node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#deleting_a_node_pool).



#### Edit by updating an existing node pool

To edit the existing node system configuration of an existing node pool, follow the instructions in the _Update node pool_ tab for adding the configuration to a node pool. When you update a node system configuration and the new configuration overrides the node pool's existing system configuration, the nodes must be re-created. If you omit any parameters during an update, the parameters are set to their respective defaults.

#### Get the existing node system configuration

To retrieve your node pool's existing node system configuration—for example, if you've already customized the configuration and want to add to it—use the [`gcloud container node-pools describe`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/describe) command. The output of the command lists any existing configurations under `kubeletConfig` and `linuxNodeConfig`.

**Caution:** When you update the Linux node configuration based on this output, you must specify the parameters under the `linuxConfig` field in the update command. The `describe` command shows these settings under **`linuxNodeConfig`** , but for updates, the correct field is **`linuxConfig`**. Using the output field `linuxNodeConfig` in an update request won't apply the changes.

For example, see the following snippet showing the _output_ format from the `describe` command:
    
    
      kubeletConfig:
        allowedUnsafeSysctls:
        - kernel.shm*
        - kernel.msg*
        - kernel.sem
        - fs.mqueue.*
        - net.*
        cpuManagerPolicy: static
        insecureKubeletReadonlyPortEnabled: false
        maxParallelImagePulls: 2
      linuxNodeConfig: # IMPORTANT: Use linuxConfig when updating these settings
        sysctl:
          net.core.somaxconn: '2048'
          net.ipv4.tcp_rmem: 4096 87380 6291456
    

If you haven't already set a node system configuration, the output doesn't list `kubeletConfig` or `linuxNodeConfig`.

#### Reset the existing node system configuration

If you want to reset the node system configuration back to the defaults, update your configuration file with empty values for the `kubelet` and `sysctl` fields, for example:
    
    
    kubeletConfig: {}
    linuxConfig:
      sysctl: {}
    

## Delete a node system configuration

To remove a node system configuration, follow the steps depending on whether you are using ComputeClasses or a configuration file.

### For ComputeClasses

To remove the custom node system configuration, do the following:

  1. Remove the `cloud.google.com/compute-class` node selector from your workload specifications.
  2. Apply the updated workload specifications. GKE re-creates the workloads on default nodes. The cluster autoscaler will eventually scale down and delete the nodes that were provisioned for the ComputeClass.
  3. Delete the ComputeClass object from the cluster:
         
         kubectl delete computeclass CUSTOM_COMPUTE_CLASS_NAME
         




### For configuration files

To remove a node system configuration that was applied using a configuration file, do the following:

  1. Create a new node pool without the configuration file.
  2. Migrate your workloads to the new node pool.
  3. [Delete the node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#deleting_a_node_pool) that has the old node system configuration.



## Configuration options for the `kubelet`

The tables in this section describe the `kubelet` options that you can modify.

### CPU management

The following table describes the CPU management options for the `kubelet`.

`kubelet` config settings | Restrictions | Default setting | Description  
---|---|---|---  
[`cpuCFSQuota`](https://www.kernel.org/doc/Documentation/scheduler/sched-bwc.txt) | Must be `true` or `false`. | `true` | This setting enforces the [Pod's CPU limit](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/#specify-a-cpu-request-and-a-cpu-limit). Setting this value to `false` means that the CPU limits for Pods are ignored.  
  
Ignoring CPU limits might be beneficial in certain scenarios where Pods are sensitive to CPU limits. The risk of disabling `cpuCFSQuota` is that a rogue Pod can consume more CPU resources than intended.  
[`cpuCFSQuotaPeriod`](https://www.kernel.org/doc/Documentation/scheduler/sched-bwc.txt) | Must be a duration of time. | `"100ms"` | This setting sets the CPU CFS quota period value, `cpu.cfs_period_us`, which specifies the period of how often a cgroup's access to CPU resources should be reallocated. This option lets you tune the CPU throttling behavior.  
  
### Memory management and eviction

The following table describes the modifiable options for memory management and eviction. This section also contains a separate table that describes the modifiable options for the `evictionSoft` flag.

`kubelet` config settings | Restrictions | Default setting | Description  
---|---|---|---  
[`evictionSoft`](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/) | Map of signal names. For value restrictions, see the following table. | `none` | This setting maps signal names to a quantity or percentage that defines soft eviction thresholds. A soft eviction threshold must have a grace period. The `kubelet` does not evict Pods until the grace period is exceeded.  
[`evictionSoftGracePeriod`](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/) | Map of signal names. For each signal name, the value must be a positive duration less than `5m`. Valid time units are `ns`, `us` (or `µs`), `ms`, `s`, or `m`. | `none` | This setting maps signal names to durations that define grace periods for soft eviction thresholds. Each soft eviction threshold must have a corresponding grace period.  
[`evictionMinimumReclaim`](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/) | Map of signal names. For each signal name, the value must be a positive percentage less than `10%`. | `none` | This setting maps signal names to percentages that define the minimum amount of a given resource that the `kubelet` reclaims when it performs a Pod eviction.  
[`evictionMaxPodGracePeriodSeconds`](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/) | Value must be an integer between `0` and `300`. | `0` | This setting defines, in seconds, the maximum grace period for Pod termination during eviction.  
[`singleProcessOOMKill`](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1beta1/) | Value must be `true` or `false`. | `true` for cgroupv1 nodes, `false` for cgroupv2 nodes. | This setting sets whether the processes in the container are OOMkilled individually or as a group. Available on GKE versions 1.32.4-gke.1132000, 1.33.0-gke.1748000 or later.  
  
The following table shows the modifiable options for the `evictionSoft` flag. The same options also apply to the `evictionSoftGracePeriod` and `evictionMinimumReclaim` flags with different restrictions.

`kubelet` config settings | Restrictions | Default setting | Description  
---|---|---|---  
[`memoryAvailable`](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/) | Value must be a quantity greater than `100Mi` and less than `50%` of the node's memory. | `none` | This setting represents the amount of memory available before soft eviction. Defines the amount of the `memory.available` signal in the `kubelet` .  
[`nodefsAvailable`](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/) | Value must be between `10%` and `50%`. | `none` | This setting represents the nodefs available before soft eviction. Defines the amount of the `nodefs.available` signal in the `kubelet` .  
[`nodefsInodesFree`](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/) | Value must be between `5%` and `50%`. | `none` | This setting represents the nodefs inodes that are free before soft eviction. Defines the amount of the `nodefs.inodesFree` signal in the `kubelet` .  
[`imagefsAvailable`](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/) | Value must be between `15%` and `50%`. | `none` | This setting represents the imagefs available before soft eviction. Defines the amount of `imagefs.available` signal in the `kubelet` .  
[`imagefsInodesFree`](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/) | Value must be between `5%` and `50%`. | `none` | This setting represents the imagefs inodes that are free before soft eviction. Defines the amount of the `imagefs.inodesFree` signal in the `kubelet`.  
[`pidAvailable`](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/) | Value must be between `10%` and `50%`. | `none` | This setting represents the PIDs available before soft eviction. Defines the amount of the `pid.available` signal in the `kubelet`.  
  
### PID management

The following table describes the modifiable options for PID management.

`kubelet` config settings | Restrictions | Default setting | Description  
---|---|---|---  
[`podPidsLimit`](https://kubernetes.io/docs/concepts/policy/pid-limiting/) | Value must be between `1024` and `4194304`. | `none` | This setting sets the maximum number of process IDs (PIDs) that each Pod can use.  
  
### Logging

The following table describes the modifiable options for logging.

`kubelet` config settings | Restrictions | Default setting | Description  
---|---|---|---  
[`containerLogMaxSize`](https://kubernetes.io/docs/concepts/cluster-administration/logging/#log-rotation) | Value must be a positive number and a unit suffix between `10Mi` and `500Mi`, inclusive. | `10Mi` | This setting controls the [containerLogMaxSize](https://kubernetes.io/docs/concepts/cluster-administration/logging/#log-rotation) setting of container log rotation policy, which lets you configure the maximum size for each log file. The default value is `10Mi`. Valid units are `Ki`, `Mi`, and `Gi`.  
[`containerLogMaxFiles`](https://kubernetes.io/docs/concepts/cluster-administration/logging/#log-rotation) | Value must be an integer between `2` and `10`, inclusive. | `5` | This setting controls the [containerLogMaxFiles](https://kubernetes.io/docs/concepts/cluster-administration/logging/#log-rotation) setting of the container log files rotation policy, which lets you configure the maximum number of files allowed for each container respectively. The default value is `5`. The total log size `(container_log_max_size*container_log_max_files)` per container can't exceed 1% of the total storage of the node.  
  
### Image garbage collection

The following table describes the modifiable options for image garbage collection.

`kubelet` config settings | Restrictions | Default setting | Description  
---|---|---|---  
[`imageGcHighThresholdPercent`](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1beta1/) | Value must be an integer between 10 and 85, inclusive, and higher than `imageGcLowThresholdPercent`. | `85` | This setting defines the percent of disk usage above which image garbage collection is run. It represents the highest disk usage to garbage collect to. The percentage is calculated by dividing this field's value by 100.  
[`imageGcLowThresholdPercent`](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1beta1/) | Value must be an integer between 10 and 85, inclusive, and lower than `imageGcHighThresholdPercent`. | `80` | This setting defines the percent of disk usage before which image garbage collection is never run. It represents the lowest disk usage to garbage collect to. The percentage is calculated by dividing this field's value by 100.  
[`imageMinimumGcAge`](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1beta1/) | Value must be a duration of time not greater than `2m`. Valid time units are `ns`, `us` (or `µs`), `ms`, `s`, `m`, or `h`. | `2m` | This setting defines the minimum age for an unused image before it is garbage-collected.  
[`imageMaximumGcAge`](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1beta1/) | Value must be a duration of time. | `0s` |  This setting defines the maximum age an image can be unused before it is garbage-collected. This field's default value is `0s`, which disables this field. Thus, images won't be garbage-collected based on being unused. When this value is specified, it must be greater than the value of the `imageMinimumGcAge` field. Available on GKE versions 1.30.7-gke.1076000, 1.31.3-gke.1023000 or later.  
  
### Image pulling

The following table describes the modifiable options for image pulling.

`kubelet` config settings | Restrictions | Default setting | Description  
---|---|---|---  
[`maxParallelImagePulls`](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1beta1/) | Value must be an integer between 2 and 5, inclusive. | `2` or `3` based on the disk type. | This setting defines the maximum number of image pulls in parallel. The default value is decided by the boot disk type.  
  
### Security and unsafe operations

The following table describes the modifiable options for configuring security and handling unsafe operations.

`kubelet` config settings | Restrictions | Default setting | Description  
---|---|---|---  
[`allowedUnsafeSysctls`](https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/) |  List of `sysctl` names or groups. The allowed `sysctl` groups are the following:

  * `kernel.shm*`
  * `kernel.msg*`
  * `kernel.sem`
  * `fs.mqueue.*`
  * `net.*`.

| `none` | This setting defines a comma-separated allowlist of unsafe `sysctl` names or `sysctl` groups that can be set on the Pods.  
[`insecureKubeletReadonlyPortEnabled`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/disable-kubelet-readonly-port) | Value must be a boolean value, either `true` or `false`. | `false` | This setting disables the insecure `kubelet` read-only port `10255` on every new node pool in your cluster. If you configure this setting in this file, you can't use a GKE API client to change the setting at the cluster level.  
  
### Resource Managers

Kubernetes offers a suite of Resource Managers. You can configure these Resource Managers to coordinate and optimize the alignment of node resources for Pods that are configured with specific requirements for CPUs, devices, and memory (hugepages) resources.

The following table describes the modifiable options for Resource Managers.

`kubelet` config settings | Restrictions | Default setting | Description  
---|---|---|---  
[`cpuManagerPolicy`](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/#cpu-management-policies) | Value must be `none` or `static`. | `none` | This setting controls the `kubelet` [CPU Manager policy](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/#cpu-management-policies). The default value is `none`, which is the default CPU affinity scheme, providing no affinity beyond what the OS scheduler does automatically.  
  
Setting this value to `static` allows Pods that are both in the `Guaranteed` QoS class and have integer CPU requests to be assigned exclusive CPUs.  
[`memoryManager.policy`](https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/) | Value must be `None` or `Static`. | `None` |  This setting controls the `kubelet` [Memory Manager policy](https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/). With the default value of `None`, Kubernetes acts the same as if the Memory Manager is not present. If you set this value to `Static`, the Memory Manager policy sends topology hints that depend on the type of Pod. For details, see [Static policy](https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/#policy-static). This setting is supported for clusters with the control plane running GKE version 1.32.3-gke.1785000 or later.  
[`topologyManager`](https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/#topology-manager-policies) |  Value must be one of the supported settings for each of the respective fields. You can't set the `topologyManager` field when you use the Terraform instructions to add the configuration to a Standard node pool. | 

  * `policy`: `none`
  * `scope`: `container`

|  These settings control the `kubelet` [Topology Manager](https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/#topology-manager-policies) configuration by using the `policy` and `scope` subfields. The Topology Manager coordinates the set of components responsible for performance optimizations related to CPU isolation, memory, and device locality. You can set the policy and scope settings independently of each other. For more information about these settings, see [Topology manager scopes and policies](https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/#topology-manager-scopes-and-policies).  The following GKE resources support this setting:

  * Clusters with the control plane running GKE version 1.32.3-gke.1785000 or later. For clusters with the control plane and nodes running 1.33.0-gke.1712000 or later, the Topology Manager also receives information about GPU topology.
  * Nodes with the following machine types: A2, A3, A4, C3, C4, C4A, C4N, G2, G4, M3, N4

  
  
### Container restart delay

This setting controls the maximum time to wait between container restart attempts when a container is in a `CrashLoopBackOff` state. You can configure this setting for Standard node pools running GKE version 1.35 or later.

**Caution:** A very short delay on a persistently failing container can lead to high CPU and resource consumption on the node, potentially impacting other workloads due to resource exhaustion. Consider reducing it only when the benefits of faster retries outweigh the risks of increased resource usage.

The following table describes the modifiable options for `crashLoopBackOff`.

`kubelet` config settings | Restrictions | Default setting | Description  
---|---|---|---  
[`crashLoopBackOff.maxContainerRestartPeriod`](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1beta1/#kubelet-config-k8s-io-v1beta1-CrashLoopBackOffConfig) | Value must be a positive duration less than or equal to 5 minutes (`5m`). Valid time units are `ns`, `us` (or `µs`), `ms`, `s`, or `m`. | `none` | The maximum duration the backoff delay can accrue to for container restarts. The delay between restarts increases exponentially from an initial value up to this maximum limit. The default maximum limit for a Kubernetes cluster is 5 minutes. For more information, see [Configurable container restart delay](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#configurable-container-restart-delay).  
  
### Graceful termination of Spot VMs in GKE

The following table describes the modifiable options for the termination and graceful shutdown period for Spot VMs in GKE. To use these options, your cluster's control plane must run GKE version 1.35.0-gke.1171000 or later. For more information, see [How Spot VMs work in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms#how-it-works).

`kubelet` config settings | Restrictions | Default setting | Description  
---|---|---|---  
[`shutdownGracePeriodSeconds`](https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/#graceful-node-shutdown) | Value must be an integer representing the duration in seconds. Allowed values are `0`, `30`, or `120`. | `30` | Specifies the total duration in seconds that the node delays shutting down in order to gracefully terminate Pods.  
[`shutdownGracePeriodCriticalPodsSeconds`](https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/#graceful-node-shutdown) | Value must be an integer between `0` and `120` (inclusive), and must be less than `shutdownGracePeriodSeconds`. Only valid if `shutdownGracePeriodSeconds` is also set. | `15` | Specifies the duration in seconds used to terminate critical Pods during a node shutdown.  
  
### System resource reservations

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For Standard node pools that run Linux and GKE 1.37 or later, you can customize the amount of memory and CPU reserved for system components. This lets you fine-tune allocatable capacity for specific scenarios such as handling high-volume image pulls or running customized node DaemonSets. For more information about the default reservations, see [About GKE node sizing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes).

The following table describes the modifiable options for system resource reservations.

`kubelet` config settings | Restrictions | Default setting | Description  
---|---|---|---  
`reservedResourcesConfig.memoryReservedMib` | Value must be an integer. Must be greater than or equal to the default memory reservation for node pools created running 1.37 or later, and less than 50% of the node's total memory capacity. | See [Memory reservations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes#memory_reservations). | The amount of memory to reserve for system components, in mebibytes (MiB).  
`reservedResourcesConfig.cpuReservedMillicore` | Value must be an integer. Must be greater than or equal to the default CPU reservation for node pools created running 1.37 or later, and less than 50% of the node's total CPU capacity. | See [CPU reservations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes#cpu_reservations). | The amount of CPU to reserve for system components, in millicores.  
  
#### Verify effective reservations

To check the active reservations applied to your node pool, inspect the `effectiveMemoryReservedMib` and `effectiveCpuReservedMillicore` output fields:
    
    
    gcloud container node-pools describe POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=LOCATION \
        --format="yaml(config.kubeletConfig.reservedResourcesConfig)"
    

## Sysctl configuration options

To tune the performance of your system, you can modify Linux kernel parameters. The tables in this section describe the various kernel parameters that you can configure.

### Filesystem parameters (`fs.*`)

The following table describes the modifiable parameters for the Linux filesystem. These settings control the behavior of the Linux filesystem, such as file handle limits and event monitoring.

`Sysctl` parameter | Restrictions | Description  
---|---|---  
[`fs.aio-max-nr`](https://docs.kernel.org/admin-guide/sysctl/fs.html#aio-nr-aio-max-nr) | Must be between [65536, 4194304]. | This setting defines the maximum system-wide number of asynchronous I/O requests.  
[`fs.file-max`](https://docs.kernel.org/admin-guide/sysctl/fs.html#file-max-file-nr) | Must be between [104857, 67108864]. | This setting defines the maximum number of file-handles that the Linux kernel can allocate.  
[`fs.inotify.max_user_instances`](https://docs.kernel.org/admin-guide/sysctl/fs.html#max-user-instances) | Must be between [8192, 1048576]. | This setting defines the maximum number of inotify instances that a user can create.  
[`fs.inotify.max_user_watches`](https://docs.kernel.org/admin-guide/sysctl/fs.html#max-user-watches) | Must be between [8192, 1048576]. | This setting defines the maximum number of inotify watches that a user can create.  
[`fs.nr_open`](https://docs.kernel.org/admin-guide/sysctl/fs.html#nr-open) | Must be between [1048576, 2147483584]. | This setting defines the maximum number of file descriptors that can be opened by a process.  
  
### Kernel parameters (`kernel.*`)

The following table describes the modifiable parameters for the Linux kernel. These settings configure core kernel functionalities, including shared memory allocation.

Sysctl parameter | Restrictions | Description  
---|---|---  
[`kernel.shmmni`](https://docs.kernel.org/admin-guide/sysctl/kernel.html#shmmni) | Must be between [4096, 32768]. | This setting defines the system-wide maximum number of shared memory segments. If this value isn't set, it defaults to `4096`.  
[`kernel.shmmax`](https://docs.kernel.org/admin-guide/sysctl/kernel.html#shmmax) | Must be between [0, 18446744073692774399]. | This setting defines the maximum size, in bytes, of a single shared memory segment allowed by the kernel. This value is ignored if it is greater than the actual amount of RAM, which means that all available RAM can be shared.  
[`kernel.shmall`](https://docs.kernel.org/admin-guide/sysctl/kernel.html#shmall) | Must be between [0, 18446744073692774399]. | This setting defines the total amount of shared memory pages that can be used on the system at one time. A page is 4,096 bytes on the AMD64 and Intel 64 architecture.  
[`kernel.perf_event_paranoid`](https://docs.kernel.org/admin-guide/sysctl/kernel.html#perf-event-paranoid) | Must be between [-1, 3]. | This setting controls use of the performance events system by unprivileged users without CAP_PERFMON. The default value is `2` in the kernel.  
[`kernel.sched_rt_runtime_us`](https://docs.kernel.org/scheduler/sched-rt-group.html#system-wide-settings) | Must be between [-1, 1000000]. | This setting defines a global limit on how much time real-time scheduling can use.  
[`kernel.softlockup_panic`](https://docs.kernel.org/admin-guide/sysctl/kernel.html#softlockup-panic) | Optional (boolean). | This setting ontrols whether the kernel panics when a soft lockup is detected.  
[`kernel.yama.ptrace_scope`](https://docs.kernel.org/admin-guide/LSM/Yama.html) | Must be between [0, 3]. |  This setting defines the scope and restrictions for the `ptrace()` system call, impacting process debugging and tracing. Supported value include the following:

  * `0`: classic ptrace permissions.
  * `1`: restricted ptrace, which is the default in many distributions. Only child processes or CAP_SYS_PTRACE.
  * `2`: admin-only ptrace. Only processes with CAP_SYS_PTRACE.
  * `3`: no ptrace. ptrace calls are disallowed.

  
[`kernel.kptr_restrict`](https://docs.kernel.org/admin-guide/sysctl/kernel.html#kptr-restrict) | Must be between [0, 2]. | This setting indicates whether restrictions are placed on exposing kernel addresses through `/proc` and other interfaces.  
[`kernel.dmesg_restrict`](https://docs.kernel.org/admin-guide/sysctl/kernel.html#dmesg-restrict) | Optional (boolean). | This setting indicates whether unprivileged users are prevented from using `dmesg(8)` to view messages from the kernel's log buffer.  
[`kernel.sysrq`](https://docs.kernel.org/admin-guide/sysctl/kernel.html#sysrq) | Must be between [0, 511]. |  This setting controls the functions allowed to be invoked through the SysRq key. Possible values include the following:

  * `0`: disables sysrq completely.
  * `1`: enables all sysrq functions.
  * `>1`: bitmask of allowed sysrq functions. For more information, see [Linux Magic System Request Key Hacks](https://docs.kernel.org/admin-guide/sysrq.html).

  
[`kernel.keys.maxbytes`](https://docs.kernel.org/security/keys/core.html) | Must be between [20000, 2097152]. | This setting defines the maximum number of bytes that a nonroot user can hold in the payload section of all their keys.  
[`kernel.keys.maxkeys`](https://docs.kernel.org/security/keys/core.html) | Must be between [200, 1048576]. | This setting defines the maximum number of keys that a nonroot user can own.  
  
### Network parameters (`net.*`)

The following table describes the modifiable parameters for networking. These settings tune the performance and behavior of the networking stack, from socket buffers to connection tracking.

Sysctl parameter | Restrictions | Description  
---|---|---  
[`net.core.busy_poll`](https://docs.kernel.org/admin-guide/sysctl/net.html#busy-poll) | Any positive integer, less than 2147483647. | This setting defines the low latency busy poll timeout for poll and select. It represents the approximate time in µs to busy loop waiting for events.  
[`net.core.busy_read`](https://docs.kernel.org/admin-guide/sysctl/net.html#busy-read) | Any positive integer, less than 2147483647. | This setting defines the low latency busy poll timeout for socket reads. It represents the approximate time in µs to busy loop waiting for packets on the device queue.  
[`net.core.netdev_max_backlog`](https://docs.kernel.org/admin-guide/sysctl/net.html#netdev-max-backlog) | Any positive integer, less than 2147483647. | This setting defines the maximum number of packets, queued on the INPUT side, when the interface receives packets faster than kernel can process them.  
[`net.core.rmem_default`](https://docs.kernel.org/admin-guide/sysctl/net.html#rmem-default) | Any positive integer, less than 2147483647. | This setting defines the default receive socket buffer size, in bytes.  
[`net.core.rmem_max`](https://docs.kernel.org/admin-guide/sysctl/net.html#rmem-max) | Any positive integer, less than 2147483647. | This setting defines the maximum receive socket buffer size, in bytes.  
[`net.core.wmem_default`](https://docs.kernel.org/admin-guide/sysctl/net.html#wmem-default) | Any positive integer, less than 2147483647. | This setting defines the default setting, in bytes, of the socket send buffer.  
[`net.core.wmem_max`](https://docs.kernel.org/admin-guide/sysctl/net.html#wmem-max) | Any positive integer, less than 2147483647. | This setting defines the maximum send socket buffer size, in bytes.  
[`net.core.optmem_max`](https://docs.kernel.org/admin-guide/sysctl/net.html#optmem-max) | Any positive integer, less than 2147483647. | This setting defines the maximum ancillary buffer size allowed per socket.  
[`net.core.somaxconn`](https://docs.kernel.org/networking/ip-sysctl.html#tcp-variables) | Must be between [128, 2147483647]. | This setting defines the limit of the `socket listen()` backlog, which is known in userspace as SOMAXCONN. This setting defaults to `128`.  
[`net.ipv4.tcp_rmem`](https://docs.kernel.org/networking/ip-sysctl.html#tcp-variables) | {min, default, max} (each > 0, memory in bytes). | This setting defines the minimal size, in bytes, of the receive buffer used by UDP sockets in moderation. The default setting is 1 page.  
[`net.ipv4.tcp_wmem`](https://docs.kernel.org/networking/ip-sysctl.html#tcp-variables) | {min, default, max} (each > 0, memory in bytes). | This setting defines the minimal size, in bytes, of the send buffer used by UDP sockets in moderation. The default setting is 1 page.  
[`net.ipv4.tcp_tw_reuse`](https://docs.kernel.org/networking/ip-sysctl.html#tcp-variables) | Must be between {0, 1}. | This setting defines whether to allow the reuse of sockets in the `TIME_WAIT` state for new connections when it is safe from a protocol viewpoint. The default value is `0`.  
[`net.ipv4.tcp_max_orphans`](https://docs.kernel.org/networking/ip-sysctl.html#tcp-variables) | Must be between [16384, 262144]. | This setting defines the maximal number of TCP sockets that aren't attached to any user file handle.  
[`net.ipv4.tcp_max_tw_buckets`](https://docs.kernel.org/networking/ip-sysctl.html#tcp-variables) | Must be between [4096, 2147483647]. | This setting defines the maximal number of timewait sockets held by the system simultaneously. If this number is exceeded, the time-wait socket is immediately destroyed and a warning is printed.  
[`net.ipv4.tcp_syn_retries`](https://docs.kernel.org/networking/ip-sysctl.html#tcp-variables) | Must be between [1, 127]. | This setting defines the number of times initial SYNs for an active TCP connection attempt is retransmitted.  
[`net.ipv4.tcp_ecn`](https://docs.kernel.org/networking/ip-sysctl.html#tcp-variables) | Must be between [0, 2]. | This setting controls the use of Explicit Congestion Notification (ECN) by TCP. ECN is used only when both ends of the TCP connection indicate support for it.  
[`net.ipv4.tcp_mtu_probing`](https://docs.kernel.org/networking/ip-sysctl.html#tcp-variables) | Must be between [0, 2]. |  This setting controls TCP Packetization-Layer Path MTU Discovery. The supported values are the following:

  * `0`: disabled.
  * `1`: disabled by default, enabled when an ICMP black hole is detected.
  * `2`: always enabled. Use the initial MSS of `tcp_base_mss`.

  
[`net.ipv4.tcp_congestion_control`](https://docs.kernel.org/networking/ip-sysctl.html#tcp-variables) | Must be one of the supported values from the **Description** column. | This setting isn't supported when [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2) is enabled on the cluster. The following supported values depend on the image type:

  * `Container-Optimized OS`: `reno`, `cubic`, `bbr`, `lp`, `htcp` (available on GKE versions 1.34.1-gke.3355001 or later)
  * `Ubuntu`: `reno`, `cubic`, `bbr`, `lp`, `htcp`, `vegas`, `dctcp`, `bic`, `cdg`, `highspeed`, `hybla`, `illinois`, `nv`, `scalable`, `veno`, `westwood`, `yeah`

  
[`net.ipv6.conf.all.disable_ipv6`](https://docs.kernel.org/networking/ip-sysctl.html#proc-sys-net-ipv6-variables) | Boolean. | Changing this value is same as changing the `conf/default/disable_ipv6` setting and also all per-interface `disable_ipv6` settings to the same value.  
[`net.ipv6.conf.default.disable_ipv6`](https://docs.kernel.org/networking/ip-sysctl.html#proc-sys-net-ipv6-variables) | Boolean. | This setting disables the operation of IPv6.  
[`net.netfilter.nf_conntrack_acct`](https://docs.kernel.org/networking/nf_conntrack-sysctl.html) | Must be between {0, 1}. | This setting enables the connection tracking flow accounting. The default value is `0`, which means that the setting is disabled. Available on GKE versions 1.32.0-gke.1448000 or later.  
[`net.netfilter.nf_conntrack_max`](https://docs.kernel.org/networking/nf_conntrack-sysctl.html) | Must be between [65536, 4194304]. | This setting defines the size of the connection tracking table. If the maximum value is reached, the new connection will fail. Available on GKE versions 1.32.0-gke.1448000 or later.  
[`net.netfilter.nf_conntrack_buckets`](https://docs.kernel.org/networking/nf_conntrack-sysctl.html) | Must be between [65536, 524288]. |  This setting defines the size of the hash table. The recommended setting is the result of the following: `nf_conntrack_max = nf_conntrack_buckets * 4`. Available on GKE versions 1.32.0-gke.1448000 or later.  
[`net.netfilter.nf_conntrack_tcp_timeout_close_wait`](https://docs.kernel.org/networking/nf_conntrack-sysctl.html) | Must be between [60, 3600]. |  This setting defines the period, in seconds, for which the TCP connections can remain in the `CLOSE_WAIT` state. The default value is `3600`. Available on GKE versions 1.32.0-gke.1448000 or later.  
[`net.netfilter.nf_conntrack_tcp_timeout_established`](https://docs.kernel.org/networking/nf_conntrack-sysctl.html) | Must be between [600, 86400]. |  This setting defines the duration, in seconds, of dead connections before they are deleted automatically from the connection tracking table. Available on GKE versions 1.32.0-gke.1448000 or later.  
[`net.netfilter.nf_conntrack_tcp_timeout_time_wait`](https://docs.kernel.org/networking/nf_conntrack-sysctl.html) | Must be between [1, 600]. |  This setting defines the period, in seconds, for which the TCP connections can remain in the `TIME_WAIT` state. The default value is `120`. Available on GKE versions 1.32.0-gke.1448000 or later.  
[`net.ipv4.neigh.default.gc_thresh1`](https://docs.kernel.org/networking/ip-sysctl.html#neigh-variables) | Must be between [0, 262144]. | This setting defines the minimum number of entries to keep in the ARP cache. The garbage collector doesn't run if the number of entries is below this setting. Setting this value to `0` can lead to cache thrashing and degraded performance.  
[`net.ipv4.neigh.default.gc_thresh2`](https://docs.kernel.org/networking/ip-sysctl.html#neigh-variables) | Must be between [512, 524288]. | This setting defines the soft maximum number of entries to keep in the ARP cache. The garbage collector allows the number of entries to exceed this value for 5 seconds before it starts soft garbage collection.  
[`net.ipv4.neigh.default.gc_thresh3`](https://docs.kernel.org/networking/ip-sysctl.html#neigh-variables) | Must be between [1024, 1048576]. | This setting defines the hard maximum number of entries to keep in the ARP cache. The garbage collector is designed to always run if the number of entries exceeds this setting.  
  
### Virtual Memory parameters (`vm.*`)

The following table describes the modifiable parameters for the Virtual Memory subsystem. These settings manage the Virtual Memory subsystem, which controls how the kernel handles memory, swapping, and disk caching.

`sysctl` parameter | Restrictions | Description  
---|---|---  
[`vm.max_map_count`](https://docs.kernel.org/admin-guide/sysctl/vm.html#max-map-count) | Must be between [65536, 2147483647]. | This file defines the maximum number of memory map areas that a process can have.  
[`vm.dirty_background_ratio`](https://docs.kernel.org/admin-guide/sysctl/vm.html#dirty-background-ratio) | Must be between [1, 100]. | This setting defines the percentage of system memory that can be filled with dirty pages before background kernel flusher threads begin writeback. The value must be less than the value of the `vm.dirty_ratio` field.  
[`vm.dirty_background_bytes`](https://docs.kernel.org/admin-guide/sysctl/vm.html#dirty-background-bytes) | Must be between [0, 68719476736]. |  This setting defines the amount of dirty memory at which the background kernel flusher threads start writeback. Be aware that `vm.dirty_background_bytes` is the counterpart of `vm.dirty_background_ratio`. Only one of these settings can be specified.  
[`vm.dirty_expire_centisecs`](https://docs.kernel.org/admin-guide/sysctl/vm.html#dirty-expire-centisecs) | Must be between [0, 6000]. | This setting defines the maximum age, in hundredths of a second, that dirty data can remain in memory before kernel flusher threads write it to disk.  
[`vm.dirty_ratio`](https://docs.kernel.org/admin-guide/sysctl/vm.html#dirty-ratio) | Must be between [1, 100]. | This setting defines the percentage of system memory that can be filled with dirty pages before processes that perform writes are forced to block and write out dirty data synchronously.  
[`vm.dirty_bytes`](https://docs.kernel.org/admin-guide/sysctl/vm.html#dirty-bytes) | Must be between [0, 68719476736]. |  This setting defines the amount of dirty memory at which a process that generates disk writes starts writeback itself. The minimum value allowed for `vm.dirty_bytes` is two pages in bytes. Any value that's lower than this limit will be ignored and the old configuration will be retained. Be aware that `vm.dirty_bytes` is the counterpart of `vm.dirty_ratio`. Only one of these settings can be specified.  
[`vm.dirty_writeback_centisecs`](https://docs.kernel.org/admin-guide/sysctl/vm.html#dirty-writeback-centisecs) | Must be between [0, 1000]. | This setting defines the interval, in hundredths of a second, at which kernel flusher threads wake up to write old dirty data to disk.  
[`vm.overcommit_memory`](https://docs.kernel.org/admin-guide/sysctl/vm.html#overcommit-memory) | Must be between {0, 1, 2}. |  This setting determines the kernel's strategy for handling memory overcommitment. The values are as follows:

  * `0`: reject large allocations
  * `1`: always allow (default value)
  * `2`: prevent commit beyond swap + ratio of RAM

This setting isn't supported on machines with less than 15 GB memory.  
[`vm.overcommit_ratio`](https://docs.kernel.org/admin-guide/sysctl/vm.html#overcommit-ratio) | Must be between [0, 100]. | This setting defines the percentage of physical RAM allowed for overcommit when the value of the `vm.overcommit_memory` field is set to `2`.  
[`vm.vfs_cache_pressure`](https://docs.kernel.org/admin-guide/sysctl/vm.html#vfs-cache-pressure) | Must be between [0, 100]. | This setting adjusts the kernel's preference for reclaiming memory used for dentry (directory) and inode caches.  
[`vm.swappiness`](https://docs.kernel.org/admin-guide/sysctl/vm.html#swappiness) | Must be between [0, 200]. | This setting controls the tendency of the kernel to move processes out of physical memory and onto the swap disk. The default value is `60`.  
[`vm.watermark_scale_factor`](https://docs.kernel.org/admin-guide/sysctl/vm.html#watermark-scale-factor) | Must be between [10, 3000]. | This setting controls the aggressiveness of kswapd. It defines the memory left before kswapd wakes and the memory to free before it sleeps. The default value is `10`.  
[`vm.min_free_kbytes`](https://docs.kernel.org/admin-guide/sysctl/vm.html#min-free-kbytes) | Must be between [67584, 1048576]. | This setting defines the minimum free memory before OOM. The default value is `67584`.  
  
For more information about the supported values for each `sysctl` flag, see the [\--system-config-from-file gcloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--system-config-from-file).

Different [Linux namespaces](https://en.wikipedia.org/wiki/Linux_namespaces) might have unique values for a given `sysctl` flag, but others might be global for the entire node. Updating `sysctl` options by using a node system configuration helps ensure that the `sysctl` is applied globally on the node and in each namespace, so that each Pod has identical `sysctl` values in each Linux namespace.

## Linux cgroup mode configuration options

**Caution:** GKE deprecates `cgroupv1` with minor version 1.31, and removes support for `cgroupv1` with version 1.35. For more information about how GKE is transitioning to `cgroupv2` and how you can prepare your clusters for this transition, see [Migrate nodes to Linux cgroupv2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-cgroupv2).

The container runtime and `kubelet` use Linux kernel [cgroups](https://www.wikipedia.org/wiki/Cgroups) for resource management, such as limiting how much CPU or memory each container in a Pod can access. There are two versions of the cgroup subsystem in the kernel: `cgroupv1` and `cgroupv2`. Kubernetes support for `cgroupv2` was introduced as alpha in Kubernetes version 1.18, beta in 1.22, and GA in 1.25. For more information, see the [Kubernetes cgroups v2 documentation](https://kubernetes.io/docs/concepts/architecture/cgroups/).

Node system configuration lets you customize the cgroup configuration of your node pools. You can use `cgroupv1` or `cgroupv2`. GKE uses `cgroupv2` for new Standard node pools that run version 1.26 and later, and `cgroupv1` for node pools that run versions earlier than 1.26. For node pools that were created with node auto-provisioning, the cgroup configuration depends on the initial cluster version, not the node pool version. `cgroupv1` is not supported on Arm machines.

You can use node system configuration to change the setting for a node pool to use `cgroupv1` or `cgroupv2` explicitly. Upgrading an existing node pool that uses `cgroupv1` to version 1.26 doesn't change the setting to `cgroupv2`. Existing node pools that run a version earlier than 1.26—and that don't include a customized cgroup configuration—will continue to use `cgroupv1`. To change the setting, you must explicitly specify `cgroupv2` for the existing node pool.

For example, to configure your node pool to use `cgroupv2`, use a node system configuration file such as the following:
    
    
    linuxConfig:
      cgroupMode: 'CGROUP_MODE_V2'
    

The supported `cgroupMode` options are the following:

  * `CGROUP_MODE_V1`: use `cgroupv1` on the node pool.
  * `CGROUP_MODE_V2`: use `cgroupv2` on the node pool.
  * `CGROUP_MODE_UNSPECIFIED`: use the default GKE cgroup configuration.



To use `cgroupv2`, the following requirements and limitations apply:

  * For a node pool that runs a version earlier than 1.26, you must use gcloud CLI version [408.0.0](https://docs.cloud.google.com/sdk/docs/release-notes#40800_2022-11-01) or later. Alternatively, use [gcloud beta](https://docs.cloud.google.com/sdk/gcloud/reference/beta) with version [395.0.0](https://docs.cloud.google.com/sdk/docs/release-notes#39500_2022-07-26) or later.
  * Your cluster and node pools must run GKE version 1.24.2-gke.300 or later.
  * You must use either the Container-Optimized OS with containerd or Ubuntu with containerd [node image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#cos).
  * If any of your workloads depend on reading the cgroup filesystem (`/sys/fs/cgroup/...`), ensure that they are compatible with the `cgroupv2` API.
  * If you use any monitoring or third-party tools, ensure that they are compatible with `cgroupv2`.
  * If you use Java workloads (JDK), we recommend that you use versions which [fully support cgroupv2](https://bugs.openjdk.org/browse/JDK-8230305), including JDK `8u372`, JDK 11.0.16 or later, or JDK 15 or later.



### Verify cgroup configuration

When you add a node system configuration, GKE must re-create the nodes to implement the changes. After you add the configuration to a node pool and the nodes are re-created, you can verify the new configuration.

You can verify the cgroup configuration for nodes in a node pool by using gcloud CLI or the `kubectl` command-line tool:

###  gcloud CLI 

Check the cgroup configuration for a node pool:
    
    
    gcloud container node-pools describe POOL_NAME \
      --format='value(Config.effectiveCgroupMode)'
    

Replace `POOL_NAME` with the name of your node pool.

The potential output is one of the following:

  * `EFFECTIVE_CGROUP_MODE_V1`: the nodes use `cgroupv1`
  * `EFFECTIVE_CGROUP_MODE_V2`: the nodes use `cgroupv2`



The output shows only the new cgroup configuration after the nodes in the node pool are re-created. The output is empty for Windows server node pools, which don't support cgroup.

### kubectl

To use `kubectl` to verify the cgroup configuration for nodes in this node pool, select a node and connect to it by using the following instructions:

  1. [Create an interactive shell](https://kubernetes.io/docs/tasks/debug/debug-cluster/kubectl-node-debug/#debugging-a-node-using-kubectl-debug-node) with any node in the node pool. In the command, replace `mynode` with the name of any node in the node pool.
  2. [Identify the cgroup version on Linux nodes](https://kubernetes.io/docs/concepts/architecture/cgroups/#check-cgroup-version).



## Linux hugepages configuration options

You can use manually pre-allocated hugepages or automatically assigned transparent hugepages.

### Pre-allocated hugepages

You can use a node system configuration file to pre-allocate [hugepages](https://docs.kernel.org/admin-guide/mm/hugetlbpage.html). Kubernetes supports pre-allocated hugepages as a resource type, similar to CPU or memory.

To use hugepages, the following limitations and requirements apply:

  * To ensure that the node is not fully occupied by hugepages, the overall size of the allocated hugepages can't exceed either the following: 
    * **On machines with less than 30 GB memory** : 60% of the total memory. For example, on e2-standard-2 machine with 8 GB of memory, you can't allocate more than 4.8 GB for hugepages.
    * **On machines with more than 30 GB memory** : 80% of the total memory. For example, on c4a-standard-8 machines with 32 GB of memory, hugepages cannot exceed 25.6 GB.
  * 1 GB hugepages are only available on A3, C2D, C3, C3D, C4, C4A, C4D, C4N, CT5E, CT5LP, CT6E, H3, M2, M3, M4, Z3, or Z4D machine types.



The following table describes the modifiable settings for Linux hugepages.

Config parameter | Restrictions | Default value | Description  
---|---|---|---  
`hugepage_size2m` | Integer count. Subject to the previously described memory allocation limits. | `0` | This setting pre-allocates a specific number of 2 MB hugepages.  
`hugepage_size1g` | Integer count. Subject to both of the previously described memory and machine type limitations. | `0` | This setting pre-allocates a specific number of 1 GB hugepages.  
  
### Transparent hugepages (THP)

You can use a node system configuration file to enable the Linux kernel's [Transparent HugePage Support](https://docs.kernel.org/admin-guide/mm/transhuge.html). With THP, the kernel automatically assigns hugepages to processes without manual pre-allocation.

The following table describes the modifiable parameters for THP.

Config parameter | Supported values | Default value | Description  
---|---|---|---  
`transparentHugepageEnabled` | 

  * `TRANSPARENT_HUGEPAGE_ENABLED_ALWAYS`: transparent hugepage is enabled system wide.
  * `TRANSPARENT_HUGEPAGE_ENABLED_MADVISE`: transparent hugepage is enabled inside MADV_HUGEPAGE regions. _This setting is the default kernel configuration._
  * `TRANSPARENT_HUGEPAGE_ENABLED_NEVER`: transparent hugepage is disabled.
  * `TRANSPARENT_HUGEPAGE_ENABLED_UNSPECIFIED`: the default value. GKE does not modify the kernel configuration.

| `UNSPECIFIED` | This setting controls whether THP is enabled for anonymous memory.  
`transparentHugepageDefrag` | 

  * `TRANSPARENT_HUGEPAGE_DEFRAG_ALWAYS`: an application requesting THP stalls on allocation failure and directly reclaims pages and compact memory in an effort to allocate a THP immediately.
  * `TRANSPARENT_HUGEPAGE_DEFRAG_DEFER`: an application wakes kswapd in the background to reclaim pages and wake kcompactd to compact memory so that THP is available in the near future. It is the responsibility of khugepaged to then install the THP pages later.
  * `TRANSPARENT_HUGEPAGE_DEFRAG_DEFER_WITH_MADVISE`: an application enters direct reclaim and compaction like usual, but only for regions that have used `madvise(MADV_HUGEPAGE)`. All other regions wake kswapd in the background to reclaim pages and wake kcompactd to compact memory so that THP is available in the near future.
  * `TRANSPARENT_HUGEPAGE_DEFRAG_MADVISE`: an application enters direct reclaim and compaction like usual, but only for regions that have used `madvise(MADV_HUGEPAGE)`. All other regions wake kswapd in the background to reclaim pages and wake kcompactd to compact memory so that THP is available in the near future.
  * `TRANSPARENT_HUGEPAGE_DEFRAG_NEVER`: an application never enters direct reclaim or compaction.
  * `TRANSPARENT_HUGEPAGE_DEFRAG_UNSPECIFIED`: the default value. GKE does not modify the kernel configuration.

| `UNSPECIFIED` | This setting defines the defragmentation configuration for THP.  
  
THP is available on GKE version 1.33.2-gke.4655000 or later. It is also enabled on new TPU node pools by default on GKE version 1.33.2-gke.4655000 or later. THP isn't enabled when you upgrade existing node pools to a supported version or later.

## Linux accurate time synchronization option

If accurate time synchronization and monitoring the accuracy of your time synchronization is important for your workloads, you can configure _accurate time_ to sync your VM's clock with the host clock by using `chrony` and `ptp_kvm`. Accurate time synchronization is available in GKE version 1.36.0-gke.3241000 and later. This configuration is designed to achieve accuracy within 1 ms for supported setups. For more information about supported machine types, supported operating systems, and supported zones, see [Configure accurate time for Compute Engine VMs](https://docs.cloud.google.com/compute/docs/instances/time-synchronization/configure-time-sync).

The following table describes the parameter to configure accurate time synchronization with GKE:

Config parameter | Supported values | Default value | Description  
---|---|---|---  
  
  * Configuration file: `accurateTimeConfig.enablePtpKvmTimeSync`
  * Terraform: `accurate_time_config.enable_ptp_kvm_time_sync`

| `true` or `false` | `false` | This setting enables accurate time synchronization. This feature is only supported with specific machine types, operating systems, and zones.  
  
After you enable accurate time synchronization, GKE collects and exports the following information:

  * The `compute.googleapis.com/instance/clock_accuracy/ptp_kvm/nanosecond_accuracy` metric, which indicates the VM host clock accuracy to UTC.
  * The `projects/PROJECT_ID/logs/chrony.tracking` log, which contains the tracking logs from `chrony`. These logs provide information such as the gain or loss rate of the system clock.



You can use this information to create log-based metrics and dashboards in Cloud Monitoring to analyze the performance and reliability of the time synchronization.

For example, the following `gke-clock-metric.json` configuration defines a log-based metric of the maximum host clock error:
    
    
    {
      "name": "phc-clock-max-error",
      "description": "Maximum error of the VM clock from the host clock exposed by ptp_kvm",
      "filter": "resource.type=\"k8s_node\" AND log_id(\"chrony.tracking\")",
      "metricDescriptor": {
        "metricKind": "DELTA",
        "valueType": "DISTRIBUTION",
        "unit": "s",
        "labels": []
      },
      "valueExtractor": "REGEXP_EXTRACT(textPayload, \"^.*PHC0.* ([-\\\\d\\\\.eE]+)$\")",
      "bucketOptions": {
        "explicitBuckets": {
          "bounds": [
            0.0, 5.0E-7, 1.0E-6, 2.0E-6, 4.0E-6, 5.0E-6, 8.0E-6, 1.0E-5, 2.0E-5,
            1.0E-4, 0.001, 0.01, 0.1, 1.0
          ]
        }
      }
    }
    

The following `gke-metrics-dashboard.json` configuration defines a Monitoring dashboard that aggregates the error data from the log-based metric and the UTC accuracy metric:
    
    
    {
      "displayName": "Overall Clock Accuracy",
      "dashboardFilters": [],
      "labels": {},
      "mosaicLayout": {
        "columns": 48,
        "tiles": [
          {
            "width": 28,
            "height": 28,
            "widget": {
              "xyChart": {
                "dataSets": [
                  {
                    "plotType": "LINE",
                    "targetAxis": "Y1",
                    "timeSeriesQuery": {
                      "prometheusQuery": "(\n  histogram_quantile(1, sum by (le, node_name) (\n    increase(logging_googleapis_com:user_phc_clock_max_error_bucket{monitored_resource=\"k8s_node\"}[1m])\n  )) * 1000000000\n)\n+ on(node_name) group_left()\nlabel_replace(\n  compute_googleapis_com:instance_clock_accuracy_ptp_kvm_nanosecond_accuracy{monitored_resource=\"gce_instance\"},\n  \"node_name\", \"$1\", \"instance_name\", \"(.*)\"\n)\n",
                      "unitOverride": "ns"
                    }
                  }
                ],
                "chartOptions": {
                  "displayHorizontal": false,
                  "mode": "COLOR"
                },
                "thresholds": [],
                "yAxis": {
                  "label": "Clock Accuracy",
                  "scale": "LINEAR"
                }
              }
            }
          }
        ]
      }
    }
    

## Linux VFIO configuration options

The following table describes the parameter to configure [VFIO](https://doc.dpdk.org/guides/linux_gsg/linux_drivers.html) (Virtual Function I/O) on a node. VFIO allows safe, unprivileged, userspace drivers to access I/O devices.

Config parameter | Restrictions | Default value | Description  
---|---|---|---  
`nodeVfioConfig.dmaEntryLimit` | Must be an integer between `65535` and `4194304`. | `65535` | Specifies the maximum number of DMA entries (pages) that can be mapped by the VFIO IOMMU type 1 driver for a container. This limit affects the total amount of host memory that can be pinned for direct device access, which is often critical for high-performance devices like TPUs and GPUs. This setting corresponds to the following kernel parameter: `/sys/module/vfio_iommu_type1/parameters/dma_entry_limit`. Higher values might be needed for workloads mapping large memory regions.  
  
Available on GKE versions 1.36.0-gke.3009000 or later.  
  
## Linux disk I/O scheduler configuration options

The following table describes the parameters to configure the disk I/O scheduler for node pools.

Config parameter | Supported values | Default value | Description  
---|---|---|---  
`diskIoScheduler.nodeSystemIoScheduler` | `mq-deadline`, `bfq`, `kyber`, `none` | `bfq` for Container-Optimized OS image, `none` for Ubuntu image | Configures the I/O scheduler for the boot disk or ephemeral local SSD that runs node system workloads.  
  
Available on GKE versions 1.36.0-gke.3009000 or later.  
`diskIoScheduler.nodeAttachedDiskIoScheduler` | `mq-deadline`, `bfq`, `kyber`, `none` | `none` | Configures the I/O scheduler for the attached disks.  
  
Available on GKE versions 1.36.0-gke.3009000 or later.  
  
## What's next

  * Learn how to [migrate nodes to Linux cgroupv2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-cgroupv2).
  * Learn how to [add and manage node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools).
  * Learn how to [customize containerd configuration in GKE nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration).
  * Learn how to [automatically bootstrap GKE nodes with DaemonSets](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/automatically-bootstrapping-gke-nodes-with-daemonsets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
