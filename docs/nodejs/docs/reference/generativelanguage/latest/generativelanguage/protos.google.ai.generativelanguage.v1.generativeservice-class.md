---
url: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.generativeservice-class
title: Class protos.google.ai.generativelanguage.v1.GenerativeService (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:05.414149+00:00
---

# Class protos.google.ai.generativelanguage.v1.GenerativeService (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.generativeservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ai.generativelanguage.v1.GenerativeService (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  4.1.0  3.7.0  3.6.0  2.9.0  2.8.0  2.7.0  2.6.0  2.4.0  2.3.0 

Represents a GenerativeService

## Inheritance

$protobuf.rpc.Service > protos.google.ai.generativelanguage.v1.GenerativeService

## Package

[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new GenerativeService service.

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

### batchEmbedContents(request, callback)
    
    
    public batchEmbedContents(request: google.ai.generativelanguage.v1.IBatchEmbedContentsRequest, callback: google.ai.generativelanguage.v1.GenerativeService.BatchEmbedContentsCallback): void;

Calls BatchEmbedContents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchEmbedContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.ibatchembedcontentsrequest)`   
BatchEmbedContentsRequest message or plain object  
`callback` |  `[BatchEmbedContentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchEmbedContentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchEmbedContents(request)
    
    
    public batchEmbedContents(request: google.ai.generativelanguage.v1.IBatchEmbedContentsRequest): Promise<google.ai.generativelanguage.v1.BatchEmbedContentsResponse>;

Calls BatchEmbedContents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchEmbedContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.ibatchembedcontentsrequest)`   
BatchEmbedContentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1.BatchEmbedContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.batchembedcontentsresponse)>` | Promise  
  
### countTokens(request, callback)
    
    
    public countTokens(request: google.ai.generativelanguage.v1.ICountTokensRequest, callback: google.ai.generativelanguage.v1.GenerativeService.CountTokensCallback): void;

Calls CountTokens.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICountTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.icounttokensrequest)`   
CountTokensRequest message or plain object  
`callback` |  `[CountTokensCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and CountTokensResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### countTokens(request)
    
    
    public countTokens(request: google.ai.generativelanguage.v1.ICountTokensRequest): Promise<google.ai.generativelanguage.v1.CountTokensResponse>;

Calls CountTokens.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICountTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.icounttokensrequest)`   
CountTokensRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1.CountTokensResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.counttokensresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): GenerativeService;

Creates new GenerativeService service using the specified rpc implementation.

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
`[GenerativeService](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.generativeservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### embedContent(request, callback)
    
    
    public embedContent(request: google.ai.generativelanguage.v1.IEmbedContentRequest, callback: google.ai.generativelanguage.v1.GenerativeService.EmbedContentCallback): void;

Calls EmbedContent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEmbedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.iembedcontentrequest)`   
EmbedContentRequest message or plain object  
`callback` |  `[EmbedContentCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and EmbedContentResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### embedContent(request)
    
    
    public embedContent(request: google.ai.generativelanguage.v1.IEmbedContentRequest): Promise<google.ai.generativelanguage.v1.EmbedContentResponse>;

Calls EmbedContent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IEmbedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.iembedcontentrequest)`   
EmbedContentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1.EmbedContentResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.embedcontentresponse)>` | Promise  
  
### generateContent(request, callback)
    
    
    public generateContent(request: google.ai.generativelanguage.v1.IGenerateContentRequest, callback: google.ai.generativelanguage.v1.GenerativeService.GenerateContentCallback): void;

Calls GenerateContent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.igeneratecontentrequest)`   
GenerateContentRequest message or plain object  
`callback` |  `[GenerateContentCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateContentResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateContent(request)
    
    
    public generateContent(request: google.ai.generativelanguage.v1.IGenerateContentRequest): Promise<google.ai.generativelanguage.v1.GenerateContentResponse>;

Calls GenerateContent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.igeneratecontentrequest)`   
GenerateContentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1.GenerateContentResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.generatecontentresponse-class)>` | Promise  
  
### streamGenerateContent(request, callback)
    
    
    public streamGenerateContent(request: google.ai.generativelanguage.v1.IGenerateContentRequest, callback: google.ai.generativelanguage.v1.GenerativeService.StreamGenerateContentCallback): void;

Calls StreamGenerateContent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.igeneratecontentrequest)`   
GenerateContentRequest message or plain object  
`callback` |  `[StreamGenerateContentCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateContentResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### streamGenerateContent(request)
    
    
    public streamGenerateContent(request: google.ai.generativelanguage.v1.IGenerateContentRequest): Promise<google.ai.generativelanguage.v1.GenerateContentResponse>;

Calls StreamGenerateContent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.igeneratecontentrequest)`   
GenerateContentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1.GenerateContentResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.generatecontentresponse-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
