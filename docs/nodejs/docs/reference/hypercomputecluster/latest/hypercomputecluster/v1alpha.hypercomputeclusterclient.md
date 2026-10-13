---
url: https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.hypercomputeclusterclient
title: Class v1alpha.HypercomputeClusterClient (0.5.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:49.700530+00:00
---

# Class v1alpha.HypercomputeClusterClient (0.5.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.hypercomputeclusterclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1alpha.HypercomputeClusterClient (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.2.0  0.1.0 

Service describing handlers for resources v1alpha

## Package

[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of HypercomputeClusterClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new HypercomputeClusterClient({fallback: true}, gax); ```  
  
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

### hypercomputeClusterStub
    
    
    hypercomputeClusterStub?: Promise<{
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

### bucketPath(project, bucket)
    
    
    bucketPath(project: string, bucket: string): string;

Return a fully-qualified bucket resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`bucket` |  `string`   
  
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
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### checkCreateClusterProgress(name)
    
    
    checkCreateClusterProgress(name: string): Promise<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.Cluster, protos.google.cloud.hypercomputecluster.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `createCluster()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.Cluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.cluster), [protos.google.cloud.hypercomputecluster.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent location in which the cluster should be created, in the
       *  format `projects/{project}/locations/{location}`.
       */
      // const parent = 'abc123'
      /**
       *  Required. ID of the cluster to create. Must conform to
       *  RFC-1034 (https://datatracker.ietf.org/doc/html/rfc1034) (lower-case,
       *  alphanumeric, and at most 63 characters).
       */
      // const clusterId = 'abc123'
      /**
       *  Required. Cluster to create.
       */
      // const cluster = {}
      /**
       *  Optional. A unique identifier for this request. A random UUID is
       *  recommended. This request is idempotent if and only if `request_id` is
       *  provided.
       */
      // const requestId = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {HypercomputeClusterClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [HypercomputeClusterClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)();
    
      async function callCreateCluster() {
        // Construct request
        const request = {
          parent,
          clusterId,
          cluster,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.createCluster(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateCluster();
    
    

### checkDeleteClusterProgress(name)
    
    
    checkDeleteClusterProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.hypercomputecluster.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `deleteCluster()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.empty), [protos.google.cloud.hypercomputecluster.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the cluster to delete, in the format
       *  `projects/{project}/locations/{location}/clusters/{cluster}`.
       */
      // const name = 'abc123'
      /**
       *  Optional. A unique identifier for this request. A random UUID is
       *  recommended. This request is idempotent if and only if `request_id` is
       *  provided.
       */
      // const requestId = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {HypercomputeClusterClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [HypercomputeClusterClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)();
    
      async function callDeleteCluster() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.deleteCluster(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteCluster();
    
    

### checkUpdateClusterProgress(name)
    
    
    checkUpdateClusterProgress(name: string): Promise<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.Cluster, protos.google.cloud.hypercomputecluster.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `updateCluster()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.Cluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.cluster), [protos.google.cloud.hypercomputecluster.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Cluster to update.
       */
      // const cluster = {}
      /**
       *  Optional. Mask specifying which fields in the cluster to update. All paths
       *  must be specified explicitly - wildcards are not supported. At least one
       *  path must be provided.
       */
      // const updateMask = {}
      /**
       *  Optional. A unique identifier for this request. A random UUID is
       *  recommended. This request is idempotent if and only if `request_id` is
       *  provided.
       */
      // const requestId = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {HypercomputeClusterClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [HypercomputeClusterClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)();
    
      async function callUpdateCluster() {
        // Construct request
        const request = {
          cluster,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.updateCluster(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateCluster();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### clusterPath(project, location, cluster)
    
    
    clusterPath(project: string, location: string, cluster: string): string;

Return a fully-qualified cluster resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`cluster` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### computeInstancePath(project, zone, instance)
    
    
    computeInstancePath(project: string, zone: string, instance: string): string;

Return a fully-qualified computeInstance resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`zone` |  `string`   
  
`instance` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### createCluster(request, options)
    
    
    createCluster(request?: protos.google.cloud.hypercomputecluster.v1alpha.ICreateClusterRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.hypercomputecluster.v1alpha.ICluster, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new Cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icreateclusterrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icluster), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent location in which the cluster should be created, in the
       *  format `projects/{project}/locations/{location}`.
       */
      // const parent = 'abc123'
      /**
       *  Required. ID of the cluster to create. Must conform to
       *  RFC-1034 (https://datatracker.ietf.org/doc/html/rfc1034) (lower-case,
       *  alphanumeric, and at most 63 characters).
       */
      // const clusterId = 'abc123'
      /**
       *  Required. Cluster to create.
       */
      // const cluster = {}
      /**
       *  Optional. A unique identifier for this request. A random UUID is
       *  recommended. This request is idempotent if and only if `request_id` is
       *  provided.
       */
      // const requestId = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {HypercomputeClusterClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [HypercomputeClusterClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)();
    
      async function callCreateCluster() {
        // Construct request
        const request = {
          parent,
          clusterId,
          cluster,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.createCluster(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateCluster();
    
    

### createCluster(request, options, callback)
    
    
    createCluster(request: protos.google.cloud.hypercomputecluster.v1alpha.ICreateClusterRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.ICluster, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icreateclusterrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icluster), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCluster(request, callback)
    
    
    createCluster(request: protos.google.cloud.hypercomputecluster.v1alpha.ICreateClusterRequest, callback: Callback<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.ICluster, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icreateclusterrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icluster), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCluster(request, options)
    
    
    deleteCluster(request?: protos.google.cloud.hypercomputecluster.v1alpha.IDeleteClusterRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ideleteclusterrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.iempty), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the cluster to delete, in the format
       *  `projects/{project}/locations/{location}/clusters/{cluster}`.
       */
      // const name = 'abc123'
      /**
       *  Optional. A unique identifier for this request. A random UUID is
       *  recommended. This request is idempotent if and only if `request_id` is
       *  provided.
       */
      // const requestId = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {HypercomputeClusterClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [HypercomputeClusterClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)();
    
      async function callDeleteCluster() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.deleteCluster(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteCluster();
    
    

### deleteCluster(request, options, callback)
    
    
    deleteCluster(request: protos.google.cloud.hypercomputecluster.v1alpha.IDeleteClusterRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ideleteclusterrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.iempty), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCluster(request, callback)
    
    
    deleteCluster(request: protos.google.cloud.hypercomputecluster.v1alpha.IDeleteClusterRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ideleteclusterrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.iempty), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### diskTypePath(project, zone, diskType)
    
    
    diskTypePath(project: string, zone: string, diskType: string): string;

Return a fully-qualified diskType resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`zone` |  `string`   
  
`diskType` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### getCluster(request, options)
    
    
    getCluster(request?: protos.google.cloud.hypercomputecluster.v1alpha.IGetClusterRequest, options?: CallOptions): Promise<[
            protos.google.cloud.hypercomputecluster.v1alpha.ICluster,
            (protos.google.cloud.hypercomputecluster.v1alpha.IGetClusterRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetclusterrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.hypercomputecluster.v1alpha.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icluster), ([protos.google.cloud.hypercomputecluster.v1alpha.IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetclusterrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Cluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.cluster). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the cluster to retrieve, in the format
       *  `projects/{project}/locations/{location}/clusters/{cluster}`.
       */
      // const name = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {HypercomputeClusterClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [HypercomputeClusterClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)();
    
      async function callGetCluster() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await hypercomputeclusterClient.getCluster(request);
        console.log(response);
      }
    
      callGetCluster();
    
    

### getCluster(request, options, callback)
    
    
    getCluster(request: protos.google.cloud.hypercomputecluster.v1alpha.IGetClusterRequest, options: CallOptions, callback: Callback<protos.google.cloud.hypercomputecluster.v1alpha.ICluster, protos.google.cloud.hypercomputecluster.v1alpha.IGetClusterRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetclusterrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.hypercomputecluster.v1alpha.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icluster), [protos.google.cloud.hypercomputecluster.v1alpha.IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetclusterrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCluster(request, callback)
    
    
    getCluster(request: protos.google.cloud.hypercomputecluster.v1alpha.IGetClusterRequest, callback: Callback<protos.google.cloud.hypercomputecluster.v1alpha.ICluster, protos.google.cloud.hypercomputecluster.v1alpha.IGetClusterRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetclusterrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.hypercomputecluster.v1alpha.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icluster), [protos.google.cloud.hypercomputecluster.v1alpha.IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetclusterrequest) | null | undefined, {} | null | undefined>`   
  
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
    

### getNode(request, options)
    
    
    getNode(request?: protos.google.cloud.hypercomputecluster.v1alpha.IGetNodeRequest, options?: CallOptions): Promise<[
            protos.google.cloud.hypercomputecluster.v1alpha.INode,
            (protos.google.cloud.hypercomputecluster.v1alpha.IGetNodeRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single Node.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetNodeRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetnoderequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.hypercomputecluster.v1alpha.INode](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.inode), ([protos.google.cloud.hypercomputecluster.v1alpha.IGetNodeRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetnoderequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the node to retrieve, in the format
       *  `projects/{project}/locations/{location}/clusters/{cluster}/nodes/{node}`.
       */
      // const name = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {HypercomputeClusterClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [HypercomputeClusterClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)();
    
      async function callGetNode() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await hypercomputeclusterClient.getNode(request);
        console.log(response);
      }
    
      callGetNode();
    
    

### getNode(request, options, callback)
    
    
    getNode(request: protos.google.cloud.hypercomputecluster.v1alpha.IGetNodeRequest, options: CallOptions, callback: Callback<protos.google.cloud.hypercomputecluster.v1alpha.INode, protos.google.cloud.hypercomputecluster.v1alpha.IGetNodeRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetNodeRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetnoderequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.hypercomputecluster.v1alpha.INode](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.inode), [protos.google.cloud.hypercomputecluster.v1alpha.IGetNodeRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetnoderequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getNode(request, callback)
    
    
    getNode(request: protos.google.cloud.hypercomputecluster.v1alpha.IGetNodeRequest, callback: Callback<protos.google.cloud.hypercomputecluster.v1alpha.INode, protos.google.cloud.hypercomputecluster.v1alpha.IGetNodeRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetNodeRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetnoderequest)`   
  
`callback` |  `Callback<[protos.google.cloud.hypercomputecluster.v1alpha.INode](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.inode), [protos.google.cloud.hypercomputecluster.v1alpha.IGetNodeRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetnoderequest) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.operation)]>` |   
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
  
### imagePath(project, image)
    
    
    imagePath(project: string, image: string): string;

Return a fully-qualified image resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`image` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
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
  
### instancePath(project, location, instance)
    
    
    instancePath(project: string, location: string, instance: string): string;

Return a fully-qualified instance resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`instance` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### listClusters(request, options)
    
    
    listClusters(request?: protos.google.cloud.hypercomputecluster.v1alpha.IListClustersRequest, options?: CallOptions): Promise<[
            protos.google.cloud.hypercomputecluster.v1alpha.ICluster[],
            protos.google.cloud.hypercomputecluster.v1alpha.IListClustersRequest | null,
            protos.google.cloud.hypercomputecluster.v1alpha.IListClustersResponse
        ]>;

Lists Clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistclustersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.hypercomputecluster.v1alpha.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icluster)[], [protos.google.cloud.hypercomputecluster.v1alpha.IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistclustersrequest) | null, [protos.google.cloud.hypercomputecluster.v1alpha.IListClustersResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistclustersresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Cluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.cluster). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listClustersAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listClusters(request, options, callback)
    
    
    listClusters(request: protos.google.cloud.hypercomputecluster.v1alpha.IListClustersRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.hypercomputecluster.v1alpha.IListClustersRequest, protos.google.cloud.hypercomputecluster.v1alpha.IListClustersResponse | null | undefined, protos.google.cloud.hypercomputecluster.v1alpha.ICluster>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistclustersrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.hypercomputecluster.v1alpha.IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistclustersrequest), [protos.google.cloud.hypercomputecluster.v1alpha.IListClustersResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistclustersresponse) | null | undefined, [protos.google.cloud.hypercomputecluster.v1alpha.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icluster)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listClusters(request, callback)
    
    
    listClusters(request: protos.google.cloud.hypercomputecluster.v1alpha.IListClustersRequest, callback: PaginationCallback<protos.google.cloud.hypercomputecluster.v1alpha.IListClustersRequest, protos.google.cloud.hypercomputecluster.v1alpha.IListClustersResponse | null | undefined, protos.google.cloud.hypercomputecluster.v1alpha.ICluster>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistclustersrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.hypercomputecluster.v1alpha.IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistclustersrequest), [protos.google.cloud.hypercomputecluster.v1alpha.IListClustersResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistclustersresponse) | null | undefined, [protos.google.cloud.hypercomputecluster.v1alpha.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icluster)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listClustersAsync(request, options)
    
    
    listClustersAsync(request?: protos.google.cloud.hypercomputecluster.v1alpha.IListClustersRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.hypercomputecluster.v1alpha.ICluster>;

Equivalent to `listClusters`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistclustersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.hypercomputecluster.v1alpha.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icluster)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Cluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.cluster). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent location of the clusters to list, in the format
       *  `projects/{project}/locations/{location}`.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Maximum number of clusters to return. The service may return
       *  fewer than this value.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token received from a previous `ListClusters` call.
       *  Provide this to retrieve the subsequent page. When paginating, all other
       *  parameters provided to `ListClusters` must match the call that provided the
       *  page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filter (https://google.aip.dev/160) to apply to the returned
       *  results.
       */
      // const filter = 'abc123'
      /**
       *  Optional. How to order the resulting clusters. Must be one of the following
       *  strings:
       *  * `name`
       *  * `name desc`
       *  * `create_time`
       *  * `create_time desc`
       *  If not specified, clusters will be returned in an arbitrary order.
       */
      // const orderBy = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {HypercomputeClusterClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [HypercomputeClusterClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)();
    
      async function callListClusters() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = hypercomputeclusterClient.listClustersAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListClusters();
    
    

### listClustersStream(request, options)
    
    
    listClustersStream(request?: protos.google.cloud.hypercomputecluster.v1alpha.IListClustersRequest, options?: CallOptions): Transform;

Equivalent to `listClusters`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistclustersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Cluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.cluster) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listClustersAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
    

### listNodes(request, options)
    
    
    listNodes(request?: protos.google.cloud.hypercomputecluster.v1alpha.IListNodesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.hypercomputecluster.v1alpha.INode[],
            protos.google.cloud.hypercomputecluster.v1alpha.IListNodesRequest | null,
            protos.google.cloud.hypercomputecluster.v1alpha.IListNodesResponse
        ]>;

Lists Nodes in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListNodesRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistnodesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.hypercomputecluster.v1alpha.INode](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.inode)[], [protos.google.cloud.hypercomputecluster.v1alpha.IListNodesRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistnodesrequest) | null, [protos.google.cloud.hypercomputecluster.v1alpha.IListNodesResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistnodesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listNodesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listNodes(request, options, callback)
    
    
    listNodes(request: protos.google.cloud.hypercomputecluster.v1alpha.IListNodesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.hypercomputecluster.v1alpha.IListNodesRequest, protos.google.cloud.hypercomputecluster.v1alpha.IListNodesResponse | null | undefined, protos.google.cloud.hypercomputecluster.v1alpha.INode>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListNodesRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistnodesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.hypercomputecluster.v1alpha.IListNodesRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistnodesrequest), [protos.google.cloud.hypercomputecluster.v1alpha.IListNodesResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistnodesresponse) | null | undefined, [protos.google.cloud.hypercomputecluster.v1alpha.INode](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.inode)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listNodes(request, callback)
    
    
    listNodes(request: protos.google.cloud.hypercomputecluster.v1alpha.IListNodesRequest, callback: PaginationCallback<protos.google.cloud.hypercomputecluster.v1alpha.IListNodesRequest, protos.google.cloud.hypercomputecluster.v1alpha.IListNodesResponse | null | undefined, protos.google.cloud.hypercomputecluster.v1alpha.INode>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListNodesRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistnodesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.hypercomputecluster.v1alpha.IListNodesRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistnodesrequest), [protos.google.cloud.hypercomputecluster.v1alpha.IListNodesResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistnodesresponse) | null | undefined, [protos.google.cloud.hypercomputecluster.v1alpha.INode](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.inode)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listNodesAsync(request, options)
    
    
    listNodesAsync(request?: protos.google.cloud.hypercomputecluster.v1alpha.IListNodesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.hypercomputecluster.v1alpha.INode>;

Equivalent to `listNodes`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListNodesRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistnodesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.hypercomputecluster.v1alpha.INode](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.inode)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent cluster of the nodes to list, in the format
       *  `projects/{project}/locations/{location}/clusters/{cluster}`.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Maximum number of nodes to return. The service may return fewer
       *  than this value.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token received from a previous `ListNodes` call. Provide
       *  this to retrieve the subsequent page. When paginating, all other parameters
       *  provided to `ListNodes` must match the call that provided the page
       *  token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filter (https://google.aip.dev/160) to apply to the returned
       *  results.
       */
      // const filter = 'abc123'
      /**
       *  Optional. How to order the resulting nodes. Must be one of the following
       *  strings:
       *  * `name`
       *  * `name desc`
       *  If not specified, nodes will be returned in an arbitrary order.
       */
      // const orderBy = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {HypercomputeClusterClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [HypercomputeClusterClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)();
    
      async function callListNodes() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = hypercomputeclusterClient.[listNodesAsync](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.hypercomputeclusterclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListNodes();
    
    

### listNodesStream(request, options)
    
    
    listNodesStream(request?: protos.google.cloud.hypercomputecluster.v1alpha.IListNodesRequest, options?: CallOptions): Transform;

Equivalent to `listNodes`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListNodesRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistnodesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listNodesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listOperationsAsync(request, options)
    
    
    listOperationsAsync(request: protos.google.longrunning.ListOperationsRequest, options?: gax.CallOptions): AsyncIterable<protos.google.longrunning.IOperation>;

Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. Returns an iterable object.

For-await-of syntax is used with the iterable to recursively get response element on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
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
  
### machineLearningRunPath(project, location, machineLearningRun)
    
    
    machineLearningRunPath(project: string, location: string, machineLearningRun: string): string;

Return a fully-qualified machineLearningRun resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`machineLearningRun` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### matchBucketFromBucketName(bucketName)
    
    
    matchBucketFromBucketName(bucketName: string): string | number;

Parse the bucket from Bucket resource.

**Parameter**  
---  
**Name** | **Description**  
`bucketName` |  `string`   
A fully-qualified path representing Bucket resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the bucket.  
  
### matchClusterFromClusterName(clusterName)
    
    
    matchClusterFromClusterName(clusterName: string): string | number;

Parse the cluster from Cluster resource.

**Parameter**  
---  
**Name** | **Description**  
`clusterName` |  `string`   
A fully-qualified path representing Cluster resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the cluster.  
  
### matchClusterFromNodeName(nodeName)
    
    
    matchClusterFromNodeName(nodeName: string): string | number;

Parse the cluster from Node resource.

**Parameter**  
---  
**Name** | **Description**  
`nodeName` |  `string`   
A fully-qualified path representing Node resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the cluster.  
  
### matchClusterFromPodName(podName)
    
    
    matchClusterFromPodName(podName: string): string | number;

Parse the cluster from Pod resource.

**Parameter**  
---  
**Name** | **Description**  
`podName` |  `string`   
A fully-qualified path representing Pod resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the cluster.  
  
### matchDiskTypeFromDiskTypeName(diskTypeName)
    
    
    matchDiskTypeFromDiskTypeName(diskTypeName: string): string | number;

Parse the disk_type from DiskType resource.

**Parameter**  
---  
**Name** | **Description**  
`diskTypeName` |  `string`   
A fully-qualified path representing DiskType resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the disk_type.  
  
### matchImageFromImageName(imageName)
    
    
    matchImageFromImageName(imageName: string): string | number;

Parse the image from Image resource.

**Parameter**  
---  
**Name** | **Description**  
`imageName` |  `string`   
A fully-qualified path representing Image resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the image.  
  
### matchInstanceFromComputeInstanceName(computeInstanceName)
    
    
    matchInstanceFromComputeInstanceName(computeInstanceName: string): string | number;

Parse the instance from ComputeInstance resource.

**Parameter**  
---  
**Name** | **Description**  
`computeInstanceName` |  `string`   
A fully-qualified path representing ComputeInstance resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the instance.  
  
### matchInstanceFromInstanceName(instanceName)
    
    
    matchInstanceFromInstanceName(instanceName: string): string | number;

Parse the instance from Instance resource.

**Parameter**  
---  
**Name** | **Description**  
`instanceName` |  `string`   
A fully-qualified path representing Instance resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the instance.  
  
### matchLocationFromClusterName(clusterName)
    
    
    matchLocationFromClusterName(clusterName: string): string | number;

Parse the location from Cluster resource.

**Parameter**  
---  
**Name** | **Description**  
`clusterName` |  `string`   
A fully-qualified path representing Cluster resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromInstanceName(instanceName)
    
    
    matchLocationFromInstanceName(instanceName: string): string | number;

Parse the location from Instance resource.

**Parameter**  
---  
**Name** | **Description**  
`instanceName` |  `string`   
A fully-qualified path representing Instance resource.  
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
  
### matchLocationFromMachineLearningRunName(machineLearningRunName)
    
    
    matchLocationFromMachineLearningRunName(machineLearningRunName: string): string | number;

Parse the location from MachineLearningRun resource.

**Parameter**  
---  
**Name** | **Description**  
`machineLearningRunName` |  `string`   
A fully-qualified path representing MachineLearningRun resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromMonitoredEventName(monitoredEventName)
    
    
    matchLocationFromMonitoredEventName(monitoredEventName: string): string | number;

Parse the location from MonitoredEvent resource.

**Parameter**  
---  
**Name** | **Description**  
`monitoredEventName` |  `string`   
A fully-qualified path representing MonitoredEvent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromNodeName(nodeName)
    
    
    matchLocationFromNodeName(nodeName: string): string | number;

Parse the location from Node resource.

**Parameter**  
---  
**Name** | **Description**  
`nodeName` |  `string`   
A fully-qualified path representing Node resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromPodName(podName)
    
    
    matchLocationFromPodName(podName: string): string | number;

Parse the location from Pod resource.

**Parameter**  
---  
**Name** | **Description**  
`podName` |  `string`   
A fully-qualified path representing Pod resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProfilerSessionName(profilerSessionName)
    
    
    matchLocationFromProfilerSessionName(profilerSessionName: string): string | number;

Parse the location from ProfilerSession resource.

**Parameter**  
---  
**Name** | **Description**  
`profilerSessionName` |  `string`   
A fully-qualified path representing ProfilerSession resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProfilerTargetName(profilerTargetName)
    
    
    matchLocationFromProfilerTargetName(profilerTargetName: string): string | number;

Parse the location from ProfilerTarget resource.

**Parameter**  
---  
**Name** | **Description**  
`profilerTargetName` |  `string`   
A fully-qualified path representing ProfilerTarget resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProfileSessionName(profileSessionName)
    
    
    matchLocationFromProfileSessionName(profileSessionName: string): string | number;

Parse the location from ProfileSession resource.

**Parameter**  
---  
**Name** | **Description**  
`profileSessionName` |  `string`   
A fully-qualified path representing ProfileSession resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchMachineLearningRunFromMachineLearningRunName(machineLearningRunName)
    
    
    matchMachineLearningRunFromMachineLearningRunName(machineLearningRunName: string): string | number;

Parse the machine_learning_run from MachineLearningRun resource.

**Parameter**  
---  
**Name** | **Description**  
`machineLearningRunName` |  `string`   
A fully-qualified path representing MachineLearningRun resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the machine_learning_run.  
  
### matchMachineLearningRunFromMonitoredEventName(monitoredEventName)
    
    
    matchMachineLearningRunFromMonitoredEventName(monitoredEventName: string): string | number;

Parse the machine_learning_run from MonitoredEvent resource.

**Parameter**  
---  
**Name** | **Description**  
`monitoredEventName` |  `string`   
A fully-qualified path representing MonitoredEvent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the machine_learning_run.  
  
### matchMachineLearningRunFromProfilerSessionName(profilerSessionName)
    
    
    matchMachineLearningRunFromProfilerSessionName(profilerSessionName: string): string | number;

Parse the machine_learning_run from ProfilerSession resource.

**Parameter**  
---  
**Name** | **Description**  
`profilerSessionName` |  `string`   
A fully-qualified path representing ProfilerSession resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the machine_learning_run.  
  
### matchMachineLearningRunFromProfilerTargetName(profilerTargetName)
    
    
    matchMachineLearningRunFromProfilerTargetName(profilerTargetName: string): string | number;

Parse the machine_learning_run from ProfilerTarget resource.

**Parameter**  
---  
**Name** | **Description**  
`profilerTargetName` |  `string`   
A fully-qualified path representing ProfilerTarget resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the machine_learning_run.  
  
### matchMachineLearningRunFromProfileSessionName(profileSessionName)
    
    
    matchMachineLearningRunFromProfileSessionName(profileSessionName: string): string | number;

Parse the machine_learning_run from ProfileSession resource.

**Parameter**  
---  
**Name** | **Description**  
`profileSessionName` |  `string`   
A fully-qualified path representing ProfileSession resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the machine_learning_run.  
  
### matchMonitoredEventFromMonitoredEventName(monitoredEventName)
    
    
    matchMonitoredEventFromMonitoredEventName(monitoredEventName: string): string | number;

Parse the monitored_event from MonitoredEvent resource.

**Parameter**  
---  
**Name** | **Description**  
`monitoredEventName` |  `string`   
A fully-qualified path representing MonitoredEvent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the monitored_event.  
  
### matchNamespaceFromPodName(podName)
    
    
    matchNamespaceFromPodName(podName: string): string | number;

Parse the namespace from Pod resource.

**Parameter**  
---  
**Name** | **Description**  
`podName` |  `string`   
A fully-qualified path representing Pod resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the namespace.  
  
### matchNetworkFromNetworkName(networkName)
    
    
    matchNetworkFromNetworkName(networkName: string): string | number;

Parse the network from Network resource.

**Parameter**  
---  
**Name** | **Description**  
`networkName` |  `string`   
A fully-qualified path representing Network resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the network.  
  
### matchNodeFromNodeName(nodeName)
    
    
    matchNodeFromNodeName(nodeName: string): string | number;

Parse the node from Node resource.

**Parameter**  
---  
**Name** | **Description**  
`nodeName` |  `string`   
A fully-qualified path representing Node resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the node.  
  
### matchPodFromPodName(podName)
    
    
    matchPodFromPodName(podName: string): string | number;

Parse the pod from Pod resource.

**Parameter**  
---  
**Name** | **Description**  
`podName` |  `string`   
A fully-qualified path representing Pod resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the pod.  
  
### matchProfilerSessionFromProfilerSessionName(profilerSessionName)
    
    
    matchProfilerSessionFromProfilerSessionName(profilerSessionName: string): string | number;

Parse the profiler_session from ProfilerSession resource.

**Parameter**  
---  
**Name** | **Description**  
`profilerSessionName` |  `string`   
A fully-qualified path representing ProfilerSession resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the profiler_session.  
  
### matchProfilerTargetFromProfilerTargetName(profilerTargetName)
    
    
    matchProfilerTargetFromProfilerTargetName(profilerTargetName: string): string | number;

Parse the profiler_target from ProfilerTarget resource.

**Parameter**  
---  
**Name** | **Description**  
`profilerTargetName` |  `string`   
A fully-qualified path representing ProfilerTarget resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the profiler_target.  
  
### matchProfileSessionFromProfileSessionName(profileSessionName)
    
    
    matchProfileSessionFromProfileSessionName(profileSessionName: string): string | number;

Parse the profile_session from ProfileSession resource.

**Parameter**  
---  
**Name** | **Description**  
`profileSessionName` |  `string`   
A fully-qualified path representing ProfileSession resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the profile_session.  
  
### matchProjectFromBucketName(bucketName)
    
    
    matchProjectFromBucketName(bucketName: string): string | number;

Parse the project from Bucket resource.

**Parameter**  
---  
**Name** | **Description**  
`bucketName` |  `string`   
A fully-qualified path representing Bucket resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromClusterName(clusterName)
    
    
    matchProjectFromClusterName(clusterName: string): string | number;

Parse the project from Cluster resource.

**Parameter**  
---  
**Name** | **Description**  
`clusterName` |  `string`   
A fully-qualified path representing Cluster resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromComputeInstanceName(computeInstanceName)
    
    
    matchProjectFromComputeInstanceName(computeInstanceName: string): string | number;

Parse the project from ComputeInstance resource.

**Parameter**  
---  
**Name** | **Description**  
`computeInstanceName` |  `string`   
A fully-qualified path representing ComputeInstance resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromDiskTypeName(diskTypeName)
    
    
    matchProjectFromDiskTypeName(diskTypeName: string): string | number;

Parse the project from DiskType resource.

**Parameter**  
---  
**Name** | **Description**  
`diskTypeName` |  `string`   
A fully-qualified path representing DiskType resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromImageName(imageName)
    
    
    matchProjectFromImageName(imageName: string): string | number;

Parse the project from Image resource.

**Parameter**  
---  
**Name** | **Description**  
`imageName` |  `string`   
A fully-qualified path representing Image resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromInstanceName(instanceName)
    
    
    matchProjectFromInstanceName(instanceName: string): string | number;

Parse the project from Instance resource.

**Parameter**  
---  
**Name** | **Description**  
`instanceName` |  `string`   
A fully-qualified path representing Instance resource.  
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
  
### matchProjectFromMachineLearningRunName(machineLearningRunName)
    
    
    matchProjectFromMachineLearningRunName(machineLearningRunName: string): string | number;

Parse the project from MachineLearningRun resource.

**Parameter**  
---  
**Name** | **Description**  
`machineLearningRunName` |  `string`   
A fully-qualified path representing MachineLearningRun resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromMonitoredEventName(monitoredEventName)
    
    
    matchProjectFromMonitoredEventName(monitoredEventName: string): string | number;

Parse the project from MonitoredEvent resource.

**Parameter**  
---  
**Name** | **Description**  
`monitoredEventName` |  `string`   
A fully-qualified path representing MonitoredEvent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromNetworkName(networkName)
    
    
    matchProjectFromNetworkName(networkName: string): string | number;

Parse the project from Network resource.

**Parameter**  
---  
**Name** | **Description**  
`networkName` |  `string`   
A fully-qualified path representing Network resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromNodeName(nodeName)
    
    
    matchProjectFromNodeName(nodeName: string): string | number;

Parse the project from Node resource.

**Parameter**  
---  
**Name** | **Description**  
`nodeName` |  `string`   
A fully-qualified path representing Node resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromPodName(podName)
    
    
    matchProjectFromPodName(podName: string): string | number;

Parse the project from Pod resource.

**Parameter**  
---  
**Name** | **Description**  
`podName` |  `string`   
A fully-qualified path representing Pod resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProfilerSessionName(profilerSessionName)
    
    
    matchProjectFromProfilerSessionName(profilerSessionName: string): string | number;

Parse the project from ProfilerSession resource.

**Parameter**  
---  
**Name** | **Description**  
`profilerSessionName` |  `string`   
A fully-qualified path representing ProfilerSession resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProfilerTargetName(profilerTargetName)
    
    
    matchProjectFromProfilerTargetName(profilerTargetName: string): string | number;

Parse the project from ProfilerTarget resource.

**Parameter**  
---  
**Name** | **Description**  
`profilerTargetName` |  `string`   
A fully-qualified path representing ProfilerTarget resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProfileSessionName(profileSessionName)
    
    
    matchProjectFromProfileSessionName(profileSessionName: string): string | number;

Parse the project from ProfileSession resource.

**Parameter**  
---  
**Name** | **Description**  
`profileSessionName` |  `string`   
A fully-qualified path representing ProfileSession resource.  
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
  
### matchProjectFromReservationBlockName(reservationBlockName)
    
    
    matchProjectFromReservationBlockName(reservationBlockName: string): string | number;

Parse the project from ReservationBlock resource.

**Parameter**  
---  
**Name** | **Description**  
`reservationBlockName` |  `string`   
A fully-qualified path representing ReservationBlock resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromReservationName(reservationName)
    
    
    matchProjectFromReservationName(reservationName: string): string | number;

Parse the project from Reservation resource.

**Parameter**  
---  
**Name** | **Description**  
`reservationName` |  `string`   
A fully-qualified path representing Reservation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromReservationSubBlockName(reservationSubBlockName)
    
    
    matchProjectFromReservationSubBlockName(reservationSubBlockName: string): string | number;

Parse the project from ReservationSubBlock resource.

**Parameter**  
---  
**Name** | **Description**  
`reservationSubBlockName` |  `string`   
A fully-qualified path representing ReservationSubBlock resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSubnetworkName(subnetworkName)
    
    
    matchProjectFromSubnetworkName(subnetworkName: string): string | number;

Parse the project from Subnetwork resource.

**Parameter**  
---  
**Name** | **Description**  
`subnetworkName` |  `string`   
A fully-qualified path representing Subnetwork resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchRegionFromSubnetworkName(subnetworkName)
    
    
    matchRegionFromSubnetworkName(subnetworkName: string): string | number;

Parse the region from Subnetwork resource.

**Parameter**  
---  
**Name** | **Description**  
`subnetworkName` |  `string`   
A fully-qualified path representing Subnetwork resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the region.  
  
### matchReservationBlockFromReservationBlockName(reservationBlockName)
    
    
    matchReservationBlockFromReservationBlockName(reservationBlockName: string): string | number;

Parse the reservation_block from ReservationBlock resource.

**Parameter**  
---  
**Name** | **Description**  
`reservationBlockName` |  `string`   
A fully-qualified path representing ReservationBlock resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the reservation_block.  
  
### matchReservationBlockFromReservationSubBlockName(reservationSubBlockName)
    
    
    matchReservationBlockFromReservationSubBlockName(reservationSubBlockName: string): string | number;

Parse the reservation_block from ReservationSubBlock resource.

**Parameter**  
---  
**Name** | **Description**  
`reservationSubBlockName` |  `string`   
A fully-qualified path representing ReservationSubBlock resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the reservation_block.  
  
### matchReservationFromReservationBlockName(reservationBlockName)
    
    
    matchReservationFromReservationBlockName(reservationBlockName: string): string | number;

Parse the reservation from ReservationBlock resource.

**Parameter**  
---  
**Name** | **Description**  
`reservationBlockName` |  `string`   
A fully-qualified path representing ReservationBlock resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the reservation.  
  
### matchReservationFromReservationName(reservationName)
    
    
    matchReservationFromReservationName(reservationName: string): string | number;

Parse the reservation from Reservation resource.

**Parameter**  
---  
**Name** | **Description**  
`reservationName` |  `string`   
A fully-qualified path representing Reservation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the reservation.  
  
### matchReservationFromReservationSubBlockName(reservationSubBlockName)
    
    
    matchReservationFromReservationSubBlockName(reservationSubBlockName: string): string | number;

Parse the reservation from ReservationSubBlock resource.

**Parameter**  
---  
**Name** | **Description**  
`reservationSubBlockName` |  `string`   
A fully-qualified path representing ReservationSubBlock resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the reservation.  
  
### matchReservationSubBlockFromReservationSubBlockName(reservationSubBlockName)
    
    
    matchReservationSubBlockFromReservationSubBlockName(reservationSubBlockName: string): string | number;

Parse the reservation_sub_block from ReservationSubBlock resource.

**Parameter**  
---  
**Name** | **Description**  
`reservationSubBlockName` |  `string`   
A fully-qualified path representing ReservationSubBlock resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the reservation_sub_block.  
  
### matchSubnetworkFromSubnetworkName(subnetworkName)
    
    
    matchSubnetworkFromSubnetworkName(subnetworkName: string): string | number;

Parse the subnetwork from Subnetwork resource.

**Parameter**  
---  
**Name** | **Description**  
`subnetworkName` |  `string`   
A fully-qualified path representing Subnetwork resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the subnetwork.  
  
### matchZoneFromComputeInstanceName(computeInstanceName)
    
    
    matchZoneFromComputeInstanceName(computeInstanceName: string): string | number;

Parse the zone from ComputeInstance resource.

**Parameter**  
---  
**Name** | **Description**  
`computeInstanceName` |  `string`   
A fully-qualified path representing ComputeInstance resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the zone.  
  
### matchZoneFromDiskTypeName(diskTypeName)
    
    
    matchZoneFromDiskTypeName(diskTypeName: string): string | number;

Parse the zone from DiskType resource.

**Parameter**  
---  
**Name** | **Description**  
`diskTypeName` |  `string`   
A fully-qualified path representing DiskType resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the zone.  
  
### matchZoneFromReservationBlockName(reservationBlockName)
    
    
    matchZoneFromReservationBlockName(reservationBlockName: string): string | number;

Parse the zone from ReservationBlock resource.

**Parameter**  
---  
**Name** | **Description**  
`reservationBlockName` |  `string`   
A fully-qualified path representing ReservationBlock resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the zone.  
  
### matchZoneFromReservationName(reservationName)
    
    
    matchZoneFromReservationName(reservationName: string): string | number;

Parse the zone from Reservation resource.

**Parameter**  
---  
**Name** | **Description**  
`reservationName` |  `string`   
A fully-qualified path representing Reservation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the zone.  
  
### matchZoneFromReservationSubBlockName(reservationSubBlockName)
    
    
    matchZoneFromReservationSubBlockName(reservationSubBlockName: string): string | number;

Parse the zone from ReservationSubBlock resource.

**Parameter**  
---  
**Name** | **Description**  
`reservationSubBlockName` |  `string`   
A fully-qualified path representing ReservationSubBlock resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the zone.  
  
### monitoredEventPath(project, location, machineLearningRun, monitoredEvent)
    
    
    monitoredEventPath(project: string, location: string, machineLearningRun: string, monitoredEvent: string): string;

Return a fully-qualified monitoredEvent resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`machineLearningRun` |  `string`   
  
`monitoredEvent` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### networkPath(project, network)
    
    
    networkPath(project: string, network: string): string;

Return a fully-qualified network resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`network` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### nodePath(project, location, cluster, node)
    
    
    nodePath(project: string, location: string, cluster: string, node: string): string;

Return a fully-qualified node resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`cluster` |  `string`   
  
`node` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### podPath(project, location, cluster, namespace, pod)
    
    
    podPath(project: string, location: string, cluster: string, namespace: string, pod: string): string;

Return a fully-qualified pod resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`cluster` |  `string`   
  
`namespace` |  `string`   
  
`pod` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### profilerSessionPath(project, location, machineLearningRun, profilerSession)
    
    
    profilerSessionPath(project: string, location: string, machineLearningRun: string, profilerSession: string): string;

Return a fully-qualified profilerSession resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`machineLearningRun` |  `string`   
  
`profilerSession` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### profilerTargetPath(project, location, machineLearningRun, profilerTarget)
    
    
    profilerTargetPath(project: string, location: string, machineLearningRun: string, profilerTarget: string): string;

Return a fully-qualified profilerTarget resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`machineLearningRun` |  `string`   
  
`profilerTarget` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### profileSessionPath(project, location, machineLearningRun, profileSession)
    
    
    profileSessionPath(project: string, location: string, machineLearningRun: string, profileSession: string): string;

Return a fully-qualified profileSession resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`machineLearningRun` |  `string`   
  
`profileSession` |  `string`   
  
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
  
### reservationBlockPath(project, zone, reservation, reservationBlock)
    
    
    reservationBlockPath(project: string, zone: string, reservation: string, reservationBlock: string): string;

Return a fully-qualified reservationBlock resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`zone` |  `string`   
  
`reservation` |  `string`   
  
`reservationBlock` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### reservationPath(project, zone, reservation)
    
    
    reservationPath(project: string, zone: string, reservation: string): string;

Return a fully-qualified reservation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`zone` |  `string`   
  
`reservation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### reservationSubBlockPath(project, zone, reservation, reservationBlock, reservationSubBlock)
    
    
    reservationSubBlockPath(project: string, zone: string, reservation: string, reservationBlock: string, reservationSubBlock: string): string;

Return a fully-qualified reservationSubBlock resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`zone` |  `string`   
  
`reservation` |  `string`   
  
`reservationBlock` |  `string`   
  
`reservationSubBlock` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### subnetworkPath(project, region, subnetwork)
    
    
    subnetworkPath(project: string, region: string, subnetwork: string): string;

Return a fully-qualified subnetwork resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`region` |  `string`   
  
`subnetwork` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### updateCluster(request, options)
    
    
    updateCluster(request?: protos.google.cloud.hypercomputecluster.v1alpha.IUpdateClusterRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.hypercomputecluster.v1alpha.ICluster, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the parameters of a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iupdateclusterrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icluster), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Cluster to update.
       */
      // const cluster = {}
      /**
       *  Optional. Mask specifying which fields in the cluster to update. All paths
       *  must be specified explicitly - wildcards are not supported. At least one
       *  path must be provided.
       */
      // const updateMask = {}
      /**
       *  Optional. A unique identifier for this request. A random UUID is
       *  recommended. This request is idempotent if and only if `request_id` is
       *  provided.
       */
      // const requestId = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {HypercomputeClusterClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [HypercomputeClusterClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)();
    
      async function callUpdateCluster() {
        // Construct request
        const request = {
          cluster,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.updateCluster(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateCluster();
    
    

### updateCluster(request, options, callback)
    
    
    updateCluster(request: protos.google.cloud.hypercomputecluster.v1alpha.IUpdateClusterRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.ICluster, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iupdateclusterrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icluster), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCluster(request, callback)
    
    
    updateCluster(request: protos.google.cloud.hypercomputecluster.v1alpha.IUpdateClusterRequest, callback: Callback<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.ICluster, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iupdateclusterrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icluster), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
