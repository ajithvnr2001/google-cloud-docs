---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nested-virtualization/
title: Use nested VMs with GKE clusters \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:53.800392+00:00
---

# Use nested VMs with GKE clusters  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nested-virtualization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Use nested VMs with GKE clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can create virtual machine (VM) instances inside of other VMs by using [_nested virtualization_](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview). Compute Engine adds virtualization instructions to specific machine series so that those VM instances can create nested VMs. Because Google Kubernetes Engine (GKE) [nodes run on Compute Engine VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes), your GKE workloads can create and use nested VMs. This document shows you how to enable nested virtualization in GKE.

## How nested VMs work in GKE

To use nested VMs in GKE, you enable nested virtualization for specific nodes or node pools. The corresponding CPU virtualization extensions, such as [Intel Virtualization Technology (VT-x)](https://en.wikipedia.org/wiki/X86_virtualization#Intel_virtualization_\(VT-x\)) or [AMD Virtualization (AMD-V)](https://en.wikipedia.org/wiki/X86_virtualization#AMD_virtualization_\(AMD-V\)) are enabled in the underlying VMs. You can then trigger the creation of nested VMs from Pods by using software like [QEMU](https://www.qemu.org/) or [Kata Containers](https://katacontainers.io/).

**Caution:** Third-party softwawre like QEMU and Kata Containers aren't Google Cloud products. If you install and use this software, then you're responsible for management and troubleshooting. Google's support and SLAs don't apply to these third-party products.

In GKE, nested VMs are useful for the following use cases:

  * Run untrusted code like AI agents in lightweight VMs, such as Kata Containers. For more information about this use case, see [Use open source Kata Containers with GKE Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox/tree/main/examples/kata-gke-sandbox).
  * Add a layer of hardware-assisted isolation for multi-tenant workloads.
  * Run specialized software like Android emulators in the cloud.



### Reduced performance implications

With hardware-assisted nested virtualization, workloads running on the nested VMs might experience [reduced performance](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview#performance_considerations) when compared to non-nested virtualization configurations. The amount of performance impact depends on the specific workload profile, including its I/O and memory usage characteristics.

Additionally, creating nested VMs on the GKE nodes' underlying VMs might affect the performance of other workloads running on those nodes.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * [Ensure that your organization policy supports creating nested VMs](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/managing-constraint#check_whether_nested_virtualization_is_allowed).
  * Review the nested VM [restrictions](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview#restrictions).



### Requirements and limitations

Consider the following information before enabling nested virtualization with GKE and allowing your Pods to create nested VMs:

  * You can only configure node pools with nested VMs with a limited number of VM machine series. See the **Nested virtualization** row of the [Machine series comparison](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison) to confirm supported machine series.
  * Nested virtualization isn't supported in Windows Server node pools.
  * You can't use nested virtualization if the [_Disable VM nested virtualization_ constraint](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/managing-constraint#console) is enforced for your organization policy.
  * You must set `securityContext.privileged:true` for Pods to interact with nested VMs.
  * If you use GKE Autopilot, then you can't create privileged Pods nodes except in the following scenarios:

    * The Pods are owned by GKE, a [GKE partner](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners), or an [approved open source project](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/run-autopilot-open-source-workloads).
    * The Pods are owned by you and are included in a [WorkloadAllowlist](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-privileged-workloads).
  * You can't enable nested virtualization in existing node pools.

  * Nested virtualization is an immutable setting in GKE.

  * If you use ComputeClasses to enable nested virtualization, then your cluster must run GKE version 1.37.0-gke.4713000 or later.




## Enable nested virtualization

The following sections show you how to enable nested virtualization in GKE in the following ways:

  * **Use ComputeClasses** : in Autopilot or Standard mode, enable nested virtualization for specific node configurations in a ComputeClass. By using this method, you can enable nested virtualization in auto-created node pools and fall back across multiple prioritized node configurations.
  * **Use the GKE API** : in Standard mode, use a client like the Google Cloud console, the gcloud CLI, or Terraform to create specific node pools that use nested virtualization.



### Enable by using ComputeClasses

You can use a ComputeClass to enable nested virtualization for specific groups of nodes in Autopilot or Standard mode. ComputeClasses are the only method by which you can enable nested virtualization for auto-created node pools and Autopilot nodes. To deploy an example ComputeClass that enables nested virtualization, follow these steps:

  1. Save the following ComputeClass manifest as a file that's named `nested-virt-class.yaml`:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: nested-virt-class
         spec:
           priorities:
           - machineFamily: c3
             spot: true
             enableNestedVirtualization: true
           - machineFamily: c4
             spot: false
             enableNestedVirtualization: true
           - machineFamily: c4d
             spot: true
             enableNestedVirtualization: true
           nodePoolConfig:
             imageType: "cos_containerd"
           nodePoolAutoCreation:
             enabled: true
           whenUnsatisfiable: DoNotScaleUp
         

This example ComputeClass has the following properties:

     * Prioritizes C3 instances on Spot VMs, falls back to on-demand C4 instances, and then falls back to C4D instances on Spot VMs.
     * Enables nested virtualization for all of the instances.
     * Stops GKE from scaling up the cluster default machine series if prioritized instances aren't available.
     * Uses the Container-Optimized OS node image for all of the nodes.
     * Enables node pool auto-creation, so that GKE can create new node pools to run Pods when needed.

Alternatively, you can enable nested virtualization for all priority rules in your ComputeClass by specifying the `enableNestedVirtualization: true` field in the [`spec.priorityDefaults` field](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#priorityDefaults).

  2. Create the ComputeClass:
         
         kubectl apply -f nested-virt-class.yaml
         

When you enable nested virtualization in a ComputeClass, GKE checks the specified machine series for compatibility with nested VMs. If a machine series in a priority rule that enables nested virtualization isn't compatible, then GKE warns you. However, this check might not find every incompatible configuration.

  3. To trigger node pool creation, create a Pod that selects the ComputeClass:

     1. Save the following Pod manifest as a file that's named `nested-virt-example-pod.yaml`:
            
            apiVersion: v1
            kind: Pod
            metadata:
              name: nested-virt-example-pod
            spec:
              nodeSelector:
                cloud.google.com/compute-class: nested-virt-class
              containers:
              - name: example-container
                image: registry.k8s.io/pause:3.9
            

     2. Create the Pod:
            
            kubectl apply -f nested-virt-example-pod.yaml
            




The nodes that GKE creates for this ComputeClass have nested virtualization enabled. You can run applications that create nested VMs on these nodes. Any Pods that use the ComputeClass can create nested VMs. For example, you could install Kata Containers on these nodes by specifying a [node selector](https://kata-containers.github.io/kata-containers/helm-configuration/#nodeselector) for the `cloud.google.com/compute-class="nested-virt-class"` label.

### Enable in Standard node pools

If you don't want to use ComputeClasses, you can manually enable nested virtualization for specific new node pools in Standard clusters during any of the following operations:

  * When you create a new Standard cluster, which enables nested virtualization for the default node pool. This enablement applies only to the default node pool. GKE doesn't automatically enable nested virtualization for additional node pools that you create later.
  * When you create a new node pool in an existing Standard cluster.



To enable nested virtualization in manually created node pools, select one of the following options:

### Console

  * Enable nested virtualization for the default node pool of a new cluster:

    1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

    2. Configure the basic settings for your cluster.
    3. In the navigation menu, in the **Node pools** section, expand the **default-pool** section and click **Nodes**.
    4. In the **Machine configuration** section, choose a [supported machine type (see the **Nested virtualization row**)](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison).
    5. After the **Reservations** section, select the **Enable nested virtualization** checkbox.
    6. To create the cluster, click **Create**.
  * Enable nested virtualization for a new node pool in an existing cluster:

    1. In the Google Cloud console, go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list)

    2. Click the name of the cluster in which you want to create the new node pool.

    3. Configure your node pool.

    4. Click the **Nodes** tab.

    5. In the heading of **Node pools** section, click _add_box_ **Create user-managed node pool**.

    6. In the navigation menu, select **Nodes**.

    7. In the **Machine configuration** section, choose a machine series that supports nested virtualization. For more information, filter the [machine series comparison table](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison) for the **Nested virtualization** property.

    8. Select the **Enable nested virtualization** checkbox. If this checkbox is disabled, verify that you selected a machine series that supports nested virtualization.

    9. Click **Create**.




### gcloud

  * Enable nested virtualization for the default node pool of a new cluster:
        
        gcloud container clusters create CLUSTER_NAME \
            --location=CONTROL_PLANE_LOCATION
            --enable-nested-virtualization \
            --node-labels=nested-virtualization=enabled \
            --machine-type=MACHINE_TYPE
        

Replace the following:

    * `CLUSTER_NAME`: a name for the cluster.
    * `CONTROL_PLANE_LOCATION`: the region or zone for the cluster's control plane.
    * `MACHINE_TYPE`: a machine type that supports nested virtualization, such as `n4-standard-8`. For more information, filter the [machine series comparison table](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison) for the **Nested virtualization** property.
  * Enable nested virtualization for a new node pool in an existing cluster:
        
        gcloud container node-pools create NODEPOOL_NAME \
            --enable-nested-virtualization \
            --node-labels=nested-virtualization=enabled \
            --cluster=CLUSTER_NAME \
            --location=CONTROL_PLANE_LOCATION \
            --machine-type=MACHINE_TYPE
        

Replace the following:

    * `NODEPOOL_NAME`: a name for the node pool.
    * `CLUSTER_NAME`: the name of your existing cluster.
    * `CONTROL_PLANE_LOCATION`: the location of the cluster's control plane.
    * `MACHINE_TYPE`: a machine type that supports nested virtualization, such as `n4-standard-8`. For more information, filter the [machine series comparison table](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison) for the **Nested virtualization** property.



After you create the cluster or node pool, you can [check whether nested virtualization is enabled](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/enabling#confirm_that_nested_virtualization_is_enabled_on_the_vm). The nodes in these node pools have the `nested-virtualization=enabled` Kubernetes node label, which you can use to schedule Pods that create nested VMs.

## Schedule a Pod to a node that supports nested virtualization

To schedule a Pod on a node with nested virtualization enabled, add the following node selector to the specification:
    
    
    nodeSelector:
      nested-virtualization: enabled
    

Additionally, for the Pod to connect with a nested VM, you must set the Pod as privileged by configuring `securityContext.privileged:true`.

## What's next

  * [About nested virtualization](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
