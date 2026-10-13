---
url: https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/v1alpha.gkehubclient
title: Class v1alpha.GkeHubClient (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:04:58.702409+00:00
---

# Class v1alpha.GkeHubClient (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/v1alpha.gkehubclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1alpha.GkeHubClient (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.4.0  6.1.0  6.0.1  5.0.0  4.5.0  4.4.0  4.2.0  3.4.0  3.3.1  3.2.2  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.1  1.1.4 

The GKE Hub service handles the registration of many Kubernetes clusters to Google Cloud, and the management of multi-cluster features over those clusters.

The GKE Hub service operates on the following resources:

* * [Feature](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.feature)

GKE Hub is currently only available in the global region.

**Membership management may be non-trivial:** it is recommended to use one of the Google-provided client libraries or tools where possible when working with Membership resources. v1alpha

## Package

[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of GkeHubClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new GkeHubClient({fallback: true}, gax); ```  
  
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

### gkeHubStub
    
    
    gkeHubStub?: Promise<{
            [name: string]: Function;
        }>;

### innerApiCalls
    
    
    innerApiCalls: {
            [name: string]: Function;
        };

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

### checkCreateFeatureProgress(name)
    
    
    checkCreateFeatureProgress(name: string): Promise<LROperation<protos.google.cloud.gkehub.v1alpha.Feature, protos.google.cloud.gkehub.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `createFeature()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.gkehub.v1alpha.Feature](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.feature), [protos.google.cloud.gkehub.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The parent (project and location) where the Feature will be created.
       *  Specified in the format `projects/* /locations/*`.
       */
      // const parent = 'abc123'
      /**
       *  The ID of the feature to create.
       */
      // const featureId = 'abc123'
      /**
       *  The Feature resource to create.
       */
      // const resource = {}
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Gkehub library
      const {GkeHubClient} = require('[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gkehubClient = new [GkeHubClient](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)();
    
      async function callCreateFeature() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await gkehubClient.createFeature(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateFeature();
    
    

### checkDeleteFeatureProgress(name)
    
    
    checkDeleteFeatureProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.gkehub.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `deleteFeature()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.protobuf.empty), [protos.google.cloud.gkehub.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The Feature resource name in the format
       *  `projects/* /locations/* /features/*`.
       */
      // const name = 'abc123'
      /**
       *  If set to true, the delete will ignore any outstanding resources for
       *  this Feature (that is, `FeatureState.has_resources` is set to true). These
       *  resources will NOT be cleaned up or modified in any way.
       */
      // const force = true
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Gkehub library
      const {GkeHubClient} = require('[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gkehubClient = new [GkeHubClient](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)();
    
      async function callDeleteFeature() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await gkehubClient.deleteFeature(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteFeature();
    
    

### checkUpdateFeatureProgress(name)
    
    
    checkUpdateFeatureProgress(name: string): Promise<LROperation<protos.google.cloud.gkehub.v1alpha.Feature, protos.google.cloud.gkehub.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `updateFeature()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.gkehub.v1alpha.Feature](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.feature), [protos.google.cloud.gkehub.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The Feature resource name in the format
       *  `projects/* /locations/* /features/*`.
       */
      // const name = 'abc123'
      /**
       *  Mask of fields to update.
       */
      // const updateMask = {}
      /**
       *  Only fields specified in update_mask are updated.
       *  If you specify a field in the update_mask but don't specify its value here
       *  that field will be deleted.
       *  If you are updating a map field, set the value of a key to null or empty
       *  string to delete the key from the map. It's not possible to update a key's
       *  value to the empty string.
       *  If you specify the update_mask to be a special path "*", fully replaces all
       *  user-modifiable fields to match `resource`.
       */
      // const resource = {}
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Gkehub library
      const {GkeHubClient} = require('[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gkehubClient = new [GkeHubClient](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)();
    
      async function callUpdateFeature() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await gkehubClient.updateFeature(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateFeature();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### createFeature(request, options)
    
    
    createFeature(request?: protos.google.cloud.gkehub.v1alpha.ICreateFeatureRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.gkehub.v1alpha.IFeature, protos.google.cloud.gkehub.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Adds a new Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.icreatefeaturerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.gkehub.v1alpha.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ifeature), [protos.google.cloud.gkehub.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The parent (project and location) where the Feature will be created.
       *  Specified in the format `projects/* /locations/*`.
       */
      // const parent = 'abc123'
      /**
       *  The ID of the feature to create.
       */
      // const featureId = 'abc123'
      /**
       *  The Feature resource to create.
       */
      // const resource = {}
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Gkehub library
      const {GkeHubClient} = require('[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gkehubClient = new [GkeHubClient](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)();
    
      async function callCreateFeature() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await gkehubClient.createFeature(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateFeature();
    
    

### createFeature(request, options, callback)
    
    
    createFeature(request: protos.google.cloud.gkehub.v1alpha.ICreateFeatureRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.gkehub.v1alpha.IFeature, protos.google.cloud.gkehub.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.icreatefeaturerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gkehub.v1alpha.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ifeature), [protos.google.cloud.gkehub.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFeature(request, callback)
    
    
    createFeature(request: protos.google.cloud.gkehub.v1alpha.ICreateFeatureRequest, callback: Callback<LROperation<protos.google.cloud.gkehub.v1alpha.IFeature, protos.google.cloud.gkehub.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.icreatefeaturerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gkehub.v1alpha.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ifeature), [protos.google.cloud.gkehub.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFeature(request, options)
    
    
    deleteFeature(request?: protos.google.cloud.gkehub.v1alpha.IDeleteFeatureRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.gkehub.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Removes a Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ideletefeaturerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.protobuf.iempty), [protos.google.cloud.gkehub.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The Feature resource name in the format
       *  `projects/* /locations/* /features/*`.
       */
      // const name = 'abc123'
      /**
       *  If set to true, the delete will ignore any outstanding resources for
       *  this Feature (that is, `FeatureState.has_resources` is set to true). These
       *  resources will NOT be cleaned up or modified in any way.
       */
      // const force = true
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Gkehub library
      const {GkeHubClient} = require('[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gkehubClient = new [GkeHubClient](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)();
    
      async function callDeleteFeature() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await gkehubClient.deleteFeature(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteFeature();
    
    

### deleteFeature(request, options, callback)
    
    
    deleteFeature(request: protos.google.cloud.gkehub.v1alpha.IDeleteFeatureRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.gkehub.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ideletefeaturerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.protobuf.iempty), [protos.google.cloud.gkehub.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFeature(request, callback)
    
    
    deleteFeature(request: protos.google.cloud.gkehub.v1alpha.IDeleteFeatureRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.gkehub.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ideletefeaturerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.protobuf.iempty), [protos.google.cloud.gkehub.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### featurePath(project, location, feature)
    
    
    featurePath(project: string, location: string, feature: string): string;

Return a fully-qualified feature resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`feature` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### getFeature(request, options)
    
    
    getFeature(request?: protos.google.cloud.gkehub.v1alpha.IGetFeatureRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gkehub.v1alpha.IFeature,
            protos.google.cloud.gkehub.v1alpha.IGetFeatureRequest | undefined,
            {} | undefined
        ]>;

Gets details of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.igetfeaturerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gkehub.v1alpha.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ifeature), [protos.google.cloud.gkehub.v1alpha.IGetFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.igetfeaturerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Feature](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.feature). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The Feature resource name in the format
       *  `projects/* /locations/* /features/*`
       */
      // const name = 'abc123'
    
      // Imports the Gkehub library
      const {GkeHubClient} = require('[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gkehubClient = new [GkeHubClient](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)();
    
      async function callGetFeature() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await gkehubClient.getFeature(request);
        console.log(response);
      }
    
      callGetFeature();
    
    

### getFeature(request, options, callback)
    
    
    getFeature(request: protos.google.cloud.gkehub.v1alpha.IGetFeatureRequest, options: CallOptions, callback: Callback<protos.google.cloud.gkehub.v1alpha.IFeature, protos.google.cloud.gkehub.v1alpha.IGetFeatureRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.igetfeaturerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.gkehub.v1alpha.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ifeature), [protos.google.cloud.gkehub.v1alpha.IGetFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.igetfeaturerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFeature(request, callback)
    
    
    getFeature(request: protos.google.cloud.gkehub.v1alpha.IGetFeatureRequest, callback: Callback<protos.google.cloud.gkehub.v1alpha.IFeature, protos.google.cloud.gkehub.v1alpha.IGetFeatureRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.igetfeaturerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.gkehub.v1alpha.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ifeature), [protos.google.cloud.gkehub.v1alpha.IGetFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.igetfeaturerequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listFeatures(request, options)
    
    
    listFeatures(request?: protos.google.cloud.gkehub.v1alpha.IListFeaturesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gkehub.v1alpha.IFeature[],
            protos.google.cloud.gkehub.v1alpha.IListFeaturesRequest | null,
            protos.google.cloud.gkehub.v1alpha.IListFeaturesResponse
        ]>;

Lists Features in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ilistfeaturesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gkehub.v1alpha.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ifeature)[], [protos.google.cloud.gkehub.v1alpha.IListFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ilistfeaturesrequest) | null, [protos.google.cloud.gkehub.v1alpha.IListFeaturesResponse](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ilistfeaturesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Feature](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.feature). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listFeaturesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listFeatures(request, options, callback)
    
    
    listFeatures(request: protos.google.cloud.gkehub.v1alpha.IListFeaturesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.gkehub.v1alpha.IListFeaturesRequest, protos.google.cloud.gkehub.v1alpha.IListFeaturesResponse | null | undefined, protos.google.cloud.gkehub.v1alpha.IFeature>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ilistfeaturesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.gkehub.v1alpha.IListFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ilistfeaturesrequest), [protos.google.cloud.gkehub.v1alpha.IListFeaturesResponse](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ilistfeaturesresponse) | null | undefined, [protos.google.cloud.gkehub.v1alpha.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ifeature)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFeatures(request, callback)
    
    
    listFeatures(request: protos.google.cloud.gkehub.v1alpha.IListFeaturesRequest, callback: PaginationCallback<protos.google.cloud.gkehub.v1alpha.IListFeaturesRequest, protos.google.cloud.gkehub.v1alpha.IListFeaturesResponse | null | undefined, protos.google.cloud.gkehub.v1alpha.IFeature>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ilistfeaturesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.gkehub.v1alpha.IListFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ilistfeaturesrequest), [protos.google.cloud.gkehub.v1alpha.IListFeaturesResponse](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ilistfeaturesresponse) | null | undefined, [protos.google.cloud.gkehub.v1alpha.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ifeature)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFeaturesAsync(request, options)
    
    
    listFeaturesAsync(request?: protos.google.cloud.gkehub.v1alpha.IListFeaturesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.gkehub.v1alpha.IFeature>;

Equivalent to `listFeatures`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ilistfeaturesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.gkehub.v1alpha.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ifeature)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Feature](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.feature). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The parent (project and location) where the Features will be listed.
       *  Specified in the format `projects/* /locations/*`.
       */
      // const parent = 'abc123'
      /**
       *  When requesting a 'page' of resources, `page_size` specifies number of
       *  resources to return. If unspecified or set to 0, all resources will
       *  be returned.
       */
      // const pageSize = 1234
      /**
       *  Token returned by previous call to `ListFeatures` which
       *  specifies the position in the list from where to continue listing the
       *  resources.
       */
      // const pageToken = 'abc123'
      /**
       *  Lists Features that match the filter expression, following the syntax
       *  outlined in https://google.aip.dev/160.
       *  Examples:
       *    - Feature with the name "servicemesh" in project "foo-proj":
       *        name = "projects/foo-proj/locations/global/features/servicemesh"
       *    - Features that have a label called `foo`:
       *        labels.foo:*
       *    - Features that have a label called `foo` whose value is `bar`:
       *        labels.foo = bar
       */
      // const filter = 'abc123'
      /**
       *  One or more fields to compare and use to sort the output.
       *  See https://google.aip.dev/132#ordering.
       */
      // const orderBy = 'abc123'
    
      // Imports the Gkehub library
      const {GkeHubClient} = require('[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gkehubClient = new [GkeHubClient](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)();
    
      async function callListFeatures() {
        // Construct request
        const request = {
        };
    
        // Run request
        const iterable = gkehubClient.listFeaturesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListFeatures();
    
    

### listFeaturesStream(request, options)
    
    
    listFeaturesStream(request?: protos.google.cloud.gkehub.v1alpha.IListFeaturesRequest, options?: CallOptions): Transform;

Equivalent to `listFeatures`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ilistfeaturesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Feature](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.feature) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listFeaturesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### matchFeatureFromFeatureName(featureName)
    
    
    matchFeatureFromFeatureName(featureName: string): string | number;

Parse the feature from Feature resource.

**Parameter**  
---  
**Name** | **Description**  
`featureName` |  `string`   
A fully-qualified path representing Feature resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature.  
  
### matchLocationFromFeatureName(featureName)
    
    
    matchLocationFromFeatureName(featureName: string): string | number;

Parse the location from Feature resource.

**Parameter**  
---  
**Name** | **Description**  
`featureName` |  `string`   
A fully-qualified path representing Feature resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchProjectFromFeatureName(featureName)
    
    
    matchProjectFromFeatureName(featureName: string): string | number;

Parse the project from Feature resource.

**Parameter**  
---  
**Name** | **Description**  
`featureName` |  `string`   
A fully-qualified path representing Feature resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### updateFeature(request, options)
    
    
    updateFeature(request?: protos.google.cloud.gkehub.v1alpha.IUpdateFeatureRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.gkehub.v1alpha.IFeature, protos.google.cloud.gkehub.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates an existing Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.iupdatefeaturerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.gkehub.v1alpha.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ifeature), [protos.google.cloud.gkehub.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The Feature resource name in the format
       *  `projects/* /locations/* /features/*`.
       */
      // const name = 'abc123'
      /**
       *  Mask of fields to update.
       */
      // const updateMask = {}
      /**
       *  Only fields specified in update_mask are updated.
       *  If you specify a field in the update_mask but don't specify its value here
       *  that field will be deleted.
       *  If you are updating a map field, set the value of a key to null or empty
       *  string to delete the key from the map. It's not possible to update a key's
       *  value to the empty string.
       *  If you specify the update_mask to be a special path "*", fully replaces all
       *  user-modifiable fields to match `resource`.
       */
      // const resource = {}
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Gkehub library
      const {GkeHubClient} = require('[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gkehubClient = new [GkeHubClient](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)();
    
      async function callUpdateFeature() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await gkehubClient.updateFeature(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateFeature();
    
    

### updateFeature(request, options, callback)
    
    
    updateFeature(request: protos.google.cloud.gkehub.v1alpha.IUpdateFeatureRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.gkehub.v1alpha.IFeature, protos.google.cloud.gkehub.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.iupdatefeaturerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gkehub.v1alpha.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ifeature), [protos.google.cloud.gkehub.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFeature(request, callback)
    
    
    updateFeature(request: protos.google.cloud.gkehub.v1alpha.IUpdateFeatureRequest, callback: Callback<LROperation<protos.google.cloud.gkehub.v1alpha.IFeature, protos.google.cloud.gkehub.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.iupdatefeaturerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gkehub.v1alpha.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ifeature), [protos.google.cloud.gkehub.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
