---
url: https://docs.cloud.google.com/python/docs/reference/storageinsights/latest/google.cloud.storageinsights_v1.types.ReportConfig
title: Class ReportConfig (0.5.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:44.362681+00:00
---

# Class ReportConfig (0.5.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/storageinsights/latest/google.cloud.storageinsights_v1.types.ReportConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ReportConfig (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.5.0  0.4.0  0.3.0  0.2.0  0.1.16 
    
    
    ReportConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message describing ReportConfig object. ReportConfig is the configuration to generate reports. See <https://cloud.google.com/storage/docs/insights/using-inventory-reports#create-config-rest> for more details on how to set various fields. Next ID: 12

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
name of resource. It will be of form projects/  
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. [Output only] Create time stamp   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. [Output only] Update time stamp   
`frequency_options` |  `[google.cloud.storageinsights_v1.types.FrequencyOptions](https://docs.cloud.google.com/python/docs/reference/storageinsights/latest/google.cloud.storageinsights_v1.types.FrequencyOptions)`   
The frequency of report generation.   
`csv_options` |  `[google.cloud.storageinsights_v1.types.CSVOptions](https://docs.cloud.google.com/python/docs/reference/storageinsights/latest/google.cloud.storageinsights_v1.types.CSVOptions)`   
Options for CSV formatted reports. This field is a member of `oneof`_ `report_format`.   
`parquet_options` |  `[google.cloud.storageinsights_v1.types.ParquetOptions](https://docs.cloud.google.com/python/docs/reference/storageinsights/latest/google.cloud.storageinsights_v1.types.ParquetOptions)`   
Options for Parquet formatted reports. This field is a member of `oneof`_ `report_format`.   
`object_metadata_report_options` |  `[google.cloud.storageinsights_v1.types.ObjectMetadataReportOptions](https://docs.cloud.google.com/python/docs/reference/storageinsights/latest/google.cloud.storageinsights_v1.types.ObjectMetadataReportOptions)`   
Report for exporting object metadata. This field is a member of `oneof`_ `report_kind`.   
`labels` |  `MutableMapping[str, str]`   
Labels as key value pairs   
`display_name` |  `str`   
User provided display name which can be empty and limited to 256 characters that is editable.   
  
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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
