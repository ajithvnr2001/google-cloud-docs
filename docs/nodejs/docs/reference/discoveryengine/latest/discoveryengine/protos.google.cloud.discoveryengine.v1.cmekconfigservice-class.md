---
url: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.cmekconfigservice-class
title: Class protos.google.cloud.discoveryengine.v1.CmekConfigService (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:03:04.141590+00:00
---

# Class protos.google.cloud.discoveryengine.v1.CmekConfigService (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.cmekconfigservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.discoveryengine.v1.CmekConfigService (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  3.3.0  3.1.0  2.9.0  2.8.0  2.6.0  2.2.0  2.0.1  1.14.0  1.10.0  1.9.0  1.7.0  1.6.0  1.4.1  1.3.1  1.2.0  1.0.0  0.6.0  0.5.0  0.3.1  0.2.0 

Represents a CmekConfigService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.discoveryengine.v1.CmekConfigService

## Package

[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new CmekConfigService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): CmekConfigService;

Creates new CmekConfigService service using the specified rpc implementation.

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
`[CmekConfigService](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.cmekconfigservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### deleteCmekConfig(request, callback)
    
    
    public deleteCmekConfig(request: google.cloud.discoveryengine.v1.IDeleteCmekConfigRequest, callback: google.cloud.discoveryengine.v1.CmekConfigService.DeleteCmekConfigCallback): void;

Calls DeleteCmekConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCmekConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ideletecmekconfigrequest)`   
DeleteCmekConfigRequest message or plain object  
`callback` |  `[DeleteCmekConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCmekConfig(request)
    
    
    public deleteCmekConfig(request: google.cloud.discoveryengine.v1.IDeleteCmekConfigRequest): Promise<google.longrunning.Operation>;

Calls DeleteCmekConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCmekConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ideletecmekconfigrequest)`   
DeleteCmekConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.operation)>` | Promise  
  
### getCmekConfig(request, callback)
    
    
    public getCmekConfig(request: google.cloud.discoveryengine.v1.IGetCmekConfigRequest, callback: google.cloud.discoveryengine.v1.CmekConfigService.GetCmekConfigCallback): void;

Calls GetCmekConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCmekConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.igetcmekconfigrequest)`   
GetCmekConfigRequest message or plain object  
`callback` |  `[GetCmekConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and CmekConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCmekConfig(request)
    
    
    public getCmekConfig(request: google.cloud.discoveryengine.v1.IGetCmekConfigRequest): Promise<google.cloud.discoveryengine.v1.CmekConfig>;

Calls GetCmekConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCmekConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.igetcmekconfigrequest)`   
GetCmekConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1.CmekConfig](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.cmekconfig-class)>` | Promise  
  
### listCmekConfigs(request, callback)
    
    
    public listCmekConfigs(request: google.cloud.discoveryengine.v1.IListCmekConfigsRequest, callback: google.cloud.discoveryengine.v1.CmekConfigService.ListCmekConfigsCallback): void;

Calls ListCmekConfigs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCmekConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ilistcmekconfigsrequest)`   
ListCmekConfigsRequest message or plain object  
`callback` |  `[ListCmekConfigsCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCmekConfigsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCmekConfigs(request)
    
    
    public listCmekConfigs(request: google.cloud.discoveryengine.v1.IListCmekConfigsRequest): Promise<google.cloud.discoveryengine.v1.ListCmekConfigsResponse>;

Calls ListCmekConfigs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCmekConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ilistcmekconfigsrequest)`   
ListCmekConfigsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1.ListCmekConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.listcmekconfigsresponse)>` | Promise  
  
### updateCmekConfig(request, callback)
    
    
    public updateCmekConfig(request: google.cloud.discoveryengine.v1.IUpdateCmekConfigRequest, callback: google.cloud.discoveryengine.v1.CmekConfigService.UpdateCmekConfigCallback): void;

Calls UpdateCmekConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCmekConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.iupdatecmekconfigrequest)`   
UpdateCmekConfigRequest message or plain object  
`callback` |  `[UpdateCmekConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCmekConfig(request)
    
    
    public updateCmekConfig(request: google.cloud.discoveryengine.v1.IUpdateCmekConfigRequest): Promise<google.longrunning.Operation>;

Calls UpdateCmekConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCmekConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.iupdatecmekconfigrequest)`   
UpdateCmekConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
