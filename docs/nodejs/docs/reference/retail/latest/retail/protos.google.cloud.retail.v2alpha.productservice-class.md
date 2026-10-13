---
url: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.productservice-class
title: Class protos.google.cloud.retail.v2alpha.ProductService (5.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:04:58.282123+00:00
---

# Class protos.google.cloud.retail.v2alpha.ProductService (5.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.productservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.retail.v2alpha.ProductService (5.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.4.0 (latest)  5.3.1  5.0.1  4.4.0  4.3.0  3.6.0  3.5.0  3.1.0  2.4.1  2.3.1  2.1.1  2.0.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.2  1.1.6 

Represents a ProductService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.retail.v2alpha.ProductService

## Package

[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ProductService service.

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

### addFulfillmentPlaces(request, callback)
    
    
    public addFulfillmentPlaces(request: google.cloud.retail.v2alpha.IAddFulfillmentPlacesRequest, callback: google.cloud.retail.v2alpha.ProductService.AddFulfillmentPlacesCallback): void;

Calls AddFulfillmentPlaces.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddFulfillmentPlacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddfulfillmentplacesrequest)`   
AddFulfillmentPlacesRequest message or plain object  
`callback` |  `[AddFulfillmentPlacesCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addFulfillmentPlaces(request)
    
    
    public addFulfillmentPlaces(request: google.cloud.retail.v2alpha.IAddFulfillmentPlacesRequest): Promise<google.longrunning.Operation>;

Calls AddFulfillmentPlaces.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAddFulfillmentPlacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddfulfillmentplacesrequest)`   
AddFulfillmentPlacesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)>` | Promise  
  
### addLocalInventories(request, callback)
    
    
    public addLocalInventories(request: google.cloud.retail.v2alpha.IAddLocalInventoriesRequest, callback: google.cloud.retail.v2alpha.ProductService.AddLocalInventoriesCallback): void;

Calls AddLocalInventories.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddLocalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddlocalinventoriesrequest)`   
AddLocalInventoriesRequest message or plain object  
`callback` |  `[AddLocalInventoriesCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addLocalInventories(request)
    
    
    public addLocalInventories(request: google.cloud.retail.v2alpha.IAddLocalInventoriesRequest): Promise<google.longrunning.Operation>;

Calls AddLocalInventories.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAddLocalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddlocalinventoriesrequest)`   
AddLocalInventoriesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ProductService;

Creates new ProductService service using the specified rpc implementation.

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
`[ProductService](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.productservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createProduct(request, callback)
    
    
    public createProduct(request: google.cloud.retail.v2alpha.ICreateProductRequest, callback: google.cloud.retail.v2alpha.ProductService.CreateProductCallback): void;

Calls CreateProduct.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icreateproductrequest)`   
CreateProductRequest message or plain object  
`callback` |  `[CreateProductCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Product  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createProduct(request)
    
    
    public createProduct(request: google.cloud.retail.v2alpha.ICreateProductRequest): Promise<google.cloud.retail.v2alpha.Product>;

Calls CreateProduct.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icreateproductrequest)`   
CreateProductRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.retail.v2alpha.Product](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.product-class)>` | Promise  
  
### deleteProduct(request, callback)
    
    
    public deleteProduct(request: google.cloud.retail.v2alpha.IDeleteProductRequest, callback: google.cloud.retail.v2alpha.ProductService.DeleteProductCallback): void;

Calls DeleteProduct.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ideleteproductrequest)`   
DeleteProductRequest message or plain object  
`callback` |  `[DeleteProductCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteProduct(request)
    
    
    public deleteProduct(request: google.cloud.retail.v2alpha.IDeleteProductRequest): Promise<google.protobuf.Empty>;

Calls DeleteProduct.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ideleteproductrequest)`   
DeleteProductRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.empty)>` | Promise  
  
### exportProducts(request, callback)
    
    
    public exportProducts(request: google.cloud.retail.v2alpha.IExportProductsRequest, callback: google.cloud.retail.v2alpha.ProductService.ExportProductsCallback): void;

Calls ExportProducts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iexportproductsrequest)`   
ExportProductsRequest message or plain object  
`callback` |  `[ExportProductsCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportProducts(request)
    
    
    public exportProducts(request: google.cloud.retail.v2alpha.IExportProductsRequest): Promise<google.longrunning.Operation>;

Calls ExportProducts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iexportproductsrequest)`   
ExportProductsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)>` | Promise  
  
### getProduct(request, callback)
    
    
    public getProduct(request: google.cloud.retail.v2alpha.IGetProductRequest, callback: google.cloud.retail.v2alpha.ProductService.GetProductCallback): void;

Calls GetProduct.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.igetproductrequest)`   
GetProductRequest message or plain object  
`callback` |  `[GetProductCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Product  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProduct(request)
    
    
    public getProduct(request: google.cloud.retail.v2alpha.IGetProductRequest): Promise<google.cloud.retail.v2alpha.Product>;

Calls GetProduct.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.igetproductrequest)`   
GetProductRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.retail.v2alpha.Product](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.product-class)>` | Promise  
  
### importProducts(request, callback)
    
    
    public importProducts(request: google.cloud.retail.v2alpha.IImportProductsRequest, callback: google.cloud.retail.v2alpha.ProductService.ImportProductsCallback): void;

Calls ImportProducts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iimportproductsrequest)`   
ImportProductsRequest message or plain object  
`callback` |  `[ImportProductsCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importProducts(request)
    
    
    public importProducts(request: google.cloud.retail.v2alpha.IImportProductsRequest): Promise<google.longrunning.Operation>;

Calls ImportProducts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iimportproductsrequest)`   
ImportProductsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)>` | Promise  
  
### listProducts(request, callback)
    
    
    public listProducts(request: google.cloud.retail.v2alpha.IListProductsRequest, callback: google.cloud.retail.v2alpha.ProductService.ListProductsCallback): void;

Calls ListProducts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistproductsrequest)`   
ListProductsRequest message or plain object  
`callback` |  `[ListProductsCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and ListProductsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProducts(request)
    
    
    public listProducts(request: google.cloud.retail.v2alpha.IListProductsRequest): Promise<google.cloud.retail.v2alpha.ListProductsResponse>;

Calls ListProducts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistproductsrequest)`   
ListProductsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.retail.v2alpha.ListProductsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.listproductsresponse)>` | Promise  
  
### purgeProducts(request, callback)
    
    
    public purgeProducts(request: google.cloud.retail.v2alpha.IPurgeProductsRequest, callback: google.cloud.retail.v2alpha.ProductService.PurgeProductsCallback): void;

Calls PurgeProducts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPurgeProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ipurgeproductsrequest)`   
PurgeProductsRequest message or plain object  
`callback` |  `[PurgeProductsCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### purgeProducts(request)
    
    
    public purgeProducts(request: google.cloud.retail.v2alpha.IPurgeProductsRequest): Promise<google.longrunning.Operation>;

Calls PurgeProducts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPurgeProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ipurgeproductsrequest)`   
PurgeProductsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)>` | Promise  
  
### removeFulfillmentPlaces(request, callback)
    
    
    public removeFulfillmentPlaces(request: google.cloud.retail.v2alpha.IRemoveFulfillmentPlacesRequest, callback: google.cloud.retail.v2alpha.ProductService.RemoveFulfillmentPlacesCallback): void;

Calls RemoveFulfillmentPlaces.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveFulfillmentPlacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovefulfillmentplacesrequest)`   
RemoveFulfillmentPlacesRequest message or plain object  
`callback` |  `[RemoveFulfillmentPlacesCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeFulfillmentPlaces(request)
    
    
    public removeFulfillmentPlaces(request: google.cloud.retail.v2alpha.IRemoveFulfillmentPlacesRequest): Promise<google.longrunning.Operation>;

Calls RemoveFulfillmentPlaces.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRemoveFulfillmentPlacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovefulfillmentplacesrequest)`   
RemoveFulfillmentPlacesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)>` | Promise  
  
### removeLocalInventories(request, callback)
    
    
    public removeLocalInventories(request: google.cloud.retail.v2alpha.IRemoveLocalInventoriesRequest, callback: google.cloud.retail.v2alpha.ProductService.RemoveLocalInventoriesCallback): void;

Calls RemoveLocalInventories.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveLocalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovelocalinventoriesrequest)`   
RemoveLocalInventoriesRequest message or plain object  
`callback` |  `[RemoveLocalInventoriesCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeLocalInventories(request)
    
    
    public removeLocalInventories(request: google.cloud.retail.v2alpha.IRemoveLocalInventoriesRequest): Promise<google.longrunning.Operation>;

Calls RemoveLocalInventories.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRemoveLocalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovelocalinventoriesrequest)`   
RemoveLocalInventoriesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)>` | Promise  
  
### setInventory(request, callback)
    
    
    public setInventory(request: google.cloud.retail.v2alpha.ISetInventoryRequest, callback: google.cloud.retail.v2alpha.ProductService.SetInventoryCallback): void;

Calls SetInventory.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.isetinventoryrequest)`   
SetInventoryRequest message or plain object  
`callback` |  `[SetInventoryCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setInventory(request)
    
    
    public setInventory(request: google.cloud.retail.v2alpha.ISetInventoryRequest): Promise<google.longrunning.Operation>;

Calls SetInventory.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.isetinventoryrequest)`   
SetInventoryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)>` | Promise  
  
### updateProduct(request, callback)
    
    
    public updateProduct(request: google.cloud.retail.v2alpha.IUpdateProductRequest, callback: google.cloud.retail.v2alpha.ProductService.UpdateProductCallback): void;

Calls UpdateProduct.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iupdateproductrequest)`   
UpdateProductRequest message or plain object  
`callback` |  `[UpdateProductCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Product  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateProduct(request)
    
    
    public updateProduct(request: google.cloud.retail.v2alpha.IUpdateProductRequest): Promise<google.cloud.retail.v2alpha.Product>;

Calls UpdateProduct.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iupdateproductrequest)`   
UpdateProductRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.retail.v2alpha.Product](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.product-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
