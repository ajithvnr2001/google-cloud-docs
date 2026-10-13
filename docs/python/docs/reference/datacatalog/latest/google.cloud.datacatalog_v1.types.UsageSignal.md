---
url: https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.UsageSignal
title: Class UsageSignal (3.32.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:51.412527+00:00
---

# Class UsageSignal (3.32.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.UsageSignal

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class UsageSignal (3.32.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.32.0 (latest)  3.31.0  3.30.0  3.29.0  3.28.0  3.27.1  3.26.1  3.25.1  3.24.1  3.23.0  3.22.0  3.21.1  3.20.1  3.19.1  3.18.3  3.17.2  3.16.0  3.15.1  3.14.0  3.13.1  3.12.0  3.11.1  3.10.0  3.9.3  3.8.1  3.7.1  3.6.2  3.5.0  3.4.3  3.3.2  3.2.1  3.1.1  3.0.0  2.0.2  1.0.2  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0 
    
    
    UsageSignal(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The set of all usage signals that Data Catalog stores.

Note: Usually, these signals are updated daily. In rare cases, an update may fail but will be performed again on the next day.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
The end timestamp of the duration of usage statistics.   
`usage_within_time_range` |  `MutableMapping[str, [google.cloud.datacatalog_v1.types.UsageStats](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.UsageStats)]`   
Output only. BigQuery usage statistics over each of the predefined time ranges. Supported time ranges are `{"24H", "7D", "30D"}`.   
`common_usage_within_time_range` |  `MutableMapping[str, [google.cloud.datacatalog_v1.types.CommonUsageStats](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.types.CommonUsageStats)]`   
Common usage statistics over each of the predefined time ranges. Supported time ranges are `{"24H", "7D", "30D", "Lifetime"}`.   
`favorite_count` |  `int`   
Favorite count in the source system. This field is a member of `oneof`_ `_favorite_count`.   
  
## Classes 

### CommonUsageWithinTimeRangeEntry
    
    
    CommonUsageWithinTimeRangeEntry(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

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
  
### UsageWithinTimeRangeEntry
    
    
    UsageWithinTimeRangeEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
