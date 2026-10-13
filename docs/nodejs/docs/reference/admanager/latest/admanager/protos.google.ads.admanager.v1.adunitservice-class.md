---
url: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adunitservice-class
title: Class protos.google.ads.admanager.v1.AdUnitService (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:18:45.421457+00:00
---

# Class protos.google.ads.admanager.v1.AdUnitService (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adunitservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.admanager.v1.AdUnitService (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.12.0  0.11.0  0.7.0  0.6.0  0.1.0 

Represents an AdUnitService

## Inheritance

$protobuf.rpc.Service > protos.google.ads.admanager.v1.AdUnitService

## Package

[@google-ads/admanager](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AdUnitService service.

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

### batchActivateAdUnits(request, callback)
    
    
    public batchActivateAdUnits(request: google.ads.admanager.v1.IBatchActivateAdUnitsRequest, callback: google.ads.admanager.v1.AdUnitService.BatchActivateAdUnitsCallback): void;

Calls BatchActivateAdUnits.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchActivateAdUnitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchactivateadunitsrequest)`   
BatchActivateAdUnitsRequest message or plain object  
`callback` |  `[BatchActivateAdUnitsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchActivateAdUnitsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchActivateAdUnits(request)
    
    
    public batchActivateAdUnits(request: google.ads.admanager.v1.IBatchActivateAdUnitsRequest): Promise<google.ads.admanager.v1.BatchActivateAdUnitsResponse>;

Calls BatchActivateAdUnits.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchActivateAdUnitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchactivateadunitsrequest)`   
BatchActivateAdUnitsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchActivateAdUnitsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchactivateadunitsresponse)>` | Promise  
  
### batchArchiveAdUnits(request, callback)
    
    
    public batchArchiveAdUnits(request: google.ads.admanager.v1.IBatchArchiveAdUnitsRequest, callback: google.ads.admanager.v1.AdUnitService.BatchArchiveAdUnitsCallback): void;

Calls BatchArchiveAdUnits.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchArchiveAdUnitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatcharchiveadunitsrequest)`   
BatchArchiveAdUnitsRequest message or plain object  
`callback` |  `[BatchArchiveAdUnitsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchArchiveAdUnitsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchArchiveAdUnits(request)
    
    
    public batchArchiveAdUnits(request: google.ads.admanager.v1.IBatchArchiveAdUnitsRequest): Promise<google.ads.admanager.v1.BatchArchiveAdUnitsResponse>;

Calls BatchArchiveAdUnits.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchArchiveAdUnitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatcharchiveadunitsrequest)`   
BatchArchiveAdUnitsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchArchiveAdUnitsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batcharchiveadunitsresponse)>` | Promise  
  
### batchCreateAdUnits(request, callback)
    
    
    public batchCreateAdUnits(request: google.ads.admanager.v1.IBatchCreateAdUnitsRequest, callback: google.ads.admanager.v1.AdUnitService.BatchCreateAdUnitsCallback): void;

Calls BatchCreateAdUnits.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateAdUnitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchcreateadunitsrequest)`   
BatchCreateAdUnitsRequest message or plain object  
`callback` |  `[BatchCreateAdUnitsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchCreateAdUnitsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateAdUnits(request)
    
    
    public batchCreateAdUnits(request: google.ads.admanager.v1.IBatchCreateAdUnitsRequest): Promise<google.ads.admanager.v1.BatchCreateAdUnitsResponse>;

Calls BatchCreateAdUnits.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateAdUnitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchcreateadunitsrequest)`   
BatchCreateAdUnitsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchCreateAdUnitsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchcreateadunitsresponse)>` | Promise  
  
### batchDeactivateAdUnits(request, callback)
    
    
    public batchDeactivateAdUnits(request: google.ads.admanager.v1.IBatchDeactivateAdUnitsRequest, callback: google.ads.admanager.v1.AdUnitService.BatchDeactivateAdUnitsCallback): void;

Calls BatchDeactivateAdUnits.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeactivateAdUnitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchdeactivateadunitsrequest)`   
BatchDeactivateAdUnitsRequest message or plain object  
`callback` |  `[BatchDeactivateAdUnitsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchDeactivateAdUnitsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchDeactivateAdUnits(request)
    
    
    public batchDeactivateAdUnits(request: google.ads.admanager.v1.IBatchDeactivateAdUnitsRequest): Promise<google.ads.admanager.v1.BatchDeactivateAdUnitsResponse>;

Calls BatchDeactivateAdUnits.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeactivateAdUnitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchdeactivateadunitsrequest)`   
BatchDeactivateAdUnitsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchDeactivateAdUnitsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchdeactivateadunitsresponse)>` | Promise  
  
### batchUpdateAdUnits(request, callback)
    
    
    public batchUpdateAdUnits(request: google.ads.admanager.v1.IBatchUpdateAdUnitsRequest, callback: google.ads.admanager.v1.AdUnitService.BatchUpdateAdUnitsCallback): void;

Calls BatchUpdateAdUnits.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateAdUnitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchupdateadunitsrequest)`   
BatchUpdateAdUnitsRequest message or plain object  
`callback` |  `[BatchUpdateAdUnitsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchUpdateAdUnitsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchUpdateAdUnits(request)
    
    
    public batchUpdateAdUnits(request: google.ads.admanager.v1.IBatchUpdateAdUnitsRequest): Promise<google.ads.admanager.v1.BatchUpdateAdUnitsResponse>;

Calls BatchUpdateAdUnits.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateAdUnitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchupdateadunitsrequest)`   
BatchUpdateAdUnitsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchUpdateAdUnitsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchupdateadunitsresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AdUnitService;

Creates new AdUnitService service using the specified rpc implementation.

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
`[AdUnitService](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adunitservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAdUnit(request, callback)
    
    
    public createAdUnit(request: google.ads.admanager.v1.ICreateAdUnitRequest, callback: google.ads.admanager.v1.AdUnitService.CreateAdUnitCallback): void;

Calls CreateAdUnit.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAdUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.icreateadunitrequest)`   
CreateAdUnitRequest message or plain object  
`callback` |  `[CreateAdUnitCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and AdUnit  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAdUnit(request)
    
    
    public createAdUnit(request: google.ads.admanager.v1.ICreateAdUnitRequest): Promise<google.ads.admanager.v1.AdUnit>;

Calls CreateAdUnit.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAdUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.icreateadunitrequest)`   
CreateAdUnitRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.AdUnit](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adunit)>` | Promise  
  
### getAdUnit(request, callback)
    
    
    public getAdUnit(request: google.ads.admanager.v1.IGetAdUnitRequest, callback: google.ads.admanager.v1.AdUnitService.GetAdUnitCallback): void;

Calls GetAdUnit.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAdUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.igetadunitrequest)`   
GetAdUnitRequest message or plain object  
`callback` |  `[GetAdUnitCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and AdUnit  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAdUnit(request)
    
    
    public getAdUnit(request: google.ads.admanager.v1.IGetAdUnitRequest): Promise<google.ads.admanager.v1.AdUnit>;

Calls GetAdUnit.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAdUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.igetadunitrequest)`   
GetAdUnitRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.AdUnit](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adunit)>` | Promise  
  
### listAdUnits(request, callback)
    
    
    public listAdUnits(request: google.ads.admanager.v1.IListAdUnitsRequest, callback: google.ads.admanager.v1.AdUnitService.ListAdUnitsCallback): void;

Calls ListAdUnits.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAdUnitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistadunitsrequest)`   
ListAdUnitsRequest message or plain object  
`callback` |  `[ListAdUnitsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAdUnitsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAdUnits(request)
    
    
    public listAdUnits(request: google.ads.admanager.v1.IListAdUnitsRequest): Promise<google.ads.admanager.v1.ListAdUnitsResponse>;

Calls ListAdUnits.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAdUnitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistadunitsrequest)`   
ListAdUnitsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.ListAdUnitsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.listadunitsresponse)>` | Promise  
  
### listAdUnitSizes(request, callback)
    
    
    public listAdUnitSizes(request: google.ads.admanager.v1.IListAdUnitSizesRequest, callback: google.ads.admanager.v1.AdUnitService.ListAdUnitSizesCallback): void;

Calls ListAdUnitSizes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAdUnitSizesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistadunitsizesrequest)`   
ListAdUnitSizesRequest message or plain object  
`callback` |  `[ListAdUnitSizesCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAdUnitSizesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAdUnitSizes(request)
    
    
    public listAdUnitSizes(request: google.ads.admanager.v1.IListAdUnitSizesRequest): Promise<google.ads.admanager.v1.ListAdUnitSizesResponse>;

Calls ListAdUnitSizes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAdUnitSizesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistadunitsizesrequest)`   
ListAdUnitSizesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.ListAdUnitSizesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.listadunitsizesresponse)>` | Promise  
  
### updateAdUnit(request, callback)
    
    
    public updateAdUnit(request: google.ads.admanager.v1.IUpdateAdUnitRequest, callback: google.ads.admanager.v1.AdUnitService.UpdateAdUnitCallback): void;

Calls UpdateAdUnit.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAdUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iupdateadunitrequest)`   
UpdateAdUnitRequest message or plain object  
`callback` |  `[UpdateAdUnitCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and AdUnit  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAdUnit(request)
    
    
    public updateAdUnit(request: google.ads.admanager.v1.IUpdateAdUnitRequest): Promise<google.ads.admanager.v1.AdUnit>;

Calls UpdateAdUnit.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAdUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iupdateadunitrequest)`   
UpdateAdUnitRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.AdUnit](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adunit)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
