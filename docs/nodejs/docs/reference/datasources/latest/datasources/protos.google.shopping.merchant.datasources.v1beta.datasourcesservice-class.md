---
url: https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.datasourcesservice-class
title: Class protos.google.shopping.merchant.datasources.v1beta.DataSourcesService (0.12.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:13:20.130762+00:00
---

# Class protos.google.shopping.merchant.datasources.v1beta.DataSourcesService (0.12.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.datasourcesservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.datasources.v1beta.DataSourcesService (0.12.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.1 (latest)  0.11.0  0.3.0  0.2.0  0.1.0 

Represents a DataSourcesService

## Inheritance

$protobuf.rpc.Service > protos.google.shopping.merchant.datasources.v1beta.DataSourcesService

## Package

[@google-shopping/datasources](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DataSourcesService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DataSourcesService;

Creates new DataSourcesService service using the specified rpc implementation.

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
`[DataSourcesService](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.datasourcesservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createDataSource(request, callback)
    
    
    public createDataSource(request: google.shopping.merchant.datasources.v1beta.ICreateDataSourceRequest, callback: google.shopping.merchant.datasources.v1beta.DataSourcesService.CreateDataSourceCallback): void;

Calls CreateDataSource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.icreatedatasourcerequest)`   
CreateDataSourceRequest message or plain object  
`callback` |  `[CreateDataSourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/overview.html)`   
Node-style callback called with the error, if any, and DataSource  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataSource(request)
    
    
    public createDataSource(request: google.shopping.merchant.datasources.v1beta.ICreateDataSourceRequest): Promise<google.shopping.merchant.datasources.v1beta.DataSource>;

Calls CreateDataSource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.icreatedatasourcerequest)`   
CreateDataSourceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.datasources.v1beta.DataSource](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.datasource-class)>` | Promise  
  
### deleteDataSource(request, callback)
    
    
    public deleteDataSource(request: google.shopping.merchant.datasources.v1beta.IDeleteDataSourceRequest, callback: google.shopping.merchant.datasources.v1beta.DataSourcesService.DeleteDataSourceCallback): void;

Calls DeleteDataSource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.ideletedatasourcerequest)`   
DeleteDataSourceRequest message or plain object  
`callback` |  `[DeleteDataSourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataSource(request)
    
    
    public deleteDataSource(request: google.shopping.merchant.datasources.v1beta.IDeleteDataSourceRequest): Promise<google.protobuf.Empty>;

Calls DeleteDataSource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.ideletedatasourcerequest)`   
DeleteDataSourceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.protobuf.empty)>` | Promise  
  
### fetchDataSource(request, callback)
    
    
    public fetchDataSource(request: google.shopping.merchant.datasources.v1beta.IFetchDataSourceRequest, callback: google.shopping.merchant.datasources.v1beta.DataSourcesService.FetchDataSourceCallback): void;

Calls FetchDataSource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchDataSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.ifetchdatasourcerequest)`   
FetchDataSourceRequest message or plain object  
`callback` |  `[FetchDataSourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchDataSource(request)
    
    
    public fetchDataSource(request: google.shopping.merchant.datasources.v1beta.IFetchDataSourceRequest): Promise<google.protobuf.Empty>;

Calls FetchDataSource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFetchDataSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.ifetchdatasourcerequest)`   
FetchDataSourceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.protobuf.empty)>` | Promise  
  
### getDataSource(request, callback)
    
    
    public getDataSource(request: google.shopping.merchant.datasources.v1beta.IGetDataSourceRequest, callback: google.shopping.merchant.datasources.v1beta.DataSourcesService.GetDataSourceCallback): void;

Calls GetDataSource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.igetdatasourcerequest)`   
GetDataSourceRequest message or plain object  
`callback` |  `[GetDataSourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/overview.html)`   
Node-style callback called with the error, if any, and DataSource  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataSource(request)
    
    
    public getDataSource(request: google.shopping.merchant.datasources.v1beta.IGetDataSourceRequest): Promise<google.shopping.merchant.datasources.v1beta.DataSource>;

Calls GetDataSource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.igetdatasourcerequest)`   
GetDataSourceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.datasources.v1beta.DataSource](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.datasource-class)>` | Promise  
  
### listDataSources(request, callback)
    
    
    public listDataSources(request: google.shopping.merchant.datasources.v1beta.IListDataSourcesRequest, callback: google.shopping.merchant.datasources.v1beta.DataSourcesService.ListDataSourcesCallback): void;

Calls ListDataSources.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.ilistdatasourcesrequest)`   
ListDataSourcesRequest message or plain object  
`callback` |  `[ListDataSourcesCallback](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDataSourcesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataSources(request)
    
    
    public listDataSources(request: google.shopping.merchant.datasources.v1beta.IListDataSourcesRequest): Promise<google.shopping.merchant.datasources.v1beta.ListDataSourcesResponse>;

Calls ListDataSources.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDataSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.ilistdatasourcesrequest)`   
ListDataSourcesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.datasources.v1beta.ListDataSourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.listdatasourcesresponse)>` | Promise  
  
### updateDataSource(request, callback)
    
    
    public updateDataSource(request: google.shopping.merchant.datasources.v1beta.IUpdateDataSourceRequest, callback: google.shopping.merchant.datasources.v1beta.DataSourcesService.UpdateDataSourceCallback): void;

Calls UpdateDataSource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.iupdatedatasourcerequest)`   
UpdateDataSourceRequest message or plain object  
`callback` |  `[UpdateDataSourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/overview.html)`   
Node-style callback called with the error, if any, and DataSource  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataSource(request)
    
    
    public updateDataSource(request: google.shopping.merchant.datasources.v1beta.IUpdateDataSourceRequest): Promise<google.shopping.merchant.datasources.v1beta.DataSource>;

Calls UpdateDataSource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.iupdatedatasourcerequest)`   
UpdateDataSourceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.datasources.v1beta.DataSource](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.datasource-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
