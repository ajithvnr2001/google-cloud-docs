---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document
title: Module base_document (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:34.006665+00:00
---

# Module base_document (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module base_document (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 

Classes for representing documents for the Google Cloud Firestore API.

## Classes 

### [BaseDocumentReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document.BaseDocumentReference)
    
    
    BaseDocumentReference(*path, **kwargs)

A reference to a document in a Firestore database.

The document may already exist or can be created by this class.

**Parameters**  
---  
**Name** | **Description**  
`path` |  `Tuple[str, ...]`   
The components in the document path. This is a series of strings representing each collection and sub-collection ID, as well as the document IDs for any documents that contain a sub-collection (as well as the base document).  
`kwargs` |  `dict`   
The keyword arguments for the constructor. The only supported keyword is `client` and it must be a [Client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client). It represents the client that created this document reference.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | if * the `path` is empty * there are an even number of elements * a collection ID in `path` is not a string * a document ID in `path` is not a string  
`TypeError` | If a keyword other than `client` is used.  
  
### [DocumentSnapshot](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document.DocumentSnapshot)
    
    
    DocumentSnapshot(reference, data, exists, read_time, create_time, update_time)

A snapshot of document data in a Firestore database.

This represents data retrieved at a specific time and may not contain all fields stored for the document (i.e. a hand-picked selection of fields may have been retrieved).

Instances of this class are not intended to be constructed by hand, rather they'll be returned as responses to various methods, such as xref_get.

**Parameters**  
---  
**Name** | **Description**  
`reference` |  `[DocumentReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.document.DocumentReference)`   
A document reference corresponding to the document that contains the data in this snapshot.  
`data` |  `Dict[str, Any]`   
The data retrieved in the snapshot.  
`exists` |  `bool`   
Indicates if the document existed at the time the snapshot was retrieved.  
`read_time` |  ``proto.datetime_helpers.DatetimeWithNanoseconds``   
The time that this snapshot was read from the server.  
`create_time` |  ``proto.datetime_helpers.DatetimeWithNanoseconds``   
The time that this document was created.  
`update_time` |  ``proto.datetime_helpers.DatetimeWithNanoseconds``   
The time that this document was last updated.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
