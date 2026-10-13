---
url: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ListRuntimesResponse.Runtime
title: Class Runtime (1.25.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:08.820698+00:00
---

# Class Runtime (1.25.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ListRuntimesResponse.Runtime

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Runtime (1.25.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.25.0 (latest)  1.24.0  1.23.0  1.22.0  1.21.0  1.20.4  1.19.0  1.18.1  1.16.5  1.15.0  1.14.0  1.13.2  1.12.0  1.11.0  1.10.1  1.9.0  1.8.3  1.7.0  1.6.0  1.5.2  1.4.0  1.3.1  1.2.0  1.1.1  1.0.4  0.7.2  0.6.1  0.5.1  0.4.0  0.1.0 
    
    
    Runtime(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Describes a runtime and any special information (e.g., deprecation status) related to it.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
The name of the runtime, e.g., 'go113', 'nodejs12', etc.   
`display_name` |  `str`   
The user facing name, eg 'Go 1.13', 'Node.js 12', etc.   
`stage` |  `[google.cloud.functions_v2.types.ListRuntimesResponse.RuntimeStage](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ListRuntimesResponse.RuntimeStage)`   
The stage of life this runtime is in, e.g., BETA, GA, etc.   
`warnings` |  `MutableSequence[str]`   
Warning messages, e.g., a deprecation warning.   
`environment` |  `[google.cloud.functions_v2.types.Environment](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.Environment)`   
The environment for the runtime.   
`deprecation_date` |  `google.type.date_pb2.Date`   
Deprecation date for the runtime.   
`decommission_date` |  `google.type.date_pb2.Date`   
Decommission date for the runtime.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
