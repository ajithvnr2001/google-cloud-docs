---
url: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/v1alpha.modelserviceclient
title: Class v1alpha.ModelServiceClient (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:04.662296+00:00
---

# Class v1alpha.ModelServiceClient (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/v1alpha.modelserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1alpha.ModelServiceClient (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  4.1.0  3.7.0  3.6.0  2.9.0  2.8.0  2.7.0  2.6.0  2.4.0  2.3.0 

Provides methods for getting metadata information about Generative Models. v1alpha

## Package

[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)

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
    
    
    static get scopes(): never[];

The scopes needed to make gRPC calls for every method defined in this service.

### servicePath
    
    
    static get servicePath(): string;

The DNS address for this API service.

### universeDomain
    
    
    get universeDomain(): string;

### warn
    
    
    warn: (code: string, message: string, warnType?: string) => void;

## Methods 

### cachedContentPath(id)
    
    
    cachedContentPath(id: string): string;

Return a fully-qualified cachedContent resource name string.

**Parameter**  
---  
**Name** | **Description**  
`id` |  `string`   
  
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
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### checkCreateTunedModelProgress(name)
    
    
    checkCreateTunedModelProgress(name: string): Promise<LROperation<protos.google.ai.generativelanguage.v1alpha.TunedModel, protos.google.ai.generativelanguage.v1alpha.CreateTunedModelMetadata>>;

Check the status of the long running operation returned by `createTunedModel()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.ai.generativelanguage.v1alpha.TunedModel](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.tunedmodel-class), [protos.google.ai.generativelanguage.v1alpha.CreateTunedModelMetadata](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.createtunedmodelmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. The unique id for the tuned model if specified.
       *  This value should be up to 40 characters, the first character must be a
       *  letter, the last could be a letter or a number. The id must match the
       *  regular expression: `[a-z]([a-z0-9-]{0,38}[a-z0-9])?`.
       */
      // const tunedModelId = 'abc123'
      /**
       *  Required. The tuned model to create.
       */
      // const tunedModel = {}
    
      // Imports the Generativelanguage library
      const {ModelServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [ModelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callCreateTunedModel() {
        // Construct request
        const request = {
          tunedModel,
        };
    
        // Run request
        const [operation] = await generativelanguageClient.createTunedModel(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateTunedModel();
    
    

### chunkPath(corpus, document, chunk)
    
    
    chunkPath(corpus: string, document: string, chunk: string): string;

Return a fully-qualified chunk resource name string.

**Parameters**  
---  
**Name** | **Description**  
`corpus` |  `string`   
  
`document` |  `string`   
  
`chunk` |  `string`   
  
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
  
### corpusPath(corpus)
    
    
    corpusPath(corpus: string): string;

Return a fully-qualified corpus resource name string.

**Parameter**  
---  
**Name** | **Description**  
`corpus` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### corpusPermissionsPath(corpus, permission)
    
    
    corpusPermissionsPath(corpus: string, permission: string): string;

Return a fully-qualified corpusPermissions resource name string.

**Parameters**  
---  
**Name** | **Description**  
`corpus` |  `string`   
  
`permission` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### createTunedModel(request, options)
    
    
    createTunedModel(request?: protos.google.ai.generativelanguage.v1alpha.ICreateTunedModelRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.ai.generativelanguage.v1alpha.ITunedModel, protos.google.ai.generativelanguage.v1alpha.ICreateTunedModelMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a tuned model. Check intermediate tuning progress (if any) through the [google.longrunning.Operations] service.

Access status and results through the Operations service. Example: GET /v1/tunedModels/az2mb0bpw6i/operations/000-111-222

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTunedModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatetunedmodelrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.ai.generativelanguage.v1alpha.ITunedModel](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.itunedmodel), [protos.google.ai.generativelanguage.v1alpha.ICreateTunedModelMetadata](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatetunedmodelmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. The unique id for the tuned model if specified.
       *  This value should be up to 40 characters, the first character must be a
       *  letter, the last could be a letter or a number. The id must match the
       *  regular expression: `[a-z]([a-z0-9-]{0,38}[a-z0-9])?`.
       */
      // const tunedModelId = 'abc123'
      /**
       *  Required. The tuned model to create.
       */
      // const tunedModel = {}
    
      // Imports the Generativelanguage library
      const {ModelServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [ModelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callCreateTunedModel() {
        // Construct request
        const request = {
          tunedModel,
        };
    
        // Run request
        const [operation] = await generativelanguageClient.createTunedModel(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateTunedModel();
    
    

### createTunedModel(request, options, callback)
    
    
    createTunedModel(request: protos.google.ai.generativelanguage.v1alpha.ICreateTunedModelRequest, options: CallOptions, callback: Callback<LROperation<protos.google.ai.generativelanguage.v1alpha.ITunedModel, protos.google.ai.generativelanguage.v1alpha.ICreateTunedModelMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTunedModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatetunedmodelrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.ai.generativelanguage.v1alpha.ITunedModel](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.itunedmodel), [protos.google.ai.generativelanguage.v1alpha.ICreateTunedModelMetadata](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatetunedmodelmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTunedModel(request, callback)
    
    
    createTunedModel(request: protos.google.ai.generativelanguage.v1alpha.ICreateTunedModelRequest, callback: Callback<LROperation<protos.google.ai.generativelanguage.v1alpha.ITunedModel, protos.google.ai.generativelanguage.v1alpha.ICreateTunedModelMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTunedModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatetunedmodelrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.ai.generativelanguage.v1alpha.ITunedModel](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.itunedmodel), [protos.google.ai.generativelanguage.v1alpha.ICreateTunedModelMetadata](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatetunedmodelmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### deleteTunedModel(request, options)
    
    
    deleteTunedModel(request?: protos.google.ai.generativelanguage.v1alpha.IDeleteTunedModelRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.ai.generativelanguage.v1alpha.IDeleteTunedModelRequest | undefined),
            {} | undefined
        ]>;

Deletes a tuned model.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTunedModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletetunedmodelrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.iempty), ([protos.google.ai.generativelanguage.v1alpha.IDeleteTunedModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletetunedmodelrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the model.
       *  Format: `tunedModels/my-model-id`
       */
      // const name = 'abc123'
    
      // Imports the Generativelanguage library
      const {ModelServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [ModelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callDeleteTunedModel() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await generativelanguageClient.deleteTunedModel(request);
        console.log(response);
      }
    
      callDeleteTunedModel();
    
    

### deleteTunedModel(request, options, callback)
    
    
    deleteTunedModel(request: protos.google.ai.generativelanguage.v1alpha.IDeleteTunedModelRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.ai.generativelanguage.v1alpha.IDeleteTunedModelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTunedModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletetunedmodelrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.iempty), [protos.google.ai.generativelanguage.v1alpha.IDeleteTunedModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletetunedmodelrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTunedModel(request, callback)
    
    
    deleteTunedModel(request: protos.google.ai.generativelanguage.v1alpha.IDeleteTunedModelRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.ai.generativelanguage.v1alpha.IDeleteTunedModelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTunedModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletetunedmodelrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.iempty), [protos.google.ai.generativelanguage.v1alpha.IDeleteTunedModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletetunedmodelrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### documentPath(corpus, document)
    
    
    documentPath(corpus: string, document: string): string;

Return a fully-qualified document resource name string.

**Parameters**  
---  
**Name** | **Description**  
`corpus` |  `string`   
  
`document` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### filePath(file)
    
    
    filePath(file: string): string;

Return a fully-qualified file resource name string.

**Parameter**  
---  
**Name** | **Description**  
`file` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### getModel(request, options)
    
    
    getModel(request?: protos.google.ai.generativelanguage.v1alpha.IGetModelRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.IModel,
            protos.google.ai.generativelanguage.v1alpha.IGetModelRequest | undefined,
            {} | undefined
        ]>;

Gets information about a specific `Model` such as its version number, token limits, [parameters](https://ai.google.dev/gemini-api/docs/models/generative-models#model-parameters) and other metadata. Refer to the [Gemini models guide](<https://ai.google.dev/gemini-api/docs/models/gemini>) for detailed model information.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetmodelrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.IModel](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.imodel), [protos.google.ai.generativelanguage.v1alpha.IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetmodelrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Model](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.model). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the model.
       *  This name should match a model name returned by the `ListModels` method.
       *  Format: `models/{model}`
       */
      // const name = 'abc123'
    
      // Imports the Generativelanguage library
      const {ModelServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [ModelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callGetModel() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await generativelanguageClient.getModel(request);
        console.log(response);
      }
    
      callGetModel();
    
    

### getModel(request, options, callback)
    
    
    getModel(request: protos.google.ai.generativelanguage.v1alpha.IGetModelRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IModel, protos.google.ai.generativelanguage.v1alpha.IGetModelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetmodelrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IModel](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.imodel), [protos.google.ai.generativelanguage.v1alpha.IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetmodelrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getModel(request, callback)
    
    
    getModel(request: protos.google.ai.generativelanguage.v1alpha.IGetModelRequest, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IModel, protos.google.ai.generativelanguage.v1alpha.IGetModelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetmodelrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IModel](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.imodel), [protos.google.ai.generativelanguage.v1alpha.IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetmodelrequest) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.longrunning.operation)]>` |   
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
  
### getTunedModel(request, options)
    
    
    getTunedModel(request?: protos.google.ai.generativelanguage.v1alpha.IGetTunedModelRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.ITunedModel,
            (protos.google.ai.generativelanguage.v1alpha.IGetTunedModelRequest | undefined),
            {} | undefined
        ]>;

Gets information about a specific TunedModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTunedModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igettunedmodelrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.ITunedModel](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.itunedmodel), ([protos.google.ai.generativelanguage.v1alpha.IGetTunedModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igettunedmodelrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the model.
       *  Format: `tunedModels/my-model-id`
       */
      // const name = 'abc123'
    
      // Imports the Generativelanguage library
      const {ModelServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [ModelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callGetTunedModel() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await generativelanguageClient.getTunedModel(request);
        console.log(response);
      }
    
      callGetTunedModel();
    
    

### getTunedModel(request, options, callback)
    
    
    getTunedModel(request: protos.google.ai.generativelanguage.v1alpha.IGetTunedModelRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1alpha.ITunedModel, protos.google.ai.generativelanguage.v1alpha.IGetTunedModelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTunedModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igettunedmodelrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.ITunedModel](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.itunedmodel), [protos.google.ai.generativelanguage.v1alpha.IGetTunedModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igettunedmodelrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTunedModel(request, callback)
    
    
    getTunedModel(request: protos.google.ai.generativelanguage.v1alpha.IGetTunedModelRequest, callback: Callback<protos.google.ai.generativelanguage.v1alpha.ITunedModel, protos.google.ai.generativelanguage.v1alpha.IGetTunedModelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTunedModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igettunedmodelrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.ITunedModel](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.itunedmodel), [protos.google.ai.generativelanguage.v1alpha.IGetTunedModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igettunedmodelrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listModels(request, options)
    
    
    listModels(request?: protos.google.ai.generativelanguage.v1alpha.IListModelsRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.IModel[],
            protos.google.ai.generativelanguage.v1alpha.IListModelsRequest | null,
            protos.google.ai.generativelanguage.v1alpha.IListModelsResponse
        ]>;

Lists the [`Model`s](<https://ai.google.dev/gemini-api/docs/models/gemini>) available through the Gemini API.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistmodelsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.IModel](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.imodel)[], [protos.google.ai.generativelanguage.v1alpha.IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistmodelsrequest) | null, [protos.google.ai.generativelanguage.v1alpha.IListModelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistmodelsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Model](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.model). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listModelsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listModels(request, options, callback)
    
    
    listModels(request: protos.google.ai.generativelanguage.v1alpha.IListModelsRequest, options: CallOptions, callback: PaginationCallback<protos.google.ai.generativelanguage.v1alpha.IListModelsRequest, protos.google.ai.generativelanguage.v1alpha.IListModelsResponse | null | undefined, protos.google.ai.generativelanguage.v1alpha.IModel>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistmodelsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.ai.generativelanguage.v1alpha.IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistmodelsrequest), [protos.google.ai.generativelanguage.v1alpha.IListModelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistmodelsresponse) | null | undefined, [protos.google.ai.generativelanguage.v1alpha.IModel](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.imodel)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listModels(request, callback)
    
    
    listModels(request: protos.google.ai.generativelanguage.v1alpha.IListModelsRequest, callback: PaginationCallback<protos.google.ai.generativelanguage.v1alpha.IListModelsRequest, protos.google.ai.generativelanguage.v1alpha.IListModelsResponse | null | undefined, protos.google.ai.generativelanguage.v1alpha.IModel>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistmodelsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.ai.generativelanguage.v1alpha.IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistmodelsrequest), [protos.google.ai.generativelanguage.v1alpha.IListModelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistmodelsresponse) | null | undefined, [protos.google.ai.generativelanguage.v1alpha.IModel](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.imodel)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listModelsAsync(request, options)
    
    
    listModelsAsync(request?: protos.google.ai.generativelanguage.v1alpha.IListModelsRequest, options?: CallOptions): AsyncIterable<protos.google.ai.generativelanguage.v1alpha.IModel>;

Equivalent to `listModels`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistmodelsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.ai.generativelanguage.v1alpha.IModel](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.imodel)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Model](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.model). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The maximum number of `Models` to return (per page).
       *  If unspecified, 50 models will be returned per page.
       *  This method returns at most 1000 models per page, even if you pass a larger
       *  page_size.
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous `ListModels` call.
       *  Provide the `page_token` returned by one request as an argument to the next
       *  request to retrieve the next page.
       *  When paginating, all other parameters provided to `ListModels` must match
       *  the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Generativelanguage library
      const {ModelServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [ModelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callListModels() {
        // Construct request
        const request = {
        };
    
        // Run request
        const iterable = generativelanguageClient.listModelsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListModels();
    
    

### listModelsStream(request, options)
    
    
    listModelsStream(request?: protos.google.ai.generativelanguage.v1alpha.IListModelsRequest, options?: CallOptions): Transform;

Equivalent to `listModels`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistmodelsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Model](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.model) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listModelsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listOperationsAsync(request, options)
    
    
    listOperationsAsync(request: protos.google.longrunning.ListOperationsRequest, options?: gax.CallOptions): AsyncIterable<protos.google.longrunning.IOperation>;

Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. Returns an iterable object.

For-await-of syntax is used with the iterable to recursively get response element on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
**Example**
    
    
    const client = longrunning.operationsClient();
    for await (const response of client.listOperationsAsync(request));
    // doThingsWith(response)
    

### listTunedModels(request, options)
    
    
    listTunedModels(request?: protos.google.ai.generativelanguage.v1alpha.IListTunedModelsRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.ITunedModel[],
            protos.google.ai.generativelanguage.v1alpha.IListTunedModelsRequest | null,
            protos.google.ai.generativelanguage.v1alpha.IListTunedModelsResponse
        ]>;

Lists created tuned models.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTunedModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilisttunedmodelsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.ITunedModel](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.itunedmodel)[], [protos.google.ai.generativelanguage.v1alpha.IListTunedModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilisttunedmodelsrequest) | null, [protos.google.ai.generativelanguage.v1alpha.IListTunedModelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilisttunedmodelsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listTunedModelsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listTunedModels(request, options, callback)
    
    
    listTunedModels(request: protos.google.ai.generativelanguage.v1alpha.IListTunedModelsRequest, options: CallOptions, callback: PaginationCallback<protos.google.ai.generativelanguage.v1alpha.IListTunedModelsRequest, protos.google.ai.generativelanguage.v1alpha.IListTunedModelsResponse | null | undefined, protos.google.ai.generativelanguage.v1alpha.ITunedModel>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTunedModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilisttunedmodelsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.ai.generativelanguage.v1alpha.IListTunedModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilisttunedmodelsrequest), [protos.google.ai.generativelanguage.v1alpha.IListTunedModelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilisttunedmodelsresponse) | null | undefined, [protos.google.ai.generativelanguage.v1alpha.ITunedModel](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.itunedmodel)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTunedModels(request, callback)
    
    
    listTunedModels(request: protos.google.ai.generativelanguage.v1alpha.IListTunedModelsRequest, callback: PaginationCallback<protos.google.ai.generativelanguage.v1alpha.IListTunedModelsRequest, protos.google.ai.generativelanguage.v1alpha.IListTunedModelsResponse | null | undefined, protos.google.ai.generativelanguage.v1alpha.ITunedModel>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTunedModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilisttunedmodelsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.ai.generativelanguage.v1alpha.IListTunedModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilisttunedmodelsrequest), [protos.google.ai.generativelanguage.v1alpha.IListTunedModelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilisttunedmodelsresponse) | null | undefined, [protos.google.ai.generativelanguage.v1alpha.ITunedModel](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.itunedmodel)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTunedModelsAsync(request, options)
    
    
    listTunedModelsAsync(request?: protos.google.ai.generativelanguage.v1alpha.IListTunedModelsRequest, options?: CallOptions): AsyncIterable<protos.google.ai.generativelanguage.v1alpha.ITunedModel>;

Equivalent to `listTunedModels`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTunedModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilisttunedmodelsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.ai.generativelanguage.v1alpha.ITunedModel](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.itunedmodel)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. The maximum number of `TunedModels` to return (per page).
       *  The service may return fewer tuned models.
       *  If unspecified, at most 10 tuned models will be returned.
       *  This method returns at most 1000 models per page, even if you pass a larger
       *  page_size.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListTunedModels` call.
       *  Provide the `page_token` returned by one request as an argument to the next
       *  request to retrieve the next page.
       *  When paginating, all other parameters provided to `ListTunedModels`
       *  must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. A filter is a full text search over the tuned model's description
       *  and display name. By default, results will not include tuned models shared
       *  with everyone.
       *  Additional operators:
       *    - owner:me
       *    - writers:me
       *    - readers:me
       *    - readers:everyone
       *  Examples:
       *    "owner:me" returns all tuned models to which caller has owner role
       *    "readers:me" returns all tuned models to which caller has reader role
       *    "readers:everyone" returns all tuned models that are shared with everyone
       */
      // const filter = 'abc123'
    
      // Imports the Generativelanguage library
      const {ModelServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [ModelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callListTunedModels() {
        // Construct request
        const request = {
        };
    
        // Run request
        const iterable = generativelanguageClient.listTunedModelsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListTunedModels();
    
    

### listTunedModelsStream(request, options)
    
    
    listTunedModelsStream(request?: protos.google.ai.generativelanguage.v1alpha.IListTunedModelsRequest, options?: CallOptions): Transform;

Equivalent to `listTunedModels`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTunedModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilisttunedmodelsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listTunedModelsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### matchChunkFromChunkName(chunkName)
    
    
    matchChunkFromChunkName(chunkName: string): string | number;

Parse the chunk from Chunk resource.

**Parameter**  
---  
**Name** | **Description**  
`chunkName` |  `string`   
A fully-qualified path representing Chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the chunk.  
  
### matchCorpusFromChunkName(chunkName)
    
    
    matchCorpusFromChunkName(chunkName: string): string | number;

Parse the corpus from Chunk resource.

**Parameter**  
---  
**Name** | **Description**  
`chunkName` |  `string`   
A fully-qualified path representing Chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the corpus.  
  
### matchCorpusFromCorpusName(corpusName)
    
    
    matchCorpusFromCorpusName(corpusName: string): string | number;

Parse the corpus from Corpus resource.

**Parameter**  
---  
**Name** | **Description**  
`corpusName` |  `string`   
A fully-qualified path representing Corpus resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the corpus.  
  
### matchCorpusFromCorpusPermissionsName(corpusPermissionsName)
    
    
    matchCorpusFromCorpusPermissionsName(corpusPermissionsName: string): string | number;

Parse the corpus from CorpusPermissions resource.

**Parameter**  
---  
**Name** | **Description**  
`corpusPermissionsName` |  `string`   
A fully-qualified path representing corpus_permissions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the corpus.  
  
### matchCorpusFromDocumentName(documentName)
    
    
    matchCorpusFromDocumentName(documentName: string): string | number;

Parse the corpus from Document resource.

**Parameter**  
---  
**Name** | **Description**  
`documentName` |  `string`   
A fully-qualified path representing Document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the corpus.  
  
### matchDocumentFromChunkName(chunkName)
    
    
    matchDocumentFromChunkName(chunkName: string): string | number;

Parse the document from Chunk resource.

**Parameter**  
---  
**Name** | **Description**  
`chunkName` |  `string`   
A fully-qualified path representing Chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchDocumentFromDocumentName(documentName)
    
    
    matchDocumentFromDocumentName(documentName: string): string | number;

Parse the document from Document resource.

**Parameter**  
---  
**Name** | **Description**  
`documentName` |  `string`   
A fully-qualified path representing Document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchFileFromFileName(fileName)
    
    
    matchFileFromFileName(fileName: string): string | number;

Parse the file from File resource.

**Parameter**  
---  
**Name** | **Description**  
`fileName` |  `string`   
A fully-qualified path representing File resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the file.  
  
### matchIdFromCachedContentName(cachedContentName)
    
    
    matchIdFromCachedContentName(cachedContentName: string): string | number;

Parse the id from CachedContent resource.

**Parameter**  
---  
**Name** | **Description**  
`cachedContentName` |  `string`   
A fully-qualified path representing CachedContent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the id.  
  
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
  
### matchPermissionFromCorpusPermissionsName(corpusPermissionsName)
    
    
    matchPermissionFromCorpusPermissionsName(corpusPermissionsName: string): string | number;

Parse the permission from CorpusPermissions resource.

**Parameter**  
---  
**Name** | **Description**  
`corpusPermissionsName` |  `string`   
A fully-qualified path representing corpus_permissions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the permission.  
  
### matchPermissionFromTunedModelPermissionsName(tunedModelPermissionsName)
    
    
    matchPermissionFromTunedModelPermissionsName(tunedModelPermissionsName: string): string | number;

Parse the permission from TunedModelPermissions resource.

**Parameter**  
---  
**Name** | **Description**  
`tunedModelPermissionsName` |  `string`   
A fully-qualified path representing tuned_model_permissions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the permission.  
  
### matchTunedModelFromTunedModelName(tunedModelName)
    
    
    matchTunedModelFromTunedModelName(tunedModelName: string): string | number;

Parse the tuned_model from TunedModel resource.

**Parameter**  
---  
**Name** | **Description**  
`tunedModelName` |  `string`   
A fully-qualified path representing TunedModel resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tuned_model.  
  
### matchTunedModelFromTunedModelPermissionsName(tunedModelPermissionsName)
    
    
    matchTunedModelFromTunedModelPermissionsName(tunedModelPermissionsName: string): string | number;

Parse the tuned_model from TunedModelPermissions resource.

**Parameter**  
---  
**Name** | **Description**  
`tunedModelPermissionsName` |  `string`   
A fully-qualified path representing tuned_model_permissions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tuned_model.  
  
### modelPath(model)
    
    
    modelPath(model: string): string;

Return a fully-qualified model resource name string.

**Parameter**  
---  
**Name** | **Description**  
`model` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### tunedModelPath(tunedModel)
    
    
    tunedModelPath(tunedModel: string): string;

Return a fully-qualified tunedModel resource name string.

**Parameter**  
---  
**Name** | **Description**  
`tunedModel` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### tunedModelPermissionsPath(tunedModel, permission)
    
    
    tunedModelPermissionsPath(tunedModel: string, permission: string): string;

Return a fully-qualified tunedModelPermissions resource name string.

**Parameters**  
---  
**Name** | **Description**  
`tunedModel` |  `string`   
  
`permission` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### updateTunedModel(request, options)
    
    
    updateTunedModel(request?: protos.google.ai.generativelanguage.v1alpha.IUpdateTunedModelRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.ITunedModel,
            (protos.google.ai.generativelanguage.v1alpha.IUpdateTunedModelRequest | undefined),
            {} | undefined
        ]>;

Updates a tuned model.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTunedModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatetunedmodelrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.ITunedModel](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.itunedmodel), ([protos.google.ai.generativelanguage.v1alpha.IUpdateTunedModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatetunedmodelrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The tuned model to update.
       */
      // const tunedModel = {}
      /**
       *  Optional. The list of fields to update.
       */
      // const updateMask = {}
    
      // Imports the Generativelanguage library
      const {ModelServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [ModelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callUpdateTunedModel() {
        // Construct request
        const request = {
          tunedModel,
        };
    
        // Run request
        const response = await generativelanguageClient.updateTunedModel(request);
        console.log(response);
      }
    
      callUpdateTunedModel();
    
    

### updateTunedModel(request, options, callback)
    
    
    updateTunedModel(request: protos.google.ai.generativelanguage.v1alpha.IUpdateTunedModelRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1alpha.ITunedModel, protos.google.ai.generativelanguage.v1alpha.IUpdateTunedModelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTunedModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatetunedmodelrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.ITunedModel](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.itunedmodel), [protos.google.ai.generativelanguage.v1alpha.IUpdateTunedModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatetunedmodelrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTunedModel(request, callback)
    
    
    updateTunedModel(request: protos.google.ai.generativelanguage.v1alpha.IUpdateTunedModelRequest, callback: Callback<protos.google.ai.generativelanguage.v1alpha.ITunedModel, protos.google.ai.generativelanguage.v1alpha.IUpdateTunedModelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTunedModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatetunedmodelrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.ITunedModel](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.itunedmodel), [protos.google.ai.generativelanguage.v1alpha.IUpdateTunedModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatetunedmodelrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
