---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler/
title: Vertical Pod autoscaling \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:09.493130+00:00
---

# Vertical Pod autoscaling  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Vertical Pod autoscaling Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how you can analyze and optimize your resource allocation to improve your workload efficiency in Google Kubernetes Engine (GKE) by using vertical Pod autoscaling. By analyzing your workload's resource usage over time, you can get optimization recommendations and automatically adjust CPU and memory requests, and limits for containers within the Pods.

In this page, you learn how vertical Pod autoscaling works, its benefits and limitations, best practices for using it, and access the API references for the VerticalPodAutoscaler custom resource and related types.

This page is for Operators and Developers who provision and configure cloud resources, deploy workloads, and manage application scaling. To learn more about common roles, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you are familiar with [resource requests and limits in Kubernetes](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).

For rapid scaling needs in response to sudden resource usage, use the [Horizontal Pod Autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler).

To learn best practices for autoscaling, see [Best practices for running cost-optimized Kubernetes applications on GKE](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke#fine-tune_gke_autoscaling).

## Why use vertical Pod autoscaling

Vertical Pod autoscaling provides the following benefits:

  * Setting the right resource requests and limits for your workloads improves stability and cost efficiency. If your Pod resource sizes are smaller than your workloads require, your application can either be throttled or it can fail due to out-of-memory errors. If your resource sizes are too large, you have waste and, therefore, larger bills.
  * Cluster nodes are used efficiently because Pods use exactly what they need.
  * Pods are scheduled onto nodes that have the appropriate resources available.
  * You don't have to run time-consuming benchmarking tasks to determine the correct values for CPU and memory requests.
  * You can reduce maintenance time because the autoscaler can adjust CPU and memory requests over time without any action on your part.
  * Vertical Pod autoscaling works best with long-running homogenous workloads.



GKE vertical Pod autoscaling provides the following benefits over the [open source Kubernetes autoscaler](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler):

  * Takes maximum node size and resource quotas into account when determining the recommendation target.
  * Notifies the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) to adjust cluster capacity.
  * Uses historical data, including metrics collected before you enabled the VerticalPodAutoscaler.
  * Runs VerticalPodAutoscaler Pods as [control plane](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#control_plane) processes, instead of deployments on your [worker nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes).



## How vertical Pod autoscaling works

_Vertical Pod autoscaling_ lets you analyze and set CPU and memory resources required by Pods. Instead of having to set up-to-date [CPU requests and limits](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/) and [memory requests and limits](https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/) for the containers in your Pods, you can configure vertical Pod autoscaling to provide recommended values for CPU and memory requests and limits that you can use to manually update your Pods, or you can configure vertical Pod autoscaling to automatically update the values.

Vertical Pod autoscaling is enabled by default in Autopilot clusters.

### Relationship to Kubernetes open-source VerticalPodAutoscaler

GKE vertical Pod autoscaling is based on the open source Kubernetes [VerticalPodAutoscaler](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler) API, but is a separate implementation that is unique to GKE. The GKE implementation is designed for scale with its own recommender, but maintains the same VerticalPodAutoscaler API kinds and fields that are defined in the open-source version.

For more information, see the [Kubernetes documentation for vertical Pod autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/).

## Vertical Pod autoscaling modes

You can configure how vertical Pod autoscaling applies resource changes by applying different update modes.

### `Auto` (`Recreate`) mode

**Note:** The `Recreate` and `Auto` modes use the same behavior. The `Auto` update mode is the default mode if the `updateMode` field is not specified in the `VerticalPodAutoscaler` object.

In `Recreate` mode, vertical Pod autoscaling evicts a Pod if it needs to change the Pod's resource requests. Eviction is necessary because, due to Kubernetes limitations in versions earlier than 1.33, the only way to modify the resource requests of a running Pod is to re-create it.

To limit the amount of Pod re-creations, use a [Pod disruption budget](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) . To ensure that your cluster can handle the new sizes of your workloads, use [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) and [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning).

Vertical Pod autoscaling notifies the cluster autoscaler ahead of the update, and provides the resources needed for the resized workload before re-creating the workload, to minimize the disruption time.

### `Initial` mode

With `Initial` enabled, vertical Pod autoscaling only assigns resource requests on Pod creation and never changes them later.

### `InPlaceOrRecreate` mode

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The `InPlaceOrRecreate` mode aims to reduce service disruption by attempting to update Pod resources without re-creating the Pod. 

To use `InPlaceOrRecreate` mode, set the `spec.updatePolicy.updateMode` field to `"InPlaceOrRecreate"` in your `VerticalPodAutoscaler` object. This mode relies on the `resizePolicy` field defined in your workload manifest to determine if a resource change requires a restart. If the `resizePolicy` field is not defined, it defaults to `NotRequired` for CPU and memory, meaning in-place updates are attempted.

If a container terminates due to an OOM (Out of Memory) event, vertical Pod autoscaling in `InPlaceOrRecreate` mode acts similarly to `Auto` mode: it learns from the failure. Upon the subsequent Pod re-creation triggered by the crash, vertical Pod autoscaling applies a recommendation that includes a safety buffer (typically 20% additional memory or 100 MB, whichever is larger) to prevent immediate repetition of the OOM error.

The `InPlaceOrRecreate` mode is available with Kubernetes version 1.34.0-gke.2201000 and later.

#### Fallback scenarios for `InPlaceOrRecreate` mode

If vertical Pod autoscaling determines that an in-place update is not possible, it falls back to the `Recreate` mode behavior, which evicts and re-creates the Pod to apply the changes. Some common scenarios where vertical Pod autoscaling falls back to re-creation include:

  * **Insufficient node capacity:** the updated resource request exceeds the allocatable capacity of the current node, and the update cannot be scheduled in-place ("infeasible" or "deferred" state for longer than a timeout).
  * **QoS class change:** the resource update would change the Pod's Quality of Service (QoS) class, for example from `Burstable` to `Guaranteed`.
  * **`RestartContainer` policy:** the Pod's `resizePolicy` field is set to `RestartContainer` for a resource that vertical Pod autoscaling is attempting to change.
  * **Timeouts:** an in-place update request remains in a pending state for too long.



### `Off` mode

In `Off` mode, vertical Pod autoscaling doesn't automatically apply any changes to a Pod. You can still view recommended values for the requests and limits of both CPU and memory based on historical usage, but these recommendations aren't applied for you. You can manually apply the recommended values to your Pods, if needed.

## CPU startup boost

CPU startup boost accelerates application startup and improves cost efficiency by temporarily increasing CPU requests during initialization and resizing them back to baseline levels in-place.

For more information about how to configure CPU startup boost, see [Accelerate application startup with CPU startup boost](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/boost-application-startup).

### How CPU startup boost works

CPU startup boost calculates a temporary resource increase based on your container's baseline CPU request. The Pod returns to this baseline request level after the startup phase.

The boost increases this baseline request by either a multiplier or a fixed quantity. This elevated request remains active until the Pod is ready, after which GKE restores the CPU request to its baseline level.

### Understand the boost lifecycle

The startup boost process consists of three phases:

  1. **Admission phase** : during Pod admission, the VPA admission webhook intercepts the request and injects the boosted CPU values before GKE schedules the Pod.
  2. **Startup phase** : the application initializes using the temporarily elevated CPU allocation to avoid initialization throttling.
  3. **Unboosting phase** : after the Pod reaches the `Ready` status and the `durationSeconds` period has passed, VPA downscales the CPU request in-place to the base value.

**Note:** The [VPA Updater](https://github.com/kubernetes/autoscaler/blob/master/vertical-pod-autoscaler/docs/components.md#updater) checks Pod status on a regular one-minute cycle to handle unboosting. Because of this periodic evaluation, GKE measures the `durationSeconds` period in one-minute intervals, which means a boost might persist for up to one minute longer than configured.

### Choose an update mode for boosted workloads

You can configure CPU startup boost with or without VPA's continuous resource management. VPA's continuous resource management automatically adjusts your Pod resource requests after the startup phase ends. To choose your preference, set the `updateMode` field in the VPA object. For more information about VPA update modes, see Vertical Pod autoscaling modes.

  * **`updateMode: "Off"`** : VPA manages only the initial boost during [Pod admission](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) (a phase in Pod creation) and the subsequent downscale after startup. It doesn't modify your container's steady-state resource requests.
  * **`updateMode: "Auto"`, `"Recreate"`, or `"InPlaceOrRecreate"`**: VPA manages the startup boost and continues to adjust your Pod's resource requests automatically based on its ongoing usage.



### How CPU boost resource allocation is calculated

GKE calculates the temporary boosted CPU request in the following way:

  1. **Determine the base CPU** : the baseline CPU request depends on the VPA `updateMode` field:

     * **`Auto`** , **`Recreate`** , or **`InPlaceOrRecreate`** : the baseline CPU request is the VPA recommendation. If no recommendation exists, GKE falls back to the CPU request defined in the Pod specification.
     * **`Off`** : the baseline CPU request is the request value from the Pod specification.
  2. **Calculate the boosted CPU** : the calculation depends on the calculation method you specify in the boost configuration `type` field:

     * **`Factor`** : applies a multiplier to the base CPU request:

Boosted CPU = base CPU × `factor`

     * **`Quantity`** : adds an absolute CPU quantity to the base CPU request:

Boosted CPU = base CPU + `quantity`




The final CPU request depends on your cluster mode:

  * **Standard clusters** : the final CPU request is the boosted CPU value.
  * **Autopilot clusters** : the final CPU request is the boosted CPU value, capped by the maximum allowed CPU for the allocated Pod memory.



### Understand CPU limit behavior during a boost

The way GKE handles CPU limits depends on the `controlledValues` setting in your `containerResourcePolicy`:

  * **`RequestsAndLimits` (Default)**: GKE boosts both the CPU request and limit, maintaining their original ratio to preserve the container's [Quality of Service (QoS) class](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/).
  * **`RequestsOnly`** : GKE boosts only the CPU request. GKE caps the boosted request just below any defined CPU limit to preserve QoS.



### Considerations for Autopilot clusters

Because GKE Autopilot enforces specific CPU-to-memory ratio ranges and minimum Pod sizes, GKE evaluates boosts during Pod admission to ensure compliance. A boost might be modified or ignored in the following scenarios:

  * **Autopilot minimums** : if the boosted request is below the minimum CPU requirements for Autopilot workloads (for example, 50m for General Purpose Pods), GKE doesn't apply the boost and enforces the standard minimums.
  * **Ratio capping (partial or skipped boosts)** : if the boosted CPU request would exceed the [required CPU-to-memory ratio range](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#compute-class-min-max), GKE caps the boost to the highest value that respects the allocated memory. If the original Pod request already uses the maximum allowed CPU-to-memory ratio, GKE skips the boost to avoid memory resizing.
  * **Scale-Out ComputeClass** : the [Scale-Out ComputeClass](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#scale-out-default) enforces a strict 1:4 (CPU:Memory) ratio. Attempting to boost the CPU on a Scale-Out Pod without increasing its memory can result in GKE ignoring the boost.

**Best practice:** For Autopilot workloads, ensure you allocate enough base memory in your Pod specification to support the boosted CPU ratio. If you rely on startup boost, avoid using the Scale-Out ComputeClass.

## Resource policies

You can use `ContainerResourcePolicy` to customize how vertical Pod autoscaling generates recommendations for specific containers. This policy lets you set constraints and control which resources are scaled.

### Minimum and maximum limits

You can specify the minimum (`minAllowed`) and maximum (`maxAllowed`) resource values for a container.

  * **`minAllowed`** : vertical Pod autoscaling won't recommend a value lower than this limit. This limit is useful because it helps ensure a baseline level of performance or meeting application-specific requirements.
  * **`maxAllowed`** : vertical Pod autoscaling won't recommend a value higher than this limit. This limit is useful for controlling costs or preventing a single container from consuming too many node resources.



### Controlled resources

By default, vertical Pod autoscaling computes recommendations for both CPU and memory. You can use the `controlledResources` field to specify which resources to autoscale. For example, you can configure the autoscaler to provide recommendations only for memory, leaving CPU requests unchanged.

## Limitations

  * To use vertical Pod autoscaling with [horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) on CPU, use [HPA rightsizing with VPA](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rightsize-hpa-workloads-with-vpa) (Preview) or [multidimensional Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multidimensional-pod-autoscaling). You can also use vertical Pod autoscaling with horizontal Pod autoscaling on [custom and external](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/custom-and-external-metrics) metrics.
  * Vertical Pod autoscaling is not ready for use with JVM-based workloads due to limited visibility into actual memory usage of the workload.
  * In GKE version 1.35.1 and earlier, vertical Pod autoscaling has a default setting of two minimum replicas for Deployments to replace Pods with revised resource values. In version 1.35.2 and later, the default is one minimum replica. In version 1.22 and later, you can override this setting by specifying a value for the `minReplicas` field in the [PodUpdatePolicy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler#podupdatepolicy_v1_autoscalingk8sio) field.
  * If you use the `InPlaceOrRecreate` update mode of vertical Pod autoscaling and an in-place update isn't possible (for example, when upscaling the Pod beyond the node capacity), vertical Pod autoscaling evicts and re-creates the Pod to apply the recommendation. Eviction and re-creation occurs even for Pods that have a `resizePolicy` field set in their specification to avoid re-creations. This behavior occurs for Autopilot resize requests, including when applying [minimum resources and CPU:memory ratio constraints](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests).
  * Vertical Pod autoscaling requires a workload object that manages the Pods, such as a Deployment, StatefulSet, ReplicaSet, or ReplicationControllers. You can't use vertical Pod autoscaling with standalone Pods because a workload controller is required to manage the Pod re-creation process.
  * Vertical Pod autoscaling generates recommendations for, and applies updates on, only container-level resource requests and limits (`spec.containers[].resources`). Vertical Pod autoscaling doesn't support [Pod-level resource specifications](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#pod-level-resource-specification) (`spec.resources`).



### Best practices

  * **Limit the number of`VerticalPodAutoscaler` objects.** To avoid cluster update disruptions, you should keep the number of `VerticalPodAutoscaler` objects per cluster under 1,000.
  * **Vertical Pod autoscaling works best with long-running homogenous workloads.**
    * **Long-running:** workloads that run for at least 24 hours. Vertical Pod autoscaling requires a significant amount of historical data to generate high-confidence recommendations. In `Auto` or `Recreate` mode, updates usually happen after a Pod is at least 24 hours old, which helps prevent frequent Pod restarts and churn.
    * **Homogenous:** pods targeted by a single `VerticalPodAutoscaler` object (such as all replicas in a Deployment) should exhibit similar resource consumption patterns. The vertical Pod autoscaler generates recommendations by aggregating usage data across all targeted Pods. If your replicas have heterogeneous usage, for example some Pods are idle and others are heavily loaded, the vertical Pod autoscaler may provide a recommendation that over-provisions the idle pods or under-provisions the busy ones.
  * **Use horizontal Pod autoscaling for workloads with sudden spikes in demand.** Vertical Pod autoscaling is designed for steady-state rightsizing and is not a solution for sudden, short-lived resource spikes. For workloads with rapid fluctuations in traffic or demand for CPU or memory, use the [horizontal Pod autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) instead.
  * **Leverage OOM protection.** Although the vertical Pod autoscaler is reactive, it does include automated protection against Out-of-Memory (OOM) events. If a Pod is `OOMKilled`, the vertical Pod autoscaler immediately observes the event and increases the memory recommendation by approximately 20% (or 100 MB, whichever is larger) to improve stability when the Pod is re-created. For more information about OOM events, see [Troubleshoot OOM events](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/oom-events).



## API reference

This is the `v1` API reference. We strongly recommend using this version of the API.

### VerticalPodAutoscaler v1 autoscaling.k8s.io

Fields  
---  
`` |  `TypeMeta` API group, version, and kind.  
`metadata` |  `ObjectMeta` Standard [object metadata](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#metadata).  
`spec` |  `VerticalPodAutoscalerSpec` The behavior of the `VerticalPodAutoscaler`.  
`status` |  `VerticalPodAutoscalerStatus` The most recently observed status of the `VerticalPodAutoscaler`.   
  
### VerticalPodAutoscalerSpec v1 autoscaling.k8s.io

Fields  
---  
`targetRef` |  `[CrossVersionObjectReference](https://v1-30.docs.kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#crossversionobjectreference-v1-autoscaling)` Reference to the controller that manages the set of Pods for the autoscaler to control, for example, a Deployment or a StatefulSet. You can point a `VerticalPodAutoscaler` at any controller that has a [Scale](https://v1-30.docs.kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#scalespec-v1-autoscaling) subresource. Typically, the `VerticalPodAutoscaler` retrieves the Pod set from the controller's ScaleStatus. For some well known controllers, for example DaemonSet, the `VerticalPodAutoscaler` retrieves the Pod set from the controller's spec.  
`updatePolicy` |  `PodUpdatePolicy` Specifies whether recommended updates are applied when a Pod is started and whether recommended updates are applied during the life of a Pod.  
`resourcePolicy` |  `PodResourcePolicy` Specifies policies for how CPU and memory requests are adjusted for individual containers. The resource policy can be used to set constraints on the recommendations for individual containers. If not specified, the autoscaler computes recommended resources for all containers in the Pod, without additional constraints.   
`recommenders` |  `VerticalPodAutoscalerRecommenderSelector array` The recommender responsible for generating recommendations for this VPA object. Leave empty to use the default recommender provided by GKE. Otherwise the list can contain exactly one entry for a user-provided alternative recommender. Supported since GKE 1.22.   
  
### VerticalPodAutoscalerList v1 autoscaling.k8s.io

Fields  
---  
`` |  `TypeMeta` API group, version, and kind.  
`metadata` |  `ObjectMeta` Standard [object metadata](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#metadata).  
`items` |  `VerticalPodAutoscaler array` A list of `VerticalPodAutoscaler` objects.  
  
### PodUpdatePolicy v1 autoscaling.k8s.io

Fields  
---  
`updateMode` |  `string` Specifies whether recommended updates are applied when a Pod is started and whether recommended updates are applied during the life of a Pod. Possible values are the following:

  * `"Off"`: recommended updates are generated, but aren't automatically applied to the Pod.
  * `"Initial"`: recommended updates are applied only when a Pod is first started. Updates that happen while the Pod is already running aren't automatically applied.
  * `"Recreate"`: recommended updates are applied by re-creating the Pod. The existing Pod is terminated, and a new Pod with the updated configuration is created.
  * `"Auto"`: the default value that essentially enforces the `"Recreate"` mode.
  * `"InPlaceOrRecreate"`: recommended updates are applied without re-creating the Pod, if possible.

  
`minReplicas` |  `int32` The minimum number of replicas which need to be alive to attempt Pod eviction (pending other checks like Pod Disruption Budget). Only positive values are allowed. The default is `1` in GKE version 1.35.2 and later, and `2` in version 1.35.1 and earlier. Supported since GKE 1.22.   
  
### PodResourcePolicy v1 autoscaling.k8s.io

Fields  
---  
`containerPolicies` |  `ContainerResourcePolicy array` An array of resource policies for individual containers. There can be at most one entry for every named container and optionally a single wildcard entry with `containerName = '*'`, which handles all containers that do not have individual policies.   
  
### ContainerResourcePolicy v1 autoscaling.k8s.io

Fields  
---  
`containerName` |  `string` The name of the container that the policy applies to. If not specified, the policy serves as the default policy.  
`mode` |  `ContainerScalingMode` Specifies whether recommended updates are applied to the container when it is started and whether recommended updates are applied during the life of the container. Possible values are "Off" and "Auto". The default is "Auto" if you don't specify a value.  
`minAllowed` |  `ResourceList` Specifies the minimum CPU request and memory request allowed for the container. By default, there is no minimum applied.  
`maxAllowed` |  `ResourceList` Specifies the maximum CPU request and memory request allowed for the container. By default, there is no maximum applied.  
`controlledResources` |  `[]ResourceName` Specifies the type of recommendations that will be computed (and possibly applied) by the `VerticalPodAutoscaler`. If empty, the default of `[ResourceCPU, ResourceMemory]` is used.  
  
### VerticalPodAutoscalerRecommenderSelector v1 autoscaling.k8s.io

Fields  
---  
`name` |  `string` Name of the recommender responsible for generating recommendation for this object.  
  
### VerticalPodAutoscalerStatus v1 autoscaling.k8s.io

Fields  
---  
`recommendation` |  `RecommendedPodResources` The most recently recommended CPU and memory requests.  
`conditions` |  `VerticalPodAutoscalerCondition array` Describes the current state of the `VerticalPodAutoscaler`.  
  
### RecommendedPodResources v1 autoscaling.k8s.io

Fields  
---  
`containerRecommendations` |  `RecommendedContainerResources array` An array of resource recommendations for individual containers.  
  
### RecommendedContainerResources v1 autoscaling.k8s.io

Fields  
---  
`containerName` |  `string` The name of the container that the recommendation applies to.  
`target` |  `ResourceList` The recommended CPU request and memory request for the container.  
`lowerBound` |  `ResourceList` The minimum recommended CPU request and memory request for the container. This amount is not guaranteed to be sufficient for the application to be stable. Running with smaller CPU and memory requests is likely to have a significant impact on performance or availability.  
`upperBound` |  `ResourceList` The maximum recommended CPU request and memory request for the container. CPU and memory requests higher than these values are likely to be wasted.  
`uncappedTarget` |  `ResourceList` The most recent resource recommendation computed by the autoscaler, based on actual resource usage, not taking into account the ContainerResourcePolicy. If actual resource usage causes the target to violate the ContainerResourcePolicy, this value might be different from the bounded recommendation. This field does not affect actual resource assignment. It is used only as a status indication.   
  
### VerticalPodAutoscalerCondition v1 autoscaling.k8s.io

Fields  
---  
`type` |  `VerticalPodAutoscalerConditionType` The type of condition being described. Possible values are "RecommendationProvided", "LowConfidence", "NoPodsMatched", and "FetchingHistory".  
`status` |  `ConditionStatus` The status of the condition. Possible values are True, False, and Unknown.  
`lastTransitionTime` |  `Time` The last time the condition made a transition from one status to another.  
`reason` |  `string` The reason for the last transition from one status to another.  
`message` |  `string` A human-readable string that gives details about the last transition from one status to another.  
  
## What's next

  * Learn how to [configure Vertical Pod Autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling).
  * Learn how to [rightsize HPA workloads with VPA](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rightsize-hpa-workloads-with-vpa).
  * Learn how to [accelerate application startup using CPU startup boost](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/boost-application-startup).
  * Learn more about [Horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler).
  * Learn more about [Cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
