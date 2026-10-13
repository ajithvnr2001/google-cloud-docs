---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.conversations-class
title: Class protos.google.cloud.dialogflow.v2.Conversations (8.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:59:38.944901+00:00
---

# Class protos.google.cloud.dialogflow.v2.Conversations (8.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.conversations-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.v2.Conversations (8.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

8.2.0 (latest)  8.1.1  7.9.0  7.8.0  7.7.0  7.5.0  7.4.0  7.1.0  7.0.1  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.8.0  6.6.0  6.4.0  6.3.1  6.2.0  6.0.0  5.7.1  5.6.0  5.5.1  5.3.0  5.2.1  4.7.0  4.6.0  4.5.0  4.4.0  4.3.1  4.2.0  4.1.4  3.5.0  3.3.0 

Represents a Conversations

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dialogflow.v2.Conversations

## Package

[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Conversations service.

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

### completeConversation(request, callback)
    
    
    public completeConversation(request: google.cloud.dialogflow.v2.ICompleteConversationRequest, callback: google.cloud.dialogflow.v2.Conversations.CompleteConversationCallback): void;

Calls CompleteConversation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICompleteConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.icompleteconversationrequest)`   
CompleteConversationRequest message or plain object  
`callback` |  `[CompleteConversationCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Conversation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### completeConversation(request)
    
    
    public completeConversation(request: google.cloud.dialogflow.v2.ICompleteConversationRequest): Promise<google.cloud.dialogflow.v2.Conversation>;

Calls CompleteConversation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICompleteConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.icompleteconversationrequest)`   
CompleteConversationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.Conversation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.conversation-class)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Conversations;

Creates new Conversations service using the specified rpc implementation.

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
`[Conversations](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.conversations-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createConversation(request, callback)
    
    
    public createConversation(request: google.cloud.dialogflow.v2.ICreateConversationRequest, callback: google.cloud.dialogflow.v2.Conversations.CreateConversationCallback): void;

Calls CreateConversation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.icreateconversationrequest)`   
CreateConversationRequest message or plain object  
`callback` |  `[CreateConversationCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Conversation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConversation(request)
    
    
    public createConversation(request: google.cloud.dialogflow.v2.ICreateConversationRequest): Promise<google.cloud.dialogflow.v2.Conversation>;

Calls CreateConversation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.icreateconversationrequest)`   
CreateConversationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.Conversation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.conversation-class)>` | Promise  
  
### generateStatelessSuggestion(request, callback)
    
    
    public generateStatelessSuggestion(request: google.cloud.dialogflow.v2.IGenerateStatelessSuggestionRequest, callback: google.cloud.dialogflow.v2.Conversations.GenerateStatelessSuggestionCallback): void;

Calls GenerateStatelessSuggestion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateStatelessSuggestionRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igeneratestatelesssuggestionrequest)`   
GenerateStatelessSuggestionRequest message or plain object  
`callback` |  `[GenerateStatelessSuggestionCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateStatelessSuggestionResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateStatelessSuggestion(request)
    
    
    public generateStatelessSuggestion(request: google.cloud.dialogflow.v2.IGenerateStatelessSuggestionRequest): Promise<google.cloud.dialogflow.v2.GenerateStatelessSuggestionResponse>;

Calls GenerateStatelessSuggestion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateStatelessSuggestionRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igeneratestatelesssuggestionrequest)`   
GenerateStatelessSuggestionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.GenerateStatelessSuggestionResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.generatestatelesssuggestionresponse)>` | Promise  
  
### generateStatelessSummary(request, callback)
    
    
    public generateStatelessSummary(request: google.cloud.dialogflow.v2.IGenerateStatelessSummaryRequest, callback: google.cloud.dialogflow.v2.Conversations.GenerateStatelessSummaryCallback): void;

Calls GenerateStatelessSummary.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateStatelessSummaryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igeneratestatelesssummaryrequest)`   
GenerateStatelessSummaryRequest message or plain object  
`callback` |  `[GenerateStatelessSummaryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateStatelessSummaryResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateStatelessSummary(request)
    
    
    public generateStatelessSummary(request: google.cloud.dialogflow.v2.IGenerateStatelessSummaryRequest): Promise<google.cloud.dialogflow.v2.GenerateStatelessSummaryResponse>;

Calls GenerateStatelessSummary.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateStatelessSummaryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igeneratestatelesssummaryrequest)`   
GenerateStatelessSummaryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.GenerateStatelessSummaryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.generatestatelesssummaryresponse-class)>` | Promise  
  
### generateSuggestions(request, callback)
    
    
    public generateSuggestions(request: google.cloud.dialogflow.v2.IGenerateSuggestionsRequest, callback: google.cloud.dialogflow.v2.Conversations.GenerateSuggestionsCallback): void;

Calls GenerateSuggestions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateSuggestionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igeneratesuggestionsrequest)`   
GenerateSuggestionsRequest message or plain object  
`callback` |  `[GenerateSuggestionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateSuggestionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateSuggestions(request)
    
    
    public generateSuggestions(request: google.cloud.dialogflow.v2.IGenerateSuggestionsRequest): Promise<google.cloud.dialogflow.v2.GenerateSuggestionsResponse>;

Calls GenerateSuggestions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateSuggestionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igeneratesuggestionsrequest)`   
GenerateSuggestionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.GenerateSuggestionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.generatesuggestionsresponse-class)>` | Promise  
  
### getConversation(request, callback)
    
    
    public getConversation(request: google.cloud.dialogflow.v2.IGetConversationRequest, callback: google.cloud.dialogflow.v2.Conversations.GetConversationCallback): void;

Calls GetConversation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetconversationrequest)`   
GetConversationRequest message or plain object  
`callback` |  `[GetConversationCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Conversation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConversation(request)
    
    
    public getConversation(request: google.cloud.dialogflow.v2.IGetConversationRequest): Promise<google.cloud.dialogflow.v2.Conversation>;

Calls GetConversation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetconversationrequest)`   
GetConversationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.Conversation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.conversation-class)>` | Promise  
  
### ingestContextReferences(request, callback)
    
    
    public ingestContextReferences(request: google.cloud.dialogflow.v2.IIngestContextReferencesRequest, callback: google.cloud.dialogflow.v2.Conversations.IngestContextReferencesCallback): void;

Calls IngestContextReferences.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IIngestContextReferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iingestcontextreferencesrequest)`   
IngestContextReferencesRequest message or plain object  
`callback` |  `[IngestContextReferencesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and IngestContextReferencesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### ingestContextReferences(request)
    
    
    public ingestContextReferences(request: google.cloud.dialogflow.v2.IIngestContextReferencesRequest): Promise<google.cloud.dialogflow.v2.IngestContextReferencesResponse>;

Calls IngestContextReferences.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IIngestContextReferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iingestcontextreferencesrequest)`   
IngestContextReferencesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.IngestContextReferencesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ingestcontextreferencesresponse)>` | Promise  
  
### listConversations(request, callback)
    
    
    public listConversations(request: google.cloud.dialogflow.v2.IListConversationsRequest, callback: google.cloud.dialogflow.v2.Conversations.ListConversationsCallback): void;

Calls ListConversations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistconversationsrequest)`   
ListConversationsRequest message or plain object  
`callback` |  `[ListConversationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and ListConversationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConversations(request)
    
    
    public listConversations(request: google.cloud.dialogflow.v2.IListConversationsRequest): Promise<google.cloud.dialogflow.v2.ListConversationsResponse>;

Calls ListConversations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistconversationsrequest)`   
ListConversationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.ListConversationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.listconversationsresponse)>` | Promise  
  
### listMessages(request, callback)
    
    
    public listMessages(request: google.cloud.dialogflow.v2.IListMessagesRequest, callback: google.cloud.dialogflow.v2.Conversations.ListMessagesCallback): void;

Calls ListMessages.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMessagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistmessagesrequest)`   
ListMessagesRequest message or plain object  
`callback` |  `[ListMessagesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and ListMessagesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMessages(request)
    
    
    public listMessages(request: google.cloud.dialogflow.v2.IListMessagesRequest): Promise<google.cloud.dialogflow.v2.ListMessagesResponse>;

Calls ListMessages.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMessagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistmessagesrequest)`   
ListMessagesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.ListMessagesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.listmessagesresponse)>` | Promise  
  
### searchKnowledge(request, callback)
    
    
    public searchKnowledge(request: google.cloud.dialogflow.v2.ISearchKnowledgeRequest, callback: google.cloud.dialogflow.v2.Conversations.SearchKnowledgeCallback): void;

Calls SearchKnowledge.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchKnowledgeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.isearchknowledgerequest)`   
SearchKnowledgeRequest message or plain object  
`callback` |  `[SearchKnowledgeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchKnowledgeResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchKnowledge(request)
    
    
    public searchKnowledge(request: google.cloud.dialogflow.v2.ISearchKnowledgeRequest): Promise<google.cloud.dialogflow.v2.SearchKnowledgeResponse>;

Calls SearchKnowledge.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchKnowledgeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.isearchknowledgerequest)`   
SearchKnowledgeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.SearchKnowledgeResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.searchknowledgeresponse)>` | Promise  
  
### suggestConversationSummary(request, callback)
    
    
    public suggestConversationSummary(request: google.cloud.dialogflow.v2.ISuggestConversationSummaryRequest, callback: google.cloud.dialogflow.v2.Conversations.SuggestConversationSummaryCallback): void;

Calls SuggestConversationSummary.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISuggestConversationSummaryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.isuggestconversationsummaryrequest)`   
SuggestConversationSummaryRequest message or plain object  
`callback` |  `[SuggestConversationSummaryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and SuggestConversationSummaryResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### suggestConversationSummary(request)
    
    
    public suggestConversationSummary(request: google.cloud.dialogflow.v2.ISuggestConversationSummaryRequest): Promise<google.cloud.dialogflow.v2.SuggestConversationSummaryResponse>;

Calls SuggestConversationSummary.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISuggestConversationSummaryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.isuggestconversationsummaryrequest)`   
SuggestConversationSummaryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.SuggestConversationSummaryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.suggestconversationsummaryresponse-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
