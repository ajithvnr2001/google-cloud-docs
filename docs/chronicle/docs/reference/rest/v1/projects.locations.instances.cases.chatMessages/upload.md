---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.chatMessages/upload/
title: Method: chatMessages.upload \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:37:34.416654+00:00
---

# Method: chatMessages.upload  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.chatMessages/upload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: chatMessages.upload Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.cases.chatMessages.upload

Creates a `ChatMessage` in a `Case` and uploads a `ChatMessageAttachment`. Use this method to share files (up to 100MB) along with a descriptive message.

### HTTP request

  * Upload URI, for media upload requests:  
`POST https://{endpoint}/upload/v1/{parent}/chatMessages:createWithAttachment`
  * Metadata URI, for metadata-only requests:  
`POST https://{endpoint}/v1/{parent}/chatMessages:createWithAttachment`



Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The instance to create the Casechat for. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}/chatMessage/{chatMessage}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "text": string,
      "media": {
        object ([Media](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/MediaResponseInfo#Media))
      },
      "mediaInfo": {
        object ([MediaRequestInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/MediaRequestInfo))
      }
    }  
  
Fields  
---  
`text` |  `string` Optional. This is a required field.  
`media` |  `object (`[Media](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/MediaResponseInfo#Media)`)` The content of the attachment.  
`mediaInfo` |  `object (`[MediaRequestInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/MediaRequestInfo)`)` The media request info.  
  
### Response body

Response model for create a chat-message with an attachment operation

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "chatMessage": {
        object ([ChatMessage](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.chatMessages#ChatMessage))
      },
      "mediaInfo": {
        object ([MediaResponseInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/MediaResponseInfo))
      }
    }  
  
Fields  
---  
`chatMessage` |  `object (`[ChatMessage](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.chatMessages#ChatMessage)`)` The updated localization  
`mediaInfo` |  `object (`[MediaResponseInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/MediaResponseInfo)`)` The media response info.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.chatMessages.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
