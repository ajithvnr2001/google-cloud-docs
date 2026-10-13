---
url: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.generativequestionservice-class
title: Class protos.google.cloud.retail.v2alpha.GenerativeQuestionService (5.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:14:46.737089+00:00
---

# Class protos.google.cloud.retail.v2alpha.GenerativeQuestionService (5.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.generativequestionservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.retail.v2alpha.GenerativeQuestionService (5.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.4.0 (latest)  5.3.1  5.0.1  4.4.0  4.3.0  3.6.0  3.5.0  3.1.0  2.4.1  2.3.1  2.1.1  2.0.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.2  1.1.6 

Represents a GenerativeQuestionService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.retail.v2alpha.GenerativeQuestionService

## Package

[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new GenerativeQuestionService service.

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

### batchUpdateGenerativeQuestionConfigs(request, callback)
    
    
    public batchUpdateGenerativeQuestionConfigs(request: google.cloud.retail.v2alpha.IBatchUpdateGenerativeQuestionConfigsRequest, callback: google.cloud.retail.v2alpha.GenerativeQuestionService.BatchUpdateGenerativeQuestionConfigsCallback): void;

Calls BatchUpdateGenerativeQuestionConfigs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ibatchupdategenerativequestionconfigsrequest)`   
BatchUpdateGenerativeQuestionConfigsRequest message or plain object  
`callback` |  `[BatchUpdateGenerativeQuestionConfigsCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchUpdateGenerativeQuestionConfigsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchUpdateGenerativeQuestionConfigs(request)
    
    
    public batchUpdateGenerativeQuestionConfigs(request: google.cloud.retail.v2alpha.IBatchUpdateGenerativeQuestionConfigsRequest): Promise<google.cloud.retail.v2alpha.BatchUpdateGenerativeQuestionConfigsResponse>;

Calls BatchUpdateGenerativeQuestionConfigs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ibatchupdategenerativequestionconfigsrequest)`   
BatchUpdateGenerativeQuestionConfigsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.retail.v2alpha.BatchUpdateGenerativeQuestionConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.batchupdategenerativequestionconfigsresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): GenerativeQuestionService;

Creates new GenerativeQuestionService service using the specified rpc implementation.

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
`[GenerativeQuestionService](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.generativequestionservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### getGenerativeQuestionsFeatureConfig(request, callback)
    
    
    public getGenerativeQuestionsFeatureConfig(request: google.cloud.retail.v2alpha.IGetGenerativeQuestionsFeatureConfigRequest, callback: google.cloud.retail.v2alpha.GenerativeQuestionService.GetGenerativeQuestionsFeatureConfigCallback): void;

Calls GetGenerativeQuestionsFeatureConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetGenerativeQuestionsFeatureConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.igetgenerativequestionsfeatureconfigrequest)`   
GetGenerativeQuestionsFeatureConfigRequest message or plain object  
`callback` |  `[GetGenerativeQuestionsFeatureConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerativeQuestionsFeatureConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getGenerativeQuestionsFeatureConfig(request)
    
    
    public getGenerativeQuestionsFeatureConfig(request: google.cloud.retail.v2alpha.IGetGenerativeQuestionsFeatureConfigRequest): Promise<google.cloud.retail.v2alpha.GenerativeQuestionsFeatureConfig>;

Calls GetGenerativeQuestionsFeatureConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetGenerativeQuestionsFeatureConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.igetgenerativequestionsfeatureconfigrequest)`   
GetGenerativeQuestionsFeatureConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.retail.v2alpha.GenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.generativequestionsfeatureconfig)>` | Promise  
  
### listGenerativeQuestionConfigs(request, callback)
    
    
    public listGenerativeQuestionConfigs(request: google.cloud.retail.v2alpha.IListGenerativeQuestionConfigsRequest, callback: google.cloud.retail.v2alpha.GenerativeQuestionService.ListGenerativeQuestionConfigsCallback): void;

Calls ListGenerativeQuestionConfigs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistgenerativequestionconfigsrequest)`   
ListGenerativeQuestionConfigsRequest message or plain object  
`callback` |  `[ListGenerativeQuestionConfigsCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and ListGenerativeQuestionConfigsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listGenerativeQuestionConfigs(request)
    
    
    public listGenerativeQuestionConfigs(request: google.cloud.retail.v2alpha.IListGenerativeQuestionConfigsRequest): Promise<google.cloud.retail.v2alpha.ListGenerativeQuestionConfigsResponse>;

Calls ListGenerativeQuestionConfigs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistgenerativequestionconfigsrequest)`   
ListGenerativeQuestionConfigsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.retail.v2alpha.ListGenerativeQuestionConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.listgenerativequestionconfigsresponse)>` | Promise  
  
### updateGenerativeQuestionConfig(request, callback)
    
    
    public updateGenerativeQuestionConfig(request: google.cloud.retail.v2alpha.IUpdateGenerativeQuestionConfigRequest, callback: google.cloud.retail.v2alpha.GenerativeQuestionService.UpdateGenerativeQuestionConfigCallback): void;

Calls UpdateGenerativeQuestionConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGenerativeQuestionConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iupdategenerativequestionconfigrequest)`   
UpdateGenerativeQuestionConfigRequest message or plain object  
`callback` |  `[UpdateGenerativeQuestionConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerativeQuestionConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateGenerativeQuestionConfig(request)
    
    
    public updateGenerativeQuestionConfig(request: google.cloud.retail.v2alpha.IUpdateGenerativeQuestionConfigRequest): Promise<google.cloud.retail.v2alpha.GenerativeQuestionConfig>;

Calls UpdateGenerativeQuestionConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGenerativeQuestionConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iupdategenerativequestionconfigrequest)`   
UpdateGenerativeQuestionConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.retail.v2alpha.GenerativeQuestionConfig](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.generativequestionconfig)>` | Promise  
  
### updateGenerativeQuestionsFeatureConfig(request, callback)
    
    
    public updateGenerativeQuestionsFeatureConfig(request: google.cloud.retail.v2alpha.IUpdateGenerativeQuestionsFeatureConfigRequest, callback: google.cloud.retail.v2alpha.GenerativeQuestionService.UpdateGenerativeQuestionsFeatureConfigCallback): void;

Calls UpdateGenerativeQuestionsFeatureConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGenerativeQuestionsFeatureConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iupdategenerativequestionsfeatureconfigrequest)`   
UpdateGenerativeQuestionsFeatureConfigRequest message or plain object  
`callback` |  `[UpdateGenerativeQuestionsFeatureConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerativeQuestionsFeatureConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateGenerativeQuestionsFeatureConfig(request)
    
    
    public updateGenerativeQuestionsFeatureConfig(request: google.cloud.retail.v2alpha.IUpdateGenerativeQuestionsFeatureConfigRequest): Promise<google.cloud.retail.v2alpha.GenerativeQuestionsFeatureConfig>;

Calls UpdateGenerativeQuestionsFeatureConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGenerativeQuestionsFeatureConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iupdategenerativequestionsfeatureconfigrequest)`   
UpdateGenerativeQuestionsFeatureConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.retail.v2alpha.GenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.generativequestionsfeatureconfig)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
