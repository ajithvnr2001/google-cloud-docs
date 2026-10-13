---
url: https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.DriveLinkData
title: Google Apps Chat V1 Client - Class DriveLinkData (0.28.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:38:10.299675+00:00
---

# Google Apps Chat V1 Client - Class DriveLinkData (0.28.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.DriveLinkData

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Apps Chat V1 Client - Class DriveLinkData (0.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.28.0 (latest)  0.27.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.1  0.15.0  0.14.0  0.13.1  0.12.1  0.11.2  0.10.0  0.9.0  0.8.1  0.7.2  0.6.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Google Apps Chat V1 Client class DriveLinkData.

Data for Google Drive links.

Generated from protobuf message `google.chat.v1.DriveLinkData`

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
`↳ drive_data_ref` |  `[DriveDataRef](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.DriveDataRef)`   
A [DriveDataRef](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages.attachments#drivedataref) which references a Google Drive file.  
`↳ mime_type` |  `string`   
The mime type of the linked Google Drive resource.  
  
### getDriveDataRef

A [DriveDataRef](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages.attachments#drivedataref) which references a Google Drive file.

**Returns**  
---  
**Type** | **Description**  
`[DriveDataRef](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.DriveDataRef)|null` |   
  
### hasDriveDataRef

### clearDriveDataRef

### setDriveDataRef

A [DriveDataRef](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages.attachments#drivedataref) which references a Google Drive file.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[DriveDataRef](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.DriveDataRef)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMimeType

The mime type of the linked Google Drive resource.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setMimeType

The mime type of the linked Google Drive resource.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
