---
url: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featurestoreservice-class
title: Class protos.google.cloud.aiplatform.v1beta1.FeaturestoreService (7.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:44:50.684599+00:00
---

# Class protos.google.cloud.aiplatform.v1beta1.FeaturestoreService (7.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featurestoreservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.aiplatform.v1beta1.FeaturestoreService (7.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.4.1 (latest)  7.3.0  6.10.0  6.9.0  6.8.1  6.6.0  6.4.0  6.3.0  6.2.0  6.1.0  6.0.0  5.14.0  5.13.0  3.15.0  3.13.0  3.11.0  3.10.1  3.9.0  3.7.0  3.6.0  3.4.0  3.3.0  3.0.0  2.12.0  2.11.0  2.10.0  2.7.0  2.6.1  2.5.0  2.3.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0  1.11.0  1.7.2 

Represents a FeaturestoreService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.aiplatform.v1beta1.FeaturestoreService

## Package

[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new FeaturestoreService service.

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

### batchCreateFeatures(request, callback)
    
    
    public batchCreateFeatures(request: google.cloud.aiplatform.v1beta1.IBatchCreateFeaturesRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreService.BatchCreateFeaturesCallback): void;

Calls BatchCreateFeatures.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatefeaturesrequest)`   
BatchCreateFeaturesRequest message or plain object  
`callback` |  `[BatchCreateFeaturesCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateFeatures(request)
    
    
    public batchCreateFeatures(request: google.cloud.aiplatform.v1beta1.IBatchCreateFeaturesRequest): Promise<google.longrunning.Operation>;

Calls BatchCreateFeatures.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatefeaturesrequest)`   
BatchCreateFeaturesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### batchReadFeatureValues(request, callback)
    
    
    public batchReadFeatureValues(request: google.cloud.aiplatform.v1beta1.IBatchReadFeatureValuesRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreService.BatchReadFeatureValuesCallback): void;

Calls BatchReadFeatureValues.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchReadFeatureValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchreadfeaturevaluesrequest)`   
BatchReadFeatureValuesRequest message or plain object  
`callback` |  `[BatchReadFeatureValuesCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchReadFeatureValues(request)
    
    
    public batchReadFeatureValues(request: google.cloud.aiplatform.v1beta1.IBatchReadFeatureValuesRequest): Promise<google.longrunning.Operation>;

Calls BatchReadFeatureValues.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchReadFeatureValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchreadfeaturevaluesrequest)`   
BatchReadFeatureValuesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): FeaturestoreService;

Creates new FeaturestoreService service using the specified rpc implementation.

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
`[FeaturestoreService](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featurestoreservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createEntityType(request, callback)
    
    
    public createEntityType(request: google.cloud.aiplatform.v1beta1.ICreateEntityTypeRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreService.CreateEntityTypeCallback): void;

Calls CreateEntityType.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEntityTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreateentitytyperequest)`   
CreateEntityTypeRequest message or plain object  
`callback` |  `[CreateEntityTypeCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEntityType(request)
    
    
    public createEntityType(request: google.cloud.aiplatform.v1beta1.ICreateEntityTypeRequest): Promise<google.longrunning.Operation>;

Calls CreateEntityType.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateEntityTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreateentitytyperequest)`   
CreateEntityTypeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### createFeature(request, callback)
    
    
    public createFeature(request: google.cloud.aiplatform.v1beta1.ICreateFeatureRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreService.CreateFeatureCallback): void;

Calls CreateFeature.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturerequest)`   
CreateFeatureRequest message or plain object  
`callback` |  `[CreateFeatureCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFeature(request)
    
    
    public createFeature(request: google.cloud.aiplatform.v1beta1.ICreateFeatureRequest): Promise<google.longrunning.Operation>;

Calls CreateFeature.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturerequest)`   
CreateFeatureRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### createFeaturestore(request, callback)
    
    
    public createFeaturestore(request: google.cloud.aiplatform.v1beta1.ICreateFeaturestoreRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreService.CreateFeaturestoreCallback): void;

Calls CreateFeaturestore.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeaturestoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturestorerequest)`   
CreateFeaturestoreRequest message or plain object  
`callback` |  `[CreateFeaturestoreCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFeaturestore(request)
    
    
    public createFeaturestore(request: google.cloud.aiplatform.v1beta1.ICreateFeaturestoreRequest): Promise<google.longrunning.Operation>;

Calls CreateFeaturestore.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeaturestoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturestorerequest)`   
CreateFeaturestoreRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### deleteEntityType(request, callback)
    
    
    public deleteEntityType(request: google.cloud.aiplatform.v1beta1.IDeleteEntityTypeRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreService.DeleteEntityTypeCallback): void;

Calls DeleteEntityType.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEntityTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteentitytyperequest)`   
DeleteEntityTypeRequest message or plain object  
`callback` |  `[DeleteEntityTypeCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEntityType(request)
    
    
    public deleteEntityType(request: google.cloud.aiplatform.v1beta1.IDeleteEntityTypeRequest): Promise<google.longrunning.Operation>;

Calls DeleteEntityType.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEntityTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteentitytyperequest)`   
DeleteEntityTypeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### deleteFeature(request, callback)
    
    
    public deleteFeature(request: google.cloud.aiplatform.v1beta1.IDeleteFeatureRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreService.DeleteFeatureCallback): void;

Calls DeleteFeature.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletefeaturerequest)`   
DeleteFeatureRequest message or plain object  
`callback` |  `[DeleteFeatureCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFeature(request)
    
    
    public deleteFeature(request: google.cloud.aiplatform.v1beta1.IDeleteFeatureRequest): Promise<google.longrunning.Operation>;

Calls DeleteFeature.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletefeaturerequest)`   
DeleteFeatureRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### deleteFeaturestore(request, callback)
    
    
    public deleteFeaturestore(request: google.cloud.aiplatform.v1beta1.IDeleteFeaturestoreRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreService.DeleteFeaturestoreCallback): void;

Calls DeleteFeaturestore.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeaturestoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletefeaturestorerequest)`   
DeleteFeaturestoreRequest message or plain object  
`callback` |  `[DeleteFeaturestoreCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFeaturestore(request)
    
    
    public deleteFeaturestore(request: google.cloud.aiplatform.v1beta1.IDeleteFeaturestoreRequest): Promise<google.longrunning.Operation>;

Calls DeleteFeaturestore.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeaturestoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletefeaturestorerequest)`   
DeleteFeaturestoreRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### deleteFeatureValues(request, callback)
    
    
    public deleteFeatureValues(request: google.cloud.aiplatform.v1beta1.IDeleteFeatureValuesRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreService.DeleteFeatureValuesCallback): void;

Calls DeleteFeatureValues.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeatureValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletefeaturevaluesrequest)`   
DeleteFeatureValuesRequest message or plain object  
`callback` |  `[DeleteFeatureValuesCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFeatureValues(request)
    
    
    public deleteFeatureValues(request: google.cloud.aiplatform.v1beta1.IDeleteFeatureValuesRequest): Promise<google.longrunning.Operation>;

Calls DeleteFeatureValues.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeatureValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletefeaturevaluesrequest)`   
DeleteFeatureValuesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### exportFeatureValues(request, callback)
    
    
    public exportFeatureValues(request: google.cloud.aiplatform.v1beta1.IExportFeatureValuesRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreService.ExportFeatureValuesCallback): void;

Calls ExportFeatureValues.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportFeatureValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexportfeaturevaluesrequest)`   
ExportFeatureValuesRequest message or plain object  
`callback` |  `[ExportFeatureValuesCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportFeatureValues(request)
    
    
    public exportFeatureValues(request: google.cloud.aiplatform.v1beta1.IExportFeatureValuesRequest): Promise<google.longrunning.Operation>;

Calls ExportFeatureValues.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportFeatureValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexportfeaturevaluesrequest)`   
ExportFeatureValuesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### getEntityType(request, callback)
    
    
    public getEntityType(request: google.cloud.aiplatform.v1beta1.IGetEntityTypeRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreService.GetEntityTypeCallback): void;

Calls GetEntityType.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEntityTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetentitytyperequest)`   
GetEntityTypeRequest message or plain object  
`callback` |  `[GetEntityTypeCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and EntityType  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEntityType(request)
    
    
    public getEntityType(request: google.cloud.aiplatform.v1beta1.IGetEntityTypeRequest): Promise<google.cloud.aiplatform.v1beta1.EntityType>;

Calls GetEntityType.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEntityTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetentitytyperequest)`   
GetEntityTypeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.EntityType](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.entitytype)>` | Promise  
  
### getFeature(request, callback)
    
    
    public getFeature(request: google.cloud.aiplatform.v1beta1.IGetFeatureRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreService.GetFeatureCallback): void;

Calls GetFeature.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturerequest)`   
GetFeatureRequest message or plain object  
`callback` |  `[GetFeatureCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Feature  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFeature(request)
    
    
    public getFeature(request: google.cloud.aiplatform.v1beta1.IGetFeatureRequest): Promise<google.cloud.aiplatform.v1beta1.Feature>;

Calls GetFeature.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturerequest)`   
GetFeatureRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.Feature](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.feature-class)>` | Promise  
  
### getFeaturestore(request, callback)
    
    
    public getFeaturestore(request: google.cloud.aiplatform.v1beta1.IGetFeaturestoreRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreService.GetFeaturestoreCallback): void;

Calls GetFeaturestore.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeaturestoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturestorerequest)`   
GetFeaturestoreRequest message or plain object  
`callback` |  `[GetFeaturestoreCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Featurestore  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFeaturestore(request)
    
    
    public getFeaturestore(request: google.cloud.aiplatform.v1beta1.IGetFeaturestoreRequest): Promise<google.cloud.aiplatform.v1beta1.Featurestore>;

Calls GetFeaturestore.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetFeaturestoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturestorerequest)`   
GetFeaturestoreRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.Featurestore](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featurestore-class)>` | Promise  
  
### importFeatureValues(request, callback)
    
    
    public importFeatureValues(request: google.cloud.aiplatform.v1beta1.IImportFeatureValuesRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreService.ImportFeatureValuesCallback): void;

Calls ImportFeatureValues.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportFeatureValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iimportfeaturevaluesrequest)`   
ImportFeatureValuesRequest message or plain object  
`callback` |  `[ImportFeatureValuesCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importFeatureValues(request)
    
    
    public importFeatureValues(request: google.cloud.aiplatform.v1beta1.IImportFeatureValuesRequest): Promise<google.longrunning.Operation>;

Calls ImportFeatureValues.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportFeatureValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iimportfeaturevaluesrequest)`   
ImportFeatureValuesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### listEntityTypes(request, callback)
    
    
    public listEntityTypes(request: google.cloud.aiplatform.v1beta1.IListEntityTypesRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreService.ListEntityTypesCallback): void;

Calls ListEntityTypes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEntityTypesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistentitytypesrequest)`   
ListEntityTypesRequest message or plain object  
`callback` |  `[ListEntityTypesCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListEntityTypesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEntityTypes(request)
    
    
    public listEntityTypes(request: google.cloud.aiplatform.v1beta1.IListEntityTypesRequest): Promise<google.cloud.aiplatform.v1beta1.ListEntityTypesResponse>;

Calls ListEntityTypes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListEntityTypesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistentitytypesrequest)`   
ListEntityTypesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.ListEntityTypesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.listentitytypesresponse)>` | Promise  
  
### listFeatures(request, callback)
    
    
    public listFeatures(request: google.cloud.aiplatform.v1beta1.IListFeaturesRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreService.ListFeaturesCallback): void;

Calls ListFeatures.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturesrequest)`   
ListFeaturesRequest message or plain object  
`callback` |  `[ListFeaturesCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListFeaturesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFeatures(request)
    
    
    public listFeatures(request: google.cloud.aiplatform.v1beta1.IListFeaturesRequest): Promise<google.cloud.aiplatform.v1beta1.ListFeaturesResponse>;

Calls ListFeatures.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturesrequest)`   
ListFeaturesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.ListFeaturesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.listfeaturesresponse)>` | Promise  
  
### listFeaturestores(request, callback)
    
    
    public listFeaturestores(request: google.cloud.aiplatform.v1beta1.IListFeaturestoresRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreService.ListFeaturestoresCallback): void;

Calls ListFeaturestores.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeaturestoresRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturestoresrequest)`   
ListFeaturestoresRequest message or plain object  
`callback` |  `[ListFeaturestoresCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListFeaturestoresResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFeaturestores(request)
    
    
    public listFeaturestores(request: google.cloud.aiplatform.v1beta1.IListFeaturestoresRequest): Promise<google.cloud.aiplatform.v1beta1.ListFeaturestoresResponse>;

Calls ListFeaturestores.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListFeaturestoresRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturestoresrequest)`   
ListFeaturestoresRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.ListFeaturestoresResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.listfeaturestoresresponse)>` | Promise  
  
### searchFeatures(request, callback)
    
    
    public searchFeatures(request: google.cloud.aiplatform.v1beta1.ISearchFeaturesRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreService.SearchFeaturesCallback): void;

Calls SearchFeatures.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isearchfeaturesrequest)`   
SearchFeaturesRequest message or plain object  
`callback` |  `[SearchFeaturesCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchFeaturesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchFeatures(request)
    
    
    public searchFeatures(request: google.cloud.aiplatform.v1beta1.ISearchFeaturesRequest): Promise<google.cloud.aiplatform.v1beta1.SearchFeaturesResponse>;

Calls SearchFeatures.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isearchfeaturesrequest)`   
SearchFeaturesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.SearchFeaturesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.searchfeaturesresponse)>` | Promise  
  
### updateEntityType(request, callback)
    
    
    public updateEntityType(request: google.cloud.aiplatform.v1beta1.IUpdateEntityTypeRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreService.UpdateEntityTypeCallback): void;

Calls UpdateEntityType.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEntityTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdateentitytyperequest)`   
UpdateEntityTypeRequest message or plain object  
`callback` |  `[UpdateEntityTypeCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and EntityType  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEntityType(request)
    
    
    public updateEntityType(request: google.cloud.aiplatform.v1beta1.IUpdateEntityTypeRequest): Promise<google.cloud.aiplatform.v1beta1.EntityType>;

Calls UpdateEntityType.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEntityTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdateentitytyperequest)`   
UpdateEntityTypeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.EntityType](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.entitytype)>` | Promise  
  
### updateFeature(request, callback)
    
    
    public updateFeature(request: google.cloud.aiplatform.v1beta1.IUpdateFeatureRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreService.UpdateFeatureCallback): void;

Calls UpdateFeature.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeaturerequest)`   
UpdateFeatureRequest message or plain object  
`callback` |  `[UpdateFeatureCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Feature  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFeature(request)
    
    
    public updateFeature(request: google.cloud.aiplatform.v1beta1.IUpdateFeatureRequest): Promise<google.cloud.aiplatform.v1beta1.Feature>;

Calls UpdateFeature.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeaturerequest)`   
UpdateFeatureRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.Feature](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.feature-class)>` | Promise  
  
### updateFeaturestore(request, callback)
    
    
    public updateFeaturestore(request: google.cloud.aiplatform.v1beta1.IUpdateFeaturestoreRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreService.UpdateFeaturestoreCallback): void;

Calls UpdateFeaturestore.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeaturestoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeaturestorerequest)`   
UpdateFeaturestoreRequest message or plain object  
`callback` |  `[UpdateFeaturestoreCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFeaturestore(request)
    
    
    public updateFeaturestore(request: google.cloud.aiplatform.v1beta1.IUpdateFeaturestoreRequest): Promise<google.longrunning.Operation>;

Calls UpdateFeaturestore.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeaturestoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeaturestorerequest)`   
UpdateFeaturestoreRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
