---
url: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SavedQuery
title: Class SavedQuery (4.5.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:36.297627+00:00
---

# Class SavedQuery (4.5.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SavedQuery

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SavedQuery (4.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.5.0 (latest)  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.30.1  3.29.2  3.28.0  3.27.1  3.26.4  3.25.1  3.24.3  3.23.0  3.22.0  3.21.0  3.20.1  3.19.1  3.18.1  3.17.1  3.16.0  3.15.0  3.14.2  3.13.1  3.12.0  3.11.0  3.10.0  3.9.1  3.8.1  3.7.1  3.6.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.0  2.2.2  2.1.0  2.0.0  1.3.2  1.2.0  1.1.0  1.0.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0 
    
    
    SavedQuery(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A saved query which can be shared with others or used later.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
The resource name of the saved query. The format must be: \- projects/project_number/savedQueries/saved_query_id \- folders/folder_number/savedQueries/saved_query_id \- organizations/organization_number/savedQueries/saved_query_id   
`description` |  `str`   
The description of this saved query. This value should be fewer than 255 characters.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The create time of this saved query.   
`creator` |  `str`   
Output only. The account's email address who has created this saved query.   
`last_update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The last update time of this saved query.   
`last_updater` |  `str`   
Output only. The account's email address who has updated this saved query most recently.   
`labels` |  `MutableMapping[str, str]`   
Labels applied on the resource. This value should not contain more than 10 entries. The key and value of each entry must be non-empty and fewer than 64 characters.   
`content` |  `[google.cloud.asset_v1.types.SavedQuery.QueryContent](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SavedQuery.QueryContent)`   
The query content.   
  
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
  
### QueryContent
    
    
    QueryContent(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The query content.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
