---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/NodeTaint/
title: NodeTaint \u00a0|\u00a0 GKE Multi-Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:58:40.468483+00:00
---

# NodeTaint  |  GKE Multi-Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/NodeTaint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE Multi-Cloud Reference ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations)



Send feedback 

#  NodeTaint Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Effect



The taint content for the node taint.

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string,
      "effect": enum ([Effect](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/NodeTaint#Effect))
    }  
  
Fields  
---  
`key` |  `string` Required. Key for the taint.  
`value` |  `string` Required. Value for the taint.  
`effect` |  `enum (`[Effect](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/NodeTaint#Effect)`)` Required. The taint effect.  
  
## Effect

The taint effect.

Enums  
---  
`EFFECT_UNSPECIFIED` | Not set.  
`NO_SCHEDULE` | Do not allow new pods to schedule onto the node unless they tolerate the taint, but allow all pods submitted to Kubelet without going through the scheduler to start, and allow all already-running pods to continue running. Enforced by the scheduler.  
`PREFER_NO_SCHEDULE` | Like TaintEffectNoSchedule, but the scheduler tries not to schedule new pods onto the node, rather than prohibiting new pods from scheduling onto the node entirely. Enforced by the scheduler.  
`NO_EXECUTE` | Evict any already-running pods that do not tolerate the taint. Currently enforced by NodeController.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
