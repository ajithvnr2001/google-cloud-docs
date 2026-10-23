---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/boost-application-startup/
title: Accelerate application startup with CPU startup boost \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:25.322803+00:00
---

# Accelerate application startup with CPU startup boost  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/boost-application-startup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Accelerate application startup with CPU startup boost Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how you can use CPU startup boost with the [vertical Pod autoscaler (VPA)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling) in Google Kubernetes Engine (GKE) to temporarily increase the CPU resources allocated to a Pod during its initialization phase.

CPU startup boost accelerates application startup and improves cost efficiency by temporarily increasing CPU requests during initialization and resizing them back to baseline levels in-place. This document covers the startup boost requirements, configuration (Pod and container-level), verification, and best practices.

This document is for DevOps, Platform engineers and Application developers who want to optimize application startup performance in GKE.

### Benefits

Using CPU startup boost provides the following benefits:

  * **Faster startup** : Accelerate the initialization of resource-intensive applications, such as those written in Java, Node.js, or Python.
  * **Cost efficiency** : Avoid over-provisioning CPU for steady-state operation while still meeting startup demands. Steady-state operation is the period after an application has finished its initialization and its resource usage has stabilized.
  * **No disruption** : Scale resources back to baseline levels using Kubernetes in-place Pod resize (IPPR) without restarting your containers.
  * **Reduced manual effort** : Minimize resource waste and the manual effort required to rightsize your workloads.



### Requirements

To use CPU startup boost, you must meet the following requirements:

  * **GKE version** : use `1.36.0-gke.4447000` and later for both Standard and Autopilot clusters.
  * **VPA enabled** : enable vertical Pod autoscaling on Standard clusters. GKE enables VPA by default on Autopilot clusters. You can use VPA exclusively for CPU startup boost by choosing a specific [update mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler#vpa-update-modes). To enable and configure VPA, see [Set Pod resource requests automatically](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling#update-requests-automatically).
  * **Workload type** : use a controller, such as a Deployment or a StatefulSet, to manage your workload.
  * **Node capacity** : ensure that Standard clusters have sufficient capacity for the boosted Pod. If there is insufficient capacity, GKE caps the boosted Pod request to fit the node.



## How CPU startup boost works

For more information about the boost lifecycle and how CPU startup boost calculates resource increases, see [How CPU startup boost works](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler#cpu-startup-boost).

## Before you begin

Before you start, make sure that you have selected the Google Cloud project containing the cluster you want to boost and have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Configure the gcloud CLI to use your selected project:
        
        gcloud config set project PROJECT_ID
        

Replace `PROJECT_ID` with the ID of your project.

  * Ensure that you have an existing GKE cluster. If you don't have one, see [Create a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-container-cluster).




### Required roles

To get the permissions that you need to enable and use CPU startup boost, ask your administrator to grant you the following IAM roles on your project: 

  * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
  * [Kubernetes Engine Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.developer) (`roles/container.developer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable CPU startup boost

To enable CPU startup boost, add a `startupBoost` configuration block to your VerticalPodAutoscaler (VPA) manifest. You can configure the boost to apply to all containers in a Pod or target individual containers with specific resource increases.

### Configure a Pod-level boost

A Pod-level boost applies the same CPU resource increase to every container in the workload. You can configure the CPU startup boost with or without VPA's continuous resource management.

To configure a Pod-level boost, use one of the following options.

#### Option A: Startup boost enabled and VPA update mode disabled

Use this option to leverage VPA exclusively for its CPU startup boost capabilities without actuating regular VPA recommendations. The following example applies a CPU multiplication factor of `2` and maintains it for 10 seconds after the Pod reaches the `Ready` status:
    
    
    apiVersion: "autoscaling.k8s.io/v1"
    kind: VerticalPodAutoscaler
    metadata:
      name: example-vpa
    spec:
      targetRef:
        apiVersion: "apps/v1"
        kind: Deployment
        name: example
      updatePolicy:
        updateMode: "Off"
      **startupBoost :**
        cpu:
          type: "Factor"
          factor: 2
          **durationSeconds : 10**
    

#### Option B: Both startup boost and VPA update mode enabled

If you want GKE to manage the startup boost and then continue to automatically adjust your Pod's resource requests based on ongoing usage, use this option. The following example applies the startup boost and sets `updateMode` field to `InPlaceOrRecreate`:
    
    
    apiVersion: "autoscaling.k8s.io/v1"
    kind: VerticalPodAutoscaler
    metadata:
      name: example-vpa
    spec:
      targetRef:
        apiVersion: "apps/v1"
        kind: Deployment
        name: example
      updatePolicy:
        updateMode: "InPlaceOrRecreate"
      **startupBoost :**
        cpu:
          type: "Factor"
          factor: 2
          **durationSeconds : 10**
    

### Configure a container-level boost

If your workload includes sidecars or other containers that don't require extra resources, you can target specific containers for a startup boost within the `resourcePolicy` section. The `containerName` value must match the `name` field of a container in your Deployment specification.

To configure a container-level boost, use one of the following options.

#### Option A: Boost a specific container (VPA actuation disabled)

Use this option to apply a boost to a single container while keeping the rest of the Pod's resource requests untouched. The following example manifest adds two vCPUs to the baseline request for a container named `boosted-container-name`:
    
    
    apiVersion: "autoscaling.k8s.io/v1"
    kind: VerticalPodAutoscaler
    metadata:
      name: example-vpa
    spec:
      targetRef:
        apiVersion: "apps/v1"
        kind: Deployment
        name: example
      updatePolicy:
        updateMode: "Off"
      resourcePolicy:
        containerPolicies:
        - containerName: "**boosted-container-name** "
          mode: "Off"
          **startupBoost :**
            cpu:
              type: "Quantity"
              **quantity : "2"**
    

#### Option B: Opt-out a specific container from a Pod-level boost

If you have a Pod-level boost configured but want to exclude a specific container, use this option. The following example manifest applies a CPU multiplication factor of `2` to the whole Pod, but disables the boost for a container named `disable-cpu-boost-for-this-container` by setting its factor to 1:
    
    
    apiVersion: "autoscaling.k8s.io/v1"
    kind: VerticalPodAutoscaler
    metadata:
      name: example-vpa
    spec:
      targetRef:
        apiVersion: "apps/v1"
        kind: Deployment
        name: example
      updatePolicy:
        updateMode: "InPlaceOrRecreate"
      **startupBoost :**
        cpu:
          type: "Factor"
          factor: 2
      resourcePolicy:
        containerPolicies:
        - containerName: "**disable-cpu-boost-for-this-container** "
          **startupBoost :**
            cpu:
              type: "Factor"
              **factor : 1**
    

## Verify CPU startup boost

To verify that your Pods receive the boost, check the VPA configuration, Pod resource requests, Pod annotations, and VPA events.

### Verify the VPA configuration

To check the details of your VerticalPodAutoscaler object, run the following command:
    
    
    kubectl describe vpa VPA_NAME
    

Replace `VPA_NAME` with the name of your VPA object.

### Check the boosted CPU request on the Pod

To verify the current resource requests for your Pod, run the following command:
    
    
    kubectl describe pod POD_NAME
    

Replace `POD_NAME` with the name of your Pod.

### Verify the CPU boost by using Pod annotations

The VPA admission webhook injects a container-scoped annotation to track the original resources that each container should revert to when the boost expires. To check these annotations, run the following command:
    
    
    kubectl get pod POD_NAME --output yaml
    

Under `metadata.annotations` section, look for an annotation formatted as `vpaCpuStartupBoost/CONTAINER_NAME`. For example:
    
    
    metadata:
      annotations:
        **vpaCpuStartupBoost/slow-starter : '{"requests":{"cpu":"50m","memory":"64Mi"},"limits":{"cpu":"200m","memory":"128Mi"}}'**
    

The command output indicates one of the following verification results:

  * **Successful boost** : the `vpaCpuStartupBoost/CONTAINER_NAME` annotation is present on the Pod.
  * **Unsuccessful boost** : the annotation is missing entirely. This means the admission controller ignored the boost, possibly due to [node capacity limits](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-up) or [Autopilot resource limitations](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/autopilot-clusters).



### Check for downscaling events

To verify that GKE successfully decreased the CPU resource allocation back to the baseline, check the cluster events by running the following command:
    
    
    kubectl get events --field-selector reason=InPlaceResizedByVPA
    

The command output indicates one of the following verification results:

  * **Successful unboost** : you see an `InPlaceResizedByVPA` event with a message indicating the Pod was resized in-place by the VPA Updater. This confirms that the CPU request has returned to its baseline value without restarting the container.
  * **Unsuccessful unboost** : the `vpaCpuStartupBoost/CONTAINER_NAME` annotation remains on the Pod long after the boost should have expired, and there is no `InPlaceResizedByVPA` event.



## Best practices and limitations

Review the following when you use CPU startup boost.

### Interactions with horizontal Pod autoscaling

If you use the [horizontal Pod autoscaler (HPA)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling) with CPU startup boost, follow these guidelines:

  * **Define health probes** : you must define a `readinessProbe` for your workloads.
  * **Configure duration delay** : you must set the `durationSeconds` parameter to `0`. This configuration prevents HPA from scaling out your application prematurely due to high CPU utilization during startup.



### Cluster autoscaler and eviction loops

If you use the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler) on GKE Standard clusters, consider these node behaviors:

  * **Potential eviction loops** : a temporary CPU boost might trigger a node scale-up. After the Pod is ready and downscales, underutilization might trigger node scale-down and evict the Pod, leading to an endless loop.
  * **Mitigation** : we strongly recommend using GKE Autopilot to mitigate node defragmentation and eviction loop issues.



### Container restarts

Understand how container restarts affect CPU startup boost by reviewing the following behaviors:

  * **Only during Pod creation** : CPU startup boost applies only during the initial Pod creation stage.
  * **No boost on restart** : if a container restarts—for example, due to an OOMKill event—but the Pod remains active, GKE doesn't apply the boost again. This behavior occurs because the Pod admission webhook triggers only during the initial Pod creation process.



## Clean up

Because you configure CPU startup boost on existing workloads, keep the following in mind to avoid workload disruption:

  * You don't need to delete any Kubernetes resources.
  * If your VerticalPodAutoscaler object or workload controllers (such as Deployments or StatefulSets) are still needed for steady-state operations, don't delete them.
  * If you don't need CPU startup boost, you can disable only the boost using one of the following methods based on your scope:

    * **Disable boost for the entire workload** : delete the `startupBoost` block from your VerticalPodAutoscaler object specification and apply the updated manifest to your cluster.
    * **Disable boost for a specific container** : to exclude a specific container from a Pod-level boost, add a container policy under `containerPolicies` section and set the CPU multiplier factor to 1.
          
          **startupBoost :**
              cpu:
                type: "Factor"
                **factor : 1**
          

For more information, see Configure a container-level boost.




## What's next

  * [Scale container resource requests and limits](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling)
  * [Configuring horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling)
  * [Right-size workloads at scale](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/right-size-workloads-at-scale)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
