---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods/
title: Isolate workloads by using GKE Sandbox \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:11.003208+00:00
---

# Isolate workloads by using GKE Sandbox  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Isolate workloads by using GKE Sandbox Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can protect the host kernel of your Google Kubernetes Engine (GKE) nodes from containers that run untrusted or unknown code by using GKE Sandbox. This document shows Security specialists how to enable GKE Sandbox, run Pods in sandboxes, and verify the isolation.

You should already be familiar with [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods).

## Available sandbox types

GKE Sandbox supports the following sandbox types, each of which uses a specific technology to separate application code from the host kernel:

  * `gvisor`: a userspace re-implementation of the Linux kernel API that doesn't need elevated privileges. The userspace kernel intercepts and services the majority of system calls on behalf of the host kernel, which limits direct access to the host kernel.
  * `microvm`: lightweight VMs that are nested on the host VM by using [nested virtualization](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nested-virtualization). Each Pod on the node runs in its own nested VM with its own guest kernel. Because code runs in a dedicated VM, this sandbox type provides stronger isolation than gVisor sandboxes.



For more information about how each sandbox type works and when to use a specific type, see [About GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods).

## Limitations

GKE Sandbox and specific sandbox technologies have various limitations, such as GPU and TPU support or support for specific Linux and Kubernetes features. For more information, see [Limitations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#limitations).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * To follow the steps in the Choose a sandbox type for auto-created nodes section, use an existing Autopilot or Standard cluster. To use microVM sandboxes, your nodes must run GKE version 1.37.0-gke.4713000 or later.



## Choose a sandbox type for auto-created nodes

You can use [ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-compute-classes) with Autopilot mode or node pool auto-creation to enable GKE Sandbox on nodes that GKE creates. In Autopilot clusters, gVisor is supported by default, so you can optionally omit the sandbox configuration from your ComputeClass.

To configure GKE Sandbox for auto-created nodes, follow these steps:

  1. Connect to an existing Autopilot or Standard cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `CONTROL_PLANE_LOCATION`: the region or zone of your cluster's control plane.
  2. Save one of the following ComputeClass manifests, depending on the sandbox technology that you want:

     * **gVisor** :
           
           apiVersion: cloud.google.com/v1
           kind: ComputeClass
           metadata:
             name: sandbox-gvisor-class
           spec:
             priorities:
             - machineFamily: n4
             - machineFamily: c4
             **nodePoolConfig :
               sandbox:
                 type: gvisor**
             nodePoolAutoCreation:
               enabled: true
             whenUnsatisfiable: DoNotScaleUp
           

     * **microVM** :
           
           apiVersion: cloud.google.com/v1
           kind: ComputeClass
           metadata:
             name: sandbox-microvm-class
           spec:
             priorities:
             - machineFamily: n4
             - machineFamily: c4
             **nodePoolConfig :
               sandbox:
                 type: microvm
             priorityDefaults:
               enableNestedVirtualization: true**
             nodePoolAutoCreation:
               enabled: true
             whenUnsatisfiable: DoNotScaleUp
           

The ComputeClass for microVM sandboxes enables nested virtualization by using the `enableNestedVirtualization` field. This field is required for microVM sandboxes. To use this field, your cluster must run version 1.37.0-gke.4713000 or later.

These example manifests use the `nodePoolAutoCreation` field to enable node pool auto-creation. You can also specify the sandbox configuration in a ComputeClass that uses the `autopilot` field to run Pods in Autopilot mode. If you use Autopilot clusters, then GKE ignores both the `nodePoolAutoCreation` and `autopilot` fields.

  3. Create the ComputeClass:
         
         kubectl apply -f PATH_TO_COMPUTE_CLASS_MANIFEST
         

Replace `PATH_TO_COMPUTE_CLASS_MANIFEST` with the path to the ComputeClass manifest.




To select this ComputeClass and request a sandbox environment, see Request a sandbox environment for a Pod.

## Choose a sandbox type when you create node pools

You can manually enable GKE Sandbox when you create a new node pool in a Standard cluster. The following limitations apply when you manually enable GKE Sandbox:

  * To enable GKE Sandbox during Standard cluster creation, you must configure at least one extra node pool. The extra node pool is required because GKE needs at least one node pool in the cluster that doesn't use GKE Sandbox to run GKE-managed system workloads. If you use the gcloud CLI to create your cluster, you must create the cluster and then create a node pool that uses GKE Sandbox.
  * To select the microVM sandbox type, you must use the gcloud CLI or the GKE API. The Google Cloud console doesn't support selecting the microVM sandbox type.



### Enable the gVisor sandbox type

To manually enable gVisor sandboxes when you create a new node pool, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster that you want to modify. The **Cluster details** page opens.

  3. Click the **Nodes** tab.

  4. In the **Node pools** section, click add_box **Add user-managed node pool**. The **Add a node pool** page opens.

  5. In the navigation menu, click **Nodes** and configure the following settings:

     1. In the **Image type** drop-down list, select **Container-Optimized OS with Containerd (cos_containerd)**.
     2. In the **Machine configuration** section, select a machine series and a machine type for the nodes.
     3. Optional: select a [supported GPU type](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#gpu_model_support) or a [supported TPU type](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#tpus).
  6. In the navigation menu, click **Security**. The **Node security** page opens.

  7. Select the **Enable sandbox with gVisor** checkbox.

  8. To create the node pool, click **Create**.




### gcloud

To create a node pool that uses gVisor for sandboxes, run the following command:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        **--sandbox =type=gvisor**
    

Replace the following:

  * `NODE_POOL_NAME`: a name for the node pool.
  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the region or zone of your cluster's control plane.



You can also enable gVisor sandboxes when you create node pools that use a [supported GPU type](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#gpu_model_support) or a [supported TPU type](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#tpus). For more information, see the following documents:

  * [Deploy TPU workloads in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#create-node-pool)
  * [Deploy GPU workloads in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#create-gpu-pool-auto-drivers)



### Enable the microVM sandbox type

You can enable the microVM sandbox type when you create a node pool by using the gcloud CLI or the GKE API. The Google Cloud console doesn't support enabling the microVM sandbox type. To create a node pool that uses microVM sandboxes, run the following command:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        **--sandbox =type=microvm \
        --enable-nested-virtualization \
        --machine-type=MACHINE_TYPE**
    

Replace the following:

  * `NODE_POOL_NAME`: a name for the node pool.
  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the region or zone of your cluster's control plane.
  * `MACHINE_TYPE`: the machine type for the nodes. This value must be a machine type that supports nested virtualization. For more information, see the **Nested virtualization** row in the [machine series comparison table](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison).



### Enable monitoring and logging

To collect and view logs and metrics from your sandboxes, ensure that your cluster enables the following observability services:

  * [Cloud Logging](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs#logging-agent)
  * [Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#enable-system-metrics)
  * [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#enable-mgdcoll-gke)



These services are enabled by default in all new GKE clusters.

## Request a sandbox environment for a Pod

To run a specific Pod in a sandbox, you can specify the `gvisor` or `microvm` RuntimeClass in the Pod specification. GKE schedules the Pod on nodes that use the specified sandbox type. To select a sandbox type in a Pod specification, follow these steps:

  1. Save one of the following example Deployment manifests, depending on whether you enable GKE Sandbox by using ComputeClasses or manually created node pools:

     * **ComputeClasses** :
           
           apiVersion: apps/v1
           kind: Deployment
           metadata:
             name: sandbox-pod
             labels:
               environment: sandbox
           spec:
             replicas: 2
             selector:
               matchLabels:
                 environment: sandbox
             template:
               metadata:
                 labels:
                   environment: sandbox
               spec:
                 **nodeSelector :
                   cloud.google.com/compute-class: COMPUTECLASS_NAME
                 runtimeClassName: SANDBOX_TYPE
                 **
                 containers:
                 - name: nginx
                   image: nginx
           

Replace the following:

       * `COMPUTECLASS_NAME`: the name of the ComputeClass that you created, as described in Choose a sandbox type for auto-created nodes.

       * `SANDBOX_TYPE`: the sandbox type to use for the Pods. The following values are supported:

         * `gvisor`
         * `microvm`

The sandbox type that you specify must match the sandbox type that the selected ComputeClass enables.

     * **Manually created node pools** :
           
           apiVersion: apps/v1
           kind: Deployment
           metadata:
             name: httpd
             labels:
               app: httpd
           spec:
             replicas: 1
             selector:
               matchLabels:
                 app: httpd
             template:
               metadata:
                 labels:
                   app: httpd
               spec:
                 **runtimeClassName : SANDBOX_TYPE**
                 containers:
                 - name: httpd
                   image: httpd
           

Replace `SANDBOX_TYPE` with the sandbox type. The following values are supported:

       * `gvisor`
       * `microvm`

The sandbox type that you specify must match the sandbox type of an existing node pool in the cluster.

  2. Create the Deployment:
         
         kubectl apply -f PATH_TO_DEPLOYMENT_MANIFEST
         

Replace `PATH_TO_DEPLOYMENT_MANIFEST` with the path to the Deployment manifest.

  3. Verify that the Pods were created:
         
         kubectl get pods
         

The output is similar to the following:
         
         NAME                    READY   STATUS    RESTARTS   AGE
         httpd-db5899bc9-dk7lk   1/1     Running   0          24s
         




You can also request sandboxes when you run Pods on a [supported GPU type](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#gpu_model_support) or a [supported TPU type](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#tpus) by using the `runtimeClassName` field. For more information, see the following documents:

  * [Deploy GPU workloads in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#create-gpu-pool-auto-drivers)
  * [Deploy TPU workloads in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#create-node-pool)
  * [Deploy GPU workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus)
  * [Deploy TPU workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus-autopilot)



### Run a regular Pod along with sandboxed Pods

The steps in this section apply to Standard mode workloads. You don't need to run regular Pods alongside sandbox Pods in Autopilot mode, because the [Autopilot pricing model](https://cloud.google.com/kubernetes-engine/pricing#autopilot_mode) eliminates the need to manually optimize the number of Pods scheduled on nodes.

After enabling GKE Sandbox on a node pool, you can run trusted applications on those nodes without using a sandbox by using node taints and tolerations. These Pods are referred to as "regular Pods" to distinguish them from sandboxed Pods.

Regular Pods, just like sandboxed Pods, are prevented from accessing other Google Cloud services or cluster metadata. This prevention is part of the node's configuration. If your regular Pods or sandboxed Pods require access to Google Cloud services, use [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).

**Warning:** Running untrusted code on the same nodes as critical system services comes with potential risk, even if the untrusted code is running in a sandbox. Consider these risks when designing your applications.

GKE Sandbox adds the following label and taint to nodes that can run sandboxed Pods:

  * The `sandbox.gke.io/runtime: SANDBOX_TYPE` node label.
  * The `sandbox.gke.io/runtime=SANDBOX_TYPE:NoSchedule` node taint. Only Pods that have a matching toleration can be scheduled on the node.



If you use the `RuntimeClass` field to run a Pod in a sandbox, then GKE automatically applies a node affinity and a toleration to the Pod. To run a regular Pod on a node that uses GKE Sandbox, you must manually apply the following selectors to the Pod specification:

  * To let your Pod run on nodes that use GKE Sandbox when needed, add only the toleration for the node taint.
  * To run your Pod only on nodes that use GKE Sandbox, add a node selector and the toleration for the node taint.



The following steps show you how to run a regular Pod on a node that uses GKE Sandbox:

  1. Save the following Deployment manifest as `httpd-regular.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: httpd-regular
           labels:
             app: httpd-regular
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: httpd-regular
           template:
             metadata:
               labels:
                 app: httpd-regular
             spec:
               containers:
               - name: httpd-regular
                 image: httpd
               **affinity :
                 nodeAffinity:
                   requiredDuringSchedulingIgnoredDuringExecution:
                     nodeSelectorTerms:
                     - matchExpressions:
                       - key: sandbox.gke.io/runtime
                         operator: In
                         values:
                         - SANDBOX_TYPE
               tolerations:
                 - effect: NoSchedule
                   key: sandbox.gke.io/runtime
                   operator: Equal
                   value: SANDBOX_TYPE**
         

Replace `SANDBOX_TYPE` with the sandbox type, such as `gvisor` or `microvm`.

  2. Create the Deployment:
         
         kubectl apply -f httpd-regular.yaml
         

If the Pod is unschedulable, verify that the node affinity and the toleration are set correctly in the Pod manifest.

  3. Verify that the Pod isn't in a sandbox:
         
         kubectl get pods -o jsonpath=$'{range .items[*]}{.metadata.name}: {.spec.runtimeClassName}\n{end}'
         

The output is similar to the following:
         
         httpd-db5899bc9-dk7lk: SANDBOX_TYPE
         httpd-regular-5bf87996c6-cfmmd:
         

The `httpd-regular` Pod has no RuntimeClass value, which means that the Pod isn't in a sandbox.

  4. Verify that the regular Pod is running on a node that uses GKE Sandbox:
         
         kubectl get pod -o jsonpath=$'{range .items[*]}{.metadata.name}: {.spec.nodeName}\n{end}'
         

The output is similar to the following:
         
         httpd-db5899bc9-dk7lk: gke-cluster-2-pool-1-75c8fc63-h373
         httpd-regular-5bf87996c6-cfmmd: gke-cluster-2-pool-1-75c8fc63-h373
         

Both the sandboxed Pod and the regular Pod are on the same node, which indicates that the regular Pod is running on a node that uses GKE Sandbox.




## Verify the sandbox configuration

The following sections show you how to verify that a Pod is running in a sandbox and that the sandboxed Pod is isolated from the host kernel. These sections assume that you created the example Deployment in Request a sandbox environment for a Pod.

### Verify that a Pod is running in a sandbox

To check whether your Pods use a sandbox, get the RuntimeClass of the Pods. This method is more trustworthy than running a command inside the Pod, because you won't see data from inside the sandbox itself. Anything reported from within the sandbox is untrustworthy, because it could be defective or malicious.

  * Get the RuntimeClass of each running Pod:
        
        kubectl get pods -l=app=httpd -o jsonpath=$'{range .items[*]}{.metadata.name}: {.spec.runtimeClassName}\n{end}'
        

The output is similar to the following:
        
        httpd-db5899bc9-dk7lk: gvisor
        httpd-db5899bc9-ab3cd: gvisor
        

If the output shows `gvisor` or `microvm`, then the Pod is running in a sandbox.




### Verify the isolation of sandboxed Pods from the host

You can verify whether a sandboxed Pod is isolated from the host node by checking the available virtual devices and the version of the kernel that the Pod can access.

  1. For gVisor and microVM sandboxes, check whether the version of the kernel that the Pod can access is different from the kernel version of the host node:

     1. Get the version of the kernel that the Pod can access:
            
            kubectl exec POD_NAME -- uname -r
            

Replace `POD_NAME` with the name of the Pod.

The output is similar to the following:
            
            4.19.0-gvisor
            

     2. Get the version of the kernel on the host node:
            
            kubectl get node NODE_NAME \
                -o jsonpath='{.status.nodeInfo.kernelVersion}'
            

Replace `NODE_NAME` with the name of the node that runs the Pod.

The output is similar to the following:
            
            6.12.94+
            

The kernel version of the host node is different from the kernel version that the sandboxed Pod can access, because the Pod sees only the userspace kernel for gVisor or the guest kernel for microVMs.

  2. For microVM sandboxes, you can also check whether the devices that the Pod can access are virtualized by Cloud Hypervisor:
         
         kubectl exec POD_NAME -- cat /sys/class/dmi/id/product_name
         

If the output is `cloud-hypervisor`, then the Pod is in a microVM sandbox.




## Disable GKE Sandbox

You can't disable GKE Sandbox in GKE Autopilot clusters or in GKE Standard node pools. If you want to stop using GKE Sandbox, [delete the node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#deleting_a_node_pool).

## What's next

  * Learn more about [managing node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools).
  * Read the [security overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
