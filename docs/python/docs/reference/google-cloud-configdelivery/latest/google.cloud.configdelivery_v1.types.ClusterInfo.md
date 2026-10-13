---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-configdelivery/latest/google.cloud.configdelivery_v1.types.ClusterInfo
title: Class ClusterInfo (0.5.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:09.768766+00:00
---

# Class ClusterInfo (0.5.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-configdelivery/latest/google.cloud.configdelivery_v1.types.ClusterInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ClusterInfo (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.5.0  0.4.0  0.3.0  0.2.0  0.1.3 
    
    
    ClusterInfo(mapping=None, *, ignore_unknown_fields=False, **kwargs)

ClusterInfo represents status of a resource bundle rollout for a cluster.

## Attributes  
  
---  
**Name** | **Description**  
`membership` |  `str`   
Output only. gkehub membership of target cluster   
`desired` |  `[google.cloud.configdelivery_v1.types.ResourceBundleDeploymentInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-configdelivery/latest/google.cloud.configdelivery_v1.types.ResourceBundleDeploymentInfo)`   
Output only. Desired state for the resource bundle.   
`initial` |  `[google.cloud.configdelivery_v1.types.ResourceBundleDeploymentInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-configdelivery/latest/google.cloud.configdelivery_v1.types.ResourceBundleDeploymentInfo)`   
Output only. Initial state of the resource bundle prior to the deployment.   
`current` |  `[google.cloud.configdelivery_v1.types.ResourceBundleDeploymentInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-configdelivery/latest/google.cloud.configdelivery_v1.types.ResourceBundleDeploymentInfo)`   
Output only. Current state of the resource bundle.   
`state` |  `[google.cloud.configdelivery_v1.types.ClusterInfo.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-configdelivery/latest/google.cloud.configdelivery_v1.types.ClusterInfo.State)`   
Output only. State of the rollout for the cluster.   
`messages` |  `MutableSequence[str]`   
Output only. Unordered list. Messages convey additional information related to the deployment.   
`start_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Timestamp when reconciliation starts.   
`end_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Timestamp when reconciliation ends.   
  
## Classes 

### State
    
    
    State(value)

State of the rollout for the cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
