---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apphub/latest/google.cloud.apphub_v1.types.WorkloadProperties
title: Class WorkloadProperties (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:53.754265+00:00
---

# Class WorkloadProperties (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apphub/latest/google.cloud.apphub_v1.types.WorkloadProperties

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class WorkloadProperties (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    WorkloadProperties(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Properties of an underlying compute resource represented by the Workload.

## Attributes  
  
---  
**Name** | **Description**  
`gcp_project` |  `str`   
Output only. The service project identifier that the underlying cloud resource resides in. Empty for non-cloud resources.   
`location` |  `str`   
Output only. The location that the underlying compute resource resides in (for example, us-west1).   
`zone` |  `str`   
Output only. The location that the underlying compute resource resides in if it is zonal (for example, us-west1-a).   
`functional_type` |  `[google.cloud.apphub_v1.types.FunctionalType](https://docs.cloud.google.com/python/docs/reference/google-cloud-apphub/latest/google.cloud.apphub_v1.types.FunctionalType)`   
Output only. The type of the workload.   
`extended_metadata` |  `MutableMapping[str, [google.cloud.apphub_v1.types.ExtendedMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-apphub/latest/google.cloud.apphub_v1.types.ExtendedMetadata)]`   
Output only. Additional metadata specific to the resource type. The key is a string that identifies the type of metadata and the value is the metadata contents specific to that type. Key format: `apphub.googleapis.com/{metadataType}`  
`identity` |  `[google.cloud.apphub_v1.types.Identity](https://docs.cloud.google.com/python/docs/reference/google-cloud-apphub/latest/google.cloud.apphub_v1.types.Identity)`   
Output only. The identity associated with the workload.   
  
## Classes 

### ExtendedMetadataEntry
    
    
    ExtendedMetadataEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
