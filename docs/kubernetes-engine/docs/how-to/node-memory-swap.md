---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-memory-swap/
title: Configure nodes to use disk space as virtual memory \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:17.107900+00:00
---

# Configure nodes to use disk space as virtual memory  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-memory-swap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Configure nodes to use disk space as virtual memory Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Google Kubernetes Engine (GKE) node memory swap lets GKE nodes use disk space as virtual memory when physical memory is exhausted. Node memory swap can help improve application resilience and prevent out-of-memory (OOM) errors for certain workloads.

## When to use node memory swap

Use node memory swap to provide a buffer against OOM errors for memory-intensive applications, especially during unexpected usage spikes. Node memory swap can help improve your workload resilience, such as in the following scenarios:

  * Run workloads with unpredictable memory patterns.
  * Reduce the risk of applications crashing because of node memory exhaustion.
  * Optimize costs by avoiding the need to overprovision memory for occasional peaks.



## How node memory swap works

When you enable node memory swap, GKE configures the node's operating system to use disk space as virtual memory. This process provides a buffer for applications that experience temporary memory pressure.

GKE calculates [container swap limits](https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/) based on the container's memory resource limits and the node's total memory.

You can configure swap on different storage types to balance performance and cost:

  * **Boot disk** : uses the node's boot disk for swap space.
  * **Ephemeral local SSD** : uses a local SSD that is also shared with Pod ephemeral storage.
  * **Dedicated local SSD** : reserves one or more local SSDs exclusively for swap.



To protect sensitive data, GKE encrypts swap space by default using an ephemeral key.

## Requirements and limitations

Node memory swap has the following requirements and limitations:

  * GKE clusters must be version `1.34.1-gke.1341000` or later.
  * Only Pods that have the `Burstable` Quality of Service (QoS) class can use node memory swap. For more information about QoS classes, see the Kubernetes documentation for [Pod quality of service classes](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#burstable).
  * To resize the memory resources of containers, you must set the [container resize policy](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/#container-resize-policies) to `RestartContainer`.
  * If you configure node memory swap to use a boot disk, the swap size cannot exceed 50% of the boot disk's total capacity.



If you configure node memory swap to use a local SSD, you must ensure the following requirements are met:

  * The machine type must support local SSDs. You can't use raw block storage with a local SSD.
  * Nodes must be provisioned with local SSDs. The provisioning method depends on the machine series: 
    * For first or second generation machine series, set the `--ephemeral-storage-local-ssd=count` flag.
    * For third or fourth generation machine series, choose a machine type that bundles local SSDs.
  * The default `e2-medium` machine type does not support local SSDs, so you must select a different machine type.
  * For instructions on how to create or update a cluster so it provisions local SSDs, see [Provision and use Local SSD-backed ephemeral storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd).



## Best practices

Node memory swap is intended as a safety net for unpredictable memory spikes, not a replacement for sufficient physical memory. For guidance on optimizing workloads, see [Right-size your GKE workloads at scale](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/right-size-workloads-at-scale).

You should also consider the following best practices when using node memory swap:

  * Isolate node memory swap-enabled nodes by [applying a taint to the node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/isolate-workloads-dedicated-nodes), for example, `gke-swap=enabled:NoSchedule`, and adding a corresponding toleration to the workloads intended to use swap.
  * Size your node memory swap space appropriately. Insufficient node memory swap space might not prevent OOM errors, and excessive use can degrade performance.
  * Monitor node memory swap use on your workloads. Frequent use of node memory swap can be an indicator of memory pressure.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Enable node memory swap

You can enable node memory swap on a cluster or node pool basis. To enable node memory swap, create or update a `system-config.yaml` file that contains the node memory swap configuration that you want. The following example enables node memory swap with default settings:
    
    
    linuxConfig:
      swapConfig:
        enabled: true
    

There are additional settings that you can configure. This example configures unencrypted swap to use 30% of an ephemeral local SSD's storage:
    
    
    linuxConfig:
      swapConfig:
        enabled: true
        encryptionConfig:
          disabled: true
        ephemeralLocalSsdProfile:
          swapSizePercent: 30
    

For a list of optional fields that you can configure, see the [`LinuxNodeConfig` API documentation](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/LinuxNodeConfig#swapconfig).

### Enable node memory swap on a cluster

To enable node memory swap on a cluster, complete one of the following steps:

  * To create a new cluster with node memory swap enabled, run the following command:
        
        gcloud container clusters create CLUSTER_NAME \
            --location=LOCATION \
            --cluster-version=1.34.1-gke.1341000 \
            --system-config-from-file=system-config.yaml
        

Replace the following:

    * `CLUSTER_NAME`: the name of your new cluster.
    * `LOCATION`: the region or zone for your cluster.
**Note:** For local SSDs on first and second generation machine types, pass the [`--ephemeral-storage-local-ssd` flag](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd).
  * To update an existing cluster to enable node memory swap, run the following command:
        
        gcloud container clusters update CLUSTER_NAME \
            --location=LOCATION \
            --system-config-from-file=system-config.yaml
        

Replace the following:

    * `CLUSTER_NAME`: the name of your new cluster.
    * `LOCATION`: the region or zone for your cluster.



### Enable node memory swap on a node pool

To enable node memory swap on a node pool, complete one of the following steps:

  * To create a new node pool with node memory swap enabled, run the following command:
        
        gcloud container node-pools create NODEPOOL_NAME \
            --cluster=CLUSTER_NAME \
            --location=LOCATION \
            --node-version=1.34.1-gke.1293000 \
            --system-config-from-file=system-config.yaml \
            --machine-type=MACHINE_TYPE
        

Replace the following:

    * `NODEPOOL_NAME`: the name of your new node pool.
    * `CLUSTER_NAME`: the name of your cluster.
    * `LOCATION`: the region or zone for your cluster.
    * `MACHINE_TYPE`: a compatible machine type. For local SSDs, ensure that you choose a machine type that [bundles local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd), for example `n1-standard-1`.
**Note:** For local SSDs on first and second generation machine types, pass the [`--ephemeral-storage-local-ssd` flag](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd).
  * To update an existing node pool to enable node memory swap, run the following command:
        
        gcloud container node-pools update NODEPOOL_NAME \
            --cluster=CLUSTER_NAME \
            --location=LOCATION \
            --system-config-from-file=system-config.yaml
        

Replace the following:

    * `NODEPOOL_NAME`: the name of your node pool.
    * `CLUSTER_NAME`: the name of your cluster.
    * `LOCATION`: the region or zone for your cluster.



## Verify the configuration

To verify that node memory swap is enabled, complete the following steps:

  1. Verify that the `system-config.yaml` is applied with the `swapConfig` settings by running the following command:
         
         gcloud container node-pools describe NODEPOOL_NAME \
             --cluster=CLUSTER_NAME \
             --location=LOCATION \
             --format='yaml(config.linuxNodeConfig.swapConfig)'
         

  2. Verify the kubelet configuration exists on the node by running the following command:
         
         kubectl get --raw "/api/v1/nodes/NODE_NAME/proxy/configz" | jq .kubeletconfig.memorySwap
         




## Monitor memory swap use

You can monitor node memory with Cloud Monitoring or `kubectl`.

###  Monitoring 

The following system metrics are available by default for observing swap usage:

  * `kubernetes.io/node/memory/swap_used_bytes`
  * `kubernetes.io/container/memory/swap_used_bytes`



GKE also provides container-level swap usage metrics through cAdvisor. To use these metrics, [enable cAdvisor on the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cadvisor-kubelet-metrics):

  * `prometheus.googleapis.com/container_memory_swap/gauge`



### kubectl

Monitor swap usage with `kubectl` commands by completing the following steps:

  1. Check the `SwapDetected` condition on the node object by running the following command:
         
         kubectl get node NODE_NAME -o jsonpath='{.status.conditions[?(@.type=="Swap")]}' | jq .
         

The output is similar to the following:
         
         {
           "lastHeartbeatTime": "2025-07-11T00:14:52Z",
           "lastTransitionTime": "2025-06-25T05:20:10Z",
           "message": "Swap is active: Total=49Gi Used=0B Free=49Gi",
           "reason": "SwapDetected",
           "status": "True",
           "type": "Swap"
         }
         

  2. Check the swap capacity by running the following command:
         
         kubectl get node NODE_NAME -o jsonpath='{.status.nodeInfo.swap}'
         

The output is similar to the following:
         
         {"capacity":53687087104}
         




## Disable node memory swap

To disable node memory swap, update your `system-config.yaml` file by completing the following steps:

  1. Update the `system-config.yaml` file to set `swapConfig.enabled` to `false`:
         
         linuxConfig:
           swapConfig:
             enabled: false
         

  2. Update the node pool with the new configuration:
         
         gcloud container node-pools update NODEPOOL_NAME \
             --cluster=CLUSTER_NAME \
             --location=LOCATION \
             --system-config-from-file=system-config.yaml
         




## What's next

  * Learn more about [customizing node system configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config).
  * Learn more about [GKE storage options](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/storage-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
