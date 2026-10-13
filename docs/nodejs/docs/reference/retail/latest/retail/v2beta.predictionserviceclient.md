---
url: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/v2beta.predictionserviceclient
title: Class v2beta.PredictionServiceClient (5.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:02:40.915766+00:00
---

# Class v2beta.PredictionServiceClient (5.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/v2beta.predictionserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v2beta.PredictionServiceClient (5.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.4.0 (latest)  5.3.1  5.0.1  4.4.0  4.3.0  3.6.0  3.5.0  3.1.0  2.4.1  2.3.1  2.1.1  2.0.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.2  1.1.6 

Service for making recommendation prediction. v2beta

## Package

[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of PredictionServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new PredictionServiceClient({fallback: true}, gax); ```  
  
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

### predictionServiceStub
    
    
    predictionServiceStub?: Promise<{
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
  
### predict(request, options)
    
    
    predict(request?: protos.google.cloud.retail.v2beta.IPredictRequest, options?: CallOptions): Promise<[
            protos.google.cloud.retail.v2beta.IPredictResponse,
            protos.google.cloud.retail.v2beta.IPredictRequest | undefined,
            {} | undefined
        ]>;

Makes a recommendation prediction.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPredictRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ipredictrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.retail.v2beta.IPredictResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ipredictresponse), [protos.google.cloud.retail.v2beta.IPredictRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ipredictrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of the format:
       *  `{placement=projects/* /locations/global/catalogs/default_catalog/servingConfigs/*}`
       *  or
       *  `{placement=projects/* /locations/global/catalogs/default_catalog/placements/*}`.
       *  We recommend using the `servingConfigs` resource. `placements` is a legacy
       *  resource.
       *  The ID of the Recommendations AI serving config or placement.
       *  Before you can request predictions from your model, you must create at
       *  least one serving config or placement for it. For more information, see
       *  Manage serving configs 
       *  (https://cloud.google.com/retail/docs/manage-configs).
       *  The full list of available serving configs can be seen at
       *  https://console.cloud.google.com/ai/retail/catalogs/default_catalog/configs
       */
      // const placement = 'abc123'
      /**
       *  Required. Context about the user, what they are looking at and what action
       *  they took to trigger the predict request. Note that this user event detail
       *  won't be ingested to userEvent logs. Thus, a separate userEvent write
       *  request is required for event logging.
       *  Don't set
       *  UserEvent.visitor_id google.cloud.retail.v2beta.UserEvent.visitor_id  or
       *  UserInfo.user_id google.cloud.retail.v2beta.UserInfo.user_id  to the same
       *  fixed ID for different users. If you are trying to receive non-personalized
       *  recommendations (not recommended; this can negatively impact model
       *  performance), instead set
       *  UserEvent.visitor_id google.cloud.retail.v2beta.UserEvent.visitor_id  to
       *  a random unique ID and leave
       *  UserInfo.user_id google.cloud.retail.v2beta.UserInfo.user_id  unset.
       */
      // const userEvent = {}
      /**
       *  Maximum number of results to return. Set this property to the number of
       *  prediction results needed. If zero, the service will choose a reasonable
       *  default. The maximum allowed value is 100. Values above 100 will be coerced
       *  to 100.
       */
      // const pageSize = 1234
      /**
       *  This field is not used; leave it unset.
       */
      // const pageToken = 'abc123'
      /**
       *  Filter for restricting prediction results with a length limit of 5,000
       *  characters. Accepts values for tags and the `filterOutOfStockItems` flag.
       *   * Tag expressions. Restricts predictions to products that match all of the
       *     specified tags. Boolean operators `OR` and `NOT` are supported if the
       *     expression is enclosed in parentheses, and must be separated from the
       *     tag values by a space. `-"tagA"` is also supported and is equivalent to
       *     `NOT "tagA"`. Tag values must be double quoted UTF-8 encoded strings
       *     with a size limit of 1,000 characters.
       *     Note: "Recently viewed" models don't support tag filtering at the
       *     moment.
       *   * filterOutOfStockItems. Restricts predictions to products that do not
       *   have a
       *     stockState value of OUT_OF_STOCK.
       *  Examples:
       *   * tag=("Red" OR "Blue") tag="New-Arrival" tag=(NOT "promotional")
       *   * filterOutOfStockItems  tag=(-"promotional")
       *   * filterOutOfStockItems
       *  If your filter blocks all prediction results, the API will return *no*
       *  results. If instead you want empty result sets to return generic
       *  (unfiltered) popular products, set `strictFiltering` to False in
       *  `PredictRequest.params`. Note that the API will never return items with
       *  storageStatus of "EXPIRED" or "DELETED" regardless of filter choices.
       *  If `filterSyntaxV2` is set to true under the `params` field, then
       *  attribute-based expressions are expected instead of the above described
       *  tag-based syntax. Examples:
       *   * (colors: ANY("Red", "Blue")) AND NOT (categories: ANY("Phones"))
       *   * (availability: ANY("IN_STOCK")) AND
       *     (colors: ANY("Red") OR categories: ANY("Phones"))
       *  For more information, see
       *  Filter recommendations (https://cloud.google.com/retail/docs/filter-recs).
       */
      // const filter = 'abc123'
      /**
       *  Use validate only mode for this prediction query. If set to true, a
       *  dummy model will be used that returns arbitrary products.
       *  Note that the validate only mode should only be used for testing the API,
       *  or if the model is not ready.
       */
      // const validateOnly = true
      /**
       *  Additional domain specific parameters for the predictions.
       *  Allowed values:
       *  * `returnProduct`: Boolean. If set to true, the associated product
       *     object will be returned in the `results.metadata` field in the
       *     prediction response.
       *  * `returnScore`: Boolean. If set to true, the prediction 'score'
       *     corresponding to each returned product will be set in the
       *     `results.metadata` field in the prediction response. The given
       *     'score' indicates the probability of a product being clicked/purchased
       *     given the user's context and history.
       *  * `strictFiltering`: Boolean. True by default. If set to false, the service
       *     will return generic (unfiltered) popular products instead of empty if
       *     your filter blocks all prediction results.
       *  * `priceRerankLevel`: String. Default empty. If set to be non-empty, then
       *     it needs to be one of {'no-price-reranking', 'low-price-reranking',
       *     'medium-price-reranking', 'high-price-reranking'}. This gives
       *     request-level control and adjusts prediction results based on product
       *     price.
       *  * `diversityLevel`: String. Default empty. If set to be non-empty, then
       *     it needs to be one of {'no-diversity', 'low-diversity',
       *     'medium-diversity', 'high-diversity', 'auto-diversity'}. This gives
       *     request-level control and adjusts prediction results based on product
       *     category.
       *  * `filterSyntaxV2`: Boolean. False by default. If set to true, the `filter`
       *    field is interpreteted according to the new, attribute-based syntax.
       */
      // const params = [1,2,3,4]
      /**
       *  The labels applied to a resource must meet the following requirements:
       *  * Each resource can have multiple labels, up to a maximum of 64.
       *  * Each label must be a key-value pair.
       *  * Keys have a minimum length of 1 character and a maximum length of 63
       *    characters and cannot be empty. Values can be empty and have a maximum
       *    length of 63 characters.
       *  * Keys and values can contain only lowercase letters, numeric characters,
       *    underscores, and dashes. All characters must use UTF-8 encoding, and
       *    international characters are allowed.
       *  * The key portion of a label must be unique. However, you can use the same
       *    key with multiple resources.
       *  * Keys must start with a lowercase letter or international character.
       *  See Google Cloud
       *  Document (https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements)
       *  for more details.
       */
      // const labels = [1,2,3,4]
    
      // Imports the Retail library
      const {PredictionServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const retailClient = new [PredictionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callPredict() {
        // Construct request
        const request = {
          placement,
          userEvent,
        };
    
        // Run request
        const response = await retailClient.predict(request);
        console.log(response);
      }
    
      callPredict();
    
    

### predict(request, options, callback)
    
    
    predict(request: protos.google.cloud.retail.v2beta.IPredictRequest, options: CallOptions, callback: Callback<protos.google.cloud.retail.v2beta.IPredictResponse, protos.google.cloud.retail.v2beta.IPredictRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPredictRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ipredictrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2beta.IPredictResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ipredictresponse), [protos.google.cloud.retail.v2beta.IPredictRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ipredictrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### predict(request, callback)
    
    
    predict(request: protos.google.cloud.retail.v2beta.IPredictRequest, callback: Callback<protos.google.cloud.retail.v2beta.IPredictResponse, protos.google.cloud.retail.v2beta.IPredictRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPredictRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ipredictrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2beta.IPredictResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ipredictresponse), [protos.google.cloud.retail.v2beta.IPredictRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ipredictrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
