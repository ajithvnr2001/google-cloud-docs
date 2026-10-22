---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/performance-tuning/
title: Tune node performance \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:23.698454+00:00
---

# Tune node performance  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/performance-tuning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Tune node performance Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

One way to improve performance for container-based applications is to increase cluster resources by adding nodes or adding resources, like CPUs or memory, to your nodes. This approach, however, can become expensive. _Tuning_ your cluster Nodes for better performance helps you optimize resource utilization for your workloads in a cost-effective way. This document describes how to use Performance Tuning Operator to tune worker nodes to optimize workload performance for Google Distributed Cloud.

To get the most from underlying hardware and software, different types of applications, especially high-performance applications, benefit from tuning node settings like the following:

  * Dedicated CPUs for performance-sensitive workloads
  * Reserved CPUs for standard Kubernetes Daemons and Services
  * Increased memory page sizes with 1 GiB (gibibyte) or 2 MiB (mebibyte) hugepages
  * Workload distribution based on the system architecture, such as multi-core processors and NUMA



With Performance Tuning Operator, you configure node-level performance settings by creating Kubernetes custom resources that apply performance configurations. Here are the benefits:

  * **Single, unified configuration interface:** With Performance Tuning Operator, you update one or more `PerformanceTuningProfile` manifests that can be applied to worker nodes with node selectors. You don't need to configure each node individually with multiple configuration and policy settings. This approach lets you manage node-level and container-level configurations in a single, unified way.

  * **Persistence and reliability:** You also get all the reliability that Kubernetes provides with its high-availability architecture. `PerformanceTuningProfile` custom resources can be updated whenever you like and their settings persist across major cluster operations, such as upgrades.




Performance Tuning Operator works by orchestrating the following performance-related Kubernetes and operating system (OS) features and tools:

  * [Memory Manager](https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/)
  * [CPU Manager](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/)
  * [Topology Manager](https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/)
  * [TuneD](https://tuned-project.org/)



To prevent conflicts, when you use Performance Tuning Operator, we recommend that you don't use the previously mentioned Kubernetes and OS tools and features independently.

## Prerequisites and limitations

Here are the prerequisites and limitations for using Performance Tuning Operator:

  * **Red Hat Enterprise Linux (RHEL) only:** Performance Tuning Operator is supported for nodes running [supported versions of RHEL](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-os/rhel) only.

  * **User or hybrid cluster with worker nodes:** Performance Tuning Operator is supported for use with worker nodes in user or hybrid clusters only. Using Performance Tuning Operator to tune control plane nodes isn't supported. Performance Tuning Operator uses a node selector to determine how to apply tuning profiles. To ensure that tuning profiles are applied to worker nodes only, the `nodeSelector` in each profile custom resource must include the standard worker node label `node-role.kubernetes.io/worker: ""`. If the `nodeSelector` in a tuning profile matches labels on a control plane node, that node isn't tuned and an error condition is set. For more information about error conditions, see Check status. Make sure your cluster is operating correctly before installing Performance Tuning Operator and applying tuning profiles.

  * **TuneD 2.22.0:** Performance Tuning Operator requires TuneD version 2.22.0 to be pre-installed in worker nodes you intend to tune. For additional information about TuneD, including installation instructions, see [Getting started with TuneD](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/monitoring_and_managing_system_status_and_performance/getting-started-with-tuned_monitoring-and-managing-system-status-and-performance) in the Red Hat Enterprise Linux documentation. Performance Tuning Operator uses TuneD with the `cpu-partitioning` profile. If you don't have this profile, you can install it with the following command:
        
        dnf install -y tuned-profiles-cpu-partitioning
        

  * **Workload resource requirements:** To get the most from performance tuning, you should have a good understanding of the memory and CPU requirements (resource requests and limits) for your workloads.

  * **Available node resources:** Find the CPU and memory resources for your nodes. You can get detailed CPU and memory information for your node in the `/proc/cpuinfo` and `/proc/meminfo` files respectively. You can also use `kubectl get nodes` to retrieve the amount of compute and memory resources (`status.allocatable`) a worker node has that are available for Pods.

  * **Requires draining:** As part of the tuning process, Performance Tuning Operator first drains nodes, then applies a tuning profile. As a result, nodes may report a `NotReady` status during performance tuning. We recommend that you use the rolling update strategy (`spec.updateStrategy.type: rolling`) instead of a batch update to minimize workload unavailability.

  * **Requires rebooting:** For node tuning changes to take effect, Performance Tuning Operator reboots the node after applying the tuning profile.




## Install Performance Tuning Operator

Performance Tuning Operator consists primarily of two controllers (a Deployment and a DaemonSet) that interact with each other to tune nodes based on your profile settings. Performance Tuning Operator isn't installed with Google Distributed Cloud, by default. You download the Performance Tuning Operator manifests from Cloud Storage and you use `kubectl apply` to create Performance Tuning Operator resources on your cluster.

To enable performance tuning with default values for your cluster:

  1. Create a `performance-tuning` directory on your admin workstation.

  2. From the `performance-tuning` directory, download the latest Performance Tuning Operator package from the Cloud Storage release bucket:
         
         gcloud storage cp gs://anthos-baremetal-release/node-performance-tuning/0.1.0-gke.47 . --recursive
         

The downloaded files include manifests for the `performance-tuning-operator` Deployment and the `nodeconfig-controller-manager` DaemonSet. Manifests for related functions, such as role-based access control (RBAC) and dynamic admission control, are also included.

  3. As the root user, apply all of Performance Tuning Operator manifests recursively to your user (or hybrid) cluster:
         
         kubectl apply -f performance-tuning --recursive –-kubeconfig USER_KUBECONFIG
         

Once the Deployment and DaemonSet are created and running, your only interaction is to edit and apply `PerformanceTuningProfile` manifests.




## Review the resource requirements for your workloads

Before you can tune your nodes, you need to understand the computing and memory resource requirements of your workloads. If your worker nodes have sufficient resources, nodes can be tuned to provide guaranteed memory (standard and hugepages) for your workloads in the guaranteed Quality of Service (QoS) class.

Kubernetes assigns QoS classes to each of your Pods, based on the resource constraints you specify for the associated containers. Kubernetes then uses QoS classes to determine how to schedule your Pods and containers and allocate resources to your workloads. To take full advantage of Node tuning for your workloads, your workloads must have CPU or memory resource requests or limits settings.

To be assigned a QoS class of guaranteed, your Pods must meet the following requirements:

  * For each Container in the Pod: 
    * Specify values for both memory resource requests (`spec.containers[].resources.requests.memory`) and limits (`spec.containers[].resources.limits.memory`).
    * The memory limits value must equal the memory requests value.
    * Specify values for both CPU resource requests (`spec.containers[].resources.requests.cpu`) and limits (`spec.containers[].resources.limits.cpu`).
    * The CPU limits value must equal the CPU requests value.



The following Pod spec excerpt shows CPU resources settings that meet the guaranteed QoS class requirements:
    
    
    spec:
      containers:
      - name: sample-app
        image: images.my-company.example/app:v4
        resources:
          requests:
            memory: "128Mi"
            cpu: "2"
          limits:
            memory: "128Mi"
            cpu: "2"
      ...
    

When you retrieve pod details with `kubectl get pods`, the `status` section should include the assigned QoS class as shown in the following example:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      creationTimestamp: "2023-09-22T21:05:23Z"
      generateName: my-deployment-6fdd69987d-
      labels:
        app: metrics
        department: sales
        pod-template-hash: 6fdd69987d
      name: my-deployment-6fdd69987d-7kv42
      namespace: default
      ...
    spec:
      containers:
      ...
    status:
      conditions:
      - lastProbeTime: null
        lastTransitionTime: "2023-09-22T21:05:23Z"
        status: "True"
        type: Initialized
      ...**  qosClass: BestEffort**
      startTime: "2023-09-22T21:05:23Z"
    

For more information about the QoS classes, see [Pod Quality of Service Classes](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/) in the Kubernetes documentation. For instructions for configuring your Pods and containers so that they get assigned a QoS class, see [Configure Quality of Service for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/)

### CPU requirements

When tuning a node, you can specify a set of _reserved_ CPU cores (`spec.cpu.reservedCPUs`) for running Kubernetes system daemons like the kubelet and container runtime. This same set of reserved CPUs runs operating system daemons, such as `sshd` and `udev`, too. The remainder of CPU cores on the are allocated as _isolated_. The isolated CPUs are meant for _CPU-bound_ applications, which require dedicated CPU time without interference from other applications or interrupts from network or other devices.

To schedule a Pod on the isolated CPUs of a worker node:

  * Configure the Pod for a guaranteed quality of service (QoS).

  * The CPU requirements and limits must be specified in integers. If you specify partial CPU resources in your Pod spec, such as `cpu: 0.5` or `cpu: 250m` (250 millicores), scheduling can't be guaranteed.




### Memory requirements

When tuning a node with Performance Tuning Operator, you can create hugepages and associate them with the non-uniform memory access (NUMA) nodes on the machine. Based on Pod and Node settings, Pods can be scheduled with NUMA-node affinity.

## Create a performance tuning profile

After you've installed Performance Tuning Operator, you interact only with the cluster that runs your workloads. You create `PerformanceTuningProfile` custom resources directly on your user cluster or hybrid cluster, not on your admin cluster. Each `PerformanceTuningProfile` resource contains a set of parameters that specifies the performance configuration that's applied to a node.

The `nodeSelector` in the resource determines the nodes to which the tuning profile is applied. To apply a profile to a node, you place the corresponding key-value pair label on the node. A tuning profile is applied to nodes that have all the labels specified in the `nodeSelector` field.

You can create multiple `PerformanceTuningProfile` resources in a cluster. If more than one profile matches a given node, then an error condition is set in the `status` of the `PerformanceTuningProfile` custom resource. For more information about the `status` section, see Check status.

Set the namespace for your `PerformanceTuningProfile` custom resource to `kube-system`.

To tune one or more worker nodes:

  1. Edit the `PerformanceTuningProfile` manifest.

For information about each field in the manifest and a sample manifest, see the `PerformanceTuningProfile` resource reference.

  2. (Optional) For the worker Nodes to which you're applying a profile, add labels to match the `spec.nodeSelector` key-value pair.

If no `spec.nodeSelector` key-value pair is specified in the `PerformanceTuningProfile` custom resource, the profile is applied to all worker nodes.

  3. Apply the manifest to your cluster.
         
         kubectl apply -f PROFILE_MANIFEST --kubeconfig KUBECONFIG
         

Replace the following:

     * `PROFILE_MANIFEST`: the path of the manifest file for the `PerformanceTuningProfile` custom resource.
     * `KUBECONFIG`: the path of the cluster kubeconfig file.



## Remove a tuning profile

To reset a node to its original, untuned state:

  1. Delete the `PerformanceTuningProfile` custom resource from the cluster.

  2. Update or remove the labels on the node so that it isn't selected by the tuning profile, again.




If you have multiple tuning profiles associated with the node, repeat the preceding steps, as needed.

## Pause a tuning profile

If you need to perform maintenance on your cluster, you can temporarily pause tuning by editing the `PerformanceTuningProfile` custom resource. We recommend that you pause tuning before you perform critical cluster operations, such as a cluster upgrade.

Unsuccessful profile application is another case where you might pause tuning. If the tuning process is unsuccessful, the controller may continue trying to tune the node, which may result in the node rebooting over and over. If you observe the node status flipping between the ready and not ready state, pause tuning so that you can recover from the broken state.

To pause tuning:

  1. Edit the `PerformanceTuningProfile` custom resource manifest to set `spec.paused` to `true`.

  2. Use `kubectl apply` to update the resource.




When performance tuning is paused, the Performance Tuning Operator controller stops all of its operations. Pausing prevents the risk of Performance Tuning Operator controller operations conflicting with any Google Distributed Cloud controller operations.

## `PerformanceTuningProfile` resource reference

This section describes each of the fields in the `PerformanceTuningProfile` custom resource. This resource is used to create a tuning profile for one or more of your cluster nodes. All the fields in the resource are mutable after profile creation. Profiles have to be in the `kube-system` namespace.

The following `numa` sample profile manifest for nodes with 8 CPU cores specifies the following resource allocations:

  * 4 CPU cores (`0-3`) are reserved for Kubernetes system overhead.

  * 4 CPU cores (`4-7`) are set aside for workloads only.

  * Node memory is split into 2‑MiB pages by default, instead of the standard 4‑Ki pages.

  * 10 pages of memory sized at 1 GiB are set aside for use by NUMA node 0.

  * 5 pages of memory sized at 2 MiB are set aside for use by NUMA node 1.

  * Topology Manager uses the [best-effort policy](https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/#policy-best-effort) for scheduling workloads.



    
    
    apiVersion: anthos.gke.io/v1alpha1
    kind: PerformanceTuningProfile
    metadata:
      name: numa
      namespace: kube-system
    spec:
      cpu:
        isolatedCPUs: 4-7
        reservedCPUs: 0-3
      defaultHugepagesSize: 2M
      nodeSelector:
        app: database
        node-role.kubernetes.io/worker: ""
      pages:
      - count: 10
        numaNode: 0
        size: 1G
      - count: 5
        numaNode: 1
        size: 2M
      topologyManagerPolicy: best-effort
    

You can retrieve the related `PerformanceTuningProfile` custom resource definition from the `anthos.gke.io` group in your cluster. The custom resource definition is installed once the preview feature annotation is added to the self-managed cluster resource.

### CPU configuration

Property | Description  
---|---  
`cpu.reservedCPUs` | Required. Mutable. String. This field defines a set of CPU cores to reserve for Kubernetes system daemons, such as the kubelet, the container runtime, and the node problem detector. These CPU cores are also used for operating system (OS) system daemons, such as `sshd` and `udev`. The `cpu.reservedCPUs` field takes a list of CPU numbers or ranges of CPU numbers. Ensure that the list of CPUs doesn't overlap with the list specified with `cpu.isolatedCPUs`. The union of the CPUs listed in these two fields must include all CPUs for the node.  
`cpu.isolatedCPUs` | Optional. Mutable. String. The `cpu.isolatedCPUs` field defines a set of CPUs that are used exclusively for performance sensitive applications. CPU Manager schedules containers on the non-reserved CPUs only, according to Kubernetes [Quality of Service (QoS) classes](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/). To ensure that workloads run on the isolated CPUs, [configure Pods with the guaranteed QoS class](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/) and [assign a CPU resource to the Pod or Container](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/). For guaranteed Pod scheduling, you must specify integer CPU units, not partial CPU resources (`cpu: "0.5"`). 
    
    
    apiVersion: v1
    kind: Pod
    ...
    spec:
      containers:
      ...
        resources:
          limits:**        cpu: "1"**
          requests:**        cpu: "1"**
      ...

Maximizing isolated CPUs for workloads provides the best performance benefit. This field takes a list of CPU numbers or ranges of CPU numbers. Ensure that the list of CPUs doesn't overlap with the list specified with `cpu.reservedCPUs` and that the union of the lists in these two fields includes all CPUs for the node.  
`cpu.balanceIsolated` | Optional. Mutable. Boolean. Default: `true`. This field specifies whether or not the Isolated CPU set is eligible for automatic load balancing of workloads across CPUs. When you set this field to `false`, your workloads have to assign each thread explicitly to a specific CPU to distribute the load across CPUs. With explicit CPU assignments, you get the most predictable performance for guaranteed workloads, but it adds more complexity to your workloads.  
`cpu.globallyEnableIRQLoadBalancing` | Required. Mutable. Boolean. Default: `true`. This field specifies whether or not to enable interrupt request (IRQ) load balancing for the isolated CPU set.   
  
### Memory configuration

Property | Description  
---|---  
`defaultHugePageSize` | Optional. Mutable. Enumeration: `1G` or `2M`. This field defines the default hugepage size in kernel boot parameters. Hugepages are allocated at boot time, before memory becomes fragmented. It's important to notice that setting hugepages default size to 1G removes all 2M related folders from the node. A default hugepage size of 1G prevents you from configuring 2M hugepages in the node.   
`pages` | Optional. Mutable. Integer. This field specifies the number of hugepages to create at boot time. This field accepts an array of pages. Check available memory for your nodes before specifying hugepages. Don't request more hugepages than needed and don't reserve all memory for hugepages, either. Your workloads need standard memory, as well.   
  
### Node Selection

Property | Description  
---|---  
`nodeSelector` | Required. Mutable. This field always requires the Kubernetes worker node label, `node-role.kubernetes.io/worker:""`, which ensures that performance tuning is done on worker nodes only. This field takes an optional node label as a key-value pair. The key-value pair labels are used to select specific worker nodes with matching labels. When the `nodeSelector` labels match labels on a worker node, the performance profile is applied to that node. If you don't specify a key-value label in your profile, it's applied to all worker nodes in the cluster. For example, the following `nodeSelector` specifies that the tuning profile is applied only to worker nodes with matching `app: database` labels:
    
    
    ...
    spec:
      nodeSelector:
        app: database
        node-role.kubernetes.io/worker: ""
      ...  
  
### Kubelet Configuration

Property | Description  
---|---  
`topologyManagerPolicy` | Optional. Mutable. Enumeration: `none`, `best-effort`, `restricted`, or `single-numa-node`. Default: `best-effort`. This field specifies the Kubernetes [Topology Manager policy](https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/#topology-manager-policies) used to allocate resources for your workloads, based on assigned quality of service (QoS) class. For more information about how QoS classes are assigned, see [Configure Quality of Service for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/).   
  
### Profile operations

Property | Description  
---|---  
`paused` | Optional. Mutable. Boolean. Set `paused` to `true` to temporarily prevent the DaemonSet controllers from tuning selected nodes.  
`updateStrategy` | Optional. Mutable. Specifies the strategy for applying tuning configuration changes to selected nodes.  
`updateStrategy.rollingUpdateMaxUnavailalble` | Optional. Mutable. Integer. Default: `1`. Specifies the maximum number of nodes that can be tuned at the same time. This field applies only when `type` is set to `rolling`.  
`updateStrategy.type` | Optional. Mutable. Enumeration: `batch` or `rolling`. Default: `rolling`. Specifies how to apply profile updates to selected nodes. If you want to apply the update to all selected nodes at the same time, set `type` to `batch`. By default, updates are rolled out sequentially to individual nodes, one after the other.  
  
## Check status

After the `PerformanceTuningProfile` custom resource is created or updated, a controller tunes the selected nodes based on the configuration provided in the resource. To check the status of the `PerformanceTuningProfile`, we are exposing the following field in `Status`:

Property | Description  
---|---  
`conditions` | Condition represents the latest available observations of the current state of the profile resource.  
`conditions.lastTransitionTime` | Always returned. String (in date-time format). Last time the condition transitioned from one status to another. This time usually indicates when the underlying condition changed. If that time isn't known, then the time indicates when the API field changed.  
`conditions.message` | Optional. String. A human readable message indicating details about the transition. This field might be empty.   
`conditions.observedGeneration` | Optional. Integer. If set, this field represents the `metadata.generation` that the condition was set based on. For example, if `metadata.generation` is `12`, but the `status.condition[x].observedGeneration` is `9`, the condition is out of date regarding the current state of the instance.  
`conditions.reason` | Required. String. The reason for the last condition transition.  
`conditions.status` | Required. Status of the condition: `True`, `False`, or `Unknown`.  
`conditions.type` | Required. Type is the condition type: `Stalled` or `Reconciling`.  
`readyNodes` | The number of nodes to which the tuning profile has been successfully applied.  
`reconcilingNodes` | The number of selected (or previously selected) nodes that are in the process of being reconciled with the latest tuning profile by the `nodeconfig-controller-manager` DaemonSet.  
`selectedNodes` | The number of notes that have been selected. That is, the number of nodes that match the node selector for this `PerformanceTuningProfile` custom resource.  
  
## What's next

  * [Set up SR-IOV networking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/sriov)
  * [etcd performance](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/scale#etcd_performance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
