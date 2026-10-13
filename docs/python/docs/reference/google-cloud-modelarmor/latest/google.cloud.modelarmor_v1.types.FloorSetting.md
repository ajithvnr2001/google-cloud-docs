---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FloorSetting
title: Class FloorSetting (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:18:56.087283+00:00
---

# Class FloorSetting (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FloorSetting

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class FloorSetting (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.8  0.1.1 
    
    
    FloorSetting(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message describing FloorSetting resource

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The resource name.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. [Output only] Create timestamp   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. [Output only] Update timestamp   
`filter_config` |  `[google.cloud.modelarmor_v1.types.FilterConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FilterConfig)`   
Required. ModelArmor filter configuration.   
`enable_floor_setting_enforcement` |  `bool`   
Optional. Floor Settings enforcement status. This field is a member of `oneof`_ `_enable_floor_setting_enforcement`.   
`integrated_services` |  `MutableSequence[[google.cloud.modelarmor_v1.types.FloorSetting.IntegratedService](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FloorSetting.IntegratedService)]`   
Optional. List of integrated services for which the floor setting is applicable.   
`ai_platform_floor_setting` |  `[google.cloud.modelarmor_v1.types.AiPlatformFloorSetting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.AiPlatformFloorSetting)`   
Optional. AI Platform floor setting. This field is a member of `oneof`_ `_ai_platform_floor_setting`.   
`floor_setting_metadata` |  `[google.cloud.modelarmor_v1.types.FloorSetting.FloorSettingMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FloorSetting.FloorSettingMetadata)`   
Optional. Metadata for FloorSetting   
  
## Classes 

### FloorSettingMetadata
    
    
    FloorSettingMetadata(mapping=None, *, ignore_unknown_fields=False, **kwargs)

message describing FloorSetting Metadata

### IntegratedService
    
    
    IntegratedService(value)

Integrated service for which the floor setting is applicable.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
