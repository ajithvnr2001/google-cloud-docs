---
url: https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.datalabelingservice-class
title: Class protos.google.cloud.datalabeling.v1beta1.DataLabelingService (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:51.102024+00:00
---

# Class protos.google.cloud.datalabeling.v1beta1.DataLabelingService (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.datalabelingservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.datalabeling.v1beta1.DataLabelingService (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  3.2.2  3.1.1  2.3.0  2.2.7 

Represents a DataLabelingService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.datalabeling.v1beta1.DataLabelingService

## Package

[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DataLabelingService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DataLabelingService;

Creates new DataLabelingService service using the specified rpc implementation.

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
`[DataLabelingService](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.datalabelingservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAnnotationSpecSet(request, callback)
    
    
    public createAnnotationSpecSet(request: google.cloud.datalabeling.v1beta1.ICreateAnnotationSpecSetRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.CreateAnnotationSpecSetCallback): void;

Calls CreateAnnotationSpecSet.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateannotationspecsetrequest)`   
CreateAnnotationSpecSetRequest message or plain object  
`callback` |  `[CreateAnnotationSpecSetCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and AnnotationSpecSet  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAnnotationSpecSet(request)
    
    
    public createAnnotationSpecSet(request: google.cloud.datalabeling.v1beta1.ICreateAnnotationSpecSetRequest): Promise<google.cloud.datalabeling.v1beta1.AnnotationSpecSet>;

Calls CreateAnnotationSpecSet.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateannotationspecsetrequest)`   
CreateAnnotationSpecSetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datalabeling.v1beta1.AnnotationSpecSet](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotationspecset)>` | Promise  
  
### createDataset(request, callback)
    
    
    public createDataset(request: google.cloud.datalabeling.v1beta1.ICreateDatasetRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.CreateDatasetCallback): void;

Calls CreateDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreatedatasetrequest)`   
CreateDatasetRequest message or plain object  
`callback` |  `[CreateDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and Dataset  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataset(request)
    
    
    public createDataset(request: google.cloud.datalabeling.v1beta1.ICreateDatasetRequest): Promise<google.cloud.datalabeling.v1beta1.Dataset>;

Calls CreateDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreatedatasetrequest)`   
CreateDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datalabeling.v1beta1.Dataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.dataset)>` | Promise  
  
### createEvaluationJob(request, callback)
    
    
    public createEvaluationJob(request: google.cloud.datalabeling.v1beta1.ICreateEvaluationJobRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.CreateEvaluationJobCallback): void;

Calls CreateEvaluationJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateevaluationjobrequest)`   
CreateEvaluationJobRequest message or plain object  
`callback` |  `[CreateEvaluationJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and EvaluationJob  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEvaluationJob(request)
    
    
    public createEvaluationJob(request: google.cloud.datalabeling.v1beta1.ICreateEvaluationJobRequest): Promise<google.cloud.datalabeling.v1beta1.EvaluationJob>;

Calls CreateEvaluationJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateevaluationjobrequest)`   
CreateEvaluationJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datalabeling.v1beta1.EvaluationJob](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.evaluationjob-class)>` | Promise  
  
### createInstruction(request, callback)
    
    
    public createInstruction(request: google.cloud.datalabeling.v1beta1.ICreateInstructionRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.CreateInstructionCallback): void;

Calls CreateInstruction.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateInstructionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateinstructionrequest)`   
CreateInstructionRequest message or plain object  
`callback` |  `[CreateInstructionCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createInstruction(request)
    
    
    public createInstruction(request: google.cloud.datalabeling.v1beta1.ICreateInstructionRequest): Promise<google.longrunning.Operation>;

Calls CreateInstruction.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateInstructionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateinstructionrequest)`   
CreateInstructionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.operation)>` | Promise  
  
### deleteAnnotatedDataset(request, callback)
    
    
    public deleteAnnotatedDataset(request: google.cloud.datalabeling.v1beta1.IDeleteAnnotatedDatasetRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.DeleteAnnotatedDatasetCallback): void;

Calls DeleteAnnotatedDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAnnotatedDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteannotateddatasetrequest)`   
DeleteAnnotatedDatasetRequest message or plain object  
`callback` |  `[DeleteAnnotatedDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAnnotatedDataset(request)
    
    
    public deleteAnnotatedDataset(request: google.cloud.datalabeling.v1beta1.IDeleteAnnotatedDatasetRequest): Promise<google.protobuf.Empty>;

Calls DeleteAnnotatedDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAnnotatedDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteannotateddatasetrequest)`   
DeleteAnnotatedDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.empty)>` | Promise  
  
### deleteAnnotationSpecSet(request, callback)
    
    
    public deleteAnnotationSpecSet(request: google.cloud.datalabeling.v1beta1.IDeleteAnnotationSpecSetRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.DeleteAnnotationSpecSetCallback): void;

Calls DeleteAnnotationSpecSet.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteannotationspecsetrequest)`   
DeleteAnnotationSpecSetRequest message or plain object  
`callback` |  `[DeleteAnnotationSpecSetCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAnnotationSpecSet(request)
    
    
    public deleteAnnotationSpecSet(request: google.cloud.datalabeling.v1beta1.IDeleteAnnotationSpecSetRequest): Promise<google.protobuf.Empty>;

Calls DeleteAnnotationSpecSet.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteannotationspecsetrequest)`   
DeleteAnnotationSpecSetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.empty)>` | Promise  
  
### deleteDataset(request, callback)
    
    
    public deleteDataset(request: google.cloud.datalabeling.v1beta1.IDeleteDatasetRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.DeleteDatasetCallback): void;

Calls DeleteDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideletedatasetrequest)`   
DeleteDatasetRequest message or plain object  
`callback` |  `[DeleteDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataset(request)
    
    
    public deleteDataset(request: google.cloud.datalabeling.v1beta1.IDeleteDatasetRequest): Promise<google.protobuf.Empty>;

Calls DeleteDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideletedatasetrequest)`   
DeleteDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.empty)>` | Promise  
  
### deleteEvaluationJob(request, callback)
    
    
    public deleteEvaluationJob(request: google.cloud.datalabeling.v1beta1.IDeleteEvaluationJobRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.DeleteEvaluationJobCallback): void;

Calls DeleteEvaluationJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteevaluationjobrequest)`   
DeleteEvaluationJobRequest message or plain object  
`callback` |  `[DeleteEvaluationJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEvaluationJob(request)
    
    
    public deleteEvaluationJob(request: google.cloud.datalabeling.v1beta1.IDeleteEvaluationJobRequest): Promise<google.protobuf.Empty>;

Calls DeleteEvaluationJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteevaluationjobrequest)`   
DeleteEvaluationJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.empty)>` | Promise  
  
### deleteInstruction(request, callback)
    
    
    public deleteInstruction(request: google.cloud.datalabeling.v1beta1.IDeleteInstructionRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.DeleteInstructionCallback): void;

Calls DeleteInstruction.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteInstructionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteinstructionrequest)`   
DeleteInstructionRequest message or plain object  
`callback` |  `[DeleteInstructionCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteInstruction(request)
    
    
    public deleteInstruction(request: google.cloud.datalabeling.v1beta1.IDeleteInstructionRequest): Promise<google.protobuf.Empty>;

Calls DeleteInstruction.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteInstructionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteinstructionrequest)`   
DeleteInstructionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.empty)>` | Promise  
  
### exportData(request, callback)
    
    
    public exportData(request: google.cloud.datalabeling.v1beta1.IExportDataRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.ExportDataCallback): void;

Calls ExportData.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iexportdatarequest)`   
ExportDataRequest message or plain object  
`callback` |  `[ExportDataCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportData(request)
    
    
    public exportData(request: google.cloud.datalabeling.v1beta1.IExportDataRequest): Promise<google.longrunning.Operation>;

Calls ExportData.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iexportdatarequest)`   
ExportDataRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.operation)>` | Promise  
  
### getAnnotatedDataset(request, callback)
    
    
    public getAnnotatedDataset(request: google.cloud.datalabeling.v1beta1.IGetAnnotatedDatasetRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.GetAnnotatedDatasetCallback): void;

Calls GetAnnotatedDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotatedDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetannotateddatasetrequest)`   
GetAnnotatedDatasetRequest message or plain object  
`callback` |  `[GetAnnotatedDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and AnnotatedDataset  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAnnotatedDataset(request)
    
    
    public getAnnotatedDataset(request: google.cloud.datalabeling.v1beta1.IGetAnnotatedDatasetRequest): Promise<google.cloud.datalabeling.v1beta1.AnnotatedDataset>;

Calls GetAnnotatedDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotatedDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetannotateddatasetrequest)`   
GetAnnotatedDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datalabeling.v1beta1.AnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotateddataset)>` | Promise  
  
### getAnnotationSpecSet(request, callback)
    
    
    public getAnnotationSpecSet(request: google.cloud.datalabeling.v1beta1.IGetAnnotationSpecSetRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.GetAnnotationSpecSetCallback): void;

Calls GetAnnotationSpecSet.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetannotationspecsetrequest)`   
GetAnnotationSpecSetRequest message or plain object  
`callback` |  `[GetAnnotationSpecSetCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and AnnotationSpecSet  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAnnotationSpecSet(request)
    
    
    public getAnnotationSpecSet(request: google.cloud.datalabeling.v1beta1.IGetAnnotationSpecSetRequest): Promise<google.cloud.datalabeling.v1beta1.AnnotationSpecSet>;

Calls GetAnnotationSpecSet.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetannotationspecsetrequest)`   
GetAnnotationSpecSetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datalabeling.v1beta1.AnnotationSpecSet](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotationspecset)>` | Promise  
  
### getDataItem(request, callback)
    
    
    public getDataItem(request: google.cloud.datalabeling.v1beta1.IGetDataItemRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.GetDataItemCallback): void;

Calls GetDataItem.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataItemRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetdataitemrequest)`   
GetDataItemRequest message or plain object  
`callback` |  `[GetDataItemCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and DataItem  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataItem(request)
    
    
    public getDataItem(request: google.cloud.datalabeling.v1beta1.IGetDataItemRequest): Promise<google.cloud.datalabeling.v1beta1.DataItem>;

Calls GetDataItem.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataItemRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetdataitemrequest)`   
GetDataItemRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datalabeling.v1beta1.DataItem](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.dataitem)>` | Promise  
  
### getDataset(request, callback)
    
    
    public getDataset(request: google.cloud.datalabeling.v1beta1.IGetDatasetRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.GetDatasetCallback): void;

Calls GetDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetdatasetrequest)`   
GetDatasetRequest message or plain object  
`callback` |  `[GetDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and Dataset  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataset(request)
    
    
    public getDataset(request: google.cloud.datalabeling.v1beta1.IGetDatasetRequest): Promise<google.cloud.datalabeling.v1beta1.Dataset>;

Calls GetDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetdatasetrequest)`   
GetDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datalabeling.v1beta1.Dataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.dataset)>` | Promise  
  
### getEvaluation(request, callback)
    
    
    public getEvaluation(request: google.cloud.datalabeling.v1beta1.IGetEvaluationRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.GetEvaluationCallback): void;

Calls GetEvaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetevaluationrequest)`   
GetEvaluationRequest message or plain object  
`callback` |  `[GetEvaluationCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and Evaluation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEvaluation(request)
    
    
    public getEvaluation(request: google.cloud.datalabeling.v1beta1.IGetEvaluationRequest): Promise<google.cloud.datalabeling.v1beta1.Evaluation>;

Calls GetEvaluation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetevaluationrequest)`   
GetEvaluationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datalabeling.v1beta1.Evaluation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.evaluation)>` | Promise  
  
### getEvaluationJob(request, callback)
    
    
    public getEvaluationJob(request: google.cloud.datalabeling.v1beta1.IGetEvaluationJobRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.GetEvaluationJobCallback): void;

Calls GetEvaluationJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetevaluationjobrequest)`   
GetEvaluationJobRequest message or plain object  
`callback` |  `[GetEvaluationJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and EvaluationJob  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEvaluationJob(request)
    
    
    public getEvaluationJob(request: google.cloud.datalabeling.v1beta1.IGetEvaluationJobRequest): Promise<google.cloud.datalabeling.v1beta1.EvaluationJob>;

Calls GetEvaluationJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetevaluationjobrequest)`   
GetEvaluationJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datalabeling.v1beta1.EvaluationJob](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.evaluationjob-class)>` | Promise  
  
### getExample(request, callback)
    
    
    public getExample(request: google.cloud.datalabeling.v1beta1.IGetExampleRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.GetExampleCallback): void;

Calls GetExample.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetExampleRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetexamplerequest)`   
GetExampleRequest message or plain object  
`callback` |  `[GetExampleCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and Example  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getExample(request)
    
    
    public getExample(request: google.cloud.datalabeling.v1beta1.IGetExampleRequest): Promise<google.cloud.datalabeling.v1beta1.Example>;

Calls GetExample.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetExampleRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetexamplerequest)`   
GetExampleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datalabeling.v1beta1.Example](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.example)>` | Promise  
  
### getInstruction(request, callback)
    
    
    public getInstruction(request: google.cloud.datalabeling.v1beta1.IGetInstructionRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.GetInstructionCallback): void;

Calls GetInstruction.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetInstructionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetinstructionrequest)`   
GetInstructionRequest message or plain object  
`callback` |  `[GetInstructionCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and Instruction  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getInstruction(request)
    
    
    public getInstruction(request: google.cloud.datalabeling.v1beta1.IGetInstructionRequest): Promise<google.cloud.datalabeling.v1beta1.Instruction>;

Calls GetInstruction.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetInstructionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetinstructionrequest)`   
GetInstructionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datalabeling.v1beta1.Instruction](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.instruction)>` | Promise  
  
### importData(request, callback)
    
    
    public importData(request: google.cloud.datalabeling.v1beta1.IImportDataRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.ImportDataCallback): void;

Calls ImportData.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iimportdatarequest)`   
ImportDataRequest message or plain object  
`callback` |  `[ImportDataCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importData(request)
    
    
    public importData(request: google.cloud.datalabeling.v1beta1.IImportDataRequest): Promise<google.longrunning.Operation>;

Calls ImportData.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iimportdatarequest)`   
ImportDataRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.operation)>` | Promise  
  
### labelImage(request, callback)
    
    
    public labelImage(request: google.cloud.datalabeling.v1beta1.ILabelImageRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.LabelImageCallback): void;

Calls LabelImage.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILabelImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabelimagerequest)`   
LabelImageRequest message or plain object  
`callback` |  `[LabelImageCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### labelImage(request)
    
    
    public labelImage(request: google.cloud.datalabeling.v1beta1.ILabelImageRequest): Promise<google.longrunning.Operation>;

Calls LabelImage.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ILabelImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabelimagerequest)`   
LabelImageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.operation)>` | Promise  
  
### labelText(request, callback)
    
    
    public labelText(request: google.cloud.datalabeling.v1beta1.ILabelTextRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.LabelTextCallback): void;

Calls LabelText.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILabelTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabeltextrequest)`   
LabelTextRequest message or plain object  
`callback` |  `[LabelTextCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### labelText(request)
    
    
    public labelText(request: google.cloud.datalabeling.v1beta1.ILabelTextRequest): Promise<google.longrunning.Operation>;

Calls LabelText.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ILabelTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabeltextrequest)`   
LabelTextRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.operation)>` | Promise  
  
### labelVideo(request, callback)
    
    
    public labelVideo(request: google.cloud.datalabeling.v1beta1.ILabelVideoRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.LabelVideoCallback): void;

Calls LabelVideo.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILabelVideoRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabelvideorequest)`   
LabelVideoRequest message or plain object  
`callback` |  `[LabelVideoCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### labelVideo(request)
    
    
    public labelVideo(request: google.cloud.datalabeling.v1beta1.ILabelVideoRequest): Promise<google.longrunning.Operation>;

Calls LabelVideo.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ILabelVideoRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabelvideorequest)`   
LabelVideoRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.operation)>` | Promise  
  
### listAnnotatedDatasets(request, callback)
    
    
    public listAnnotatedDatasets(request: google.cloud.datalabeling.v1beta1.IListAnnotatedDatasetsRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.ListAnnotatedDatasetsCallback): void;

Calls ListAnnotatedDatasets.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnnotatedDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotateddatasetsrequest)`   
ListAnnotatedDatasetsRequest message or plain object  
`callback` |  `[ListAnnotatedDatasetsCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAnnotatedDatasetsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAnnotatedDatasets(request)
    
    
    public listAnnotatedDatasets(request: google.cloud.datalabeling.v1beta1.IListAnnotatedDatasetsRequest): Promise<google.cloud.datalabeling.v1beta1.ListAnnotatedDatasetsResponse>;

Calls ListAnnotatedDatasets.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAnnotatedDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotateddatasetsrequest)`   
ListAnnotatedDatasetsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datalabeling.v1beta1.ListAnnotatedDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.listannotateddatasetsresponse)>` | Promise  
  
### listAnnotationSpecSets(request, callback)
    
    
    public listAnnotationSpecSets(request: google.cloud.datalabeling.v1beta1.IListAnnotationSpecSetsRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.ListAnnotationSpecSetsCallback): void;

Calls ListAnnotationSpecSets.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnnotationSpecSetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotationspecsetsrequest)`   
ListAnnotationSpecSetsRequest message or plain object  
`callback` |  `[ListAnnotationSpecSetsCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAnnotationSpecSetsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAnnotationSpecSets(request)
    
    
    public listAnnotationSpecSets(request: google.cloud.datalabeling.v1beta1.IListAnnotationSpecSetsRequest): Promise<google.cloud.datalabeling.v1beta1.ListAnnotationSpecSetsResponse>;

Calls ListAnnotationSpecSets.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAnnotationSpecSetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotationspecsetsrequest)`   
ListAnnotationSpecSetsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datalabeling.v1beta1.ListAnnotationSpecSetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.listannotationspecsetsresponse)>` | Promise  
  
### listDataItems(request, callback)
    
    
    public listDataItems(request: google.cloud.datalabeling.v1beta1.IListDataItemsRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.ListDataItemsCallback): void;

Calls ListDataItems.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdataitemsrequest)`   
ListDataItemsRequest message or plain object  
`callback` |  `[ListDataItemsCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDataItemsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataItems(request)
    
    
    public listDataItems(request: google.cloud.datalabeling.v1beta1.IListDataItemsRequest): Promise<google.cloud.datalabeling.v1beta1.ListDataItemsResponse>;

Calls ListDataItems.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdataitemsrequest)`   
ListDataItemsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datalabeling.v1beta1.ListDataItemsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.listdataitemsresponse)>` | Promise  
  
### listDatasets(request, callback)
    
    
    public listDatasets(request: google.cloud.datalabeling.v1beta1.IListDatasetsRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.ListDatasetsCallback): void;

Calls ListDatasets.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdatasetsrequest)`   
ListDatasetsRequest message or plain object  
`callback` |  `[ListDatasetsCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDatasetsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDatasets(request)
    
    
    public listDatasets(request: google.cloud.datalabeling.v1beta1.IListDatasetsRequest): Promise<google.cloud.datalabeling.v1beta1.ListDatasetsResponse>;

Calls ListDatasets.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdatasetsrequest)`   
ListDatasetsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datalabeling.v1beta1.ListDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.listdatasetsresponse)>` | Promise  
  
### listEvaluationJobs(request, callback)
    
    
    public listEvaluationJobs(request: google.cloud.datalabeling.v1beta1.IListEvaluationJobsRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.ListEvaluationJobsCallback): void;

Calls ListEvaluationJobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistevaluationjobsrequest)`   
ListEvaluationJobsRequest message or plain object  
`callback` |  `[ListEvaluationJobsCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and ListEvaluationJobsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEvaluationJobs(request)
    
    
    public listEvaluationJobs(request: google.cloud.datalabeling.v1beta1.IListEvaluationJobsRequest): Promise<google.cloud.datalabeling.v1beta1.ListEvaluationJobsResponse>;

Calls ListEvaluationJobs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistevaluationjobsrequest)`   
ListEvaluationJobsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datalabeling.v1beta1.ListEvaluationJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.listevaluationjobsresponse)>` | Promise  
  
### listExamples(request, callback)
    
    
    public listExamples(request: google.cloud.datalabeling.v1beta1.IListExamplesRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.ListExamplesCallback): void;

Calls ListExamples.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListExamplesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistexamplesrequest)`   
ListExamplesRequest message or plain object  
`callback` |  `[ListExamplesCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and ListExamplesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listExamples(request)
    
    
    public listExamples(request: google.cloud.datalabeling.v1beta1.IListExamplesRequest): Promise<google.cloud.datalabeling.v1beta1.ListExamplesResponse>;

Calls ListExamples.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListExamplesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistexamplesrequest)`   
ListExamplesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datalabeling.v1beta1.ListExamplesResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.listexamplesresponse)>` | Promise  
  
### listInstructions(request, callback)
    
    
    public listInstructions(request: google.cloud.datalabeling.v1beta1.IListInstructionsRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.ListInstructionsCallback): void;

Calls ListInstructions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInstructionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistinstructionsrequest)`   
ListInstructionsRequest message or plain object  
`callback` |  `[ListInstructionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and ListInstructionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listInstructions(request)
    
    
    public listInstructions(request: google.cloud.datalabeling.v1beta1.IListInstructionsRequest): Promise<google.cloud.datalabeling.v1beta1.ListInstructionsResponse>;

Calls ListInstructions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListInstructionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistinstructionsrequest)`   
ListInstructionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datalabeling.v1beta1.ListInstructionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.listinstructionsresponse)>` | Promise  
  
### pauseEvaluationJob(request, callback)
    
    
    public pauseEvaluationJob(request: google.cloud.datalabeling.v1beta1.IPauseEvaluationJobRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.PauseEvaluationJobCallback): void;

Calls PauseEvaluationJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPauseEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ipauseevaluationjobrequest)`   
PauseEvaluationJobRequest message or plain object  
`callback` |  `[PauseEvaluationJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### pauseEvaluationJob(request)
    
    
    public pauseEvaluationJob(request: google.cloud.datalabeling.v1beta1.IPauseEvaluationJobRequest): Promise<google.protobuf.Empty>;

Calls PauseEvaluationJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPauseEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ipauseevaluationjobrequest)`   
PauseEvaluationJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.empty)>` | Promise  
  
### resumeEvaluationJob(request, callback)
    
    
    public resumeEvaluationJob(request: google.cloud.datalabeling.v1beta1.IResumeEvaluationJobRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.ResumeEvaluationJobCallback): void;

Calls ResumeEvaluationJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResumeEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iresumeevaluationjobrequest)`   
ResumeEvaluationJobRequest message or plain object  
`callback` |  `[ResumeEvaluationJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### resumeEvaluationJob(request)
    
    
    public resumeEvaluationJob(request: google.cloud.datalabeling.v1beta1.IResumeEvaluationJobRequest): Promise<google.protobuf.Empty>;

Calls ResumeEvaluationJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IResumeEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iresumeevaluationjobrequest)`   
ResumeEvaluationJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.empty)>` | Promise  
  
### searchEvaluations(request, callback)
    
    
    public searchEvaluations(request: google.cloud.datalabeling.v1beta1.ISearchEvaluationsRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.SearchEvaluationsCallback): void;

Calls SearchEvaluations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchevaluationsrequest)`   
SearchEvaluationsRequest message or plain object  
`callback` |  `[SearchEvaluationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchEvaluationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchEvaluations(request)
    
    
    public searchEvaluations(request: google.cloud.datalabeling.v1beta1.ISearchEvaluationsRequest): Promise<google.cloud.datalabeling.v1beta1.SearchEvaluationsResponse>;

Calls SearchEvaluations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchevaluationsrequest)`   
SearchEvaluationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datalabeling.v1beta1.SearchEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.searchevaluationsresponse)>` | Promise  
  
### searchExampleComparisons(request, callback)
    
    
    public searchExampleComparisons(request: google.cloud.datalabeling.v1beta1.ISearchExampleComparisonsRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.SearchExampleComparisonsCallback): void;

Calls SearchExampleComparisons.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchExampleComparisonsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchexamplecomparisonsrequest)`   
SearchExampleComparisonsRequest message or plain object  
`callback` |  `[SearchExampleComparisonsCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchExampleComparisonsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchExampleComparisons(request)
    
    
    public searchExampleComparisons(request: google.cloud.datalabeling.v1beta1.ISearchExampleComparisonsRequest): Promise<google.cloud.datalabeling.v1beta1.SearchExampleComparisonsResponse>;

Calls SearchExampleComparisons.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchExampleComparisonsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchexamplecomparisonsrequest)`   
SearchExampleComparisonsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datalabeling.v1beta1.SearchExampleComparisonsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.searchexamplecomparisonsresponse-class)>` | Promise  
  
### updateEvaluationJob(request, callback)
    
    
    public updateEvaluationJob(request: google.cloud.datalabeling.v1beta1.IUpdateEvaluationJobRequest, callback: google.cloud.datalabeling.v1beta1.DataLabelingService.UpdateEvaluationJobCallback): void;

Calls UpdateEvaluationJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iupdateevaluationjobrequest)`   
UpdateEvaluationJobRequest message or plain object  
`callback` |  `[UpdateEvaluationJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)`   
Node-style callback called with the error, if any, and EvaluationJob  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEvaluationJob(request)
    
    
    public updateEvaluationJob(request: google.cloud.datalabeling.v1beta1.IUpdateEvaluationJobRequest): Promise<google.cloud.datalabeling.v1beta1.EvaluationJob>;

Calls UpdateEvaluationJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iupdateevaluationjobrequest)`   
UpdateEvaluationJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datalabeling.v1beta1.EvaluationJob](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.evaluationjob-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
