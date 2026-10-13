---
url: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.datachatservice-class
title: Class protos.google.cloud.geminidataanalytics.v1.DataChatService (0.13.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:37:35.982392+00:00
---

# Class protos.google.cloud.geminidataanalytics.v1.DataChatService (0.13.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.datachatservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.geminidataanalytics.v1.DataChatService (0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.13.0  0.7.0  0.6.0  0.4.0  0.2.0 

Represents a DataChatService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.geminidataanalytics.v1.DataChatService

## Package

[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DataChatService service.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
  
## Methods 

### chat(request, callback)
    
    
    public chat(request: google.cloud.geminidataanalytics.v1.IChatRequest, callback: google.cloud.geminidataanalytics.v1.DataChatService.ChatCallback): void;

Calls Chat.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IChatRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.ichatrequest)`   
ChatRequest message or plain object  
`callback` |  `[ChatCallback](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)`   
Node-style callback called with the error, if any, and Message  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### chat(request)
    
    
    public chat(request: google.cloud.geminidataanalytics.v1.IChatRequest): Promise<google.cloud.geminidataanalytics.v1.Message>;

Calls Chat.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IChatRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.ichatrequest)`   
ChatRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.geminidataanalytics.v1.Message](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.message)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DataChatService;

Creates new DataChatService service using the specified rpc implementation.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
**Returns**  
---  
**Type** | **Description**  
`[DataChatService](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.datachatservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createConversation(request, callback)
    
    
    public createConversation(request: google.cloud.geminidataanalytics.v1.ICreateConversationRequest, callback: google.cloud.geminidataanalytics.v1.DataChatService.CreateConversationCallback): void;

Calls CreateConversation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.icreateconversationrequest)`   
CreateConversationRequest message or plain object  
`callback` |  `[CreateConversationCallback](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)`   
Node-style callback called with the error, if any, and Conversation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConversation(request)
    
    
    public createConversation(request: google.cloud.geminidataanalytics.v1.ICreateConversationRequest): Promise<google.cloud.geminidataanalytics.v1.Conversation>;

Calls CreateConversation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.icreateconversationrequest)`   
CreateConversationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.geminidataanalytics.v1.Conversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.conversation)>` | Promise  
  
### deleteConversation(request, callback)
    
    
    public deleteConversation(request: google.cloud.geminidataanalytics.v1.IDeleteConversationRequest, callback: google.cloud.geminidataanalytics.v1.DataChatService.DeleteConversationCallback): void;

Calls DeleteConversation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.ideleteconversationrequest)`   
DeleteConversationRequest message or plain object  
`callback` |  `[DeleteConversationCallback](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConversation(request)
    
    
    public deleteConversation(request: google.cloud.geminidataanalytics.v1.IDeleteConversationRequest): Promise<google.protobuf.Empty>;

Calls DeleteConversation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.ideleteconversationrequest)`   
DeleteConversationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.protobuf.empty)>` | Promise  
  
### getConversation(request, callback)
    
    
    public getConversation(request: google.cloud.geminidataanalytics.v1.IGetConversationRequest, callback: google.cloud.geminidataanalytics.v1.DataChatService.GetConversationCallback): void;

Calls GetConversation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.igetconversationrequest)`   
GetConversationRequest message or plain object  
`callback` |  `[GetConversationCallback](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)`   
Node-style callback called with the error, if any, and Conversation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConversation(request)
    
    
    public getConversation(request: google.cloud.geminidataanalytics.v1.IGetConversationRequest): Promise<google.cloud.geminidataanalytics.v1.Conversation>;

Calls GetConversation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.igetconversationrequest)`   
GetConversationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.geminidataanalytics.v1.Conversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.conversation)>` | Promise  
  
### listConversations(request, callback)
    
    
    public listConversations(request: google.cloud.geminidataanalytics.v1.IListConversationsRequest, callback: google.cloud.geminidataanalytics.v1.DataChatService.ListConversationsCallback): void;

Calls ListConversations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.ilistconversationsrequest)`   
ListConversationsRequest message or plain object  
`callback` |  `[ListConversationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)`   
Node-style callback called with the error, if any, and ListConversationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConversations(request)
    
    
    public listConversations(request: google.cloud.geminidataanalytics.v1.IListConversationsRequest): Promise<google.cloud.geminidataanalytics.v1.ListConversationsResponse>;

Calls ListConversations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.ilistconversationsrequest)`   
ListConversationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.geminidataanalytics.v1.ListConversationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.listconversationsresponse)>` | Promise  
  
### listMessages(request, callback)
    
    
    public listMessages(request: google.cloud.geminidataanalytics.v1.IListMessagesRequest, callback: google.cloud.geminidataanalytics.v1.DataChatService.ListMessagesCallback): void;

Calls ListMessages.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMessagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.ilistmessagesrequest)`   
ListMessagesRequest message or plain object  
`callback` |  `[ListMessagesCallback](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)`   
Node-style callback called with the error, if any, and ListMessagesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMessages(request)
    
    
    public listMessages(request: google.cloud.geminidataanalytics.v1.IListMessagesRequest): Promise<google.cloud.geminidataanalytics.v1.ListMessagesResponse>;

Calls ListMessages.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMessagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.ilistmessagesrequest)`   
ListMessagesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.geminidataanalytics.v1.ListMessagesResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.listmessagesresponse)>` | Promise  
  
### updateConversation(request, callback)
    
    
    public updateConversation(request: google.cloud.geminidataanalytics.v1.IUpdateConversationRequest, callback: google.cloud.geminidataanalytics.v1.DataChatService.UpdateConversationCallback): void;

Calls UpdateConversation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.iupdateconversationrequest)`   
UpdateConversationRequest message or plain object  
`callback` |  `[UpdateConversationCallback](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)`   
Node-style callback called with the error, if any, and Conversation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConversation(request)
    
    
    public updateConversation(request: google.cloud.geminidataanalytics.v1.IUpdateConversationRequest): Promise<google.cloud.geminidataanalytics.v1.Conversation>;

Calls UpdateConversation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.iupdateconversationrequest)`   
UpdateConversationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.geminidataanalytics.v1.Conversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.conversation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
