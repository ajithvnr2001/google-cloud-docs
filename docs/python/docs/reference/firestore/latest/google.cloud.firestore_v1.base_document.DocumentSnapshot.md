---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document.DocumentSnapshot
title: Class DocumentSnapshot (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:34.252955+00:00
---

# Class DocumentSnapshot (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document.DocumentSnapshot

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DocumentSnapshot (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 
    
    
    DocumentSnapshot(reference, data, exists, read_time, create_time, update_time)

A snapshot of document data in a Firestore database.

This represents data retrieved at a specific time and may not contain all fields stored for the document (i.e. a hand-picked selection of fields may have been retrieved).

Instances of this class are not intended to be constructed by hand, rather they'll be returned as responses to various methods, such as xref_get.

## Parameters  
  
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
  
## Properties 

### exists

Existence flag.

Indicates if the document existed at the time this snapshot was retrieved.

**Returns**  
---  
**Type** | **Description**  
`bool` | The existence flag.  
  
### id

The document identifier (within its collection).

**Returns**  
---  
**Type** | **Description**  
`str` | The last component of the path of the document.  
  
### reference

Document reference corresponding to document that owns this data.

**Returns**  
---  
**Type** | **Description**  
`[DocumentReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.document.DocumentReference)` | A document reference corresponding to this document.  
  
## Methods 

### get
    
    
    get(field_path: str) -> typing.Any

Get a value from the snapshot data.

If the data is nested, for example:
    
    
    >>> snapshot.to_dict()
    {
        'top1': {
            'middle2': {
                'bottom3': 20,
                'bottom4': 22,
            },
            'middle5': True,
        },
        'top6': b' foo',
    }
    

a **field path** can be used to access the nested data. For example:
    
    
    >>> snapshot.get('top1')
    {
        'middle2': {
            'bottom3': 20,
            'bottom4': 22,
        },
        'middle5': True,
    }
    >>> snapshot.get('top1.middle2')
    {
        'bottom3': 20,
        'bottom4': 22,
    }
    >>> snapshot.get('top1.middle2.bottom3')
    20
    

See xref_field_path for more information on **field paths**.

A copy is returned since the data may contain mutable values, but the data stored in the snapshot must remain immutable.

**Parameter**  
---  
**Name** | **Description**  
`field_path` |  `str`   
A field path (`.`-delimited list of field names).  
**Exceptions**  
---  
**Type** | **Description**  
`KeyError` | If the `field_path` does not match nested data in the snapshot.  
**Returns**  
---  
**Type** | **Description**  
`Any or None` | (A copy of) the value stored for the `field_path` or None if snapshot document does not exist.  
  
### to_dict
    
    
    to_dict() -> typing.Optional[typing.Dict[str, typing.Any]]

Retrieve the data contained in this snapshot.

A copy is returned since the data may contain mutable values, but the data stored in the snapshot must remain immutable.

**Returns**  
---  
**Type** | **Description**  
`Dict[str, Any] or None` | The data in the snapshot. Returns None if reference does not exist.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
