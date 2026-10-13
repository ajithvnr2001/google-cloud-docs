---
url: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featureonlinestoreadminservice-class
title: Class protos.google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminService (7.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:33.715483+00:00
---

# Class protos.google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminService (7.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featureonlinestoreadminservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminService (7.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.4.1 (latest)  7.3.0  6.10.0  6.9.0  6.8.1  6.6.0  6.4.0  6.3.0  6.2.0  6.1.0  6.0.0  5.14.0  5.13.0  3.15.0  3.13.0  3.11.0  3.10.1  3.9.0  3.7.0  3.6.0  3.4.0  3.3.0  3.0.0  2.12.0  2.11.0  2.10.0  2.7.0  2.6.1  2.5.0  2.3.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0  1.11.0  1.7.2 

Represents a FeatureOnlineStoreAdminService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminService

## Package

[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new FeatureOnlineStoreAdminService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): FeatureOnlineStoreAdminService;

Creates new FeatureOnlineStoreAdminService service using the specified rpc implementation.

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
`[FeatureOnlineStoreAdminService](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featureonlinestoreadminservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createFeatureOnlineStore(request, callback)
    
    
    public createFeatureOnlineStore(request: google.cloud.aiplatform.v1beta1.ICreateFeatureOnlineStoreRequest, callback: google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminService.CreateFeatureOnlineStoreCallback): void;

Calls CreateFeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeatureOnlineStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeatureonlinestorerequest)`   
CreateFeatureOnlineStoreRequest message or plain object  
`callback` |  `[CreateFeatureOnlineStoreCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFeatureOnlineStore(request)
    
    
    public createFeatureOnlineStore(request: google.cloud.aiplatform.v1beta1.ICreateFeatureOnlineStoreRequest): Promise<google.longrunning.Operation>;

Calls CreateFeatureOnlineStore.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeatureOnlineStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeatureonlinestorerequest)`   
CreateFeatureOnlineStoreRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### createFeatureView(request, callback)
    
    
    public createFeatureView(request: google.cloud.aiplatform.v1beta1.ICreateFeatureViewRequest, callback: google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminService.CreateFeatureViewCallback): void;

Calls CreateFeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeatureViewRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeatureviewrequest)`   
CreateFeatureViewRequest message or plain object  
`callback` |  `[CreateFeatureViewCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFeatureView(request)
    
    
    public createFeatureView(request: google.cloud.aiplatform.v1beta1.ICreateFeatureViewRequest): Promise<google.longrunning.Operation>;

Calls CreateFeatureView.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeatureViewRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeatureviewrequest)`   
CreateFeatureViewRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### deleteFeatureOnlineStore(request, callback)
    
    
    public deleteFeatureOnlineStore(request: google.cloud.aiplatform.v1beta1.IDeleteFeatureOnlineStoreRequest, callback: google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminService.DeleteFeatureOnlineStoreCallback): void;

Calls DeleteFeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeatureOnlineStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletefeatureonlinestorerequest)`   
DeleteFeatureOnlineStoreRequest message or plain object  
`callback` |  `[DeleteFeatureOnlineStoreCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFeatureOnlineStore(request)
    
    
    public deleteFeatureOnlineStore(request: google.cloud.aiplatform.v1beta1.IDeleteFeatureOnlineStoreRequest): Promise<google.longrunning.Operation>;

Calls DeleteFeatureOnlineStore.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeatureOnlineStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletefeatureonlinestorerequest)`   
DeleteFeatureOnlineStoreRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### deleteFeatureView(request, callback)
    
    
    public deleteFeatureView(request: google.cloud.aiplatform.v1beta1.IDeleteFeatureViewRequest, callback: google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminService.DeleteFeatureViewCallback): void;

Calls DeleteFeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeatureViewRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletefeatureviewrequest)`   
DeleteFeatureViewRequest message or plain object  
`callback` |  `[DeleteFeatureViewCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFeatureView(request)
    
    
    public deleteFeatureView(request: google.cloud.aiplatform.v1beta1.IDeleteFeatureViewRequest): Promise<google.longrunning.Operation>;

Calls DeleteFeatureView.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeatureViewRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletefeatureviewrequest)`   
DeleteFeatureViewRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### getFeatureOnlineStore(request, callback)
    
    
    public getFeatureOnlineStore(request: google.cloud.aiplatform.v1beta1.IGetFeatureOnlineStoreRequest, callback: google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminService.GetFeatureOnlineStoreCallback): void;

Calls GetFeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureOnlineStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeatureonlinestorerequest)`   
GetFeatureOnlineStoreRequest message or plain object  
`callback` |  `[GetFeatureOnlineStoreCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and FeatureOnlineStore  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFeatureOnlineStore(request)
    
    
    public getFeatureOnlineStore(request: google.cloud.aiplatform.v1beta1.IGetFeatureOnlineStoreRequest): Promise<google.cloud.aiplatform.v1beta1.FeatureOnlineStore>;

Calls GetFeatureOnlineStore.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureOnlineStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeatureonlinestorerequest)`   
GetFeatureOnlineStoreRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.FeatureOnlineStore](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featureonlinestore-class)>` | Promise  
  
### getFeatureView(request, callback)
    
    
    public getFeatureView(request: google.cloud.aiplatform.v1beta1.IGetFeatureViewRequest, callback: google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminService.GetFeatureViewCallback): void;

Calls GetFeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureViewRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeatureviewrequest)`   
GetFeatureViewRequest message or plain object  
`callback` |  `[GetFeatureViewCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and FeatureView  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFeatureView(request)
    
    
    public getFeatureView(request: google.cloud.aiplatform.v1beta1.IGetFeatureViewRequest): Promise<google.cloud.aiplatform.v1beta1.FeatureView>;

Calls GetFeatureView.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureViewRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeatureviewrequest)`   
GetFeatureViewRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.FeatureView](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featureview-class)>` | Promise  
  
### getFeatureViewSync(request, callback)
    
    
    public getFeatureViewSync(request: google.cloud.aiplatform.v1beta1.IGetFeatureViewSyncRequest, callback: google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminService.GetFeatureViewSyncCallback): void;

Calls GetFeatureViewSync.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureViewSyncRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeatureviewsyncrequest)`   
GetFeatureViewSyncRequest message or plain object  
`callback` |  `[GetFeatureViewSyncCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and FeatureViewSync  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFeatureViewSync(request)
    
    
    public getFeatureViewSync(request: google.cloud.aiplatform.v1beta1.IGetFeatureViewSyncRequest): Promise<google.cloud.aiplatform.v1beta1.FeatureViewSync>;

Calls GetFeatureViewSync.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureViewSyncRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeatureviewsyncrequest)`   
GetFeatureViewSyncRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.FeatureViewSync](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featureviewsync-class)>` | Promise  
  
### listFeatureOnlineStores(request, callback)
    
    
    public listFeatureOnlineStores(request: google.cloud.aiplatform.v1beta1.IListFeatureOnlineStoresRequest, callback: google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminService.ListFeatureOnlineStoresCallback): void;

Calls ListFeatureOnlineStores.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeatureOnlineStoresRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeatureonlinestoresrequest)`   
ListFeatureOnlineStoresRequest message or plain object  
`callback` |  `[ListFeatureOnlineStoresCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListFeatureOnlineStoresResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFeatureOnlineStores(request)
    
    
    public listFeatureOnlineStores(request: google.cloud.aiplatform.v1beta1.IListFeatureOnlineStoresRequest): Promise<google.cloud.aiplatform.v1beta1.ListFeatureOnlineStoresResponse>;

Calls ListFeatureOnlineStores.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListFeatureOnlineStoresRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeatureonlinestoresrequest)`   
ListFeatureOnlineStoresRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.ListFeatureOnlineStoresResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.listfeatureonlinestoresresponse)>` | Promise  
  
### listFeatureViews(request, callback)
    
    
    public listFeatureViews(request: google.cloud.aiplatform.v1beta1.IListFeatureViewsRequest, callback: google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminService.ListFeatureViewsCallback): void;

Calls ListFeatureViews.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeatureViewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeatureviewsrequest)`   
ListFeatureViewsRequest message or plain object  
`callback` |  `[ListFeatureViewsCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListFeatureViewsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFeatureViews(request)
    
    
    public listFeatureViews(request: google.cloud.aiplatform.v1beta1.IListFeatureViewsRequest): Promise<google.cloud.aiplatform.v1beta1.ListFeatureViewsResponse>;

Calls ListFeatureViews.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListFeatureViewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeatureviewsrequest)`   
ListFeatureViewsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.ListFeatureViewsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.listfeatureviewsresponse)>` | Promise  
  
### listFeatureViewSyncs(request, callback)
    
    
    public listFeatureViewSyncs(request: google.cloud.aiplatform.v1beta1.IListFeatureViewSyncsRequest, callback: google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminService.ListFeatureViewSyncsCallback): void;

Calls ListFeatureViewSyncs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeatureViewSyncsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeatureviewsyncsrequest)`   
ListFeatureViewSyncsRequest message or plain object  
`callback` |  `[ListFeatureViewSyncsCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListFeatureViewSyncsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFeatureViewSyncs(request)
    
    
    public listFeatureViewSyncs(request: google.cloud.aiplatform.v1beta1.IListFeatureViewSyncsRequest): Promise<google.cloud.aiplatform.v1beta1.ListFeatureViewSyncsResponse>;

Calls ListFeatureViewSyncs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListFeatureViewSyncsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeatureviewsyncsrequest)`   
ListFeatureViewSyncsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.ListFeatureViewSyncsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.listfeatureviewsyncsresponse)>` | Promise  
  
### syncFeatureView(request, callback)
    
    
    public syncFeatureView(request: google.cloud.aiplatform.v1beta1.ISyncFeatureViewRequest, callback: google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminService.SyncFeatureViewCallback): void;

Calls SyncFeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISyncFeatureViewRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isyncfeatureviewrequest)`   
SyncFeatureViewRequest message or plain object  
`callback` |  `[SyncFeatureViewCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and SyncFeatureViewResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### syncFeatureView(request)
    
    
    public syncFeatureView(request: google.cloud.aiplatform.v1beta1.ISyncFeatureViewRequest): Promise<google.cloud.aiplatform.v1beta1.SyncFeatureViewResponse>;

Calls SyncFeatureView.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISyncFeatureViewRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isyncfeatureviewrequest)`   
SyncFeatureViewRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.SyncFeatureViewResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.syncfeatureviewresponse)>` | Promise  
  
### updateFeatureOnlineStore(request, callback)
    
    
    public updateFeatureOnlineStore(request: google.cloud.aiplatform.v1beta1.IUpdateFeatureOnlineStoreRequest, callback: google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminService.UpdateFeatureOnlineStoreCallback): void;

Calls UpdateFeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeatureOnlineStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeatureonlinestorerequest)`   
UpdateFeatureOnlineStoreRequest message or plain object  
`callback` |  `[UpdateFeatureOnlineStoreCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFeatureOnlineStore(request)
    
    
    public updateFeatureOnlineStore(request: google.cloud.aiplatform.v1beta1.IUpdateFeatureOnlineStoreRequest): Promise<google.longrunning.Operation>;

Calls UpdateFeatureOnlineStore.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeatureOnlineStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeatureonlinestorerequest)`   
UpdateFeatureOnlineStoreRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### updateFeatureView(request, callback)
    
    
    public updateFeatureView(request: google.cloud.aiplatform.v1beta1.IUpdateFeatureViewRequest, callback: google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminService.UpdateFeatureViewCallback): void;

Calls UpdateFeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeatureViewRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeatureviewrequest)`   
UpdateFeatureViewRequest message or plain object  
`callback` |  `[UpdateFeatureViewCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFeatureView(request)
    
    
    public updateFeatureView(request: google.cloud.aiplatform.v1beta1.IUpdateFeatureViewRequest): Promise<google.longrunning.Operation>;

Calls UpdateFeatureView.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeatureViewRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeatureviewrequest)`   
UpdateFeatureViewRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
