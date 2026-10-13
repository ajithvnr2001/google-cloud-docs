---
url: https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/UpgradeInfoEvent/
title: UpgradeInfoEvent \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:41.621748+00:00
---

# UpgradeInfoEvent  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/UpgradeInfoEvent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/authentication)



Send feedback 

#  UpgradeInfoEvent Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



UpgradeInfoEvent is a notification sent to customers about the upgrade information of a resource.

JSON representation  
---  
      
    
    {
      "resourceType": enum ([UpgradeResourceType](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/UpgradeResourceType)),
      "operation": string,
      "startTime": string,
      "endTime": string,
      "currentVersion": string,
      "targetVersion": string,
      "currentEmulatedVersion": string,
      "targetEmulatedVersion": string,
      "resource": string,
      "state": enum ([State](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/State)),
      "description": string,
      "eventType": enum ([EventType](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/EventType)),
      "standardSupportEndTime": string,
      "extendedSupportEndTime": string,
      "disruptionEvent": {
        object ([DisruptionEvent](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/DisruptionEvent))
      }
    }  
  
Fields  
---  
`resourceType` |  `enum (`[UpgradeResourceType](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/UpgradeResourceType)`)` The resource type associated with the upgrade.  
`operation` |  `string` The operation associated with this upgrade.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time when the operation was started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time when the operation ended.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`currentVersion` |  `string` The current version before the upgrade.  
`targetVersion` |  `string` The target version for the upgrade.  
`currentEmulatedVersion` |  `string` The current emulated version before the upgrade.  
`targetEmulatedVersion` |  `string` The target emulated version for the upgrade.  
`resource` |  `string` Optional relative path to the resource. For example in node pool upgrades, the relative path of the node pool.  
`state` |  `enum (`[State](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/State)`)` Output only. The state of the upgrade.  
`description` |  `string` A brief description of the event.  
`eventType` |  `enum (`[EventType](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/EventType)`)` The type of the event.  
`standardSupportEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The end of standard support timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`extendedSupportEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The end of extended support timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`disruptionEvent` |  `object (`[DisruptionEvent](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/DisruptionEvent)`)` The information about the disruption event. This field is only populated when eventType is DISRUPTION_EVENT.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-15 UTC."],[],[]] 
