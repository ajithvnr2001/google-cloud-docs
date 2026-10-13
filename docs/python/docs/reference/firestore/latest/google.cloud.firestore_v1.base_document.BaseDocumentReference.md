---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document.BaseDocumentReference
title: Class BaseDocumentReference (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:34.090437+00:00
---

# Class BaseDocumentReference (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document.BaseDocumentReference

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BaseDocumentReference (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 
    
    
    BaseDocumentReference(*path, **kwargs)

A reference to a document in a Firestore database.

The document may already exist or can be created by this class.

## Parameters  
  
---  
**Name** | **Description**  
`path` |  `Tuple[str, ...]`   
The components in the document path. This is a series of strings representing each collection and sub-collection ID, as well as the document IDs for any documents that contain a sub-collection (as well as the base document).  
`kwargs` |  `dict`   
The keyword arguments for the constructor. The only supported keyword is `client` and it must be a [Client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client). It represents the client that created this document reference.  
  
## Properties 

### id

The document identifier (within its collection).

**Returns**  
---  
**Type** | **Description**  
`str` | The last component of the path.  
  
### parent

Collection that owns the current document.

**Returns**  
---  
**Type** | **Description**  
`[CollectionReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.collection.CollectionReference)` | The parent collection.  
  
### path

Database-relative for this document.

**Returns**  
---  
**Type** | **Description**  
`str` | The document's relative path.  
  
## Methods 

### __copy__
    
    
    __copy__()

Shallow copy the instance.

We leave the client "as-is" but tuple-unpack the path.

**Returns**  
---  
**Type** | **Description**  
`.DocumentReference` | A copy of the current document.  
  
### __deepcopy__
    
    
    __deepcopy__(unused_memo)

Deep copy the instance.

This isn't a true deep copy, wee leave the client "as-is" but tuple-unpack the path.

**Returns**  
---  
**Type** | **Description**  
`.DocumentReference` | A copy of the current document.  
  
### __eq__
    
    
    __eq__(other)

Equality check against another instance.

**Parameter**  
---  
**Name** | **Description**  
`other` |  `Any`   
A value to compare against.  
**Returns**  
---  
**Type** | **Description**  
`Union[bool, NotImplementedType]` | Indicating if the values are equal.  
  
### __ne__
    
    
    __ne__(other)

Inequality check against another instance.

**Parameter**  
---  
**Name** | **Description**  
`other` |  `Any`   
A value to compare against.  
**Returns**  
---  
**Type** | **Description**  
`Union[bool, NotImplementedType]` | Indicating if the values are not equal.  
  
### collection
    
    
    collection(collection_id: str)

Create a sub-collection underneath the current document.

**Parameter**  
---  
**Name** | **Description**  
`collection_id` |  `str`   
The sub-collection identifier (sometimes referred to as the "kind").  
**Returns**  
---  
**Type** | **Description**  
`[CollectionReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.collection.CollectionReference)` | The child collection.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
