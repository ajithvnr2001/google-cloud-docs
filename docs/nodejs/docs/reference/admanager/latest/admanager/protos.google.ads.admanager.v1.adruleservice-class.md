---
url: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adruleservice-class
title: Class protos.google.ads.admanager.v1.AdRuleService (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:18:40.896758+00:00
---

# Class protos.google.ads.admanager.v1.AdRuleService (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adruleservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.admanager.v1.AdRuleService (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.12.0  0.11.0  0.7.0  0.6.0  0.1.0 

Represents an AdRuleService

## Inheritance

$protobuf.rpc.Service > protos.google.ads.admanager.v1.AdRuleService

## Package

[@google-ads/admanager](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AdRuleService service.

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

### batchActivateAdRules(request, callback)
    
    
    public batchActivateAdRules(request: google.ads.admanager.v1.IBatchActivateAdRulesRequest, callback: google.ads.admanager.v1.AdRuleService.BatchActivateAdRulesCallback): void;

Calls BatchActivateAdRules.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchActivateAdRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchactivateadrulesrequest)`   
BatchActivateAdRulesRequest message or plain object  
`callback` |  `[BatchActivateAdRulesCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchActivateAdRulesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchActivateAdRules(request)
    
    
    public batchActivateAdRules(request: google.ads.admanager.v1.IBatchActivateAdRulesRequest): Promise<google.ads.admanager.v1.BatchActivateAdRulesResponse>;

Calls BatchActivateAdRules.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchActivateAdRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchactivateadrulesrequest)`   
BatchActivateAdRulesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchActivateAdRulesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchactivateadrulesresponse)>` | Promise  
  
### batchCreateAdRules(request, callback)
    
    
    public batchCreateAdRules(request: google.ads.admanager.v1.IBatchCreateAdRulesRequest, callback: google.ads.admanager.v1.AdRuleService.BatchCreateAdRulesCallback): void;

Calls BatchCreateAdRules.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateAdRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchcreateadrulesrequest)`   
BatchCreateAdRulesRequest message or plain object  
`callback` |  `[BatchCreateAdRulesCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchCreateAdRulesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateAdRules(request)
    
    
    public batchCreateAdRules(request: google.ads.admanager.v1.IBatchCreateAdRulesRequest): Promise<google.ads.admanager.v1.BatchCreateAdRulesResponse>;

Calls BatchCreateAdRules.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateAdRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchcreateadrulesrequest)`   
BatchCreateAdRulesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchCreateAdRulesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchcreateadrulesresponse)>` | Promise  
  
### batchDeactivateAdRules(request, callback)
    
    
    public batchDeactivateAdRules(request: google.ads.admanager.v1.IBatchDeactivateAdRulesRequest, callback: google.ads.admanager.v1.AdRuleService.BatchDeactivateAdRulesCallback): void;

Calls BatchDeactivateAdRules.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeactivateAdRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchdeactivateadrulesrequest)`   
BatchDeactivateAdRulesRequest message or plain object  
`callback` |  `[BatchDeactivateAdRulesCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchDeactivateAdRulesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchDeactivateAdRules(request)
    
    
    public batchDeactivateAdRules(request: google.ads.admanager.v1.IBatchDeactivateAdRulesRequest): Promise<google.ads.admanager.v1.BatchDeactivateAdRulesResponse>;

Calls BatchDeactivateAdRules.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeactivateAdRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchdeactivateadrulesrequest)`   
BatchDeactivateAdRulesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchDeactivateAdRulesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchdeactivateadrulesresponse)>` | Promise  
  
### batchDeleteAdRules(request, callback)
    
    
    public batchDeleteAdRules(request: google.ads.admanager.v1.IBatchDeleteAdRulesRequest, callback: google.ads.admanager.v1.AdRuleService.BatchDeleteAdRulesCallback): void;

Calls BatchDeleteAdRules.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteAdRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchdeleteadrulesrequest)`   
BatchDeleteAdRulesRequest message or plain object  
`callback` |  `[BatchDeleteAdRulesCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchDeleteAdRules(request)
    
    
    public batchDeleteAdRules(request: google.ads.admanager.v1.IBatchDeleteAdRulesRequest): Promise<google.protobuf.Empty>;

Calls BatchDeleteAdRules.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteAdRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchdeleteadrulesrequest)`   
BatchDeleteAdRulesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.protobuf.empty)>` | Promise  
  
### batchUpdateAdRules(request, callback)
    
    
    public batchUpdateAdRules(request: google.ads.admanager.v1.IBatchUpdateAdRulesRequest, callback: google.ads.admanager.v1.AdRuleService.BatchUpdateAdRulesCallback): void;

Calls BatchUpdateAdRules.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateAdRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchupdateadrulesrequest)`   
BatchUpdateAdRulesRequest message or plain object  
`callback` |  `[BatchUpdateAdRulesCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchUpdateAdRulesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchUpdateAdRules(request)
    
    
    public batchUpdateAdRules(request: google.ads.admanager.v1.IBatchUpdateAdRulesRequest): Promise<google.ads.admanager.v1.BatchUpdateAdRulesResponse>;

Calls BatchUpdateAdRules.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateAdRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchupdateadrulesrequest)`   
BatchUpdateAdRulesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchUpdateAdRulesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchupdateadrulesresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AdRuleService;

Creates new AdRuleService service using the specified rpc implementation.

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
`[AdRuleService](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adruleservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAdRule(request, callback)
    
    
    public createAdRule(request: google.ads.admanager.v1.ICreateAdRuleRequest, callback: google.ads.admanager.v1.AdRuleService.CreateAdRuleCallback): void;

Calls CreateAdRule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAdRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.icreateadrulerequest)`   
CreateAdRuleRequest message or plain object  
`callback` |  `[CreateAdRuleCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and AdRule  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAdRule(request)
    
    
    public createAdRule(request: google.ads.admanager.v1.ICreateAdRuleRequest): Promise<google.ads.admanager.v1.AdRule>;

Calls CreateAdRule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAdRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.icreateadrulerequest)`   
CreateAdRuleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.AdRule](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adrule)>` | Promise  
  
### getAdRule(request, callback)
    
    
    public getAdRule(request: google.ads.admanager.v1.IGetAdRuleRequest, callback: google.ads.admanager.v1.AdRuleService.GetAdRuleCallback): void;

Calls GetAdRule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAdRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.igetadrulerequest)`   
GetAdRuleRequest message or plain object  
`callback` |  `[GetAdRuleCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and AdRule  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAdRule(request)
    
    
    public getAdRule(request: google.ads.admanager.v1.IGetAdRuleRequest): Promise<google.ads.admanager.v1.AdRule>;

Calls GetAdRule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAdRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.igetadrulerequest)`   
GetAdRuleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.AdRule](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adrule)>` | Promise  
  
### listAdRules(request, callback)
    
    
    public listAdRules(request: google.ads.admanager.v1.IListAdRulesRequest, callback: google.ads.admanager.v1.AdRuleService.ListAdRulesCallback): void;

Calls ListAdRules.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAdRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistadrulesrequest)`   
ListAdRulesRequest message or plain object  
`callback` |  `[ListAdRulesCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAdRulesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAdRules(request)
    
    
    public listAdRules(request: google.ads.admanager.v1.IListAdRulesRequest): Promise<google.ads.admanager.v1.ListAdRulesResponse>;

Calls ListAdRules.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAdRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistadrulesrequest)`   
ListAdRulesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.ListAdRulesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.listadrulesresponse)>` | Promise  
  
### updateAdRule(request, callback)
    
    
    public updateAdRule(request: google.ads.admanager.v1.IUpdateAdRuleRequest, callback: google.ads.admanager.v1.AdRuleService.UpdateAdRuleCallback): void;

Calls UpdateAdRule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAdRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iupdateadrulerequest)`   
UpdateAdRuleRequest message or plain object  
`callback` |  `[UpdateAdRuleCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and AdRule  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAdRule(request)
    
    
    public updateAdRule(request: google.ads.admanager.v1.IUpdateAdRuleRequest): Promise<google.ads.admanager.v1.AdRule>;

Calls UpdateAdRule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAdRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iupdateadrulerequest)`   
UpdateAdRuleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.AdRule](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adrule)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
