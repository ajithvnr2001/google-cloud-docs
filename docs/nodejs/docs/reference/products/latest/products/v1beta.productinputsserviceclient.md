---
url: https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/v1beta.productinputsserviceclient
title: Class v1beta.ProductInputsServiceClient (0.11.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:07.638494+00:00
---

# Class v1beta.ProductInputsServiceClient (0.11.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/v1beta.productinputsserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.ProductInputsServiceClient (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.1.1 

Service to use ProductInput resource. This service works for products with online channel only. v1beta

## Package

[@google-shopping/products](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of ProductInputsServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new ProductInputsServiceClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### descriptors
    
    
    descriptors: Descriptors;

### innerApiCalls
    
    
    innerApiCalls: {
            [name: string]: Function;
        };

### pathTemplates
    
    
    pathTemplates: {
            [name: string]: gax.PathTemplate;
        };

### port
    
    
    static get port(): number;

The port for this API service.

### productInputsServiceStub
    
    
    productInputsServiceStub?: Promise<{
            [name: string]: Function;
        }>;

### scopes
    
    
    static get scopes(): string[];

The scopes needed to make gRPC calls for every method defined in this service.

### servicePath
    
    
    static get servicePath(): string;

The DNS address for this API service.

### universeDomain
    
    
    get universeDomain(): string;

### warn
    
    
    warn: (code: string, message: string, warnType?: string) => void;

## Methods 

### accountPath(account)
    
    
    accountPath(account: string): string;

Return a fully-qualified account resource name string.

**Parameter**  
---  
**Name** | **Description**  
`account` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### deleteProductInput(request, options)
    
    
    deleteProductInput(request?: protos.google.shopping.merchant.products.v1beta.IDeleteProductInputRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.shopping.merchant.products.v1beta.IDeleteProductInputRequest | undefined),
            {} | undefined
        ]>;

Deletes a product input from your Merchant Center account.

After inserting, updating, or deleting a product input, it may take several minutes before the processed product can be retrieved.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.ideleteproductinputrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.protobuf.iempty), ([protos.google.shopping.merchant.products.v1beta.IDeleteProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.ideleteproductinputrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the product input resource to delete.
       *  Format: `accounts/{account}/productInputs/{product}`
       *  where the last section `product` consists of 4 parts:
       *  `channel~content_language~feed_label~offer_id`
       *  example for product name is
       *  `accounts/123/productInputs/online~en~US~sku123`.
       */
      // const name = 'abc123'
      /**
       *  Required. The primary or supplemental data source from which the product
       *  input should be deleted. Format:
       *  `accounts/{account}/dataSources/{datasource}`. For example,
       *  `accounts/123456/dataSources/104628`.
       */
      // const dataSource = 'abc123'
    
      // Imports the Products library
      const {ProductInputsServiceClient} = require('[@google-shopping/products](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const productsClient = new [ProductInputsServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/overview.html)();
    
      async function callDeleteProductInput() {
        // Construct request
        const request = {
          name,
          dataSource,
        };
    
        // Run request
        const response = await productsClient.deleteProductInput(request);
        console.log(response);
      }
    
      callDeleteProductInput();
    
    

### deleteProductInput(request, options, callback)
    
    
    deleteProductInput(request: protos.google.shopping.merchant.products.v1beta.IDeleteProductInputRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.shopping.merchant.products.v1beta.IDeleteProductInputRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.ideleteproductinputrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.protobuf.iempty), [protos.google.shopping.merchant.products.v1beta.IDeleteProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.ideleteproductinputrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteProductInput(request, callback)
    
    
    deleteProductInput(request: protos.google.shopping.merchant.products.v1beta.IDeleteProductInputRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.shopping.merchant.products.v1beta.IDeleteProductInputRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.ideleteproductinputrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.protobuf.iempty), [protos.google.shopping.merchant.products.v1beta.IDeleteProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.ideleteproductinputrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProjectId()
    
    
    getProjectId(): Promise<string>;

**Returns**  
---  
**Type** | **Description**  
`Promise<string>` |   
  
### getProjectId(callback)
    
    
    getProjectId(callback: Callback<string, undefined, undefined>): void;

**Parameter**  
---  
**Name** | **Description**  
`callback` |  `Callback<string, undefined, undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### initialize()
    
    
    initialize(): Promise<{
            [name: string]: Function;
        }>;

Initialize the client. Performs asynchronous operations (such as authentication) and prepares the client. This function will be called automatically when any class method is called for the first time, but if you need to initialize it before calling an actual method, feel free to call initialize() directly.

You can await on this method if you want to make sure the client is initialized.

**Returns**  
---  
**Type** | **Description**  
`Promise<{ [name: string]: Function; }>` | {Promise} A promise that resolves to an authenticated service stub.  
  
### insertProductInput(request, options)
    
    
    insertProductInput(request?: protos.google.shopping.merchant.products.v1beta.IInsertProductInputRequest, options?: CallOptions): Promise<[
            protos.google.shopping.merchant.products.v1beta.IProductInput,
            (protos.google.shopping.merchant.products.v1beta.IInsertProductInputRequest | undefined),
            {} | undefined
        ]>;

[Uploads a product input to your Merchant Center account](/merchant/api/guides/products/overview#upload-product-input). You must have a products data source to be able to insert a product. The unique identifier of the data source is passed as a query parameter in the request URL.

If an input with the same contentLanguage, offerId, and dataSource already exists, this method replaces that entry.

After inserting, updating, or deleting a product input, it may take several minutes before the processed product can be retrieved.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.iinsertproductinputrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.shopping.merchant.products.v1beta.IProductInput](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.iproductinput), ([protos.google.shopping.merchant.products.v1beta.IInsertProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.iinsertproductinputrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ProductInput](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.productinput). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The account where this product will be inserted.
       *  Format: `accounts/{account}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The product input to insert.
       */
      // const productInput = {}
      /**
       *  Required. The primary or supplemental product data source name. If the
       *  product already exists and data source provided is different, then the
       *  product will be moved to a new data source. For more information, see
       *  Overview of Data sources
       *  sub-API (/merchant/api/guides/data-sources/overview).
       *  Only API data sources are supported.
       *  Format: `accounts/{account}/dataSources/{datasource}`. For example,
       *  `accounts/123456/dataSources/104628`.
       */
      // const dataSource = 'abc123'
    
      // Imports the Products library
      const {ProductInputsServiceClient} = require('[@google-shopping/products](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const productsClient = new [ProductInputsServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/overview.html)();
    
      async function callInsertProductInput() {
        // Construct request
        const request = {
          parent,
          productInput,
          dataSource,
        };
    
        // Run request
        const response = await productsClient.insertProductInput(request);
        console.log(response);
      }
    
      callInsertProductInput();
    
    

### insertProductInput(request, options, callback)
    
    
    insertProductInput(request: protos.google.shopping.merchant.products.v1beta.IInsertProductInputRequest, options: CallOptions, callback: Callback<protos.google.shopping.merchant.products.v1beta.IProductInput, protos.google.shopping.merchant.products.v1beta.IInsertProductInputRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.iinsertproductinputrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.products.v1beta.IProductInput](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.iproductinput), [protos.google.shopping.merchant.products.v1beta.IInsertProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.iinsertproductinputrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insertProductInput(request, callback)
    
    
    insertProductInput(request: protos.google.shopping.merchant.products.v1beta.IInsertProductInputRequest, callback: Callback<protos.google.shopping.merchant.products.v1beta.IProductInput, protos.google.shopping.merchant.products.v1beta.IInsertProductInputRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.iinsertproductinputrequest)`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.products.v1beta.IProductInput](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.iproductinput), [protos.google.shopping.merchant.products.v1beta.IInsertProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.iinsertproductinputrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### matchAccountFromAccountName(accountName)
    
    
    matchAccountFromAccountName(accountName: string): string | number;

Parse the account from Account resource.

**Parameter**  
---  
**Name** | **Description**  
`accountName` |  `string`   
A fully-qualified path representing Account resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromProductInputName(productInputName)
    
    
    matchAccountFromProductInputName(productInputName: string): string | number;

Parse the account from ProductInput resource.

**Parameter**  
---  
**Name** | **Description**  
`productInputName` |  `string`   
A fully-qualified path representing ProductInput resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromProductName(productName)
    
    
    matchAccountFromProductName(productName: string): string | number;

Parse the account from Product resource.

**Parameter**  
---  
**Name** | **Description**  
`productName` |  `string`   
A fully-qualified path representing Product resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchProductFromProductName(productName)
    
    
    matchProductFromProductName(productName: string): string | number;

Parse the product from Product resource.

**Parameter**  
---  
**Name** | **Description**  
`productName` |  `string`   
A fully-qualified path representing Product resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the product.  
  
### matchProductinputFromProductInputName(productInputName)
    
    
    matchProductinputFromProductInputName(productInputName: string): string | number;

Parse the productinput from ProductInput resource.

**Parameter**  
---  
**Name** | **Description**  
`productInputName` |  `string`   
A fully-qualified path representing ProductInput resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the productinput.  
  
### productInputPath(account, productinput)
    
    
    productInputPath(account: string, productinput: string): string;

Return a fully-qualified productInput resource name string.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`productinput` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### productPath(account, product)
    
    
    productPath(account: string, product: string): string;

Return a fully-qualified product resource name string.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`product` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### updateProductInput(request, options)
    
    
    updateProductInput(request?: protos.google.shopping.merchant.products.v1beta.IUpdateProductInputRequest, options?: CallOptions): Promise<[
            protos.google.shopping.merchant.products.v1beta.IProductInput,
            (protos.google.shopping.merchant.products.v1beta.IUpdateProductInputRequest | undefined),
            {} | undefined
        ]>;

Updates the existing product input in your Merchant Center account.

After inserting, updating, or deleting a product input, it may take several minutes before the processed product can be retrieved.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.iupdateproductinputrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.shopping.merchant.products.v1beta.IProductInput](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.iproductinput), ([protos.google.shopping.merchant.products.v1beta.IUpdateProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.iupdateproductinputrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ProductInput](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.productinput). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The product input resource to update. Information you submit will
       *  be applied to the processed product as well.
       */
      // const productInput = {}
      /**
       *  Optional. The list of product attributes to be updated.
       *  If the update mask is omitted, then it is treated as implied field mask
       *  equivalent to all fields that are populated (have a non-empty value).
       *  Attributes specified in the update mask without a value specified in the
       *  body will be deleted from the product.
       *  Update mask can only be specified for top level fields in
       *  attributes and custom attributes.
       *  To specify the update mask for custom attributes you need to add the
       *  `custom_attribute.` prefix.
       *  Providing special "*" value for full product replacement is not supported.
       */
      // const updateMask = {}
      /**
       *  Required. The primary or supplemental product data source where
       *  `data_source` name identifies the product input to be updated.
       *  Only API data sources are supported.
       *  Format: `accounts/{account}/dataSources/{datasource}`. For example,
       *  `accounts/123456/dataSources/104628`.
       */
      // const dataSource = 'abc123'
    
      // Imports the Products library
      const {ProductInputsServiceClient} = require('[@google-shopping/products](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const productsClient = new [ProductInputsServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/overview.html)();
    
      async function callUpdateProductInput() {
        // Construct request
        const request = {
          productInput,
          dataSource,
        };
    
        // Run request
        const response = await productsClient.updateProductInput(request);
        console.log(response);
      }
    
      callUpdateProductInput();
    
    

### updateProductInput(request, options, callback)
    
    
    updateProductInput(request: protos.google.shopping.merchant.products.v1beta.IUpdateProductInputRequest, options: CallOptions, callback: Callback<protos.google.shopping.merchant.products.v1beta.IProductInput, protos.google.shopping.merchant.products.v1beta.IUpdateProductInputRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.iupdateproductinputrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.products.v1beta.IProductInput](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.iproductinput), [protos.google.shopping.merchant.products.v1beta.IUpdateProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.iupdateproductinputrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateProductInput(request, callback)
    
    
    updateProductInput(request: protos.google.shopping.merchant.products.v1beta.IUpdateProductInputRequest, callback: Callback<protos.google.shopping.merchant.products.v1beta.IProductInput, protos.google.shopping.merchant.products.v1beta.IUpdateProductInputRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.iupdateproductinputrequest)`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.products.v1beta.IProductInput](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.iproductinput), [protos.google.shopping.merchant.products.v1beta.IUpdateProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1beta.iupdateproductinputrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
