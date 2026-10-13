---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.chatMessages
title: REST Resource: projects.locations.instances.cases.chatMessages \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:37:31.216363+00:00
---

# REST Resource: projects.locations.instances.cases.chatMessages  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.chatMessages

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.cases.chatMessages Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ChatMessage
    * JSON representation
  * FileAttachment
    * JSON representation
  * Methods



## Resource: ChatMessage

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. ChatMessage represents a message in a case chat.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "author": string,
      "text": string,
      "attachments": [
        {
          object ([FileAttachment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.chatMessages#FileAttachment))
        }
      ],
      "pinned": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique name(ID) of the chat message. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}/chatMessage/{chatMessage}  
`createTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The message creation time.  
`author` |  `string` Output only. The message author.  
`text` |  `string` Required. The message text.  
`attachments[]` |  `object (`[FileAttachment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.chatMessages#FileAttachment)`)` Optional. The message attachments.  
`pinned` |  `boolean` Output only. Whether the message is pinned to the case wall  
  
## FileAttachment

Attachments

JSON representation  
---  
      
    
    {
      "name": string,
      "fileName": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the file attachment.  
`fileName` |  `string` Required. The file name of the attachment.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.chatMessages/create)`

|  Creates a new `ChatMessage` in a `Case`.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.chatMessages/get)`

|  Gets a single `ChatMessage` by its resource name.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.chatMessages/list)`

|  Lists `ChatMessages` for a specific `Case`.  
  
### `[pinMessage](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.chatMessages/pinMessage)`

|  Pins a specific `ChatMessage` to the `Case` wall.  
  
### `[unpinMessage](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.chatMessages/unpinMessage)`

|  Unpins a pinned `ChatMessage` from the `Case` wall.  
  
### `[unreadMessagesCount](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.chatMessages/unreadMessagesCount)`

|  Returns the number of `ChatMessages` in the Case chat that the current user has not yet read.  
  
### `[upload](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.chatMessages/upload)`

|  Creates a `ChatMessage` in a `Case` and uploads a `ChatMessageAttachment`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
