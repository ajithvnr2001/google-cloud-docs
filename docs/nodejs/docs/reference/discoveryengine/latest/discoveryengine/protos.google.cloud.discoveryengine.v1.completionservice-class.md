---
url: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.completionservice-class
title: Class protos.google.cloud.discoveryengine.v1.CompletionService (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:03:07.954114+00:00
---

# Class protos.google.cloud.discoveryengine.v1.CompletionService (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.completionservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.discoveryengine.v1.CompletionService (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  3.3.0  3.1.0  2.9.0  2.8.0  2.6.0  2.2.0  2.0.1  1.14.0  1.10.0  1.9.0  1.7.0  1.6.0  1.4.1  1.3.1  1.2.0  1.0.0  0.6.0  0.5.0  0.3.1  0.2.0 

Represents a CompletionService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.discoveryengine.v1.CompletionService

## Package

[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new CompletionService service.

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

### completeQuery(request, callback)
    
    
    public completeQuery(request: google.cloud.discoveryengine.v1.ICompleteQueryRequest, callback: google.cloud.discoveryengine.v1.CompletionService.CompleteQueryCallback): void;

Calls CompleteQuery.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICompleteQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.icompletequeryrequest)`   
CompleteQueryRequest message or plain object  
`callback` |  `[CompleteQueryCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and CompleteQueryResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### completeQuery(request)
    
    
    public completeQuery(request: google.cloud.discoveryengine.v1.ICompleteQueryRequest): Promise<google.cloud.discoveryengine.v1.CompleteQueryResponse>;

Calls CompleteQuery.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICompleteQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.icompletequeryrequest)`   
CompleteQueryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1.CompleteQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.completequeryresponse-class)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): CompletionService;

Creates new CompletionService service using the specified rpc implementation.

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
`[CompletionService](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.completionservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### importCompletionSuggestions(request, callback)
    
    
    public importCompletionSuggestions(request: google.cloud.discoveryengine.v1.IImportCompletionSuggestionsRequest, callback: google.cloud.discoveryengine.v1.CompletionService.ImportCompletionSuggestionsCallback): void;

Calls ImportCompletionSuggestions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportCompletionSuggestionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.iimportcompletionsuggestionsrequest)`   
ImportCompletionSuggestionsRequest message or plain object  
`callback` |  `[ImportCompletionSuggestionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importCompletionSuggestions(request)
    
    
    public importCompletionSuggestions(request: google.cloud.discoveryengine.v1.IImportCompletionSuggestionsRequest): Promise<google.longrunning.Operation>;

Calls ImportCompletionSuggestions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportCompletionSuggestionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.iimportcompletionsuggestionsrequest)`   
ImportCompletionSuggestionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.operation)>` | Promise  
  
### importSuggestionDenyListEntries(request, callback)
    
    
    public importSuggestionDenyListEntries(request: google.cloud.discoveryengine.v1.IImportSuggestionDenyListEntriesRequest, callback: google.cloud.discoveryengine.v1.CompletionService.ImportSuggestionDenyListEntriesCallback): void;

Calls ImportSuggestionDenyListEntries.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.iimportsuggestiondenylistentriesrequest)`   
ImportSuggestionDenyListEntriesRequest message or plain object  
`callback` |  `[ImportSuggestionDenyListEntriesCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importSuggestionDenyListEntries(request)
    
    
    public importSuggestionDenyListEntries(request: google.cloud.discoveryengine.v1.IImportSuggestionDenyListEntriesRequest): Promise<google.longrunning.Operation>;

Calls ImportSuggestionDenyListEntries.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.iimportsuggestiondenylistentriesrequest)`   
ImportSuggestionDenyListEntriesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.operation)>` | Promise  
  
### purgeCompletionSuggestions(request, callback)
    
    
    public purgeCompletionSuggestions(request: google.cloud.discoveryengine.v1.IPurgeCompletionSuggestionsRequest, callback: google.cloud.discoveryengine.v1.CompletionService.PurgeCompletionSuggestionsCallback): void;

Calls PurgeCompletionSuggestions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPurgeCompletionSuggestionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ipurgecompletionsuggestionsrequest)`   
PurgeCompletionSuggestionsRequest message or plain object  
`callback` |  `[PurgeCompletionSuggestionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### purgeCompletionSuggestions(request)
    
    
    public purgeCompletionSuggestions(request: google.cloud.discoveryengine.v1.IPurgeCompletionSuggestionsRequest): Promise<google.longrunning.Operation>;

Calls PurgeCompletionSuggestions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPurgeCompletionSuggestionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ipurgecompletionsuggestionsrequest)`   
PurgeCompletionSuggestionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.operation)>` | Promise  
  
### purgeSuggestionDenyListEntries(request, callback)
    
    
    public purgeSuggestionDenyListEntries(request: google.cloud.discoveryengine.v1.IPurgeSuggestionDenyListEntriesRequest, callback: google.cloud.discoveryengine.v1.CompletionService.PurgeSuggestionDenyListEntriesCallback): void;

Calls PurgeSuggestionDenyListEntries.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPurgeSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ipurgesuggestiondenylistentriesrequest)`   
PurgeSuggestionDenyListEntriesRequest message or plain object  
`callback` |  `[PurgeSuggestionDenyListEntriesCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### purgeSuggestionDenyListEntries(request)
    
    
    public purgeSuggestionDenyListEntries(request: google.cloud.discoveryengine.v1.IPurgeSuggestionDenyListEntriesRequest): Promise<google.longrunning.Operation>;

Calls PurgeSuggestionDenyListEntries.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPurgeSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ipurgesuggestiondenylistentriesrequest)`   
PurgeSuggestionDenyListEntriesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
