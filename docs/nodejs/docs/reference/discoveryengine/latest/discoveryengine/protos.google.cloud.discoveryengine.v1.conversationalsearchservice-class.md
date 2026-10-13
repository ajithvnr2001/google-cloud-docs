---
url: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.conversationalsearchservice-class
title: Class protos.google.cloud.discoveryengine.v1.ConversationalSearchService (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:41.011538+00:00
---

# Class protos.google.cloud.discoveryengine.v1.ConversationalSearchService (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.conversationalsearchservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.discoveryengine.v1.ConversationalSearchService (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  3.3.0  3.1.0  2.9.0  2.8.0  2.6.0  2.2.0  2.0.1  1.14.0  1.10.0  1.9.0  1.7.0  1.6.0  1.4.1  1.3.1  1.2.0  1.0.0  0.6.0  0.5.0  0.3.1  0.2.0 

Represents a ConversationalSearchService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.discoveryengine.v1.ConversationalSearchService

## Package

[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ConversationalSearchService service.

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

### answerQuery(request, callback)
    
    
    public answerQuery(request: google.cloud.discoveryengine.v1.IAnswerQueryRequest, callback: google.cloud.discoveryengine.v1.ConversationalSearchService.AnswerQueryCallback): void;

Calls AnswerQuery.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnswerQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ianswerqueryrequest)`   
AnswerQueryRequest message or plain object  
`callback` |  `[AnswerQueryCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and AnswerQueryResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### answerQuery(request)
    
    
    public answerQuery(request: google.cloud.discoveryengine.v1.IAnswerQueryRequest): Promise<google.cloud.discoveryengine.v1.AnswerQueryResponse>;

Calls AnswerQuery.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAnswerQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ianswerqueryrequest)`   
AnswerQueryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1.AnswerQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.answerqueryresponse)>` | Promise  
  
### converseConversation(request, callback)
    
    
    public converseConversation(request: google.cloud.discoveryengine.v1.IConverseConversationRequest, callback: google.cloud.discoveryengine.v1.ConversationalSearchService.ConverseConversationCallback): void;

Calls ConverseConversation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IConverseConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.iconverseconversationrequest)`   
ConverseConversationRequest message or plain object  
`callback` |  `[ConverseConversationCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and ConverseConversationResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### converseConversation(request)
    
    
    public converseConversation(request: google.cloud.discoveryengine.v1.IConverseConversationRequest): Promise<google.cloud.discoveryengine.v1.ConverseConversationResponse>;

Calls ConverseConversation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IConverseConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.iconverseconversationrequest)`   
ConverseConversationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1.ConverseConversationResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.converseconversationresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ConversationalSearchService;

Creates new ConversationalSearchService service using the specified rpc implementation.

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
`[ConversationalSearchService](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.conversationalsearchservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createConversation(request, callback)
    
    
    public createConversation(request: google.cloud.discoveryengine.v1.ICreateConversationRequest, callback: google.cloud.discoveryengine.v1.ConversationalSearchService.CreateConversationCallback): void;

Calls CreateConversation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.icreateconversationrequest)`   
CreateConversationRequest message or plain object  
`callback` |  `[CreateConversationCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and Conversation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConversation(request)
    
    
    public createConversation(request: google.cloud.discoveryengine.v1.ICreateConversationRequest): Promise<google.cloud.discoveryengine.v1.Conversation>;

Calls CreateConversation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.icreateconversationrequest)`   
CreateConversationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1.Conversation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.conversation-class)>` | Promise  
  
### createSession(request, callback)
    
    
    public createSession(request: google.cloud.discoveryengine.v1.ICreateSessionRequest, callback: google.cloud.discoveryengine.v1.ConversationalSearchService.CreateSessionCallback): void;

Calls CreateSession.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.icreatesessionrequest)`   
CreateSessionRequest message or plain object  
`callback` |  `[CreateSessionCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and Session  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSession(request)
    
    
    public createSession(request: google.cloud.discoveryengine.v1.ICreateSessionRequest): Promise<google.cloud.discoveryengine.v1.Session>;

Calls CreateSession.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.icreatesessionrequest)`   
CreateSessionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1.Session](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.session-class)>` | Promise  
  
### deleteConversation(request, callback)
    
    
    public deleteConversation(request: google.cloud.discoveryengine.v1.IDeleteConversationRequest, callback: google.cloud.discoveryengine.v1.ConversationalSearchService.DeleteConversationCallback): void;

Calls DeleteConversation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ideleteconversationrequest)`   
DeleteConversationRequest message or plain object  
`callback` |  `[DeleteConversationCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConversation(request)
    
    
    public deleteConversation(request: google.cloud.discoveryengine.v1.IDeleteConversationRequest): Promise<google.protobuf.Empty>;

Calls DeleteConversation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ideleteconversationrequest)`   
DeleteConversationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty)>` | Promise  
  
### deleteSession(request, callback)
    
    
    public deleteSession(request: google.cloud.discoveryengine.v1.IDeleteSessionRequest, callback: google.cloud.discoveryengine.v1.ConversationalSearchService.DeleteSessionCallback): void;

Calls DeleteSession.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ideletesessionrequest)`   
DeleteSessionRequest message or plain object  
`callback` |  `[DeleteSessionCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSession(request)
    
    
    public deleteSession(request: google.cloud.discoveryengine.v1.IDeleteSessionRequest): Promise<google.protobuf.Empty>;

Calls DeleteSession.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ideletesessionrequest)`   
DeleteSessionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty)>` | Promise  
  
### getAnswer(request, callback)
    
    
    public getAnswer(request: google.cloud.discoveryengine.v1.IGetAnswerRequest, callback: google.cloud.discoveryengine.v1.ConversationalSearchService.GetAnswerCallback): void;

Calls GetAnswer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnswerRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.igetanswerrequest)`   
GetAnswerRequest message or plain object  
`callback` |  `[GetAnswerCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and Answer  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAnswer(request)
    
    
    public getAnswer(request: google.cloud.discoveryengine.v1.IGetAnswerRequest): Promise<google.cloud.discoveryengine.v1.Answer>;

Calls GetAnswer.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAnswerRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.igetanswerrequest)`   
GetAnswerRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1.Answer](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.answer-class)>` | Promise  
  
### getConversation(request, callback)
    
    
    public getConversation(request: google.cloud.discoveryengine.v1.IGetConversationRequest, callback: google.cloud.discoveryengine.v1.ConversationalSearchService.GetConversationCallback): void;

Calls GetConversation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.igetconversationrequest)`   
GetConversationRequest message or plain object  
`callback` |  `[GetConversationCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and Conversation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConversation(request)
    
    
    public getConversation(request: google.cloud.discoveryengine.v1.IGetConversationRequest): Promise<google.cloud.discoveryengine.v1.Conversation>;

Calls GetConversation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.igetconversationrequest)`   
GetConversationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1.Conversation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.conversation-class)>` | Promise  
  
### getSession(request, callback)
    
    
    public getSession(request: google.cloud.discoveryengine.v1.IGetSessionRequest, callback: google.cloud.discoveryengine.v1.ConversationalSearchService.GetSessionCallback): void;

Calls GetSession.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.igetsessionrequest)`   
GetSessionRequest message or plain object  
`callback` |  `[GetSessionCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and Session  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSession(request)
    
    
    public getSession(request: google.cloud.discoveryengine.v1.IGetSessionRequest): Promise<google.cloud.discoveryengine.v1.Session>;

Calls GetSession.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.igetsessionrequest)`   
GetSessionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1.Session](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.session-class)>` | Promise  
  
### listConversations(request, callback)
    
    
    public listConversations(request: google.cloud.discoveryengine.v1.IListConversationsRequest, callback: google.cloud.discoveryengine.v1.ConversationalSearchService.ListConversationsCallback): void;

Calls ListConversations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ilistconversationsrequest)`   
ListConversationsRequest message or plain object  
`callback` |  `[ListConversationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and ListConversationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConversations(request)
    
    
    public listConversations(request: google.cloud.discoveryengine.v1.IListConversationsRequest): Promise<google.cloud.discoveryengine.v1.ListConversationsResponse>;

Calls ListConversations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ilistconversationsrequest)`   
ListConversationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1.ListConversationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.listconversationsresponse)>` | Promise  
  
### listSessions(request, callback)
    
    
    public listSessions(request: google.cloud.discoveryengine.v1.IListSessionsRequest, callback: google.cloud.discoveryengine.v1.ConversationalSearchService.ListSessionsCallback): void;

Calls ListSessions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ilistsessionsrequest)`   
ListSessionsRequest message or plain object  
`callback` |  `[ListSessionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSessionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSessions(request)
    
    
    public listSessions(request: google.cloud.discoveryengine.v1.IListSessionsRequest): Promise<google.cloud.discoveryengine.v1.ListSessionsResponse>;

Calls ListSessions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ilistsessionsrequest)`   
ListSessionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1.ListSessionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.listsessionsresponse)>` | Promise  
  
### streamAnswerQuery(request, callback)
    
    
    public streamAnswerQuery(request: google.cloud.discoveryengine.v1.IAnswerQueryRequest, callback: google.cloud.discoveryengine.v1.ConversationalSearchService.StreamAnswerQueryCallback): void;

Calls StreamAnswerQuery.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnswerQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ianswerqueryrequest)`   
AnswerQueryRequest message or plain object  
`callback` |  `[StreamAnswerQueryCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and AnswerQueryResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### streamAnswerQuery(request)
    
    
    public streamAnswerQuery(request: google.cloud.discoveryengine.v1.IAnswerQueryRequest): Promise<google.cloud.discoveryengine.v1.AnswerQueryResponse>;

Calls StreamAnswerQuery.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAnswerQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ianswerqueryrequest)`   
AnswerQueryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1.AnswerQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.answerqueryresponse)>` | Promise  
  
### updateConversation(request, callback)
    
    
    public updateConversation(request: google.cloud.discoveryengine.v1.IUpdateConversationRequest, callback: google.cloud.discoveryengine.v1.ConversationalSearchService.UpdateConversationCallback): void;

Calls UpdateConversation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.iupdateconversationrequest)`   
UpdateConversationRequest message or plain object  
`callback` |  `[UpdateConversationCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and Conversation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConversation(request)
    
    
    public updateConversation(request: google.cloud.discoveryengine.v1.IUpdateConversationRequest): Promise<google.cloud.discoveryengine.v1.Conversation>;

Calls UpdateConversation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.iupdateconversationrequest)`   
UpdateConversationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1.Conversation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.conversation-class)>` | Promise  
  
### updateSession(request, callback)
    
    
    public updateSession(request: google.cloud.discoveryengine.v1.IUpdateSessionRequest, callback: google.cloud.discoveryengine.v1.ConversationalSearchService.UpdateSessionCallback): void;

Calls UpdateSession.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.iupdatesessionrequest)`   
UpdateSessionRequest message or plain object  
`callback` |  `[UpdateSessionCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and Session  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSession(request)
    
    
    public updateSession(request: google.cloud.discoveryengine.v1.IUpdateSessionRequest): Promise<google.cloud.discoveryengine.v1.Session>;

Calls UpdateSession.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.iupdatesessionrequest)`   
UpdateSessionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1.Session](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.session-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
