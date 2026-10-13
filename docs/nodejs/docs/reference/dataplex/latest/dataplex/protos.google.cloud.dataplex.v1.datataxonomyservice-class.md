---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.datataxonomyservice-class
title: Class protos.google.cloud.dataplex.v1.DataTaxonomyService (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:33:42.422818+00:00
---

# Class protos.google.cloud.dataplex.v1.DataTaxonomyService (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.datataxonomyservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataplex.v1.DataTaxonomyService (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.4.0  5.3.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.5.1  3.2.0  3.1.0  2.4.0  2.3.2  2.2.2  2.1.1  1.2.0  1.1.0  1.0.0 

Represents a DataTaxonomyService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dataplex.v1.DataTaxonomyService

## Package

[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DataTaxonomyService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DataTaxonomyService;

Creates new DataTaxonomyService service using the specified rpc implementation.

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
`[DataTaxonomyService](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.datataxonomyservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createDataAttribute(request, callback)
    
    
    public createDataAttribute(request: google.cloud.dataplex.v1.ICreateDataAttributeRequest, callback: google.cloud.dataplex.v1.DataTaxonomyService.CreateDataAttributeCallback): void;

Calls CreateDataAttribute.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataAttributeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatedataattributerequest)`   
CreateDataAttributeRequest message or plain object  
`callback` |  `[CreateDataAttributeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataAttribute(request)
    
    
    public createDataAttribute(request: google.cloud.dataplex.v1.ICreateDataAttributeRequest): Promise<google.longrunning.Operation>;

Calls CreateDataAttribute.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataAttributeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatedataattributerequest)`   
CreateDataAttributeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### createDataAttributeBinding(request, callback)
    
    
    public createDataAttributeBinding(request: google.cloud.dataplex.v1.ICreateDataAttributeBindingRequest, callback: google.cloud.dataplex.v1.DataTaxonomyService.CreateDataAttributeBindingCallback): void;

Calls CreateDataAttributeBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataAttributeBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatedataattributebindingrequest)`   
CreateDataAttributeBindingRequest message or plain object  
`callback` |  `[CreateDataAttributeBindingCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataAttributeBinding(request)
    
    
    public createDataAttributeBinding(request: google.cloud.dataplex.v1.ICreateDataAttributeBindingRequest): Promise<google.longrunning.Operation>;

Calls CreateDataAttributeBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataAttributeBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatedataattributebindingrequest)`   
CreateDataAttributeBindingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### createDataTaxonomy(request, callback)
    
    
    public createDataTaxonomy(request: google.cloud.dataplex.v1.ICreateDataTaxonomyRequest, callback: google.cloud.dataplex.v1.DataTaxonomyService.CreateDataTaxonomyCallback): void;

Calls CreateDataTaxonomy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataTaxonomyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatedatataxonomyrequest)`   
CreateDataTaxonomyRequest message or plain object  
`callback` |  `[CreateDataTaxonomyCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataTaxonomy(request)
    
    
    public createDataTaxonomy(request: google.cloud.dataplex.v1.ICreateDataTaxonomyRequest): Promise<google.longrunning.Operation>;

Calls CreateDataTaxonomy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataTaxonomyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatedatataxonomyrequest)`   
CreateDataTaxonomyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### deleteDataAttribute(request, callback)
    
    
    public deleteDataAttribute(request: google.cloud.dataplex.v1.IDeleteDataAttributeRequest, callback: google.cloud.dataplex.v1.DataTaxonomyService.DeleteDataAttributeCallback): void;

Calls DeleteDataAttribute.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataAttributeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideletedataattributerequest)`   
DeleteDataAttributeRequest message or plain object  
`callback` |  `[DeleteDataAttributeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataAttribute(request)
    
    
    public deleteDataAttribute(request: google.cloud.dataplex.v1.IDeleteDataAttributeRequest): Promise<google.longrunning.Operation>;

Calls DeleteDataAttribute.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataAttributeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideletedataattributerequest)`   
DeleteDataAttributeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### deleteDataAttributeBinding(request, callback)
    
    
    public deleteDataAttributeBinding(request: google.cloud.dataplex.v1.IDeleteDataAttributeBindingRequest, callback: google.cloud.dataplex.v1.DataTaxonomyService.DeleteDataAttributeBindingCallback): void;

Calls DeleteDataAttributeBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataAttributeBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideletedataattributebindingrequest)`   
DeleteDataAttributeBindingRequest message or plain object  
`callback` |  `[DeleteDataAttributeBindingCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataAttributeBinding(request)
    
    
    public deleteDataAttributeBinding(request: google.cloud.dataplex.v1.IDeleteDataAttributeBindingRequest): Promise<google.longrunning.Operation>;

Calls DeleteDataAttributeBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataAttributeBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideletedataattributebindingrequest)`   
DeleteDataAttributeBindingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### deleteDataTaxonomy(request, callback)
    
    
    public deleteDataTaxonomy(request: google.cloud.dataplex.v1.IDeleteDataTaxonomyRequest, callback: google.cloud.dataplex.v1.DataTaxonomyService.DeleteDataTaxonomyCallback): void;

Calls DeleteDataTaxonomy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataTaxonomyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideletedatataxonomyrequest)`   
DeleteDataTaxonomyRequest message or plain object  
`callback` |  `[DeleteDataTaxonomyCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataTaxonomy(request)
    
    
    public deleteDataTaxonomy(request: google.cloud.dataplex.v1.IDeleteDataTaxonomyRequest): Promise<google.longrunning.Operation>;

Calls DeleteDataTaxonomy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataTaxonomyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideletedatataxonomyrequest)`   
DeleteDataTaxonomyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### getDataAttribute(request, callback)
    
    
    public getDataAttribute(request: google.cloud.dataplex.v1.IGetDataAttributeRequest, callback: google.cloud.dataplex.v1.DataTaxonomyService.GetDataAttributeCallback): void;

Calls GetDataAttribute.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataAttributeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetdataattributerequest)`   
GetDataAttributeRequest message or plain object  
`callback` |  `[GetDataAttributeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and DataAttribute  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataAttribute(request)
    
    
    public getDataAttribute(request: google.cloud.dataplex.v1.IGetDataAttributeRequest): Promise<google.cloud.dataplex.v1.DataAttribute>;

Calls GetDataAttribute.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataAttributeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetdataattributerequest)`   
GetDataAttributeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.DataAttribute](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataattribute)>` | Promise  
  
### getDataAttributeBinding(request, callback)
    
    
    public getDataAttributeBinding(request: google.cloud.dataplex.v1.IGetDataAttributeBindingRequest, callback: google.cloud.dataplex.v1.DataTaxonomyService.GetDataAttributeBindingCallback): void;

Calls GetDataAttributeBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataAttributeBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetdataattributebindingrequest)`   
GetDataAttributeBindingRequest message or plain object  
`callback` |  `[GetDataAttributeBindingCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and DataAttributeBinding  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataAttributeBinding(request)
    
    
    public getDataAttributeBinding(request: google.cloud.dataplex.v1.IGetDataAttributeBindingRequest): Promise<google.cloud.dataplex.v1.DataAttributeBinding>;

Calls GetDataAttributeBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataAttributeBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetdataattributebindingrequest)`   
GetDataAttributeBindingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.DataAttributeBinding](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataattributebinding-class)>` | Promise  
  
### getDataTaxonomy(request, callback)
    
    
    public getDataTaxonomy(request: google.cloud.dataplex.v1.IGetDataTaxonomyRequest, callback: google.cloud.dataplex.v1.DataTaxonomyService.GetDataTaxonomyCallback): void;

Calls GetDataTaxonomy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataTaxonomyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetdatataxonomyrequest)`   
GetDataTaxonomyRequest message or plain object  
`callback` |  `[GetDataTaxonomyCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and DataTaxonomy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataTaxonomy(request)
    
    
    public getDataTaxonomy(request: google.cloud.dataplex.v1.IGetDataTaxonomyRequest): Promise<google.cloud.dataplex.v1.DataTaxonomy>;

Calls GetDataTaxonomy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataTaxonomyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetdatataxonomyrequest)`   
GetDataTaxonomyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.DataTaxonomy](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.datataxonomy)>` | Promise  
  
### listDataAttributeBindings(request, callback)
    
    
    public listDataAttributeBindings(request: google.cloud.dataplex.v1.IListDataAttributeBindingsRequest, callback: google.cloud.dataplex.v1.DataTaxonomyService.ListDataAttributeBindingsCallback): void;

Calls ListDataAttributeBindings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataAttributeBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistdataattributebindingsrequest)`   
ListDataAttributeBindingsRequest message or plain object  
`callback` |  `[ListDataAttributeBindingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDataAttributeBindingsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataAttributeBindings(request)
    
    
    public listDataAttributeBindings(request: google.cloud.dataplex.v1.IListDataAttributeBindingsRequest): Promise<google.cloud.dataplex.v1.ListDataAttributeBindingsResponse>;

Calls ListDataAttributeBindings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDataAttributeBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistdataattributebindingsrequest)`   
ListDataAttributeBindingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListDataAttributeBindingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listdataattributebindingsresponse)>` | Promise  
  
### listDataAttributes(request, callback)
    
    
    public listDataAttributes(request: google.cloud.dataplex.v1.IListDataAttributesRequest, callback: google.cloud.dataplex.v1.DataTaxonomyService.ListDataAttributesCallback): void;

Calls ListDataAttributes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataAttributesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistdataattributesrequest)`   
ListDataAttributesRequest message or plain object  
`callback` |  `[ListDataAttributesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDataAttributesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataAttributes(request)
    
    
    public listDataAttributes(request: google.cloud.dataplex.v1.IListDataAttributesRequest): Promise<google.cloud.dataplex.v1.ListDataAttributesResponse>;

Calls ListDataAttributes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDataAttributesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistdataattributesrequest)`   
ListDataAttributesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListDataAttributesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listdataattributesresponse)>` | Promise  
  
### listDataTaxonomies(request, callback)
    
    
    public listDataTaxonomies(request: google.cloud.dataplex.v1.IListDataTaxonomiesRequest, callback: google.cloud.dataplex.v1.DataTaxonomyService.ListDataTaxonomiesCallback): void;

Calls ListDataTaxonomies.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataTaxonomiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistdatataxonomiesrequest)`   
ListDataTaxonomiesRequest message or plain object  
`callback` |  `[ListDataTaxonomiesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDataTaxonomiesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataTaxonomies(request)
    
    
    public listDataTaxonomies(request: google.cloud.dataplex.v1.IListDataTaxonomiesRequest): Promise<google.cloud.dataplex.v1.ListDataTaxonomiesResponse>;

Calls ListDataTaxonomies.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDataTaxonomiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistdatataxonomiesrequest)`   
ListDataTaxonomiesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListDataTaxonomiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listdatataxonomiesresponse)>` | Promise  
  
### updateDataAttribute(request, callback)
    
    
    public updateDataAttribute(request: google.cloud.dataplex.v1.IUpdateDataAttributeRequest, callback: google.cloud.dataplex.v1.DataTaxonomyService.UpdateDataAttributeCallback): void;

Calls UpdateDataAttribute.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataAttributeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdatedataattributerequest)`   
UpdateDataAttributeRequest message or plain object  
`callback` |  `[UpdateDataAttributeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataAttribute(request)
    
    
    public updateDataAttribute(request: google.cloud.dataplex.v1.IUpdateDataAttributeRequest): Promise<google.longrunning.Operation>;

Calls UpdateDataAttribute.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataAttributeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdatedataattributerequest)`   
UpdateDataAttributeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### updateDataAttributeBinding(request, callback)
    
    
    public updateDataAttributeBinding(request: google.cloud.dataplex.v1.IUpdateDataAttributeBindingRequest, callback: google.cloud.dataplex.v1.DataTaxonomyService.UpdateDataAttributeBindingCallback): void;

Calls UpdateDataAttributeBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataAttributeBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdatedataattributebindingrequest)`   
UpdateDataAttributeBindingRequest message or plain object  
`callback` |  `[UpdateDataAttributeBindingCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataAttributeBinding(request)
    
    
    public updateDataAttributeBinding(request: google.cloud.dataplex.v1.IUpdateDataAttributeBindingRequest): Promise<google.longrunning.Operation>;

Calls UpdateDataAttributeBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataAttributeBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdatedataattributebindingrequest)`   
UpdateDataAttributeBindingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### updateDataTaxonomy(request, callback)
    
    
    public updateDataTaxonomy(request: google.cloud.dataplex.v1.IUpdateDataTaxonomyRequest, callback: google.cloud.dataplex.v1.DataTaxonomyService.UpdateDataTaxonomyCallback): void;

Calls UpdateDataTaxonomy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataTaxonomyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdatedatataxonomyrequest)`   
UpdateDataTaxonomyRequest message or plain object  
`callback` |  `[UpdateDataTaxonomyCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataTaxonomy(request)
    
    
    public updateDataTaxonomy(request: google.cloud.dataplex.v1.IUpdateDataTaxonomyRequest): Promise<google.longrunning.Operation>;

Calls UpdateDataTaxonomy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataTaxonomyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdatedatataxonomyrequest)`   
UpdateDataTaxonomyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
