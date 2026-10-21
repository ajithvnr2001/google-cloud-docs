---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-arm-workloads/
title: Deploy Autopilot workloads on Arm architecture \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:03:46.329644+00:00
---

# Deploy Autopilot workloads on Arm architecture  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-arm-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Deploy Autopilot workloads on Arm architecture Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This page shows you how to configure your Google Kubernetes Engine (GKE) Autopilot deployments to request nodes that are backed by Arm architecture.

## About Arm architecture in Autopilot

Autopilot clusters offer [_compute classes_](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes) for workloads that have specific hardware requirements. Some of these compute classes support multiple CPU architectures, such as `amd64` and `arm64`.

## Use cases for Arm nodes

Nodes with Arm architecture offer more cost-efficient performance than similar x86 nodes. You should select Arm for your Autopilot workloads in situations such as the following:

  * Your environment relies on Arm architecture for building and testing.
  * You're developing applications for Android devices that run on Arm CPUs.
  * You use multi-arch images and want to optimize costs while running your workloads.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Review the [requirements and limitations for Arm nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke#arm-requirements-limitations).



### Requirements

  * To use the `autopilot-arm` ComputeClass, ensure that your cluster is running GKE version 1.35.3-gke.1389000 or later.
  * To use features like smart defaulting (by specifying only the `kubernetes.io/arch: arm64` label), the `autopilot-arm-spot` ComputeClass, or the `autopilot-arm` ComputeClass in GKE Standard clusters that use Autopilot ComputeClasses, your cluster must run version 1.36.0-gke.3302001 or later.
  * Ensure that you have quota for the [C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series), [N4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series), or [Tau T2A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines) Compute Engine machine types.
  * Ensure that you have a Pod with a container image that's built for Arm architecture.



## How to request Arm nodes in Autopilot

To tell Autopilot to run your Pods on Arm nodes, specify one of the following selectors (depending on your GKE type and version) using a [nodeSelector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector) or [node affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity) rule:

  * **In Autopilot clusters (smart defaulting):** Specify only the architecture type:

    * `kubernetes.io/arch: arm64`

If your workload runs on an Autopilot cluster, this selects the general-purpose Arm platform.

  * **In Autopilot clusters or Standard clusters that use Autopilot ComputeClasses (ComputeClass only):** Specify the ComputeClass:

    * `cloud.google.com/compute-class: autopilot-arm` (or `autopilot-arm-spot`)

Selecting this class schedules your workload on the container-optimized Arm platform (or its Spot VMs variant) and automatically adds the required `kubernetes.io/arch: arm64` selector to the Pod during admission.

  * **Explicit selection (older GKE versions):** In Autopilot clusters running version 1.35.3-gke.1389000 or later but earlier than 1.36.0-gke.3302001, specify both of the following selector to select the general-purpose Arm platform. This combination is also supported in newer GKE versions for backward compatibility:

    * `cloud.google.com/compute-class: autopilot-arm`
    * `kubernetes.io/arch: arm64`
  * **For workloads with specific hardware requirements:** Specify one of the following:

    * `kubernetes.io/arch: arm64` in a Standard cluster. GKE defaults to placing the Pods on `C4A` machine types.
    * `cloud.google.com/machine-family: ARM_MACHINE_SERIES`. Replace `ARM_MACHINE_SERIES` with an Arm machine series like `C4A`, `N4A`, or `T2A`. GKE places Pods on the specified series.



By default, using any of the labels except `Performance` lets GKE place other Pods on the same node if there's availability capacity on that node. To request a dedicated node for each Pod, add the `cloud.google.com/compute-class: Performance` label to your manifest alongside the architecture or machine-family labels. For details, see [Optimize Autopilot Pod performance by choosing a machine series](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/performance-pods).

Or, you can use the `Scale-Out` label with the `arm64` label to request `T2A`. You can also request Arm architecture for [Spot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-spot-pods).

When you deploy your workload, Autopilot does the following:

  1. Automatically provisions Arm nodes to run your Pods.
  2. Automatically taints the new nodes to prevent non-Arm Pods from being scheduled on those nodes.
  3. Automatically adds a toleration to your Arm Pods to allow scheduling on the new nodes.

**Note:** You can configure the default Arm architecture taint for [ Standard node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment#configure-default-taint), and [custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#architecture-taint). Updating the taints by using these methods doesn't affect the nodes that GKE creates for the built-in Autopilot Arm ComputeClasses. You can't modify the Arm architecture taint behavior for those built-in ComputeClasses.

## Example request for Arm architecture

The following example specifications show you how to use a node selector or a node affinity rule to request Arm architecture in Autopilot.

### nodeSelector

The following example manifest requests an Autopilot container-optimized Arm node using smart defaulting:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: nginx-arm
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: nginx-arm
      template:
        metadata:
          labels:
            app: nginx-arm
        spec:
          **nodeSelector :
            kubernetes.io/arch: arm64**
          containers:
          - name: nginx-arm
            image: nginx
            resources:
              requests:
                cpu: 2000m
                memory: 2Gi
    

Alternatively, you can request the container-optimized Arm platform by explicitly specifying the `autopilot-arm` (or `autopilot-arm-spot` for Spot VMs) ComputeClass:
    
    
    ...
        spec:
          **nodeSelector :
            cloud.google.com/compute-class: autopilot-arm**
    ...
    

To request specific hardware instead of Autopilot container-optimized nodes, replace the ComputeClasses or add `cloud.google.com/machine-family: C4A` to your selector.

### nodeAffinity

You can use [node affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity) to request Arm nodes.

The following example manifest requests an Autopilot container-optimized Arm node using smart defaulting:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: nginx-arm
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: nginx-arm
      template:
        metadata:
          labels:
            app: nginx-arm
        spec:
          terminationGracePeriodSeconds: 25
          containers:
          - name: nginx-arm
            image: nginx
            resources:
              requests:
                cpu: 2000m
                memory: 2Gi
                ephemeral-storage: 1Gi
          **affinity :
            nodeAffinity:
              requiredDuringSchedulingIgnoredDuringExecution:
                nodeSelectorTerms:
                - matchExpressions:
                  - key: kubernetes.io/arch
                    operator: In
                    values:
                    - arm64**
    

To request specific hardware instead of Autopilot container-optimized nodes, replace `kubernetes.io/arch` with specific machine-family affinity rules or request classes like `Performance` or `Scale-Out`.

## Recommendations

  * [Build and use multi-arch images](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/build-multi-arch-for-arm) as part of your pipeline. Multi-arch images ensure that your Pods run even if they're placed on x86 nodes.
  * Explicitly request architecture and compute classes in your workload manifests. If you don't, Autopilot uses the default architecture of the selected compute class, which might not be Arm.



## Availability

You can deploy Autopilot workloads on Arm architecture in the following regions: `us-east1`, `us-west1`, `europe-west1`, `europe-west2`, `europe-west4`, `asia-southeast1`, and `us-central1`.

## Troubleshooting

For common errors and troubleshooting information, refer to [Troubleshooting Arm workloads](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshooting-arm-workloads).

## What's next

  * [Learn more about Autopilot cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-architecture).
  * [Learn about the lifecycle of Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/).
  * [Learn about the available Autopilot compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes).
  * [Read about the default, minimum, and maximum resource requests for each platform](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
