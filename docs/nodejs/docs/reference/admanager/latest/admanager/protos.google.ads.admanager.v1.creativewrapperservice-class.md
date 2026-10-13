---
url: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.creativewrapperservice-class
title: Class protos.google.ads.admanager.v1.CreativeWrapperService (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:39:05.281567+00:00
---

# Class protos.google.ads.admanager.v1.CreativeWrapperService (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.creativewrapperservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.admanager.v1.CreativeWrapperService (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.12.0  0.11.0  0.7.0  0.6.0  0.1.0 

Represents a CreativeWrapperService

## Inheritance

$protobuf.rpc.Service > protos.google.ads.admanager.v1.CreativeWrapperService

## Package

[@google-ads/admanager](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new CreativeWrapperService service.

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

### batchActivateCreativeWrappers(request, callback)
    
    
    public batchActivateCreativeWrappers(request: google.ads.admanager.v1.IBatchActivateCreativeWrappersRequest, callback: google.ads.admanager.v1.CreativeWrapperService.BatchActivateCreativeWrappersCallback): void;

Calls BatchActivateCreativeWrappers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchActivateCreativeWrappersRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchactivatecreativewrappersrequest)`   
BatchActivateCreativeWrappersRequest message or plain object  
`callback` |  `[BatchActivateCreativeWrappersCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchActivateCreativeWrappersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchActivateCreativeWrappers(request)
    
    
    public batchActivateCreativeWrappers(request: google.ads.admanager.v1.IBatchActivateCreativeWrappersRequest): Promise<google.ads.admanager.v1.BatchActivateCreativeWrappersResponse>;

Calls BatchActivateCreativeWrappers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchActivateCreativeWrappersRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchactivatecreativewrappersrequest)`   
BatchActivateCreativeWrappersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchActivateCreativeWrappersResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchactivatecreativewrappersresponse)>` | Promise  
  
### batchCreateCreativeWrappers(request, callback)
    
    
    public batchCreateCreativeWrappers(request: google.ads.admanager.v1.IBatchCreateCreativeWrappersRequest, callback: google.ads.admanager.v1.CreativeWrapperService.BatchCreateCreativeWrappersCallback): void;

Calls BatchCreateCreativeWrappers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateCreativeWrappersRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchcreatecreativewrappersrequest)`   
BatchCreateCreativeWrappersRequest message or plain object  
`callback` |  `[BatchCreateCreativeWrappersCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchCreateCreativeWrappersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateCreativeWrappers(request)
    
    
    public batchCreateCreativeWrappers(request: google.ads.admanager.v1.IBatchCreateCreativeWrappersRequest): Promise<google.ads.admanager.v1.BatchCreateCreativeWrappersResponse>;

Calls BatchCreateCreativeWrappers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateCreativeWrappersRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchcreatecreativewrappersrequest)`   
BatchCreateCreativeWrappersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchCreateCreativeWrappersResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchcreatecreativewrappersresponse)>` | Promise  
  
### batchDeactivateCreativeWrappers(request, callback)
    
    
    public batchDeactivateCreativeWrappers(request: google.ads.admanager.v1.IBatchDeactivateCreativeWrappersRequest, callback: google.ads.admanager.v1.CreativeWrapperService.BatchDeactivateCreativeWrappersCallback): void;

Calls BatchDeactivateCreativeWrappers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeactivateCreativeWrappersRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchdeactivatecreativewrappersrequest)`   
BatchDeactivateCreativeWrappersRequest message or plain object  
`callback` |  `[BatchDeactivateCreativeWrappersCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchDeactivateCreativeWrappersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchDeactivateCreativeWrappers(request)
    
    
    public batchDeactivateCreativeWrappers(request: google.ads.admanager.v1.IBatchDeactivateCreativeWrappersRequest): Promise<google.ads.admanager.v1.BatchDeactivateCreativeWrappersResponse>;

Calls BatchDeactivateCreativeWrappers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeactivateCreativeWrappersRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchdeactivatecreativewrappersrequest)`   
BatchDeactivateCreativeWrappersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchDeactivateCreativeWrappersResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchdeactivatecreativewrappersresponse)>` | Promise  
  
### batchUpdateCreativeWrappers(request, callback)
    
    
    public batchUpdateCreativeWrappers(request: google.ads.admanager.v1.IBatchUpdateCreativeWrappersRequest, callback: google.ads.admanager.v1.CreativeWrapperService.BatchUpdateCreativeWrappersCallback): void;

Calls BatchUpdateCreativeWrappers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateCreativeWrappersRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchupdatecreativewrappersrequest)`   
BatchUpdateCreativeWrappersRequest message or plain object  
`callback` |  `[BatchUpdateCreativeWrappersCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchUpdateCreativeWrappersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchUpdateCreativeWrappers(request)
    
    
    public batchUpdateCreativeWrappers(request: google.ads.admanager.v1.IBatchUpdateCreativeWrappersRequest): Promise<google.ads.admanager.v1.BatchUpdateCreativeWrappersResponse>;

Calls BatchUpdateCreativeWrappers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateCreativeWrappersRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchupdatecreativewrappersrequest)`   
BatchUpdateCreativeWrappersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchUpdateCreativeWrappersResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchupdatecreativewrappersresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): CreativeWrapperService;

Creates new CreativeWrapperService service using the specified rpc implementation.

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
`[CreativeWrapperService](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.creativewrapperservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createCreativeWrapper(request, callback)
    
    
    public createCreativeWrapper(request: google.ads.admanager.v1.ICreateCreativeWrapperRequest, callback: google.ads.admanager.v1.CreativeWrapperService.CreateCreativeWrapperCallback): void;

Calls CreateCreativeWrapper.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCreativeWrapperRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.icreatecreativewrapperrequest)`   
CreateCreativeWrapperRequest message or plain object  
`callback` |  `[CreateCreativeWrapperCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and CreativeWrapper  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCreativeWrapper(request)
    
    
    public createCreativeWrapper(request: google.ads.admanager.v1.ICreateCreativeWrapperRequest): Promise<google.ads.admanager.v1.CreativeWrapper>;

Calls CreateCreativeWrapper.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCreativeWrapperRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.icreatecreativewrapperrequest)`   
CreateCreativeWrapperRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.CreativeWrapper](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.creativewrapper)>` | Promise  
  
### getCreativeWrapper(request, callback)
    
    
    public getCreativeWrapper(request: google.ads.admanager.v1.IGetCreativeWrapperRequest, callback: google.ads.admanager.v1.CreativeWrapperService.GetCreativeWrapperCallback): void;

Calls GetCreativeWrapper.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCreativeWrapperRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.igetcreativewrapperrequest)`   
GetCreativeWrapperRequest message or plain object  
`callback` |  `[GetCreativeWrapperCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and CreativeWrapper  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCreativeWrapper(request)
    
    
    public getCreativeWrapper(request: google.ads.admanager.v1.IGetCreativeWrapperRequest): Promise<google.ads.admanager.v1.CreativeWrapper>;

Calls GetCreativeWrapper.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCreativeWrapperRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.igetcreativewrapperrequest)`   
GetCreativeWrapperRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.CreativeWrapper](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.creativewrapper)>` | Promise  
  
### listCreativeWrappers(request, callback)
    
    
    public listCreativeWrappers(request: google.ads.admanager.v1.IListCreativeWrappersRequest, callback: google.ads.admanager.v1.CreativeWrapperService.ListCreativeWrappersCallback): void;

Calls ListCreativeWrappers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCreativeWrappersRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistcreativewrappersrequest)`   
ListCreativeWrappersRequest message or plain object  
`callback` |  `[ListCreativeWrappersCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCreativeWrappersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCreativeWrappers(request)
    
    
    public listCreativeWrappers(request: google.ads.admanager.v1.IListCreativeWrappersRequest): Promise<google.ads.admanager.v1.ListCreativeWrappersResponse>;

Calls ListCreativeWrappers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCreativeWrappersRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistcreativewrappersrequest)`   
ListCreativeWrappersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.ListCreativeWrappersResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.listcreativewrappersresponse)>` | Promise  
  
### updateCreativeWrapper(request, callback)
    
    
    public updateCreativeWrapper(request: google.ads.admanager.v1.IUpdateCreativeWrapperRequest, callback: google.ads.admanager.v1.CreativeWrapperService.UpdateCreativeWrapperCallback): void;

Calls UpdateCreativeWrapper.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCreativeWrapperRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iupdatecreativewrapperrequest)`   
UpdateCreativeWrapperRequest message or plain object  
`callback` |  `[UpdateCreativeWrapperCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and CreativeWrapper  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCreativeWrapper(request)
    
    
    public updateCreativeWrapper(request: google.ads.admanager.v1.IUpdateCreativeWrapperRequest): Promise<google.ads.admanager.v1.CreativeWrapper>;

Calls UpdateCreativeWrapper.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCreativeWrapperRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iupdatecreativewrapperrequest)`   
UpdateCreativeWrapperRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.CreativeWrapper](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.creativewrapper)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
