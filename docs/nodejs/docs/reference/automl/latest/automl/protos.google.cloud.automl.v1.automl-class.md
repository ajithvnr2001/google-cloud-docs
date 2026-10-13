---
url: https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.automl-class
title: Class protos.google.cloud.automl.v1.AutoMl (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:29.137757+00:00
---

# Class protos.google.cloud.automl.v1.AutoMl (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.automl-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.automl.v1.AutoMl (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.1.3  4.0.1  3.1.2  2.5.2  2.4.5 

Represents an AutoMl

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.automl.v1.AutoMl

## Package

[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AutoMl service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AutoMl;

Creates new AutoMl service using the specified rpc implementation.

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
`[AutoMl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.automl-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createDataset(request, callback)
    
    
    public createDataset(request: google.cloud.automl.v1.ICreateDatasetRequest, callback: google.cloud.automl.v1.AutoMl.CreateDatasetCallback): void;

Calls CreateDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.icreatedatasetrequest)`   
CreateDatasetRequest message or plain object  
`callback` |  `[CreateDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataset(request)
    
    
    public createDataset(request: google.cloud.automl.v1.ICreateDatasetRequest): Promise<google.longrunning.Operation>;

Calls CreateDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.icreatedatasetrequest)`   
CreateDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation)>` | Promise  
  
### createModel(request, callback)
    
    
    public createModel(request: google.cloud.automl.v1.ICreateModelRequest, callback: google.cloud.automl.v1.AutoMl.CreateModelCallback): void;

Calls CreateModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.icreatemodelrequest)`   
CreateModelRequest message or plain object  
`callback` |  `[CreateModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createModel(request)
    
    
    public createModel(request: google.cloud.automl.v1.ICreateModelRequest): Promise<google.longrunning.Operation>;

Calls CreateModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.icreatemodelrequest)`   
CreateModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation)>` | Promise  
  
### deleteDataset(request, callback)
    
    
    public deleteDataset(request: google.cloud.automl.v1.IDeleteDatasetRequest, callback: google.cloud.automl.v1.AutoMl.DeleteDatasetCallback): void;

Calls DeleteDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.ideletedatasetrequest)`   
DeleteDatasetRequest message or plain object  
`callback` |  `[DeleteDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataset(request)
    
    
    public deleteDataset(request: google.cloud.automl.v1.IDeleteDatasetRequest): Promise<google.longrunning.Operation>;

Calls DeleteDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.ideletedatasetrequest)`   
DeleteDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation)>` | Promise  
  
### deleteModel(request, callback)
    
    
    public deleteModel(request: google.cloud.automl.v1.IDeleteModelRequest, callback: google.cloud.automl.v1.AutoMl.DeleteModelCallback): void;

Calls DeleteModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.ideletemodelrequest)`   
DeleteModelRequest message or plain object  
`callback` |  `[DeleteModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteModel(request)
    
    
    public deleteModel(request: google.cloud.automl.v1.IDeleteModelRequest): Promise<google.longrunning.Operation>;

Calls DeleteModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.ideletemodelrequest)`   
DeleteModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation)>` | Promise  
  
### deployModel(request, callback)
    
    
    public deployModel(request: google.cloud.automl.v1.IDeployModelRequest, callback: google.cloud.automl.v1.AutoMl.DeployModelCallback): void;

Calls DeployModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeployModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.ideploymodelrequest)`   
DeployModelRequest message or plain object  
`callback` |  `[DeployModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deployModel(request)
    
    
    public deployModel(request: google.cloud.automl.v1.IDeployModelRequest): Promise<google.longrunning.Operation>;

Calls DeployModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeployModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.ideploymodelrequest)`   
DeployModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation)>` | Promise  
  
### exportData(request, callback)
    
    
    public exportData(request: google.cloud.automl.v1.IExportDataRequest, callback: google.cloud.automl.v1.AutoMl.ExportDataCallback): void;

Calls ExportData.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.iexportdatarequest)`   
ExportDataRequest message or plain object  
`callback` |  `[ExportDataCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportData(request)
    
    
    public exportData(request: google.cloud.automl.v1.IExportDataRequest): Promise<google.longrunning.Operation>;

Calls ExportData.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.iexportdatarequest)`   
ExportDataRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation)>` | Promise  
  
### exportModel(request, callback)
    
    
    public exportModel(request: google.cloud.automl.v1.IExportModelRequest, callback: google.cloud.automl.v1.AutoMl.ExportModelCallback): void;

Calls ExportModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.iexportmodelrequest)`   
ExportModelRequest message or plain object  
`callback` |  `[ExportModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportModel(request)
    
    
    public exportModel(request: google.cloud.automl.v1.IExportModelRequest): Promise<google.longrunning.Operation>;

Calls ExportModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.iexportmodelrequest)`   
ExportModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation)>` | Promise  
  
### getAnnotationSpec(request, callback)
    
    
    public getAnnotationSpec(request: google.cloud.automl.v1.IGetAnnotationSpecRequest, callback: google.cloud.automl.v1.AutoMl.GetAnnotationSpecCallback): void;

Calls GetAnnotationSpec.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotationSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.igetannotationspecrequest)`   
GetAnnotationSpecRequest message or plain object  
`callback` |  `[GetAnnotationSpecCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and AnnotationSpec  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAnnotationSpec(request)
    
    
    public getAnnotationSpec(request: google.cloud.automl.v1.IGetAnnotationSpecRequest): Promise<google.cloud.automl.v1.AnnotationSpec>;

Calls GetAnnotationSpec.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotationSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.igetannotationspecrequest)`   
GetAnnotationSpecRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1.AnnotationSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.annotationspec)>` | Promise  
  
### getDataset(request, callback)
    
    
    public getDataset(request: google.cloud.automl.v1.IGetDatasetRequest, callback: google.cloud.automl.v1.AutoMl.GetDatasetCallback): void;

Calls GetDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.igetdatasetrequest)`   
GetDatasetRequest message or plain object  
`callback` |  `[GetDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Dataset  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataset(request)
    
    
    public getDataset(request: google.cloud.automl.v1.IGetDatasetRequest): Promise<google.cloud.automl.v1.Dataset>;

Calls GetDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.igetdatasetrequest)`   
GetDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1.Dataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.dataset)>` | Promise  
  
### getModel(request, callback)
    
    
    public getModel(request: google.cloud.automl.v1.IGetModelRequest, callback: google.cloud.automl.v1.AutoMl.GetModelCallback): void;

Calls GetModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.igetmodelrequest)`   
GetModelRequest message or plain object  
`callback` |  `[GetModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Model  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getModel(request)
    
    
    public getModel(request: google.cloud.automl.v1.IGetModelRequest): Promise<google.cloud.automl.v1.Model>;

Calls GetModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.igetmodelrequest)`   
GetModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1.Model](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.model-class)>` | Promise  
  
### getModelEvaluation(request, callback)
    
    
    public getModelEvaluation(request: google.cloud.automl.v1.IGetModelEvaluationRequest, callback: google.cloud.automl.v1.AutoMl.GetModelEvaluationCallback): void;

Calls GetModelEvaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetModelEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.igetmodelevaluationrequest)`   
GetModelEvaluationRequest message or plain object  
`callback` |  `[GetModelEvaluationCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and ModelEvaluation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getModelEvaluation(request)
    
    
    public getModelEvaluation(request: google.cloud.automl.v1.IGetModelEvaluationRequest): Promise<google.cloud.automl.v1.ModelEvaluation>;

Calls GetModelEvaluation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetModelEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.igetmodelevaluationrequest)`   
GetModelEvaluationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1.ModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.modelevaluation)>` | Promise  
  
### importData(request, callback)
    
    
    public importData(request: google.cloud.automl.v1.IImportDataRequest, callback: google.cloud.automl.v1.AutoMl.ImportDataCallback): void;

Calls ImportData.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.iimportdatarequest)`   
ImportDataRequest message or plain object  
`callback` |  `[ImportDataCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importData(request)
    
    
    public importData(request: google.cloud.automl.v1.IImportDataRequest): Promise<google.longrunning.Operation>;

Calls ImportData.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.iimportdatarequest)`   
ImportDataRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation)>` | Promise  
  
### listDatasets(request, callback)
    
    
    public listDatasets(request: google.cloud.automl.v1.IListDatasetsRequest, callback: google.cloud.automl.v1.AutoMl.ListDatasetsCallback): void;

Calls ListDatasets.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.ilistdatasetsrequest)`   
ListDatasetsRequest message or plain object  
`callback` |  `[ListDatasetsCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDatasetsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDatasets(request)
    
    
    public listDatasets(request: google.cloud.automl.v1.IListDatasetsRequest): Promise<google.cloud.automl.v1.ListDatasetsResponse>;

Calls ListDatasets.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.ilistdatasetsrequest)`   
ListDatasetsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1.ListDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.listdatasetsresponse)>` | Promise  
  
### listModelEvaluations(request, callback)
    
    
    public listModelEvaluations(request: google.cloud.automl.v1.IListModelEvaluationsRequest, callback: google.cloud.automl.v1.AutoMl.ListModelEvaluationsCallback): void;

Calls ListModelEvaluations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.ilistmodelevaluationsrequest)`   
ListModelEvaluationsRequest message or plain object  
`callback` |  `[ListModelEvaluationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and ListModelEvaluationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listModelEvaluations(request)
    
    
    public listModelEvaluations(request: google.cloud.automl.v1.IListModelEvaluationsRequest): Promise<google.cloud.automl.v1.ListModelEvaluationsResponse>;

Calls ListModelEvaluations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListModelEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.ilistmodelevaluationsrequest)`   
ListModelEvaluationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1.ListModelEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.listmodelevaluationsresponse)>` | Promise  
  
### listModels(request, callback)
    
    
    public listModels(request: google.cloud.automl.v1.IListModelsRequest, callback: google.cloud.automl.v1.AutoMl.ListModelsCallback): void;

Calls ListModels.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.ilistmodelsrequest)`   
ListModelsRequest message or plain object  
`callback` |  `[ListModelsCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and ListModelsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listModels(request)
    
    
    public listModels(request: google.cloud.automl.v1.IListModelsRequest): Promise<google.cloud.automl.v1.ListModelsResponse>;

Calls ListModels.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.ilistmodelsrequest)`   
ListModelsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1.ListModelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.listmodelsresponse)>` | Promise  
  
### undeployModel(request, callback)
    
    
    public undeployModel(request: google.cloud.automl.v1.IUndeployModelRequest, callback: google.cloud.automl.v1.AutoMl.UndeployModelCallback): void;

Calls UndeployModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUndeployModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.iundeploymodelrequest)`   
UndeployModelRequest message or plain object  
`callback` |  `[UndeployModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### undeployModel(request)
    
    
    public undeployModel(request: google.cloud.automl.v1.IUndeployModelRequest): Promise<google.longrunning.Operation>;

Calls UndeployModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUndeployModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.iundeploymodelrequest)`   
UndeployModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation)>` | Promise  
  
### updateDataset(request, callback)
    
    
    public updateDataset(request: google.cloud.automl.v1.IUpdateDatasetRequest, callback: google.cloud.automl.v1.AutoMl.UpdateDatasetCallback): void;

Calls UpdateDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.iupdatedatasetrequest)`   
UpdateDatasetRequest message or plain object  
`callback` |  `[UpdateDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Dataset  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataset(request)
    
    
    public updateDataset(request: google.cloud.automl.v1.IUpdateDatasetRequest): Promise<google.cloud.automl.v1.Dataset>;

Calls UpdateDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.iupdatedatasetrequest)`   
UpdateDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1.Dataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.dataset)>` | Promise  
  
### updateModel(request, callback)
    
    
    public updateModel(request: google.cloud.automl.v1.IUpdateModelRequest, callback: google.cloud.automl.v1.AutoMl.UpdateModelCallback): void;

Calls UpdateModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.iupdatemodelrequest)`   
UpdateModelRequest message or plain object  
`callback` |  `[UpdateModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Model  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateModel(request)
    
    
    public updateModel(request: google.cloud.automl.v1.IUpdateModelRequest): Promise<google.cloud.automl.v1.Model>;

Calls UpdateModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.iupdatemodelrequest)`   
UpdateModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1.Model](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.model-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
