---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/BatchDedicatedResources/
title: BatchDedicatedResources \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:51:31.744199+00:00
---

# BatchDedicatedResources  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/BatchDedicatedResources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  BatchDedicatedResources Stay organized with collections  Save and categorize content based on your preferences. 

A description of resources that are used for performing batch operations, are dedicated to a Model, and need manual configuration.

Fields  
  
`machineSpec` `object (`MachineSpec`)` Required. Immutable. The specification of a single machine. | `startingReplicaCount` `integer` Immutable. The number of machine replicas used at the start of the batch operation. If not set, Agent Platform decides starting number, not greater than `[maxReplicaCount](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/BatchDedicatedResources#FIELDS.max_replica_count)` | `maxReplicaCount` `integer` Immutable. The maximum number of machine replicas the batch operation may be scaled to. The default value is 10. | `flexStart` `object (`[FlexStart](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FlexStart)`)` Optional. Immutable. If set, use DWS resource to schedule the deployment workload. reference: (<https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler>) | `spot` `boolean` Optional. If true, schedule the deployment workload on [spot VMs](https://cloud.google.com/kubernetes-engine/docs/concepts/spot-vms). | JSON representation  
---  
      
    
    {
      "machineSpec": {
        object (MachineSpec)
      },
      "startingReplicaCount": integer,
      "maxReplicaCount": integer,
      "flexStart": {
        object ([FlexStart](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FlexStart))
      },
      "spot": boolean
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
