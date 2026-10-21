---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/krm/vertex-ai-prediction-common-krm/
title: KRM API aiplatform.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:55.192072+00:00
---

# KRM API aiplatform.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/krm/vertex-ai-prediction-common-krm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API aiplatform.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## aiplatform.gdc.goog/v1

Package v1 contains API Schema definitions for the aiplatform.gdc.goog v1 API group.

### Destination

Presents the amount of traffic that must be routed to the service.

_Appears in:_

  * EndpointSpec

Field | Description  
---|---  
`trafficPercentage` _integer_ | Represents the percentage of traffic that needs to be routed to the specific service. All traffic percentage values must sum up to 100, or, alternatively, no destinations should be specified if the Endpoint is currently intended to receive zero traffic.  
`serviceRef` _DestinationServiceRef_ | Indicates the service reference.  
`httpPort` _integer_ | Represents the hard-coded sidecar HTTP port that is used when `ServiceRef.Kind` is `DeployedModel`.  
`grpcPort` _integer_ | Represents the hard-coded sidecar gRPC port that is used when `ServiceRef.Kind` is `DeployedModel`.  
  
### DestinationServiceRef

Defines the services that the traffic can be routed to.

_Appears in:_

  * Destination

Field | Description  
---|---  
`kind` _string_ | Represents the kind of the destination service reference, for example, `DeployedModel`, `MicroService`, or `Service`.  
`name` _string_ |   
`namespace` _string_ |   
  
### Endpoint

Defines the dataplane for the services and handles the routing for those services.

_Appears in:_

  * EndpointList

Field | Description  
---|---  
`apiVersion` _string_ | `aiplatform.gdc.goog`  
`kind` _string_ | `Endpoint`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _EndpointSpec_ |   
`status` _EndpointStatus_ |   
  
### EndpointList

Contains a list of `Endpoint` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `aiplatform.gdc.goog`  
`kind` _string_ | `EndpointList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Endpoint array_ |   
  
### EndpointSpec

Includes traffic destinations with weight and defines whether a new Domain Name System (DNS) name must be created or an existing one must be used.

_Appears in:_

  * Endpoint

Field | Description  
---|---  
`destinations` _Destination array_ |   
`createDns` _boolean_ | Specifies whether a new DNS name must be created or not.  
`dnsName` _string_ | Presents the existing or new DNS name. This field is deprecated; use `UserProvidedID` instead.  
`id` _string_ | Indicates the auto-generated endpoint ID.  
`userProvidedId` _string_ | Indicates the user-provided endpoint ID.  
  
### EndpointStatus

_Appears in:_

  * Endpoint

Field | Description  
---|---  
`ready` _boolean_ | Indicates whether the resource is in a ready state.  
`primaryCondition` | Represents the primary condition of a resource. If the resource is ready, then the condition indicates the resource is ready. Otherwise, the condition is the primary reason why the resource is not ready.  
`resourceConditions` _array_ | Represents a collection of conditions for a resource and its subresources. You can use it to determine the overall health of a resource and its subresources.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Represents raw resource conditions populated from Kubernetes resources for debugging purposes.  
`endpointFQDN` _string_ | Indicates the fully qualified domain name (FQDN) of the endpoint that is saved when a new DNS name is created successfully.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
