---
url: https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.UpdateSectionRequest
title: Google Apps Chat V1 Client - Class UpdateSectionRequest (0.28.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:41:35.578848+00:00
---

# Google Apps Chat V1 Client - Class UpdateSectionRequest (0.28.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.UpdateSectionRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Apps Chat V1 Client - Class UpdateSectionRequest (0.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.28.0 (latest)  0.27.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.1  0.15.0  0.14.0  0.13.1  0.12.1  0.11.2  0.10.0  0.9.0  0.8.1  0.7.2  0.6.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Google Apps Chat V1 Client class UpdateSectionRequest.

Request message for updating a section.

Generated from protobuf message `google.chat.v1.UpdateSectionRequest`

## Namespace

Google \ Apps \ Chat \ V1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ section` |  `[Section](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.Section)`   
Required. The section to update.  
`↳ update_mask` |  `Google\Protobuf\FieldMask`   
Required. The mask to specify which fields to update. Currently supported field paths: - `display_name`  
  
### getSection

Required. The section to update.

**Returns**  
---  
**Type** | **Description**  
`[Section](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.Section)|null` |   
  
### hasSection

### clearSection

### setSection

Required. The section to update.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Section](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.Section)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateMask

Required. The mask to specify which fields to update.

Currently supported field paths:

  * `display_name`



**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\FieldMask|null` |   
  
### hasUpdateMask

### clearUpdateMask

### setUpdateMask

Required. The mask to specify which fields to update.

Currently supported field paths:

  * `display_name`



**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\FieldMask`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameters**  
---  
**Name** | **Description**  
`section` |  `[Section](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.Section)`   
Required. The section to update.  
`updateMask` |  `Google\Protobuf\FieldMask`   
Required. The mask to specify which fields to update. Currently supported field paths:

  * `display_name`

  
**Returns**  
---  
**Type** | **Description**  
`[UpdateSectionRequest](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.UpdateSectionRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
