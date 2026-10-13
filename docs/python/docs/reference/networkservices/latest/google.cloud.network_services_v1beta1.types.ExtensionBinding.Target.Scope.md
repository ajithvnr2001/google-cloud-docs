---
url: https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.ExtensionBinding.Target.Scope
title: Class Scope (0.10.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:33.668242+00:00
---

# Class Scope (0.10.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.ExtensionBinding.Target.Scope

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Scope (0.10.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.4 (latest)  0.10.3  0.9.0  0.8.0  0.7.0  0.6.0  0.5.24  0.4.1  0.3.0  0.2.2  0.1.1 
    
    
    Scope(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Specifies the scope of resources to which this binding should attach.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. Parent resource name specification, in the format: `projects/{project_number}`.   
`resource_types` |  `MutableSequence[[google.cloud.network_services_v1beta1.types.ExtensionBinding.Target.Scope.ResourceType](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.ExtensionBinding.Target.Scope.ResourceType)]`   
Required. Type of the resource to which the binding should attach. Limited to 1 resource type.   
  
## Classes 

### ResourceType
    
    
    ResourceType(value)

Resource types that should be targeted by the binding.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
