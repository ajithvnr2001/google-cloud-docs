---
url: https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.productsearch-class
title: Class protos.google.cloud.vision.v1p4beta1.ProductSearch (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:53:57.104258+00:00
---

# Class protos.google.cloud.vision.v1p4beta1.ProductSearch (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.productsearch-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.vision.v1p4beta1.ProductSearch (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.3.5  5.2.0  4.3.2  4.2.1  4.0.3  3.1.3  3.0.1  2.4.2  2.3.8 

Represents a ProductSearch

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.vision.v1p4beta1.ProductSearch

## Package

[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ProductSearch service.

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

### addProductToProductSet(request, callback)
    
    
    public addProductToProductSet(request: google.cloud.vision.v1p4beta1.IAddProductToProductSetRequest, callback: google.cloud.vision.v1p4beta1.ProductSearch.AddProductToProductSetCallback): void;

Calls AddProductToProductSet.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddProductToProductSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.iaddproducttoproductsetrequest)`   
AddProductToProductSetRequest message or plain object  
`callback` |  `[AddProductToProductSetCallback](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addProductToProductSet(request)
    
    
    public addProductToProductSet(request: google.cloud.vision.v1p4beta1.IAddProductToProductSetRequest): Promise<google.protobuf.Empty>;

Calls AddProductToProductSet.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAddProductToProductSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.iaddproducttoproductsetrequest)`   
AddProductToProductSetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.protobuf.empty)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ProductSearch;

Creates new ProductSearch service using the specified rpc implementation.

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
`[ProductSearch](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.productsearch-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createProduct(request, callback)
    
    
    public createProduct(request: google.cloud.vision.v1p4beta1.ICreateProductRequest, callback: google.cloud.vision.v1p4beta1.ProductSearch.CreateProductCallback): void;

Calls CreateProduct.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.icreateproductrequest)`   
CreateProductRequest message or plain object  
`callback` |  `[CreateProductCallback](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)`   
Node-style callback called with the error, if any, and Product  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createProduct(request)
    
    
    public createProduct(request: google.cloud.vision.v1p4beta1.ICreateProductRequest): Promise<google.cloud.vision.v1p4beta1.Product>;

Calls CreateProduct.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.icreateproductrequest)`   
CreateProductRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vision.v1p4beta1.Product](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.product-class)>` | Promise  
  
### createProductSet(request, callback)
    
    
    public createProductSet(request: google.cloud.vision.v1p4beta1.ICreateProductSetRequest, callback: google.cloud.vision.v1p4beta1.ProductSearch.CreateProductSetCallback): void;

Calls CreateProductSet.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateProductSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.icreateproductsetrequest)`   
CreateProductSetRequest message or plain object  
`callback` |  `[CreateProductSetCallback](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)`   
Node-style callback called with the error, if any, and ProductSet  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createProductSet(request)
    
    
    public createProductSet(request: google.cloud.vision.v1p4beta1.ICreateProductSetRequest): Promise<google.cloud.vision.v1p4beta1.ProductSet>;

Calls CreateProductSet.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateProductSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.icreateproductsetrequest)`   
CreateProductSetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vision.v1p4beta1.ProductSet](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.productset)>` | Promise  
  
### createReferenceImage(request, callback)
    
    
    public createReferenceImage(request: google.cloud.vision.v1p4beta1.ICreateReferenceImageRequest, callback: google.cloud.vision.v1p4beta1.ProductSearch.CreateReferenceImageCallback): void;

Calls CreateReferenceImage.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateReferenceImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.icreatereferenceimagerequest)`   
CreateReferenceImageRequest message or plain object  
`callback` |  `[CreateReferenceImageCallback](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)`   
Node-style callback called with the error, if any, and ReferenceImage  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createReferenceImage(request)
    
    
    public createReferenceImage(request: google.cloud.vision.v1p4beta1.ICreateReferenceImageRequest): Promise<google.cloud.vision.v1p4beta1.ReferenceImage>;

Calls CreateReferenceImage.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateReferenceImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.icreatereferenceimagerequest)`   
CreateReferenceImageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vision.v1p4beta1.ReferenceImage](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.referenceimage)>` | Promise  
  
### deleteProduct(request, callback)
    
    
    public deleteProduct(request: google.cloud.vision.v1p4beta1.IDeleteProductRequest, callback: google.cloud.vision.v1p4beta1.ProductSearch.DeleteProductCallback): void;

Calls DeleteProduct.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.ideleteproductrequest)`   
DeleteProductRequest message or plain object  
`callback` |  `[DeleteProductCallback](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteProduct(request)
    
    
    public deleteProduct(request: google.cloud.vision.v1p4beta1.IDeleteProductRequest): Promise<google.protobuf.Empty>;

Calls DeleteProduct.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.ideleteproductrequest)`   
DeleteProductRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.protobuf.empty)>` | Promise  
  
### deleteProductSet(request, callback)
    
    
    public deleteProductSet(request: google.cloud.vision.v1p4beta1.IDeleteProductSetRequest, callback: google.cloud.vision.v1p4beta1.ProductSearch.DeleteProductSetCallback): void;

Calls DeleteProductSet.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProductSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.ideleteproductsetrequest)`   
DeleteProductSetRequest message or plain object  
`callback` |  `[DeleteProductSetCallback](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteProductSet(request)
    
    
    public deleteProductSet(request: google.cloud.vision.v1p4beta1.IDeleteProductSetRequest): Promise<google.protobuf.Empty>;

Calls DeleteProductSet.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProductSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.ideleteproductsetrequest)`   
DeleteProductSetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.protobuf.empty)>` | Promise  
  
### deleteReferenceImage(request, callback)
    
    
    public deleteReferenceImage(request: google.cloud.vision.v1p4beta1.IDeleteReferenceImageRequest, callback: google.cloud.vision.v1p4beta1.ProductSearch.DeleteReferenceImageCallback): void;

Calls DeleteReferenceImage.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteReferenceImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.ideletereferenceimagerequest)`   
DeleteReferenceImageRequest message or plain object  
`callback` |  `[DeleteReferenceImageCallback](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteReferenceImage(request)
    
    
    public deleteReferenceImage(request: google.cloud.vision.v1p4beta1.IDeleteReferenceImageRequest): Promise<google.protobuf.Empty>;

Calls DeleteReferenceImage.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteReferenceImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.ideletereferenceimagerequest)`   
DeleteReferenceImageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.protobuf.empty)>` | Promise  
  
### getProduct(request, callback)
    
    
    public getProduct(request: google.cloud.vision.v1p4beta1.IGetProductRequest, callback: google.cloud.vision.v1p4beta1.ProductSearch.GetProductCallback): void;

Calls GetProduct.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.igetproductrequest)`   
GetProductRequest message or plain object  
`callback` |  `[GetProductCallback](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)`   
Node-style callback called with the error, if any, and Product  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProduct(request)
    
    
    public getProduct(request: google.cloud.vision.v1p4beta1.IGetProductRequest): Promise<google.cloud.vision.v1p4beta1.Product>;

Calls GetProduct.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.igetproductrequest)`   
GetProductRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vision.v1p4beta1.Product](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.product-class)>` | Promise  
  
### getProductSet(request, callback)
    
    
    public getProductSet(request: google.cloud.vision.v1p4beta1.IGetProductSetRequest, callback: google.cloud.vision.v1p4beta1.ProductSearch.GetProductSetCallback): void;

Calls GetProductSet.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProductSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.igetproductsetrequest)`   
GetProductSetRequest message or plain object  
`callback` |  `[GetProductSetCallback](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)`   
Node-style callback called with the error, if any, and ProductSet  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProductSet(request)
    
    
    public getProductSet(request: google.cloud.vision.v1p4beta1.IGetProductSetRequest): Promise<google.cloud.vision.v1p4beta1.ProductSet>;

Calls GetProductSet.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetProductSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.igetproductsetrequest)`   
GetProductSetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vision.v1p4beta1.ProductSet](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.productset)>` | Promise  
  
### getReferenceImage(request, callback)
    
    
    public getReferenceImage(request: google.cloud.vision.v1p4beta1.IGetReferenceImageRequest, callback: google.cloud.vision.v1p4beta1.ProductSearch.GetReferenceImageCallback): void;

Calls GetReferenceImage.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetReferenceImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.igetreferenceimagerequest)`   
GetReferenceImageRequest message or plain object  
`callback` |  `[GetReferenceImageCallback](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)`   
Node-style callback called with the error, if any, and ReferenceImage  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getReferenceImage(request)
    
    
    public getReferenceImage(request: google.cloud.vision.v1p4beta1.IGetReferenceImageRequest): Promise<google.cloud.vision.v1p4beta1.ReferenceImage>;

Calls GetReferenceImage.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetReferenceImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.igetreferenceimagerequest)`   
GetReferenceImageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vision.v1p4beta1.ReferenceImage](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.referenceimage)>` | Promise  
  
### importProductSets(request, callback)
    
    
    public importProductSets(request: google.cloud.vision.v1p4beta1.IImportProductSetsRequest, callback: google.cloud.vision.v1p4beta1.ProductSearch.ImportProductSetsCallback): void;

Calls ImportProductSets.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportProductSetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.iimportproductsetsrequest)`   
ImportProductSetsRequest message or plain object  
`callback` |  `[ImportProductSetsCallback](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importProductSets(request)
    
    
    public importProductSets(request: google.cloud.vision.v1p4beta1.IImportProductSetsRequest): Promise<google.longrunning.Operation>;

Calls ImportProductSets.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportProductSetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.iimportproductsetsrequest)`   
ImportProductSetsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.longrunning.operation)>` | Promise  
  
### listProducts(request, callback)
    
    
    public listProducts(request: google.cloud.vision.v1p4beta1.IListProductsRequest, callback: google.cloud.vision.v1p4beta1.ProductSearch.ListProductsCallback): void;

Calls ListProducts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.ilistproductsrequest)`   
ListProductsRequest message or plain object  
`callback` |  `[ListProductsCallback](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)`   
Node-style callback called with the error, if any, and ListProductsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProducts(request)
    
    
    public listProducts(request: google.cloud.vision.v1p4beta1.IListProductsRequest): Promise<google.cloud.vision.v1p4beta1.ListProductsResponse>;

Calls ListProducts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.ilistproductsrequest)`   
ListProductsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vision.v1p4beta1.ListProductsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.listproductsresponse)>` | Promise  
  
### listProductSets(request, callback)
    
    
    public listProductSets(request: google.cloud.vision.v1p4beta1.IListProductSetsRequest, callback: google.cloud.vision.v1p4beta1.ProductSearch.ListProductSetsCallback): void;

Calls ListProductSets.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProductSetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.ilistproductsetsrequest)`   
ListProductSetsRequest message or plain object  
`callback` |  `[ListProductSetsCallback](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)`   
Node-style callback called with the error, if any, and ListProductSetsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProductSets(request)
    
    
    public listProductSets(request: google.cloud.vision.v1p4beta1.IListProductSetsRequest): Promise<google.cloud.vision.v1p4beta1.ListProductSetsResponse>;

Calls ListProductSets.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListProductSetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.ilistproductsetsrequest)`   
ListProductSetsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vision.v1p4beta1.ListProductSetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.listproductsetsresponse)>` | Promise  
  
### listProductsInProductSet(request, callback)
    
    
    public listProductsInProductSet(request: google.cloud.vision.v1p4beta1.IListProductsInProductSetRequest, callback: google.cloud.vision.v1p4beta1.ProductSearch.ListProductsInProductSetCallback): void;

Calls ListProductsInProductSet.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProductsInProductSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.ilistproductsinproductsetrequest)`   
ListProductsInProductSetRequest message or plain object  
`callback` |  `[ListProductsInProductSetCallback](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)`   
Node-style callback called with the error, if any, and ListProductsInProductSetResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProductsInProductSet(request)
    
    
    public listProductsInProductSet(request: google.cloud.vision.v1p4beta1.IListProductsInProductSetRequest): Promise<google.cloud.vision.v1p4beta1.ListProductsInProductSetResponse>;

Calls ListProductsInProductSet.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListProductsInProductSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.ilistproductsinproductsetrequest)`   
ListProductsInProductSetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vision.v1p4beta1.ListProductsInProductSetResponse](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.listproductsinproductsetresponse)>` | Promise  
  
### listReferenceImages(request, callback)
    
    
    public listReferenceImages(request: google.cloud.vision.v1p4beta1.IListReferenceImagesRequest, callback: google.cloud.vision.v1p4beta1.ProductSearch.ListReferenceImagesCallback): void;

Calls ListReferenceImages.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReferenceImagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.ilistreferenceimagesrequest)`   
ListReferenceImagesRequest message or plain object  
`callback` |  `[ListReferenceImagesCallback](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)`   
Node-style callback called with the error, if any, and ListReferenceImagesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listReferenceImages(request)
    
    
    public listReferenceImages(request: google.cloud.vision.v1p4beta1.IListReferenceImagesRequest): Promise<google.cloud.vision.v1p4beta1.ListReferenceImagesResponse>;

Calls ListReferenceImages.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListReferenceImagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.ilistreferenceimagesrequest)`   
ListReferenceImagesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vision.v1p4beta1.ListReferenceImagesResponse](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.listreferenceimagesresponse)>` | Promise  
  
### purgeProducts(request, callback)
    
    
    public purgeProducts(request: google.cloud.vision.v1p4beta1.IPurgeProductsRequest, callback: google.cloud.vision.v1p4beta1.ProductSearch.PurgeProductsCallback): void;

Calls PurgeProducts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPurgeProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.ipurgeproductsrequest)`   
PurgeProductsRequest message or plain object  
`callback` |  `[PurgeProductsCallback](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### purgeProducts(request)
    
    
    public purgeProducts(request: google.cloud.vision.v1p4beta1.IPurgeProductsRequest): Promise<google.longrunning.Operation>;

Calls PurgeProducts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPurgeProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.ipurgeproductsrequest)`   
PurgeProductsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.longrunning.operation)>` | Promise  
  
### removeProductFromProductSet(request, callback)
    
    
    public removeProductFromProductSet(request: google.cloud.vision.v1p4beta1.IRemoveProductFromProductSetRequest, callback: google.cloud.vision.v1p4beta1.ProductSearch.RemoveProductFromProductSetCallback): void;

Calls RemoveProductFromProductSet.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveProductFromProductSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.iremoveproductfromproductsetrequest)`   
RemoveProductFromProductSetRequest message or plain object  
`callback` |  `[RemoveProductFromProductSetCallback](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeProductFromProductSet(request)
    
    
    public removeProductFromProductSet(request: google.cloud.vision.v1p4beta1.IRemoveProductFromProductSetRequest): Promise<google.protobuf.Empty>;

Calls RemoveProductFromProductSet.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRemoveProductFromProductSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.iremoveproductfromproductsetrequest)`   
RemoveProductFromProductSetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.protobuf.empty)>` | Promise  
  
### updateProduct(request, callback)
    
    
    public updateProduct(request: google.cloud.vision.v1p4beta1.IUpdateProductRequest, callback: google.cloud.vision.v1p4beta1.ProductSearch.UpdateProductCallback): void;

Calls UpdateProduct.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.iupdateproductrequest)`   
UpdateProductRequest message or plain object  
`callback` |  `[UpdateProductCallback](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)`   
Node-style callback called with the error, if any, and Product  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateProduct(request)
    
    
    public updateProduct(request: google.cloud.vision.v1p4beta1.IUpdateProductRequest): Promise<google.cloud.vision.v1p4beta1.Product>;

Calls UpdateProduct.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.iupdateproductrequest)`   
UpdateProductRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vision.v1p4beta1.Product](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.product-class)>` | Promise  
  
### updateProductSet(request, callback)
    
    
    public updateProductSet(request: google.cloud.vision.v1p4beta1.IUpdateProductSetRequest, callback: google.cloud.vision.v1p4beta1.ProductSearch.UpdateProductSetCallback): void;

Calls UpdateProductSet.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateProductSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.iupdateproductsetrequest)`   
UpdateProductSetRequest message or plain object  
`callback` |  `[UpdateProductSetCallback](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)`   
Node-style callback called with the error, if any, and ProductSet  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateProductSet(request)
    
    
    public updateProductSet(request: google.cloud.vision.v1p4beta1.IUpdateProductSetRequest): Promise<google.cloud.vision.v1p4beta1.ProductSet>;

Calls UpdateProductSet.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateProductSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.iupdateproductsetrequest)`   
UpdateProductSetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vision.v1p4beta1.ProductSet](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p4beta1.productset)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
