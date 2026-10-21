---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus/
title: ResourceStatus \u00a0|\u00a0 GKE On-Prem API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:19.013787+00:00
---

# ResourceStatus  |  GKE On-Prem API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ GKE On-Prem API ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview)



Send feedback 

#  ResourceStatus Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ResourceCondition
    * JSON representation
  * State
  * Versions
    * JSON representation
  * Version
    * JSON representation



ResourceStatus describes why a cluster or node pool has a certain status. (e.g., ERROR or DEGRADED).

JSON representation  
---  
      
    
    {
      "errorMessage": string,
      "conditions": [
        {
          object ([ResourceCondition](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus#ResourceCondition))
        }
      ],
      "version": string,
      "versions": {
        object ([Versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus#Versions))
      }
    }  
  
Fields  
---  
`errorMessage` |  `string` Human-friendly representation of the error message from controller. The error message can be temporary as the controller controller creates a cluster or node pool. If the error message persists for a longer period of time, it can be used to surface error message to indicate real problems requiring user intervention.  
`conditions[]` |  `object (`[ResourceCondition](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus#ResourceCondition)`)` ResourceCondition provide a standard mechanism for higher-level status reporting from controller.  
`version` |  `string` Reflect current version of the resource.  
`versions` |  `object (`[Versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus#Versions)`)` Shows the mapping of a given version to the number of machines under this version.  
  
## ResourceCondition

ResourceCondition provides a standard mechanism for higher-level status reporting from controller.

JSON representation  
---  
      
    
    {
      "type": string,
      "reason": string,
      "message": string,
      "lastTransitionTime": string,
      "state": enum ([State](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus#State))
    }  
  
Fields  
---  
`type` |  `string` Type of the condition. (e.g., ClusterRunning, NodePoolRunning or ServerSidePreflightReady)  
`reason` |  `string` Machine-readable message indicating details about last transition.  
`message` |  `string` Human-readable message indicating details about last transition.  
`lastTransitionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last time the condition transit from one status to another.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus#State)`)` state of the condition.  
  
## State

The lifecycle state of the condition. Additional intermediate State, e.g. STATE_DEGRADED can be added.

Enums  
---  
`STATE_UNSPECIFIED` | Not set.  
`STATE_TRUE` | Resource is in the condition.  
`STATE_FALSE` | Resource is not in the condition.  
`STATE_UNKNOWN` | Kubernetes controller can't decide if the resource is in the condition or not.  
  
## Versions

Versions describes the mapping of a given version to the number of machines under this version.

JSON representation  
---  
      
    
    {
      "versions": [
        {
          object ([Version](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus#Version))
        }
      ]
    }  
  
Fields  
---  
`versions[]` |  `object (`[Version](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus#Version)`)` Shows the mapping of a given version to the number of machines under this version.  
  
## Version

Version describes the number of nodes at a given version under a resource.

JSON representation  
---  
      
    
    {
      "version": string,
      "count": string
    }  
  
Fields  
---  
`version` |  `string` Resource version.  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of machines under the above version.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-29 UTC."],[],[]] 
