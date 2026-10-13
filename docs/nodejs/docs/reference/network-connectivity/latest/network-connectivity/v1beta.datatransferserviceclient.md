---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/v1beta.datatransferserviceclient
title: Class v1beta.DataTransferServiceClient (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:06.532392+00:00
---

# Class v1beta.DataTransferServiceClient (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/v1beta.datatransferserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.DataTransferServiceClient (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.6.0  4.2.0  3.6.0  3.2.0  2.3.3  2.2.0  2.1.2  1.5.0  1.4.2  1.3.0  1.2.1  1.1.6 

DataTransferService is the service for the Data Transfer API. v1beta

## Package

[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of DataTransferServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new DataTransferServiceClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### dataTransferServiceStub
    
    
    dataTransferServiceStub?: Promise<{
            [name: string]: Function;
        }>;

### descriptors
    
    
    descriptors: Descriptors;

### iamClient
    
    
    iamClient: IamClient;

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

### cancelOperation(request, optionsOrCallback, callback)
    
    
    cancelOperation(request: protos.google.longrunning.CancelOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>, callback?: Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>): Promise<protos.google.protobuf.Empty>;

Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an value with a of 1, corresponding to `Code.CANCELLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### checkCreateDestinationProgress(name)
    
    
    checkCreateDestinationProgress(name: string): Promise<LROperation<protos.google.cloud.networkconnectivity.v1beta.Destination, protos.google.cloud.networkconnectivity.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `createDestination()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.networkconnectivity.v1beta.Destination](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.destination-class), [protos.google.cloud.networkconnectivity.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the parent resource.
       */
      // const parent = 'abc123'
      /**
       *  Required. The ID to use for the `Destination` resource, which becomes the
       *  final component of the `Destination` resource name.
       */
      // const destinationId = 'abc123'
      /**
       *  Required. The `Destination` resource to create.
       */
      // const destination = {}
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server can ignore
       *  the request if it has already been completed. The server waits
       *  for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, can ignore the second request. This prevents
       *  clients from accidentally creating duplicate `Destination`
       *  resources.
       *  The request ID must be a valid UUID with the exception that zero UUID
       *  (00000000-0000-0000-0000-000000000000) isn't supported.
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {DataTransferServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callCreateDestination() {
        // Construct request
        const request = {
          parent,
          destinationId,
          destination,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.createDestination(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateDestination();
    
    

### checkCreateMulticloudDataTransferConfigProgress(name)
    
    
    checkCreateMulticloudDataTransferConfigProgress(name: string): Promise<LROperation<protos.google.cloud.networkconnectivity.v1beta.MulticloudDataTransferConfig, protos.google.cloud.networkconnectivity.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `createMulticloudDataTransferConfig()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.networkconnectivity.v1beta.MulticloudDataTransferConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.multiclouddatatransferconfig), [protos.google.cloud.networkconnectivity.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the parent resource.
       */
      // const parent = 'abc123'
      /**
       *  Required. The ID to use for the `MulticloudDataTransferConfig` resource,
       *  which becomes the final component of the `MulticloudDataTransferConfig`
       *  resource name.
       */
      // const multicloudDataTransferConfigId = 'abc123'
      /**
       *  Required. The `MulticloudDataTransferConfig` resource to create.
       */
      // const multicloudDataTransferConfig = {}
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server can ignore
       *  the request if it has already been completed. The server waits
       *  for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, can ignore the second request. This prevents
       *  clients from accidentally creating duplicate `MulticloudDataTransferConfig`
       *  resources.
       *  The request ID must be a valid UUID with the exception that zero UUID
       *  (00000000-0000-0000-0000-000000000000) isn't supported.
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {DataTransferServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callCreateMulticloudDataTransferConfig() {
        // Construct request
        const request = {
          parent,
          multicloudDataTransferConfigId,
          multicloudDataTransferConfig,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.createMulticloudDataTransferConfig(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateMulticloudDataTransferConfig();
    
    

### checkDeleteDestinationProgress(name)
    
    
    checkDeleteDestinationProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.networkconnectivity.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `deleteDestination()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.empty), [protos.google.cloud.networkconnectivity.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `Destination` resource to delete.
       */
      // const name = 'abc123'
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server can ignore
       *  the request if it has already been completed. The server waits
       *  for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, can ignore the second request.
       *  The request ID must be a valid UUID with the exception that zero UUID
       *  (00000000-0000-0000-0000-000000000000) isn't supported.
       */
      // const requestId = 'abc123'
      /**
       *  Optional. The etag is computed by the server, and might be sent with update
       *  and delete requests so that the client has an up-to-date value before
       *  proceeding.
       */
      // const etag = 'abc123'
    
      // Imports the Networkconnectivity library
      const {DataTransferServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callDeleteDestination() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.deleteDestination(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteDestination();
    
    

### checkDeleteMulticloudDataTransferConfigProgress(name)
    
    
    checkDeleteMulticloudDataTransferConfigProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.networkconnectivity.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `deleteMulticloudDataTransferConfig()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.empty), [protos.google.cloud.networkconnectivity.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `MulticloudDataTransferConfig` resource to
       *  delete.
       */
      // const name = 'abc123'
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server can ignore
       *  the request if it has already been completed. The server waits
       *  for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, can ignore the second request. This prevents
       *  clients from accidentally creating duplicate `MulticloudDataTransferConfig`
       *  resources.
       *  The request ID must be a valid UUID with the exception that zero UUID
       *  (00000000-0000-0000-0000-000000000000) isn't supported.
       */
      // const requestId = 'abc123'
      /**
       *  Optional. The etag is computed by the server, and might be sent with update
       *  and delete requests so that the client has an up-to-date value before
       *  proceeding.
       */
      // const etag = 'abc123'
    
      // Imports the Networkconnectivity library
      const {DataTransferServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callDeleteMulticloudDataTransferConfig() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.deleteMulticloudDataTransferConfig(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteMulticloudDataTransferConfig();
    
    

### checkUpdateDestinationProgress(name)
    
    
    checkUpdateDestinationProgress(name: string): Promise<LROperation<protos.google.cloud.networkconnectivity.v1beta.Destination, protos.google.cloud.networkconnectivity.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `updateDestination()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.networkconnectivity.v1beta.Destination](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.destination-class), [protos.google.cloud.networkconnectivity.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. `FieldMask is used to specify the fields to be overwritten in the
       *  `Destination` resource by the update.
       *  The fields specified in `update_mask` are relative to the resource, not
       *  the full request. A field is overwritten if it is in the mask. If you
       *  don't specify a mask, all fields are overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The `Destination` resource to update.
       */
      // const destination = {}
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server can ignore
       *  the request if it has already been completed. The server waits
       *  for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, can ignore the second request.
       *  The request ID must be a valid UUID with the exception that zero UUID
       *  (00000000-0000-0000-0000-000000000000) isn't supported.
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {DataTransferServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callUpdateDestination() {
        // Construct request
        const request = {
          destination,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.updateDestination(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateDestination();
    
    

### checkUpdateMulticloudDataTransferConfigProgress(name)
    
    
    checkUpdateMulticloudDataTransferConfigProgress(name: string): Promise<LROperation<protos.google.cloud.networkconnectivity.v1beta.MulticloudDataTransferConfig, protos.google.cloud.networkconnectivity.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `updateMulticloudDataTransferConfig()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.networkconnectivity.v1beta.MulticloudDataTransferConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.multiclouddatatransferconfig), [protos.google.cloud.networkconnectivity.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. `FieldMask` is used to specify the fields in the
       *  `MulticloudDataTransferConfig` resource to be overwritten by the update.
       *  The fields specified in `update_mask` are relative to the resource, not
       *  the full request. A field is overwritten if it is in the mask. If you
       *  don't specify a mask, all fields are overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The `MulticloudDataTransferConfig` resource to update.
       */
      // const multicloudDataTransferConfig = {}
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server can ignore
       *  the request if it has already been completed. The server waits
       *  for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, can ignore the second request. This prevents
       *  clients from accidentally creating duplicate `MulticloudDataTransferConfig`
       *  resources.
       *  The request ID must be a valid UUID with the exception that zero UUID
       *  (00000000-0000-0000-0000-000000000000) isn't supported.
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {DataTransferServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callUpdateMulticloudDataTransferConfig() {
        // Construct request
        const request = {
          multicloudDataTransferConfig,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.updateMulticloudDataTransferConfig(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateMulticloudDataTransferConfig();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### createDestination(request, options)
    
    
    createDestination(request?: protos.google.cloud.networkconnectivity.v1beta.ICreateDestinationRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.networkconnectivity.v1beta.IDestination, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a `Destination` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.icreatedestinationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.networkconnectivity.v1beta.IDestination](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.idestination), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the parent resource.
       */
      // const parent = 'abc123'
      /**
       *  Required. The ID to use for the `Destination` resource, which becomes the
       *  final component of the `Destination` resource name.
       */
      // const destinationId = 'abc123'
      /**
       *  Required. The `Destination` resource to create.
       */
      // const destination = {}
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server can ignore
       *  the request if it has already been completed. The server waits
       *  for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, can ignore the second request. This prevents
       *  clients from accidentally creating duplicate `Destination`
       *  resources.
       *  The request ID must be a valid UUID with the exception that zero UUID
       *  (00000000-0000-0000-0000-000000000000) isn't supported.
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {DataTransferServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callCreateDestination() {
        // Construct request
        const request = {
          parent,
          destinationId,
          destination,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.createDestination(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateDestination();
    
    

### createDestination(request, options, callback)
    
    
    createDestination(request: protos.google.cloud.networkconnectivity.v1beta.ICreateDestinationRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.networkconnectivity.v1beta.IDestination, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.icreatedestinationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkconnectivity.v1beta.IDestination](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.idestination), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDestination(request, callback)
    
    
    createDestination(request: protos.google.cloud.networkconnectivity.v1beta.ICreateDestinationRequest, callback: Callback<LROperation<protos.google.cloud.networkconnectivity.v1beta.IDestination, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.icreatedestinationrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkconnectivity.v1beta.IDestination](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.idestination), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMulticloudDataTransferConfig(request, options)
    
    
    createMulticloudDataTransferConfig(request?: protos.google.cloud.networkconnectivity.v1beta.ICreateMulticloudDataTransferConfigRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a `MulticloudDataTransferConfig` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.icreatemulticlouddatatransferconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.imulticlouddatatransferconfig), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the parent resource.
       */
      // const parent = 'abc123'
      /**
       *  Required. The ID to use for the `MulticloudDataTransferConfig` resource,
       *  which becomes the final component of the `MulticloudDataTransferConfig`
       *  resource name.
       */
      // const multicloudDataTransferConfigId = 'abc123'
      /**
       *  Required. The `MulticloudDataTransferConfig` resource to create.
       */
      // const multicloudDataTransferConfig = {}
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server can ignore
       *  the request if it has already been completed. The server waits
       *  for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, can ignore the second request. This prevents
       *  clients from accidentally creating duplicate `MulticloudDataTransferConfig`
       *  resources.
       *  The request ID must be a valid UUID with the exception that zero UUID
       *  (00000000-0000-0000-0000-000000000000) isn't supported.
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {DataTransferServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callCreateMulticloudDataTransferConfig() {
        // Construct request
        const request = {
          parent,
          multicloudDataTransferConfigId,
          multicloudDataTransferConfig,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.createMulticloudDataTransferConfig(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateMulticloudDataTransferConfig();
    
    

### createMulticloudDataTransferConfig(request, options, callback)
    
    
    createMulticloudDataTransferConfig(request: protos.google.cloud.networkconnectivity.v1beta.ICreateMulticloudDataTransferConfigRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.icreatemulticlouddatatransferconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.imulticlouddatatransferconfig), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMulticloudDataTransferConfig(request, callback)
    
    
    createMulticloudDataTransferConfig(request: protos.google.cloud.networkconnectivity.v1beta.ICreateMulticloudDataTransferConfigRequest, callback: Callback<LROperation<protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.icreatemulticlouddatatransferconfigrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.imulticlouddatatransferconfig), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDestination(request, options)
    
    
    deleteDestination(request?: protos.google.cloud.networkconnectivity.v1beta.IDeleteDestinationRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a `Destination` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ideletedestinationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.iempty), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `Destination` resource to delete.
       */
      // const name = 'abc123'
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server can ignore
       *  the request if it has already been completed. The server waits
       *  for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, can ignore the second request.
       *  The request ID must be a valid UUID with the exception that zero UUID
       *  (00000000-0000-0000-0000-000000000000) isn't supported.
       */
      // const requestId = 'abc123'
      /**
       *  Optional. The etag is computed by the server, and might be sent with update
       *  and delete requests so that the client has an up-to-date value before
       *  proceeding.
       */
      // const etag = 'abc123'
    
      // Imports the Networkconnectivity library
      const {DataTransferServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callDeleteDestination() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.deleteDestination(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteDestination();
    
    

### deleteDestination(request, options, callback)
    
    
    deleteDestination(request: protos.google.cloud.networkconnectivity.v1beta.IDeleteDestinationRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ideletedestinationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.iempty), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDestination(request, callback)
    
    
    deleteDestination(request: protos.google.cloud.networkconnectivity.v1beta.IDeleteDestinationRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ideletedestinationrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.iempty), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMulticloudDataTransferConfig(request, options)
    
    
    deleteMulticloudDataTransferConfig(request?: protos.google.cloud.networkconnectivity.v1beta.IDeleteMulticloudDataTransferConfigRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a `MulticloudDataTransferConfig` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ideletemulticlouddatatransferconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.iempty), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `MulticloudDataTransferConfig` resource to
       *  delete.
       */
      // const name = 'abc123'
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server can ignore
       *  the request if it has already been completed. The server waits
       *  for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, can ignore the second request. This prevents
       *  clients from accidentally creating duplicate `MulticloudDataTransferConfig`
       *  resources.
       *  The request ID must be a valid UUID with the exception that zero UUID
       *  (00000000-0000-0000-0000-000000000000) isn't supported.
       */
      // const requestId = 'abc123'
      /**
       *  Optional. The etag is computed by the server, and might be sent with update
       *  and delete requests so that the client has an up-to-date value before
       *  proceeding.
       */
      // const etag = 'abc123'
    
      // Imports the Networkconnectivity library
      const {DataTransferServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callDeleteMulticloudDataTransferConfig() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.deleteMulticloudDataTransferConfig(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteMulticloudDataTransferConfig();
    
    

### deleteMulticloudDataTransferConfig(request, options, callback)
    
    
    deleteMulticloudDataTransferConfig(request: protos.google.cloud.networkconnectivity.v1beta.IDeleteMulticloudDataTransferConfigRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ideletemulticlouddatatransferconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.iempty), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMulticloudDataTransferConfig(request, callback)
    
    
    deleteMulticloudDataTransferConfig(request: protos.google.cloud.networkconnectivity.v1beta.IDeleteMulticloudDataTransferConfigRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ideletemulticlouddatatransferconfigrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.iempty), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### destinationPath(project, location, multicloudDataTransferConfig, destination)
    
    
    destinationPath(project: string, location: string, multicloudDataTransferConfig: string, destination: string): string;

Return a fully-qualified destination resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`multicloudDataTransferConfig` |  `string`   
  
`destination` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### gatewayAdvertisedRoutePath(project, location, spoke, gatewayAdvertisedRoute)
    
    
    gatewayAdvertisedRoutePath(project: string, location: string, spoke: string, gatewayAdvertisedRoute: string): string;

Return a fully-qualified gatewayAdvertisedRoute resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`spoke` |  `string`   
  
`gatewayAdvertisedRoute` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### getDestination(request, options)
    
    
    getDestination(request?: protos.google.cloud.networkconnectivity.v1beta.IGetDestinationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networkconnectivity.v1beta.IDestination,
            (protos.google.cloud.networkconnectivity.v1beta.IGetDestinationRequest | undefined),
            {} | undefined
        ]>;

Gets the details of a `Destination` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetdestinationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networkconnectivity.v1beta.IDestination](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.idestination), ([protos.google.cloud.networkconnectivity.v1beta.IGetDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetdestinationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `Destination` resource to get.
       */
      // const name = 'abc123'
    
      // Imports the Networkconnectivity library
      const {DataTransferServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callGetDestination() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await networkconnectivityClient.getDestination(request);
        console.log(response);
      }
    
      callGetDestination();
    
    

### getDestination(request, options, callback)
    
    
    getDestination(request: protos.google.cloud.networkconnectivity.v1beta.IGetDestinationRequest, options: CallOptions, callback: Callback<protos.google.cloud.networkconnectivity.v1beta.IDestination, protos.google.cloud.networkconnectivity.v1beta.IGetDestinationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetdestinationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.networkconnectivity.v1beta.IDestination](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.idestination), [protos.google.cloud.networkconnectivity.v1beta.IGetDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetdestinationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDestination(request, callback)
    
    
    getDestination(request: protos.google.cloud.networkconnectivity.v1beta.IGetDestinationRequest, callback: Callback<protos.google.cloud.networkconnectivity.v1beta.IDestination, protos.google.cloud.networkconnectivity.v1beta.IGetDestinationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetdestinationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.networkconnectivity.v1beta.IDestination](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.idestination), [protos.google.cloud.networkconnectivity.v1beta.IGetDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetdestinationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request, options, callback)
    
    
    getIamPolicy(request: IamProtos.google.iam.v1.GetIamPolicyRequest, options?: gax.CallOptions | Callback<IamProtos.google.iam.v1.Policy, IamProtos.google.iam.v1.GetIamPolicyRequest | null | undefined, {} | null | undefined>, callback?: Callback<IamProtos.google.iam.v1.Policy, IamProtos.google.iam.v1.GetIamPolicyRequest | null | undefined, {} | null | undefined>): Promise<[IamProtos.google.iam.v1.Policy]>;

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `IamProtos.google.iam.v1.GetIamPolicyRequest`   
The request object that will be sent.  
`options` |  `CallOptions | Callback<google.iam.v1.Policy, google.iam.v1.GetIamPolicyRequest | null | undefined, {} | null | undefined>`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/interfaces/CallOptions.html) for the details.  
`callback` |  `Callback<google.iam.v1.Policy, google.iam.v1.GetIamPolicyRequest | null | undefined, {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing .  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.Policy]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
  
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
    

### getMulticloudDataTransferConfig(request, options)
    
    
    getMulticloudDataTransferConfig(request?: protos.google.cloud.networkconnectivity.v1beta.IGetMulticloudDataTransferConfigRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig,
            (protos.google.cloud.networkconnectivity.v1beta.IGetMulticloudDataTransferConfigRequest | undefined),
            {} | undefined
        ]>;

Gets the details of a `MulticloudDataTransferConfig` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetmulticlouddatatransferconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.imulticlouddatatransferconfig), ([protos.google.cloud.networkconnectivity.v1beta.IGetMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetmulticlouddatatransferconfigrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [MulticloudDataTransferConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.multiclouddatatransferconfig). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `MulticloudDataTransferConfig` resource to get.
       */
      // const name = 'abc123'
    
      // Imports the Networkconnectivity library
      const {DataTransferServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callGetMulticloudDataTransferConfig() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await networkconnectivityClient.getMulticloudDataTransferConfig(request);
        console.log(response);
      }
    
      callGetMulticloudDataTransferConfig();
    
    

### getMulticloudDataTransferConfig(request, options, callback)
    
    
    getMulticloudDataTransferConfig(request: protos.google.cloud.networkconnectivity.v1beta.IGetMulticloudDataTransferConfigRequest, options: CallOptions, callback: Callback<protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig, protos.google.cloud.networkconnectivity.v1beta.IGetMulticloudDataTransferConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetmulticlouddatatransferconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.imulticlouddatatransferconfig), [protos.google.cloud.networkconnectivity.v1beta.IGetMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetmulticlouddatatransferconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMulticloudDataTransferConfig(request, callback)
    
    
    getMulticloudDataTransferConfig(request: protos.google.cloud.networkconnectivity.v1beta.IGetMulticloudDataTransferConfigRequest, callback: Callback<protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig, protos.google.cloud.networkconnectivity.v1beta.IGetMulticloudDataTransferConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetmulticlouddatatransferconfigrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.imulticlouddatatransferconfig), [protos.google.cloud.networkconnectivity.v1beta.IGetMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetmulticlouddatatransferconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMulticloudDataTransferSupportedService(request, options)
    
    
    getMulticloudDataTransferSupportedService(request?: protos.google.cloud.networkconnectivity.v1beta.IGetMulticloudDataTransferSupportedServiceRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferSupportedService,
            (protos.google.cloud.networkconnectivity.v1beta.IGetMulticloudDataTransferSupportedServiceRequest | undefined),
            {} | undefined
        ]>;

Gets the details of a service that is supported for Data Transfer Essentials.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMulticloudDataTransferSupportedServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetmulticlouddatatransfersupportedservicerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferSupportedService](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.imulticlouddatatransfersupportedservice), ([protos.google.cloud.networkconnectivity.v1beta.IGetMulticloudDataTransferSupportedServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetmulticlouddatatransfersupportedservicerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [MulticloudDataTransferSupportedService](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.multiclouddatatransfersupportedservice). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the service.
       */
      // const name = 'abc123'
    
      // Imports the Networkconnectivity library
      const {DataTransferServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callGetMulticloudDataTransferSupportedService() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await networkconnectivityClient.getMulticloudDataTransferSupportedService(request);
        console.log(response);
      }
    
      callGetMulticloudDataTransferSupportedService();
    
    

### getMulticloudDataTransferSupportedService(request, options, callback)
    
    
    getMulticloudDataTransferSupportedService(request: protos.google.cloud.networkconnectivity.v1beta.IGetMulticloudDataTransferSupportedServiceRequest, options: CallOptions, callback: Callback<protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferSupportedService, protos.google.cloud.networkconnectivity.v1beta.IGetMulticloudDataTransferSupportedServiceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMulticloudDataTransferSupportedServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetmulticlouddatatransfersupportedservicerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferSupportedService](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.imulticlouddatatransfersupportedservice), [protos.google.cloud.networkconnectivity.v1beta.IGetMulticloudDataTransferSupportedServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetmulticlouddatatransfersupportedservicerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMulticloudDataTransferSupportedService(request, callback)
    
    
    getMulticloudDataTransferSupportedService(request: protos.google.cloud.networkconnectivity.v1beta.IGetMulticloudDataTransferSupportedServiceRequest, callback: Callback<protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferSupportedService, protos.google.cloud.networkconnectivity.v1beta.IGetMulticloudDataTransferSupportedServiceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMulticloudDataTransferSupportedServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetmulticlouddatatransfersupportedservicerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferSupportedService](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.imulticlouddatatransfersupportedservice), [protos.google.cloud.networkconnectivity.v1beta.IGetMulticloudDataTransferSupportedServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetmulticlouddatatransfersupportedservicerequest) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)]>` |   
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
  
### groupPath(project, hub, group)
    
    
    groupPath(project: string, hub: string, group: string): string;

Return a fully-qualified group resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`hub` |  `string`   
  
`group` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### hubPath(project, hub)
    
    
    hubPath(project: string, hub: string): string;

Return a fully-qualified hub resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`hub` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### hubRoutePath(project, hub, routeTable, route)
    
    
    hubRoutePath(project: string, hub: string, routeTable: string, route: string): string;

Return a fully-qualified hubRoute resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`hub` |  `string`   
  
`routeTable` |  `string`   
  
`route` |  `string`   
  
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
  
### listDestinations(request, options)
    
    
    listDestinations(request?: protos.google.cloud.networkconnectivity.v1beta.IListDestinationsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networkconnectivity.v1beta.IDestination[],
            protos.google.cloud.networkconnectivity.v1beta.IListDestinationsRequest | null,
            protos.google.cloud.networkconnectivity.v1beta.IListDestinationsResponse
        ]>;

Lists the `Destination` resources in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDestinationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistdestinationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networkconnectivity.v1beta.IDestination](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.idestination)[], [protos.google.cloud.networkconnectivity.v1beta.IListDestinationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistdestinationsrequest) | null, [protos.google.cloud.networkconnectivity.v1beta.IListDestinationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistdestinationsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listDestinationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDestinations(request, options, callback)
    
    
    listDestinations(request: protos.google.cloud.networkconnectivity.v1beta.IListDestinationsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.networkconnectivity.v1beta.IListDestinationsRequest, protos.google.cloud.networkconnectivity.v1beta.IListDestinationsResponse | null | undefined, protos.google.cloud.networkconnectivity.v1beta.IDestination>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDestinationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistdestinationsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networkconnectivity.v1beta.IListDestinationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistdestinationsrequest), [protos.google.cloud.networkconnectivity.v1beta.IListDestinationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistdestinationsresponse) | null | undefined, [protos.google.cloud.networkconnectivity.v1beta.IDestination](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.idestination)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDestinations(request, callback)
    
    
    listDestinations(request: protos.google.cloud.networkconnectivity.v1beta.IListDestinationsRequest, callback: PaginationCallback<protos.google.cloud.networkconnectivity.v1beta.IListDestinationsRequest, protos.google.cloud.networkconnectivity.v1beta.IListDestinationsResponse | null | undefined, protos.google.cloud.networkconnectivity.v1beta.IDestination>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDestinationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistdestinationsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networkconnectivity.v1beta.IListDestinationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistdestinationsrequest), [protos.google.cloud.networkconnectivity.v1beta.IListDestinationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistdestinationsresponse) | null | undefined, [protos.google.cloud.networkconnectivity.v1beta.IDestination](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.idestination)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDestinationsAsync(request, options)
    
    
    listDestinationsAsync(request?: protos.google.cloud.networkconnectivity.v1beta.IListDestinationsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.networkconnectivity.v1beta.IDestination>;

Equivalent to `listDestinations`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDestinationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistdestinationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.networkconnectivity.v1beta.IDestination](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.idestination)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the parent resource.
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of results listed per page.
       */
      // const pageSize = 1234
      /**
       *  Optional. The page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. An expression that filters the results listed in the response.
       */
      // const filter = 'abc123'
      /**
       *  Optional. The sort order of the results.
       */
      // const orderBy = 'abc123'
      /**
       *  Optional. If `true`, allow partial responses for multi-regional aggregated
       *  list requests.
       */
      // const returnPartialSuccess = true
    
      // Imports the Networkconnectivity library
      const {DataTransferServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callListDestinations() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = networkconnectivityClient.listDestinationsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListDestinations();
    
    

### listDestinationsStream(request, options)
    
    
    listDestinationsStream(request?: protos.google.cloud.networkconnectivity.v1beta.IListDestinationsRequest, options?: CallOptions): Transform;

Equivalent to `listDestinations`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDestinationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistdestinationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listDestinationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
    

### listMulticloudDataTransferConfigs(request, options)
    
    
    listMulticloudDataTransferConfigs(request?: protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferConfigsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig[],
            protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferConfigsRequest | null,
            protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferConfigsResponse
        ]>;

Lists the `MulticloudDataTransferConfig` resources in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMulticloudDataTransferConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransferconfigsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.imulticlouddatatransferconfig)[], [protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransferconfigsrequest) | null, [protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransferconfigsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [MulticloudDataTransferConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.multiclouddatatransferconfig). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listMulticloudDataTransferConfigsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listMulticloudDataTransferConfigs(request, options, callback)
    
    
    listMulticloudDataTransferConfigs(request: protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferConfigsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferConfigsRequest, protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferConfigsResponse | null | undefined, protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMulticloudDataTransferConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransferconfigsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransferconfigsrequest), [protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransferconfigsresponse) | null | undefined, [protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.imulticlouddatatransferconfig)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMulticloudDataTransferConfigs(request, callback)
    
    
    listMulticloudDataTransferConfigs(request: protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferConfigsRequest, callback: PaginationCallback<protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferConfigsRequest, protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferConfigsResponse | null | undefined, protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMulticloudDataTransferConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransferconfigsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransferconfigsrequest), [protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransferconfigsresponse) | null | undefined, [protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.imulticlouddatatransferconfig)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMulticloudDataTransferConfigsAsync(request, options)
    
    
    listMulticloudDataTransferConfigsAsync(request?: protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferConfigsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig>;

Equivalent to `listMulticloudDataTransferConfigs`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMulticloudDataTransferConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransferconfigsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.imulticlouddatatransferconfig)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [MulticloudDataTransferConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.multiclouddatatransferconfig). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the parent resource.
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of results listed per page.
       */
      // const pageSize = 1234
      /**
       *  Optional. The page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. An expression that filters the results listed in the response.
       */
      // const filter = 'abc123'
      /**
       *  Optional. The sort order of the results.
       */
      // const orderBy = 'abc123'
      /**
       *  Optional. If `true`, allows partial responses for multi-regional aggregated
       *  list requests.
       */
      // const returnPartialSuccess = true
    
      // Imports the Networkconnectivity library
      const {DataTransferServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callListMulticloudDataTransferConfigs() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = networkconnectivityClient.listMulticloudDataTransferConfigsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListMulticloudDataTransferConfigs();
    
    

### listMulticloudDataTransferConfigsStream(request, options)
    
    
    listMulticloudDataTransferConfigsStream(request?: protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferConfigsRequest, options?: CallOptions): Transform;

Equivalent to `listMulticloudDataTransferConfigs`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMulticloudDataTransferConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransferconfigsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [MulticloudDataTransferConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.multiclouddatatransferconfig) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listMulticloudDataTransferConfigsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listMulticloudDataTransferSupportedServices(request, options)
    
    
    listMulticloudDataTransferSupportedServices(request?: protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferSupportedServicesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferSupportedService[],
            protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferSupportedServicesRequest | null,
            protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferSupportedServicesResponse
        ]>;

Lists the services in the project for a region that are supported for Data Transfer Essentials.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMulticloudDataTransferSupportedServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransfersupportedservicesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferSupportedService](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.imulticlouddatatransfersupportedservice)[], [protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferSupportedServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransfersupportedservicesrequest) | null, [protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferSupportedServicesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransfersupportedservicesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [MulticloudDataTransferSupportedService](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.multiclouddatatransfersupportedservice). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listMulticloudDataTransferSupportedServicesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listMulticloudDataTransferSupportedServices(request, options, callback)
    
    
    listMulticloudDataTransferSupportedServices(request: protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferSupportedServicesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferSupportedServicesRequest, protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferSupportedServicesResponse | null | undefined, protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferSupportedService>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMulticloudDataTransferSupportedServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransfersupportedservicesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferSupportedServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransfersupportedservicesrequest), [protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferSupportedServicesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransfersupportedservicesresponse) | null | undefined, [protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferSupportedService](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.imulticlouddatatransfersupportedservice)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMulticloudDataTransferSupportedServices(request, callback)
    
    
    listMulticloudDataTransferSupportedServices(request: protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferSupportedServicesRequest, callback: PaginationCallback<protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferSupportedServicesRequest, protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferSupportedServicesResponse | null | undefined, protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferSupportedService>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMulticloudDataTransferSupportedServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransfersupportedservicesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferSupportedServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransfersupportedservicesrequest), [protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferSupportedServicesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransfersupportedservicesresponse) | null | undefined, [protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferSupportedService](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.imulticlouddatatransfersupportedservice)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMulticloudDataTransferSupportedServicesAsync(request, options)
    
    
    listMulticloudDataTransferSupportedServicesAsync(request?: protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferSupportedServicesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferSupportedService>;

Equivalent to `listMulticloudDataTransferSupportedServices`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMulticloudDataTransferSupportedServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransfersupportedservicesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferSupportedService](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.imulticlouddatatransfersupportedservice)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [MulticloudDataTransferSupportedService](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.multiclouddatatransfersupportedservice). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the parent resource.
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of results listed per page.
       */
      // const pageSize = 1234
      /**
       *  Optional. The page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Networkconnectivity library
      const {DataTransferServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callListMulticloudDataTransferSupportedServices() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = networkconnectivityClient.listMulticloudDataTransferSupportedServicesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListMulticloudDataTransferSupportedServices();
    
    

### listMulticloudDataTransferSupportedServicesStream(request, options)
    
    
    listMulticloudDataTransferSupportedServicesStream(request?: protos.google.cloud.networkconnectivity.v1beta.IListMulticloudDataTransferSupportedServicesRequest, options?: CallOptions): Transform;

Equivalent to `listMulticloudDataTransferSupportedServices`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMulticloudDataTransferSupportedServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistmulticlouddatatransfersupportedservicesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [MulticloudDataTransferSupportedService](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.multiclouddatatransfersupportedservice) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listMulticloudDataTransferSupportedServicesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listOperationsAsync(request, options)
    
    
    listOperationsAsync(request: protos.google.longrunning.ListOperationsRequest, options?: gax.CallOptions): AsyncIterable<protos.google.longrunning.IOperation>;

Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. Returns an iterable object.

For-await-of syntax is used with the iterable to recursively get response element on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
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
  
### matchDestinationFromDestinationName(destinationName)
    
    
    matchDestinationFromDestinationName(destinationName: string): string | number;

Parse the destination from Destination resource.

**Parameter**  
---  
**Name** | **Description**  
`destinationName` |  `string`   
A fully-qualified path representing Destination resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the destination.  
  
### matchGatewayAdvertisedRouteFromGatewayAdvertisedRouteName(gatewayAdvertisedRouteName)
    
    
    matchGatewayAdvertisedRouteFromGatewayAdvertisedRouteName(gatewayAdvertisedRouteName: string): string | number;

Parse the gateway_advertised_route from GatewayAdvertisedRoute resource.

**Parameter**  
---  
**Name** | **Description**  
`gatewayAdvertisedRouteName` |  `string`   
A fully-qualified path representing GatewayAdvertisedRoute resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the gateway_advertised_route.  
  
### matchGroupFromGroupName(groupName)
    
    
    matchGroupFromGroupName(groupName: string): string | number;

Parse the group from Group resource.

**Parameter**  
---  
**Name** | **Description**  
`groupName` |  `string`   
A fully-qualified path representing Group resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the group.  
  
### matchHubFromGroupName(groupName)
    
    
    matchHubFromGroupName(groupName: string): string | number;

Parse the hub from Group resource.

**Parameter**  
---  
**Name** | **Description**  
`groupName` |  `string`   
A fully-qualified path representing Group resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the hub.  
  
### matchHubFromHubName(hubName)
    
    
    matchHubFromHubName(hubName: string): string | number;

Parse the hub from Hub resource.

**Parameter**  
---  
**Name** | **Description**  
`hubName` |  `string`   
A fully-qualified path representing Hub resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the hub.  
  
### matchHubFromHubRouteName(hubRouteName)
    
    
    matchHubFromHubRouteName(hubRouteName: string): string | number;

Parse the hub from HubRoute resource.

**Parameter**  
---  
**Name** | **Description**  
`hubRouteName` |  `string`   
A fully-qualified path representing HubRoute resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the hub.  
  
### matchHubFromRouteTableName(routeTableName)
    
    
    matchHubFromRouteTableName(routeTableName: string): string | number;

Parse the hub from RouteTable resource.

**Parameter**  
---  
**Name** | **Description**  
`routeTableName` |  `string`   
A fully-qualified path representing RouteTable resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the hub.  
  
### matchLocationFromDestinationName(destinationName)
    
    
    matchLocationFromDestinationName(destinationName: string): string | number;

Parse the location from Destination resource.

**Parameter**  
---  
**Name** | **Description**  
`destinationName` |  `string`   
A fully-qualified path representing Destination resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromGatewayAdvertisedRouteName(gatewayAdvertisedRouteName)
    
    
    matchLocationFromGatewayAdvertisedRouteName(gatewayAdvertisedRouteName: string): string | number;

Parse the location from GatewayAdvertisedRoute resource.

**Parameter**  
---  
**Name** | **Description**  
`gatewayAdvertisedRouteName` |  `string`   
A fully-qualified path representing GatewayAdvertisedRoute resource.  
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
  
### matchLocationFromMulticloudDataTransferConfigName(multicloudDataTransferConfigName)
    
    
    matchLocationFromMulticloudDataTransferConfigName(multicloudDataTransferConfigName: string): string | number;

Parse the location from MulticloudDataTransferConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`multicloudDataTransferConfigName` |  `string`   
A fully-qualified path representing MulticloudDataTransferConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromMulticloudDataTransferSupportedServiceName(multicloudDataTransferSupportedServiceName)
    
    
    matchLocationFromMulticloudDataTransferSupportedServiceName(multicloudDataTransferSupportedServiceName: string): string | number;

Parse the location from MulticloudDataTransferSupportedService resource.

**Parameter**  
---  
**Name** | **Description**  
`multicloudDataTransferSupportedServiceName` |  `string`   
A fully-qualified path representing MulticloudDataTransferSupportedService resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromRemoteTransportProfileName(remoteTransportProfileName)
    
    
    matchLocationFromRemoteTransportProfileName(remoteTransportProfileName: string): string | number;

Parse the location from RemoteTransportProfile resource.

**Parameter**  
---  
**Name** | **Description**  
`remoteTransportProfileName` |  `string`   
A fully-qualified path representing RemoteTransportProfile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSpokeName(spokeName)
    
    
    matchLocationFromSpokeName(spokeName: string): string | number;

Parse the location from Spoke resource.

**Parameter**  
---  
**Name** | **Description**  
`spokeName` |  `string`   
A fully-qualified path representing Spoke resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTransportName(transportName)
    
    
    matchLocationFromTransportName(transportName: string): string | number;

Parse the location from Transport resource.

**Parameter**  
---  
**Name** | **Description**  
`transportName` |  `string`   
A fully-qualified path representing Transport resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchMulticloudDataTransferConfigFromDestinationName(destinationName)
    
    
    matchMulticloudDataTransferConfigFromDestinationName(destinationName: string): string | number;

Parse the multicloud_data_transfer_config from Destination resource.

**Parameter**  
---  
**Name** | **Description**  
`destinationName` |  `string`   
A fully-qualified path representing Destination resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the multicloud_data_transfer_config.  
  
### matchMulticloudDataTransferConfigFromMulticloudDataTransferConfigName(multicloudDataTransferConfigName)
    
    
    matchMulticloudDataTransferConfigFromMulticloudDataTransferConfigName(multicloudDataTransferConfigName: string): string | number;

Parse the multicloud_data_transfer_config from MulticloudDataTransferConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`multicloudDataTransferConfigName` |  `string`   
A fully-qualified path representing MulticloudDataTransferConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the multicloud_data_transfer_config.  
  
### matchMulticloudDataTransferSupportedServiceFromMulticloudDataTransferSupportedServiceName(multicloudDataTransferSupportedServiceName)
    
    
    matchMulticloudDataTransferSupportedServiceFromMulticloudDataTransferSupportedServiceName(multicloudDataTransferSupportedServiceName: string): string | number;

Parse the multicloud_data_transfer_supported_service from MulticloudDataTransferSupportedService resource.

**Parameter**  
---  
**Name** | **Description**  
`multicloudDataTransferSupportedServiceName` |  `string`   
A fully-qualified path representing MulticloudDataTransferSupportedService resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the multicloud_data_transfer_supported_service.  
  
### matchPolicyBasedRouteFromPolicyBasedRouteName(policyBasedRouteName)
    
    
    matchPolicyBasedRouteFromPolicyBasedRouteName(policyBasedRouteName: string): string | number;

Parse the policy_based_route from PolicyBasedRoute resource.

**Parameter**  
---  
**Name** | **Description**  
`policyBasedRouteName` |  `string`   
A fully-qualified path representing PolicyBasedRoute resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the policy_based_route.  
  
### matchProjectFromDestinationName(destinationName)
    
    
    matchProjectFromDestinationName(destinationName: string): string | number;

Parse the project from Destination resource.

**Parameter**  
---  
**Name** | **Description**  
`destinationName` |  `string`   
A fully-qualified path representing Destination resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromGatewayAdvertisedRouteName(gatewayAdvertisedRouteName)
    
    
    matchProjectFromGatewayAdvertisedRouteName(gatewayAdvertisedRouteName: string): string | number;

Parse the project from GatewayAdvertisedRoute resource.

**Parameter**  
---  
**Name** | **Description**  
`gatewayAdvertisedRouteName` |  `string`   
A fully-qualified path representing GatewayAdvertisedRoute resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromGroupName(groupName)
    
    
    matchProjectFromGroupName(groupName: string): string | number;

Parse the project from Group resource.

**Parameter**  
---  
**Name** | **Description**  
`groupName` |  `string`   
A fully-qualified path representing Group resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromHubName(hubName)
    
    
    matchProjectFromHubName(hubName: string): string | number;

Parse the project from Hub resource.

**Parameter**  
---  
**Name** | **Description**  
`hubName` |  `string`   
A fully-qualified path representing Hub resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromHubRouteName(hubRouteName)
    
    
    matchProjectFromHubRouteName(hubRouteName: string): string | number;

Parse the project from HubRoute resource.

**Parameter**  
---  
**Name** | **Description**  
`hubRouteName` |  `string`   
A fully-qualified path representing HubRoute resource.  
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
  
### matchProjectFromMulticloudDataTransferConfigName(multicloudDataTransferConfigName)
    
    
    matchProjectFromMulticloudDataTransferConfigName(multicloudDataTransferConfigName: string): string | number;

Parse the project from MulticloudDataTransferConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`multicloudDataTransferConfigName` |  `string`   
A fully-qualified path representing MulticloudDataTransferConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromMulticloudDataTransferSupportedServiceName(multicloudDataTransferSupportedServiceName)
    
    
    matchProjectFromMulticloudDataTransferSupportedServiceName(multicloudDataTransferSupportedServiceName: string): string | number;

Parse the project from MulticloudDataTransferSupportedService resource.

**Parameter**  
---  
**Name** | **Description**  
`multicloudDataTransferSupportedServiceName` |  `string`   
A fully-qualified path representing MulticloudDataTransferSupportedService resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromPolicyBasedRouteName(policyBasedRouteName)
    
    
    matchProjectFromPolicyBasedRouteName(policyBasedRouteName: string): string | number;

Parse the project from PolicyBasedRoute resource.

**Parameter**  
---  
**Name** | **Description**  
`policyBasedRouteName` |  `string`   
A fully-qualified path representing PolicyBasedRoute resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromRemoteTransportProfileName(remoteTransportProfileName)
    
    
    matchProjectFromRemoteTransportProfileName(remoteTransportProfileName: string): string | number;

Parse the project from RemoteTransportProfile resource.

**Parameter**  
---  
**Name** | **Description**  
`remoteTransportProfileName` |  `string`   
A fully-qualified path representing RemoteTransportProfile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromRouteTableName(routeTableName)
    
    
    matchProjectFromRouteTableName(routeTableName: string): string | number;

Parse the project from RouteTable resource.

**Parameter**  
---  
**Name** | **Description**  
`routeTableName` |  `string`   
A fully-qualified path representing RouteTable resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSpokeName(spokeName)
    
    
    matchProjectFromSpokeName(spokeName: string): string | number;

Parse the project from Spoke resource.

**Parameter**  
---  
**Name** | **Description**  
`spokeName` |  `string`   
A fully-qualified path representing Spoke resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTransportName(transportName)
    
    
    matchProjectFromTransportName(transportName: string): string | number;

Parse the project from Transport resource.

**Parameter**  
---  
**Name** | **Description**  
`transportName` |  `string`   
A fully-qualified path representing Transport resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchRemoteTransportProfileFromRemoteTransportProfileName(remoteTransportProfileName)
    
    
    matchRemoteTransportProfileFromRemoteTransportProfileName(remoteTransportProfileName: string): string | number;

Parse the remote_transport_profile from RemoteTransportProfile resource.

**Parameter**  
---  
**Name** | **Description**  
`remoteTransportProfileName` |  `string`   
A fully-qualified path representing RemoteTransportProfile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the remote_transport_profile.  
  
### matchRouteFromHubRouteName(hubRouteName)
    
    
    matchRouteFromHubRouteName(hubRouteName: string): string | number;

Parse the route from HubRoute resource.

**Parameter**  
---  
**Name** | **Description**  
`hubRouteName` |  `string`   
A fully-qualified path representing HubRoute resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the route.  
  
### matchRouteTableFromHubRouteName(hubRouteName)
    
    
    matchRouteTableFromHubRouteName(hubRouteName: string): string | number;

Parse the route_table from HubRoute resource.

**Parameter**  
---  
**Name** | **Description**  
`hubRouteName` |  `string`   
A fully-qualified path representing HubRoute resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the route_table.  
  
### matchRouteTableFromRouteTableName(routeTableName)
    
    
    matchRouteTableFromRouteTableName(routeTableName: string): string | number;

Parse the route_table from RouteTable resource.

**Parameter**  
---  
**Name** | **Description**  
`routeTableName` |  `string`   
A fully-qualified path representing RouteTable resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the route_table.  
  
### matchSpokeFromGatewayAdvertisedRouteName(gatewayAdvertisedRouteName)
    
    
    matchSpokeFromGatewayAdvertisedRouteName(gatewayAdvertisedRouteName: string): string | number;

Parse the spoke from GatewayAdvertisedRoute resource.

**Parameter**  
---  
**Name** | **Description**  
`gatewayAdvertisedRouteName` |  `string`   
A fully-qualified path representing GatewayAdvertisedRoute resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the spoke.  
  
### matchSpokeFromSpokeName(spokeName)
    
    
    matchSpokeFromSpokeName(spokeName: string): string | number;

Parse the spoke from Spoke resource.

**Parameter**  
---  
**Name** | **Description**  
`spokeName` |  `string`   
A fully-qualified path representing Spoke resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the spoke.  
  
### matchTransportFromTransportName(transportName)
    
    
    matchTransportFromTransportName(transportName: string): string | number;

Parse the transport from Transport resource.

**Parameter**  
---  
**Name** | **Description**  
`transportName` |  `string`   
A fully-qualified path representing Transport resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the transport.  
  
### multicloudDataTransferConfigPath(project, location, multicloudDataTransferConfig)
    
    
    multicloudDataTransferConfigPath(project: string, location: string, multicloudDataTransferConfig: string): string;

Return a fully-qualified multicloudDataTransferConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`multicloudDataTransferConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### multicloudDataTransferSupportedServicePath(project, location, multicloudDataTransferSupportedService)
    
    
    multicloudDataTransferSupportedServicePath(project: string, location: string, multicloudDataTransferSupportedService: string): string;

Return a fully-qualified multicloudDataTransferSupportedService resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`multicloudDataTransferSupportedService` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### policyBasedRoutePath(project, policyBasedRoute)
    
    
    policyBasedRoutePath(project: string, policyBasedRoute: string): string;

Return a fully-qualified policyBasedRoute resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`policyBasedRoute` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### remoteTransportProfilePath(project, location, remoteTransportProfile)
    
    
    remoteTransportProfilePath(project: string, location: string, remoteTransportProfile: string): string;

Return a fully-qualified remoteTransportProfile resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`remoteTransportProfile` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### routeTablePath(project, hub, routeTable)
    
    
    routeTablePath(project: string, hub: string, routeTable: string): string;

Return a fully-qualified routeTable resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`hub` |  `string`   
  
`routeTable` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### setIamPolicy(request, options, callback)
    
    
    setIamPolicy(request: IamProtos.google.iam.v1.SetIamPolicyRequest, options?: gax.CallOptions | Callback<IamProtos.google.iam.v1.Policy, IamProtos.google.iam.v1.SetIamPolicyRequest | null | undefined, {} | null | undefined>, callback?: Callback<IamProtos.google.iam.v1.Policy, IamProtos.google.iam.v1.SetIamPolicyRequest | null | undefined, {} | null | undefined>): Promise<[IamProtos.google.iam.v1.Policy]>;

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `IamProtos.google.iam.v1.SetIamPolicyRequest`   
The request object that will be sent.  
`options` |  `CallOptions | Callback<google.iam.v1.Policy, google.iam.v1.SetIamPolicyRequest | null | undefined, {} | null | undefined>`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/interfaces/CallOptions.html) for the details.  
`callback` |  `Callback<google.iam.v1.Policy, google.iam.v1.SetIamPolicyRequest | null | undefined, {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing .  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.Policy]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
  
### spokePath(project, location, spoke)
    
    
    spokePath(project: string, location: string, spoke: string): string;

Return a fully-qualified spoke resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`spoke` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### testIamPermissions(request, options, callback)
    
    
    testIamPermissions(request: IamProtos.google.iam.v1.TestIamPermissionsRequest, options?: gax.CallOptions | Callback<IamProtos.google.iam.v1.TestIamPermissionsResponse, IamProtos.google.iam.v1.TestIamPermissionsRequest | null | undefined, {} | null | undefined>, callback?: Callback<IamProtos.google.iam.v1.TestIamPermissionsResponse, IamProtos.google.iam.v1.TestIamPermissionsRequest | null | undefined, {} | null | undefined>): Promise<[IamProtos.google.iam.v1.TestIamPermissionsResponse]>;

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `IamProtos.google.iam.v1.TestIamPermissionsRequest`   
The request object that will be sent.  
`options` |  `CallOptions | Callback<google.iam.v1.TestIamPermissionsResponse, google.iam.v1.TestIamPermissionsRequest | null | undefined, {} | null | undefined>`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/interfaces/CallOptions.html) for the details.  
`callback` |  `Callback<google.iam.v1.TestIamPermissionsResponse, google.iam.v1.TestIamPermissionsRequest | null | undefined, {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing .  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.TestIamPermissionsResponse]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
  
### transportPath(project, location, transport)
    
    
    transportPath(project: string, location: string, transport: string): string;

Return a fully-qualified transport resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`transport` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### updateDestination(request, options)
    
    
    updateDestination(request?: protos.google.cloud.networkconnectivity.v1beta.IUpdateDestinationRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.networkconnectivity.v1beta.IDestination, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates a `Destination` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.iupdatedestinationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.networkconnectivity.v1beta.IDestination](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.idestination), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. `FieldMask is used to specify the fields to be overwritten in the
       *  `Destination` resource by the update.
       *  The fields specified in `update_mask` are relative to the resource, not
       *  the full request. A field is overwritten if it is in the mask. If you
       *  don't specify a mask, all fields are overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The `Destination` resource to update.
       */
      // const destination = {}
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server can ignore
       *  the request if it has already been completed. The server waits
       *  for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, can ignore the second request.
       *  The request ID must be a valid UUID with the exception that zero UUID
       *  (00000000-0000-0000-0000-000000000000) isn't supported.
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {DataTransferServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callUpdateDestination() {
        // Construct request
        const request = {
          destination,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.updateDestination(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateDestination();
    
    

### updateDestination(request, options, callback)
    
    
    updateDestination(request: protos.google.cloud.networkconnectivity.v1beta.IUpdateDestinationRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.networkconnectivity.v1beta.IDestination, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.iupdatedestinationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkconnectivity.v1beta.IDestination](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.idestination), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDestination(request, callback)
    
    
    updateDestination(request: protos.google.cloud.networkconnectivity.v1beta.IUpdateDestinationRequest, callback: Callback<LROperation<protos.google.cloud.networkconnectivity.v1beta.IDestination, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDestinationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.iupdatedestinationrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkconnectivity.v1beta.IDestination](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.idestination), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMulticloudDataTransferConfig(request, options)
    
    
    updateMulticloudDataTransferConfig(request?: protos.google.cloud.networkconnectivity.v1beta.IUpdateMulticloudDataTransferConfigRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates a `MulticloudDataTransferConfig` resource in a specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.iupdatemulticlouddatatransferconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.imulticlouddatatransferconfig), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. `FieldMask` is used to specify the fields in the
       *  `MulticloudDataTransferConfig` resource to be overwritten by the update.
       *  The fields specified in `update_mask` are relative to the resource, not
       *  the full request. A field is overwritten if it is in the mask. If you
       *  don't specify a mask, all fields are overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The `MulticloudDataTransferConfig` resource to update.
       */
      // const multicloudDataTransferConfig = {}
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server can ignore
       *  the request if it has already been completed. The server waits
       *  for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, can ignore the second request. This prevents
       *  clients from accidentally creating duplicate `MulticloudDataTransferConfig`
       *  resources.
       *  The request ID must be a valid UUID with the exception that zero UUID
       *  (00000000-0000-0000-0000-000000000000) isn't supported.
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {DataTransferServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [DataTransferServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callUpdateMulticloudDataTransferConfig() {
        // Construct request
        const request = {
          multicloudDataTransferConfig,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.updateMulticloudDataTransferConfig(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateMulticloudDataTransferConfig();
    
    

### updateMulticloudDataTransferConfig(request, options, callback)
    
    
    updateMulticloudDataTransferConfig(request: protos.google.cloud.networkconnectivity.v1beta.IUpdateMulticloudDataTransferConfigRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.iupdatemulticlouddatatransferconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.imulticlouddatatransferconfig), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMulticloudDataTransferConfig(request, callback)
    
    
    updateMulticloudDataTransferConfig(request: protos.google.cloud.networkconnectivity.v1beta.IUpdateMulticloudDataTransferConfigRequest, callback: Callback<LROperation<protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.iupdatemulticlouddatatransferconfigrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkconnectivity.v1beta.IMulticloudDataTransferConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.imulticlouddatatransferconfig), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
