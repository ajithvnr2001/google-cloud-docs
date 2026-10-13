---
url: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.datasetservice-class
title: Class protos.google.cloud.aiplatform.v1beta1.DatasetService (7.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:44:21.986514+00:00
---

# Class protos.google.cloud.aiplatform.v1beta1.DatasetService (7.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.datasetservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.aiplatform.v1beta1.DatasetService (7.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.4.1 (latest)  7.3.0  6.10.0  6.9.0  6.8.1  6.6.0  6.4.0  6.3.0  6.2.0  6.1.0  6.0.0  5.14.0  5.13.0  3.15.0  3.13.0  3.11.0  3.10.1  3.9.0  3.7.0  3.6.0  3.4.0  3.3.0  3.0.0  2.12.0  2.11.0  2.10.0  2.7.0  2.6.1  2.5.0  2.3.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0  1.11.0  1.7.2 

Represents a DatasetService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.aiplatform.v1beta1.DatasetService

## Package

[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DatasetService service.

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

### assembleData(request, callback)
    
    
    public assembleData(request: google.cloud.aiplatform.v1beta1.IAssembleDataRequest, callback: google.cloud.aiplatform.v1beta1.DatasetService.AssembleDataCallback): void;

Calls AssembleData.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAssembleDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassembledatarequest)`   
AssembleDataRequest message or plain object  
`callback` |  `[AssembleDataCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### assembleData(request)
    
    
    public assembleData(request: google.cloud.aiplatform.v1beta1.IAssembleDataRequest): Promise<google.longrunning.Operation>;

Calls AssembleData.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAssembleDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassembledatarequest)`   
AssembleDataRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### assessData(request, callback)
    
    
    public assessData(request: google.cloud.aiplatform.v1beta1.IAssessDataRequest, callback: google.cloud.aiplatform.v1beta1.DatasetService.AssessDataCallback): void;

Calls AssessData.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAssessDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassessdatarequest)`   
AssessDataRequest message or plain object  
`callback` |  `[AssessDataCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### assessData(request)
    
    
    public assessData(request: google.cloud.aiplatform.v1beta1.IAssessDataRequest): Promise<google.longrunning.Operation>;

Calls AssessData.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAssessDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassessdatarequest)`   
AssessDataRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DatasetService;

Creates new DatasetService service using the specified rpc implementation.

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
`[DatasetService](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.datasetservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createDataset(request, callback)
    
    
    public createDataset(request: google.cloud.aiplatform.v1beta1.ICreateDatasetRequest, callback: google.cloud.aiplatform.v1beta1.DatasetService.CreateDatasetCallback): void;

Calls CreateDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatedatasetrequest)`   
CreateDatasetRequest message or plain object  
`callback` |  `[CreateDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataset(request)
    
    
    public createDataset(request: google.cloud.aiplatform.v1beta1.ICreateDatasetRequest): Promise<google.longrunning.Operation>;

Calls CreateDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatedatasetrequest)`   
CreateDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### createDatasetVersion(request, callback)
    
    
    public createDatasetVersion(request: google.cloud.aiplatform.v1beta1.ICreateDatasetVersionRequest, callback: google.cloud.aiplatform.v1beta1.DatasetService.CreateDatasetVersionCallback): void;

Calls CreateDatasetVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatedatasetversionrequest)`   
CreateDatasetVersionRequest message or plain object  
`callback` |  `[CreateDatasetVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDatasetVersion(request)
    
    
    public createDatasetVersion(request: google.cloud.aiplatform.v1beta1.ICreateDatasetVersionRequest): Promise<google.longrunning.Operation>;

Calls CreateDatasetVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatedatasetversionrequest)`   
CreateDatasetVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### deleteDataset(request, callback)
    
    
    public deleteDataset(request: google.cloud.aiplatform.v1beta1.IDeleteDatasetRequest, callback: google.cloud.aiplatform.v1beta1.DatasetService.DeleteDatasetCallback): void;

Calls DeleteDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletedatasetrequest)`   
DeleteDatasetRequest message or plain object  
`callback` |  `[DeleteDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataset(request)
    
    
    public deleteDataset(request: google.cloud.aiplatform.v1beta1.IDeleteDatasetRequest): Promise<google.longrunning.Operation>;

Calls DeleteDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletedatasetrequest)`   
DeleteDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### deleteDatasetVersion(request, callback)
    
    
    public deleteDatasetVersion(request: google.cloud.aiplatform.v1beta1.IDeleteDatasetVersionRequest, callback: google.cloud.aiplatform.v1beta1.DatasetService.DeleteDatasetVersionCallback): void;

Calls DeleteDatasetVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletedatasetversionrequest)`   
DeleteDatasetVersionRequest message or plain object  
`callback` |  `[DeleteDatasetVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDatasetVersion(request)
    
    
    public deleteDatasetVersion(request: google.cloud.aiplatform.v1beta1.IDeleteDatasetVersionRequest): Promise<google.longrunning.Operation>;

Calls DeleteDatasetVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletedatasetversionrequest)`   
DeleteDatasetVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### deleteSavedQuery(request, callback)
    
    
    public deleteSavedQuery(request: google.cloud.aiplatform.v1beta1.IDeleteSavedQueryRequest, callback: google.cloud.aiplatform.v1beta1.DatasetService.DeleteSavedQueryCallback): void;

Calls DeleteSavedQuery.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSavedQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletesavedqueryrequest)`   
DeleteSavedQueryRequest message or plain object  
`callback` |  `[DeleteSavedQueryCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSavedQuery(request)
    
    
    public deleteSavedQuery(request: google.cloud.aiplatform.v1beta1.IDeleteSavedQueryRequest): Promise<google.longrunning.Operation>;

Calls DeleteSavedQuery.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSavedQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletesavedqueryrequest)`   
DeleteSavedQueryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### exportData(request, callback)
    
    
    public exportData(request: google.cloud.aiplatform.v1beta1.IExportDataRequest, callback: google.cloud.aiplatform.v1beta1.DatasetService.ExportDataCallback): void;

Calls ExportData.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexportdatarequest)`   
ExportDataRequest message or plain object  
`callback` |  `[ExportDataCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportData(request)
    
    
    public exportData(request: google.cloud.aiplatform.v1beta1.IExportDataRequest): Promise<google.longrunning.Operation>;

Calls ExportData.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexportdatarequest)`   
ExportDataRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### getAnnotationSpec(request, callback)
    
    
    public getAnnotationSpec(request: google.cloud.aiplatform.v1beta1.IGetAnnotationSpecRequest, callback: google.cloud.aiplatform.v1beta1.DatasetService.GetAnnotationSpecCallback): void;

Calls GetAnnotationSpec.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotationSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetannotationspecrequest)`   
GetAnnotationSpecRequest message or plain object  
`callback` |  `[GetAnnotationSpecCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and AnnotationSpec  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAnnotationSpec(request)
    
    
    public getAnnotationSpec(request: google.cloud.aiplatform.v1beta1.IGetAnnotationSpecRequest): Promise<google.cloud.aiplatform.v1beta1.AnnotationSpec>;

Calls GetAnnotationSpec.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotationSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetannotationspecrequest)`   
GetAnnotationSpecRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.AnnotationSpec](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.annotationspec)>` | Promise  
  
### getDataset(request, callback)
    
    
    public getDataset(request: google.cloud.aiplatform.v1beta1.IGetDatasetRequest, callback: google.cloud.aiplatform.v1beta1.DatasetService.GetDatasetCallback): void;

Calls GetDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetdatasetrequest)`   
GetDatasetRequest message or plain object  
`callback` |  `[GetDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Dataset  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataset(request)
    
    
    public getDataset(request: google.cloud.aiplatform.v1beta1.IGetDatasetRequest): Promise<google.cloud.aiplatform.v1beta1.Dataset>;

Calls GetDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetdatasetrequest)`   
GetDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.Dataset](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.dataset)>` | Promise  
  
### getDatasetVersion(request, callback)
    
    
    public getDatasetVersion(request: google.cloud.aiplatform.v1beta1.IGetDatasetVersionRequest, callback: google.cloud.aiplatform.v1beta1.DatasetService.GetDatasetVersionCallback): void;

Calls GetDatasetVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetdatasetversionrequest)`   
GetDatasetVersionRequest message or plain object  
`callback` |  `[GetDatasetVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and DatasetVersion  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDatasetVersion(request)
    
    
    public getDatasetVersion(request: google.cloud.aiplatform.v1beta1.IGetDatasetVersionRequest): Promise<google.cloud.aiplatform.v1beta1.DatasetVersion>;

Calls GetDatasetVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetdatasetversionrequest)`   
GetDatasetVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.DatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.datasetversion)>` | Promise  
  
### importData(request, callback)
    
    
    public importData(request: google.cloud.aiplatform.v1beta1.IImportDataRequest, callback: google.cloud.aiplatform.v1beta1.DatasetService.ImportDataCallback): void;

Calls ImportData.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iimportdatarequest)`   
ImportDataRequest message or plain object  
`callback` |  `[ImportDataCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importData(request)
    
    
    public importData(request: google.cloud.aiplatform.v1beta1.IImportDataRequest): Promise<google.longrunning.Operation>;

Calls ImportData.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iimportdatarequest)`   
ImportDataRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### listAnnotations(request, callback)
    
    
    public listAnnotations(request: google.cloud.aiplatform.v1beta1.IListAnnotationsRequest, callback: google.cloud.aiplatform.v1beta1.DatasetService.ListAnnotationsCallback): void;

Calls ListAnnotations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnnotationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistannotationsrequest)`   
ListAnnotationsRequest message or plain object  
`callback` |  `[ListAnnotationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAnnotationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAnnotations(request)
    
    
    public listAnnotations(request: google.cloud.aiplatform.v1beta1.IListAnnotationsRequest): Promise<google.cloud.aiplatform.v1beta1.ListAnnotationsResponse>;

Calls ListAnnotations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAnnotationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistannotationsrequest)`   
ListAnnotationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.ListAnnotationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.listannotationsresponse)>` | Promise  
  
### listDataItems(request, callback)
    
    
    public listDataItems(request: google.cloud.aiplatform.v1beta1.IListDataItemsRequest, callback: google.cloud.aiplatform.v1beta1.DatasetService.ListDataItemsCallback): void;

Calls ListDataItems.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdataitemsrequest)`   
ListDataItemsRequest message or plain object  
`callback` |  `[ListDataItemsCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDataItemsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataItems(request)
    
    
    public listDataItems(request: google.cloud.aiplatform.v1beta1.IListDataItemsRequest): Promise<google.cloud.aiplatform.v1beta1.ListDataItemsResponse>;

Calls ListDataItems.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdataitemsrequest)`   
ListDataItemsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.ListDataItemsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.listdataitemsresponse)>` | Promise  
  
### listDatasets(request, callback)
    
    
    public listDatasets(request: google.cloud.aiplatform.v1beta1.IListDatasetsRequest, callback: google.cloud.aiplatform.v1beta1.DatasetService.ListDatasetsCallback): void;

Calls ListDatasets.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetsrequest)`   
ListDatasetsRequest message or plain object  
`callback` |  `[ListDatasetsCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDatasetsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDatasets(request)
    
    
    public listDatasets(request: google.cloud.aiplatform.v1beta1.IListDatasetsRequest): Promise<google.cloud.aiplatform.v1beta1.ListDatasetsResponse>;

Calls ListDatasets.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetsrequest)`   
ListDatasetsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.ListDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.listdatasetsresponse)>` | Promise  
  
### listDatasetVersions(request, callback)
    
    
    public listDatasetVersions(request: google.cloud.aiplatform.v1beta1.IListDatasetVersionsRequest, callback: google.cloud.aiplatform.v1beta1.DatasetService.ListDatasetVersionsCallback): void;

Calls ListDatasetVersions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetversionsrequest)`   
ListDatasetVersionsRequest message or plain object  
`callback` |  `[ListDatasetVersionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDatasetVersionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDatasetVersions(request)
    
    
    public listDatasetVersions(request: google.cloud.aiplatform.v1beta1.IListDatasetVersionsRequest): Promise<google.cloud.aiplatform.v1beta1.ListDatasetVersionsResponse>;

Calls ListDatasetVersions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetversionsrequest)`   
ListDatasetVersionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.ListDatasetVersionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.listdatasetversionsresponse)>` | Promise  
  
### listSavedQueries(request, callback)
    
    
    public listSavedQueries(request: google.cloud.aiplatform.v1beta1.IListSavedQueriesRequest, callback: google.cloud.aiplatform.v1beta1.DatasetService.ListSavedQueriesCallback): void;

Calls ListSavedQueries.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSavedQueriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistsavedqueriesrequest)`   
ListSavedQueriesRequest message or plain object  
`callback` |  `[ListSavedQueriesCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSavedQueriesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSavedQueries(request)
    
    
    public listSavedQueries(request: google.cloud.aiplatform.v1beta1.IListSavedQueriesRequest): Promise<google.cloud.aiplatform.v1beta1.ListSavedQueriesResponse>;

Calls ListSavedQueries.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSavedQueriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistsavedqueriesrequest)`   
ListSavedQueriesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.ListSavedQueriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.listsavedqueriesresponse)>` | Promise  
  
### restoreDatasetVersion(request, callback)
    
    
    public restoreDatasetVersion(request: google.cloud.aiplatform.v1beta1.IRestoreDatasetVersionRequest, callback: google.cloud.aiplatform.v1beta1.DatasetService.RestoreDatasetVersionCallback): void;

Calls RestoreDatasetVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRestoreDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.irestoredatasetversionrequest)`   
RestoreDatasetVersionRequest message or plain object  
`callback` |  `[RestoreDatasetVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### restoreDatasetVersion(request)
    
    
    public restoreDatasetVersion(request: google.cloud.aiplatform.v1beta1.IRestoreDatasetVersionRequest): Promise<google.longrunning.Operation>;

Calls RestoreDatasetVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRestoreDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.irestoredatasetversionrequest)`   
RestoreDatasetVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### searchDataItems(request, callback)
    
    
    public searchDataItems(request: google.cloud.aiplatform.v1beta1.ISearchDataItemsRequest, callback: google.cloud.aiplatform.v1beta1.DatasetService.SearchDataItemsCallback): void;

Calls SearchDataItems.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isearchdataitemsrequest)`   
SearchDataItemsRequest message or plain object  
`callback` |  `[SearchDataItemsCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchDataItemsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchDataItems(request)
    
    
    public searchDataItems(request: google.cloud.aiplatform.v1beta1.ISearchDataItemsRequest): Promise<google.cloud.aiplatform.v1beta1.SearchDataItemsResponse>;

Calls SearchDataItems.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isearchdataitemsrequest)`   
SearchDataItemsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.SearchDataItemsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.searchdataitemsresponse)>` | Promise  
  
### updateDataset(request, callback)
    
    
    public updateDataset(request: google.cloud.aiplatform.v1beta1.IUpdateDatasetRequest, callback: google.cloud.aiplatform.v1beta1.DatasetService.UpdateDatasetCallback): void;

Calls UpdateDataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatedatasetrequest)`   
UpdateDatasetRequest message or plain object  
`callback` |  `[UpdateDatasetCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Dataset  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataset(request)
    
    
    public updateDataset(request: google.cloud.aiplatform.v1beta1.IUpdateDatasetRequest): Promise<google.cloud.aiplatform.v1beta1.Dataset>;

Calls UpdateDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatedatasetrequest)`   
UpdateDatasetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.Dataset](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.dataset)>` | Promise  
  
### updateDatasetVersion(request, callback)
    
    
    public updateDatasetVersion(request: google.cloud.aiplatform.v1beta1.IUpdateDatasetVersionRequest, callback: google.cloud.aiplatform.v1beta1.DatasetService.UpdateDatasetVersionCallback): void;

Calls UpdateDatasetVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatedatasetversionrequest)`   
UpdateDatasetVersionRequest message or plain object  
`callback` |  `[UpdateDatasetVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and DatasetVersion  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDatasetVersion(request)
    
    
    public updateDatasetVersion(request: google.cloud.aiplatform.v1beta1.IUpdateDatasetVersionRequest): Promise<google.cloud.aiplatform.v1beta1.DatasetVersion>;

Calls UpdateDatasetVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatedatasetversionrequest)`   
UpdateDatasetVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.DatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.datasetversion)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
