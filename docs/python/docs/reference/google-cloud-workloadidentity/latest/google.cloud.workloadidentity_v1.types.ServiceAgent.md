---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.types.ServiceAgent
title: Class ServiceAgent (0.1.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:27:31.334064+00:00
---

# Class ServiceAgent (0.1.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.types.ServiceAgent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ServiceAgent (0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    ServiceAgent(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message describing ServiceAgent object

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The name of the service agent resource   
`container` |  `str`   
Optional. Name of the container that the service agent is associated with. For example: \- projects/1234 \- folders/1234 \- organizations/2344   
`service_producer` |  `str`   
Optional. The service the agent belongs to. For example, bigquery.googleapis.com   
`principal` |  `str`   
Optional. The principal identifier for the service agent. This identifier is used in allow policies to grant access to the service agent.   
`role` |  `str`   
Optional. The role that should be granted to service agent on consumer project, if any. For example, "roles/aiplatform.serviceAgent".   
`state` |  `[google.cloud.workloadidentity_v1.types.ServiceAgent.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.types.ServiceAgent.State)`   
Output only. Service agent state.   
  
## Classes 

### State
    
    
    State(value)

Enum for service agent `state`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-13 UTC."],[],[]] 
