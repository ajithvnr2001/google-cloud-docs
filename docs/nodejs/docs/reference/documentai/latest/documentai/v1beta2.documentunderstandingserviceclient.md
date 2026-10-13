---
url: https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/v1beta2.documentunderstandingserviceclient
title: Class v1beta2.DocumentUnderstandingServiceClient (9.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:44.036189+00:00
---

# Class v1beta2.DocumentUnderstandingServiceClient (9.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/v1beta2.documentunderstandingserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta2.DocumentUnderstandingServiceClient (9.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

10.1.1 (latest)  9.6.0  9.2.0  8.12.0  8.10.0  8.8.0  8.6.0  8.5.0  8.4.0  8.2.0  8.1.2  8.0.0  7.3.1  7.1.0  7.0.1  6.3.0  6.1.0  6.0.0  3.3.0  3.2.1  3.1.0  3.0.2  2.10.0 

Service to parse structured information from unstructured or semi-structured documents using state-of-the-art Google AI such as natural language, computer vision, and translation. v1beta2

## Package

[@google-cloud/documentai](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of DocumentUnderstandingServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new DocumentUnderstandingServiceClient({fallback: true}, gax); ```  
  
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

### documentUnderstandingServiceStub
    
    
    documentUnderstandingServiceStub?: Promise<{
            [name: string]: Function;
        }>;

### innerApiCalls
    
    
    innerApiCalls: {
            [name: string]: Function;
        };

### locationsClient
    
    
    locationsClient: LocationsClient;

### operationsClient
    
    
    operationsClient: gax.OperationsClient;

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

### batchProcessDocuments(request, options)
    
    
    batchProcessDocuments(request?: protos.google.cloud.documentai.v1beta2.IBatchProcessDocumentsRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.documentai.v1beta2.IBatchProcessDocumentsResponse, protos.google.cloud.documentai.v1beta2.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

LRO endpoint to batch process many documents. The output is written to Cloud Storage as JSON in the [Document] format.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchProcessDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1beta2.ibatchprocessdocumentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.documentai.v1beta2.IBatchProcessDocumentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1beta2.ibatchprocessdocumentsresponse), [protos.google.cloud.documentai.v1beta2.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1beta2.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Individual requests for each document.
       */
      // const requests = [1,2,3,4]
      /**
       *  Target project and location to make a call.
       *  Format: `projects/{project-id}/locations/{location-id}`.
       *  If no location is specified, a region will be chosen automatically.
       */
      // const parent = 'abc123'
    
      // Imports the Documentai library
      const {DocumentUnderstandingServiceClient} = require('[@google-cloud/documentai](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)').v1beta2;
    
      // Instantiates a client
      const documentaiClient = new DocumentUnderstandingServiceClient();
    
      async function callBatchProcessDocuments() {
        // Construct request
        const request = {
          requests,
        };
    
        // Run request
        const [operation] = await documentaiClient.batchProcessDocuments(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callBatchProcessDocuments();
    
    

### batchProcessDocuments(request, options, callback)
    
    
    batchProcessDocuments(request: protos.google.cloud.documentai.v1beta2.IBatchProcessDocumentsRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.documentai.v1beta2.IBatchProcessDocumentsResponse, protos.google.cloud.documentai.v1beta2.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchProcessDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1beta2.ibatchprocessdocumentsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.documentai.v1beta2.IBatchProcessDocumentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1beta2.ibatchprocessdocumentsresponse), [protos.google.cloud.documentai.v1beta2.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1beta2.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchProcessDocuments(request, callback)
    
    
    batchProcessDocuments(request: protos.google.cloud.documentai.v1beta2.IBatchProcessDocumentsRequest, callback: Callback<LROperation<protos.google.cloud.documentai.v1beta2.IBatchProcessDocumentsResponse, protos.google.cloud.documentai.v1beta2.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchProcessDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1beta2.ibatchprocessdocumentsrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.documentai.v1beta2.IBatchProcessDocumentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1beta2.ibatchprocessdocumentsresponse), [protos.google.cloud.documentai.v1beta2.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1beta2.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelOperation(request, options, callback)
    
    
    cancelOperation(request: protos.google.longrunning.CancelOperationRequest, options?: gax.CallOptions | Callback<protos.google.protobuf.Empty, protos.google.longrunning.CancelOperationRequest, {} | undefined | null>, callback?: Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>): Promise<protos.google.protobuf.Empty>;

Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an value with a of 1, corresponding to `Code.CANCELLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.protobuf.empty), [protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.canceloperationrequest), {} | undefined | null>`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### checkBatchProcessDocumentsProgress(name)
    
    
    checkBatchProcessDocumentsProgress(name: string): Promise<LROperation<protos.google.cloud.documentai.v1beta2.BatchProcessDocumentsResponse, protos.google.cloud.documentai.v1beta2.OperationMetadata>>;

Check the status of the long running operation returned by `batchProcessDocuments()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.documentai.v1beta2.BatchProcessDocumentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1beta2.batchprocessdocumentsresponse), [protos.google.cloud.documentai.v1beta2.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1beta2.operationmetadata-class)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Individual requests for each document.
       */
      // const requests = [1,2,3,4]
      /**
       *  Target project and location to make a call.
       *  Format: `projects/{project-id}/locations/{location-id}`.
       *  If no location is specified, a region will be chosen automatically.
       */
      // const parent = 'abc123'
    
      // Imports the Documentai library
      const {DocumentUnderstandingServiceClient} = require('[@google-cloud/documentai](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)').v1beta2;
    
      // Instantiates a client
      const documentaiClient = new DocumentUnderstandingServiceClient();
    
      async function callBatchProcessDocuments() {
        // Construct request
        const request = {
          requests,
        };
    
        // Run request
        const [operation] = await documentaiClient.batchProcessDocuments(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callBatchProcessDocuments();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### deleteOperation(request, options, callback)
    
    
    deleteOperation(request: protos.google.longrunning.DeleteOperationRequest, options?: gax.CallOptions | Callback<protos.google.protobuf.Empty, protos.google.longrunning.DeleteOperationRequest, {} | null | undefined>, callback?: Callback<protos.google.protobuf.Empty, protos.google.longrunning.DeleteOperationRequest, {} | null | undefined>): Promise<protos.google.protobuf.Empty>;

Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.protobuf.empty)>` |   
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
    

### getOperation(request, options, callback)
    
    
    getOperation(request: protos.google.longrunning.GetOperationRequest, options?: gax.CallOptions | Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>, callback?: Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>): Promise<[protos.google.longrunning.Operation]>;

Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.operation)]>` |   
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
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
**Example**
    
    
    const client = longrunning.operationsClient();
    for await (const response of client.listOperationsAsync(request));
    // doThingsWith(response)
    

### processDocument(request, options)
    
    
    processDocument(request?: protos.google.cloud.documentai.v1beta2.IProcessDocumentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.documentai.v1beta2.IDocument,
            (protos.google.cloud.documentai.v1beta2.IProcessDocumentRequest | undefined),
            {} | undefined
        ]>;

Processes a single document.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IProcessDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1beta2.iprocessdocumentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.documentai.v1beta2.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1beta2.idocument), ([protos.google.cloud.documentai.v1beta2.IProcessDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1beta2.iprocessdocumentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Target project and location to make a call.
       *  Format: `projects/{project-id}/locations/{location-id}`.
       *  If no location is specified, a region will be chosen automatically.
       *  This field is only populated when used in ProcessDocument method.
       */
      // const parent = 'abc123'
      /**
       *  Required. Information about the input file.
       */
      // const inputConfig = {}
      /**
       *  The desired output location. This field is only needed in
       *  BatchProcessDocumentsRequest.
       */
      // const outputConfig = {}
      /**
       *  Specifies a known document type for deeper structure detection. Valid
       *  values are currently "general" and "invoice". If not provided, "general"\
       *  is used as default. If any other value is given, the request is rejected.
       */
      // const documentType = 'abc123'
      /**
       *  Controls table extraction behavior. If not specified, the system will
       *  decide reasonable defaults.
       */
      // const tableExtractionParams = {}
      /**
       *  Controls form extraction behavior. If not specified, the system will
       *  decide reasonable defaults.
       */
      // const formExtractionParams = {}
      /**
       *  Controls entity extraction behavior. If not specified, the system will
       *  decide reasonable defaults.
       */
      // const entityExtractionParams = {}
      /**
       *  Controls OCR behavior. If not specified, the system will decide reasonable
       *  defaults.
       */
      // const ocrParams = {}
      /**
       *  Controls AutoML model prediction behavior. AutoMlParams cannot be used
       *  together with other Params.
       */
      // const automlParams = {}
    
      // Imports the Documentai library
      const {DocumentUnderstandingServiceClient} = require('[@google-cloud/documentai](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)').v1beta2;
    
      // Instantiates a client
      const documentaiClient = new DocumentUnderstandingServiceClient();
    
      async function callProcessDocument() {
        // Construct request
        const request = {
          inputConfig,
        };
    
        // Run request
        const response = await documentaiClient.processDocument(request);
        console.log(response);
      }
    
      callProcessDocument();
    
    

### processDocument(request, options, callback)
    
    
    processDocument(request: protos.google.cloud.documentai.v1beta2.IProcessDocumentRequest, options: CallOptions, callback: Callback<protos.google.cloud.documentai.v1beta2.IDocument, protos.google.cloud.documentai.v1beta2.IProcessDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IProcessDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1beta2.iprocessdocumentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.documentai.v1beta2.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1beta2.idocument), [protos.google.cloud.documentai.v1beta2.IProcessDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1beta2.iprocessdocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### processDocument(request, callback)
    
    
    processDocument(request: protos.google.cloud.documentai.v1beta2.IProcessDocumentRequest, callback: Callback<protos.google.cloud.documentai.v1beta2.IDocument, protos.google.cloud.documentai.v1beta2.IProcessDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IProcessDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1beta2.iprocessdocumentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.documentai.v1beta2.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1beta2.idocument), [protos.google.cloud.documentai.v1beta2.IProcessDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1beta2.iprocessdocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
