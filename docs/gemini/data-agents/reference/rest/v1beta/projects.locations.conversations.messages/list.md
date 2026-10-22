---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.conversations.messages/list/
title: Method: projects.locations.conversations.messages.list \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:59.944458+00:00
---

# Method: projects.locations.conversations.messages.list  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.conversations.messages/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  Method: projects.locations.conversations.messages.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * StorageMessage
    * JSON representation



Lists all messages for a given conversation.

### HTTP request

`GET https://geminidataanalytics.googleapis.com/v1beta/{parent=projects/*/locations/*/conversations/*}/messages`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The conversation to list messages under. Format: `projects/{project}/locations/{location}/conversations/{conversationId}`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. The max page size is `100`. All larger page sizes will be coerced to `100`. If unspecified, server will pick `50` as an appropriate default.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. Filtering results. See [AIP-160](https://google.aip.dev/160) for syntax.messages.list allows filtering by: * createTime (e.g., `createTime > "2025-01-28T06:51:56-08:00"`) * updateTime  
  
### Request body

The request body must be empty.

### Response body

Response for listing chat messages.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "messages": [
        {
          object ([StorageMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.conversations.messages/list#StorageMessage))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`messages[]` |  `object (`[StorageMessage](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.conversations.messages/list#StorageMessage)`)` The list of chat messages.  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## StorageMessage

A stored message containing user message or system message.

JSON representation  
---  
      
    
    {
      "messageId": string,
      "message": {
        object ([Message](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/Message))
      }
    }  
  
Fields  
---  
`messageId` |  `string` The unique resource name of a chat message.  
`message` |  `object (`[Message](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/Message)`)` The message content.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
