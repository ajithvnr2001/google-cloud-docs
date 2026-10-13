---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apphub/latest/google.cloud.apphub_v1.types.Application
title: Class Application (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:54:37.274473+00:00
---

# Class Application (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apphub/latest/google.cloud.apphub_v1.types.Application

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Application (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    Application(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Application defines the governance boundary for App Hub entities that perform a logical end-to-end business function. App Hub supports application level IAM permission to align with governance requirements.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The resource name of an Application. Format: `"projects/{host-project-id}/locations/{location}/applications/{application-id}"`  
`display_name` |  `str`   
Optional. User-defined name for the Application. Can have a maximum length of 63 characters.   
`description` |  `str`   
Optional. User-defined description of an Application. Can have a maximum length of 2048 characters.   
`attributes` |  `[google.cloud.apphub_v1.types.Attributes](https://docs.cloud.google.com/python/docs/reference/google-cloud-apphub/latest/google.cloud.apphub_v1.types.Attributes)`   
Optional. Consumer provided attributes.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Create time.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Update time.   
`scope` |  `[google.cloud.apphub_v1.types.Scope](https://docs.cloud.google.com/python/docs/reference/google-cloud-apphub/latest/google.cloud.apphub_v1.types.Scope)`   
Required. Immutable. Defines what data can be included into this Application. Limits which Services and Workloads can be registered.   
`uid` |  `str`   
Output only. A universally unique identifier (in UUID4 format) for the `Application`.   
`state` |  `[google.cloud.apphub_v1.types.Application.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-apphub/latest/google.cloud.apphub_v1.types.Application.State)`   
Output only. Application state.   
`application_properties` |  `[google.cloud.apphub_v1.types.ApplicationProperties](https://docs.cloud.google.com/python/docs/reference/google-cloud-apphub/latest/google.cloud.apphub_v1.types.ApplicationProperties)`   
Output only. Properties of an underlying cloud resource that can comprise an Application.   
`application_type` |  `[google.cloud.apphub_v1.types.ApplicationType](https://docs.cloud.google.com/python/docs/reference/google-cloud-apphub/latest/google.cloud.apphub_v1.types.ApplicationType)`   
Output only. Application type.   
  
## Classes 

### State
    
    
    State(value)

Application state.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
