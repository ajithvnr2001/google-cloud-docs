---
url: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.servingconfigservice-class
title: Class protos.google.cloud.discoveryengine.v1beta.ServingConfigService (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:40:12.210645+00:00
---

# Class protos.google.cloud.discoveryengine.v1beta.ServingConfigService (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.servingconfigservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.discoveryengine.v1beta.ServingConfigService (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  3.3.0  3.1.0  2.9.0  2.8.0  2.6.0  2.2.0  2.0.1  1.14.0  1.10.0  1.9.0  1.7.0  1.6.0  1.4.1  1.3.1  1.2.0  1.0.0  0.6.0  0.5.0  0.3.1  0.2.0 

Represents a ServingConfigService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.discoveryengine.v1beta.ServingConfigService

## Package

[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ServingConfigService service.

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

### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ServingConfigService;

Creates new ServingConfigService service using the specified rpc implementation.

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
`[ServingConfigService](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.servingconfigservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createServingConfig(request, callback)
    
    
    public createServingConfig(request: google.cloud.discoveryengine.v1beta.ICreateServingConfigRequest, callback: google.cloud.discoveryengine.v1beta.ServingConfigService.CreateServingConfigCallback): void;

Calls CreateServingConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateServingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreateservingconfigrequest)`   
CreateServingConfigRequest message or plain object  
`callback` |  `[CreateServingConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and ServingConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createServingConfig(request)
    
    
    public createServingConfig(request: google.cloud.discoveryengine.v1beta.ICreateServingConfigRequest): Promise<google.cloud.discoveryengine.v1beta.ServingConfig>;

Calls CreateServingConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateServingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreateservingconfigrequest)`   
CreateServingConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1beta.ServingConfig](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.servingconfig-class)>` | Promise  
  
### deleteServingConfig(request, callback)
    
    
    public deleteServingConfig(request: google.cloud.discoveryengine.v1beta.IDeleteServingConfigRequest, callback: google.cloud.discoveryengine.v1beta.ServingConfigService.DeleteServingConfigCallback): void;

Calls DeleteServingConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteServingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ideleteservingconfigrequest)`   
DeleteServingConfigRequest message or plain object  
`callback` |  `[DeleteServingConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteServingConfig(request)
    
    
    public deleteServingConfig(request: google.cloud.discoveryengine.v1beta.IDeleteServingConfigRequest): Promise<google.protobuf.Empty>;

Calls DeleteServingConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteServingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ideleteservingconfigrequest)`   
DeleteServingConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty)>` | Promise  
  
### getServingConfig(request, callback)
    
    
    public getServingConfig(request: google.cloud.discoveryengine.v1beta.IGetServingConfigRequest, callback: google.cloud.discoveryengine.v1beta.ServingConfigService.GetServingConfigCallback): void;

Calls GetServingConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetservingconfigrequest)`   
GetServingConfigRequest message or plain object  
`callback` |  `[GetServingConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and ServingConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getServingConfig(request)
    
    
    public getServingConfig(request: google.cloud.discoveryengine.v1beta.IGetServingConfigRequest): Promise<google.cloud.discoveryengine.v1beta.ServingConfig>;

Calls GetServingConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetServingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetservingconfigrequest)`   
GetServingConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1beta.ServingConfig](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.servingconfig-class)>` | Promise  
  
### listServingConfigs(request, callback)
    
    
    public listServingConfigs(request: google.cloud.discoveryengine.v1beta.IListServingConfigsRequest, callback: google.cloud.discoveryengine.v1beta.ServingConfigService.ListServingConfigsCallback): void;

Calls ListServingConfigs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServingConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistservingconfigsrequest)`   
ListServingConfigsRequest message or plain object  
`callback` |  `[ListServingConfigsCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and ListServingConfigsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listServingConfigs(request)
    
    
    public listServingConfigs(request: google.cloud.discoveryengine.v1beta.IListServingConfigsRequest): Promise<google.cloud.discoveryengine.v1beta.ListServingConfigsResponse>;

Calls ListServingConfigs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListServingConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistservingconfigsrequest)`   
ListServingConfigsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1beta.ListServingConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.listservingconfigsresponse)>` | Promise  
  
### updateServingConfig(request, callback)
    
    
    public updateServingConfig(request: google.cloud.discoveryengine.v1beta.IUpdateServingConfigRequest, callback: google.cloud.discoveryengine.v1beta.ServingConfigService.UpdateServingConfigCallback): void;

Calls UpdateServingConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateServingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iupdateservingconfigrequest)`   
UpdateServingConfigRequest message or plain object  
`callback` |  `[UpdateServingConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and ServingConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateServingConfig(request)
    
    
    public updateServingConfig(request: google.cloud.discoveryengine.v1beta.IUpdateServingConfigRequest): Promise<google.cloud.discoveryengine.v1beta.ServingConfig>;

Calls UpdateServingConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateServingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iupdateservingconfigrequest)`   
UpdateServingConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1beta.ServingConfig](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.servingconfig-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
