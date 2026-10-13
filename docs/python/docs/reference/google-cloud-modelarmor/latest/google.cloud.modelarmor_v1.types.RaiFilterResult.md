---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterResult
title: Class RaiFilterResult (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:18:59.495900+00:00
---

# Class RaiFilterResult (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RaiFilterResult (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.8  0.1.1 
    
    
    RaiFilterResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Responsible AI Result.

## Attributes  
  
---  
**Name** | **Description**  
`execution_state` |  `[google.cloud.modelarmor_v1.types.FilterExecutionState](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FilterExecutionState)`   
Output only. Reports whether the RAI filter was successfully executed or not.   
`message_items` |  `MutableSequence[[google.cloud.modelarmor_v1.types.MessageItem](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.MessageItem)]`   
Optional messages corresponding to the result. A message can provide warnings or error details. For example, if execution state is skipped then this field provides related reason/explanation.   
`match_state` |  `[google.cloud.modelarmor_v1.types.FilterMatchState](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FilterMatchState)`   
Output only. Overall filter match state for RAI. Value is MATCH_FOUND if at least one RAI filter confidence level is equal to or higher than the confidence level defined in configuration.   
`rai_filter_type_results` |  `MutableMapping[str, [google.cloud.modelarmor_v1.types.RaiFilterResult.RaiFilterTypeResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.RaiFilterResult.RaiFilterTypeResult)]`   
The map of RAI filter results where key is RAI filter type - either of "sexually_explicit", "hate_speech", "harassment", "dangerous", "violence", "sexually_suggestive".   
  
## Classes 

### RaiFilterTypeResult
    
    
    RaiFilterTypeResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Detailed Filter result for each of the responsible AI Filter Types.

### RaiFilterTypeResultsEntry
    
    
    RaiFilterTypeResultsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
