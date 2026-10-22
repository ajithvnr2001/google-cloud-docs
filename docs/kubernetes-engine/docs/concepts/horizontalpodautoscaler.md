---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler/
title: Horizontal Pod autoscaling \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:05.229646+00:00
---

# Horizontal Pod autoscaling  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Horizontal Pod autoscaling Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides an overview of horizontal Pod autoscaling and explains how it works in Google Kubernetes Engine (GKE). You can also read about how to [configure and use horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling) on your clusters.

The horizontal Pod autoscaler changes the shape of your Kubernetes workload by automatically increasing or decreasing the number of Pods in response to the workload's CPU or memory consumption, or in response to custom metrics reported from within Kubernetes or external metrics from sources outside of your cluster.

Horizontal Pod autoscaling doesn't change the number of nodes in a GKE cluster. To automatically scale the number of nodes in the cluster based on changes in the number of Pods, you can use the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).

When you first deploy your workload to a Kubernetes cluster, you might not be sure about its resource requirements. These requirements might also change over time depending on usage patterns, external dependencies, or other factors. Horizontal Pod autoscaling helps to ensure that your workload functions consistently in different situations, and lets you control costs by only paying for extra capacity when you need it.

It's not always easy to predict the indicators that show whether your workload is under-resourced or under-utilized. The horizontal Pod autoscaler can automatically scale the number of Pods in your workload based on one or more metrics of the following types:

  * **Actual resource usage** : when a given Pod's CPU or memory usage exceeds a threshold. This can be expressed as a raw value or as a percentage of the amount the Pod requests for that resource.

  * **Custom metrics** : based on any metric reported by a Kubernetes object in a cluster, such as the rate of client requests per second or I/O writes per second.

This can be useful if your application is prone to network bottlenecks, rather than CPU or memory.

  * **External metrics** : based on a metric from an application or service external to your cluster.

For example, your workload might need more CPU when ingesting a large number of requests from a pipeline such as Pub/Sub. You can create an external metric for the size of the queue, and configure the horizontal Pod autoscaler to automatically increase the number of Pods when the queue size reaches a given threshold, and to reduce the number of Pods when the queue size shrinks.




You can combine a horizontal Pod autoscaler with a vertical Pod autoscaler, with some limitations.

## How horizontal Pod autoscaling works

Each configured horizontal Pod autoscaler operates using a control loop. A separate horizontal Pod autoscaler exists for each workload. Each horizontal Pod autoscaler periodically checks a given workload's metrics against the target thresholds you configure, and changes the shape of the workload automatically.

### Per-Pod resources

For resources that are allocated per-Pod, such as CPU, the controller queries the resource metrics API for each container running in the Pod.

  * If you specify a raw value for CPU or memory, the value is used.
  * If you specify a percentage value for CPU or memory, the horizontal Pod autoscaler calculates the **average** utilization value as a percentage of that Pod's CPU or memory requests.
  * Custom and external metrics are expressed as raw values or average values.

**Note:** To use resource utilization percentage targets with horizontal Pod autoscaling, you must configure requests for that resource for each container running in each Pod in the workload. Otherwise, the horizontal Pod autoscaler cannot perform the calculations it needs to, and takes no action related to that metric.

The controller uses the average or raw value for a reported metric to produce a ratio, and uses that ratio to autoscale the workload. You can read a description of the [horizontal Pod autoscaler algorithm](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#algorithm-details) in the Kubernetes project documentation.

### Responding to multiple metrics

If you configure a workload to autoscale based on multiple metrics, the horizontal Pod autoscaler evaluates each metric separately and uses the scaling algorithm to determine the new workload scale based on each one. The **largest** scale is selected for the autoscale action.

If one or more of the metrics are unavailable for some reason, the horizontal Pod autoscaler still scales **up** based on the largest size calculated, but does not scale **down**.

### Preventing thrashing

_Thrashing_ refers to a situation in which the horizontal Pod autoscaler attempts to perform subsequent autoscaling actions before the workload finishes responding to prior autoscaling actions. To prevent thrashing, the horizontal Pod autoscaler chooses the largest recommendation from a specified stabilization window. This behavior is controlled by the `scaleDown.stabilizationWindowSeconds` field in the HPA `behavior` specification, which defaults to 300 seconds (five minutes) in GKE.

To prevent minor fluctuations from causing unnecessary scaling events, the horizontal Pod autoscaler uses a tolerance value of 10%. For a given target, no scaling action is taken if the ratio of the current metric value to the target metric value is within 10% of 1.0.

### Scaling to and from zero

In GKE version 1.37 or later, you can configure the horizontal Pod autoscaler to scale a workload down to `0` replicas when there is no demand, and automatically scale the workload back up when demand resumes. Scaling to and from zero includes the following behaviors:

  * **Tolerance bypass** : when a workload is at `0` replicas, GKE bypasses the standard metric tolerance check (0.9 to 1.1 ratio). Any metric value greater than zero, such as a single message in a queue, immediately triggers a scale-up to at least `1` replica without waiting to cross a tolerance threshold.
  * **Stabilization windows** : scale-up defaults to `0` seconds (`scaleUp.stabilizationWindowSeconds: 0`) for immediate activation, while scale-down defaults to `300` seconds (`scaleDown.stabilizationWindowSeconds: 300`) to help ensure five continuous minutes of zero demand before scaling to `0` replicas.
  * **Status conditions** : when scaled to `0` replicas by the HPA, the controller reports the `ScaledToZero: True` condition while remaining active (`ScalingActive: True`). If a workload is manually scaled to `0` replicas outside the HPA (such as with the `kubectl scale` command), autoscaling pauses (`ScalingActive: False`) until the workload is scaled back to `1` or more replicas.



For step-by-step instructions, see [Scale GKE workloads to and from zero using HPA](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scale-to-from-zero-hpa).

## Limitations

  * Unless you use [HPA rightsizing with VPA](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rightsize-hpa-workloads-with-vpa) (Preview), don't use the horizontal Pod autoscaler together with standard [vertical Pod autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler) on CPU or memory. You can use the horizontal Pod autoscaler with the vertical Pod autoscaler for other metrics, or [configure multidimensional Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multidimensional-pod-autoscaling) to scale horizontally on CPU and vertically on memory at the same time.
  * If you have a Deployment, don't configure horizontal Pod autoscaling on the ReplicaSet or Replication Controller backing it. When you perform a rolling update on the Deployment or Replication Controller, it is replaced by a new Replication Controller. Instead configure horizontal Pod autoscaling on the Deployment itself.
  * You can't use horizontal Pod autoscaling for workloads that cannot be scaled, such as DaemonSets.
  * Horizontal Pod autoscaling exposes metrics as Kubernetes resources, which imposes limitations on metric names such as no uppercase or '/' characters. Your metric adapter might allow renaming. For example, see the [`prometheus-adapter` `as` operator](https://github.com/kubernetes-sigs/prometheus-adapter/blob/master/docs/config.md#naming).
  * The horizontal Pod autoscaler doesn't scale down if any of the [metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#multiple-metrics) that it's configured to monitor are unavailable. To check if you have unavailable metrics, see [Viewing details about a horizontal Pod autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#viewing).



## Scalability

While the horizontal Pod autoscaler doesn't have a hard limit on the number of supported HPA objects, its performance can be affected as this number grows. Specifically, the period between HPA recalculations might become longer than the standard 15 seconds.

  * In **GKE minor version 1.31 or 1.32** , if the **Performance HPA profile** is configured, the recalculation period should stay within 15 seconds with up to **1,000 HPA objects**. Learn how to [configure the Performance HPA profile](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#hpa-profile).
  * In **GKE minor version 1.33 or later** , if the **Performance HPA profile** is configured, the recalculation period should stay within 15 seconds with up to **5,000 HPA objects**. The Performance HPA profile is enabled by default on all clusters that meet the [requirements](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#requirements_2).
  * If the **Performance HPA profile** is not configured, the recalculation period should stay within 15 seconds with up to **300 HPA objects**.



The following factors can also affect performance:

  * **[Scaling on multiple metrics](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#scaling-on-multiple-metrics)** : each metric adds a fetch call for recommendation calculations, which affects the recalculation period.
  * **The latency of the[custom metrics](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#scaling-on-custom-metrics) stack**: response times over approximately 50 milliseconds would be more than typically observed with the standard Kubernetes metrics, affecting the recalculation period.



## Interacting with HorizontalPodAutoscaler objects

You can configure a horizontal Pod autoscaler for a workload, and get information about autoscaling events and what caused them, by visiting the [Workloads](https://console.cloud.google.com/kubernetes/workload/overview) page in the Google Cloud console.

Each horizontal Pod autoscaler exists in the cluster as a HorizontalPodAutoscaler object. You can use commands like `kubectl get hpa` or `kubectl describe hpa HPA_NAME` to interact with these objects.

You can also create HorizontalPodAutoscaler objects using the [`kubectl autoscale` command](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#autoscale).

## What's next

  * Learn how to [configure horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling).
  * Learn how to [rightsize HPA workloads with VPA](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rightsize-hpa-workloads-with-vpa).
  * Learn how to [scale to and from zero using HPA](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scale-to-from-zero-hpa).
  * Learn how to [manually scale an Application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/scaling-apps).
  * Learn more about the [vertical Pod autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler).
  * Learn more about the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
