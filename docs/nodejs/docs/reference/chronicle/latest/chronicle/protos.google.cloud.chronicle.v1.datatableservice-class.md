---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.datatableservice-class
title: Class protos.google.cloud.chronicle.v1.DataTableService (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:51:21.610968+00:00
---

# Class protos.google.cloud.chronicle.v1.DataTableService (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.datatableservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.chronicle.v1.DataTableService (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents a DataTableService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.chronicle.v1.DataTableService

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DataTableService service.

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

### bulkCreateDataTableRows(request, callback)
    
    
    public bulkCreateDataTableRows(request: google.cloud.chronicle.v1.IBulkCreateDataTableRowsRequest, callback: google.cloud.chronicle.v1.DataTableService.BulkCreateDataTableRowsCallback): void;

Calls BulkCreateDataTableRows.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBulkCreateDataTableRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ibulkcreatedatatablerowsrequest)`   
BulkCreateDataTableRowsRequest message or plain object  
`callback` |  `[BulkCreateDataTableRowsCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and BulkCreateDataTableRowsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### bulkCreateDataTableRows(request)
    
    
    public bulkCreateDataTableRows(request: google.cloud.chronicle.v1.IBulkCreateDataTableRowsRequest): Promise<google.cloud.chronicle.v1.BulkCreateDataTableRowsResponse>;

Calls BulkCreateDataTableRows.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBulkCreateDataTableRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ibulkcreatedatatablerowsrequest)`   
BulkCreateDataTableRowsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.BulkCreateDataTableRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.bulkcreatedatatablerowsresponse)>` | Promise  
  
### bulkGetDataTableRows(request, callback)
    
    
    public bulkGetDataTableRows(request: google.cloud.chronicle.v1.IBulkGetDataTableRowsRequest, callback: google.cloud.chronicle.v1.DataTableService.BulkGetDataTableRowsCallback): void;

Calls BulkGetDataTableRows.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBulkGetDataTableRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ibulkgetdatatablerowsrequest)`   
BulkGetDataTableRowsRequest message or plain object  
`callback` |  `[BulkGetDataTableRowsCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and BulkGetDataTableRowsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### bulkGetDataTableRows(request)
    
    
    public bulkGetDataTableRows(request: google.cloud.chronicle.v1.IBulkGetDataTableRowsRequest): Promise<google.cloud.chronicle.v1.BulkGetDataTableRowsResponse>;

Calls BulkGetDataTableRows.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBulkGetDataTableRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ibulkgetdatatablerowsrequest)`   
BulkGetDataTableRowsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.BulkGetDataTableRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.bulkgetdatatablerowsresponse)>` | Promise  
  
### bulkReplaceDataTableRows(request, callback)
    
    
    public bulkReplaceDataTableRows(request: google.cloud.chronicle.v1.IBulkReplaceDataTableRowsRequest, callback: google.cloud.chronicle.v1.DataTableService.BulkReplaceDataTableRowsCallback): void;

Calls BulkReplaceDataTableRows.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBulkReplaceDataTableRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ibulkreplacedatatablerowsrequest)`   
BulkReplaceDataTableRowsRequest message or plain object  
`callback` |  `[BulkReplaceDataTableRowsCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and BulkReplaceDataTableRowsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### bulkReplaceDataTableRows(request)
    
    
    public bulkReplaceDataTableRows(request: google.cloud.chronicle.v1.IBulkReplaceDataTableRowsRequest): Promise<google.cloud.chronicle.v1.BulkReplaceDataTableRowsResponse>;

Calls BulkReplaceDataTableRows.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBulkReplaceDataTableRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ibulkreplacedatatablerowsrequest)`   
BulkReplaceDataTableRowsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.BulkReplaceDataTableRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.bulkreplacedatatablerowsresponse)>` | Promise  
  
### bulkUpdateDataTableRows(request, callback)
    
    
    public bulkUpdateDataTableRows(request: google.cloud.chronicle.v1.IBulkUpdateDataTableRowsRequest, callback: google.cloud.chronicle.v1.DataTableService.BulkUpdateDataTableRowsCallback): void;

Calls BulkUpdateDataTableRows.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBulkUpdateDataTableRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ibulkupdatedatatablerowsrequest)`   
BulkUpdateDataTableRowsRequest message or plain object  
`callback` |  `[BulkUpdateDataTableRowsCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and BulkUpdateDataTableRowsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### bulkUpdateDataTableRows(request)
    
    
    public bulkUpdateDataTableRows(request: google.cloud.chronicle.v1.IBulkUpdateDataTableRowsRequest): Promise<google.cloud.chronicle.v1.BulkUpdateDataTableRowsResponse>;

Calls BulkUpdateDataTableRows.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBulkUpdateDataTableRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ibulkupdatedatatablerowsrequest)`   
BulkUpdateDataTableRowsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.BulkUpdateDataTableRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.bulkupdatedatatablerowsresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DataTableService;

Creates new DataTableService service using the specified rpc implementation.

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
`[DataTableService](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.datatableservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createDataTable(request, callback)
    
    
    public createDataTable(request: google.cloud.chronicle.v1.ICreateDataTableRequest, callback: google.cloud.chronicle.v1.DataTableService.CreateDataTableCallback): void;

Calls CreateDataTable.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataTableRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.icreatedatatablerequest)`   
CreateDataTableRequest message or plain object  
`callback` |  `[CreateDataTableCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and DataTable  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataTable(request)
    
    
    public createDataTable(request: google.cloud.chronicle.v1.ICreateDataTableRequest): Promise<google.cloud.chronicle.v1.DataTable>;

Calls CreateDataTable.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataTableRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.icreatedatatablerequest)`   
CreateDataTableRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.DataTable](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.datatable)>` | Promise  
  
### createDataTableRow(request, callback)
    
    
    public createDataTableRow(request: google.cloud.chronicle.v1.ICreateDataTableRowRequest, callback: google.cloud.chronicle.v1.DataTableService.CreateDataTableRowCallback): void;

Calls CreateDataTableRow.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataTableRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.icreatedatatablerowrequest)`   
CreateDataTableRowRequest message or plain object  
`callback` |  `[CreateDataTableRowCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and DataTableRow  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataTableRow(request)
    
    
    public createDataTableRow(request: google.cloud.chronicle.v1.ICreateDataTableRowRequest): Promise<google.cloud.chronicle.v1.DataTableRow>;

Calls CreateDataTableRow.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataTableRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.icreatedatatablerowrequest)`   
CreateDataTableRowRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.DataTableRow](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.datatablerow)>` | Promise  
  
### deleteDataTable(request, callback)
    
    
    public deleteDataTable(request: google.cloud.chronicle.v1.IDeleteDataTableRequest, callback: google.cloud.chronicle.v1.DataTableService.DeleteDataTableCallback): void;

Calls DeleteDataTable.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataTableRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ideletedatatablerequest)`   
DeleteDataTableRequest message or plain object  
`callback` |  `[DeleteDataTableCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataTable(request)
    
    
    public deleteDataTable(request: google.cloud.chronicle.v1.IDeleteDataTableRequest): Promise<google.protobuf.Empty>;

Calls DeleteDataTable.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataTableRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ideletedatatablerequest)`   
DeleteDataTableRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.protobuf.empty)>` | Promise  
  
### deleteDataTableRow(request, callback)
    
    
    public deleteDataTableRow(request: google.cloud.chronicle.v1.IDeleteDataTableRowRequest, callback: google.cloud.chronicle.v1.DataTableService.DeleteDataTableRowCallback): void;

Calls DeleteDataTableRow.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataTableRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ideletedatatablerowrequest)`   
DeleteDataTableRowRequest message or plain object  
`callback` |  `[DeleteDataTableRowCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataTableRow(request)
    
    
    public deleteDataTableRow(request: google.cloud.chronicle.v1.IDeleteDataTableRowRequest): Promise<google.protobuf.Empty>;

Calls DeleteDataTableRow.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataTableRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ideletedatatablerowrequest)`   
DeleteDataTableRowRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.protobuf.empty)>` | Promise  
  
### getDataTable(request, callback)
    
    
    public getDataTable(request: google.cloud.chronicle.v1.IGetDataTableRequest, callback: google.cloud.chronicle.v1.DataTableService.GetDataTableCallback): void;

Calls GetDataTable.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataTableRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetdatatablerequest)`   
GetDataTableRequest message or plain object  
`callback` |  `[GetDataTableCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and DataTable  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataTable(request)
    
    
    public getDataTable(request: google.cloud.chronicle.v1.IGetDataTableRequest): Promise<google.cloud.chronicle.v1.DataTable>;

Calls GetDataTable.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataTableRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetdatatablerequest)`   
GetDataTableRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.DataTable](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.datatable)>` | Promise  
  
### getDataTableOperationErrors(request, callback)
    
    
    public getDataTableOperationErrors(request: google.cloud.chronicle.v1.IGetDataTableOperationErrorsRequest, callback: google.cloud.chronicle.v1.DataTableService.GetDataTableOperationErrorsCallback): void;

Calls GetDataTableOperationErrors.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataTableOperationErrorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetdatatableoperationerrorsrequest)`   
GetDataTableOperationErrorsRequest message or plain object  
`callback` |  `[GetDataTableOperationErrorsCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and DataTableOperationErrors  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataTableOperationErrors(request)
    
    
    public getDataTableOperationErrors(request: google.cloud.chronicle.v1.IGetDataTableOperationErrorsRequest): Promise<google.cloud.chronicle.v1.DataTableOperationErrors>;

Calls GetDataTableOperationErrors.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataTableOperationErrorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetdatatableoperationerrorsrequest)`   
GetDataTableOperationErrorsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.DataTableOperationErrors](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.datatableoperationerrors)>` | Promise  
  
### getDataTableRow(request, callback)
    
    
    public getDataTableRow(request: google.cloud.chronicle.v1.IGetDataTableRowRequest, callback: google.cloud.chronicle.v1.DataTableService.GetDataTableRowCallback): void;

Calls GetDataTableRow.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataTableRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetdatatablerowrequest)`   
GetDataTableRowRequest message or plain object  
`callback` |  `[GetDataTableRowCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and DataTableRow  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataTableRow(request)
    
    
    public getDataTableRow(request: google.cloud.chronicle.v1.IGetDataTableRowRequest): Promise<google.cloud.chronicle.v1.DataTableRow>;

Calls GetDataTableRow.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataTableRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetdatatablerowrequest)`   
GetDataTableRowRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.DataTableRow](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.datatablerow)>` | Promise  
  
### listDataTableRows(request, callback)
    
    
    public listDataTableRows(request: google.cloud.chronicle.v1.IListDataTableRowsRequest, callback: google.cloud.chronicle.v1.DataTableService.ListDataTableRowsCallback): void;

Calls ListDataTableRows.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataTableRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistdatatablerowsrequest)`   
ListDataTableRowsRequest message or plain object  
`callback` |  `[ListDataTableRowsCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDataTableRowsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataTableRows(request)
    
    
    public listDataTableRows(request: google.cloud.chronicle.v1.IListDataTableRowsRequest): Promise<google.cloud.chronicle.v1.ListDataTableRowsResponse>;

Calls ListDataTableRows.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDataTableRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistdatatablerowsrequest)`   
ListDataTableRowsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.ListDataTableRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.listdatatablerowsresponse)>` | Promise  
  
### listDataTables(request, callback)
    
    
    public listDataTables(request: google.cloud.chronicle.v1.IListDataTablesRequest, callback: google.cloud.chronicle.v1.DataTableService.ListDataTablesCallback): void;

Calls ListDataTables.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataTablesRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistdatatablesrequest)`   
ListDataTablesRequest message or plain object  
`callback` |  `[ListDataTablesCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDataTablesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataTables(request)
    
    
    public listDataTables(request: google.cloud.chronicle.v1.IListDataTablesRequest): Promise<google.cloud.chronicle.v1.ListDataTablesResponse>;

Calls ListDataTables.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDataTablesRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistdatatablesrequest)`   
ListDataTablesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.ListDataTablesResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.listdatatablesresponse)>` | Promise  
  
### updateDataTable(request, callback)
    
    
    public updateDataTable(request: google.cloud.chronicle.v1.IUpdateDataTableRequest, callback: google.cloud.chronicle.v1.DataTableService.UpdateDataTableCallback): void;

Calls UpdateDataTable.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataTableRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iupdatedatatablerequest)`   
UpdateDataTableRequest message or plain object  
`callback` |  `[UpdateDataTableCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and DataTable  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataTable(request)
    
    
    public updateDataTable(request: google.cloud.chronicle.v1.IUpdateDataTableRequest): Promise<google.cloud.chronicle.v1.DataTable>;

Calls UpdateDataTable.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataTableRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iupdatedatatablerequest)`   
UpdateDataTableRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.DataTable](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.datatable)>` | Promise  
  
### updateDataTableRow(request, callback)
    
    
    public updateDataTableRow(request: google.cloud.chronicle.v1.IUpdateDataTableRowRequest, callback: google.cloud.chronicle.v1.DataTableService.UpdateDataTableRowCallback): void;

Calls UpdateDataTableRow.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataTableRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iupdatedatatablerowrequest)`   
UpdateDataTableRowRequest message or plain object  
`callback` |  `[UpdateDataTableRowCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and DataTableRow  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataTableRow(request)
    
    
    public updateDataTableRow(request: google.cloud.chronicle.v1.IUpdateDataTableRowRequest): Promise<google.cloud.chronicle.v1.DataTableRow>;

Calls UpdateDataTableRow.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataTableRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iupdatedatatablerowrequest)`   
UpdateDataTableRowRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.DataTableRow](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.datatablerow)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
