---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizationResult
title: Class SanitizationResult (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:00.690910+00:00
---

# Class SanitizationResult (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizationResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SanitizationResult (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.8  0.1.1 
    
    
    SanitizationResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Sanitization result after applying all the filters on input content.

## Attributes  
  
---  
**Name** | **Description**  
`filter_match_state` |  `[google.cloud.modelarmor_v1.types.FilterMatchState](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FilterMatchState)`   
Output only. Overall filter match state for Sanitization. The state can have below two values. 1) NO_MATCH_FOUND: No filters in configuration satisfy matching criteria. In other words, input passed all filters. 2) MATCH_FOUND: At least one filter in configuration satisfies matching. In other words, input did not pass one or more filters.   
`filter_results` |  `MutableMapping[str, [google.cloud.modelarmor_v1.types.FilterResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FilterResult)]`   
Output only. Results for all filters where the key is the filter name - either of "csam", "malicious_uris", "rai", "pi_and_jailbreak" ,"sdp".   
`invocation_result` |  `[google.cloud.modelarmor_v1.types.InvocationResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.InvocationResult)`   
Output only. A field indicating the outcome of the invocation, irrespective of match status. It can have the following three values: SUCCESS: All filters were executed successfully. PARTIAL: Some filters were skipped or failed execution. FAILURE: All filters were skipped or failed execution.   
`sanitization_metadata` |  `[google.cloud.modelarmor_v1.types.SanitizationResult.SanitizationMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizationResult.SanitizationMetadata)`   
Output only. Metadata related to Sanitization.   
  
## Classes 

### FilterResultsEntry
    
    
    FilterResultsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
### SanitizationMetadata
    
    
    SanitizationMetadata(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message describing Sanitization metadata.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
