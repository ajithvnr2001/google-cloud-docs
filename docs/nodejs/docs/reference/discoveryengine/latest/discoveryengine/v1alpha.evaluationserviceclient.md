---
url: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/v1alpha.evaluationserviceclient
title: Class v1alpha.EvaluationServiceClient (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:05:17.345513+00:00
---

# Class v1alpha.EvaluationServiceClient (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/v1alpha.evaluationserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1alpha.EvaluationServiceClient (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  3.3.0  3.1.0  2.9.0  2.8.0  2.6.0  2.2.0  2.0.1  1.14.0  1.10.0  1.9.0  1.7.0  1.6.0  1.4.1  1.3.1  1.2.0  1.0.0  0.6.0  0.5.0  0.3.1  0.2.0 

Service for managing s, v1alpha

## Package

[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of EvaluationServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new EvaluationServiceClient({fallback: true}, gax); ```  
  
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

### evaluationServiceStub
    
    
    evaluationServiceStub?: Promise<{
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

### aclConfigPath(project, location)
    
    
    aclConfigPath(project: string, location: string): string;

Return a fully-qualified aclConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
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
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### checkCreateEvaluationProgress(name)
    
    
    checkCreateEvaluationProgress(name: string): Promise<LROperation<protos.google.cloud.discoveryengine.v1alpha.Evaluation, protos.google.cloud.discoveryengine.v1alpha.CreateEvaluationMetadata>>;

Check the status of the long running operation returned by `createEvaluation()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.discoveryengine.v1alpha.Evaluation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.evaluation-class), [protos.google.cloud.discoveryengine.v1alpha.CreateEvaluationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.createevaluationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource name, such as
       *  `projects/{project}/locations/{location}`.
       */
      // const parent = 'abc123'
      /**
       *  Required. The Evaluation google.cloud.discoveryengine.v1alpha.Evaluation 
       *  to create.
       */
      // const evaluation = {}
    
      // Imports the Discoveryengine library
      const {EvaluationServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new EvaluationServiceClient();
    
      async function callCreateEvaluation() {
        // Construct request
        const request = {
          parent,
          evaluation,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.createEvaluation(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateEvaluation();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### createEvaluation(request, options)
    
    
    createEvaluation(request?: protos.google.cloud.discoveryengine.v1alpha.ICreateEvaluationRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.discoveryengine.v1alpha.IEvaluation, protos.google.cloud.discoveryengine.v1alpha.ICreateEvaluationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a .

Upon creation, the evaluation will be automatically triggered and begin execution.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.icreateevaluationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.discoveryengine.v1alpha.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ievaluation), [protos.google.cloud.discoveryengine.v1alpha.ICreateEvaluationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.icreateevaluationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource name, such as
       *  `projects/{project}/locations/{location}`.
       */
      // const parent = 'abc123'
      /**
       *  Required. The Evaluation google.cloud.discoveryengine.v1alpha.Evaluation 
       *  to create.
       */
      // const evaluation = {}
    
      // Imports the Discoveryengine library
      const {EvaluationServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new EvaluationServiceClient();
    
      async function callCreateEvaluation() {
        // Construct request
        const request = {
          parent,
          evaluation,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.createEvaluation(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateEvaluation();
    
    

### createEvaluation(request, options, callback)
    
    
    createEvaluation(request: protos.google.cloud.discoveryengine.v1alpha.ICreateEvaluationRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.discoveryengine.v1alpha.IEvaluation, protos.google.cloud.discoveryengine.v1alpha.ICreateEvaluationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.icreateevaluationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.discoveryengine.v1alpha.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ievaluation), [protos.google.cloud.discoveryengine.v1alpha.ICreateEvaluationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.icreateevaluationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEvaluation(request, callback)
    
    
    createEvaluation(request: protos.google.cloud.discoveryengine.v1alpha.ICreateEvaluationRequest, callback: Callback<LROperation<protos.google.cloud.discoveryengine.v1alpha.IEvaluation, protos.google.cloud.discoveryengine.v1alpha.ICreateEvaluationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.icreateevaluationrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.discoveryengine.v1alpha.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ievaluation), [protos.google.cloud.discoveryengine.v1alpha.ICreateEvaluationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.icreateevaluationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### enginePath(project, location, collection, engine)
    
    
    enginePath(project: string, location: string, collection: string, engine: string): string;

Return a fully-qualified engine resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### evaluationPath(project, location, evaluation)
    
    
    evaluationPath(project: string, location: string, evaluation: string): string;

Return a fully-qualified evaluation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`evaluation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### getEvaluation(request, options)
    
    
    getEvaluation(request?: protos.google.cloud.discoveryengine.v1alpha.IGetEvaluationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1alpha.IEvaluation,
            (protos.google.cloud.discoveryengine.v1alpha.IGetEvaluationRequest | undefined),
            {} | undefined
        ]>;

Gets a .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igetevaluationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1alpha.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ievaluation), ([protos.google.cloud.discoveryengine.v1alpha.IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igetevaluationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of
       *  Evaluation google.cloud.discoveryengine.v1alpha.Evaluation, such as
       *  `projects/{project}/locations/{location}/evaluations/{evaluation}`.
       *  If the caller does not have permission to access the
       *  Evaluation google.cloud.discoveryengine.v1alpha.Evaluation, regardless
       *  of whether or not it exists, a PERMISSION_DENIED error is returned.
       *  If the requested
       *  Evaluation google.cloud.discoveryengine.v1alpha.Evaluation  does not
       *  exist, a NOT_FOUND error is returned.
       */
      // const name = 'abc123'
    
      // Imports the Discoveryengine library
      const {EvaluationServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new EvaluationServiceClient();
    
      async function callGetEvaluation() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await discoveryengineClient.getEvaluation(request);
        console.log(response);
      }
    
      callGetEvaluation();
    
    

### getEvaluation(request, options, callback)
    
    
    getEvaluation(request: protos.google.cloud.discoveryengine.v1alpha.IGetEvaluationRequest, options: CallOptions, callback: Callback<protos.google.cloud.discoveryengine.v1alpha.IEvaluation, protos.google.cloud.discoveryengine.v1alpha.IGetEvaluationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igetevaluationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1alpha.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ievaluation), [protos.google.cloud.discoveryengine.v1alpha.IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igetevaluationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEvaluation(request, callback)
    
    
    getEvaluation(request: protos.google.cloud.discoveryengine.v1alpha.IGetEvaluationRequest, callback: Callback<protos.google.cloud.discoveryengine.v1alpha.IEvaluation, protos.google.cloud.discoveryengine.v1alpha.IGetEvaluationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igetevaluationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1alpha.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ievaluation), [protos.google.cloud.discoveryengine.v1alpha.IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igetevaluationrequest) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.operation)]>` |   
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
  
### listEvaluationResults(request, options)
    
    
    listEvaluationResults(request?: protos.google.cloud.discoveryengine.v1alpha.IListEvaluationResultsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1alpha.ListEvaluationResultsResponse.IEvaluationResult[],
            protos.google.cloud.discoveryengine.v1alpha.IListEvaluationResultsRequest | null,
            protos.google.cloud.discoveryengine.v1alpha.IListEvaluationResultsResponse
        ]>;

Gets a list of results for a given a .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationresultsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1alpha.ListEvaluationResultsResponse.IEvaluationResult](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.listevaluationresultsresponse.ievaluationresult)[], [protos.google.cloud.discoveryengine.v1alpha.IListEvaluationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationresultsrequest) | null, [protos.google.cloud.discoveryengine.v1alpha.IListEvaluationResultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationresultsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listEvaluationResultsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listEvaluationResults(request, options, callback)
    
    
    listEvaluationResults(request: protos.google.cloud.discoveryengine.v1alpha.IListEvaluationResultsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.discoveryengine.v1alpha.IListEvaluationResultsRequest, protos.google.cloud.discoveryengine.v1alpha.IListEvaluationResultsResponse | null | undefined, protos.google.cloud.discoveryengine.v1alpha.ListEvaluationResultsResponse.IEvaluationResult>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationresultsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.discoveryengine.v1alpha.IListEvaluationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationresultsrequest), [protos.google.cloud.discoveryengine.v1alpha.IListEvaluationResultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationresultsresponse) | null | undefined, [protos.google.cloud.discoveryengine.v1alpha.ListEvaluationResultsResponse.IEvaluationResult](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.listevaluationresultsresponse.ievaluationresult)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEvaluationResults(request, callback)
    
    
    listEvaluationResults(request: protos.google.cloud.discoveryengine.v1alpha.IListEvaluationResultsRequest, callback: PaginationCallback<protos.google.cloud.discoveryengine.v1alpha.IListEvaluationResultsRequest, protos.google.cloud.discoveryengine.v1alpha.IListEvaluationResultsResponse | null | undefined, protos.google.cloud.discoveryengine.v1alpha.ListEvaluationResultsResponse.IEvaluationResult>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationresultsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.discoveryengine.v1alpha.IListEvaluationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationresultsrequest), [protos.google.cloud.discoveryengine.v1alpha.IListEvaluationResultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationresultsresponse) | null | undefined, [protos.google.cloud.discoveryengine.v1alpha.ListEvaluationResultsResponse.IEvaluationResult](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.listevaluationresultsresponse.ievaluationresult)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEvaluationResultsAsync(request, options)
    
    
    listEvaluationResultsAsync(request?: protos.google.cloud.discoveryengine.v1alpha.IListEvaluationResultsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.discoveryengine.v1alpha.ListEvaluationResultsResponse.IEvaluationResult>;

Equivalent to `listEvaluationResults`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationresultsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.discoveryengine.v1alpha.ListEvaluationResultsResponse.IEvaluationResult](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.listevaluationresultsresponse.ievaluationresult)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The evaluation resource name, such as
       *  `projects/{project}/locations/{location}/evaluations/{evaluation}`.
       *  If the caller does not have permission to list EvaluationResult  
       *  under this evaluation, regardless of whether or not this evaluation
       *  set exists, a `PERMISSION_DENIED` error is returned.
       */
      // const evaluation = 'abc123'
      /**
       *  Maximum number of EvaluationResult   to return. If unspecified,
       *  defaults to 100. The maximum allowed value is 1000. Values above 1000 will
       *  be coerced to 1000.
       *  If this field is negative, an `INVALID_ARGUMENT` error is returned.
       */
      // const pageSize = 1234
      /**
       *  A page token
       *  ListEvaluationResultsResponse.next_page_token google.cloud.discoveryengine.v1alpha.ListEvaluationResultsResponse.next_page_token,
       *  received from a previous
       *  EvaluationService.ListEvaluationResults google.cloud.discoveryengine.v1alpha.EvaluationService.ListEvaluationResults 
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  EvaluationService.ListEvaluationResults google.cloud.discoveryengine.v1alpha.EvaluationService.ListEvaluationResults 
       *  must match the call that provided the page token. Otherwise, an
       *  `INVALID_ARGUMENT` error is returned.
       */
      // const pageToken = 'abc123'
    
      // Imports the Discoveryengine library
      const {EvaluationServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new EvaluationServiceClient();
    
      async function callListEvaluationResults() {
        // Construct request
        const request = {
          evaluation,
        };
    
        // Run request
        const iterable = discoveryengineClient.listEvaluationResultsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListEvaluationResults();
    
    

### listEvaluationResultsStream(request, options)
    
    
    listEvaluationResultsStream(request?: protos.google.cloud.discoveryengine.v1alpha.IListEvaluationResultsRequest, options?: CallOptions): Transform;

Equivalent to `listEvaluationResults`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationresultsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listEvaluationResultsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listEvaluations(request, options)
    
    
    listEvaluations(request?: protos.google.cloud.discoveryengine.v1alpha.IListEvaluationsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1alpha.IEvaluation[],
            protos.google.cloud.discoveryengine.v1alpha.IListEvaluationsRequest | null,
            protos.google.cloud.discoveryengine.v1alpha.IListEvaluationsResponse
        ]>;

Gets a list of s.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1alpha.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ievaluation)[], [protos.google.cloud.discoveryengine.v1alpha.IListEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationsrequest) | null, [protos.google.cloud.discoveryengine.v1alpha.IListEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listEvaluationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listEvaluations(request, options, callback)
    
    
    listEvaluations(request: protos.google.cloud.discoveryengine.v1alpha.IListEvaluationsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.discoveryengine.v1alpha.IListEvaluationsRequest, protos.google.cloud.discoveryengine.v1alpha.IListEvaluationsResponse | null | undefined, protos.google.cloud.discoveryengine.v1alpha.IEvaluation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.discoveryengine.v1alpha.IListEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationsrequest), [protos.google.cloud.discoveryengine.v1alpha.IListEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationsresponse) | null | undefined, [protos.google.cloud.discoveryengine.v1alpha.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ievaluation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEvaluations(request, callback)
    
    
    listEvaluations(request: protos.google.cloud.discoveryengine.v1alpha.IListEvaluationsRequest, callback: PaginationCallback<protos.google.cloud.discoveryengine.v1alpha.IListEvaluationsRequest, protos.google.cloud.discoveryengine.v1alpha.IListEvaluationsResponse | null | undefined, protos.google.cloud.discoveryengine.v1alpha.IEvaluation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.discoveryengine.v1alpha.IListEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationsrequest), [protos.google.cloud.discoveryengine.v1alpha.IListEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationsresponse) | null | undefined, [protos.google.cloud.discoveryengine.v1alpha.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ievaluation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEvaluationsAsync(request, options)
    
    
    listEvaluationsAsync(request?: protos.google.cloud.discoveryengine.v1alpha.IListEvaluationsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.discoveryengine.v1alpha.IEvaluation>;

Equivalent to `listEvaluations`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.discoveryengine.v1alpha.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ievaluation)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent location resource name, such as
       *  `projects/{project}/locations/{location}`.
       *  If the caller does not have permission to list
       *  Evaluation google.cloud.discoveryengine.v1alpha.Evaluation s under this
       *  location, regardless of whether or not this location exists, a
       *  `PERMISSION_DENIED` error is returned.
       */
      // const parent = 'abc123'
      /**
       *  Maximum number of
       *  Evaluation google.cloud.discoveryengine.v1alpha.Evaluation s to return.
       *  If unspecified, defaults to 100. The maximum allowed value is 1000. Values
       *  above 1000 will be coerced to 1000.
       *  If this field is negative, an `INVALID_ARGUMENT` error is returned.
       */
      // const pageSize = 1234
      /**
       *  A page token
       *  ListEvaluationsResponse.next_page_token google.cloud.discoveryengine.v1alpha.ListEvaluationsResponse.next_page_token,
       *  received from a previous
       *  EvaluationService.ListEvaluations google.cloud.discoveryengine.v1alpha.EvaluationService.ListEvaluations 
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  EvaluationService.ListEvaluations google.cloud.discoveryengine.v1alpha.EvaluationService.ListEvaluations 
       *  must match the call that provided the page token. Otherwise, an
       *  `INVALID_ARGUMENT` error is returned.
       */
      // const pageToken = 'abc123'
    
      // Imports the Discoveryengine library
      const {EvaluationServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new EvaluationServiceClient();
    
      async function callListEvaluations() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = discoveryengineClient.listEvaluationsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListEvaluations();
    
    

### listEvaluationsStream(request, options)
    
    
    listEvaluationsStream(request?: protos.google.cloud.discoveryengine.v1alpha.IListEvaluationsRequest, options?: CallOptions): Transform;

Equivalent to `listEvaluations`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistevaluationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listEvaluationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
**Example**
    
    
    const client = longrunning.operationsClient();
    for await (const response of client.listOperationsAsync(request));
    // doThingsWith(response)
    

### locationPath(project, location)
    
    
    locationPath(project: string, location: string): string;

Return a fully-qualified location resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### matchAnswerFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchAnswerFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the answer from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the answer.  
  
### matchAnswerFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchAnswerFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the answer from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the answer.  
  
### matchAnswerFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName)
    
    
    matchAnswerFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName: string): string | number;

Parse the answer from ProjectLocationDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the answer.  
  
### matchBranchFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchBranchFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the branch from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchBranchFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchBranchFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the branch from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchBranchFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchBranchFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the branch from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchBranchFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName)
    
    
    matchBranchFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName: string): string | number;

Parse the branch from ProjectLocationDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchChunkFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchChunkFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the chunk from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the chunk.  
  
### matchChunkFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchChunkFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the chunk from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the chunk.  
  
### matchCollectionFromEngineName(engineName)
    
    
    matchCollectionFromEngineName(engineName: string): string | number;

Parse the collection from Engine resource.

**Parameter**  
---  
**Name** | **Description**  
`engineName` |  `string`   
A fully-qualified path representing Engine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreName` |  `string`   
A fully-qualified path representing project_location_collection_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName)
    
    
    matchCollectionFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineControlName` |  `string`   
A fully-qualified path representing project_location_collection_engine_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName)
    
    
    matchCollectionFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineConversationName` |  `string`   
A fully-qualified path representing project_location_collection_engine_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName)
    
    
    matchCollectionFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_engine_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchCollectionFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName)
    
    
    matchCollectionFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchControlFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName)
    
    
    matchControlFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName: string): string | number;

Parse the control from ProjectLocationCollectionDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the control.  
  
### matchControlFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName)
    
    
    matchControlFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName: string): string | number;

Parse the control from ProjectLocationCollectionEngineControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineControlName` |  `string`   
A fully-qualified path representing project_location_collection_engine_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the control.  
  
### matchControlFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName)
    
    
    matchControlFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName: string): string | number;

Parse the control from ProjectLocationDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the control.  
  
### matchConversationFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName)
    
    
    matchConversationFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName: string): string | number;

Parse the conversation from ProjectLocationCollectionDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversation.  
  
### matchConversationFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName)
    
    
    matchConversationFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName: string): string | number;

Parse the conversation from ProjectLocationCollectionEngineConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineConversationName` |  `string`   
A fully-qualified path representing project_location_collection_engine_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversation.  
  
### matchConversationFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName)
    
    
    matchConversationFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName: string): string | number;

Parse the conversation from ProjectLocationDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversation.  
  
### matchCustomTuningModelFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName)
    
    
    matchCustomTuningModelFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName: string): string | number;

Parse the custom_tuning_model from ProjectLocationCollectionDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the custom_tuning_model.  
  
### matchCustomTuningModelFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName)
    
    
    matchCustomTuningModelFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName: string): string | number;

Parse the custom_tuning_model from ProjectLocationDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the custom_tuning_model.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreName` |  `string`   
A fully-qualified path representing project_location_collection_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchDataStoreFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the data_store from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName)
    
    
    matchDataStoreFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName: string): string | number;

Parse the data_store from ProjectLocationDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName)
    
    
    matchDataStoreFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName: string): string | number;

Parse the data_store from ProjectLocationDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName)
    
    
    matchDataStoreFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName: string): string | number;

Parse the data_store from ProjectLocationDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName)
    
    
    matchDataStoreFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName: string): string | number;

Parse the data_store from ProjectLocationDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName)
    
    
    matchDataStoreFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName: string): string | number;

Parse the data_store from ProjectLocationDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreName(projectLocationDataStoreName)
    
    
    matchDataStoreFromProjectLocationDataStoreName(projectLocationDataStoreName: string): string | number;

Parse the data_store from ProjectLocationDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreName` |  `string`   
A fully-qualified path representing project_location_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName)
    
    
    matchDataStoreFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName)
    
    
    matchDataStoreFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName: string): string | number;

Parse the data_store from ProjectLocationDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName)
    
    
    matchDataStoreFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName)
    
    
    matchDataStoreFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName)
    
    
    matchDataStoreFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchDataStoreFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDocumentFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchDocumentFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the document from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchDocumentFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchDocumentFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the document from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchDocumentFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchDocumentFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the document from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchDocumentFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName)
    
    
    matchDocumentFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName: string): string | number;

Parse the document from ProjectLocationDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchEngineFromEngineName(engineName)
    
    
    matchEngineFromEngineName(engineName: string): string | number;

Parse the engine from Engine resource.

**Parameter**  
---  
**Name** | **Description**  
`engineName` |  `string`   
A fully-qualified path representing Engine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName)
    
    
    matchEngineFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineControlName` |  `string`   
A fully-qualified path representing project_location_collection_engine_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName)
    
    
    matchEngineFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineConversationName` |  `string`   
A fully-qualified path representing project_location_collection_engine_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName)
    
    
    matchEngineFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_engine_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchEngineFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName)
    
    
    matchEngineFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEvaluationFromEvaluationName(evaluationName)
    
    
    matchEvaluationFromEvaluationName(evaluationName: string): string | number;

Parse the evaluation from Evaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationName` |  `string`   
A fully-qualified path representing Evaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the evaluation.  
  
### matchLocationFromAclConfigName(aclConfigName)
    
    
    matchLocationFromAclConfigName(aclConfigName: string): string | number;

Parse the location from AclConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`aclConfigName` |  `string`   
A fully-qualified path representing AclConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromEngineName(engineName)
    
    
    matchLocationFromEngineName(engineName: string): string | number;

Parse the location from Engine resource.

**Parameter**  
---  
**Name** | **Description**  
`engineName` |  `string`   
A fully-qualified path representing Engine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromEvaluationName(evaluationName)
    
    
    matchLocationFromEvaluationName(evaluationName: string): string | number;

Parse the location from Evaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationName` |  `string`   
A fully-qualified path representing Evaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromLocationName(locationName)
    
    
    matchLocationFromLocationName(locationName: string): string | number;

Parse the location from Location resource.

**Parameter**  
---  
**Name** | **Description**  
`locationName` |  `string`   
A fully-qualified path representing Location resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName: string): string | number;

Parse the location from ProjectLocationCollectionDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreName` |  `string`   
A fully-qualified path representing project_location_collection_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName)
    
    
    matchLocationFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName: string): string | number;

Parse the location from ProjectLocationCollectionEngineControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineControlName` |  `string`   
A fully-qualified path representing project_location_collection_engine_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName)
    
    
    matchLocationFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName: string): string | number;

Parse the location from ProjectLocationCollectionEngineConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineConversationName` |  `string`   
A fully-qualified path representing project_location_collection_engine_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName)
    
    
    matchLocationFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName: string): string | number;

Parse the location from ProjectLocationCollectionEngineServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_engine_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchLocationFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the location from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName)
    
    
    matchLocationFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName: string): string | number;

Parse the location from ProjectLocationCollectionEngineSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchLocationFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the location from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName)
    
    
    matchLocationFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName: string): string | number;

Parse the location from ProjectLocationDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName)
    
    
    matchLocationFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName: string): string | number;

Parse the location from ProjectLocationDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName)
    
    
    matchLocationFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName: string): string | number;

Parse the location from ProjectLocationDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName)
    
    
    matchLocationFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName: string): string | number;

Parse the location from ProjectLocationDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName)
    
    
    matchLocationFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName: string): string | number;

Parse the location from ProjectLocationDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreName(projectLocationDataStoreName)
    
    
    matchLocationFromProjectLocationDataStoreName(projectLocationDataStoreName: string): string | number;

Parse the location from ProjectLocationDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreName` |  `string`   
A fully-qualified path representing project_location_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName)
    
    
    matchLocationFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName: string): string | number;

Parse the location from ProjectLocationDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName)
    
    
    matchLocationFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName: string): string | number;

Parse the location from ProjectLocationDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName)
    
    
    matchLocationFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName: string): string | number;

Parse the location from ProjectLocationDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName)
    
    
    matchLocationFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName: string): string | number;

Parse the location from ProjectLocationDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName)
    
    
    matchLocationFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName: string): string | number;

Parse the location from ProjectLocationDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchLocationFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the location from ProjectLocationDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSampleQueryName(sampleQueryName)
    
    
    matchLocationFromSampleQueryName(sampleQueryName: string): string | number;

Parse the location from SampleQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQueryName` |  `string`   
A fully-qualified path representing SampleQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSampleQuerySetName(sampleQuerySetName)
    
    
    matchLocationFromSampleQuerySetName(sampleQuerySetName: string): string | number;

Parse the location from SampleQuerySet resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQuerySetName` |  `string`   
A fully-qualified path representing SampleQuerySet resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchProjectFromAclConfigName(aclConfigName)
    
    
    matchProjectFromAclConfigName(aclConfigName: string): string | number;

Parse the project from AclConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`aclConfigName` |  `string`   
A fully-qualified path representing AclConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromEngineName(engineName)
    
    
    matchProjectFromEngineName(engineName: string): string | number;

Parse the project from Engine resource.

**Parameter**  
---  
**Name** | **Description**  
`engineName` |  `string`   
A fully-qualified path representing Engine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromEvaluationName(evaluationName)
    
    
    matchProjectFromEvaluationName(evaluationName: string): string | number;

Parse the project from Evaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationName` |  `string`   
A fully-qualified path representing Evaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromLocationName(locationName)
    
    
    matchProjectFromLocationName(locationName: string): string | number;

Parse the project from Location resource.

**Parameter**  
---  
**Name** | **Description**  
`locationName` |  `string`   
A fully-qualified path representing Location resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName: string): string | number;

Parse the project from ProjectLocationCollectionDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreName` |  `string`   
A fully-qualified path representing project_location_collection_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName)
    
    
    matchProjectFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName: string): string | number;

Parse the project from ProjectLocationCollectionEngineControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineControlName` |  `string`   
A fully-qualified path representing project_location_collection_engine_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName)
    
    
    matchProjectFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName: string): string | number;

Parse the project from ProjectLocationCollectionEngineConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineConversationName` |  `string`   
A fully-qualified path representing project_location_collection_engine_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName)
    
    
    matchProjectFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName: string): string | number;

Parse the project from ProjectLocationCollectionEngineServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_engine_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchProjectFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the project from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName)
    
    
    matchProjectFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName: string): string | number;

Parse the project from ProjectLocationCollectionEngineSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchProjectFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the project from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName)
    
    
    matchProjectFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName: string): string | number;

Parse the project from ProjectLocationDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName)
    
    
    matchProjectFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName: string): string | number;

Parse the project from ProjectLocationDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName)
    
    
    matchProjectFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName: string): string | number;

Parse the project from ProjectLocationDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName)
    
    
    matchProjectFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName: string): string | number;

Parse the project from ProjectLocationDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName)
    
    
    matchProjectFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName: string): string | number;

Parse the project from ProjectLocationDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreName(projectLocationDataStoreName)
    
    
    matchProjectFromProjectLocationDataStoreName(projectLocationDataStoreName: string): string | number;

Parse the project from ProjectLocationDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreName` |  `string`   
A fully-qualified path representing project_location_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName)
    
    
    matchProjectFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName: string): string | number;

Parse the project from ProjectLocationDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName)
    
    
    matchProjectFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName: string): string | number;

Parse the project from ProjectLocationDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName)
    
    
    matchProjectFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName: string): string | number;

Parse the project from ProjectLocationDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName)
    
    
    matchProjectFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName: string): string | number;

Parse the project from ProjectLocationDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName)
    
    
    matchProjectFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName: string): string | number;

Parse the project from ProjectLocationDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchProjectFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the project from ProjectLocationDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectName(projectName)
    
    
    matchProjectFromProjectName(projectName: string): string | number;

Parse the project from Project resource.

**Parameter**  
---  
**Name** | **Description**  
`projectName` |  `string`   
A fully-qualified path representing Project resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSampleQueryName(sampleQueryName)
    
    
    matchProjectFromSampleQueryName(sampleQueryName: string): string | number;

Parse the project from SampleQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQueryName` |  `string`   
A fully-qualified path representing SampleQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSampleQuerySetName(sampleQuerySetName)
    
    
    matchProjectFromSampleQuerySetName(sampleQuerySetName: string): string | number;

Parse the project from SampleQuerySet resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQuerySetName` |  `string`   
A fully-qualified path representing SampleQuerySet resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchSampleQueryFromSampleQueryName(sampleQueryName)
    
    
    matchSampleQueryFromSampleQueryName(sampleQueryName: string): string | number;

Parse the sample_query from SampleQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQueryName` |  `string`   
A fully-qualified path representing SampleQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sample_query.  
  
### matchSampleQuerySetFromSampleQueryName(sampleQueryName)
    
    
    matchSampleQuerySetFromSampleQueryName(sampleQueryName: string): string | number;

Parse the sample_query_set from SampleQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQueryName` |  `string`   
A fully-qualified path representing SampleQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sample_query_set.  
  
### matchSampleQuerySetFromSampleQuerySetName(sampleQuerySetName)
    
    
    matchSampleQuerySetFromSampleQuerySetName(sampleQuerySetName: string): string | number;

Parse the sample_query_set from SampleQuerySet resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQuerySetName` |  `string`   
A fully-qualified path representing SampleQuerySet resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sample_query_set.  
  
### matchSchemaFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName)
    
    
    matchSchemaFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName: string): string | number;

Parse the schema from ProjectLocationCollectionDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the schema.  
  
### matchSchemaFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName)
    
    
    matchSchemaFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName: string): string | number;

Parse the schema from ProjectLocationDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the schema.  
  
### matchServingConfigFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName)
    
    
    matchServingConfigFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName: string): string | number;

Parse the serving_config from ProjectLocationCollectionDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the serving_config.  
  
### matchServingConfigFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName)
    
    
    matchServingConfigFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName: string): string | number;

Parse the serving_config from ProjectLocationCollectionEngineServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_engine_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the serving_config.  
  
### matchServingConfigFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName)
    
    
    matchServingConfigFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName: string): string | number;

Parse the serving_config from ProjectLocationDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the serving_config.  
  
### matchSessionFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchSessionFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the session from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName)
    
    
    matchSessionFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName: string): string | number;

Parse the session from ProjectLocationCollectionDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchSessionFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the session from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName)
    
    
    matchSessionFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName: string): string | number;

Parse the session from ProjectLocationCollectionEngineSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName)
    
    
    matchSessionFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName: string): string | number;

Parse the session from ProjectLocationDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName)
    
    
    matchSessionFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName: string): string | number;

Parse the session from ProjectLocationDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchTargetSiteFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchTargetSiteFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the target_site from ProjectLocationCollectionDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the target_site.  
  
### matchTargetSiteFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchTargetSiteFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the target_site from ProjectLocationDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the target_site.  
  
### projectLocationCollectionDataStoreBranchDocumentChunkPath(project, location, collection, dataStore, branch, document, chunk)
    
    
    projectLocationCollectionDataStoreBranchDocumentChunkPath(project: string, location: string, collection: string, dataStore: string, branch: string, document: string, chunk: string): string;

Return a fully-qualified projectLocationCollectionDataStoreBranchDocumentChunk resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`branch` |  `string`   
  
`document` |  `string`   
  
`chunk` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreBranchDocumentPath(project, location, collection, dataStore, branch, document)
    
    
    projectLocationCollectionDataStoreBranchDocumentPath(project: string, location: string, collection: string, dataStore: string, branch: string, document: string): string;

Return a fully-qualified projectLocationCollectionDataStoreBranchDocument resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`branch` |  `string`   
  
`document` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreControlPath(project, location, collection, dataStore, control)
    
    
    projectLocationCollectionDataStoreControlPath(project: string, location: string, collection: string, dataStore: string, control: string): string;

Return a fully-qualified projectLocationCollectionDataStoreControl resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`control` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreConversationPath(project, location, collection, dataStore, conversation)
    
    
    projectLocationCollectionDataStoreConversationPath(project: string, location: string, collection: string, dataStore: string, conversation: string): string;

Return a fully-qualified projectLocationCollectionDataStoreConversation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`conversation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreCustomTuningModelPath(project, location, collection, dataStore, customTuningModel)
    
    
    projectLocationCollectionDataStoreCustomTuningModelPath(project: string, location: string, collection: string, dataStore: string, customTuningModel: string): string;

Return a fully-qualified projectLocationCollectionDataStoreCustomTuningModel resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`customTuningModel` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreDocumentProcessingConfigPath(project, location, collection, dataStore)
    
    
    projectLocationCollectionDataStoreDocumentProcessingConfigPath(project: string, location: string, collection: string, dataStore: string): string;

Return a fully-qualified projectLocationCollectionDataStoreDocumentProcessingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStorePath(project, location, collection, dataStore)
    
    
    projectLocationCollectionDataStorePath(project: string, location: string, collection: string, dataStore: string): string;

Return a fully-qualified projectLocationCollectionDataStore resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreSchemaPath(project, location, collection, dataStore, schema)
    
    
    projectLocationCollectionDataStoreSchemaPath(project: string, location: string, collection: string, dataStore: string, schema: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSchema resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`schema` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreServingConfigPath(project, location, collection, dataStore, servingConfig)
    
    
    projectLocationCollectionDataStoreServingConfigPath(project: string, location: string, collection: string, dataStore: string, servingConfig: string): string;

Return a fully-qualified projectLocationCollectionDataStoreServingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`servingConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreSessionAnswerPath(project, location, collection, dataStore, session, answer)
    
    
    projectLocationCollectionDataStoreSessionAnswerPath(project: string, location: string, collection: string, dataStore: string, session: string, answer: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSessionAnswer resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`session` |  `string`   
  
`answer` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreSessionsPath(project, location, collection, dataStore, session)
    
    
    projectLocationCollectionDataStoreSessionsPath(project: string, location: string, collection: string, dataStore: string, session: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSessions resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`session` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreSiteSearchEnginePath(project, location, collection, dataStore)
    
    
    projectLocationCollectionDataStoreSiteSearchEnginePath(project: string, location: string, collection: string, dataStore: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSiteSearchEngine resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreSiteSearchEngineTargetSitePath(project, location, collection, dataStore, targetSite)
    
    
    projectLocationCollectionDataStoreSiteSearchEngineTargetSitePath(project: string, location: string, collection: string, dataStore: string, targetSite: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSiteSearchEngineTargetSite resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`targetSite` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionEngineControlPath(project, location, collection, engine, control)
    
    
    projectLocationCollectionEngineControlPath(project: string, location: string, collection: string, engine: string, control: string): string;

Return a fully-qualified projectLocationCollectionEngineControl resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`control` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionEngineConversationPath(project, location, collection, engine, conversation)
    
    
    projectLocationCollectionEngineConversationPath(project: string, location: string, collection: string, engine: string, conversation: string): string;

Return a fully-qualified projectLocationCollectionEngineConversation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`conversation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionEngineServingConfigPath(project, location, collection, engine, servingConfig)
    
    
    projectLocationCollectionEngineServingConfigPath(project: string, location: string, collection: string, engine: string, servingConfig: string): string;

Return a fully-qualified projectLocationCollectionEngineServingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`servingConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionEngineSessionAnswerPath(project, location, collection, engine, session, answer)
    
    
    projectLocationCollectionEngineSessionAnswerPath(project: string, location: string, collection: string, engine: string, session: string, answer: string): string;

Return a fully-qualified projectLocationCollectionEngineSessionAnswer resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`session` |  `string`   
  
`answer` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionEngineSessionsPath(project, location, collection, engine, session)
    
    
    projectLocationCollectionEngineSessionsPath(project: string, location: string, collection: string, engine: string, session: string): string;

Return a fully-qualified projectLocationCollectionEngineSessions resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`session` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreBranchDocumentChunkPath(project, location, dataStore, branch, document, chunk)
    
    
    projectLocationDataStoreBranchDocumentChunkPath(project: string, location: string, dataStore: string, branch: string, document: string, chunk: string): string;

Return a fully-qualified projectLocationDataStoreBranchDocumentChunk resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`branch` |  `string`   
  
`document` |  `string`   
  
`chunk` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreBranchDocumentPath(project, location, dataStore, branch, document)
    
    
    projectLocationDataStoreBranchDocumentPath(project: string, location: string, dataStore: string, branch: string, document: string): string;

Return a fully-qualified projectLocationDataStoreBranchDocument resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`branch` |  `string`   
  
`document` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreControlPath(project, location, dataStore, control)
    
    
    projectLocationDataStoreControlPath(project: string, location: string, dataStore: string, control: string): string;

Return a fully-qualified projectLocationDataStoreControl resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`control` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreConversationPath(project, location, dataStore, conversation)
    
    
    projectLocationDataStoreConversationPath(project: string, location: string, dataStore: string, conversation: string): string;

Return a fully-qualified projectLocationDataStoreConversation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`conversation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreCustomTuningModelPath(project, location, dataStore, customTuningModel)
    
    
    projectLocationDataStoreCustomTuningModelPath(project: string, location: string, dataStore: string, customTuningModel: string): string;

Return a fully-qualified projectLocationDataStoreCustomTuningModel resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`customTuningModel` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreDocumentProcessingConfigPath(project, location, dataStore)
    
    
    projectLocationDataStoreDocumentProcessingConfigPath(project: string, location: string, dataStore: string): string;

Return a fully-qualified projectLocationDataStoreDocumentProcessingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStorePath(project, location, dataStore)
    
    
    projectLocationDataStorePath(project: string, location: string, dataStore: string): string;

Return a fully-qualified projectLocationDataStore resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreSchemaPath(project, location, dataStore, schema)
    
    
    projectLocationDataStoreSchemaPath(project: string, location: string, dataStore: string, schema: string): string;

Return a fully-qualified projectLocationDataStoreSchema resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`schema` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreServingConfigPath(project, location, dataStore, servingConfig)
    
    
    projectLocationDataStoreServingConfigPath(project: string, location: string, dataStore: string, servingConfig: string): string;

Return a fully-qualified projectLocationDataStoreServingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`servingConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreSessionAnswerPath(project, location, dataStore, session, answer)
    
    
    projectLocationDataStoreSessionAnswerPath(project: string, location: string, dataStore: string, session: string, answer: string): string;

Return a fully-qualified projectLocationDataStoreSessionAnswer resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`session` |  `string`   
  
`answer` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreSessionsPath(project, location, dataStore, session)
    
    
    projectLocationDataStoreSessionsPath(project: string, location: string, dataStore: string, session: string): string;

Return a fully-qualified projectLocationDataStoreSessions resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`session` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreSiteSearchEnginePath(project, location, dataStore)
    
    
    projectLocationDataStoreSiteSearchEnginePath(project: string, location: string, dataStore: string): string;

Return a fully-qualified projectLocationDataStoreSiteSearchEngine resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreSiteSearchEngineTargetSitePath(project, location, dataStore, targetSite)
    
    
    projectLocationDataStoreSiteSearchEngineTargetSitePath(project: string, location: string, dataStore: string, targetSite: string): string;

Return a fully-qualified projectLocationDataStoreSiteSearchEngineTargetSite resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`targetSite` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectPath(project)
    
    
    projectPath(project: string): string;

Return a fully-qualified project resource name string.

**Parameter**  
---  
**Name** | **Description**  
`project` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### sampleQueryPath(project, location, sampleQuerySet, sampleQuery)
    
    
    sampleQueryPath(project: string, location: string, sampleQuerySet: string, sampleQuery: string): string;

Return a fully-qualified sampleQuery resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`sampleQuerySet` |  `string`   
  
`sampleQuery` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### sampleQuerySetPath(project, location, sampleQuerySet)
    
    
    sampleQuerySetPath(project: string, location: string, sampleQuerySet: string): string;

Return a fully-qualified sampleQuerySet resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`sampleQuerySet` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
