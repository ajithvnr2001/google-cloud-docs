---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataproductservice-class
title: Class protos.google.cloud.dataplex.v1.DataProductService (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:07:29.408419+00:00
---

# Class protos.google.cloud.dataplex.v1.DataProductService (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataproductservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataplex.v1.DataProductService (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.4.0  5.3.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.5.1  3.2.0  3.1.0  2.4.0  2.3.2  2.2.2  2.1.1  1.2.0  1.1.0  1.0.0 

Represents a DataProductService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dataplex.v1.DataProductService

## Package

[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DataProductService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DataProductService;

Creates new DataProductService service using the specified rpc implementation.

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
`[DataProductService](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataproductservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createDataAsset(request, callback)
    
    
    public createDataAsset(request: google.cloud.dataplex.v1.ICreateDataAssetRequest, callback: google.cloud.dataplex.v1.DataProductService.CreateDataAssetCallback): void;

Calls CreateDataAsset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatedataassetrequest)`   
CreateDataAssetRequest message or plain object  
`callback` |  `[CreateDataAssetCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataAsset(request)
    
    
    public createDataAsset(request: google.cloud.dataplex.v1.ICreateDataAssetRequest): Promise<google.longrunning.Operation>;

Calls CreateDataAsset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatedataassetrequest)`   
CreateDataAssetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### createDataProduct(request, callback)
    
    
    public createDataProduct(request: google.cloud.dataplex.v1.ICreateDataProductRequest, callback: google.cloud.dataplex.v1.DataProductService.CreateDataProductCallback): void;

Calls CreateDataProduct.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatedataproductrequest)`   
CreateDataProductRequest message or plain object  
`callback` |  `[CreateDataProductCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataProduct(request)
    
    
    public createDataProduct(request: google.cloud.dataplex.v1.ICreateDataProductRequest): Promise<google.longrunning.Operation>;

Calls CreateDataProduct.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatedataproductrequest)`   
CreateDataProductRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### deleteDataAsset(request, callback)
    
    
    public deleteDataAsset(request: google.cloud.dataplex.v1.IDeleteDataAssetRequest, callback: google.cloud.dataplex.v1.DataProductService.DeleteDataAssetCallback): void;

Calls DeleteDataAsset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideletedataassetrequest)`   
DeleteDataAssetRequest message or plain object  
`callback` |  `[DeleteDataAssetCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataAsset(request)
    
    
    public deleteDataAsset(request: google.cloud.dataplex.v1.IDeleteDataAssetRequest): Promise<google.longrunning.Operation>;

Calls DeleteDataAsset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideletedataassetrequest)`   
DeleteDataAssetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### deleteDataProduct(request, callback)
    
    
    public deleteDataProduct(request: google.cloud.dataplex.v1.IDeleteDataProductRequest, callback: google.cloud.dataplex.v1.DataProductService.DeleteDataProductCallback): void;

Calls DeleteDataProduct.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideletedataproductrequest)`   
DeleteDataProductRequest message or plain object  
`callback` |  `[DeleteDataProductCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataProduct(request)
    
    
    public deleteDataProduct(request: google.cloud.dataplex.v1.IDeleteDataProductRequest): Promise<google.longrunning.Operation>;

Calls DeleteDataProduct.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideletedataproductrequest)`   
DeleteDataProductRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### getDataAsset(request, callback)
    
    
    public getDataAsset(request: google.cloud.dataplex.v1.IGetDataAssetRequest, callback: google.cloud.dataplex.v1.DataProductService.GetDataAssetCallback): void;

Calls GetDataAsset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetdataassetrequest)`   
GetDataAssetRequest message or plain object  
`callback` |  `[GetDataAssetCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and DataAsset  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataAsset(request)
    
    
    public getDataAsset(request: google.cloud.dataplex.v1.IGetDataAssetRequest): Promise<google.cloud.dataplex.v1.DataAsset>;

Calls GetDataAsset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetdataassetrequest)`   
GetDataAssetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.DataAsset](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataasset-class)>` | Promise  
  
### getDataProduct(request, callback)
    
    
    public getDataProduct(request: google.cloud.dataplex.v1.IGetDataProductRequest, callback: google.cloud.dataplex.v1.DataProductService.GetDataProductCallback): void;

Calls GetDataProduct.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetdataproductrequest)`   
GetDataProductRequest message or plain object  
`callback` |  `[GetDataProductCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and DataProduct  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataProduct(request)
    
    
    public getDataProduct(request: google.cloud.dataplex.v1.IGetDataProductRequest): Promise<google.cloud.dataplex.v1.DataProduct>;

Calls GetDataProduct.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetdataproductrequest)`   
GetDataProductRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.DataProduct](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataproduct-class)>` | Promise  
  
### listDataAssets(request, callback)
    
    
    public listDataAssets(request: google.cloud.dataplex.v1.IListDataAssetsRequest, callback: google.cloud.dataplex.v1.DataProductService.ListDataAssetsCallback): void;

Calls ListDataAssets.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataAssetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistdataassetsrequest)`   
ListDataAssetsRequest message or plain object  
`callback` |  `[ListDataAssetsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDataAssetsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataAssets(request)
    
    
    public listDataAssets(request: google.cloud.dataplex.v1.IListDataAssetsRequest): Promise<google.cloud.dataplex.v1.ListDataAssetsResponse>;

Calls ListDataAssets.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDataAssetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistdataassetsrequest)`   
ListDataAssetsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListDataAssetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listdataassetsresponse)>` | Promise  
  
### listDataProducts(request, callback)
    
    
    public listDataProducts(request: google.cloud.dataplex.v1.IListDataProductsRequest, callback: google.cloud.dataplex.v1.DataProductService.ListDataProductsCallback): void;

Calls ListDataProducts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistdataproductsrequest)`   
ListDataProductsRequest message or plain object  
`callback` |  `[ListDataProductsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDataProductsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataProducts(request)
    
    
    public listDataProducts(request: google.cloud.dataplex.v1.IListDataProductsRequest): Promise<google.cloud.dataplex.v1.ListDataProductsResponse>;

Calls ListDataProducts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDataProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistdataproductsrequest)`   
ListDataProductsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListDataProductsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listdataproductsresponse)>` | Promise  
  
### requestDataProductAccess(request, callback)
    
    
    public requestDataProductAccess(request: google.cloud.dataplex.v1.IRequestDataProductAccessRequest, callback: google.cloud.dataplex.v1.DataProductService.RequestDataProductAccessCallback): void;

Calls RequestDataProductAccess.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRequestDataProductAccessRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.irequestdataproductaccessrequest)`   
RequestDataProductAccessRequest message or plain object  
`callback` |  `[RequestDataProductAccessCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and RequestDataProductAccessResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### requestDataProductAccess(request)
    
    
    public requestDataProductAccess(request: google.cloud.dataplex.v1.IRequestDataProductAccessRequest): Promise<google.cloud.dataplex.v1.RequestDataProductAccessResponse>;

Calls RequestDataProductAccess.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRequestDataProductAccessRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.irequestdataproductaccessrequest)`   
RequestDataProductAccessRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.RequestDataProductAccessResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.requestdataproductaccessresponse)>` | Promise  
  
### updateDataAsset(request, callback)
    
    
    public updateDataAsset(request: google.cloud.dataplex.v1.IUpdateDataAssetRequest, callback: google.cloud.dataplex.v1.DataProductService.UpdateDataAssetCallback): void;

Calls UpdateDataAsset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdatedataassetrequest)`   
UpdateDataAssetRequest message or plain object  
`callback` |  `[UpdateDataAssetCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataAsset(request)
    
    
    public updateDataAsset(request: google.cloud.dataplex.v1.IUpdateDataAssetRequest): Promise<google.longrunning.Operation>;

Calls UpdateDataAsset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdatedataassetrequest)`   
UpdateDataAssetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### updateDataProduct(request, callback)
    
    
    public updateDataProduct(request: google.cloud.dataplex.v1.IUpdateDataProductRequest, callback: google.cloud.dataplex.v1.DataProductService.UpdateDataProductCallback): void;

Calls UpdateDataProduct.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdatedataproductrequest)`   
UpdateDataProductRequest message or plain object  
`callback` |  `[UpdateDataProductCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataProduct(request)
    
    
    public updateDataProduct(request: google.cloud.dataplex.v1.IUpdateDataProductRequest): Promise<google.longrunning.Operation>;

Calls UpdateDataProduct.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdatedataproductrequest)`   
UpdateDataProductRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
