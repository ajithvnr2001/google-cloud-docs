---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multidimensional-pod-autoscaling/
title: Configure multidimensional Pod autoscaling \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:27.803589+00:00
---

# Configure multidimensional Pod autoscaling  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multidimensional-pod-autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Configure multidimensional Pod autoscaling Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Multidimensional Pod autoscaling frees you from choosing a single way to scale your clusters. With multidimensional Pod autoscaling, you can use [horizontal scaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) based on CPU and [vertical scaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler) based on memory at the same time.

A `MultidimPodAutoscaler` object modifies memory requests and adds replicas so that the average CPU utilization of each replica matches your target utilization.

## Prerequisites

  * GKE cluster version 1.19.4-gke.1700 or later.
  * For Standard clusters, [enable vertical Pod autoscaling in your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling#gcloud-cli). Vertical Pod autoscaling is already enabled in [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) clusters.



## Using multidimensional Pod autoscaling

This example shows you how to create a Deployment and a `MultidimPodAutoscaler` object to autoscale your Deployment.

### Creating a Deployment

Before you can create a `MultidimPodAutoscaler`, you must create the workload it monitors. The following file, `php-apache.yaml`, specifies a value for the CPU requests:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: php-apache
    spec:
      selector:
        matchLabels:
          run: php-apache
      replicas: 1
      template:
        metadata:
          labels:
            run: php-apache
        spec:
          containers:
          - name: php-apache
            image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
            ports:
            - containerPort: 80
            resources:
            # Since MPA does not specify CPU requests, you must specify a request in
            # the Deployment
              limits:
                cpu: 500m
              requests:
                cpu: 200m
    

To create the Deployment, apply the `php-apache.yaml` manifest:
    
    
    kubectl apply -f php-apache.yaml
    

### Creating a MultidimPodAutoscaler

Once you have created the Deployment, you can create a `MultidimPodAutoscaler` object. The following `MultidimPodAutoscaler` manifest automatically adjusts the number of replicas and memory requests based on the values you specify.

For more information on the fields in this example, see the API reference section.
    
    
    apiVersion: autoscaling.gke.io/v1beta1
    kind: MultidimPodAutoscaler
    metadata:
      name: php-apache-autoscaler
    spec:
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: php-apache
      goals:
        metrics:
        - type: Resource
          resource:
          # Define the target CPU utilization request here
            name: cpu
            target:
              type: Utilization
              averageUtilization: 60
      constraints:
        global:
          minReplicas: 1
          maxReplicas: 5
        containerControlledResources: [ memory ]
        container:
        - name: '*'
        # Define boundaries for the memory request here
          requests:
            minAllowed:
              memory: 1Gi
            maxAllowed:
              memory: 2Gi
      policy:
        updateMode: Auto
    

To create the `MultidimPodAutoscaler`, apply the `php-apache-autoscaler.yaml` manifest:
    
    
    kubectl apply -f php-apache-autoscaler.yaml
    

## Viewing a MultidimPodAutoscaler

View all `MultidimPodAutoscaler` objects by using the `kubectl get` command:
    
    
    kubectl get mpa
    

## Deleting a MultidimPodAutoscaler

Delete a `MultidimPodAutoscaler` object by using the `kubectl delete` command:
    
    
    kubectl delete -f php-apache-autoscaler.yaml
    

## API reference

The following sections provide information on the possible fields you can add to your `MultidimPodAutoscaler` object.

All fields are for `apiVersion` `v1beta1 autoscaling.gke.io`.

### MultidimPodAutoscaler

`MultidimPodAutoscaler` is the configuration for a multidimensional Pod autoscaler, which automatically manages Pod resources and their count based on historical and real-time resource utilization.

Field | Type | Description  
---|---|---  
`metadata` | `ObjectMeta` | Standard [object metadata](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#metadata).  
`spec` | `MultidimPodAutoscalerSpec` | The desired behavior of the multidimensional Pod autoscaler.  
`status` | `MultidimPodAutoscalerStatus` | The most recently observed status of the multidimensional Pod autoscaler.  
  
### MultidimPodAutoscalerSpec

`MultidimPodAutoscalerSpec` is the specification that defines the behavior of the autoscaler.

Field | Type | Description  
---|---|---  
`ScaleTargetRef` | `autoscaling.CrossVersionObjectReference` | A reference that points to a target resource to scale (with the Scale subresource).  
`Goals` | `*MultidimGoals` | Goals that the multidimensional Pod autoscaler tries to achieve and maintain.  
`Constraints` | `*MultidimConstraints` | Describes the constraints for autoscaling. Constraints outweigh goals. If constraints block some goal, then the goal will not be reached. For example, reaching the maximum replica count prevents further scale up even if the replicas might need to scale.  
`Policy` | `*MultidimPolicy` | Policy allows you to specify how the recommendations are applied.  
  
### MultidimGoals

`MultidimGoals` are goals that the multidimensional Pod autoscaler tries to achieve.

Field | Type | Description  
---|---|---  
`Metrics` | `[]MetricSpec` | Contains the list of metrics along with the desired value. Multidimensional Pod autoscaler tries to stay close to the desired values.  
  
### MultidimConstraints

`MultidimConstraints` describe the constraints for autoscaling. Constraints take precedence over goals.

Field | Type | Description  
---|---|---  
`Global` | `*GlobalConstraints` | Constraints that apply to the autoscaled application as a whole.  
`Pod` | `*PodConstraints` | Constraints that apply to a single Pods from the targeted application.  
`ContainerControlledResources` | `[]ResourceName` | Container Resources that should be controlled by the autoscaler. `memory` is the only supported value.  
`Container` | `[]ContainerConstraints` | Constraints that apply to Pods' containers.  
  
### ResourceConstraints

`ResourceConstraints` define the minimum and maximum amount of resources that you can assign to a container, Pod, or application.

Field | Type | Description  
---|---|---  
`MinAllowed` | `ResourceList` | Minimum amount of resources that you can assign. If not provided, 0 is used.  
`MaxAllowed` | `ResourceList` | Maximum amount of resources that you can assign. If not provided, there are no limits on the maximum amount of resources.  
  
### GlobalConstraints

`GlobalConstraints` define the constraints which apply to the application altogether. These constraints include the number of replicas or the total amount of resources.

Field | Type | Description  
---|---|---  
`MinReplicas` | `*Int32` | Minimum amount of replicas that the application can have. If not provided, 1 is used.  
`MaxReplicas` | `*Int32` | Maximum amount of replicas that the application can have. If not provided, there are no limits on the maximum amount of replicas.  
`Requests` | `*ResourceConstraints` | Minimum and maximum amount of resources that an application can request, summed across all pods.  
  
### PodConstraints

`PodConstraints` define the minimum and maximum amount of resources that a single Pod can request, summed across all containers that belong to the Pod.

Field | Type | Description  
---|---|---  
`Requests` | `*ResourceConstraints` | Minimum and maximum amount of resources that a single Pod can request, summed across all containers that belong to the Pod.  
  
### ContainerConstraints

`ContainerConstraints` are constraints that apply to Pods' containers.

Fields | Type | Description  
---|---|---  
`Name` | `String` | Name of the container for which the constraints are specified. You can also use `*` to specify constraints for all containers in a Pod.  
`Requests` | `*ResourceConstraints` | Minimum and maximum amount of resources that the specified container can request.  
  
### UpdateMode

Use `UpdateMode` to control how the calculated recommendations are applied.

Fields | Type | Description  
---|---|---  
`AutoUpdates` | `UpdateMode = "Auto"` | AutoUpdates means that all autoscaler recommendations can be applied at any time.  
  
### MultidimPolicy

Fields | Type | Description  
---|---|---  
`Update` | `UpdateMode` | Defines how the recommendations should be applied. An empty value fails validation.  
  
### MultidimPodAutoscalerStatus

`MultidimPodAutoscalerStatus` describes the runtime state of the autoscaler.

Fields | Type | Description  
---|---|---  
`ObservedGeneration` | `*Int64` | The most recently generation observed by this autoscaler.  
`RecommendedPodResources` | `*RecommendedPodResources` | The most recently computed amount of resources recommended by the autoscaler for the controlled Pods.  
`CurrentReplicas` | `Int32` | `CurrentReplicas` is the current number of replicas of Pods managed by this autoscaler, as last seen by the autoscaler.  
`DesiredReplicas` | `Int32` | `DesiredReplicas` is the desired number of replicas of Pods managed by this autoscaler, as last calculated by the autoscaler.  
`CurrentMetrics` | `[]autoscaling.MetricStatus` | The last read state of the metrics used by this autoscaler.  
`Conditions` | `[]metav1.Condition` | `Conditions` is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met.  
  
## What's next

  * Learn more about configuring [horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling).
  * Learn more about configuring [vertical Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
