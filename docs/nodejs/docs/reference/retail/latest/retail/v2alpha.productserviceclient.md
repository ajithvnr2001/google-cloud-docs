---
url: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/v2alpha.productserviceclient
title: Class v2alpha.ProductServiceClient (5.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:02:43.194806+00:00
---

# Class v2alpha.ProductServiceClient (5.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/v2alpha.productserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v2alpha.ProductServiceClient (5.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.4.0 (latest)  5.3.1  5.0.1  4.4.0  4.3.0  3.6.0  3.5.0  3.1.0  2.4.1  2.3.1  2.1.1  2.0.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.2  1.1.6 

Service for ingesting information of the customer's website. v2alpha

## Package

[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of ProductServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new ProductServiceClient({fallback: true}, gax); ```  
  
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

### locationsClient
    
    
    locationsClient: LocationsClient;

### operationsClient
    
    
    operationsClient: gax.OperationsClient;

### pathTemplates
    
    
    pathTemplates: {
            [name: string]: gax.PathTemplate;
        };

### port
    
    
    static get port(): number;

The port for this API service.

### productServiceStub
    
    
    productServiceStub?: Promise<{
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

### addFulfillmentPlaces(request, options)
    
    
    addFulfillmentPlaces(request?: protos.google.cloud.retail.v2alpha.IAddFulfillmentPlacesRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.retail.v2alpha.IAddFulfillmentPlacesResponse, protos.google.cloud.retail.v2alpha.IAddFulfillmentPlacesMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

We recommend that you use the method instead of the method. achieves the same results but provides more fine-grained control over ingesting local inventory data.

Incrementally adds place IDs to .

This process is asynchronous and does not require the to exist before updating fulfillment information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, the added place IDs are not immediately manifested in the queried by or .

The returned [Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)s will be obsolete after 1 day, and API will return NOT_FOUND afterwards.

If conflicting updates are issued, the [Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)s associated with the stale updates will not be marked as [done](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation) until being obsolete.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddFulfillmentPlacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddfulfillmentplacesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.retail.v2alpha.IAddFulfillmentPlacesResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddfulfillmentplacesresponse), [protos.google.cloud.retail.v2alpha.IAddFulfillmentPlacesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddfulfillmentplacesmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of
       *  Product google.cloud.retail.v2alpha.Product, such as
       *  `projects/* /locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`.
       *  If the caller does not have permission to access the
       *  Product google.cloud.retail.v2alpha.Product, regardless of whether or
       *  not it exists, a PERMISSION_DENIED error is returned.
       */
      // const product = 'abc123'
      /**
       *  Required. The fulfillment type, including commonly used types (such as
       *  pickup in store and same day delivery), and custom types.
       *  Supported values:
       *  * "pickup-in-store"
       *  * "ship-to-store"
       *  * "same-day-delivery"
       *  * "next-day-delivery"
       *  * "custom-type-1"
       *  * "custom-type-2"
       *  * "custom-type-3"
       *  * "custom-type-4"
       *  * "custom-type-5"
       *  If this field is set to an invalid value other than these, an
       *  INVALID_ARGUMENT error is returned.
       *  This field directly corresponds to
       *  Product.fulfillment_info.type google.cloud.retail.v2alpha.FulfillmentInfo.type.
       */
      // const type = 'abc123'
      /**
       *  Required. The IDs for this
       *  type google.cloud.retail.v2alpha.AddFulfillmentPlacesRequest.type, such
       *  as the store IDs for "pickup-in-store" or the region IDs for
       *  "same-day-delivery" to be added for this
       *  type google.cloud.retail.v2alpha.AddFulfillmentPlacesRequest.type.
       *  Duplicate IDs will be automatically ignored.
       *  At least 1 value is required, and a maximum of 2000 values are allowed.
       *  Each value must be a string with a length limit of 10 characters, matching
       *  the pattern `[a-zA-Z0-9_-]+`, such as "store1" or "REGION-2". Otherwise, an
       *  INVALID_ARGUMENT error is returned.
       *  If the total number of place IDs exceeds 2000 for this
       *  type google.cloud.retail.v2alpha.AddFulfillmentPlacesRequest.type  after
       *  adding, then the update will be rejected.
       */
      // const placeIds = ['abc','def']
      /**
       *  The time when the fulfillment updates are issued, used to prevent
       *  out-of-order updates on fulfillment information. If not provided, the
       *  internal system time will be used.
       */
      // const addTime = {}
      /**
       *  If set to true, and the Product google.cloud.retail.v2alpha.Product  is
       *  not found, the fulfillment information will still be processed and retained
       *  for at most 1 day and processed once the
       *  Product google.cloud.retail.v2alpha.Product  is created. If set to false,
       *  a NOT_FOUND error is returned if the
       *  Product google.cloud.retail.v2alpha.Product  is not found.
       */
      // const allowMissing = true
    
      // Imports the Retail library
      const {ProductServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callAddFulfillmentPlaces() {
        // Construct request
        const request = {
          product,
          type,
          placeIds,
        };
    
        // Run request
        const [operation] = await retailClient.addFulfillmentPlaces(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callAddFulfillmentPlaces();
    
    

### addFulfillmentPlaces(request, options, callback)
    
    
    addFulfillmentPlaces(request: protos.google.cloud.retail.v2alpha.IAddFulfillmentPlacesRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.retail.v2alpha.IAddFulfillmentPlacesResponse, protos.google.cloud.retail.v2alpha.IAddFulfillmentPlacesMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddFulfillmentPlacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddfulfillmentplacesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.retail.v2alpha.IAddFulfillmentPlacesResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddfulfillmentplacesresponse), [protos.google.cloud.retail.v2alpha.IAddFulfillmentPlacesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddfulfillmentplacesmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addFulfillmentPlaces(request, callback)
    
    
    addFulfillmentPlaces(request: protos.google.cloud.retail.v2alpha.IAddFulfillmentPlacesRequest, callback: Callback<LROperation<protos.google.cloud.retail.v2alpha.IAddFulfillmentPlacesResponse, protos.google.cloud.retail.v2alpha.IAddFulfillmentPlacesMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddFulfillmentPlacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddfulfillmentplacesrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.retail.v2alpha.IAddFulfillmentPlacesResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddfulfillmentplacesresponse), [protos.google.cloud.retail.v2alpha.IAddFulfillmentPlacesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddfulfillmentplacesmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addLocalInventories(request, options)
    
    
    addLocalInventories(request?: protos.google.cloud.retail.v2alpha.IAddLocalInventoriesRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.retail.v2alpha.IAddLocalInventoriesResponse, protos.google.cloud.retail.v2alpha.IAddLocalInventoriesMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates local inventory information for a at a list of places, while respecting the last update timestamps of each inventory field.

This process is asynchronous and does not require the to exist before updating inventory information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, updates are not immediately manifested in the queried by or .

Local inventory information can only be modified using this method. and has no effect on local inventories.

The returned [Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)s will be obsolete after 1 day, and API will return NOT_FOUND afterwards.

If conflicting updates are issued, the [Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)s associated with the stale updates will not be marked as [done](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation) until being obsolete.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddLocalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddlocalinventoriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.retail.v2alpha.IAddLocalInventoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddlocalinventoriesresponse), [protos.google.cloud.retail.v2alpha.IAddLocalInventoriesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddlocalinventoriesmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of
       *  Product google.cloud.retail.v2alpha.Product, such as
       *  `projects/* /locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`.
       *  If the caller does not have permission to access the
       *  Product google.cloud.retail.v2alpha.Product, regardless of whether or
       *  not it exists, a PERMISSION_DENIED error is returned.
       */
      // const product = 'abc123'
      /**
       *  Required. A list of inventory information at difference places. Each place
       *  is identified by its place ID. At most 3000 inventories are allowed per
       *  request.
       */
      // const localInventories = [1,2,3,4]
      /**
       *  Indicates which inventory fields in the provided list of
       *  LocalInventory google.cloud.retail.v2alpha.LocalInventory  to update. The
       *  field is updated to the provided value.
       *  If a field is set while the place does not have a previous local inventory,
       *  the local inventory at that store is created.
       *  If a field is set while the value of that field is not provided, the
       *  original field value, if it exists, is deleted.
       *  If the mask is not set or set with empty paths, all inventory fields will
       *  be updated.
       *  If an unsupported or unknown field is provided, an INVALID_ARGUMENT error
       *  is returned and the entire update will be ignored.
       */
      // const addMask = {}
      /**
       *  The time when the inventory updates are issued. Used to prevent
       *  out-of-order updates on local inventory fields. If not provided, the
       *  internal system time will be used.
       */
      // const addTime = {}
      /**
       *  If set to true, and the Product google.cloud.retail.v2alpha.Product  is
       *  not found, the local inventory will still be processed and retained for at
       *  most 1 day and processed once the
       *  Product google.cloud.retail.v2alpha.Product  is created. If set to false,
       *  a NOT_FOUND error is returned if the
       *  Product google.cloud.retail.v2alpha.Product  is not found.
       */
      // const allowMissing = true
    
      // Imports the Retail library
      const {ProductServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callAddLocalInventories() {
        // Construct request
        const request = {
          product,
          localInventories,
        };
    
        // Run request
        const [operation] = await retailClient.addLocalInventories(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callAddLocalInventories();
    
    

### addLocalInventories(request, options, callback)
    
    
    addLocalInventories(request: protos.google.cloud.retail.v2alpha.IAddLocalInventoriesRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.retail.v2alpha.IAddLocalInventoriesResponse, protos.google.cloud.retail.v2alpha.IAddLocalInventoriesMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddLocalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddlocalinventoriesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.retail.v2alpha.IAddLocalInventoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddlocalinventoriesresponse), [protos.google.cloud.retail.v2alpha.IAddLocalInventoriesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddlocalinventoriesmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addLocalInventories(request, callback)
    
    
    addLocalInventories(request: protos.google.cloud.retail.v2alpha.IAddLocalInventoriesRequest, callback: Callback<LROperation<protos.google.cloud.retail.v2alpha.IAddLocalInventoriesResponse, protos.google.cloud.retail.v2alpha.IAddLocalInventoriesMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddLocalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddlocalinventoriesrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.retail.v2alpha.IAddLocalInventoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddlocalinventoriesresponse), [protos.google.cloud.retail.v2alpha.IAddLocalInventoriesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iaddlocalinventoriesmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### alertConfigPath(project)
    
    
    alertConfigPath(project: string): string;

Return a fully-qualified alertConfig resource name string.

**Parameter**  
---  
**Name** | **Description**  
`project` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### attributesConfigPath(project, location, catalog)
    
    
    attributesConfigPath(project: string, location: string, catalog: string): string;

Return a fully-qualified attributesConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`catalog` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### branchPath(project, location, catalog, branch)
    
    
    branchPath(project: string, location: string, catalog: string, branch: string): string;

Return a fully-qualified branch resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`catalog` |  `string`   
  
`branch` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### cancelOperation(request, optionsOrCallback, callback)
    
    
    cancelOperation(request: protos.google.longrunning.CancelOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>, callback?: Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>): Promise<protos.google.protobuf.Empty>;

Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an value with a of 1, corresponding to `Code.CANCELLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### catalogPath(project, location, catalog)
    
    
    catalogPath(project: string, location: string, catalog: string): string;

Return a fully-qualified catalog resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`catalog` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### checkAddFulfillmentPlacesProgress(name)
    
    
    checkAddFulfillmentPlacesProgress(name: string): Promise<LROperation<protos.google.cloud.retail.v2alpha.AddFulfillmentPlacesResponse, protos.google.cloud.retail.v2alpha.AddFulfillmentPlacesMetadata>>;

Check the status of the long running operation returned by `addFulfillmentPlaces()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.retail.v2alpha.AddFulfillmentPlacesResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.addfulfillmentplacesresponse), [protos.google.cloud.retail.v2alpha.AddFulfillmentPlacesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.addfulfillmentplacesmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of
       *  Product google.cloud.retail.v2alpha.Product, such as
       *  `projects/* /locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`.
       *  If the caller does not have permission to access the
       *  Product google.cloud.retail.v2alpha.Product, regardless of whether or
       *  not it exists, a PERMISSION_DENIED error is returned.
       */
      // const product = 'abc123'
      /**
       *  Required. The fulfillment type, including commonly used types (such as
       *  pickup in store and same day delivery), and custom types.
       *  Supported values:
       *  * "pickup-in-store"
       *  * "ship-to-store"
       *  * "same-day-delivery"
       *  * "next-day-delivery"
       *  * "custom-type-1"
       *  * "custom-type-2"
       *  * "custom-type-3"
       *  * "custom-type-4"
       *  * "custom-type-5"
       *  If this field is set to an invalid value other than these, an
       *  INVALID_ARGUMENT error is returned.
       *  This field directly corresponds to
       *  Product.fulfillment_info.type google.cloud.retail.v2alpha.FulfillmentInfo.type.
       */
      // const type = 'abc123'
      /**
       *  Required. The IDs for this
       *  type google.cloud.retail.v2alpha.AddFulfillmentPlacesRequest.type, such
       *  as the store IDs for "pickup-in-store" or the region IDs for
       *  "same-day-delivery" to be added for this
       *  type google.cloud.retail.v2alpha.AddFulfillmentPlacesRequest.type.
       *  Duplicate IDs will be automatically ignored.
       *  At least 1 value is required, and a maximum of 2000 values are allowed.
       *  Each value must be a string with a length limit of 10 characters, matching
       *  the pattern `[a-zA-Z0-9_-]+`, such as "store1" or "REGION-2". Otherwise, an
       *  INVALID_ARGUMENT error is returned.
       *  If the total number of place IDs exceeds 2000 for this
       *  type google.cloud.retail.v2alpha.AddFulfillmentPlacesRequest.type  after
       *  adding, then the update will be rejected.
       */
      // const placeIds = ['abc','def']
      /**
       *  The time when the fulfillment updates are issued, used to prevent
       *  out-of-order updates on fulfillment information. If not provided, the
       *  internal system time will be used.
       */
      // const addTime = {}
      /**
       *  If set to true, and the Product google.cloud.retail.v2alpha.Product  is
       *  not found, the fulfillment information will still be processed and retained
       *  for at most 1 day and processed once the
       *  Product google.cloud.retail.v2alpha.Product  is created. If set to false,
       *  a NOT_FOUND error is returned if the
       *  Product google.cloud.retail.v2alpha.Product  is not found.
       */
      // const allowMissing = true
    
      // Imports the Retail library
      const {ProductServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callAddFulfillmentPlaces() {
        // Construct request
        const request = {
          product,
          type,
          placeIds,
        };
    
        // Run request
        const [operation] = await retailClient.addFulfillmentPlaces(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callAddFulfillmentPlaces();
    
    

### checkAddLocalInventoriesProgress(name)
    
    
    checkAddLocalInventoriesProgress(name: string): Promise<LROperation<protos.google.cloud.retail.v2alpha.AddLocalInventoriesResponse, protos.google.cloud.retail.v2alpha.AddLocalInventoriesMetadata>>;

Check the status of the long running operation returned by `addLocalInventories()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.retail.v2alpha.AddLocalInventoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.addlocalinventoriesresponse), [protos.google.cloud.retail.v2alpha.AddLocalInventoriesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.addlocalinventoriesmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of
       *  Product google.cloud.retail.v2alpha.Product, such as
       *  `projects/* /locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`.
       *  If the caller does not have permission to access the
       *  Product google.cloud.retail.v2alpha.Product, regardless of whether or
       *  not it exists, a PERMISSION_DENIED error is returned.
       */
      // const product = 'abc123'
      /**
       *  Required. A list of inventory information at difference places. Each place
       *  is identified by its place ID. At most 3000 inventories are allowed per
       *  request.
       */
      // const localInventories = [1,2,3,4]
      /**
       *  Indicates which inventory fields in the provided list of
       *  LocalInventory google.cloud.retail.v2alpha.LocalInventory  to update. The
       *  field is updated to the provided value.
       *  If a field is set while the place does not have a previous local inventory,
       *  the local inventory at that store is created.
       *  If a field is set while the value of that field is not provided, the
       *  original field value, if it exists, is deleted.
       *  If the mask is not set or set with empty paths, all inventory fields will
       *  be updated.
       *  If an unsupported or unknown field is provided, an INVALID_ARGUMENT error
       *  is returned and the entire update will be ignored.
       */
      // const addMask = {}
      /**
       *  The time when the inventory updates are issued. Used to prevent
       *  out-of-order updates on local inventory fields. If not provided, the
       *  internal system time will be used.
       */
      // const addTime = {}
      /**
       *  If set to true, and the Product google.cloud.retail.v2alpha.Product  is
       *  not found, the local inventory will still be processed and retained for at
       *  most 1 day and processed once the
       *  Product google.cloud.retail.v2alpha.Product  is created. If set to false,
       *  a NOT_FOUND error is returned if the
       *  Product google.cloud.retail.v2alpha.Product  is not found.
       */
      // const allowMissing = true
    
      // Imports the Retail library
      const {ProductServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callAddLocalInventories() {
        // Construct request
        const request = {
          product,
          localInventories,
        };
    
        // Run request
        const [operation] = await retailClient.addLocalInventories(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callAddLocalInventories();
    
    

### checkExportProductsProgress(name)
    
    
    checkExportProductsProgress(name: string): Promise<LROperation<protos.google.cloud.retail.v2alpha.ExportProductsResponse, protos.google.cloud.retail.v2alpha.ExportMetadata>>;

Check the status of the long running operation returned by `exportProducts()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.retail.v2alpha.ExportProductsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.exportproductsresponse), [protos.google.cloud.retail.v2alpha.ExportMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.exportmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name of a Branch google.cloud.retail.v2alpha.Branch,
       *  and `default_branch` for branch_id component is supported. For example
       *   `projects/1234/locations/global/catalogs/default_catalog/branches/default_branch`
       */
      // const parent = 'abc123'
      /**
       *  Required. The output location of the data.
       */
      // const outputConfig = {}
      /**
       *  A filtering expression to specify restrictions on returned events.
       *  The expression is a sequence of terms. Each term applies a restriction to
       *  the returned products. Use this expression to restrict results to a
       *  specific time range, tag, or stock state or to filter products by product
       *  type.
       *  For example, `lastModifiedTime > "2012-04-23T18:25:43.511Z"
       *  lastModifiedTime<"2012-04-23t18:25:43.511z" producttype="primary`" *="" we="" expect="" only="" four="" types="" of="" fields:="" *="" *="" `lastmodifiedtime`:="" this="" can="" be="" specified="" twice,="" once="" with="" a="" *="" less="" than="" operator="" and="" once="" with="" a="" greater="" than="" operator.="" the="" *="" `lastmodifiedtime`="" restriction="" should="" result="" in="" one,="" contiguous,="" *="" valid,="" last-modified,="" time="" range.="" *="" *="" `producttype`:="" supported="" values="" are="" `primary`="" and="" `variant`.="" the="" *="" boolean="" operators="" `or`="" and="" `not`="" are="" supported="" if="" the="" expression="" is="" *="" enclosed="" in="" parentheses="" and="" must="" be="" separated="" from="" the="" *="" `producttype`="" values="" by="" a="" space.="" *="" *="" `availability`:="" supported="" values="" are="" `in_stock`,="" `out_of_stock`,="" *="" `preorder`,="" and="" `backorder`.="" boolean="" operators="" `or`="" and="" `not`="" are="" *="" supported="" if="" the="" expression="" is="" enclosed="" in="" parentheses="" and="" must="" be="" *="" separated="" from="" the="" `availability`="" values="" by="" a="" space.="" *="" *="" `tag="" expressions`:="" restricts="" output="" to="" products="" that="" match="" all="" of="" the="" *="" specified="" tags.="" boolean="" operators="" `or`="" and="" `not`="" are="" supported="" if="" the="" *="" expression="" is="" enclosed="" in="" parentheses="" and="" the="" operators="" are="" separated="" *="" from="" the="" tag="" values="" by="" a="" space.="" also="" supported="" is="" '`-"taga"`',="" which="" *="" is="" equivalent="" to="" '`not="" "taga"`'.="" tag="" values="" must="" be="" double-quoted,="" *="" utf-8="" encoded="" strings="" and="" have="" a="" size="" limit="" of="" 1,000="" characters.="" *="" some="" examples="" of="" valid="" filters="" expressions:="" *="" *="" example="" 1:="" `lastmodifiedtime=""> "2012-04-23T18:25:43.511Z"
       *              lastModifiedTime < "2012-04-23t18:30:43.511z"`="" *="" *="" example="" 2:="" `lastmodifiedtime=""> "2012-04-23T18:25:43.511Z"
       *              productType = "variant"`
       *    * Example 3: `tag=("Red" OR "Blue") tag="New-Arrival"
       *              tag=(NOT "promotional")
       *              productType = "primary" lastModifiedTime < *="" "2018-04-23t18:30:43.511z"`="" *="" *="" example="" 4:="" `lastmodifiedtime=""> "2012-04-23T18:25:43.511Z"`
       *    * Example 5: `availability = (IN_STOCK OR BACKORDER)`
       */
      // const filter = 'abc123'
    
      // Imports the Retail library
      const {ProductServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callExportProducts() {
        // Construct request
        const request = {
          parent,
          outputConfig,
        };
    
        // Run request
        const [operation] = await retailClient.exportProducts(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportProducts();
    
    

### checkImportProductsProgress(name)
    
    
    checkImportProductsProgress(name: string): Promise<LROperation<protos.google.cloud.retail.v2alpha.ImportProductsResponse, protos.google.cloud.retail.v2alpha.ImportMetadata>>;

Check the status of the long running operation returned by `importProducts()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.retail.v2alpha.ImportProductsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.importproductsresponse), [protos.google.cloud.retail.v2alpha.ImportMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.importmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required.
       *  `projects/1234/locations/global/catalogs/default_catalog/branches/default_branch`
       *  If no updateMask is specified, requires products.create permission.
       *  If updateMask is specified, requires products.update permission.
       */
      // const parent = 'abc123'
      /**
       *  Required. The desired input location of the data.
       */
      // const inputConfig = {}
      /**
       *  The desired location of errors incurred during the Import.
       */
      // const errorsConfig = {}
      /**
       *  Indicates which fields in the provided imported `products` to update. If
       *  not set, all fields are updated. If provided, only the existing product
       *  fields are updated. Missing products will not be created.
       */
      // const updateMask = {}
      /**
       *  The mode of reconciliation between existing products and the products to be
       *  imported. Defaults to
       *  ReconciliationMode.INCREMENTAL google.cloud.retail.v2alpha.ImportProductsRequest.ReconciliationMode.INCREMENTAL.
       */
      // const reconciliationMode = {}
      /**
       *  Full Pub/Sub topic name for receiving notification. If this field is set,
       *  when the import is finished, a notification is sent to
       *  specified Pub/Sub topic. The message data is JSON string of a
       *  Operation google.longrunning.Operation.
       *  Format of the Pub/Sub topic is `projects/{project}/topics/{topic}`. It has
       *  to be within the same project as
       *  ImportProductsRequest.parent google.cloud.retail.v2alpha.ImportProductsRequest.parent.
       *  Make sure that both
       *  `cloud-retail-customer-data-access@system.gserviceaccount.com` and
       *  `service-

### checkPurgeProductsProgress(name)
    
    
    checkPurgeProductsProgress(name: string): Promise<LROperation<protos.google.cloud.retail.v2alpha.PurgeProductsResponse, protos.google.cloud.retail.v2alpha.PurgeProductsMetadata>>;

Check the status of the long running operation returned by `purgeProducts()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.retail.v2alpha.PurgeProductsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.purgeproductsresponse), [protos.google.cloud.retail.v2alpha.PurgeProductsMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.purgeproductsmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the branch under which the products are
       *  created. The format is
       *  `projects/${projectId}/locations/global/catalogs/${catalogId}/branches/${branchId}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The filter string to specify the products to be deleted with a
       *  length limit of 5,000 characters.
       *  Empty string filter is not allowed. "*" implies delete all items in a
       *  branch.
       *  The eligible fields for filtering are:
       *  * `availability`: Double quoted
       *  Product.availability google.cloud.retail.v2alpha.Product.availability 
       *  string.
       *  * `create_time` : in ISO 8601 "zulu" format.
       *  Supported syntax:
       *  * Comparators (">", "<", "="">=", "<=", "=").
       *    Examples:
       *    * create_time <= " 2015-02-13t17:05:46z"="" *="" *="" availability="IN_STOCK" *="" *="" conjunctions="" ("and")="" *="" examples:="" *="" *="" create_time=""><= "2015-02-13t17:05:46z"="" and="" availability="PREORDER" *="" *="" disjunctions="" ("or")="" *="" examples:="" *="" *="" create_time=""><= "2015-02-13t17:05:46z"="" or="" availability="IN_STOCK" *="" *="" can="" support="" nested="" queries.="" *="" examples:="" *="" *="" (create_time=""><= "2015-02-13t17:05:46z"="" and="" availability="PREORDER" )="" *="" or="" (create_time="">= "2015-02-14T13:03:32Z" AND availability = "IN_STOCK")
       *  * Filter Limits:
       *    * Filter should not contain more than 6 conditions.
       *    * Max nesting depth should not exceed 2 levels.
       *  Examples queries:
       *  * Delete back order products created before a timestamp.
       *    create_time <= "2015-02-13t17:05:46z"="" or="" availability="BACKORDER" */="" const="" filter='abc123' *="" *="" actually="" perform="" the="" purge.="" *="" if="" `force`="" is="" set="" to="" false,="" the="" method="" will="" return="" the="" expected="" purge="" count="" *="" without="" deleting="" any="" products.="" */="" const="" force="true" imports="" the="" retail="" library="" const="" {productserviceclient}="require('@google-cloud/retail').v2alpha;" instantiates="" a="" client="" const="" retailclient="new" productserviceclient();="" async="" function="" callpurgeproducts()="" {="" construct="" request="" const="" request="{" parent,="" filter,="" };="" run="" request="" const="" [operation]="await" retailclient.purgeproducts(request);="" const="" [response]="await" operation.promise();="" console.log(response);="" }="" callpurgeproducts();="">

### checkRemoveFulfillmentPlacesProgress(name)
    
    
    checkRemoveFulfillmentPlacesProgress(name: string): Promise<LROperation<protos.google.cloud.retail.v2alpha.RemoveFulfillmentPlacesResponse, protos.google.cloud.retail.v2alpha.RemoveFulfillmentPlacesMetadata>>;

Check the status of the long running operation returned by `removeFulfillmentPlaces()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.retail.v2alpha.RemoveFulfillmentPlacesResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.removefulfillmentplacesresponse), [protos.google.cloud.retail.v2alpha.RemoveFulfillmentPlacesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.removefulfillmentplacesmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of
       *  Product google.cloud.retail.v2alpha.Product, such as
       *  `projects/* /locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`.
       *  If the caller does not have permission to access the
       *  Product google.cloud.retail.v2alpha.Product, regardless of whether or
       *  not it exists, a PERMISSION_DENIED error is returned.
       */
      // const product = 'abc123'
      /**
       *  Required. The fulfillment type, including commonly used types (such as
       *  pickup in store and same day delivery), and custom types.
       *  Supported values:
       *  * "pickup-in-store"
       *  * "ship-to-store"
       *  * "same-day-delivery"
       *  * "next-day-delivery"
       *  * "custom-type-1"
       *  * "custom-type-2"
       *  * "custom-type-3"
       *  * "custom-type-4"
       *  * "custom-type-5"
       *  If this field is set to an invalid value other than these, an
       *  INVALID_ARGUMENT error is returned.
       *  This field directly corresponds to
       *  Product.fulfillment_info.type google.cloud.retail.v2alpha.FulfillmentInfo.type.
       */
      // const type = 'abc123'
      /**
       *  Required. The IDs for this
       *  type google.cloud.retail.v2alpha.RemoveFulfillmentPlacesRequest.type,
       *  such as the store IDs for "pickup-in-store" or the region IDs for
       *  "same-day-delivery", to be removed for this
       *  type google.cloud.retail.v2alpha.RemoveFulfillmentPlacesRequest.type.
       *  At least 1 value is required, and a maximum of 2000 values are allowed.
       *  Each value must be a string with a length limit of 10 characters, matching
       *  the pattern `[a-zA-Z0-9_-]+`, such as "store1" or "REGION-2". Otherwise, an
       *  INVALID_ARGUMENT error is returned.
       */
      // const placeIds = ['abc','def']
      /**
       *  The time when the fulfillment updates are issued, used to prevent
       *  out-of-order updates on fulfillment information. If not provided, the
       *  internal system time will be used.
       */
      // const removeTime = {}
      /**
       *  If set to true, and the Product google.cloud.retail.v2alpha.Product  is
       *  not found, the fulfillment information will still be processed and retained
       *  for at most 1 day and processed once the
       *  Product google.cloud.retail.v2alpha.Product  is created. If set to false,
       *  a NOT_FOUND error is returned if the
       *  Product google.cloud.retail.v2alpha.Product  is not found.
       */
      // const allowMissing = true
    
      // Imports the Retail library
      const {ProductServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callRemoveFulfillmentPlaces() {
        // Construct request
        const request = {
          product,
          type,
          placeIds,
        };
    
        // Run request
        const [operation] = await retailClient.removeFulfillmentPlaces(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callRemoveFulfillmentPlaces();
    
    

### checkRemoveLocalInventoriesProgress(name)
    
    
    checkRemoveLocalInventoriesProgress(name: string): Promise<LROperation<protos.google.cloud.retail.v2alpha.RemoveLocalInventoriesResponse, protos.google.cloud.retail.v2alpha.RemoveLocalInventoriesMetadata>>;

Check the status of the long running operation returned by `removeLocalInventories()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.retail.v2alpha.RemoveLocalInventoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.removelocalinventoriesresponse), [protos.google.cloud.retail.v2alpha.RemoveLocalInventoriesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.removelocalinventoriesmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of
       *  Product google.cloud.retail.v2alpha.Product, such as
       *  `projects/* /locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`.
       *  If the caller does not have permission to access the
       *  Product google.cloud.retail.v2alpha.Product, regardless of whether or
       *  not it exists, a PERMISSION_DENIED error is returned.
       */
      // const product = 'abc123'
      /**
       *  Required. A list of place IDs to have their inventory deleted.
       *  At most 3000 place IDs are allowed per request.
       */
      // const placeIds = ['abc','def']
      /**
       *  The time when the inventory deletions are issued. Used to prevent
       *  out-of-order updates and deletions on local inventory fields. If not
       *  provided, the internal system time will be used.
       */
      // const removeTime = {}
      /**
       *  If set to true, and the Product google.cloud.retail.v2alpha.Product  is
       *  not found, the local inventory removal request will still be processed and
       *  retained for at most 1 day and processed once the
       *  Product google.cloud.retail.v2alpha.Product  is created. If set to false,
       *  a NOT_FOUND error is returned if the
       *  Product google.cloud.retail.v2alpha.Product  is not found.
       */
      // const allowMissing = true
    
      // Imports the Retail library
      const {ProductServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callRemoveLocalInventories() {
        // Construct request
        const request = {
          product,
          placeIds,
        };
    
        // Run request
        const [operation] = await retailClient.removeLocalInventories(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callRemoveLocalInventories();
    
    

### checkSetInventoryProgress(name)
    
    
    checkSetInventoryProgress(name: string): Promise<LROperation<protos.google.cloud.retail.v2alpha.SetInventoryResponse, protos.google.cloud.retail.v2alpha.SetInventoryMetadata>>;

Check the status of the long running operation returned by `setInventory()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.retail.v2alpha.SetInventoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.setinventoryresponse), [protos.google.cloud.retail.v2alpha.SetInventoryMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.setinventorymetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The inventory information to update. The allowable fields to
       *  update are:
       *  * Product.price_info google.cloud.retail.v2alpha.Product.price_info 
       *  * Product.availability google.cloud.retail.v2alpha.Product.availability 
       *  * Product.available_quantity google.cloud.retail.v2alpha.Product.available_quantity 
       *  * Product.fulfillment_info google.cloud.retail.v2alpha.Product.fulfillment_info 
       *  The updated inventory fields must be specified in
       *  SetInventoryRequest.set_mask google.cloud.retail.v2alpha.SetInventoryRequest.set_mask.
       *  If
       *  SetInventoryRequest.inventory.name google.cloud.retail.v2alpha.Product.name 
       *  is empty or invalid, an INVALID_ARGUMENT error is returned.
       *  If the caller does not have permission to update the
       *  Product google.cloud.retail.v2alpha.Product  named in
       *  Product.name google.cloud.retail.v2alpha.Product.name, regardless of
       *  whether or not it exists, a PERMISSION_DENIED error is returned.
       *  If the Product google.cloud.retail.v2alpha.Product  to update does not
       *  have existing inventory information, the provided inventory information
       *  will be inserted.
       *  If the Product google.cloud.retail.v2alpha.Product  to update has
       *  existing inventory information, the provided inventory information will be
       *  merged while respecting the last update time for each inventory field,
       *  using the provided or default value for
       *  SetInventoryRequest.set_time google.cloud.retail.v2alpha.SetInventoryRequest.set_time.
       *  The caller can replace place IDs for a subset of fulfillment types in the
       *  following ways:
       *  * Adds "fulfillment_info" in
       *  SetInventoryRequest.set_mask google.cloud.retail.v2alpha.SetInventoryRequest.set_mask 
       *  * Specifies only the desired fulfillment types and corresponding place IDs
       *  to update in
       *  SetInventoryRequest.inventory.fulfillment_info google.cloud.retail.v2alpha.Product.fulfillment_info 
       *  The caller can clear all place IDs from a subset of fulfillment types in
       *  the following ways:
       *  * Adds "fulfillment_info" in
       *  SetInventoryRequest.set_mask google.cloud.retail.v2alpha.SetInventoryRequest.set_mask 
       *  * Specifies only the desired fulfillment types to clear in
       *  SetInventoryRequest.inventory.fulfillment_info google.cloud.retail.v2alpha.Product.fulfillment_info 
       *  * Checks that only the desired fulfillment info types have empty
       *  SetInventoryRequest.inventory.fulfillment_info.place_ids google.cloud.retail.v2alpha.FulfillmentInfo.place_ids 
       *  The last update time is recorded for the following inventory fields:
       *  * Product.price_info google.cloud.retail.v2alpha.Product.price_info 
       *  * Product.availability google.cloud.retail.v2alpha.Product.availability 
       *  * Product.available_quantity google.cloud.retail.v2alpha.Product.available_quantity 
       *  * Product.fulfillment_info google.cloud.retail.v2alpha.Product.fulfillment_info 
       *  If a full overwrite of inventory information while ignoring timestamps is
       *  needed,
       *  ProductService.UpdateProduct google.cloud.retail.v2alpha.ProductService.UpdateProduct 
       *  should be invoked instead.
       */
      // const inventory = {}
      /**
       *  Indicates which inventory fields in the provided
       *  Product google.cloud.retail.v2alpha.Product  to update.
       *  At least one field must be provided.
       *  If an unsupported or unknown field is provided, an INVALID_ARGUMENT error
       *  is returned and the entire update will be ignored.
       */
      // const setMask = {}
      /**
       *  The time when the request is issued, used to prevent
       *  out-of-order updates on inventory fields with the last update time
       *  recorded. If not provided, the internal system time will be used.
       */
      // const setTime = {}
      /**
       *  If set to true, and the Product google.cloud.retail.v2alpha.Product  with
       *  name Product.name google.cloud.retail.v2alpha.Product.name  is not found,
       *  the inventory update will still be processed and retained for at most 1 day
       *  until the Product google.cloud.retail.v2alpha.Product  is created. If set
       *  to false, a NOT_FOUND error is returned if the
       *  Product google.cloud.retail.v2alpha.Product  is not found.
       */
      // const allowMissing = true
    
      // Imports the Retail library
      const {ProductServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callSetInventory() {
        // Construct request
        const request = {
          inventory,
        };
    
        // Run request
        const [operation] = await retailClient.setInventory(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callSetInventory();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### completionConfigPath(project, location, catalog)
    
    
    completionConfigPath(project: string, location: string, catalog: string): string;

Return a fully-qualified completionConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`catalog` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### controlPath(project, location, catalog, control)
    
    
    controlPath(project: string, location: string, catalog: string, control: string): string;

Return a fully-qualified control resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`catalog` |  `string`   
  
`control` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### createProduct(request, options)
    
    
    createProduct(request?: protos.google.cloud.retail.v2alpha.ICreateProductRequest, options?: CallOptions): Promise<[
            protos.google.cloud.retail.v2alpha.IProduct,
            protos.google.cloud.retail.v2alpha.ICreateProductRequest | undefined,
            {} | undefined
        ]>;

Creates a .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icreateproductrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.retail.v2alpha.IProduct](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iproduct), [protos.google.cloud.retail.v2alpha.ICreateProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icreateproductrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent catalog resource name, such as
       *  `projects/* /locations/global/catalogs/default_catalog/branches/default_branch`.
       */
      // const parent = 'abc123'
      /**
       *  Required. The Product google.cloud.retail.v2alpha.Product  to create.
       */
      // const product = {}
      /**
       *  Required. The ID to use for the
       *  Product google.cloud.retail.v2alpha.Product, which will become the final
       *  component of the Product.name google.cloud.retail.v2alpha.Product.name.
       *  If the caller does not have permission to create the
       *  Product google.cloud.retail.v2alpha.Product, regardless of whether or
       *  not it exists, a PERMISSION_DENIED error is returned.
       *  This field must be unique among all
       *  Product google.cloud.retail.v2alpha.Product s with the same
       *  parent google.cloud.retail.v2alpha.CreateProductRequest.parent.
       *  Otherwise, an ALREADY_EXISTS error is returned.
       *  This field must be a UTF-8 encoded string with a length limit of 128
       *  characters. Otherwise, an INVALID_ARGUMENT error is returned.
       */
      // const productId = 'abc123'
    
      // Imports the Retail library
      const {ProductServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callCreateProduct() {
        // Construct request
        const request = {
          parent,
          product,
          productId,
        };
    
        // Run request
        const response = await retailClient.createProduct(request);
        console.log(response);
      }
    
      callCreateProduct();
    
    

### createProduct(request, options, callback)
    
    
    createProduct(request: protos.google.cloud.retail.v2alpha.ICreateProductRequest, options: CallOptions, callback: Callback<protos.google.cloud.retail.v2alpha.IProduct, protos.google.cloud.retail.v2alpha.ICreateProductRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icreateproductrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2alpha.IProduct](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iproduct), [protos.google.cloud.retail.v2alpha.ICreateProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icreateproductrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createProduct(request, callback)
    
    
    createProduct(request: protos.google.cloud.retail.v2alpha.ICreateProductRequest, callback: Callback<protos.google.cloud.retail.v2alpha.IProduct, protos.google.cloud.retail.v2alpha.ICreateProductRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icreateproductrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2alpha.IProduct](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iproduct), [protos.google.cloud.retail.v2alpha.ICreateProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icreateproductrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteOperation(request, optionsOrCallback, callback)
    
    
    deleteOperation(request: protos.google.longrunning.DeleteOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.protobuf.Empty, protos.google.longrunning.DeleteOperationRequest, {} | null | undefined>, callback?: Callback<protos.google.protobuf.Empty, protos.google.longrunning.DeleteOperationRequest, {} | null | undefined>): Promise<protos.google.protobuf.Empty>;

Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### deleteProduct(request, options)
    
    
    deleteProduct(request?: protos.google.cloud.retail.v2alpha.IDeleteProductRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.cloud.retail.v2alpha.IDeleteProductRequest | undefined,
            {} | undefined
        ]>;

Deletes a .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ideleteproductrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.iempty), [protos.google.cloud.retail.v2alpha.IDeleteProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ideleteproductrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of
       *  Product google.cloud.retail.v2alpha.Product, such as
       *  `projects/* /locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`.
       *  If the caller does not have permission to delete the
       *  Product google.cloud.retail.v2alpha.Product, regardless of whether or
       *  not it exists, a PERMISSION_DENIED error is returned.
       *  If the Product google.cloud.retail.v2alpha.Product  to delete does not
       *  exist, a NOT_FOUND error is returned.
       *  The Product google.cloud.retail.v2alpha.Product  to delete can neither be
       *  a
       *  Product.Type.COLLECTION google.cloud.retail.v2alpha.Product.Type.COLLECTION 
       *  Product google.cloud.retail.v2alpha.Product  member nor a
       *  Product.Type.PRIMARY google.cloud.retail.v2alpha.Product.Type.PRIMARY 
       *  Product google.cloud.retail.v2alpha.Product  with more than one
       *  variants google.cloud.retail.v2alpha.Product.Type.VARIANT. Otherwise, an
       *  INVALID_ARGUMENT error is returned.
       *  All inventory information for the named
       *  Product google.cloud.retail.v2alpha.Product  will be deleted.
       */
      // const name = 'abc123'
      /**
       *  This value only applies to the case when the target product is of type
       *  PRIMARY.
       *  When deleting a product of VARIANT/COLLECTION type, this value
       *  will be ignored.
       *  When set to true, the subsequent variant products will be
       *  deleted.
       *  When set to false, if the primary product has active variant products, an
       *  error will be returned.
       */
      // const force = true
    
      // Imports the Retail library
      const {ProductServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callDeleteProduct() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await retailClient.deleteProduct(request);
        console.log(response);
      }
    
      callDeleteProduct();
    
    

### deleteProduct(request, options, callback)
    
    
    deleteProduct(request: protos.google.cloud.retail.v2alpha.IDeleteProductRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.retail.v2alpha.IDeleteProductRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ideleteproductrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.iempty), [protos.google.cloud.retail.v2alpha.IDeleteProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ideleteproductrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteProduct(request, callback)
    
    
    deleteProduct(request: protos.google.cloud.retail.v2alpha.IDeleteProductRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.retail.v2alpha.IDeleteProductRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ideleteproductrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.iempty), [protos.google.cloud.retail.v2alpha.IDeleteProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ideleteproductrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportProducts(request, options)
    
    
    exportProducts(request?: protos.google.cloud.retail.v2alpha.IExportProductsRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.retail.v2alpha.IExportProductsResponse, protos.google.cloud.retail.v2alpha.IExportMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Exports multiple s.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iexportproductsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.retail.v2alpha.IExportProductsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iexportproductsresponse), [protos.google.cloud.retail.v2alpha.IExportMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iexportmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name of a Branch google.cloud.retail.v2alpha.Branch,
       *  and `default_branch` for branch_id component is supported. For example
       *   `projects/1234/locations/global/catalogs/default_catalog/branches/default_branch`
       */
      // const parent = 'abc123'
      /**
       *  Required. The output location of the data.
       */
      // const outputConfig = {}
      /**
       *  A filtering expression to specify restrictions on returned events.
       *  The expression is a sequence of terms. Each term applies a restriction to
       *  the returned products. Use this expression to restrict results to a
       *  specific time range, tag, or stock state or to filter products by product
       *  type.
       *  For example, `lastModifiedTime > "2012-04-23T18:25:43.511Z"
       *  lastModifiedTime<"2012-04-23t18:25:43.511z" producttype="primary`" *="" we="" expect="" only="" four="" types="" of="" fields:="" *="" *="" `lastmodifiedtime`:="" this="" can="" be="" specified="" twice,="" once="" with="" a="" *="" less="" than="" operator="" and="" once="" with="" a="" greater="" than="" operator.="" the="" *="" `lastmodifiedtime`="" restriction="" should="" result="" in="" one,="" contiguous,="" *="" valid,="" last-modified,="" time="" range.="" *="" *="" `producttype`:="" supported="" values="" are="" `primary`="" and="" `variant`.="" the="" *="" boolean="" operators="" `or`="" and="" `not`="" are="" supported="" if="" the="" expression="" is="" *="" enclosed="" in="" parentheses="" and="" must="" be="" separated="" from="" the="" *="" `producttype`="" values="" by="" a="" space.="" *="" *="" `availability`:="" supported="" values="" are="" `in_stock`,="" `out_of_stock`,="" *="" `preorder`,="" and="" `backorder`.="" boolean="" operators="" `or`="" and="" `not`="" are="" *="" supported="" if="" the="" expression="" is="" enclosed="" in="" parentheses="" and="" must="" be="" *="" separated="" from="" the="" `availability`="" values="" by="" a="" space.="" *="" *="" `tag="" expressions`:="" restricts="" output="" to="" products="" that="" match="" all="" of="" the="" *="" specified="" tags.="" boolean="" operators="" `or`="" and="" `not`="" are="" supported="" if="" the="" *="" expression="" is="" enclosed="" in="" parentheses="" and="" the="" operators="" are="" separated="" *="" from="" the="" tag="" values="" by="" a="" space.="" also="" supported="" is="" '`-"taga"`',="" which="" *="" is="" equivalent="" to="" '`not="" "taga"`'.="" tag="" values="" must="" be="" double-quoted,="" *="" utf-8="" encoded="" strings="" and="" have="" a="" size="" limit="" of="" 1,000="" characters.="" *="" some="" examples="" of="" valid="" filters="" expressions:="" *="" *="" example="" 1:="" `lastmodifiedtime=""> "2012-04-23T18:25:43.511Z"
       *              lastModifiedTime < "2012-04-23t18:30:43.511z"`="" *="" *="" example="" 2:="" `lastmodifiedtime=""> "2012-04-23T18:25:43.511Z"
       *              productType = "variant"`
       *    * Example 3: `tag=("Red" OR "Blue") tag="New-Arrival"
       *              tag=(NOT "promotional")
       *              productType = "primary" lastModifiedTime < *="" "2018-04-23t18:30:43.511z"`="" *="" *="" example="" 4:="" `lastmodifiedtime=""> "2012-04-23T18:25:43.511Z"`
       *    * Example 5: `availability = (IN_STOCK OR BACKORDER)`
       */
      // const filter = 'abc123'
    
      // Imports the Retail library
      const {ProductServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callExportProducts() {
        // Construct request
        const request = {
          parent,
          outputConfig,
        };
    
        // Run request
        const [operation] = await retailClient.exportProducts(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportProducts();
    
    

### exportProducts(request, options, callback)
    
    
    exportProducts(request: protos.google.cloud.retail.v2alpha.IExportProductsRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.retail.v2alpha.IExportProductsResponse, protos.google.cloud.retail.v2alpha.IExportMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iexportproductsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.retail.v2alpha.IExportProductsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iexportproductsresponse), [protos.google.cloud.retail.v2alpha.IExportMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iexportmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportProducts(request, callback)
    
    
    exportProducts(request: protos.google.cloud.retail.v2alpha.IExportProductsRequest, callback: Callback<LROperation<protos.google.cloud.retail.v2alpha.IExportProductsResponse, protos.google.cloud.retail.v2alpha.IExportMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iexportproductsrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.retail.v2alpha.IExportProductsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iexportproductsresponse), [protos.google.cloud.retail.v2alpha.IExportMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iexportmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getLocation(request, options, callback)
    
    
    getLocation(request: LocationProtos.google.cloud.location.IGetLocationRequest, options?: gax.CallOptions | Callback<LocationProtos.google.cloud.location.ILocation, LocationProtos.google.cloud.location.IGetLocationRequest | null | undefined, {} | null | undefined>, callback?: Callback<LocationProtos.google.cloud.location.ILocation, LocationProtos.google.cloud.location.IGetLocationRequest | null | undefined, {} | null | undefined>): Promise<LocationProtos.google.cloud.location.ILocation>;

Gets information about a location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `LocationProtos.google.cloud.location.IGetLocationRequest`   
The request object that will be sent.  
`options` |  `CallOptions | Callback<google.cloud.location.ILocation, google.cloud.location.IGetLocationRequest | null | undefined, {} | null | undefined>`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
`callback` |  `Callback<google.cloud.location.ILocation, google.cloud.location.IGetLocationRequest | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`Promise<google.cloud.location.ILocation>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
    const [response] = await client.getLocation(request);
    

### getOperation(request, optionsOrCallback, callback)
    
    
    getOperation(request: protos.google.longrunning.GetOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>, callback?: Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>): Promise<[protos.google.longrunning.Operation]>;

Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)]>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    const name = '';
    const [response] = await client.getOperation({name});
    // doThingsWith(response)
    

### getProduct(request, options)
    
    
    getProduct(request?: protos.google.cloud.retail.v2alpha.IGetProductRequest, options?: CallOptions): Promise<[
            protos.google.cloud.retail.v2alpha.IProduct,
            protos.google.cloud.retail.v2alpha.IGetProductRequest | undefined,
            {} | undefined
        ]>;

Gets a .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.igetproductrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.retail.v2alpha.IProduct](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iproduct), [protos.google.cloud.retail.v2alpha.IGetProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.igetproductrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of
       *  Product google.cloud.retail.v2alpha.Product, such as
       *  `projects/* /locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`.
       *  If the caller does not have permission to access the
       *  Product google.cloud.retail.v2alpha.Product, regardless of whether or
       *  not it exists, a PERMISSION_DENIED error is returned.
       *  If the requested Product google.cloud.retail.v2alpha.Product  does not
       *  exist, a NOT_FOUND error is returned.
       */
      // const name = 'abc123'
    
      // Imports the Retail library
      const {ProductServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callGetProduct() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await retailClient.getProduct(request);
        console.log(response);
      }
    
      callGetProduct();
    
    

### getProduct(request, options, callback)
    
    
    getProduct(request: protos.google.cloud.retail.v2alpha.IGetProductRequest, options: CallOptions, callback: Callback<protos.google.cloud.retail.v2alpha.IProduct, protos.google.cloud.retail.v2alpha.IGetProductRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.igetproductrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2alpha.IProduct](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iproduct), [protos.google.cloud.retail.v2alpha.IGetProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.igetproductrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProduct(request, callback)
    
    
    getProduct(request: protos.google.cloud.retail.v2alpha.IGetProductRequest, callback: Callback<protos.google.cloud.retail.v2alpha.IProduct, protos.google.cloud.retail.v2alpha.IGetProductRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.igetproductrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2alpha.IProduct](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iproduct), [protos.google.cloud.retail.v2alpha.IGetProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.igetproductrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### importProducts(request, options)
    
    
    importProducts(request?: protos.google.cloud.retail.v2alpha.IImportProductsRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.retail.v2alpha.IImportProductsResponse, protos.google.cloud.retail.v2alpha.IImportMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Bulk import of multiple s.

Request processing may be synchronous. Non-existing items are created.

Note that it is possible for a subset of the s to be successfully updated.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iimportproductsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.retail.v2alpha.IImportProductsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iimportproductsresponse), [protos.google.cloud.retail.v2alpha.IImportMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iimportmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required.
       *  `projects/1234/locations/global/catalogs/default_catalog/branches/default_branch`
       *  If no updateMask is specified, requires products.create permission.
       *  If updateMask is specified, requires products.update permission.
       */
      // const parent = 'abc123'
      /**
       *  Required. The desired input location of the data.
       */
      // const inputConfig = {}
      /**
       *  The desired location of errors incurred during the Import.
       */
      // const errorsConfig = {}
      /**
       *  Indicates which fields in the provided imported `products` to update. If
       *  not set, all fields are updated. If provided, only the existing product
       *  fields are updated. Missing products will not be created.
       */
      // const updateMask = {}
      /**
       *  The mode of reconciliation between existing products and the products to be
       *  imported. Defaults to
       *  ReconciliationMode.INCREMENTAL google.cloud.retail.v2alpha.ImportProductsRequest.ReconciliationMode.INCREMENTAL.
       */
      // const reconciliationMode = {}
      /**
       *  Full Pub/Sub topic name for receiving notification. If this field is set,
       *  when the import is finished, a notification is sent to
       *  specified Pub/Sub topic. The message data is JSON string of a
       *  Operation google.longrunning.Operation.
       *  Format of the Pub/Sub topic is `projects/{project}/topics/{topic}`. It has
       *  to be within the same project as
       *  ImportProductsRequest.parent google.cloud.retail.v2alpha.ImportProductsRequest.parent.
       *  Make sure that both
       *  `cloud-retail-customer-data-access@system.gserviceaccount.com` and
       *  `service-

### importProducts(request, options, callback)
    
    
    importProducts(request: protos.google.cloud.retail.v2alpha.IImportProductsRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.retail.v2alpha.IImportProductsResponse, protos.google.cloud.retail.v2alpha.IImportMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iimportproductsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.retail.v2alpha.IImportProductsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iimportproductsresponse), [protos.google.cloud.retail.v2alpha.IImportMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iimportmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importProducts(request, callback)
    
    
    importProducts(request: protos.google.cloud.retail.v2alpha.IImportProductsRequest, callback: Callback<LROperation<protos.google.cloud.retail.v2alpha.IImportProductsResponse, protos.google.cloud.retail.v2alpha.IImportMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iimportproductsrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.retail.v2alpha.IImportProductsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iimportproductsresponse), [protos.google.cloud.retail.v2alpha.IImportMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iimportmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
  
### listLocationsAsync(request, options)
    
    
    listLocationsAsync(request: LocationProtos.google.cloud.location.IListLocationsRequest, options?: CallOptions): AsyncIterable<LocationProtos.google.cloud.location.ILocation>;

Lists information about the supported locations for this service. Returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `LocationProtos.google.cloud.location.IListLocationsRequest`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<google.cloud.location.ILocation>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
    const iterable = client.listLocationsAsync(request);
    for await (const response of iterable) {
      // process response
    }
    

### listOperationsAsync(request, options)
    
    
    listOperationsAsync(request: protos.google.longrunning.ListOperationsRequest, options?: gax.CallOptions): AsyncIterable<protos.google.longrunning.IOperation>;

Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. Returns an iterable object.

For-await-of syntax is used with the iterable to recursively get response element on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
**Example**
    
    
    const client = longrunning.operationsClient();
    for await (const response of client.listOperationsAsync(request));
    // doThingsWith(response)
    

### listProducts(request, options)
    
    
    listProducts(request?: protos.google.cloud.retail.v2alpha.IListProductsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.retail.v2alpha.IProduct[],
            protos.google.cloud.retail.v2alpha.IListProductsRequest | null,
            protos.google.cloud.retail.v2alpha.IListProductsResponse
        ]>;

Gets a list of s.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistproductsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.retail.v2alpha.IProduct](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iproduct)[], [protos.google.cloud.retail.v2alpha.IListProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistproductsrequest) | null, [protos.google.cloud.retail.v2alpha.IListProductsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistproductsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listProductsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listProducts(request, options, callback)
    
    
    listProducts(request: protos.google.cloud.retail.v2alpha.IListProductsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.retail.v2alpha.IListProductsRequest, protos.google.cloud.retail.v2alpha.IListProductsResponse | null | undefined, protos.google.cloud.retail.v2alpha.IProduct>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistproductsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.retail.v2alpha.IListProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistproductsrequest), [protos.google.cloud.retail.v2alpha.IListProductsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistproductsresponse) | null | undefined, [protos.google.cloud.retail.v2alpha.IProduct](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iproduct)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProducts(request, callback)
    
    
    listProducts(request: protos.google.cloud.retail.v2alpha.IListProductsRequest, callback: PaginationCallback<protos.google.cloud.retail.v2alpha.IListProductsRequest, protos.google.cloud.retail.v2alpha.IListProductsResponse | null | undefined, protos.google.cloud.retail.v2alpha.IProduct>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistproductsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.retail.v2alpha.IListProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistproductsrequest), [protos.google.cloud.retail.v2alpha.IListProductsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistproductsresponse) | null | undefined, [protos.google.cloud.retail.v2alpha.IProduct](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iproduct)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProductsAsync(request, options)
    
    
    listProductsAsync(request?: protos.google.cloud.retail.v2alpha.IListProductsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.retail.v2alpha.IProduct>;

Equivalent to `listProducts`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistproductsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.retail.v2alpha.IProduct](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iproduct)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent branch resource name, such as
       *  `projects/* /locations/global/catalogs/default_catalog/branches/0`. Use
       *  `default_branch` as the branch ID, to list products under the default
       *  branch.
       *  If the caller does not have permission to list
       *  Product google.cloud.retail.v2alpha.Product s under this branch,
       *  regardless of whether or not this branch exists, a PERMISSION_DENIED error
       *  is returned.
       */
      // const parent = 'abc123'
      /**
       *  Maximum number of Product google.cloud.retail.v2alpha.Product s to
       *  return. If unspecified, defaults to 100. The maximum allowed value is 1000.
       *  Values above 1000 will be coerced to 1000.
       *  If this field is negative, an INVALID_ARGUMENT error is returned.
       */
      // const pageSize = 1234
      /**
       *  A page token
       *  ListProductsResponse.next_page_token google.cloud.retail.v2alpha.ListProductsResponse.next_page_token,
       *  received from a previous
       *  ProductService.ListProducts google.cloud.retail.v2alpha.ProductService.ListProducts 
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  ProductService.ListProducts google.cloud.retail.v2alpha.ProductService.ListProducts 
       *  must match the call that provided the page token. Otherwise, an
       *  INVALID_ARGUMENT error is returned.
       */
      // const pageToken = 'abc123'
      /**
       *  A filter to apply on the list results. Supported features:
       *  * List all the products under the parent branch if
       *  filter google.cloud.retail.v2alpha.ListProductsRequest.filter  is unset.
       *  * List
       *  Product.Type.VARIANT google.cloud.retail.v2alpha.Product.Type.VARIANT 
       *  Product google.cloud.retail.v2alpha.Product s sharing the same
       *    Product.Type.PRIMARY google.cloud.retail.v2alpha.Product.Type.PRIMARY 
       *    Product google.cloud.retail.v2alpha.Product. For example:
       *      `primary_product_id = "some_product_id"`
       *  * List Product google.cloud.retail.v2alpha.Product s bundled in a
       *  Product.Type.COLLECTION google.cloud.retail.v2alpha.Product.Type.COLLECTION 
       *  Product google.cloud.retail.v2alpha.Product.
       *    For example:
       *      `collection_product_id = "some_product_id"`
       *  * List Product google.cloud.retail.v2alpha.Product s with a partibular
       *  type. For example:
       *      `type = "PRIMARY"`
       *      `type = "VARIANT"`
       *      `type = "COLLECTION"`
       *  If the field is unrecognizable, an INVALID_ARGUMENT error is returned.
       *  If the specified
       *  Product.Type.PRIMARY google.cloud.retail.v2alpha.Product.Type.PRIMARY 
       *  Product google.cloud.retail.v2alpha.Product  or
       *  Product.Type.COLLECTION google.cloud.retail.v2alpha.Product.Type.COLLECTION 
       *  Product google.cloud.retail.v2alpha.Product  does not exist, a NOT_FOUND
       *  error is returned.
       */
      // const filter = 'abc123'
      /**
       *  The fields of Product google.cloud.retail.v2alpha.Product  to return in
       *  the responses. If not set or empty, the following fields are returned:
       *  * Product.name google.cloud.retail.v2alpha.Product.name 
       *  * Product.id google.cloud.retail.v2alpha.Product.id 
       *  * Product.title google.cloud.retail.v2alpha.Product.title 
       *  * Product.uri google.cloud.retail.v2alpha.Product.uri 
       *  * Product.images google.cloud.retail.v2alpha.Product.images 
       *  * Product.price_info google.cloud.retail.v2alpha.Product.price_info 
       *  * Product.brands google.cloud.retail.v2alpha.Product.brands 
       *  If "*" is provided, all fields are returned.
       *  Product.name google.cloud.retail.v2alpha.Product.name  is always returned
       *  no matter what mask is set.
       *  If an unsupported or unknown field is provided, an INVALID_ARGUMENT error
       *  is returned.
       */
      // const readMask = {}
      /**
       *  If true and
       *  page_token google.cloud.retail.v2alpha.ListProductsRequest.page_token  is
       *  empty,
       *  ListProductsResponse.total_size google.cloud.retail.v2alpha.ListProductsResponse.total_size 
       *  is set to the total count of matched items irrespective of pagination.
       *  Notice that setting this field to true affects the performance.
       */
      // const requireTotalSize = true
    
      // Imports the Retail library
      const {ProductServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callListProducts() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = retailClient.listProductsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListProducts();
    
    

### listProductsStream(request, options)
    
    
    listProductsStream(request?: protos.google.cloud.retail.v2alpha.IListProductsRequest, options?: CallOptions): Transform;

Equivalent to `listProducts`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistproductsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listProductsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### loggingConfigPath(project)
    
    
    loggingConfigPath(project: string): string;

Return a fully-qualified loggingConfig resource name string.

**Parameter**  
---  
**Name** | **Description**  
`project` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### matchBranchFromBranchName(branchName)
    
    
    matchBranchFromBranchName(branchName: string): string | number;

Parse the branch from Branch resource.

**Parameter**  
---  
**Name** | **Description**  
`branchName` |  `string`   
A fully-qualified path representing Branch resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchBranchFromProductName(productName)
    
    
    matchBranchFromProductName(productName: string): string | number;

Parse the branch from Product resource.

**Parameter**  
---  
**Name** | **Description**  
`productName` |  `string`   
A fully-qualified path representing Product resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchCatalogFromAttributesConfigName(attributesConfigName)
    
    
    matchCatalogFromAttributesConfigName(attributesConfigName: string): string | number;

Parse the catalog from AttributesConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`attributesConfigName` |  `string`   
A fully-qualified path representing AttributesConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the catalog.  
  
### matchCatalogFromBranchName(branchName)
    
    
    matchCatalogFromBranchName(branchName: string): string | number;

Parse the catalog from Branch resource.

**Parameter**  
---  
**Name** | **Description**  
`branchName` |  `string`   
A fully-qualified path representing Branch resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the catalog.  
  
### matchCatalogFromCatalogName(catalogName)
    
    
    matchCatalogFromCatalogName(catalogName: string): string | number;

Parse the catalog from Catalog resource.

**Parameter**  
---  
**Name** | **Description**  
`catalogName` |  `string`   
A fully-qualified path representing Catalog resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the catalog.  
  
### matchCatalogFromCompletionConfigName(completionConfigName)
    
    
    matchCatalogFromCompletionConfigName(completionConfigName: string): string | number;

Parse the catalog from CompletionConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`completionConfigName` |  `string`   
A fully-qualified path representing CompletionConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the catalog.  
  
### matchCatalogFromControlName(controlName)
    
    
    matchCatalogFromControlName(controlName: string): string | number;

Parse the catalog from Control resource.

**Parameter**  
---  
**Name** | **Description**  
`controlName` |  `string`   
A fully-qualified path representing Control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the catalog.  
  
### matchCatalogFromMerchantCenterAccountLinkName(merchantCenterAccountLinkName)
    
    
    matchCatalogFromMerchantCenterAccountLinkName(merchantCenterAccountLinkName: string): string | number;

Parse the catalog from MerchantCenterAccountLink resource.

**Parameter**  
---  
**Name** | **Description**  
`merchantCenterAccountLinkName` |  `string`   
A fully-qualified path representing MerchantCenterAccountLink resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the catalog.  
  
### matchCatalogFromModelName(modelName)
    
    
    matchCatalogFromModelName(modelName: string): string | number;

Parse the catalog from Model resource.

**Parameter**  
---  
**Name** | **Description**  
`modelName` |  `string`   
A fully-qualified path representing Model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the catalog.  
  
### matchCatalogFromProductName(productName)
    
    
    matchCatalogFromProductName(productName: string): string | number;

Parse the catalog from Product resource.

**Parameter**  
---  
**Name** | **Description**  
`productName` |  `string`   
A fully-qualified path representing Product resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the catalog.  
  
### matchCatalogFromServingConfigName(servingConfigName)
    
    
    matchCatalogFromServingConfigName(servingConfigName: string): string | number;

Parse the catalog from ServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`servingConfigName` |  `string`   
A fully-qualified path representing ServingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the catalog.  
  
### matchControlFromControlName(controlName)
    
    
    matchControlFromControlName(controlName: string): string | number;

Parse the control from Control resource.

**Parameter**  
---  
**Name** | **Description**  
`controlName` |  `string`   
A fully-qualified path representing Control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the control.  
  
### matchLocationFromAttributesConfigName(attributesConfigName)
    
    
    matchLocationFromAttributesConfigName(attributesConfigName: string): string | number;

Parse the location from AttributesConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`attributesConfigName` |  `string`   
A fully-qualified path representing AttributesConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromBranchName(branchName)
    
    
    matchLocationFromBranchName(branchName: string): string | number;

Parse the location from Branch resource.

**Parameter**  
---  
**Name** | **Description**  
`branchName` |  `string`   
A fully-qualified path representing Branch resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromCatalogName(catalogName)
    
    
    matchLocationFromCatalogName(catalogName: string): string | number;

Parse the location from Catalog resource.

**Parameter**  
---  
**Name** | **Description**  
`catalogName` |  `string`   
A fully-qualified path representing Catalog resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromCompletionConfigName(completionConfigName)
    
    
    matchLocationFromCompletionConfigName(completionConfigName: string): string | number;

Parse the location from CompletionConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`completionConfigName` |  `string`   
A fully-qualified path representing CompletionConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromControlName(controlName)
    
    
    matchLocationFromControlName(controlName: string): string | number;

Parse the location from Control resource.

**Parameter**  
---  
**Name** | **Description**  
`controlName` |  `string`   
A fully-qualified path representing Control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromMerchantCenterAccountLinkName(merchantCenterAccountLinkName)
    
    
    matchLocationFromMerchantCenterAccountLinkName(merchantCenterAccountLinkName: string): string | number;

Parse the location from MerchantCenterAccountLink resource.

**Parameter**  
---  
**Name** | **Description**  
`merchantCenterAccountLinkName` |  `string`   
A fully-qualified path representing MerchantCenterAccountLink resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromModelName(modelName)
    
    
    matchLocationFromModelName(modelName: string): string | number;

Parse the location from Model resource.

**Parameter**  
---  
**Name** | **Description**  
`modelName` |  `string`   
A fully-qualified path representing Model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProductName(productName)
    
    
    matchLocationFromProductName(productName: string): string | number;

Parse the location from Product resource.

**Parameter**  
---  
**Name** | **Description**  
`productName` |  `string`   
A fully-qualified path representing Product resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromServingConfigName(servingConfigName)
    
    
    matchLocationFromServingConfigName(servingConfigName: string): string | number;

Parse the location from ServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`servingConfigName` |  `string`   
A fully-qualified path representing ServingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchMerchantCenterAccountLinkFromMerchantCenterAccountLinkName(merchantCenterAccountLinkName)
    
    
    matchMerchantCenterAccountLinkFromMerchantCenterAccountLinkName(merchantCenterAccountLinkName: string): string | number;

Parse the merchant_center_account_link from MerchantCenterAccountLink resource.

**Parameter**  
---  
**Name** | **Description**  
`merchantCenterAccountLinkName` |  `string`   
A fully-qualified path representing MerchantCenterAccountLink resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the merchant_center_account_link.  
  
### matchModelFromModelName(modelName)
    
    
    matchModelFromModelName(modelName: string): string | number;

Parse the model from Model resource.

**Parameter**  
---  
**Name** | **Description**  
`modelName` |  `string`   
A fully-qualified path representing Model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the model.  
  
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
  
### matchProjectFromAlertConfigName(alertConfigName)
    
    
    matchProjectFromAlertConfigName(alertConfigName: string): string | number;

Parse the project from AlertConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`alertConfigName` |  `string`   
A fully-qualified path representing AlertConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromAttributesConfigName(attributesConfigName)
    
    
    matchProjectFromAttributesConfigName(attributesConfigName: string): string | number;

Parse the project from AttributesConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`attributesConfigName` |  `string`   
A fully-qualified path representing AttributesConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromBranchName(branchName)
    
    
    matchProjectFromBranchName(branchName: string): string | number;

Parse the project from Branch resource.

**Parameter**  
---  
**Name** | **Description**  
`branchName` |  `string`   
A fully-qualified path representing Branch resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromCatalogName(catalogName)
    
    
    matchProjectFromCatalogName(catalogName: string): string | number;

Parse the project from Catalog resource.

**Parameter**  
---  
**Name** | **Description**  
`catalogName` |  `string`   
A fully-qualified path representing Catalog resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromCompletionConfigName(completionConfigName)
    
    
    matchProjectFromCompletionConfigName(completionConfigName: string): string | number;

Parse the project from CompletionConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`completionConfigName` |  `string`   
A fully-qualified path representing CompletionConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromControlName(controlName)
    
    
    matchProjectFromControlName(controlName: string): string | number;

Parse the project from Control resource.

**Parameter**  
---  
**Name** | **Description**  
`controlName` |  `string`   
A fully-qualified path representing Control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromLoggingConfigName(loggingConfigName)
    
    
    matchProjectFromLoggingConfigName(loggingConfigName: string): string | number;

Parse the project from LoggingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`loggingConfigName` |  `string`   
A fully-qualified path representing LoggingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromMerchantCenterAccountLinkName(merchantCenterAccountLinkName)
    
    
    matchProjectFromMerchantCenterAccountLinkName(merchantCenterAccountLinkName: string): string | number;

Parse the project from MerchantCenterAccountLink resource.

**Parameter**  
---  
**Name** | **Description**  
`merchantCenterAccountLinkName` |  `string`   
A fully-qualified path representing MerchantCenterAccountLink resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromModelName(modelName)
    
    
    matchProjectFromModelName(modelName: string): string | number;

Parse the project from Model resource.

**Parameter**  
---  
**Name** | **Description**  
`modelName` |  `string`   
A fully-qualified path representing Model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProductName(productName)
    
    
    matchProjectFromProductName(productName: string): string | number;

Parse the project from Product resource.

**Parameter**  
---  
**Name** | **Description**  
`productName` |  `string`   
A fully-qualified path representing Product resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromRetailProjectName(retailProjectName)
    
    
    matchProjectFromRetailProjectName(retailProjectName: string): string | number;

Parse the project from RetailProject resource.

**Parameter**  
---  
**Name** | **Description**  
`retailProjectName` |  `string`   
A fully-qualified path representing RetailProject resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromServingConfigName(servingConfigName)
    
    
    matchProjectFromServingConfigName(servingConfigName: string): string | number;

Parse the project from ServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`servingConfigName` |  `string`   
A fully-qualified path representing ServingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchServingConfigFromServingConfigName(servingConfigName)
    
    
    matchServingConfigFromServingConfigName(servingConfigName: string): string | number;

Parse the serving_config from ServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`servingConfigName` |  `string`   
A fully-qualified path representing ServingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the serving_config.  
  
### merchantCenterAccountLinkPath(project, location, catalog, merchantCenterAccountLink)
    
    
    merchantCenterAccountLinkPath(project: string, location: string, catalog: string, merchantCenterAccountLink: string): string;

Return a fully-qualified merchantCenterAccountLink resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`catalog` |  `string`   
  
`merchantCenterAccountLink` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### modelPath(project, location, catalog, model)
    
    
    modelPath(project: string, location: string, catalog: string, model: string): string;

Return a fully-qualified model resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`catalog` |  `string`   
  
`model` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### productPath(project, location, catalog, branch, product)
    
    
    productPath(project: string, location: string, catalog: string, branch: string, product: string): string;

Return a fully-qualified product resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`catalog` |  `string`   
  
`branch` |  `string`   
  
`product` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### purgeProducts(request, options)
    
    
    purgeProducts(request?: protos.google.cloud.retail.v2alpha.IPurgeProductsRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.retail.v2alpha.IPurgeProductsResponse, protos.google.cloud.retail.v2alpha.IPurgeProductsMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Permanently deletes all selected s under a branch.

This process is asynchronous. If the request is valid, the removal will be enqueued and processed offline. Depending on the number of s, this operation could take hours to complete. Before the operation completes, some s may still be returned by or .

Depending on the number of s, this operation could take hours to complete. To get a sample of s that would be deleted, set [PurgeProductsRequest.force](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.purgeproductsrequest) to false.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPurgeProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ipurgeproductsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.retail.v2alpha.IPurgeProductsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ipurgeproductsresponse), [protos.google.cloud.retail.v2alpha.IPurgeProductsMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ipurgeproductsmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the branch under which the products are
       *  created. The format is
       *  `projects/${projectId}/locations/global/catalogs/${catalogId}/branches/${branchId}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The filter string to specify the products to be deleted with a
       *  length limit of 5,000 characters.
       *  Empty string filter is not allowed. "*" implies delete all items in a
       *  branch.
       *  The eligible fields for filtering are:
       *  * `availability`: Double quoted
       *  Product.availability google.cloud.retail.v2alpha.Product.availability 
       *  string.
       *  * `create_time` : in ISO 8601 "zulu" format.
       *  Supported syntax:
       *  * Comparators (">", "<", "="">=", "<=", "=").
       *    Examples:
       *    * create_time <= " 2015-02-13t17:05:46z"="" *="" *="" availability="IN_STOCK" *="" *="" conjunctions="" ("and")="" *="" examples:="" *="" *="" create_time=""><= "2015-02-13t17:05:46z"="" and="" availability="PREORDER" *="" *="" disjunctions="" ("or")="" *="" examples:="" *="" *="" create_time=""><= "2015-02-13t17:05:46z"="" or="" availability="IN_STOCK" *="" *="" can="" support="" nested="" queries.="" *="" examples:="" *="" *="" (create_time=""><= "2015-02-13t17:05:46z"="" and="" availability="PREORDER" )="" *="" or="" (create_time="">= "2015-02-14T13:03:32Z" AND availability = "IN_STOCK")
       *  * Filter Limits:
       *    * Filter should not contain more than 6 conditions.
       *    * Max nesting depth should not exceed 2 levels.
       *  Examples queries:
       *  * Delete back order products created before a timestamp.
       *    create_time <= "2015-02-13t17:05:46z"="" or="" availability="BACKORDER" */="" const="" filter='abc123' *="" *="" actually="" perform="" the="" purge.="" *="" if="" `force`="" is="" set="" to="" false,="" the="" method="" will="" return="" the="" expected="" purge="" count="" *="" without="" deleting="" any="" products.="" */="" const="" force="true" imports="" the="" retail="" library="" const="" {productserviceclient}="require('@google-cloud/retail').v2alpha;" instantiates="" a="" client="" const="" retailclient="new" productserviceclient();="" async="" function="" callpurgeproducts()="" {="" construct="" request="" const="" request="{" parent,="" filter,="" };="" run="" request="" const="" [operation]="await" retailclient.purgeproducts(request);="" const="" [response]="await" operation.promise();="" console.log(response);="" }="" callpurgeproducts();="">

### purgeProducts(request, options, callback)
    
    
    purgeProducts(request: protos.google.cloud.retail.v2alpha.IPurgeProductsRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.retail.v2alpha.IPurgeProductsResponse, protos.google.cloud.retail.v2alpha.IPurgeProductsMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPurgeProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ipurgeproductsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.retail.v2alpha.IPurgeProductsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ipurgeproductsresponse), [protos.google.cloud.retail.v2alpha.IPurgeProductsMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ipurgeproductsmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### purgeProducts(request, callback)
    
    
    purgeProducts(request: protos.google.cloud.retail.v2alpha.IPurgeProductsRequest, callback: Callback<LROperation<protos.google.cloud.retail.v2alpha.IPurgeProductsResponse, protos.google.cloud.retail.v2alpha.IPurgeProductsMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPurgeProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ipurgeproductsrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.retail.v2alpha.IPurgeProductsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ipurgeproductsresponse), [protos.google.cloud.retail.v2alpha.IPurgeProductsMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ipurgeproductsmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeFulfillmentPlaces(request, options)
    
    
    removeFulfillmentPlaces(request?: protos.google.cloud.retail.v2alpha.IRemoveFulfillmentPlacesRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.retail.v2alpha.IRemoveFulfillmentPlacesResponse, protos.google.cloud.retail.v2alpha.IRemoveFulfillmentPlacesMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

We recommend that you use the method instead of the method. achieves the same results but provides more fine-grained control over ingesting local inventory data.

Incrementally removes place IDs from a .

This process is asynchronous and does not require the to exist before updating fulfillment information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, the removed place IDs are not immediately manifested in the queried by or .

The returned [Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)s will be obsolete after 1 day, and API will return NOT_FOUND afterwards.

If conflicting updates are issued, the [Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)s associated with the stale updates will not be marked as [done](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation) until being obsolete.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveFulfillmentPlacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovefulfillmentplacesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.retail.v2alpha.IRemoveFulfillmentPlacesResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovefulfillmentplacesresponse), [protos.google.cloud.retail.v2alpha.IRemoveFulfillmentPlacesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovefulfillmentplacesmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of
       *  Product google.cloud.retail.v2alpha.Product, such as
       *  `projects/* /locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`.
       *  If the caller does not have permission to access the
       *  Product google.cloud.retail.v2alpha.Product, regardless of whether or
       *  not it exists, a PERMISSION_DENIED error is returned.
       */
      // const product = 'abc123'
      /**
       *  Required. The fulfillment type, including commonly used types (such as
       *  pickup in store and same day delivery), and custom types.
       *  Supported values:
       *  * "pickup-in-store"
       *  * "ship-to-store"
       *  * "same-day-delivery"
       *  * "next-day-delivery"
       *  * "custom-type-1"
       *  * "custom-type-2"
       *  * "custom-type-3"
       *  * "custom-type-4"
       *  * "custom-type-5"
       *  If this field is set to an invalid value other than these, an
       *  INVALID_ARGUMENT error is returned.
       *  This field directly corresponds to
       *  Product.fulfillment_info.type google.cloud.retail.v2alpha.FulfillmentInfo.type.
       */
      // const type = 'abc123'
      /**
       *  Required. The IDs for this
       *  type google.cloud.retail.v2alpha.RemoveFulfillmentPlacesRequest.type,
       *  such as the store IDs for "pickup-in-store" or the region IDs for
       *  "same-day-delivery", to be removed for this
       *  type google.cloud.retail.v2alpha.RemoveFulfillmentPlacesRequest.type.
       *  At least 1 value is required, and a maximum of 2000 values are allowed.
       *  Each value must be a string with a length limit of 10 characters, matching
       *  the pattern `[a-zA-Z0-9_-]+`, such as "store1" or "REGION-2". Otherwise, an
       *  INVALID_ARGUMENT error is returned.
       */
      // const placeIds = ['abc','def']
      /**
       *  The time when the fulfillment updates are issued, used to prevent
       *  out-of-order updates on fulfillment information. If not provided, the
       *  internal system time will be used.
       */
      // const removeTime = {}
      /**
       *  If set to true, and the Product google.cloud.retail.v2alpha.Product  is
       *  not found, the fulfillment information will still be processed and retained
       *  for at most 1 day and processed once the
       *  Product google.cloud.retail.v2alpha.Product  is created. If set to false,
       *  a NOT_FOUND error is returned if the
       *  Product google.cloud.retail.v2alpha.Product  is not found.
       */
      // const allowMissing = true
    
      // Imports the Retail library
      const {ProductServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callRemoveFulfillmentPlaces() {
        // Construct request
        const request = {
          product,
          type,
          placeIds,
        };
    
        // Run request
        const [operation] = await retailClient.removeFulfillmentPlaces(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callRemoveFulfillmentPlaces();
    
    

### removeFulfillmentPlaces(request, options, callback)
    
    
    removeFulfillmentPlaces(request: protos.google.cloud.retail.v2alpha.IRemoveFulfillmentPlacesRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.retail.v2alpha.IRemoveFulfillmentPlacesResponse, protos.google.cloud.retail.v2alpha.IRemoveFulfillmentPlacesMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveFulfillmentPlacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovefulfillmentplacesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.retail.v2alpha.IRemoveFulfillmentPlacesResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovefulfillmentplacesresponse), [protos.google.cloud.retail.v2alpha.IRemoveFulfillmentPlacesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovefulfillmentplacesmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeFulfillmentPlaces(request, callback)
    
    
    removeFulfillmentPlaces(request: protos.google.cloud.retail.v2alpha.IRemoveFulfillmentPlacesRequest, callback: Callback<LROperation<protos.google.cloud.retail.v2alpha.IRemoveFulfillmentPlacesResponse, protos.google.cloud.retail.v2alpha.IRemoveFulfillmentPlacesMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveFulfillmentPlacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovefulfillmentplacesrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.retail.v2alpha.IRemoveFulfillmentPlacesResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovefulfillmentplacesresponse), [protos.google.cloud.retail.v2alpha.IRemoveFulfillmentPlacesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovefulfillmentplacesmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeLocalInventories(request, options)
    
    
    removeLocalInventories(request?: protos.google.cloud.retail.v2alpha.IRemoveLocalInventoriesRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.retail.v2alpha.IRemoveLocalInventoriesResponse, protos.google.cloud.retail.v2alpha.IRemoveLocalInventoriesMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Remove local inventory information for a at a list of places at a removal timestamp.

This process is asynchronous. If the request is valid, the removal will be enqueued and processed downstream. As a consequence, when a response is returned, removals are not immediately manifested in the queried by or .

Local inventory information can only be removed using this method. and has no effect on local inventories.

The returned [Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)s will be obsolete after 1 day, and API will return NOT_FOUND afterwards.

If conflicting updates are issued, the [Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)s associated with the stale updates will not be marked as [done](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation) until being obsolete.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveLocalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovelocalinventoriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.retail.v2alpha.IRemoveLocalInventoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovelocalinventoriesresponse), [protos.google.cloud.retail.v2alpha.IRemoveLocalInventoriesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovelocalinventoriesmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of
       *  Product google.cloud.retail.v2alpha.Product, such as
       *  `projects/* /locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`.
       *  If the caller does not have permission to access the
       *  Product google.cloud.retail.v2alpha.Product, regardless of whether or
       *  not it exists, a PERMISSION_DENIED error is returned.
       */
      // const product = 'abc123'
      /**
       *  Required. A list of place IDs to have their inventory deleted.
       *  At most 3000 place IDs are allowed per request.
       */
      // const placeIds = ['abc','def']
      /**
       *  The time when the inventory deletions are issued. Used to prevent
       *  out-of-order updates and deletions on local inventory fields. If not
       *  provided, the internal system time will be used.
       */
      // const removeTime = {}
      /**
       *  If set to true, and the Product google.cloud.retail.v2alpha.Product  is
       *  not found, the local inventory removal request will still be processed and
       *  retained for at most 1 day and processed once the
       *  Product google.cloud.retail.v2alpha.Product  is created. If set to false,
       *  a NOT_FOUND error is returned if the
       *  Product google.cloud.retail.v2alpha.Product  is not found.
       */
      // const allowMissing = true
    
      // Imports the Retail library
      const {ProductServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callRemoveLocalInventories() {
        // Construct request
        const request = {
          product,
          placeIds,
        };
    
        // Run request
        const [operation] = await retailClient.removeLocalInventories(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callRemoveLocalInventories();
    
    

### removeLocalInventories(request, options, callback)
    
    
    removeLocalInventories(request: protos.google.cloud.retail.v2alpha.IRemoveLocalInventoriesRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.retail.v2alpha.IRemoveLocalInventoriesResponse, protos.google.cloud.retail.v2alpha.IRemoveLocalInventoriesMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveLocalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovelocalinventoriesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.retail.v2alpha.IRemoveLocalInventoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovelocalinventoriesresponse), [protos.google.cloud.retail.v2alpha.IRemoveLocalInventoriesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovelocalinventoriesmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeLocalInventories(request, callback)
    
    
    removeLocalInventories(request: protos.google.cloud.retail.v2alpha.IRemoveLocalInventoriesRequest, callback: Callback<LROperation<protos.google.cloud.retail.v2alpha.IRemoveLocalInventoriesResponse, protos.google.cloud.retail.v2alpha.IRemoveLocalInventoriesMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveLocalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovelocalinventoriesrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.retail.v2alpha.IRemoveLocalInventoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovelocalinventoriesresponse), [protos.google.cloud.retail.v2alpha.IRemoveLocalInventoriesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iremovelocalinventoriesmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### retailProjectPath(project)
    
    
    retailProjectPath(project: string): string;

Return a fully-qualified retailProject resource name string.

**Parameter**  
---  
**Name** | **Description**  
`project` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### servingConfigPath(project, location, catalog, servingConfig)
    
    
    servingConfigPath(project: string, location: string, catalog: string, servingConfig: string): string;

Return a fully-qualified servingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`catalog` |  `string`   
  
`servingConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### setInventory(request, options)
    
    
    setInventory(request?: protos.google.cloud.retail.v2alpha.ISetInventoryRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.retail.v2alpha.ISetInventoryResponse, protos.google.cloud.retail.v2alpha.ISetInventoryMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates inventory information for a while respecting the last update timestamps of each inventory field.

This process is asynchronous and does not require the to exist before updating fulfillment information. If the request is valid, the update is enqueued and processed downstream. As a consequence, when a response is returned, updates are not immediately manifested in the queried by or .

When inventory is updated with and , the specified inventory field value(s) overwrite any existing value(s) while ignoring the last update time for this field. Furthermore, the last update times for the specified inventory fields are overwritten by the times of the or request.

If no inventory fields are set in [CreateProductRequest.product](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.createproductrequest), then any pre-existing inventory information for this product is used.

If no inventory fields are set in , then any existing inventory information is preserved.

Pre-existing inventory information can only be updated with , , and .

The returned [Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)s is obsolete after one day, and the API returns `NOT_FOUND` afterwards.

If conflicting updates are issued, the [Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)s associated with the stale updates are not marked as [done](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation) until they are obsolete.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.isetinventoryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.retail.v2alpha.ISetInventoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.isetinventoryresponse), [protos.google.cloud.retail.v2alpha.ISetInventoryMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.isetinventorymetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The inventory information to update. The allowable fields to
       *  update are:
       *  * Product.price_info google.cloud.retail.v2alpha.Product.price_info 
       *  * Product.availability google.cloud.retail.v2alpha.Product.availability 
       *  * Product.available_quantity google.cloud.retail.v2alpha.Product.available_quantity 
       *  * Product.fulfillment_info google.cloud.retail.v2alpha.Product.fulfillment_info 
       *  The updated inventory fields must be specified in
       *  SetInventoryRequest.set_mask google.cloud.retail.v2alpha.SetInventoryRequest.set_mask.
       *  If
       *  SetInventoryRequest.inventory.name google.cloud.retail.v2alpha.Product.name 
       *  is empty or invalid, an INVALID_ARGUMENT error is returned.
       *  If the caller does not have permission to update the
       *  Product google.cloud.retail.v2alpha.Product  named in
       *  Product.name google.cloud.retail.v2alpha.Product.name, regardless of
       *  whether or not it exists, a PERMISSION_DENIED error is returned.
       *  If the Product google.cloud.retail.v2alpha.Product  to update does not
       *  have existing inventory information, the provided inventory information
       *  will be inserted.
       *  If the Product google.cloud.retail.v2alpha.Product  to update has
       *  existing inventory information, the provided inventory information will be
       *  merged while respecting the last update time for each inventory field,
       *  using the provided or default value for
       *  SetInventoryRequest.set_time google.cloud.retail.v2alpha.SetInventoryRequest.set_time.
       *  The caller can replace place IDs for a subset of fulfillment types in the
       *  following ways:
       *  * Adds "fulfillment_info" in
       *  SetInventoryRequest.set_mask google.cloud.retail.v2alpha.SetInventoryRequest.set_mask 
       *  * Specifies only the desired fulfillment types and corresponding place IDs
       *  to update in
       *  SetInventoryRequest.inventory.fulfillment_info google.cloud.retail.v2alpha.Product.fulfillment_info 
       *  The caller can clear all place IDs from a subset of fulfillment types in
       *  the following ways:
       *  * Adds "fulfillment_info" in
       *  SetInventoryRequest.set_mask google.cloud.retail.v2alpha.SetInventoryRequest.set_mask 
       *  * Specifies only the desired fulfillment types to clear in
       *  SetInventoryRequest.inventory.fulfillment_info google.cloud.retail.v2alpha.Product.fulfillment_info 
       *  * Checks that only the desired fulfillment info types have empty
       *  SetInventoryRequest.inventory.fulfillment_info.place_ids google.cloud.retail.v2alpha.FulfillmentInfo.place_ids 
       *  The last update time is recorded for the following inventory fields:
       *  * Product.price_info google.cloud.retail.v2alpha.Product.price_info 
       *  * Product.availability google.cloud.retail.v2alpha.Product.availability 
       *  * Product.available_quantity google.cloud.retail.v2alpha.Product.available_quantity 
       *  * Product.fulfillment_info google.cloud.retail.v2alpha.Product.fulfillment_info 
       *  If a full overwrite of inventory information while ignoring timestamps is
       *  needed,
       *  ProductService.UpdateProduct google.cloud.retail.v2alpha.ProductService.UpdateProduct 
       *  should be invoked instead.
       */
      // const inventory = {}
      /**
       *  Indicates which inventory fields in the provided
       *  Product google.cloud.retail.v2alpha.Product  to update.
       *  At least one field must be provided.
       *  If an unsupported or unknown field is provided, an INVALID_ARGUMENT error
       *  is returned and the entire update will be ignored.
       */
      // const setMask = {}
      /**
       *  The time when the request is issued, used to prevent
       *  out-of-order updates on inventory fields with the last update time
       *  recorded. If not provided, the internal system time will be used.
       */
      // const setTime = {}
      /**
       *  If set to true, and the Product google.cloud.retail.v2alpha.Product  with
       *  name Product.name google.cloud.retail.v2alpha.Product.name  is not found,
       *  the inventory update will still be processed and retained for at most 1 day
       *  until the Product google.cloud.retail.v2alpha.Product  is created. If set
       *  to false, a NOT_FOUND error is returned if the
       *  Product google.cloud.retail.v2alpha.Product  is not found.
       */
      // const allowMissing = true
    
      // Imports the Retail library
      const {ProductServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callSetInventory() {
        // Construct request
        const request = {
          inventory,
        };
    
        // Run request
        const [operation] = await retailClient.setInventory(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callSetInventory();
    
    

### setInventory(request, options, callback)
    
    
    setInventory(request: protos.google.cloud.retail.v2alpha.ISetInventoryRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.retail.v2alpha.ISetInventoryResponse, protos.google.cloud.retail.v2alpha.ISetInventoryMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.isetinventoryrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.retail.v2alpha.ISetInventoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.isetinventoryresponse), [protos.google.cloud.retail.v2alpha.ISetInventoryMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.isetinventorymetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setInventory(request, callback)
    
    
    setInventory(request: protos.google.cloud.retail.v2alpha.ISetInventoryRequest, callback: Callback<LROperation<protos.google.cloud.retail.v2alpha.ISetInventoryResponse, protos.google.cloud.retail.v2alpha.ISetInventoryMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.isetinventoryrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.retail.v2alpha.ISetInventoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.isetinventoryresponse), [protos.google.cloud.retail.v2alpha.ISetInventoryMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.isetinventorymetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateProduct(request, options)
    
    
    updateProduct(request?: protos.google.cloud.retail.v2alpha.IUpdateProductRequest, options?: CallOptions): Promise<[
            protos.google.cloud.retail.v2alpha.IProduct,
            protos.google.cloud.retail.v2alpha.IUpdateProductRequest | undefined,
            {} | undefined
        ]>;

Updates a .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iupdateproductrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.retail.v2alpha.IProduct](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iproduct), [protos.google.cloud.retail.v2alpha.IUpdateProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iupdateproductrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The product to update/create.
       *  If the caller does not have permission to update the
       *  Product google.cloud.retail.v2alpha.Product, regardless of whether or
       *  not it exists, a PERMISSION_DENIED error is returned.
       *  If the Product google.cloud.retail.v2alpha.Product  to update does not
       *  exist and
       *  allow_missing google.cloud.retail.v2alpha.UpdateProductRequest.allow_missing 
       *  is not set, a NOT_FOUND error is returned.
       */
      // const product = {}
      /**
       *  Indicates which fields in the provided
       *  Product google.cloud.retail.v2alpha.Product  to update. The immutable and
       *  output only fields are NOT supported. If not set, all supported fields (the
       *  fields that are neither immutable nor output only) are updated.
       *  If an unsupported or unknown field is provided, an INVALID_ARGUMENT error
       *  is returned.
       *  The attribute key can be updated by setting the mask path as
       *  "attributes.${key_name}". If a key name is present in the mask but not in
       *  the patching product from the request, this key will be deleted after the
       *  update.
       */
      // const updateMask = {}
      /**
       *  If set to true, and the Product google.cloud.retail.v2alpha.Product  is
       *  not found, a new Product google.cloud.retail.v2alpha.Product  will be
       *  created. In this situation, `update_mask` is ignored.
       */
      // const allowMissing = true
    
      // Imports the Retail library
      const {ProductServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callUpdateProduct() {
        // Construct request
        const request = {
          product,
        };
    
        // Run request
        const response = await retailClient.updateProduct(request);
        console.log(response);
      }
    
      callUpdateProduct();
    
    

### updateProduct(request, options, callback)
    
    
    updateProduct(request: protos.google.cloud.retail.v2alpha.IUpdateProductRequest, options: CallOptions, callback: Callback<protos.google.cloud.retail.v2alpha.IProduct, protos.google.cloud.retail.v2alpha.IUpdateProductRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iupdateproductrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2alpha.IProduct](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iproduct), [protos.google.cloud.retail.v2alpha.IUpdateProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iupdateproductrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateProduct(request, callback)
    
    
    updateProduct(request: protos.google.cloud.retail.v2alpha.IUpdateProductRequest, callback: Callback<protos.google.cloud.retail.v2alpha.IProduct, protos.google.cloud.retail.v2alpha.IUpdateProductRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iupdateproductrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2alpha.IProduct](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iproduct), [protos.google.cloud.retail.v2alpha.IUpdateProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iupdateproductrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
