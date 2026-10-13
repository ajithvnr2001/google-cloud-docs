---
url: https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/v1beta.localinventoryserviceclient
title: Class v1beta.LocalInventoryServiceClient (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:03:10.540213+00:00
---

# Class v1beta.LocalInventoryServiceClient (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/v1beta.localinventoryserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.LocalInventoryServiceClient (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.12.0  0.7.1  0.5.0  0.4.0 

Service to manage local inventory for products v1beta

## Package

[@google-shopping/inventories](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of LocalInventoryServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new LocalInventoryServiceClient({fallback: true}, gax); ```  
  
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

### localInventoryServiceStub
    
    
    localInventoryServiceStub?: Promise<{
            [name: string]: Function;
        }>;

### pathTemplates
    
    
    pathTemplates: {
            [name: string]: gax.PathTemplate;
        };

### port
    
    
    static get port(): number;

The port for this API service.

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

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### deleteLocalInventory(request, options)
    
    
    deleteLocalInventory(request?: protos.google.shopping.merchant.inventories.v1beta.IDeleteLocalInventoryRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.shopping.merchant.inventories.v1beta.IDeleteLocalInventoryRequest | undefined),
            {} | undefined
        ]>;

Deletes the specified `LocalInventory` from the given product in your merchant account. It might take a up to an hour for the `LocalInventory` to be deleted from the specific product. Once you have received a successful delete response, wait for that period before attempting a delete again.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteLocalInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ideletelocalinventoryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.protobuf.iempty), ([protos.google.shopping.merchant.inventories.v1beta.IDeleteLocalInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ideletelocalinventoryrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the local inventory for the given product to delete.
       *  Format:
       *  `accounts/{account}/products/{product}/localInventories/{store_code}`
       */
      // const name = 'abc123'
    
      // Imports the Inventories library
      const {LocalInventoryServiceClient} = require('[@google-shopping/inventories](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const inventoriesClient = new [LocalInventoryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/overview.html)();
    
      async function callDeleteLocalInventory() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await inventoriesClient.deleteLocalInventory(request);
        console.log(response);
      }
    
      callDeleteLocalInventory();
    
    

### deleteLocalInventory(request, options, callback)
    
    
    deleteLocalInventory(request: protos.google.shopping.merchant.inventories.v1beta.IDeleteLocalInventoryRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.shopping.merchant.inventories.v1beta.IDeleteLocalInventoryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteLocalInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ideletelocalinventoryrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.protobuf.iempty), [protos.google.shopping.merchant.inventories.v1beta.IDeleteLocalInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ideletelocalinventoryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteLocalInventory(request, callback)
    
    
    deleteLocalInventory(request: protos.google.shopping.merchant.inventories.v1beta.IDeleteLocalInventoryRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.shopping.merchant.inventories.v1beta.IDeleteLocalInventoryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteLocalInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ideletelocalinventoryrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.protobuf.iempty), [protos.google.shopping.merchant.inventories.v1beta.IDeleteLocalInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ideletelocalinventoryrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### insertLocalInventory(request, options)
    
    
    insertLocalInventory(request?: protos.google.shopping.merchant.inventories.v1beta.IInsertLocalInventoryRequest, options?: CallOptions): Promise<[
            protos.google.shopping.merchant.inventories.v1beta.ILocalInventory,
            (protos.google.shopping.merchant.inventories.v1beta.IInsertLocalInventoryRequest | undefined),
            {} | undefined
        ]>;

Inserts a `LocalInventory` resource to a product in your merchant account.

Replaces the full `LocalInventory` resource if an entry with the same already exists for the product.

It might take up to 30 minutes for the new or updated `LocalInventory` resource to appear in products.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertLocalInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.iinsertlocalinventoryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.shopping.merchant.inventories.v1beta.ILocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilocalinventory), ([protos.google.shopping.merchant.inventories.v1beta.IInsertLocalInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.iinsertlocalinventoryrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [LocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.localinventory). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The account and product where this inventory will be inserted.
       *  Format: `accounts/{account}/products/{product}`
       */
      // const parent = 'abc123'
      /**
       *  Required. Local inventory information of the product. If the product
       *  already has a `LocalInventory` resource for the same `storeCode`, full
       *  replacement of the `LocalInventory` resource is performed.
       */
      // const localInventory = {}
    
      // Imports the Inventories library
      const {LocalInventoryServiceClient} = require('[@google-shopping/inventories](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const inventoriesClient = new [LocalInventoryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/overview.html)();
    
      async function callInsertLocalInventory() {
        // Construct request
        const request = {
          parent,
          localInventory,
        };
    
        // Run request
        const response = await inventoriesClient.insertLocalInventory(request);
        console.log(response);
      }
    
      callInsertLocalInventory();
    
    

### insertLocalInventory(request, options, callback)
    
    
    insertLocalInventory(request: protos.google.shopping.merchant.inventories.v1beta.IInsertLocalInventoryRequest, options: CallOptions, callback: Callback<protos.google.shopping.merchant.inventories.v1beta.ILocalInventory, protos.google.shopping.merchant.inventories.v1beta.IInsertLocalInventoryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertLocalInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.iinsertlocalinventoryrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.inventories.v1beta.ILocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilocalinventory), [protos.google.shopping.merchant.inventories.v1beta.IInsertLocalInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.iinsertlocalinventoryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insertLocalInventory(request, callback)
    
    
    insertLocalInventory(request: protos.google.shopping.merchant.inventories.v1beta.IInsertLocalInventoryRequest, callback: Callback<protos.google.shopping.merchant.inventories.v1beta.ILocalInventory, protos.google.shopping.merchant.inventories.v1beta.IInsertLocalInventoryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertLocalInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.iinsertlocalinventoryrequest)`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.inventories.v1beta.ILocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilocalinventory), [protos.google.shopping.merchant.inventories.v1beta.IInsertLocalInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.iinsertlocalinventoryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listLocalInventories(request, options)
    
    
    listLocalInventories(request?: protos.google.shopping.merchant.inventories.v1beta.IListLocalInventoriesRequest, options?: CallOptions): Promise<[
            protos.google.shopping.merchant.inventories.v1beta.ILocalInventory[],
            protos.google.shopping.merchant.inventories.v1beta.IListLocalInventoriesRequest | null,
            protos.google.shopping.merchant.inventories.v1beta.IListLocalInventoriesResponse
        ]>;

Lists the `LocalInventory` resources for the given product in your merchant account. The response might contain fewer items than specified by `pageSize`. If `pageToken` was returned in previous request, it can be used to obtain additional results.

`LocalInventory` resources are listed per product for a given account.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListLocalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilistlocalinventoriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.shopping.merchant.inventories.v1beta.ILocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilocalinventory)[], [protos.google.shopping.merchant.inventories.v1beta.IListLocalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilistlocalinventoriesrequest) | null, [protos.google.shopping.merchant.inventories.v1beta.IListLocalInventoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilistlocalinventoriesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [LocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.localinventory). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listLocalInventoriesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listLocalInventories(request, options, callback)
    
    
    listLocalInventories(request: protos.google.shopping.merchant.inventories.v1beta.IListLocalInventoriesRequest, options: CallOptions, callback: PaginationCallback<protos.google.shopping.merchant.inventories.v1beta.IListLocalInventoriesRequest, protos.google.shopping.merchant.inventories.v1beta.IListLocalInventoriesResponse | null | undefined, protos.google.shopping.merchant.inventories.v1beta.ILocalInventory>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListLocalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilistlocalinventoriesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.shopping.merchant.inventories.v1beta.IListLocalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilistlocalinventoriesrequest), [protos.google.shopping.merchant.inventories.v1beta.IListLocalInventoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilistlocalinventoriesresponse) | null | undefined, [protos.google.shopping.merchant.inventories.v1beta.ILocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilocalinventory)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listLocalInventories(request, callback)
    
    
    listLocalInventories(request: protos.google.shopping.merchant.inventories.v1beta.IListLocalInventoriesRequest, callback: PaginationCallback<protos.google.shopping.merchant.inventories.v1beta.IListLocalInventoriesRequest, protos.google.shopping.merchant.inventories.v1beta.IListLocalInventoriesResponse | null | undefined, protos.google.shopping.merchant.inventories.v1beta.ILocalInventory>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListLocalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilistlocalinventoriesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.shopping.merchant.inventories.v1beta.IListLocalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilistlocalinventoriesrequest), [protos.google.shopping.merchant.inventories.v1beta.IListLocalInventoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilistlocalinventoriesresponse) | null | undefined, [protos.google.shopping.merchant.inventories.v1beta.ILocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilocalinventory)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listLocalInventoriesAsync(request, options)
    
    
    listLocalInventoriesAsync(request?: protos.google.shopping.merchant.inventories.v1beta.IListLocalInventoriesRequest, options?: CallOptions): AsyncIterable<protos.google.shopping.merchant.inventories.v1beta.ILocalInventory>;

Equivalent to `listLocalInventories`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListLocalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilistlocalinventoriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.shopping.merchant.inventories.v1beta.ILocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilocalinventory)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [LocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.localinventory). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The `name` of the parent product to list local inventories for.
       *  Format:
       *  `accounts/{account}/products/{product}`
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of `LocalInventory` resources for the given
       *  product to return. The service returns fewer than this value if the number
       *  of inventories for the given product is less that than the `pageSize`. The
       *  default value is 25000. The maximum value is 25000; If a value higher than
       *  the maximum is specified, then the `pageSize` will default to the maximum
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous `ListLocalInventories` call.
       *  Provide the page token to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListLocalInventories`
       *  must match the call that provided the page token. The token returned as
       *  nextPageToken google.shopping.merchant.inventories.v1beta.ListLocalInventoriesResponse.next_page_token 
       *  in the response to the previous request.
       */
      // const pageToken = 'abc123'
    
      // Imports the Inventories library
      const {LocalInventoryServiceClient} = require('[@google-shopping/inventories](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const inventoriesClient = new [LocalInventoryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/overview.html)();
    
      async function callListLocalInventories() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = inventoriesClient.listLocalInventoriesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListLocalInventories();
    
    

### listLocalInventoriesStream(request, options)
    
    
    listLocalInventoriesStream(request?: protos.google.shopping.merchant.inventories.v1beta.IListLocalInventoriesRequest, options?: CallOptions): Transform;

Equivalent to `listLocalInventories`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListLocalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilistlocalinventoriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [LocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.localinventory) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listLocalInventoriesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### localInventoryPath(account, product, storeCode)
    
    
    localInventoryPath(account: string, product: string, storeCode: string): string;

Return a fully-qualified localInventory resource name string.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`product` |  `string`   
  
`storeCode` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### matchAccountFromLocalInventoryName(localInventoryName)
    
    
    matchAccountFromLocalInventoryName(localInventoryName: string): string | number;

Parse the account from LocalInventory resource.

**Parameter**  
---  
**Name** | **Description**  
`localInventoryName` |  `string`   
A fully-qualified path representing LocalInventory resource.  
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
  
### matchAccountFromRegionalInventoryName(regionalInventoryName)
    
    
    matchAccountFromRegionalInventoryName(regionalInventoryName: string): string | number;

Parse the account from RegionalInventory resource.

**Parameter**  
---  
**Name** | **Description**  
`regionalInventoryName` |  `string`   
A fully-qualified path representing RegionalInventory resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchProductFromLocalInventoryName(localInventoryName)
    
    
    matchProductFromLocalInventoryName(localInventoryName: string): string | number;

Parse the product from LocalInventory resource.

**Parameter**  
---  
**Name** | **Description**  
`localInventoryName` |  `string`   
A fully-qualified path representing LocalInventory resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the product.  
  
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
  
### matchProductFromRegionalInventoryName(regionalInventoryName)
    
    
    matchProductFromRegionalInventoryName(regionalInventoryName: string): string | number;

Parse the product from RegionalInventory resource.

**Parameter**  
---  
**Name** | **Description**  
`regionalInventoryName` |  `string`   
A fully-qualified path representing RegionalInventory resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the product.  
  
### matchRegionFromRegionalInventoryName(regionalInventoryName)
    
    
    matchRegionFromRegionalInventoryName(regionalInventoryName: string): string | number;

Parse the region from RegionalInventory resource.

**Parameter**  
---  
**Name** | **Description**  
`regionalInventoryName` |  `string`   
A fully-qualified path representing RegionalInventory resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the region.  
  
### matchStoreCodeFromLocalInventoryName(localInventoryName)
    
    
    matchStoreCodeFromLocalInventoryName(localInventoryName: string): string | number;

Parse the store_code from LocalInventory resource.

**Parameter**  
---  
**Name** | **Description**  
`localInventoryName` |  `string`   
A fully-qualified path representing LocalInventory resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the store_code.  
  
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
  
### regionalInventoryPath(account, product, region)
    
    
    regionalInventoryPath(account: string, product: string, region: string): string;

Return a fully-qualified regionalInventory resource name string.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`product` |  `string`   
  
`region` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
