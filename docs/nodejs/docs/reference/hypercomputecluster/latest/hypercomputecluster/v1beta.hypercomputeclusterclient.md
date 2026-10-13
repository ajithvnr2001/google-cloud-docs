---
url: https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1beta.hypercomputeclusterclient
title: Class v1beta.HypercomputeClusterClient (0.5.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:35.054724+00:00
---

# Class v1beta.HypercomputeClusterClient (0.5.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1beta.hypercomputeclusterclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.HypercomputeClusterClient (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.2.0  0.1.0 

Service describing handlers for resources v1beta

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
    
    
    checkCreateClusterProgress(name: string): Promise<LROperation<protos.google.cloud.hypercomputecluster.v1beta.Cluster, protos.google.cloud.hypercomputecluster.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `createCluster()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.hypercomputecluster.v1beta.Cluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.cluster), [protos.google.cloud.hypercomputecluster.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
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
      const {HypercomputeClusterClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1beta;
    
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
    
    
    checkDeleteClusterProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.hypercomputecluster.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `deleteCluster()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.empty), [protos.google.cloud.hypercomputecluster.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
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
      const {HypercomputeClusterClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1beta;
    
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
    
    
    checkUpdateClusterProgress(name: string): Promise<LROperation<protos.google.cloud.hypercomputecluster.v1beta.Cluster, protos.google.cloud.hypercomputecluster.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `updateCluster()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.hypercomputecluster.v1beta.Cluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.cluster), [protos.google.cloud.hypercomputecluster.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
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
      const {HypercomputeClusterClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1beta;
    
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
    
    
    createCluster(request?: protos.google.cloud.hypercomputecluster.v1beta.ICreateClusterRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.hypercomputecluster.v1beta.ICluster, protos.google.cloud.hypercomputecluster.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new Cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.icreateclusterrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.hypercomputecluster.v1beta.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.icluster), [protos.google.cloud.hypercomputecluster.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
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
      const {HypercomputeClusterClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1beta;
    
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
    
    
    createCluster(request: protos.google.cloud.hypercomputecluster.v1beta.ICreateClusterRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.hypercomputecluster.v1beta.ICluster, protos.google.cloud.hypercomputecluster.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.icreateclusterrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.hypercomputecluster.v1beta.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.icluster), [protos.google.cloud.hypercomputecluster.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCluster(request, callback)
    
    
    createCluster(request: protos.google.cloud.hypercomputecluster.v1beta.ICreateClusterRequest, callback: Callback<LROperation<protos.google.cloud.hypercomputecluster.v1beta.ICluster, protos.google.cloud.hypercomputecluster.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.icreateclusterrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.hypercomputecluster.v1beta.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.icluster), [protos.google.cloud.hypercomputecluster.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCluster(request, options)
    
    
    deleteCluster(request?: protos.google.cloud.hypercomputecluster.v1beta.IDeleteClusterRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.hypercomputecluster.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ideleteclusterrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.iempty), [protos.google.cloud.hypercomputecluster.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
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
      const {HypercomputeClusterClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1beta;
    
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
    
    
    deleteCluster(request: protos.google.cloud.hypercomputecluster.v1beta.IDeleteClusterRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.hypercomputecluster.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ideleteclusterrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.iempty), [protos.google.cloud.hypercomputecluster.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCluster(request, callback)
    
    
    deleteCluster(request: protos.google.cloud.hypercomputecluster.v1beta.IDeleteClusterRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.hypercomputecluster.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ideleteclusterrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.iempty), [protos.google.cloud.hypercomputecluster.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
    
    
    getCluster(request?: protos.google.cloud.hypercomputecluster.v1beta.IGetClusterRequest, options?: CallOptions): Promise<[
            protos.google.cloud.hypercomputecluster.v1beta.ICluster,
            (protos.google.cloud.hypercomputecluster.v1beta.IGetClusterRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.igetclusterrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.hypercomputecluster.v1beta.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.icluster), ([protos.google.cloud.hypercomputecluster.v1beta.IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.igetclusterrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Cluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.cluster). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
      const {HypercomputeClusterClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1beta;
    
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
    
    
    getCluster(request: protos.google.cloud.hypercomputecluster.v1beta.IGetClusterRequest, options: CallOptions, callback: Callback<protos.google.cloud.hypercomputecluster.v1beta.ICluster, protos.google.cloud.hypercomputecluster.v1beta.IGetClusterRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.igetclusterrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.hypercomputecluster.v1beta.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.icluster), [protos.google.cloud.hypercomputecluster.v1beta.IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.igetclusterrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCluster(request, callback)
    
    
    getCluster(request: protos.google.cloud.hypercomputecluster.v1beta.IGetClusterRequest, callback: Callback<protos.google.cloud.hypercomputecluster.v1beta.ICluster, protos.google.cloud.hypercomputecluster.v1beta.IGetClusterRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.igetclusterrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.hypercomputecluster.v1beta.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.icluster), [protos.google.cloud.hypercomputecluster.v1beta.IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.igetclusterrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listClusters(request, options)
    
    
    listClusters(request?: protos.google.cloud.hypercomputecluster.v1beta.IListClustersRequest, options?: CallOptions): Promise<[
            protos.google.cloud.hypercomputecluster.v1beta.ICluster[],
            protos.google.cloud.hypercomputecluster.v1beta.IListClustersRequest | null,
            protos.google.cloud.hypercomputecluster.v1beta.IListClustersResponse
        ]>;

Lists Clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ilistclustersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.hypercomputecluster.v1beta.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.icluster)[], [protos.google.cloud.hypercomputecluster.v1beta.IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ilistclustersrequest) | null, [protos.google.cloud.hypercomputecluster.v1beta.IListClustersResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ilistclustersresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Cluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.cluster). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listClustersAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listClusters(request, options, callback)
    
    
    listClusters(request: protos.google.cloud.hypercomputecluster.v1beta.IListClustersRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.hypercomputecluster.v1beta.IListClustersRequest, protos.google.cloud.hypercomputecluster.v1beta.IListClustersResponse | null | undefined, protos.google.cloud.hypercomputecluster.v1beta.ICluster>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ilistclustersrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.hypercomputecluster.v1beta.IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ilistclustersrequest), [protos.google.cloud.hypercomputecluster.v1beta.IListClustersResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ilistclustersresponse) | null | undefined, [protos.google.cloud.hypercomputecluster.v1beta.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.icluster)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listClusters(request, callback)
    
    
    listClusters(request: protos.google.cloud.hypercomputecluster.v1beta.IListClustersRequest, callback: PaginationCallback<protos.google.cloud.hypercomputecluster.v1beta.IListClustersRequest, protos.google.cloud.hypercomputecluster.v1beta.IListClustersResponse | null | undefined, protos.google.cloud.hypercomputecluster.v1beta.ICluster>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ilistclustersrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.hypercomputecluster.v1beta.IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ilistclustersrequest), [protos.google.cloud.hypercomputecluster.v1beta.IListClustersResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ilistclustersresponse) | null | undefined, [protos.google.cloud.hypercomputecluster.v1beta.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.icluster)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listClustersAsync(request, options)
    
    
    listClustersAsync(request?: protos.google.cloud.hypercomputecluster.v1beta.IListClustersRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.hypercomputecluster.v1beta.ICluster>;

Equivalent to `listClusters`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ilistclustersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.hypercomputecluster.v1beta.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.icluster)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Cluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.cluster). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
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
      const {HypercomputeClusterClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1beta;
    
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
    
    
    listClustersStream(request?: protos.google.cloud.hypercomputecluster.v1beta.IListClustersRequest, options?: CallOptions): Transform;

Equivalent to `listClusters`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ilistclustersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Cluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.cluster) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listClustersAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### lustreInstancePath(project, location, instance)
    
    
    lustreInstancePath(project: string, location: string, instance: string): string;

Return a fully-qualified lustreInstance resource name string.

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
  
### matchInstanceFromLustreInstanceName(lustreInstanceName)
    
    
    matchInstanceFromLustreInstanceName(lustreInstanceName: string): string | number;

Parse the instance from LustreInstance resource.

**Parameter**  
---  
**Name** | **Description**  
`lustreInstanceName` |  `string`   
A fully-qualified path representing LustreInstance resource.  
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
  
### matchLocationFromLustreInstanceName(lustreInstanceName)
    
    
    matchLocationFromLustreInstanceName(lustreInstanceName: string): string | number;

Parse the location from LustreInstance resource.

**Parameter**  
---  
**Name** | **Description**  
`lustreInstanceName` |  `string`   
A fully-qualified path representing LustreInstance resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
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
  
### matchProjectFromLustreInstanceName(lustreInstanceName)
    
    
    matchProjectFromLustreInstanceName(lustreInstanceName: string): string | number;

Parse the project from LustreInstance resource.

**Parameter**  
---  
**Name** | **Description**  
`lustreInstanceName` |  `string`   
A fully-qualified path representing LustreInstance resource.  
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
    
    
    updateCluster(request?: protos.google.cloud.hypercomputecluster.v1beta.IUpdateClusterRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.hypercomputecluster.v1beta.ICluster, protos.google.cloud.hypercomputecluster.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the parameters of a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.iupdateclusterrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.hypercomputecluster.v1beta.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.icluster), [protos.google.cloud.hypercomputecluster.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
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
      const {HypercomputeClusterClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1beta;
    
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
    
    
    updateCluster(request: protos.google.cloud.hypercomputecluster.v1beta.IUpdateClusterRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.hypercomputecluster.v1beta.ICluster, protos.google.cloud.hypercomputecluster.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.iupdateclusterrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.hypercomputecluster.v1beta.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.icluster), [protos.google.cloud.hypercomputecluster.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCluster(request, callback)
    
    
    updateCluster(request: protos.google.cloud.hypercomputecluster.v1beta.IUpdateClusterRequest, callback: Callback<LROperation<protos.google.cloud.hypercomputecluster.v1beta.ICluster, protos.google.cloud.hypercomputecluster.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.iupdateclusterrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.hypercomputecluster.v1beta.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.icluster), [protos.google.cloud.hypercomputecluster.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
