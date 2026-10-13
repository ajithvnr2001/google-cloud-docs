---
url: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.specialistpoolservice-class
title: Class protos.google.cloud.aiplatform.v1beta1.SpecialistPoolService (7.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:41.707371+00:00
---

# Class protos.google.cloud.aiplatform.v1beta1.SpecialistPoolService (7.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.specialistpoolservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.aiplatform.v1beta1.SpecialistPoolService (7.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.4.1 (latest)  7.3.0  6.10.0  6.9.0  6.8.1  6.6.0  6.4.0  6.3.0  6.2.0  6.1.0  6.0.0  5.14.0  5.13.0  3.15.0  3.13.0  3.11.0  3.10.1  3.9.0  3.7.0  3.6.0  3.4.0  3.3.0  3.0.0  2.12.0  2.11.0  2.10.0  2.7.0  2.6.1  2.5.0  2.3.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0  1.11.0  1.7.2 

Represents a SpecialistPoolService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.aiplatform.v1beta1.SpecialistPoolService

## Package

[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new SpecialistPoolService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): SpecialistPoolService;

Creates new SpecialistPoolService service using the specified rpc implementation.

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
`[SpecialistPoolService](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.specialistpoolservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createSpecialistPool(request, callback)
    
    
    public createSpecialistPool(request: google.cloud.aiplatform.v1beta1.ICreateSpecialistPoolRequest, callback: google.cloud.aiplatform.v1beta1.SpecialistPoolService.CreateSpecialistPoolCallback): void;

Calls CreateSpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSpecialistPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatespecialistpoolrequest)`   
CreateSpecialistPoolRequest message or plain object  
`callback` |  `[CreateSpecialistPoolCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSpecialistPool(request)
    
    
    public createSpecialistPool(request: google.cloud.aiplatform.v1beta1.ICreateSpecialistPoolRequest): Promise<google.longrunning.Operation>;

Calls CreateSpecialistPool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateSpecialistPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatespecialistpoolrequest)`   
CreateSpecialistPoolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### deleteSpecialistPool(request, callback)
    
    
    public deleteSpecialistPool(request: google.cloud.aiplatform.v1beta1.IDeleteSpecialistPoolRequest, callback: google.cloud.aiplatform.v1beta1.SpecialistPoolService.DeleteSpecialistPoolCallback): void;

Calls DeleteSpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSpecialistPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletespecialistpoolrequest)`   
DeleteSpecialistPoolRequest message or plain object  
`callback` |  `[DeleteSpecialistPoolCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSpecialistPool(request)
    
    
    public deleteSpecialistPool(request: google.cloud.aiplatform.v1beta1.IDeleteSpecialistPoolRequest): Promise<google.longrunning.Operation>;

Calls DeleteSpecialistPool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSpecialistPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletespecialistpoolrequest)`   
DeleteSpecialistPoolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### getSpecialistPool(request, callback)
    
    
    public getSpecialistPool(request: google.cloud.aiplatform.v1beta1.IGetSpecialistPoolRequest, callback: google.cloud.aiplatform.v1beta1.SpecialistPoolService.GetSpecialistPoolCallback): void;

Calls GetSpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSpecialistPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetspecialistpoolrequest)`   
GetSpecialistPoolRequest message or plain object  
`callback` |  `[GetSpecialistPoolCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and SpecialistPool  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSpecialistPool(request)
    
    
    public getSpecialistPool(request: google.cloud.aiplatform.v1beta1.IGetSpecialistPoolRequest): Promise<google.cloud.aiplatform.v1beta1.SpecialistPool>;

Calls GetSpecialistPool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSpecialistPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetspecialistpoolrequest)`   
GetSpecialistPoolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.SpecialistPool](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.specialistpool)>` | Promise  
  
### listSpecialistPools(request, callback)
    
    
    public listSpecialistPools(request: google.cloud.aiplatform.v1beta1.IListSpecialistPoolsRequest, callback: google.cloud.aiplatform.v1beta1.SpecialistPoolService.ListSpecialistPoolsCallback): void;

Calls ListSpecialistPools.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSpecialistPoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistspecialistpoolsrequest)`   
ListSpecialistPoolsRequest message or plain object  
`callback` |  `[ListSpecialistPoolsCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSpecialistPoolsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSpecialistPools(request)
    
    
    public listSpecialistPools(request: google.cloud.aiplatform.v1beta1.IListSpecialistPoolsRequest): Promise<google.cloud.aiplatform.v1beta1.ListSpecialistPoolsResponse>;

Calls ListSpecialistPools.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSpecialistPoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistspecialistpoolsrequest)`   
ListSpecialistPoolsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.ListSpecialistPoolsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.listspecialistpoolsresponse)>` | Promise  
  
### updateSpecialistPool(request, callback)
    
    
    public updateSpecialistPool(request: google.cloud.aiplatform.v1beta1.IUpdateSpecialistPoolRequest, callback: google.cloud.aiplatform.v1beta1.SpecialistPoolService.UpdateSpecialistPoolCallback): void;

Calls UpdateSpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSpecialistPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatespecialistpoolrequest)`   
UpdateSpecialistPoolRequest message or plain object  
`callback` |  `[UpdateSpecialistPoolCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSpecialistPool(request)
    
    
    public updateSpecialistPool(request: google.cloud.aiplatform.v1beta1.IUpdateSpecialistPoolRequest): Promise<google.longrunning.Operation>;

Calls UpdateSpecialistPool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSpecialistPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatespecialistpoolrequest)`   
UpdateSpecialistPoolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
