---
url: https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.automl-class
title: Class protos.google.cloud.automl.v1beta1.AutoMl (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:49.304075+00:00
---

# Class protos.google.cloud.automl.v1beta1.AutoMl (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.automl-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.automl.v1beta1.AutoMl (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.1.3  4.0.1  3.1.2  2.5.2  2.4.5 

Represents an AutoMl

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.automl.v1beta1.AutoMl

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
`[AutoMl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.automl-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createDataset(request, callback)
    
    
    public createDataset(request: google.cloud.automl.v1beta1.ICreateDatasetRequest, callback: google.cloud.automl.v1beta1.AutoMl.CreateDatasetCallback): void;

Calls CreateDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icreatedatasetrequest)`   
CreateDatasetRequest message or plain object  
`callback` |  `[CreateDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Dataset  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataset(request)
    
    
    public createDataset(request: google.cloud.automl.v1beta1.ICreateDatasetRequest): Promise<google.cloud.automl.v1beta1.Dataset>;

Calls CreateDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icreatedatasetrequest)`   
CreateDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1beta1.Dataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.dataset)>` | Promise  
  
### createModel(request, callback)
    
    
    public createModel(request: google.cloud.automl.v1beta1.ICreateModelRequest, callback: google.cloud.automl.v1beta1.AutoMl.CreateModelCallback): void;

Calls CreateModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icreatemodelrequest)`   
CreateModelRequest message or plain object  
`callback` |  `[CreateModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createModel(request)
    
    
    public createModel(request: google.cloud.automl.v1beta1.ICreateModelRequest): Promise<google.longrunning.Operation>;

Calls CreateModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icreatemodelrequest)`   
CreateModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation)>` | Promise  
  
### deleteDataset(request, callback)
    
    
    public deleteDataset(request: google.cloud.automl.v1beta1.IDeleteDatasetRequest, callback: google.cloud.automl.v1beta1.AutoMl.DeleteDatasetCallback): void;

Calls DeleteDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ideletedatasetrequest)`   
DeleteDatasetRequest message or plain object  
`callback` |  `[DeleteDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataset(request)
    
    
    public deleteDataset(request: google.cloud.automl.v1beta1.IDeleteDatasetRequest): Promise<google.longrunning.Operation>;

Calls DeleteDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ideletedatasetrequest)`   
DeleteDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation)>` | Promise  
  
### deleteModel(request, callback)
    
    
    public deleteModel(request: google.cloud.automl.v1beta1.IDeleteModelRequest, callback: google.cloud.automl.v1beta1.AutoMl.DeleteModelCallback): void;

Calls DeleteModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ideletemodelrequest)`   
DeleteModelRequest message or plain object  
`callback` |  `[DeleteModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteModel(request)
    
    
    public deleteModel(request: google.cloud.automl.v1beta1.IDeleteModelRequest): Promise<google.longrunning.Operation>;

Calls DeleteModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ideletemodelrequest)`   
DeleteModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation)>` | Promise  
  
### deployModel(request, callback)
    
    
    public deployModel(request: google.cloud.automl.v1beta1.IDeployModelRequest, callback: google.cloud.automl.v1beta1.AutoMl.DeployModelCallback): void;

Calls DeployModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeployModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ideploymodelrequest)`   
DeployModelRequest message or plain object  
`callback` |  `[DeployModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deployModel(request)
    
    
    public deployModel(request: google.cloud.automl.v1beta1.IDeployModelRequest): Promise<google.longrunning.Operation>;

Calls DeployModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeployModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ideploymodelrequest)`   
DeployModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation)>` | Promise  
  
### exportData(request, callback)
    
    
    public exportData(request: google.cloud.automl.v1beta1.IExportDataRequest, callback: google.cloud.automl.v1beta1.AutoMl.ExportDataCallback): void;

Calls ExportData.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iexportdatarequest)`   
ExportDataRequest message or plain object  
`callback` |  `[ExportDataCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportData(request)
    
    
    public exportData(request: google.cloud.automl.v1beta1.IExportDataRequest): Promise<google.longrunning.Operation>;

Calls ExportData.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iexportdatarequest)`   
ExportDataRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation)>` | Promise  
  
### exportEvaluatedExamples(request, callback)
    
    
    public exportEvaluatedExamples(request: google.cloud.automl.v1beta1.IExportEvaluatedExamplesRequest, callback: google.cloud.automl.v1beta1.AutoMl.ExportEvaluatedExamplesCallback): void;

Calls ExportEvaluatedExamples.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportEvaluatedExamplesRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iexportevaluatedexamplesrequest)`   
ExportEvaluatedExamplesRequest message or plain object  
`callback` |  `[ExportEvaluatedExamplesCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportEvaluatedExamples(request)
    
    
    public exportEvaluatedExamples(request: google.cloud.automl.v1beta1.IExportEvaluatedExamplesRequest): Promise<google.longrunning.Operation>;

Calls ExportEvaluatedExamples.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportEvaluatedExamplesRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iexportevaluatedexamplesrequest)`   
ExportEvaluatedExamplesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation)>` | Promise  
  
### exportModel(request, callback)
    
    
    public exportModel(request: google.cloud.automl.v1beta1.IExportModelRequest, callback: google.cloud.automl.v1beta1.AutoMl.ExportModelCallback): void;

Calls ExportModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iexportmodelrequest)`   
ExportModelRequest message or plain object  
`callback` |  `[ExportModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportModel(request)
    
    
    public exportModel(request: google.cloud.automl.v1beta1.IExportModelRequest): Promise<google.longrunning.Operation>;

Calls ExportModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iexportmodelrequest)`   
ExportModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation)>` | Promise  
  
### getAnnotationSpec(request, callback)
    
    
    public getAnnotationSpec(request: google.cloud.automl.v1beta1.IGetAnnotationSpecRequest, callback: google.cloud.automl.v1beta1.AutoMl.GetAnnotationSpecCallback): void;

Calls GetAnnotationSpec.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotationSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetannotationspecrequest)`   
GetAnnotationSpecRequest message or plain object  
`callback` |  `[GetAnnotationSpecCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and AnnotationSpec  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAnnotationSpec(request)
    
    
    public getAnnotationSpec(request: google.cloud.automl.v1beta1.IGetAnnotationSpecRequest): Promise<google.cloud.automl.v1beta1.AnnotationSpec>;

Calls GetAnnotationSpec.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotationSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetannotationspecrequest)`   
GetAnnotationSpecRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1beta1.AnnotationSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.annotationspec)>` | Promise  
  
### getColumnSpec(request, callback)
    
    
    public getColumnSpec(request: google.cloud.automl.v1beta1.IGetColumnSpecRequest, callback: google.cloud.automl.v1beta1.AutoMl.GetColumnSpecCallback): void;

Calls GetColumnSpec.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetColumnSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetcolumnspecrequest)`   
GetColumnSpecRequest message or plain object  
`callback` |  `[GetColumnSpecCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and ColumnSpec  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getColumnSpec(request)
    
    
    public getColumnSpec(request: google.cloud.automl.v1beta1.IGetColumnSpecRequest): Promise<google.cloud.automl.v1beta1.ColumnSpec>;

Calls GetColumnSpec.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetColumnSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetcolumnspecrequest)`   
GetColumnSpecRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1beta1.ColumnSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.columnspec-class)>` | Promise  
  
### getDataset(request, callback)
    
    
    public getDataset(request: google.cloud.automl.v1beta1.IGetDatasetRequest, callback: google.cloud.automl.v1beta1.AutoMl.GetDatasetCallback): void;

Calls GetDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetdatasetrequest)`   
GetDatasetRequest message or plain object  
`callback` |  `[GetDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Dataset  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataset(request)
    
    
    public getDataset(request: google.cloud.automl.v1beta1.IGetDatasetRequest): Promise<google.cloud.automl.v1beta1.Dataset>;

Calls GetDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetdatasetrequest)`   
GetDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1beta1.Dataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.dataset)>` | Promise  
  
### getModel(request, callback)
    
    
    public getModel(request: google.cloud.automl.v1beta1.IGetModelRequest, callback: google.cloud.automl.v1beta1.AutoMl.GetModelCallback): void;

Calls GetModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetmodelrequest)`   
GetModelRequest message or plain object  
`callback` |  `[GetModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Model  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getModel(request)
    
    
    public getModel(request: google.cloud.automl.v1beta1.IGetModelRequest): Promise<google.cloud.automl.v1beta1.Model>;

Calls GetModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetmodelrequest)`   
GetModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1beta1.Model](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.model-class)>` | Promise  
  
### getModelEvaluation(request, callback)
    
    
    public getModelEvaluation(request: google.cloud.automl.v1beta1.IGetModelEvaluationRequest, callback: google.cloud.automl.v1beta1.AutoMl.GetModelEvaluationCallback): void;

Calls GetModelEvaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetModelEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetmodelevaluationrequest)`   
GetModelEvaluationRequest message or plain object  
`callback` |  `[GetModelEvaluationCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and ModelEvaluation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getModelEvaluation(request)
    
    
    public getModelEvaluation(request: google.cloud.automl.v1beta1.IGetModelEvaluationRequest): Promise<google.cloud.automl.v1beta1.ModelEvaluation>;

Calls GetModelEvaluation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetModelEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetmodelevaluationrequest)`   
GetModelEvaluationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1beta1.ModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.modelevaluation)>` | Promise  
  
### getTableSpec(request, callback)
    
    
    public getTableSpec(request: google.cloud.automl.v1beta1.IGetTableSpecRequest, callback: google.cloud.automl.v1beta1.AutoMl.GetTableSpecCallback): void;

Calls GetTableSpec.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTableSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igettablespecrequest)`   
GetTableSpecRequest message or plain object  
`callback` |  `[GetTableSpecCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and TableSpec  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTableSpec(request)
    
    
    public getTableSpec(request: google.cloud.automl.v1beta1.IGetTableSpecRequest): Promise<google.cloud.automl.v1beta1.TableSpec>;

Calls GetTableSpec.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetTableSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igettablespecrequest)`   
GetTableSpecRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1beta1.TableSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.tablespec)>` | Promise  
  
### importData(request, callback)
    
    
    public importData(request: google.cloud.automl.v1beta1.IImportDataRequest, callback: google.cloud.automl.v1beta1.AutoMl.ImportDataCallback): void;

Calls ImportData.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iimportdatarequest)`   
ImportDataRequest message or plain object  
`callback` |  `[ImportDataCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importData(request)
    
    
    public importData(request: google.cloud.automl.v1beta1.IImportDataRequest): Promise<google.longrunning.Operation>;

Calls ImportData.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iimportdatarequest)`   
ImportDataRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation)>` | Promise  
  
### listColumnSpecs(request, callback)
    
    
    public listColumnSpecs(request: google.cloud.automl.v1beta1.IListColumnSpecsRequest, callback: google.cloud.automl.v1beta1.AutoMl.ListColumnSpecsCallback): void;

Calls ListColumnSpecs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListColumnSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistcolumnspecsrequest)`   
ListColumnSpecsRequest message or plain object  
`callback` |  `[ListColumnSpecsCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and ListColumnSpecsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listColumnSpecs(request)
    
    
    public listColumnSpecs(request: google.cloud.automl.v1beta1.IListColumnSpecsRequest): Promise<google.cloud.automl.v1beta1.ListColumnSpecsResponse>;

Calls ListColumnSpecs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListColumnSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistcolumnspecsrequest)`   
ListColumnSpecsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1beta1.ListColumnSpecsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.listcolumnspecsresponse)>` | Promise  
  
### listDatasets(request, callback)
    
    
    public listDatasets(request: google.cloud.automl.v1beta1.IListDatasetsRequest, callback: google.cloud.automl.v1beta1.AutoMl.ListDatasetsCallback): void;

Calls ListDatasets.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistdatasetsrequest)`   
ListDatasetsRequest message or plain object  
`callback` |  `[ListDatasetsCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDatasetsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDatasets(request)
    
    
    public listDatasets(request: google.cloud.automl.v1beta1.IListDatasetsRequest): Promise<google.cloud.automl.v1beta1.ListDatasetsResponse>;

Calls ListDatasets.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistdatasetsrequest)`   
ListDatasetsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1beta1.ListDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.listdatasetsresponse)>` | Promise  
  
### listModelEvaluations(request, callback)
    
    
    public listModelEvaluations(request: google.cloud.automl.v1beta1.IListModelEvaluationsRequest, callback: google.cloud.automl.v1beta1.AutoMl.ListModelEvaluationsCallback): void;

Calls ListModelEvaluations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelevaluationsrequest)`   
ListModelEvaluationsRequest message or plain object  
`callback` |  `[ListModelEvaluationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and ListModelEvaluationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listModelEvaluations(request)
    
    
    public listModelEvaluations(request: google.cloud.automl.v1beta1.IListModelEvaluationsRequest): Promise<google.cloud.automl.v1beta1.ListModelEvaluationsResponse>;

Calls ListModelEvaluations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListModelEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelevaluationsrequest)`   
ListModelEvaluationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1beta1.ListModelEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.listmodelevaluationsresponse)>` | Promise  
  
### listModels(request, callback)
    
    
    public listModels(request: google.cloud.automl.v1beta1.IListModelsRequest, callback: google.cloud.automl.v1beta1.AutoMl.ListModelsCallback): void;

Calls ListModels.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelsrequest)`   
ListModelsRequest message or plain object  
`callback` |  `[ListModelsCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and ListModelsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listModels(request)
    
    
    public listModels(request: google.cloud.automl.v1beta1.IListModelsRequest): Promise<google.cloud.automl.v1beta1.ListModelsResponse>;

Calls ListModels.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelsrequest)`   
ListModelsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1beta1.ListModelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.listmodelsresponse)>` | Promise  
  
### listTableSpecs(request, callback)
    
    
    public listTableSpecs(request: google.cloud.automl.v1beta1.IListTableSpecsRequest, callback: google.cloud.automl.v1beta1.AutoMl.ListTableSpecsCallback): void;

Calls ListTableSpecs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTableSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilisttablespecsrequest)`   
ListTableSpecsRequest message or plain object  
`callback` |  `[ListTableSpecsCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and ListTableSpecsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTableSpecs(request)
    
    
    public listTableSpecs(request: google.cloud.automl.v1beta1.IListTableSpecsRequest): Promise<google.cloud.automl.v1beta1.ListTableSpecsResponse>;

Calls ListTableSpecs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListTableSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilisttablespecsrequest)`   
ListTableSpecsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1beta1.ListTableSpecsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.listtablespecsresponse)>` | Promise  
  
### undeployModel(request, callback)
    
    
    public undeployModel(request: google.cloud.automl.v1beta1.IUndeployModelRequest, callback: google.cloud.automl.v1beta1.AutoMl.UndeployModelCallback): void;

Calls UndeployModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUndeployModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iundeploymodelrequest)`   
UndeployModelRequest message or plain object  
`callback` |  `[UndeployModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### undeployModel(request)
    
    
    public undeployModel(request: google.cloud.automl.v1beta1.IUndeployModelRequest): Promise<google.longrunning.Operation>;

Calls UndeployModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUndeployModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iundeploymodelrequest)`   
UndeployModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation)>` | Promise  
  
### updateColumnSpec(request, callback)
    
    
    public updateColumnSpec(request: google.cloud.automl.v1beta1.IUpdateColumnSpecRequest, callback: google.cloud.automl.v1beta1.AutoMl.UpdateColumnSpecCallback): void;

Calls UpdateColumnSpec.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateColumnSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatecolumnspecrequest)`   
UpdateColumnSpecRequest message or plain object  
`callback` |  `[UpdateColumnSpecCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and ColumnSpec  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateColumnSpec(request)
    
    
    public updateColumnSpec(request: google.cloud.automl.v1beta1.IUpdateColumnSpecRequest): Promise<google.cloud.automl.v1beta1.ColumnSpec>;

Calls UpdateColumnSpec.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateColumnSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatecolumnspecrequest)`   
UpdateColumnSpecRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1beta1.ColumnSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.columnspec-class)>` | Promise  
  
### updateDataset(request, callback)
    
    
    public updateDataset(request: google.cloud.automl.v1beta1.IUpdateDatasetRequest, callback: google.cloud.automl.v1beta1.AutoMl.UpdateDatasetCallback): void;

Calls UpdateDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatedatasetrequest)`   
UpdateDatasetRequest message or plain object  
`callback` |  `[UpdateDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and Dataset  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataset(request)
    
    
    public updateDataset(request: google.cloud.automl.v1beta1.IUpdateDatasetRequest): Promise<google.cloud.automl.v1beta1.Dataset>;

Calls UpdateDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatedatasetrequest)`   
UpdateDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1beta1.Dataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.dataset)>` | Promise  
  
### updateTableSpec(request, callback)
    
    
    public updateTableSpec(request: google.cloud.automl.v1beta1.IUpdateTableSpecRequest, callback: google.cloud.automl.v1beta1.AutoMl.UpdateTableSpecCallback): void;

Calls UpdateTableSpec.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTableSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatetablespecrequest)`   
UpdateTableSpecRequest message or plain object  
`callback` |  `[UpdateTableSpecCallback](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)`   
Node-style callback called with the error, if any, and TableSpec  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTableSpec(request)
    
    
    public updateTableSpec(request: google.cloud.automl.v1beta1.IUpdateTableSpecRequest): Promise<google.cloud.automl.v1beta1.TableSpec>;

Calls UpdateTableSpec.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTableSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatetablespecrequest)`   
UpdateTableSpecRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.automl.v1beta1.TableSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.tablespec)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
