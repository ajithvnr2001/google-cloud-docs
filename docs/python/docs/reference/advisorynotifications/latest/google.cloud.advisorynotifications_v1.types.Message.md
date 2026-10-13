---
url: https://docs.cloud.google.com/python/docs/reference/advisorynotifications/latest/google.cloud.advisorynotifications_v1.types.Message
title: Class Message (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:23.585920+00:00
---

# Class Message (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/advisorynotifications/latest/google.cloud.advisorynotifications_v1.types.Message

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Message (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.16  0.2.1  0.1.1 
    
    
    Message(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A message which contains notification details.

## Attributes  
  
---  
**Name** | **Description**  
`body` |  `[google.cloud.advisorynotifications_v1.types.Message.Body](https://docs.cloud.google.com/python/docs/reference/advisorynotifications/latest/google.cloud.advisorynotifications_v1.types.Message.Body)`   
The message content.   
`attachments` |  `MutableSequence[[google.cloud.advisorynotifications_v1.types.Attachment](https://docs.cloud.google.com/python/docs/reference/advisorynotifications/latest/google.cloud.advisorynotifications_v1.types.Attachment)]`   
The attachments to download.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
The Message creation timestamp.   
`localization_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Time when Message was localized   
  
## Classes 

### Body
    
    
    Body(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A message body containing text.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
