---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SetUriPatternDocumentDataRequest
title: Class SetUriPatternDocumentDataRequest (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:19.693808+00:00
---

# Class SetUriPatternDocumentDataRequest (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SetUriPatternDocumentDataRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SetUriPatternDocumentDataRequest (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    SetUriPatternDocumentDataRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Request message for SiteSearchEngineService.SetUriPatternDocumentData method.

## Attributes  
  
---  
**Name** | **Description**  
`site_search_engine` |  `str`   
Required. Full resource name of the SiteSearchEngine, such as `projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine`.   
`document_data_map` |  `MutableMapping[str, google.protobuf.struct_pb2.Struct]`   
Document data keyed by URI pattern. Each entry must be consistent with the Schema. For example: Schema = { "type": "object", "properties": { "Categories": { "type": "array", "items": { "retrievable": true, "type": "string" } } } document_data_map = { "www.url1.com/*": { "Categories": ["category1", "category2"] }, "www.url2.com/*": { "Categories": ["category3"] } }   
`empty_document_data_map` |  `bool`   
If true, clears the document data map. If true, SetUriPatternDocumentDataRequest.document_data_map must be empty.   
`schema` |  `google.protobuf.struct_pb2.Struct`   
Optional. If not provided, the current Schema is used. If provided, validates and updates the Schema. If validation fails, an error is returned.   
  
## Classes 

### DocumentDataMapEntry
    
    
    DocumentDataMapEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
