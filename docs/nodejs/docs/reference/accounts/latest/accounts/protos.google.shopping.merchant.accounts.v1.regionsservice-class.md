---
url: https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.regionsservice-class
title: Class protos.google.shopping.merchant.accounts.v1.RegionsService (4.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:31:34.622280+00:00
---

# Class protos.google.shopping.merchant.accounts.v1.RegionsService (4.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.regionsservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.accounts.v1.RegionsService (4.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.1 (latest)  3.2.0  2.2.0  1.0.0 

Represents a RegionsService

## Inheritance

$protobuf.rpc.Service > protos.google.shopping.merchant.accounts.v1.RegionsService

## Package

[@google-shopping/accounts](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new RegionsService service.

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

### batchCreateRegions(request, callback)
    
    
    public batchCreateRegions(request: google.shopping.merchant.accounts.v1.IBatchCreateRegionsRequest, callback: google.shopping.merchant.accounts.v1.RegionsService.BatchCreateRegionsCallback): void;

Calls BatchCreateRegions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateRegionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.ibatchcreateregionsrequest)`   
BatchCreateRegionsRequest message or plain object  
`callback` |  `[BatchCreateRegionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchCreateRegionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateRegions(request)
    
    
    public batchCreateRegions(request: google.shopping.merchant.accounts.v1.IBatchCreateRegionsRequest): Promise<google.shopping.merchant.accounts.v1.BatchCreateRegionsResponse>;

Calls BatchCreateRegions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateRegionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.ibatchcreateregionsrequest)`   
BatchCreateRegionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.accounts.v1.BatchCreateRegionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.batchcreateregionsresponse)>` | Promise  
  
### batchDeleteRegions(request, callback)
    
    
    public batchDeleteRegions(request: google.shopping.merchant.accounts.v1.IBatchDeleteRegionsRequest, callback: google.shopping.merchant.accounts.v1.RegionsService.BatchDeleteRegionsCallback): void;

Calls BatchDeleteRegions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteRegionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.ibatchdeleteregionsrequest)`   
BatchDeleteRegionsRequest message or plain object  
`callback` |  `[BatchDeleteRegionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchDeleteRegions(request)
    
    
    public batchDeleteRegions(request: google.shopping.merchant.accounts.v1.IBatchDeleteRegionsRequest): Promise<google.protobuf.Empty>;

Calls BatchDeleteRegions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteRegionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.ibatchdeleteregionsrequest)`   
BatchDeleteRegionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.protobuf.empty)>` | Promise  
  
### batchUpdateRegions(request, callback)
    
    
    public batchUpdateRegions(request: google.shopping.merchant.accounts.v1.IBatchUpdateRegionsRequest, callback: google.shopping.merchant.accounts.v1.RegionsService.BatchUpdateRegionsCallback): void;

Calls BatchUpdateRegions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateRegionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.ibatchupdateregionsrequest)`   
BatchUpdateRegionsRequest message or plain object  
`callback` |  `[BatchUpdateRegionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchUpdateRegionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchUpdateRegions(request)
    
    
    public batchUpdateRegions(request: google.shopping.merchant.accounts.v1.IBatchUpdateRegionsRequest): Promise<google.shopping.merchant.accounts.v1.BatchUpdateRegionsResponse>;

Calls BatchUpdateRegions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateRegionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.ibatchupdateregionsrequest)`   
BatchUpdateRegionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.accounts.v1.BatchUpdateRegionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.batchupdateregionsresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): RegionsService;

Creates new RegionsService service using the specified rpc implementation.

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
`[RegionsService](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.regionsservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createRegion(request, callback)
    
    
    public createRegion(request: google.shopping.merchant.accounts.v1.ICreateRegionRequest, callback: google.shopping.merchant.accounts.v1.RegionsService.CreateRegionCallback): void;

Calls CreateRegion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRegionRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.icreateregionrequest)`   
CreateRegionRequest message or plain object  
`callback` |  `[CreateRegionCallback](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)`   
Node-style callback called with the error, if any, and Region  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createRegion(request)
    
    
    public createRegion(request: google.shopping.merchant.accounts.v1.ICreateRegionRequest): Promise<google.shopping.merchant.accounts.v1.Region>;

Calls CreateRegion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateRegionRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.icreateregionrequest)`   
CreateRegionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.accounts.v1.Region](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.region-class)>` | Promise  
  
### deleteRegion(request, callback)
    
    
    public deleteRegion(request: google.shopping.merchant.accounts.v1.IDeleteRegionRequest, callback: google.shopping.merchant.accounts.v1.RegionsService.DeleteRegionCallback): void;

Calls DeleteRegion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRegionRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.ideleteregionrequest)`   
DeleteRegionRequest message or plain object  
`callback` |  `[DeleteRegionCallback](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteRegion(request)
    
    
    public deleteRegion(request: google.shopping.merchant.accounts.v1.IDeleteRegionRequest): Promise<google.protobuf.Empty>;

Calls DeleteRegion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRegionRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.ideleteregionrequest)`   
DeleteRegionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.protobuf.empty)>` | Promise  
  
### getRegion(request, callback)
    
    
    public getRegion(request: google.shopping.merchant.accounts.v1.IGetRegionRequest, callback: google.shopping.merchant.accounts.v1.RegionsService.GetRegionCallback): void;

Calls GetRegion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRegionRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.igetregionrequest)`   
GetRegionRequest message or plain object  
`callback` |  `[GetRegionCallback](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)`   
Node-style callback called with the error, if any, and Region  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRegion(request)
    
    
    public getRegion(request: google.shopping.merchant.accounts.v1.IGetRegionRequest): Promise<google.shopping.merchant.accounts.v1.Region>;

Calls GetRegion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetRegionRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.igetregionrequest)`   
GetRegionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.accounts.v1.Region](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.region-class)>` | Promise  
  
### listRegions(request, callback)
    
    
    public listRegions(request: google.shopping.merchant.accounts.v1.IListRegionsRequest, callback: google.shopping.merchant.accounts.v1.RegionsService.ListRegionsCallback): void;

Calls ListRegions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRegionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.ilistregionsrequest)`   
ListRegionsRequest message or plain object  
`callback` |  `[ListRegionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)`   
Node-style callback called with the error, if any, and ListRegionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRegions(request)
    
    
    public listRegions(request: google.shopping.merchant.accounts.v1.IListRegionsRequest): Promise<google.shopping.merchant.accounts.v1.ListRegionsResponse>;

Calls ListRegions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListRegionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.ilistregionsrequest)`   
ListRegionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.accounts.v1.ListRegionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.listregionsresponse)>` | Promise  
  
### updateRegion(request, callback)
    
    
    public updateRegion(request: google.shopping.merchant.accounts.v1.IUpdateRegionRequest, callback: google.shopping.merchant.accounts.v1.RegionsService.UpdateRegionCallback): void;

Calls UpdateRegion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateRegionRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.iupdateregionrequest)`   
UpdateRegionRequest message or plain object  
`callback` |  `[UpdateRegionCallback](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)`   
Node-style callback called with the error, if any, and Region  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateRegion(request)
    
    
    public updateRegion(request: google.shopping.merchant.accounts.v1.IUpdateRegionRequest): Promise<google.shopping.merchant.accounts.v1.Region>;

Calls UpdateRegion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateRegionRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.iupdateregionrequest)`   
UpdateRegionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.accounts.v1.Region](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.region-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
