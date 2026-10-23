---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-smt/
title: Configure simultaneous multi-threading (SMT) \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:02.787255+00:00
---

# Configure simultaneous multi-threading (SMT)  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-smt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Configure simultaneous multi-threading (SMT) Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to configure _simultaneous multi-threading_ in your Google Kubernetes Engine (GKE) clusters.

## Overview

GKE [nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes) are Compute Engine virtual machine (VM) instances that GKE creates on your behalf. On these VMs, it's common to have [simultaneous multi-threading (SMT)](https://www.wikipedia.org/wiki/Simultaneous_multithreading) enabled by default. SMT is the ability to execute multiple independent threads on a single physical CPU core. With SMT enabled, a single physical core can run two virtual CPUs (vCPUs) as independent, separate threads. For example, an `n2-standard-32` GKE node is, in fact, running 32 vCPUs on 16 physical CPU cores.

With the introduction of SMT configurability on GKE nodes, you can now configure SMT so that the number of effective vCPUs is equal to the number of physical cores, which means that your GKE nodes can use the full physical core per vCPU.

## Benefits

Configuring SMT on GKE provides the following benefits.

### Improved performance

Some High Performance Computing (HPC) workloads might see a performance improvement by disabling SMT. Typically, for many general computing tasks or tasks that require lots of I/O, SMT can increase application throughput significantly. In contrast, for compute-bound jobs in which both virtual cores are compute bound, SMT can hinder overall application performance and add nondeterministic variance to jobs. Therefore, with SMT disabled, some HPC applications might get better and more predictable performance.

**Note:** To definitively understand any performance benefits, we recommend that you run a direct comparison of your workload performance between GKE nodes that have SMT enabled and nodes with SMT disabled.

### Reduced licensing costs

Some software licensing agreements have billing models that are tied to the number of vCPUs that are consumed. Disabling SMT reduces the number of vCPUs for each core by half, which might reduce your licensing costs. For more information, consult your licensing agreement.

See the pricing section to understand how Google Cloud bills when SMT is configured.

## Limitations

  * **Machine types** : SMT is not configurable on [machine types](https://docs.cloud.google.com/compute/docs/machine-types) that have fewer than 2 vCPUs (for example `n1-standard-1`) or with the [N4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series) or [Tau T2D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2d_machines).
  * **Node auto-provisioning** : SMT configurability is not supported for clusters that have [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) enabled.
  * **Cluster autoscaler** : Scaling from zero nodes with SMT configurability is only supported on the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) for clusters running GKE version 1.21 or later.
  * **GKE Sandbox** : You can configure SMT settings in GKE Sandbox nodes in GKE Standard clusters running version 1.24.2-gke.300 and later using the `--threads-per-core` flag, and in prior versions using a standalone DaemonSet. For instructions, refer to [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-smt#configure-smt). Since multithreading is disabled by default in GKE Sandbox before version 1.24.2-gke.300, configuring SMT using `threads-per-core` is not supported. If you use GKE Sandbox and would like to enable SMT, see [SMT may be disabled](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#hyper-threading_is_disabled).
  * **Cluster mode** : SMT configurability is not supported on GKE [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) clusters.



## Pricing

SMT for GKE is billed based on the underlying [Compute Engine pricing for SMT](https://docs.cloud.google.com/compute/docs/instances/configuring-simultaneous-multithreading#pricing). You are billed for the number of vCPUs defined by a VM's [machine type](https://docs.cloud.google.com/compute/docs/machine-types), not the number of threads that run on each core. Even if you configure SMT, you will continue to be billed for the default number of vCPUs defined by the VM machine type. For more information about how you are billed for VMs, see [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing).

For example, a GKE node created using the `n2-standard-8` machine type runs with SMT enabled by default, and can run up to 8 vCPUs, which is 2 vCPUs for each of the four physical CPU cores. If you configure SMT to use only one thread per core (effectively 4 vCPUs), you are still billed for 8 vCPUs.

## Configure SMT

You can configure SMT on new clusters or node pools by specifying the number of threads per core.

**Note:** You cannot update the number of threads per core on existing node pools.

The following table shows the possible values for threads per core and the corresponding SMT behavior for the node:

Threads per core | SMT behavior  
---|---  
`null` (not specified) | Compute Engine VM default  
`0` | Invalid  
`1` | SMT off  
`2` | SMT on  
`> 2` | Invalid  
  
### Configure SMT on a new cluster

You can configure SMT on new clusters using the gcloud CLI or the Google Cloud console.

### gcloud

To configure SMT, run the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --machine-type=MACHINE_TYPE \
        **--threads-per-core =THREADS_PER_CORE**
    

Replace the following:

  * `CLUSTER_NAME`: the name for the new cluster.
  * `MACHINE_TYPE`: the [machine type](https://docs.cloud.google.com/compute/docs/machine-types) to use for your GKE nodes. This must be a machine type with 2 or more vCPUs.
  * `THREADS_PER_CORE`: the number of threads per physical core. The previous table shows the values you can specify.



For a full list of options, refer to the [`gcloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--threads-per-core) documentation.

### Console

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. In the navigation menu, in the **Node pools** section, click the name of a node pool, and then click **Nodes**.

  3. In the **Machine Configuration** section, select a supported **Machine type** , such as **e2-standard-2**.

  4. Click expand_more **CPU Platform and GPU**.

  5. From the **vCPUs to core ratio** drop-down menu, select one of the following:

     * **1 vCPU per core** : turn SMT off.
     * **2 vCPUs per core** : keep SMT on.
  6. Configure the cluster and node pools as required, and then click **Create**.




### Configure SMT on a new node pool

You can configure SMT on new node pools using the gcloud CLI or the Google Cloud console.

### gcloud

To configure SMT, run the following command:
    
    
    gcloud container node-pools create POOL_NAME \
        --cluster=CLUSTER_NAME \
        --machine-type=MACHINE_TYPE \
        **--threads-per-core =THREADS_PER_CORE**
    

Replace the following:

  * `POOL_NAME`: the name for the new node pool.
  * `CLUSTER_NAME`: the name of the existing cluster.
  * `MACHINE_TYPE`: the [machine type](https://docs.cloud.google.com/compute/docs/machine-types) to use for your GKE nodes. This must be a machine type with 2 or more vCPUs.
  * `THREADS_PER_CORE`: the number of threads per physical core. The previous table shows the values you can specify.



For a full list of options, refer to the [`gcloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--threads-per-core) documentation.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster that you want to modify.

  3. Click the **Nodes** tab.

  4. Click add_box **Create user-managed node pool**.

  5. In the navigation menu, click **Nodes**.

  6. In the **Machine Configuration** section, select a **Machine family** and a **Machine type** that support SMT, such as **n2-standard-2**.

  7. Click expand_more **CPU Platform and GPU**.

  8. From the **vCPUs to core ratio** drop-down menu, select one of the following options:

     * **1 vCPU per core** : turn SMT off.
     * **2 vCPUs per core** : keep SMT on.
  9. Configure the node pool as needed, and then click **Create**.




## Verify the SMT configuration

### Linux

To verify the SMT configuration on Linux nodes, perform the following steps:

  1. SSH into the node:
         
         gcloud compute ssh NODE_NAME
         

Replace `NODE_NAME` with the name of your node.

  2. Check the number of vCPUs:
         
         cat /proc/cpuinfo | grep processor | wc -l
         

The output is similar to the following:
         
         16
         

If you set the number of threads per core to `1`, the output should show half the Compute Engine VM default number of vCPUs. For example, the output for the `n2-standard-32` with SMT off should be `16` instead of the default value of `32`.




### Windows

To verify the SMT configuration on Windows nodes, perform the following steps:

  1. Set a username and password to RDP to the node:
         
         gcloud compute reset-windows-password NODE_NAME
         

Replace `NODE_NAME` with the name of your node.

  2. Establish a connection to the `EXTERNAL_IP:3389` for the VM.

  3. Run the following powershell command:
         
         Get-WmiObject -Class Win32_Processor -ComputerName. | Select-Object -Property [a-z]* | Select NumberOfCores,NumberOfLogicalProcessors
         

If you set the number of threads per core to `1`, the `NumberOfCores` value should be equal to the `NumberOfLogicalProcessors` value, such as in the following example output:
         
         Output (example n1-standard-2 with SMT off)
         
         NumberOfCores NumberOfLogicalProcessors
         ------------- -------------------------
                     1                         1
         




## What's next

  * [Learn about the available machine types.](https://docs.cloud.google.com/compute/docs/machine-types)
  * [Learn how to specify a minimum CPU platform for your GKE nodes.](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/min-cpu-platform)
  * [Learn about using Compute Engine sole-tenant nodes in GKE.](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sole-tenancy)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
