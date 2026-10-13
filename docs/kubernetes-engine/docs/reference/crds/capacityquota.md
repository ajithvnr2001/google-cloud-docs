---
url: https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/capacityquota/
title: CapacityQuota \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:30.503530+00:00
---

# CapacityQuota  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/capacityquota/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/authentication)



Send feedback 

#  CapacityQuota Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The CapacityQuota CustomResourceDefinition (CRD) limits the amount of resources that can be provisioned for specific subsets of nodes that you target by using label selectors. For more information about how CapacityQuotas work, see [Configure granular resource limits](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-capacity-quotas).
    
    
    apiVersion: autoscaling.x-k8s.io/v1beta1
    kind: CapacityQuota
    metadata:
      name: capacity-quota
    spec:
      selector:
        matchLabels:
          cloud.google.com/compute-class: my-class
        matchExpressions:
          - key: cloud.google.com/machine-family
            operator: In
            values:
              - c2
              - c3
              - c3d
      limits:
        resources:
          cpu: 64
          memory: 128Gi
    status:
      observedGeneration: 1
      conditions:
      - lastTransitionTime: "2026-07-27T10:00:00Z"
        message: "CapacityQuota is valid"
        reason: "Valid"
        status: "True"
        type: "cluster-autoscaler.kubernetes.io/valid"
      used:
        resources:
          cpu: "32"
          memory: 128Gi
    

## CapacityQuota specification
    
    
    spec:
      limits: object (limits)
      selector: object (selector)

Fields  
---  
`spec.limits` _required_ |  `object (limits)` This object defines resource limits for the matched nodes.  
`spec.selector` _optional_ |  `object (selector)` Label selectors to target subsets of nodes. If you omit this field or you don't specify a value, then the CapacityQuota matches all of the nodes in the cluster.  
  
### limits

`limits` object defines the resource limits of a CapacityQuota.
    
    
    limits:
      resources:
        string: string

Fields  
---  
`resources` _required_ |  `map (string: string)` The `resources` map define the resource limits of this quota. Map keys are resource names and map values are strings in the [resource.Quantity](https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity) format. The following resource names are supported:

  * `cpu`: limits for CPU resources.
  * `memory`: limits for memory resources.
  * `nodes`: limits for the number of nodes.
  * `nvidia.com/gpu`: limits for the number of NVIDIA GPUs.
  * `google.com/tpu`: limits for the number of TPUs.

All resource quantities must be integer values that are greater than `0`. You can specify binary and decimal values if those values can be converted to integers. Milli units (`m`) aren't supported, even if the milli unit represents an integer value. Examples of valid resource quantities include `"32Gi"`, `"2k"`, and `"10.0"`. Examples of invalid quantities include `"1000m"`, `"3.67Gi"`, and `"0.3"`.  
  
### selector

This is a standard Kubernetes [LabelSelector](https://kubernetes.io/docs/reference/kubernetes-api/definitions/label-selector-v1-meta/) object.
    
    
    matchExpressions:
      - object (matchExpressions)
    matchLabels:
      string: string

Fields  
---  
`matchExpressions[]` _optional_ |  `object (matchExpressions)` A list of label selector requirements. The requirements are ANDed.  
`matchLabels` _optional_ |  `map (string: string)` A map of key-value pairs. A single entry in the `matchLabels` map is equivalent to an element of `matchExpressions` field, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.  
  
### matchExpressions

This is a standard Kubernetes [LabelSelectorRequirement](https://kubernetes.io/docs/reference/kubernetes-api/definitions/label-selector-requirement-v1-meta/#label-selector-requirement) object.
    
    
    key: string
    operator: string
    values:
      - string
    

Fields  
---  
`key` _required_ |  `string` The label key that the selector applies to.  
`operator` _required_ |  `string` This represents a key's relationship to a set of values. Valid operators are `In`, `NotIn`, `Exists` and `DoesNotExist`.  
`values` _optional_ |  `array (string)` This is an array of string values. If the operator is `In` or `NotIn`, the values array must be non-empty. If the operator is `Exists` or `DoesNotExist`, the values array must be empty. This array is replaced during a strategic merge patch.  
  
## status

The `status` object indicates the observed state of the CapacityQuota resource.
    
    
    conditions:
      - object ([Condition](https://kubernetes.io/docs/reference/kubernetes-api/definitions/condition-v1-meta/))
    observedGeneration: integer
    used: object (used)

Fields  
---  
`conditions[]` |  `object ([Condition](https://kubernetes.io/docs/reference/kubernetes-api/definitions/condition-v1-meta/))` The `conditions` array provide a standard mechanism for reporting the quota's state.  
  
Cluster Autoscaler manages the `cluster-autoscaler.kubernetes.io/valid` condition, and will enforce the quota only if the status of the condition is `True`.  
`observedGeneration` |  `integer` The `observedGeneration` represents the last `.metadata.generation` observed by the controller.  
`used` |  `object (used)` The `used` object shows the current usage of the quota.  
  
### used

The `used` object shows the current usage of the quota.
    
    
    resources:
      string: string
    

Fields  
---  
`resources` |  `map (string: string)` The `resources` map shows the current usage of the resources defined in the quota limits.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
