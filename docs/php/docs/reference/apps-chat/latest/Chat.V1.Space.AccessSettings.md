---
url: https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.Space.AccessSettings
title: Google Apps Chat V1 Client - Class AccessSettings (0.28.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:36.104032+00:00
---

# Google Apps Chat V1 Client - Class AccessSettings (0.28.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.Space.AccessSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Apps Chat V1 Client - Class AccessSettings (0.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.28.0 (latest)  0.27.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.1  0.15.0  0.14.0  0.13.1  0.12.1  0.11.2  0.10.0  0.9.0  0.8.1  0.7.2  0.6.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Google Apps Chat V1 Client class AccessSettings.

Represents the [access setting](https://support.google.com/chat/answer/11971020) of the space.

Generated from protobuf message `google.chat.v1.Space.AccessSettings`

## Namespace

Google \ Apps \ Chat \ V1 \ Space

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ access_state` |  `int`   
Output only. Indicates the access state of the space.  
`↳ audience` |  `string`   
Optional. The resource name of the [target audience](https://support.google.com/a/answer/9934697) who can discover the space, join the space, and preview the messages in the space. If unset, only users or Google Groups who have been individually invited or added to the space can access it. For details, see [Make a space discoverable to a target audience](https://developers.google.com/workspace/chat/space-target-audience). Format: `audiences/{audience}` To use the default target audience for the Google Workspace organization, set to `audiences/default`. Reading the target audience supports: - [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) \- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with the `chat.app.spaces` scope. This field is not populated when using the `chat.bot` scope with [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app). Setting the target audience requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user).  
`↳ access_permission_settings` |  `[AccessPermissionSettings](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.Space.AccessPermissionSettings)`   
Optional. Access permission settings for the space. To set the target audience when creating a space, specify the `accessSettings.audience` field in your request.  
  
### getAccessState

Output only. Indicates the access state of the space.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [AccessState](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.Space.AccessSettings.AccessState).  
  
### setAccessState

Output only. Indicates the access state of the space.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [AccessState](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.Space.AccessSettings.AccessState).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAudience

Optional. The resource name of the [target audience](https://support.google.com/a/answer/9934697) who can discover the space, join the space, and preview the messages in the space. If unset, only users or Google Groups who have been individually invited or added to the space can access it. For details, see [Make a space discoverable to a target audience](https://developers.google.com/workspace/chat/space-target-audience).

Format: `audiences/{audience}` To use the default target audience for the Google Workspace organization, set to `audiences/default`. Reading the target audience supports:

  * [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
  * [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with the `chat.app.spaces` scope. This field is not populated when using the `chat.bot` scope with [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app). Setting the target audience requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user).



**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setAudience

Optional. The resource name of the [target audience](https://support.google.com/a/answer/9934697) who can discover the space, join the space, and preview the messages in the space. If unset, only users or Google Groups who have been individually invited or added to the space can access it. For details, see [Make a space discoverable to a target audience](https://developers.google.com/workspace/chat/space-target-audience).

Format: `audiences/{audience}` To use the default target audience for the Google Workspace organization, set to `audiences/default`. Reading the target audience supports:

  * [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user)
  * [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with the `chat.app.spaces` scope. This field is not populated when using the `chat.bot` scope with [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app). Setting the target audience requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user).



**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAccessPermissionSettings

Optional. Access permission settings for the space.

To set the target audience when creating a space, specify the `accessSettings.audience` field in your request.

**Returns**  
---  
**Type** | **Description**  
`[AccessPermissionSettings](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.Space.AccessPermissionSettings)|null` |   
  
### hasAccessPermissionSettings

### clearAccessPermissionSettings

### setAccessPermissionSettings

Optional. Access permission settings for the space.

To set the target audience when creating a space, specify the `accessSettings.audience` field in your request.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AccessPermissionSettings](https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.Space.AccessPermissionSettings)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
