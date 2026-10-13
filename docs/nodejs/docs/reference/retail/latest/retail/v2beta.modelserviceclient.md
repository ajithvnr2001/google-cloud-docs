---
url: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/v2beta.modelserviceclient
title: Class v2beta.ModelServiceClient (5.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:02:39.631388+00:00
---

# Class v2beta.ModelServiceClient (5.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/v2beta.modelserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v2beta.ModelServiceClient (5.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.4.0 (latest)  5.3.1  5.0.1  4.4.0  4.3.0  3.6.0  3.5.0  3.1.0  2.4.1  2.3.1  2.1.1  2.0.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.2  1.1.6 

Service for performing CRUD operations on models. Recommendation models contain all the metadata necessary to generate a set of models for the `Predict()` API. A model is queried indirectly via a ServingConfig, which associates a model with a given Placement (e.g. Frequently Bought Together on Home Page).

This service allows you to do the following:

* Initiate training of a model. * Pause training of an existing model. * List all the available models along with their metadata. * Control their tuning schedule. v2beta

## Package

[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of ModelServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new ModelServiceClient({fallback: true}, gax); ```  
  
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

### modelServiceStub
    
    
    modelServiceStub?: Promise<{
            [name: string]: Function;
        }>;

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
  
### checkCreateModelProgress(name)
    
    
    checkCreateModelProgress(name: string): Promise<LROperation<protos.google.cloud.retail.v2beta.Model, protos.google.cloud.retail.v2beta.CreateModelMetadata>>;

Check the status of the long running operation returned by `createModel()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.retail.v2beta.Model](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.model-class), [protos.google.cloud.retail.v2beta.CreateModelMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.createmodelmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource under which to create the model. Format:
       *  `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The payload of the Model google.cloud.retail.v2beta.Model   to
       *  create.
       */
      // const model = {}
      /**
       *  Optional. Whether to run a dry run to validate the request (without
       *  actually creating the model).
       */
      // const dryRun = true
    
      // Imports the Retail library
      const {ModelServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const retailClient = new [ModelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callCreateModel() {
        // Construct request
        const request = {
          parent,
          model,
        };
    
        // Run request
        const [operation] = await retailClient.createModel(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateModel();
    
    

### checkTuneModelProgress(name)
    
    
    checkTuneModelProgress(name: string): Promise<LROperation<protos.google.cloud.retail.v2beta.TuneModelResponse, protos.google.cloud.retail.v2beta.TuneModelMetadata>>;

Check the status of the long running operation returned by `tuneModel()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.retail.v2beta.TuneModelResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.tunemodelresponse), [protos.google.cloud.retail.v2beta.TuneModelMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.tunemodelmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the model to tune.
       *  Format:
       *  `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}`
       */
      // const name = 'abc123'
    
      // Imports the Retail library
      const {ModelServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const retailClient = new [ModelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callTuneModel() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await retailClient.tuneModel(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callTuneModel();
    
    

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
  
### createModel(request, options)
    
    
    createModel(request?: protos.google.cloud.retail.v2beta.ICreateModelRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.retail.v2beta.IModel, protos.google.cloud.retail.v2beta.ICreateModelMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new model.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.icreatemodelrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.retail.v2beta.IModel](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.imodel), [protos.google.cloud.retail.v2beta.ICreateModelMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.icreatemodelmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource under which to create the model. Format:
       *  `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The payload of the Model google.cloud.retail.v2beta.Model   to
       *  create.
       */
      // const model = {}
      /**
       *  Optional. Whether to run a dry run to validate the request (without
       *  actually creating the model).
       */
      // const dryRun = true
    
      // Imports the Retail library
      const {ModelServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const retailClient = new [ModelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callCreateModel() {
        // Construct request
        const request = {
          parent,
          model,
        };
    
        // Run request
        const [operation] = await retailClient.createModel(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateModel();
    
    

### createModel(request, options, callback)
    
    
    createModel(request: protos.google.cloud.retail.v2beta.ICreateModelRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.retail.v2beta.IModel, protos.google.cloud.retail.v2beta.ICreateModelMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.icreatemodelrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.retail.v2beta.IModel](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.imodel), [protos.google.cloud.retail.v2beta.ICreateModelMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.icreatemodelmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createModel(request, callback)
    
    
    createModel(request: protos.google.cloud.retail.v2beta.ICreateModelRequest, callback: Callback<LROperation<protos.google.cloud.retail.v2beta.IModel, protos.google.cloud.retail.v2beta.ICreateModelMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.icreatemodelrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.retail.v2beta.IModel](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.imodel), [protos.google.cloud.retail.v2beta.ICreateModelMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.icreatemodelmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteModel(request, options)
    
    
    deleteModel(request?: protos.google.cloud.retail.v2beta.IDeleteModelRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.cloud.retail.v2beta.IDeleteModelRequest | undefined,
            {} | undefined
        ]>;

Deletes an existing model.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ideletemodelrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.iempty), [protos.google.cloud.retail.v2beta.IDeleteModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ideletemodelrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the
       *  Model google.cloud.retail.v2beta.Model  to delete. Format:
       *  `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}`
       */
      // const name = 'abc123'
    
      // Imports the Retail library
      const {ModelServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const retailClient = new [ModelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callDeleteModel() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await retailClient.deleteModel(request);
        console.log(response);
      }
    
      callDeleteModel();
    
    

### deleteModel(request, options, callback)
    
    
    deleteModel(request: protos.google.cloud.retail.v2beta.IDeleteModelRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.retail.v2beta.IDeleteModelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ideletemodelrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.iempty), [protos.google.cloud.retail.v2beta.IDeleteModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ideletemodelrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteModel(request, callback)
    
    
    deleteModel(request: protos.google.cloud.retail.v2beta.IDeleteModelRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.retail.v2beta.IDeleteModelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ideletemodelrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.iempty), [protos.google.cloud.retail.v2beta.IDeleteModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ideletemodelrequest) | null | undefined, {} | null | undefined>`   
  
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
    

### getModel(request, options)
    
    
    getModel(request?: protos.google.cloud.retail.v2beta.IGetModelRequest, options?: CallOptions): Promise<[
            protos.google.cloud.retail.v2beta.IModel,
            protos.google.cloud.retail.v2beta.IGetModelRequest | undefined,
            {} | undefined
        ]>;

Gets a model.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.igetmodelrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.retail.v2beta.IModel](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.imodel), [protos.google.cloud.retail.v2beta.IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.igetmodelrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the
       *  Model google.cloud.retail.v2beta.Model  to get. Format:
       *  `projects/{project_number}/locations/{location_id}/catalogs/{catalog}/models/{model_id}`
       */
      // const name = 'abc123'
    
      // Imports the Retail library
      const {ModelServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const retailClient = new [ModelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callGetModel() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await retailClient.getModel(request);
        console.log(response);
      }
    
      callGetModel();
    
    

### getModel(request, options, callback)
    
    
    getModel(request: protos.google.cloud.retail.v2beta.IGetModelRequest, options: CallOptions, callback: Callback<protos.google.cloud.retail.v2beta.IModel, protos.google.cloud.retail.v2beta.IGetModelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.igetmodelrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2beta.IModel](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.imodel), [protos.google.cloud.retail.v2beta.IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.igetmodelrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getModel(request, callback)
    
    
    getModel(request: protos.google.cloud.retail.v2beta.IGetModelRequest, callback: Callback<protos.google.cloud.retail.v2beta.IModel, protos.google.cloud.retail.v2beta.IGetModelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.igetmodelrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2beta.IModel](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.imodel), [protos.google.cloud.retail.v2beta.IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.igetmodelrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
    

### listModels(request, options)
    
    
    listModels(request?: protos.google.cloud.retail.v2beta.IListModelsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.retail.v2beta.IModel[],
            protos.google.cloud.retail.v2beta.IListModelsRequest | null,
            protos.google.cloud.retail.v2beta.IListModelsResponse
        ]>;

Lists all the models linked to this event store.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ilistmodelsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.retail.v2beta.IModel](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.imodel)[], [protos.google.cloud.retail.v2beta.IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ilistmodelsrequest) | null, [protos.google.cloud.retail.v2beta.IListModelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ilistmodelsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listModelsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listModels(request, options, callback)
    
    
    listModels(request: protos.google.cloud.retail.v2beta.IListModelsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.retail.v2beta.IListModelsRequest, protos.google.cloud.retail.v2beta.IListModelsResponse | null | undefined, protos.google.cloud.retail.v2beta.IModel>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ilistmodelsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.retail.v2beta.IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ilistmodelsrequest), [protos.google.cloud.retail.v2beta.IListModelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ilistmodelsresponse) | null | undefined, [protos.google.cloud.retail.v2beta.IModel](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.imodel)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listModels(request, callback)
    
    
    listModels(request: protos.google.cloud.retail.v2beta.IListModelsRequest, callback: PaginationCallback<protos.google.cloud.retail.v2beta.IListModelsRequest, protos.google.cloud.retail.v2beta.IListModelsResponse | null | undefined, protos.google.cloud.retail.v2beta.IModel>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ilistmodelsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.retail.v2beta.IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ilistmodelsrequest), [protos.google.cloud.retail.v2beta.IListModelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ilistmodelsresponse) | null | undefined, [protos.google.cloud.retail.v2beta.IModel](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.imodel)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listModelsAsync(request, options)
    
    
    listModelsAsync(request?: protos.google.cloud.retail.v2beta.IListModelsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.retail.v2beta.IModel>;

Equivalent to `listModels`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ilistmodelsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.retail.v2beta.IModel](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.imodel)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent for which to list models.
       *  Format:
       *  `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. Maximum number of results to return. If unspecified, defaults
       *  to 50. Max allowed value is 1000.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListModels`
       *  call. Provide this to retrieve the subsequent page.
       */
      // const pageToken = 'abc123'
    
      // Imports the Retail library
      const {ModelServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const retailClient = new [ModelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callListModels() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = retailClient.listModelsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListModels();
    
    

### listModelsStream(request, options)
    
    
    listModelsStream(request?: protos.google.cloud.retail.v2beta.IListModelsRequest, options?: CallOptions): Transform;

Equivalent to `listModels`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ilistmodelsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listModelsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### pauseModel(request, options)
    
    
    pauseModel(request?: protos.google.cloud.retail.v2beta.IPauseModelRequest, options?: CallOptions): Promise<[
            protos.google.cloud.retail.v2beta.IModel,
            protos.google.cloud.retail.v2beta.IPauseModelRequest | undefined,
            {} | undefined
        ]>;

Pauses the training of an existing model.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPauseModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ipausemodelrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.retail.v2beta.IModel](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.imodel), [protos.google.cloud.retail.v2beta.IPauseModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ipausemodelrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the model to pause.
       *  Format:
       *  `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}`
       */
      // const name = 'abc123'
    
      // Imports the Retail library
      const {ModelServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const retailClient = new [ModelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callPauseModel() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await retailClient.pauseModel(request);
        console.log(response);
      }
    
      callPauseModel();
    
    

### pauseModel(request, options, callback)
    
    
    pauseModel(request: protos.google.cloud.retail.v2beta.IPauseModelRequest, options: CallOptions, callback: Callback<protos.google.cloud.retail.v2beta.IModel, protos.google.cloud.retail.v2beta.IPauseModelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPauseModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ipausemodelrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2beta.IModel](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.imodel), [protos.google.cloud.retail.v2beta.IPauseModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ipausemodelrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### pauseModel(request, callback)
    
    
    pauseModel(request: protos.google.cloud.retail.v2beta.IPauseModelRequest, callback: Callback<protos.google.cloud.retail.v2beta.IModel, protos.google.cloud.retail.v2beta.IPauseModelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPauseModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ipausemodelrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2beta.IModel](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.imodel), [protos.google.cloud.retail.v2beta.IPauseModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ipausemodelrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### resumeModel(request, options)
    
    
    resumeModel(request?: protos.google.cloud.retail.v2beta.IResumeModelRequest, options?: CallOptions): Promise<[
            protos.google.cloud.retail.v2beta.IModel,
            protos.google.cloud.retail.v2beta.IResumeModelRequest | undefined,
            {} | undefined
        ]>;

Resumes the training of an existing model.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResumeModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iresumemodelrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.retail.v2beta.IModel](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.imodel), [protos.google.cloud.retail.v2beta.IResumeModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iresumemodelrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the model to resume.
       *  Format:
       *  `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}`
       */
      // const name = 'abc123'
    
      // Imports the Retail library
      const {ModelServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const retailClient = new [ModelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callResumeModel() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await retailClient.resumeModel(request);
        console.log(response);
      }
    
      callResumeModel();
    
    

### resumeModel(request, options, callback)
    
    
    resumeModel(request: protos.google.cloud.retail.v2beta.IResumeModelRequest, options: CallOptions, callback: Callback<protos.google.cloud.retail.v2beta.IModel, protos.google.cloud.retail.v2beta.IResumeModelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResumeModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iresumemodelrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2beta.IModel](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.imodel), [protos.google.cloud.retail.v2beta.IResumeModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iresumemodelrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### resumeModel(request, callback)
    
    
    resumeModel(request: protos.google.cloud.retail.v2beta.IResumeModelRequest, callback: Callback<protos.google.cloud.retail.v2beta.IModel, protos.google.cloud.retail.v2beta.IResumeModelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResumeModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iresumemodelrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2beta.IModel](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.imodel), [protos.google.cloud.retail.v2beta.IResumeModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iresumemodelrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
  
### tuneModel(request, options)
    
    
    tuneModel(request?: protos.google.cloud.retail.v2beta.ITuneModelRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.retail.v2beta.ITuneModelResponse, protos.google.cloud.retail.v2beta.ITuneModelMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Tunes an existing model.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITuneModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.itunemodelrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.retail.v2beta.ITuneModelResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.itunemodelresponse), [protos.google.cloud.retail.v2beta.ITuneModelMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.itunemodelmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the model to tune.
       *  Format:
       *  `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}`
       */
      // const name = 'abc123'
    
      // Imports the Retail library
      const {ModelServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const retailClient = new [ModelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callTuneModel() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await retailClient.tuneModel(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callTuneModel();
    
    

### tuneModel(request, options, callback)
    
    
    tuneModel(request: protos.google.cloud.retail.v2beta.ITuneModelRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.retail.v2beta.ITuneModelResponse, protos.google.cloud.retail.v2beta.ITuneModelMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITuneModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.itunemodelrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.retail.v2beta.ITuneModelResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.itunemodelresponse), [protos.google.cloud.retail.v2beta.ITuneModelMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.itunemodelmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### tuneModel(request, callback)
    
    
    tuneModel(request: protos.google.cloud.retail.v2beta.ITuneModelRequest, callback: Callback<LROperation<protos.google.cloud.retail.v2beta.ITuneModelResponse, protos.google.cloud.retail.v2beta.ITuneModelMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITuneModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.itunemodelrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.retail.v2beta.ITuneModelResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.itunemodelresponse), [protos.google.cloud.retail.v2beta.ITuneModelMetadata](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.itunemodelmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateModel(request, options)
    
    
    updateModel(request?: protos.google.cloud.retail.v2beta.IUpdateModelRequest, options?: CallOptions): Promise<[
            protos.google.cloud.retail.v2beta.IModel,
            protos.google.cloud.retail.v2beta.IUpdateModelRequest | undefined,
            {} | undefined
        ]>;

Update of model metadata. Only fields that currently can be updated are: `filtering_option` and `periodic_tuning_state`. If other values are provided, this API method ignores them.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iupdatemodelrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.retail.v2beta.IModel](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.imodel), [protos.google.cloud.retail.v2beta.IUpdateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iupdatemodelrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The body of the updated
       *  Model google.cloud.retail.v2beta.Model.
       */
      // const model = {}
      /**
       *  Optional. Indicates which fields in the provided 'model' to
       *  update. If not set, by default updates all fields.
       */
      // const updateMask = {}
    
      // Imports the Retail library
      const {ModelServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const retailClient = new [ModelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callUpdateModel() {
        // Construct request
        const request = {
          model,
        };
    
        // Run request
        const response = await retailClient.updateModel(request);
        console.log(response);
      }
    
      callUpdateModel();
    
    

### updateModel(request, options, callback)
    
    
    updateModel(request: protos.google.cloud.retail.v2beta.IUpdateModelRequest, options: CallOptions, callback: Callback<protos.google.cloud.retail.v2beta.IModel, protos.google.cloud.retail.v2beta.IUpdateModelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iupdatemodelrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2beta.IModel](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.imodel), [protos.google.cloud.retail.v2beta.IUpdateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iupdatemodelrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateModel(request, callback)
    
    
    updateModel(request: protos.google.cloud.retail.v2beta.IUpdateModelRequest, callback: Callback<protos.google.cloud.retail.v2beta.IModel, protos.google.cloud.retail.v2beta.IUpdateModelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iupdatemodelrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2beta.IModel](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.imodel), [protos.google.cloud.retail.v2beta.IUpdateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iupdatemodelrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
