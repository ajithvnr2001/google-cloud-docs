---
url: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.textservice-class
title: Class protos.google.ai.generativelanguage.v1alpha.TextService (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:46:42.798422+00:00
---

# Class protos.google.ai.generativelanguage.v1alpha.TextService (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.textservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ai.generativelanguage.v1alpha.TextService (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  4.1.0  3.7.0  3.6.0  2.9.0  2.8.0  2.7.0  2.6.0  2.4.0  2.3.0 

Represents a TextService

## Inheritance

$protobuf.rpc.Service > protos.google.ai.generativelanguage.v1alpha.TextService

## Package

[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new TextService service.

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

### batchEmbedText(request, callback)
    
    
    public batchEmbedText(request: google.ai.generativelanguage.v1alpha.IBatchEmbedTextRequest, callback: google.ai.generativelanguage.v1alpha.TextService.BatchEmbedTextCallback): void;

Calls BatchEmbedText.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchEmbedTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchembedtextrequest)`   
BatchEmbedTextRequest message or plain object  
`callback` |  `[BatchEmbedTextCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchEmbedTextResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchEmbedText(request)
    
    
    public batchEmbedText(request: google.ai.generativelanguage.v1alpha.IBatchEmbedTextRequest): Promise<google.ai.generativelanguage.v1alpha.BatchEmbedTextResponse>;

Calls BatchEmbedText.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchEmbedTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchembedtextrequest)`   
BatchEmbedTextRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.BatchEmbedTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.batchembedtextresponse)>` | Promise  
  
### countTextTokens(request, callback)
    
    
    public countTextTokens(request: google.ai.generativelanguage.v1alpha.ICountTextTokensRequest, callback: google.ai.generativelanguage.v1alpha.TextService.CountTextTokensCallback): void;

Calls CountTextTokens.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICountTextTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icounttexttokensrequest)`   
CountTextTokensRequest message or plain object  
`callback` |  `[CountTextTokensCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and CountTextTokensResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### countTextTokens(request)
    
    
    public countTextTokens(request: google.ai.generativelanguage.v1alpha.ICountTextTokensRequest): Promise<google.ai.generativelanguage.v1alpha.CountTextTokensResponse>;

Calls CountTextTokens.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICountTextTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icounttexttokensrequest)`   
CountTextTokensRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.CountTextTokensResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.counttexttokensresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): TextService;

Creates new TextService service using the specified rpc implementation.

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
`[TextService](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.textservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### embedText(request, callback)
    
    
    public embedText(request: google.ai.generativelanguage.v1alpha.IEmbedTextRequest, callback: google.ai.generativelanguage.v1alpha.TextService.EmbedTextCallback): void;

Calls EmbedText.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEmbedTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iembedtextrequest)`   
EmbedTextRequest message or plain object  
`callback` |  `[EmbedTextCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and EmbedTextResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### embedText(request)
    
    
    public embedText(request: google.ai.generativelanguage.v1alpha.IEmbedTextRequest): Promise<google.ai.generativelanguage.v1alpha.EmbedTextResponse>;

Calls EmbedText.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IEmbedTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iembedtextrequest)`   
EmbedTextRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.EmbedTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.embedtextresponse)>` | Promise  
  
### generateText(request, callback)
    
    
    public generateText(request: google.ai.generativelanguage.v1alpha.IGenerateTextRequest, callback: google.ai.generativelanguage.v1alpha.TextService.GenerateTextCallback): void;

Calls GenerateText.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igeneratetextrequest)`   
GenerateTextRequest message or plain object  
`callback` |  `[GenerateTextCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateTextResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateText(request)
    
    
    public generateText(request: google.ai.generativelanguage.v1alpha.IGenerateTextRequest): Promise<google.ai.generativelanguage.v1alpha.GenerateTextResponse>;

Calls GenerateText.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igeneratetextrequest)`   
GenerateTextRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.GenerateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.generatetextresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
