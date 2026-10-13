---
url: https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.AllocationPolicy.InstanceFlexibilityPolicy
title: Class InstanceFlexibilityPolicy (0.22.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:35.075774+00:00
---

# Class InstanceFlexibilityPolicy (0.22.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.AllocationPolicy.InstanceFlexibilityPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class InstanceFlexibilityPolicy (0.22.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.4 (latest)  0.22.3  0.21.0  0.20.0  0.19.0  0.18.0  0.17.37  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.2  0.2.0  0.1.2 
    
    
    InstanceFlexibilityPolicy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Allows creating VMs from multiple types of machines. Instance flexibility configuration overrides instances configuration.

## Attribute  
  
---  
**Name** | **Description**  
`instance_selections` |  `MutableMapping[str, [google.cloud.batch_v1alpha.types.AllocationPolicy.InstanceSelection](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.AllocationPolicy.InstanceSelection)]`   
Required. Named instance selections configuring properties that the group will use when creating new VMs. The map key is a user-specified name for the instance selection. The key must be 1-63 characters long, and comply with `RFC1035 `__. Specifically, the key must consist of lowercase letters, numbers, and hyphens. The first character must be a lowercase letter, and the last character must be a lowercase letter or number. The maximum number of instance selections is 50. Exceeding this limit results in a validation error with code `INVALID_ARGUMENT`.   
  
## Classes 

### InstanceSelectionsEntry
    
    
    InstanceSelectionsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
