---
url: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.discussservice-class
title: Class protos.google.ai.generativelanguage.v1beta.DiscussService (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:08.619374+00:00
---

# Class protos.google.ai.generativelanguage.v1beta.DiscussService (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.discussservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ai.generativelanguage.v1beta.DiscussService (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  4.1.0  3.7.0  3.6.0  2.9.0  2.8.0  2.7.0  2.6.0  2.4.0  2.3.0 

Represents a DiscussService

## Inheritance

$protobuf.rpc.Service > protos.google.ai.generativelanguage.v1beta.DiscussService

## Package

[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DiscussService service.

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

### countMessageTokens(request, callback)
    
    
    public countMessageTokens(request: google.ai.generativelanguage.v1beta.ICountMessageTokensRequest, callback: google.ai.generativelanguage.v1beta.DiscussService.CountMessageTokensCallback): void;

Calls CountMessageTokens.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICountMessageTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icountmessagetokensrequest)`   
CountMessageTokensRequest message or plain object  
`callback` |  `[CountMessageTokensCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and CountMessageTokensResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### countMessageTokens(request)
    
    
    public countMessageTokens(request: google.ai.generativelanguage.v1beta.ICountMessageTokensRequest): Promise<google.ai.generativelanguage.v1beta.CountMessageTokensResponse>;

Calls CountMessageTokens.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICountMessageTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icountmessagetokensrequest)`   
CountMessageTokensRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1beta.CountMessageTokensResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.countmessagetokensresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DiscussService;

Creates new DiscussService service using the specified rpc implementation.

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
`[DiscussService](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.discussservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### generateMessage(request, callback)
    
    
    public generateMessage(request: google.ai.generativelanguage.v1beta.IGenerateMessageRequest, callback: google.ai.generativelanguage.v1beta.DiscussService.GenerateMessageCallback): void;

Calls GenerateMessage.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igeneratemessagerequest)`   
GenerateMessageRequest message or plain object  
`callback` |  `[GenerateMessageCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateMessageResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateMessage(request)
    
    
    public generateMessage(request: google.ai.generativelanguage.v1beta.IGenerateMessageRequest): Promise<google.ai.generativelanguage.v1beta.GenerateMessageResponse>;

Calls GenerateMessage.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igeneratemessagerequest)`   
GenerateMessageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1beta.GenerateMessageResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.generatemessageresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
