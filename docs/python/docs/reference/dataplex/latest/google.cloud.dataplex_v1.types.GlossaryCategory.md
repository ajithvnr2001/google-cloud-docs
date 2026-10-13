---
url: https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.GlossaryCategory
title: Class GlossaryCategory (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:41.282718+00:00
---

# Class GlossaryCategory (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.GlossaryCategory

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GlossaryCategory (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.2  2.9.0  2.8.0  2.7.1  2.6.0  2.5.0  2.4.0  2.3.1  2.2.2  2.1.0  2.0.1  1.13.0  1.12.3  1.11.0  1.10.0  1.9.0  1.8.1  1.7.0  1.6.2  1.5.1  1.4.3  1.3.0  1.2.0  1.1.3  1.0.1  0.2.1  0.1.0 
    
    
    GlossaryCategory(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A GlossaryCategory represents a collection of GlossaryCategories and GlossaryTerms within a Glossary that are related to each other.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. Identifier. The resource name of the GlossaryCategory. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/categories/{category_id}   
`uid` |  `str`   
Output only. System generated unique id for the GlossaryCategory. This ID will be different if the GlossaryCategory is deleted and re-created with the same name.   
`display_name` |  `str`   
Optional. User friendly display name of the GlossaryCategory. This is user-mutable. This will be same as the GlossaryCategoryId, if not specified.   
`description` |  `str`   
Optional. The user-mutable description of the GlossaryCategory.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time at which the GlossaryCategory was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time at which the GlossaryCategory was last updated.   
`labels` |  `MutableMapping[str, str]`   
Optional. User-defined labels for the GlossaryCategory.   
`parent` |  `str`   
Required. The immediate parent of the GlossaryCategory in the resource-hierarchy. It can either be a Glossary or a GlossaryCategory. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id} OR projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/categories/{category_id}   
  
## Classes 

### LabelsEntry
    
    
    LabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
