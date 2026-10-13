---
url: https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.ActionResponse
title: Google Apps Chat V1 Client - Class ActionResponse (0.28.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:17.382373+00:00
---

# Google Apps Chat V1 Client - Class ActionResponse (0.28.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.ActionResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Apps Chat V1 Client - Class ActionResponse (0.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.28.0 (latest)  0.27.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.1  0.15.0  0.14.0  0.13.1  0.12.1  0.11.2  0.10.0  0.9.0  0.8.1  0.7.2  0.6.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Google Apps Chat V1 Client class ActionResponse.

Parameters that a Chat app can use to configure how its response is posted.

Generated from protobuf message `google.chat.v1.ActionResponse`

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
`↳ type` |  `int`   
Input only. The type of Chat app response.  
`↳ url` |  `string`   
Input only. URL for users to authenticate or configure. (Only for `REQUEST_CONFIG` response types.)  
`↳ dialog_action` |  `[DialogAction](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.DialogAction)`   
Input only. A response to an interaction event related to a [dialog](https://developers.google.com/workspace/chat/dialogs). Must be accompanied by `ResponseType.Dialog`.  
`↳ updated_widget` |  `[ActionResponse\UpdatedWidget](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.ActionResponse.UpdatedWidget)`   
Input only. The response of the updated widget.  
  
### getType

Input only. The type of Chat app response.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [ResponseType](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.ActionResponse.ResponseType).  
  
### setType

Input only. The type of Chat app response.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [ResponseType](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.ActionResponse.ResponseType).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUrl

Input only. URL for users to authenticate or configure. (Only for `REQUEST_CONFIG` response types.)

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setUrl

Input only. URL for users to authenticate or configure. (Only for `REQUEST_CONFIG` response types.)

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDialogAction

Input only. A response to an interaction event related to a [dialog](https://developers.google.com/workspace/chat/dialogs). Must be accompanied by `ResponseType.Dialog`.

**Returns**  
---  
**Type** | **Description**  
`[DialogAction](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.DialogAction)|null` |   
  
### hasDialogAction

### clearDialogAction

### setDialogAction

Input only. A response to an interaction event related to a [dialog](https://developers.google.com/workspace/chat/dialogs). Must be accompanied by `ResponseType.Dialog`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[DialogAction](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.DialogAction)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdatedWidget

Input only. The response of the updated widget.

**Returns**  
---  
**Type** | **Description**  
`[ActionResponse\UpdatedWidget](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.ActionResponse.UpdatedWidget)|null` |   
  
### hasUpdatedWidget

### clearUpdatedWidget

### setUpdatedWidget

Input only. The response of the updated widget.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[ActionResponse\UpdatedWidget](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.ActionResponse.UpdatedWidget)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
