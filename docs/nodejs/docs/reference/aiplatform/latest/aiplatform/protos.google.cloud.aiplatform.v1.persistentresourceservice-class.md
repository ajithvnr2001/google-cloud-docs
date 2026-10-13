---
url: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.persistentresourceservice-class
title: Class protos.google.cloud.aiplatform.v1.PersistentResourceService (7.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:14:54.155869+00:00
---

# Class protos.google.cloud.aiplatform.v1.PersistentResourceService (7.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.persistentresourceservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.aiplatform.v1.PersistentResourceService (7.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.4.1 (latest)  7.3.0  6.10.0  6.9.0  6.8.1  6.6.0  6.4.0  6.3.0  6.2.0  6.1.0  6.0.0  5.14.0  5.13.0  3.15.0  3.13.0  3.11.0  3.10.1  3.9.0  3.7.0  3.6.0  3.4.0  3.3.0  3.0.0  2.12.0  2.11.0  2.10.0  2.7.0  2.6.1  2.5.0  2.3.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0  1.11.0  1.7.2 

Represents a PersistentResourceService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.aiplatform.v1.PersistentResourceService

## Package

[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new PersistentResourceService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): PersistentResourceService;

Creates new PersistentResourceService service using the specified rpc implementation.

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
`[PersistentResourceService](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.persistentresourceservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createPersistentResource(request, callback)
    
    
    public createPersistentResource(request: google.cloud.aiplatform.v1.ICreatePersistentResourceRequest, callback: google.cloud.aiplatform.v1.PersistentResourceService.CreatePersistentResourceCallback): void;

Calls CreatePersistentResource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePersistentResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.icreatepersistentresourcerequest)`   
CreatePersistentResourceRequest message or plain object  
`callback` |  `[CreatePersistentResourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createPersistentResource(request)
    
    
    public createPersistentResource(request: google.cloud.aiplatform.v1.ICreatePersistentResourceRequest): Promise<google.longrunning.Operation>;

Calls CreatePersistentResource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreatePersistentResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.icreatepersistentresourcerequest)`   
CreatePersistentResourceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### deletePersistentResource(request, callback)
    
    
    public deletePersistentResource(request: google.cloud.aiplatform.v1.IDeletePersistentResourceRequest, callback: google.cloud.aiplatform.v1.PersistentResourceService.DeletePersistentResourceCallback): void;

Calls DeletePersistentResource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePersistentResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideletepersistentresourcerequest)`   
DeletePersistentResourceRequest message or plain object  
`callback` |  `[DeletePersistentResourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePersistentResource(request)
    
    
    public deletePersistentResource(request: google.cloud.aiplatform.v1.IDeletePersistentResourceRequest): Promise<google.longrunning.Operation>;

Calls DeletePersistentResource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeletePersistentResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideletepersistentresourcerequest)`   
DeletePersistentResourceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### getPersistentResource(request, callback)
    
    
    public getPersistentResource(request: google.cloud.aiplatform.v1.IGetPersistentResourceRequest, callback: google.cloud.aiplatform.v1.PersistentResourceService.GetPersistentResourceCallback): void;

Calls GetPersistentResource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPersistentResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.igetpersistentresourcerequest)`   
GetPersistentResourceRequest message or plain object  
`callback` |  `[GetPersistentResourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and PersistentResource  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPersistentResource(request)
    
    
    public getPersistentResource(request: google.cloud.aiplatform.v1.IGetPersistentResourceRequest): Promise<google.cloud.aiplatform.v1.PersistentResource>;

Calls GetPersistentResource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetPersistentResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.igetpersistentresourcerequest)`   
GetPersistentResourceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.PersistentResource](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.persistentresource-class)>` | Promise  
  
### listPersistentResources(request, callback)
    
    
    public listPersistentResources(request: google.cloud.aiplatform.v1.IListPersistentResourcesRequest, callback: google.cloud.aiplatform.v1.PersistentResourceService.ListPersistentResourcesCallback): void;

Calls ListPersistentResources.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPersistentResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ilistpersistentresourcesrequest)`   
ListPersistentResourcesRequest message or plain object  
`callback` |  `[ListPersistentResourcesCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListPersistentResourcesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPersistentResources(request)
    
    
    public listPersistentResources(request: google.cloud.aiplatform.v1.IListPersistentResourcesRequest): Promise<google.cloud.aiplatform.v1.ListPersistentResourcesResponse>;

Calls ListPersistentResources.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListPersistentResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ilistpersistentresourcesrequest)`   
ListPersistentResourcesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.ListPersistentResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.listpersistentresourcesresponse)>` | Promise  
  
### rebootPersistentResource(request, callback)
    
    
    public rebootPersistentResource(request: google.cloud.aiplatform.v1.IRebootPersistentResourceRequest, callback: google.cloud.aiplatform.v1.PersistentResourceService.RebootPersistentResourceCallback): void;

Calls RebootPersistentResource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRebootPersistentResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.irebootpersistentresourcerequest)`   
RebootPersistentResourceRequest message or plain object  
`callback` |  `[RebootPersistentResourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### rebootPersistentResource(request)
    
    
    public rebootPersistentResource(request: google.cloud.aiplatform.v1.IRebootPersistentResourceRequest): Promise<google.longrunning.Operation>;

Calls RebootPersistentResource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRebootPersistentResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.irebootpersistentresourcerequest)`   
RebootPersistentResourceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### updatePersistentResource(request, callback)
    
    
    public updatePersistentResource(request: google.cloud.aiplatform.v1.IUpdatePersistentResourceRequest, callback: google.cloud.aiplatform.v1.PersistentResourceService.UpdatePersistentResourceCallback): void;

Calls UpdatePersistentResource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePersistentResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iupdatepersistentresourcerequest)`   
UpdatePersistentResourceRequest message or plain object  
`callback` |  `[UpdatePersistentResourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updatePersistentResource(request)
    
    
    public updatePersistentResource(request: google.cloud.aiplatform.v1.IUpdatePersistentResourceRequest): Promise<google.longrunning.Operation>;

Calls UpdatePersistentResource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePersistentResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iupdatepersistentresourcerequest)`   
UpdatePersistentResourceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
