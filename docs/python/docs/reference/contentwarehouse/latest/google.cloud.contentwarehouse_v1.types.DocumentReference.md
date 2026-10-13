---
url: https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.DocumentReference
title: Class DocumentReference (0.11.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:03.661399+00:00
---

# Class DocumentReference (0.11.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.DocumentReference

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DocumentReference (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.11.0  0.10.0  0.9.0  0.8.0  0.7.16  0.6.0  0.5.1  0.4.1  0.3.1  0.2.1  0.1.0 
    
    
    DocumentReference(mapping=None, *, ignore_unknown_fields=False, **kwargs)

References to the documents.

## Attributes  
  
---  
**Name** | **Description**  
`document_name` |  `str`   
Required. Name of the referenced document.   
`display_name` |  `str`   
display_name of the referenced document; this name does not need to be consistent to the display_name in the Document proto, depending on the ACL constraint.   
`snippet` |  `str`   
Stores the subset of the referenced document's content. This is useful to allow user peek the information of the referenced document.   
`document_is_folder` |  `bool`   
The document type of the document being referenced.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the document is last updated.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the document is created.   
`delete_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the document is deleted.   
`document_is_retention_folder` |  `bool`   
Document is a folder with retention policy.   
`document_is_legal_hold_folder` |  `bool`   
Document is a folder with legal hold.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
