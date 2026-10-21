---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.conversations
title: REST Resource: projects.locations.conversations \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:42:53.018833+00:00
---

# REST Resource: projects.locations.conversations  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.conversations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  REST Resource: projects.locations.conversations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Conversation
    * JSON representation
  * Methods



## Resource: Conversation

Message for a conversation.

JSON representation  
---  
      
    
    {
      "name": string,
      "agents": [
        string
      ],
      "createTime": string,
      "lastUsedTime": string,
      "labels": {
        string: string,
        ...
      },
      "kmsKey": string,
      "memoryPaused": boolean
    }  
  
Fields  
---  
`name` |  `string` Optional. Identifier. The unique resource name of a conversation. Format: `projects/{project}/locations/{location}/conversations/{conversationId}` `{conversationId}` is the resource id and should be 63 characters or less and must match the format described in <https://google.aip.dev/122#resource-id-segments>Example: `projects/1234567890/locations/global/conversations/my-conversation`.It is recommended to skip setting this field during conversation creation as it will be inferred automatically and overwritten with the {parent}/conversations/{conversationId}.  
`agents[]` |  `string` Required. Agent(s) in the conversation. Currently, only one agent is supported. This field is repeated to allow for future support of multiple agents in a conversation. Format: `projects/{project}/locations/{location}/dataAgents/{agent}`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastUsedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp of the last used conversation.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Open-ended and user-defined labels that can be set by the client to tag a conversation (e.g. to filter conversations for specific surfaces/products).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`kmsKey` |  `string` Optional. Customer managed encryption key (CMEK) to use for encrypting the Conversation resources. Encryption will happen at Titan layer, we will pass the KMS key to Titan.Format: projects/{projectId}/locations/{location}/keyRings/{key_ring_name}/cryptoKeys/{key_name}.  
`memoryPaused` |  `boolean` Optional. Whether memory is paused for this conversation.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.conversations/create)`

|  Creates a new conversation to persist the conversation history.  
  
### `[delete](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.conversations/delete)`

|  Deletes a conversation.  
  
### `[get](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.conversations/get)`

|  Gets details of a single conversation by using conversation id and parent.  
  
### `[list](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.conversations/list)`

|  Lists all conversations for a given parent.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
