---
url: https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.aml-class
title: Class protos.google.cloud.financialservices.v1.AML (0.6.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:03:19.798482+00:00
---

# Class protos.google.cloud.financialservices.v1.AML (0.6.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.aml-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.financialservices.v1.AML (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.3.0  0.2.0 

Represents a AML

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.financialservices.v1.AML

## Package

[@google-cloud/financialservices](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AML service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AML;

Creates new AML service using the specified rpc implementation.

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
`[AML](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.aml-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createBacktestResult(request, callback)
    
    
    public createBacktestResult(request: google.cloud.financialservices.v1.ICreateBacktestResultRequest, callback: google.cloud.financialservices.v1.AML.CreateBacktestResultCallback): void;

Calls CreateBacktestResult.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateBacktestResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.icreatebacktestresultrequest)`   
CreateBacktestResultRequest message or plain object  
`callback` |  `[CreateBacktestResultCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createBacktestResult(request)
    
    
    public createBacktestResult(request: google.cloud.financialservices.v1.ICreateBacktestResultRequest): Promise<google.longrunning.Operation>;

Calls CreateBacktestResult.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateBacktestResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.icreatebacktestresultrequest)`   
CreateBacktestResultRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### createDataset(request, callback)
    
    
    public createDataset(request: google.cloud.financialservices.v1.ICreateDatasetRequest, callback: google.cloud.financialservices.v1.AML.CreateDatasetCallback): void;

Calls CreateDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.icreatedatasetrequest)`   
CreateDatasetRequest message or plain object  
`callback` |  `[CreateDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataset(request)
    
    
    public createDataset(request: google.cloud.financialservices.v1.ICreateDatasetRequest): Promise<google.longrunning.Operation>;

Calls CreateDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.icreatedatasetrequest)`   
CreateDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### createEngineConfig(request, callback)
    
    
    public createEngineConfig(request: google.cloud.financialservices.v1.ICreateEngineConfigRequest, callback: google.cloud.financialservices.v1.AML.CreateEngineConfigCallback): void;

Calls CreateEngineConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEngineConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.icreateengineconfigrequest)`   
CreateEngineConfigRequest message or plain object  
`callback` |  `[CreateEngineConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEngineConfig(request)
    
    
    public createEngineConfig(request: google.cloud.financialservices.v1.ICreateEngineConfigRequest): Promise<google.longrunning.Operation>;

Calls CreateEngineConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateEngineConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.icreateengineconfigrequest)`   
CreateEngineConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### createInstance(request, callback)
    
    
    public createInstance(request: google.cloud.financialservices.v1.ICreateInstanceRequest, callback: google.cloud.financialservices.v1.AML.CreateInstanceCallback): void;

Calls CreateInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.icreateinstancerequest)`   
CreateInstanceRequest message or plain object  
`callback` |  `[CreateInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createInstance(request)
    
    
    public createInstance(request: google.cloud.financialservices.v1.ICreateInstanceRequest): Promise<google.longrunning.Operation>;

Calls CreateInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.icreateinstancerequest)`   
CreateInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### createModel(request, callback)
    
    
    public createModel(request: google.cloud.financialservices.v1.ICreateModelRequest, callback: google.cloud.financialservices.v1.AML.CreateModelCallback): void;

Calls CreateModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.icreatemodelrequest)`   
CreateModelRequest message or plain object  
`callback` |  `[CreateModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createModel(request)
    
    
    public createModel(request: google.cloud.financialservices.v1.ICreateModelRequest): Promise<google.longrunning.Operation>;

Calls CreateModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.icreatemodelrequest)`   
CreateModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### createPredictionResult(request, callback)
    
    
    public createPredictionResult(request: google.cloud.financialservices.v1.ICreatePredictionResultRequest, callback: google.cloud.financialservices.v1.AML.CreatePredictionResultCallback): void;

Calls CreatePredictionResult.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePredictionResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.icreatepredictionresultrequest)`   
CreatePredictionResultRequest message or plain object  
`callback` |  `[CreatePredictionResultCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createPredictionResult(request)
    
    
    public createPredictionResult(request: google.cloud.financialservices.v1.ICreatePredictionResultRequest): Promise<google.longrunning.Operation>;

Calls CreatePredictionResult.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreatePredictionResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.icreatepredictionresultrequest)`   
CreatePredictionResultRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### deleteBacktestResult(request, callback)
    
    
    public deleteBacktestResult(request: google.cloud.financialservices.v1.IDeleteBacktestResultRequest, callback: google.cloud.financialservices.v1.AML.DeleteBacktestResultCallback): void;

Calls DeleteBacktestResult.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBacktestResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ideletebacktestresultrequest)`   
DeleteBacktestResultRequest message or plain object  
`callback` |  `[DeleteBacktestResultCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteBacktestResult(request)
    
    
    public deleteBacktestResult(request: google.cloud.financialservices.v1.IDeleteBacktestResultRequest): Promise<google.longrunning.Operation>;

Calls DeleteBacktestResult.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBacktestResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ideletebacktestresultrequest)`   
DeleteBacktestResultRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### deleteDataset(request, callback)
    
    
    public deleteDataset(request: google.cloud.financialservices.v1.IDeleteDatasetRequest, callback: google.cloud.financialservices.v1.AML.DeleteDatasetCallback): void;

Calls DeleteDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ideletedatasetrequest)`   
DeleteDatasetRequest message or plain object  
`callback` |  `[DeleteDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataset(request)
    
    
    public deleteDataset(request: google.cloud.financialservices.v1.IDeleteDatasetRequest): Promise<google.longrunning.Operation>;

Calls DeleteDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ideletedatasetrequest)`   
DeleteDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### deleteEngineConfig(request, callback)
    
    
    public deleteEngineConfig(request: google.cloud.financialservices.v1.IDeleteEngineConfigRequest, callback: google.cloud.financialservices.v1.AML.DeleteEngineConfigCallback): void;

Calls DeleteEngineConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEngineConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ideleteengineconfigrequest)`   
DeleteEngineConfigRequest message or plain object  
`callback` |  `[DeleteEngineConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEngineConfig(request)
    
    
    public deleteEngineConfig(request: google.cloud.financialservices.v1.IDeleteEngineConfigRequest): Promise<google.longrunning.Operation>;

Calls DeleteEngineConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEngineConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ideleteengineconfigrequest)`   
DeleteEngineConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### deleteInstance(request, callback)
    
    
    public deleteInstance(request: google.cloud.financialservices.v1.IDeleteInstanceRequest, callback: google.cloud.financialservices.v1.AML.DeleteInstanceCallback): void;

Calls DeleteInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ideleteinstancerequest)`   
DeleteInstanceRequest message or plain object  
`callback` |  `[DeleteInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteInstance(request)
    
    
    public deleteInstance(request: google.cloud.financialservices.v1.IDeleteInstanceRequest): Promise<google.longrunning.Operation>;

Calls DeleteInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ideleteinstancerequest)`   
DeleteInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### deleteModel(request, callback)
    
    
    public deleteModel(request: google.cloud.financialservices.v1.IDeleteModelRequest, callback: google.cloud.financialservices.v1.AML.DeleteModelCallback): void;

Calls DeleteModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ideletemodelrequest)`   
DeleteModelRequest message or plain object  
`callback` |  `[DeleteModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteModel(request)
    
    
    public deleteModel(request: google.cloud.financialservices.v1.IDeleteModelRequest): Promise<google.longrunning.Operation>;

Calls DeleteModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ideletemodelrequest)`   
DeleteModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### deletePredictionResult(request, callback)
    
    
    public deletePredictionResult(request: google.cloud.financialservices.v1.IDeletePredictionResultRequest, callback: google.cloud.financialservices.v1.AML.DeletePredictionResultCallback): void;

Calls DeletePredictionResult.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePredictionResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ideletepredictionresultrequest)`   
DeletePredictionResultRequest message or plain object  
`callback` |  `[DeletePredictionResultCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePredictionResult(request)
    
    
    public deletePredictionResult(request: google.cloud.financialservices.v1.IDeletePredictionResultRequest): Promise<google.longrunning.Operation>;

Calls DeletePredictionResult.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeletePredictionResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ideletepredictionresultrequest)`   
DeletePredictionResultRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### exportBacktestResultMetadata(request, callback)
    
    
    public exportBacktestResultMetadata(request: google.cloud.financialservices.v1.IExportBacktestResultMetadataRequest, callback: google.cloud.financialservices.v1.AML.ExportBacktestResultMetadataCallback): void;

Calls ExportBacktestResultMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportBacktestResultMetadataRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iexportbacktestresultmetadatarequest)`   
ExportBacktestResultMetadataRequest message or plain object  
`callback` |  `[ExportBacktestResultMetadataCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportBacktestResultMetadata(request)
    
    
    public exportBacktestResultMetadata(request: google.cloud.financialservices.v1.IExportBacktestResultMetadataRequest): Promise<google.longrunning.Operation>;

Calls ExportBacktestResultMetadata.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportBacktestResultMetadataRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iexportbacktestresultmetadatarequest)`   
ExportBacktestResultMetadataRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### exportEngineConfigMetadata(request, callback)
    
    
    public exportEngineConfigMetadata(request: google.cloud.financialservices.v1.IExportEngineConfigMetadataRequest, callback: google.cloud.financialservices.v1.AML.ExportEngineConfigMetadataCallback): void;

Calls ExportEngineConfigMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportEngineConfigMetadataRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iexportengineconfigmetadatarequest)`   
ExportEngineConfigMetadataRequest message or plain object  
`callback` |  `[ExportEngineConfigMetadataCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportEngineConfigMetadata(request)
    
    
    public exportEngineConfigMetadata(request: google.cloud.financialservices.v1.IExportEngineConfigMetadataRequest): Promise<google.longrunning.Operation>;

Calls ExportEngineConfigMetadata.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportEngineConfigMetadataRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iexportengineconfigmetadatarequest)`   
ExportEngineConfigMetadataRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### exportModelMetadata(request, callback)
    
    
    public exportModelMetadata(request: google.cloud.financialservices.v1.IExportModelMetadataRequest, callback: google.cloud.financialservices.v1.AML.ExportModelMetadataCallback): void;

Calls ExportModelMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportModelMetadataRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iexportmodelmetadatarequest)`   
ExportModelMetadataRequest message or plain object  
`callback` |  `[ExportModelMetadataCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportModelMetadata(request)
    
    
    public exportModelMetadata(request: google.cloud.financialservices.v1.IExportModelMetadataRequest): Promise<google.longrunning.Operation>;

Calls ExportModelMetadata.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportModelMetadataRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iexportmodelmetadatarequest)`   
ExportModelMetadataRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### exportPredictionResultMetadata(request, callback)
    
    
    public exportPredictionResultMetadata(request: google.cloud.financialservices.v1.IExportPredictionResultMetadataRequest, callback: google.cloud.financialservices.v1.AML.ExportPredictionResultMetadataCallback): void;

Calls ExportPredictionResultMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportPredictionResultMetadataRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iexportpredictionresultmetadatarequest)`   
ExportPredictionResultMetadataRequest message or plain object  
`callback` |  `[ExportPredictionResultMetadataCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportPredictionResultMetadata(request)
    
    
    public exportPredictionResultMetadata(request: google.cloud.financialservices.v1.IExportPredictionResultMetadataRequest): Promise<google.longrunning.Operation>;

Calls ExportPredictionResultMetadata.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportPredictionResultMetadataRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iexportpredictionresultmetadatarequest)`   
ExportPredictionResultMetadataRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### exportRegisteredParties(request, callback)
    
    
    public exportRegisteredParties(request: google.cloud.financialservices.v1.IExportRegisteredPartiesRequest, callback: google.cloud.financialservices.v1.AML.ExportRegisteredPartiesCallback): void;

Calls ExportRegisteredParties.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportRegisteredPartiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iexportregisteredpartiesrequest)`   
ExportRegisteredPartiesRequest message or plain object  
`callback` |  `[ExportRegisteredPartiesCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportRegisteredParties(request)
    
    
    public exportRegisteredParties(request: google.cloud.financialservices.v1.IExportRegisteredPartiesRequest): Promise<google.longrunning.Operation>;

Calls ExportRegisteredParties.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportRegisteredPartiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iexportregisteredpartiesrequest)`   
ExportRegisteredPartiesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### getBacktestResult(request, callback)
    
    
    public getBacktestResult(request: google.cloud.financialservices.v1.IGetBacktestResultRequest, callback: google.cloud.financialservices.v1.AML.GetBacktestResultCallback): void;

Calls GetBacktestResult.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBacktestResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.igetbacktestresultrequest)`   
GetBacktestResultRequest message or plain object  
`callback` |  `[GetBacktestResultCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and BacktestResult  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBacktestResult(request)
    
    
    public getBacktestResult(request: google.cloud.financialservices.v1.IGetBacktestResultRequest): Promise<google.cloud.financialservices.v1.BacktestResult>;

Calls GetBacktestResult.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetBacktestResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.igetbacktestresultrequest)`   
GetBacktestResultRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.financialservices.v1.BacktestResult](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.backtestresult-class)>` | Promise  
  
### getDataset(request, callback)
    
    
    public getDataset(request: google.cloud.financialservices.v1.IGetDatasetRequest, callback: google.cloud.financialservices.v1.AML.GetDatasetCallback): void;

Calls GetDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.igetdatasetrequest)`   
GetDatasetRequest message or plain object  
`callback` |  `[GetDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Dataset  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataset(request)
    
    
    public getDataset(request: google.cloud.financialservices.v1.IGetDatasetRequest): Promise<google.cloud.financialservices.v1.Dataset>;

Calls GetDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.igetdatasetrequest)`   
GetDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.financialservices.v1.Dataset](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.dataset-class)>` | Promise  
  
### getEngineConfig(request, callback)
    
    
    public getEngineConfig(request: google.cloud.financialservices.v1.IGetEngineConfigRequest, callback: google.cloud.financialservices.v1.AML.GetEngineConfigCallback): void;

Calls GetEngineConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEngineConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.igetengineconfigrequest)`   
GetEngineConfigRequest message or plain object  
`callback` |  `[GetEngineConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and EngineConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEngineConfig(request)
    
    
    public getEngineConfig(request: google.cloud.financialservices.v1.IGetEngineConfigRequest): Promise<google.cloud.financialservices.v1.EngineConfig>;

Calls GetEngineConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEngineConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.igetengineconfigrequest)`   
GetEngineConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.financialservices.v1.EngineConfig](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.engineconfig-class)>` | Promise  
  
### getEngineVersion(request, callback)
    
    
    public getEngineVersion(request: google.cloud.financialservices.v1.IGetEngineVersionRequest, callback: google.cloud.financialservices.v1.AML.GetEngineVersionCallback): void;

Calls GetEngineVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEngineVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.igetengineversionrequest)`   
GetEngineVersionRequest message or plain object  
`callback` |  `[GetEngineVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and EngineVersion  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEngineVersion(request)
    
    
    public getEngineVersion(request: google.cloud.financialservices.v1.IGetEngineVersionRequest): Promise<google.cloud.financialservices.v1.EngineVersion>;

Calls GetEngineVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEngineVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.igetengineversionrequest)`   
GetEngineVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.financialservices.v1.EngineVersion](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.engineversion-class)>` | Promise  
  
### getInstance(request, callback)
    
    
    public getInstance(request: google.cloud.financialservices.v1.IGetInstanceRequest, callback: google.cloud.financialservices.v1.AML.GetInstanceCallback): void;

Calls GetInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.igetinstancerequest)`   
GetInstanceRequest message or plain object  
`callback` |  `[GetInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Instance  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getInstance(request)
    
    
    public getInstance(request: google.cloud.financialservices.v1.IGetInstanceRequest): Promise<google.cloud.financialservices.v1.Instance>;

Calls GetInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.igetinstancerequest)`   
GetInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.financialservices.v1.Instance](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.instance-class)>` | Promise  
  
### getModel(request, callback)
    
    
    public getModel(request: google.cloud.financialservices.v1.IGetModelRequest, callback: google.cloud.financialservices.v1.AML.GetModelCallback): void;

Calls GetModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.igetmodelrequest)`   
GetModelRequest message or plain object  
`callback` |  `[GetModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Model  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getModel(request)
    
    
    public getModel(request: google.cloud.financialservices.v1.IGetModelRequest): Promise<google.cloud.financialservices.v1.Model>;

Calls GetModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.igetmodelrequest)`   
GetModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.financialservices.v1.Model](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.model-class)>` | Promise  
  
### getPredictionResult(request, callback)
    
    
    public getPredictionResult(request: google.cloud.financialservices.v1.IGetPredictionResultRequest, callback: google.cloud.financialservices.v1.AML.GetPredictionResultCallback): void;

Calls GetPredictionResult.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPredictionResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.igetpredictionresultrequest)`   
GetPredictionResultRequest message or plain object  
`callback` |  `[GetPredictionResultCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and PredictionResult  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPredictionResult(request)
    
    
    public getPredictionResult(request: google.cloud.financialservices.v1.IGetPredictionResultRequest): Promise<google.cloud.financialservices.v1.PredictionResult>;

Calls GetPredictionResult.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetPredictionResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.igetpredictionresultrequest)`   
GetPredictionResultRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.financialservices.v1.PredictionResult](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.predictionresult-class)>` | Promise  
  
### importRegisteredParties(request, callback)
    
    
    public importRegisteredParties(request: google.cloud.financialservices.v1.IImportRegisteredPartiesRequest, callback: google.cloud.financialservices.v1.AML.ImportRegisteredPartiesCallback): void;

Calls ImportRegisteredParties.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportRegisteredPartiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iimportregisteredpartiesrequest)`   
ImportRegisteredPartiesRequest message or plain object  
`callback` |  `[ImportRegisteredPartiesCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importRegisteredParties(request)
    
    
    public importRegisteredParties(request: google.cloud.financialservices.v1.IImportRegisteredPartiesRequest): Promise<google.longrunning.Operation>;

Calls ImportRegisteredParties.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportRegisteredPartiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iimportregisteredpartiesrequest)`   
ImportRegisteredPartiesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### listBacktestResults(request, callback)
    
    
    public listBacktestResults(request: google.cloud.financialservices.v1.IListBacktestResultsRequest, callback: google.cloud.financialservices.v1.AML.ListBacktestResultsCallback): void;

Calls ListBacktestResults.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBacktestResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ilistbacktestresultsrequest)`   
ListBacktestResultsRequest message or plain object  
`callback` |  `[ListBacktestResultsCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and ListBacktestResultsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBacktestResults(request)
    
    
    public listBacktestResults(request: google.cloud.financialservices.v1.IListBacktestResultsRequest): Promise<google.cloud.financialservices.v1.ListBacktestResultsResponse>;

Calls ListBacktestResults.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListBacktestResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ilistbacktestresultsrequest)`   
ListBacktestResultsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.financialservices.v1.ListBacktestResultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.listbacktestresultsresponse)>` | Promise  
  
### listDatasets(request, callback)
    
    
    public listDatasets(request: google.cloud.financialservices.v1.IListDatasetsRequest, callback: google.cloud.financialservices.v1.AML.ListDatasetsCallback): void;

Calls ListDatasets.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ilistdatasetsrequest)`   
ListDatasetsRequest message or plain object  
`callback` |  `[ListDatasetsCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDatasetsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDatasets(request)
    
    
    public listDatasets(request: google.cloud.financialservices.v1.IListDatasetsRequest): Promise<google.cloud.financialservices.v1.ListDatasetsResponse>;

Calls ListDatasets.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ilistdatasetsrequest)`   
ListDatasetsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.financialservices.v1.ListDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.listdatasetsresponse)>` | Promise  
  
### listEngineConfigs(request, callback)
    
    
    public listEngineConfigs(request: google.cloud.financialservices.v1.IListEngineConfigsRequest, callback: google.cloud.financialservices.v1.AML.ListEngineConfigsCallback): void;

Calls ListEngineConfigs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEngineConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ilistengineconfigsrequest)`   
ListEngineConfigsRequest message or plain object  
`callback` |  `[ListEngineConfigsCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and ListEngineConfigsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEngineConfigs(request)
    
    
    public listEngineConfigs(request: google.cloud.financialservices.v1.IListEngineConfigsRequest): Promise<google.cloud.financialservices.v1.ListEngineConfigsResponse>;

Calls ListEngineConfigs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListEngineConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ilistengineconfigsrequest)`   
ListEngineConfigsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.financialservices.v1.ListEngineConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.listengineconfigsresponse)>` | Promise  
  
### listEngineVersions(request, callback)
    
    
    public listEngineVersions(request: google.cloud.financialservices.v1.IListEngineVersionsRequest, callback: google.cloud.financialservices.v1.AML.ListEngineVersionsCallback): void;

Calls ListEngineVersions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEngineVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ilistengineversionsrequest)`   
ListEngineVersionsRequest message or plain object  
`callback` |  `[ListEngineVersionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and ListEngineVersionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEngineVersions(request)
    
    
    public listEngineVersions(request: google.cloud.financialservices.v1.IListEngineVersionsRequest): Promise<google.cloud.financialservices.v1.ListEngineVersionsResponse>;

Calls ListEngineVersions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListEngineVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ilistengineversionsrequest)`   
ListEngineVersionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.financialservices.v1.ListEngineVersionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.listengineversionsresponse)>` | Promise  
  
### listInstances(request, callback)
    
    
    public listInstances(request: google.cloud.financialservices.v1.IListInstancesRequest, callback: google.cloud.financialservices.v1.AML.ListInstancesCallback): void;

Calls ListInstances.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ilistinstancesrequest)`   
ListInstancesRequest message or plain object  
`callback` |  `[ListInstancesCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and ListInstancesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listInstances(request)
    
    
    public listInstances(request: google.cloud.financialservices.v1.IListInstancesRequest): Promise<google.cloud.financialservices.v1.ListInstancesResponse>;

Calls ListInstances.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListInstancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ilistinstancesrequest)`   
ListInstancesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.financialservices.v1.ListInstancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.listinstancesresponse)>` | Promise  
  
### listModels(request, callback)
    
    
    public listModels(request: google.cloud.financialservices.v1.IListModelsRequest, callback: google.cloud.financialservices.v1.AML.ListModelsCallback): void;

Calls ListModels.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ilistmodelsrequest)`   
ListModelsRequest message or plain object  
`callback` |  `[ListModelsCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and ListModelsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listModels(request)
    
    
    public listModels(request: google.cloud.financialservices.v1.IListModelsRequest): Promise<google.cloud.financialservices.v1.ListModelsResponse>;

Calls ListModels.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ilistmodelsrequest)`   
ListModelsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.financialservices.v1.ListModelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.listmodelsresponse)>` | Promise  
  
### listPredictionResults(request, callback)
    
    
    public listPredictionResults(request: google.cloud.financialservices.v1.IListPredictionResultsRequest, callback: google.cloud.financialservices.v1.AML.ListPredictionResultsCallback): void;

Calls ListPredictionResults.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPredictionResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ilistpredictionresultsrequest)`   
ListPredictionResultsRequest message or plain object  
`callback` |  `[ListPredictionResultsCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and ListPredictionResultsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPredictionResults(request)
    
    
    public listPredictionResults(request: google.cloud.financialservices.v1.IListPredictionResultsRequest): Promise<google.cloud.financialservices.v1.ListPredictionResultsResponse>;

Calls ListPredictionResults.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListPredictionResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.ilistpredictionresultsrequest)`   
ListPredictionResultsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.financialservices.v1.ListPredictionResultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.listpredictionresultsresponse)>` | Promise  
  
### updateBacktestResult(request, callback)
    
    
    public updateBacktestResult(request: google.cloud.financialservices.v1.IUpdateBacktestResultRequest, callback: google.cloud.financialservices.v1.AML.UpdateBacktestResultCallback): void;

Calls UpdateBacktestResult.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBacktestResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iupdatebacktestresultrequest)`   
UpdateBacktestResultRequest message or plain object  
`callback` |  `[UpdateBacktestResultCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateBacktestResult(request)
    
    
    public updateBacktestResult(request: google.cloud.financialservices.v1.IUpdateBacktestResultRequest): Promise<google.longrunning.Operation>;

Calls UpdateBacktestResult.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBacktestResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iupdatebacktestresultrequest)`   
UpdateBacktestResultRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### updateDataset(request, callback)
    
    
    public updateDataset(request: google.cloud.financialservices.v1.IUpdateDatasetRequest, callback: google.cloud.financialservices.v1.AML.UpdateDatasetCallback): void;

Calls UpdateDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iupdatedatasetrequest)`   
UpdateDatasetRequest message or plain object  
`callback` |  `[UpdateDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataset(request)
    
    
    public updateDataset(request: google.cloud.financialservices.v1.IUpdateDatasetRequest): Promise<google.longrunning.Operation>;

Calls UpdateDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iupdatedatasetrequest)`   
UpdateDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### updateEngineConfig(request, callback)
    
    
    public updateEngineConfig(request: google.cloud.financialservices.v1.IUpdateEngineConfigRequest, callback: google.cloud.financialservices.v1.AML.UpdateEngineConfigCallback): void;

Calls UpdateEngineConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEngineConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iupdateengineconfigrequest)`   
UpdateEngineConfigRequest message or plain object  
`callback` |  `[UpdateEngineConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEngineConfig(request)
    
    
    public updateEngineConfig(request: google.cloud.financialservices.v1.IUpdateEngineConfigRequest): Promise<google.longrunning.Operation>;

Calls UpdateEngineConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEngineConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iupdateengineconfigrequest)`   
UpdateEngineConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### updateInstance(request, callback)
    
    
    public updateInstance(request: google.cloud.financialservices.v1.IUpdateInstanceRequest, callback: google.cloud.financialservices.v1.AML.UpdateInstanceCallback): void;

Calls UpdateInstance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iupdateinstancerequest)`   
UpdateInstanceRequest message or plain object  
`callback` |  `[UpdateInstanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateInstance(request)
    
    
    public updateInstance(request: google.cloud.financialservices.v1.IUpdateInstanceRequest): Promise<google.longrunning.Operation>;

Calls UpdateInstance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iupdateinstancerequest)`   
UpdateInstanceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### updateModel(request, callback)
    
    
    public updateModel(request: google.cloud.financialservices.v1.IUpdateModelRequest, callback: google.cloud.financialservices.v1.AML.UpdateModelCallback): void;

Calls UpdateModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iupdatemodelrequest)`   
UpdateModelRequest message or plain object  
`callback` |  `[UpdateModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateModel(request)
    
    
    public updateModel(request: google.cloud.financialservices.v1.IUpdateModelRequest): Promise<google.longrunning.Operation>;

Calls UpdateModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iupdatemodelrequest)`   
UpdateModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
### updatePredictionResult(request, callback)
    
    
    public updatePredictionResult(request: google.cloud.financialservices.v1.IUpdatePredictionResultRequest, callback: google.cloud.financialservices.v1.AML.UpdatePredictionResultCallback): void;

Calls UpdatePredictionResult.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePredictionResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iupdatepredictionresultrequest)`   
UpdatePredictionResultRequest message or plain object  
`callback` |  `[UpdatePredictionResultCallback](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updatePredictionResult(request)
    
    
    public updatePredictionResult(request: google.cloud.financialservices.v1.IUpdatePredictionResultRequest): Promise<google.longrunning.Operation>;

Calls UpdatePredictionResult.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePredictionResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.iupdatepredictionresultrequest)`   
UpdatePredictionResultRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
