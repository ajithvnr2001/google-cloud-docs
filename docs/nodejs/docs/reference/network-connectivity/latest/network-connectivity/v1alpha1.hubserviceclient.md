---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/v1alpha1.hubserviceclient
title: Class v1alpha1.HubServiceClient (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:14.558842+00:00
---

# Class v1alpha1.HubServiceClient (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/v1alpha1.hubserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1alpha1.HubServiceClient (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.6.0  4.2.0  3.6.0  3.2.0  2.3.3  2.2.0  2.1.2  1.5.0  1.4.2  1.3.0  1.2.1  1.1.6 

Network Connectivity Center is a hub-and-spoke abstraction for network connectivity management in Google Cloud. It reduces operational complexity through a simple, centralized connectivity management model. v1alpha1

## Package

[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of HubServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new HubServiceClient({fallback: true}, gax); ```  
  
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

### hubServiceStub
    
    
    hubServiceStub?: Promise<{
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

### checkCreateHubProgress(name)
    
    
    checkCreateHubProgress(name: string): Promise<LROperation<protos.google.cloud.networkconnectivity.v1alpha1.Hub, protos.google.cloud.networkconnectivity.v1alpha1.OperationMetadata>>;

Check the status of the long running operation returned by `createHub()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.networkconnectivity.v1alpha1.Hub](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.hub), [protos.google.cloud.networkconnectivity.v1alpha1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource's name of the Hub.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Unique id for the Hub to create.
       */
      // const hubId = 'abc123'
      /**
       *  Required. Initial values for a new Hub.
       */
      // const hub = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {HubServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networkconnectivityClient = new [HubServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callCreateHub() {
        // Construct request
        const request = {
          parent,
          hub,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.createHub(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateHub();
    
    

### checkCreateSpokeProgress(name)
    
    
    checkCreateSpokeProgress(name: string): Promise<LROperation<protos.google.cloud.networkconnectivity.v1alpha1.Spoke, protos.google.cloud.networkconnectivity.v1alpha1.OperationMetadata>>;

Check the status of the long running operation returned by `createSpoke()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.networkconnectivity.v1alpha1.Spoke](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.spoke), [protos.google.cloud.networkconnectivity.v1alpha1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent's resource name of the Spoke.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Unique id for the Spoke to create.
       */
      // const spokeId = 'abc123'
      /**
       *  Required. Initial values for a new Hub.
       */
      // const spoke = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {HubServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networkconnectivityClient = new [HubServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callCreateSpoke() {
        // Construct request
        const request = {
          parent,
          spoke,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.createSpoke(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateSpoke();
    
    

### checkDeleteHubProgress(name)
    
    
    checkDeleteHubProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.networkconnectivity.v1alpha1.OperationMetadata>>;

Check the status of the long running operation returned by `deleteHub()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.empty), [protos.google.cloud.networkconnectivity.v1alpha1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Hub to delete.
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {HubServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networkconnectivityClient = new [HubServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callDeleteHub() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.deleteHub(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteHub();
    
    

### checkDeleteSpokeProgress(name)
    
    
    checkDeleteSpokeProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.networkconnectivity.v1alpha1.OperationMetadata>>;

Check the status of the long running operation returned by `deleteSpoke()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.empty), [protos.google.cloud.networkconnectivity.v1alpha1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Spoke to delete.
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {HubServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networkconnectivityClient = new [HubServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callDeleteSpoke() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.deleteSpoke(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteSpoke();
    
    

### checkUpdateHubProgress(name)
    
    
    checkUpdateHubProgress(name: string): Promise<LROperation<protos.google.cloud.networkconnectivity.v1alpha1.Hub, protos.google.cloud.networkconnectivity.v1alpha1.OperationMetadata>>;

Check the status of the long running operation returned by `updateHub()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.networkconnectivity.v1alpha1.Hub](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.hub), [protos.google.cloud.networkconnectivity.v1alpha1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Field mask is used to specify the fields to be overwritten in the
       *  Hub resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then all fields will be overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The state that the Hub should be in after the update.
       */
      // const hub = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {HubServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networkconnectivityClient = new [HubServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callUpdateHub() {
        // Construct request
        const request = {
          hub,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.updateHub(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateHub();
    
    

### checkUpdateSpokeProgress(name)
    
    
    checkUpdateSpokeProgress(name: string): Promise<LROperation<protos.google.cloud.networkconnectivity.v1alpha1.Spoke, protos.google.cloud.networkconnectivity.v1alpha1.OperationMetadata>>;

Check the status of the long running operation returned by `updateSpoke()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.networkconnectivity.v1alpha1.Spoke](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.spoke), [protos.google.cloud.networkconnectivity.v1alpha1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Field mask is used to specify the fields to be overwritten in the
       *  Spoke resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then all fields will be overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The state that the Spoke should be in after the update.
       */
      // const spoke = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {HubServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networkconnectivityClient = new [HubServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callUpdateSpoke() {
        // Construct request
        const request = {
          spoke,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.updateSpoke(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateSpoke();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### createHub(request, options)
    
    
    createHub(request?: protos.google.cloud.networkconnectivity.v1alpha1.ICreateHubRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.networkconnectivity.v1alpha1.IHub, protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new Hub in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.icreatehubrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.networkconnectivity.v1alpha1.IHub](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ihub), [protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource's name of the Hub.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Unique id for the Hub to create.
       */
      // const hubId = 'abc123'
      /**
       *  Required. Initial values for a new Hub.
       */
      // const hub = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {HubServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networkconnectivityClient = new [HubServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callCreateHub() {
        // Construct request
        const request = {
          parent,
          hub,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.createHub(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateHub();
    
    

### createHub(request, options, callback)
    
    
    createHub(request: protos.google.cloud.networkconnectivity.v1alpha1.ICreateHubRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.networkconnectivity.v1alpha1.IHub, protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.icreatehubrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkconnectivity.v1alpha1.IHub](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ihub), [protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createHub(request, callback)
    
    
    createHub(request: protos.google.cloud.networkconnectivity.v1alpha1.ICreateHubRequest, callback: Callback<LROperation<protos.google.cloud.networkconnectivity.v1alpha1.IHub, protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.icreatehubrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkconnectivity.v1alpha1.IHub](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ihub), [protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSpoke(request, options)
    
    
    createSpoke(request?: protos.google.cloud.networkconnectivity.v1alpha1.ICreateSpokeRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.networkconnectivity.v1alpha1.ISpoke, protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new Spoke in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.icreatespokerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.networkconnectivity.v1alpha1.ISpoke](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ispoke), [protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent's resource name of the Spoke.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Unique id for the Spoke to create.
       */
      // const spokeId = 'abc123'
      /**
       *  Required. Initial values for a new Hub.
       */
      // const spoke = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {HubServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networkconnectivityClient = new [HubServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callCreateSpoke() {
        // Construct request
        const request = {
          parent,
          spoke,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.createSpoke(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateSpoke();
    
    

### createSpoke(request, options, callback)
    
    
    createSpoke(request: protos.google.cloud.networkconnectivity.v1alpha1.ICreateSpokeRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.networkconnectivity.v1alpha1.ISpoke, protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.icreatespokerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkconnectivity.v1alpha1.ISpoke](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ispoke), [protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSpoke(request, callback)
    
    
    createSpoke(request: protos.google.cloud.networkconnectivity.v1alpha1.ICreateSpokeRequest, callback: Callback<LROperation<protos.google.cloud.networkconnectivity.v1alpha1.ISpoke, protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.icreatespokerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkconnectivity.v1alpha1.ISpoke](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ispoke), [protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteHub(request, options)
    
    
    deleteHub(request?: protos.google.cloud.networkconnectivity.v1alpha1.IDeleteHubRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a single Hub.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ideletehubrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.iempty), [protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Hub to delete.
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {HubServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networkconnectivityClient = new [HubServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callDeleteHub() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.deleteHub(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteHub();
    
    

### deleteHub(request, options, callback)
    
    
    deleteHub(request: protos.google.cloud.networkconnectivity.v1alpha1.IDeleteHubRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ideletehubrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.iempty), [protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteHub(request, callback)
    
    
    deleteHub(request: protos.google.cloud.networkconnectivity.v1alpha1.IDeleteHubRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ideletehubrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.iempty), [protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSpoke(request, options)
    
    
    deleteSpoke(request?: protos.google.cloud.networkconnectivity.v1alpha1.IDeleteSpokeRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a single Spoke.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ideletespokerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.iempty), [protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Spoke to delete.
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {HubServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networkconnectivityClient = new [HubServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callDeleteSpoke() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.deleteSpoke(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteSpoke();
    
    

### deleteSpoke(request, options, callback)
    
    
    deleteSpoke(request: protos.google.cloud.networkconnectivity.v1alpha1.IDeleteSpokeRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ideletespokerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.iempty), [protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSpoke(request, callback)
    
    
    deleteSpoke(request: protos.google.cloud.networkconnectivity.v1alpha1.IDeleteSpokeRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ideletespokerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.iempty), [protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getHub(request, options)
    
    
    getHub(request?: protos.google.cloud.networkconnectivity.v1alpha1.IGetHubRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networkconnectivity.v1alpha1.IHub,
            (protos.google.cloud.networkconnectivity.v1alpha1.IGetHubRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single Hub.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.igethubrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networkconnectivity.v1alpha1.IHub](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ihub), ([protos.google.cloud.networkconnectivity.v1alpha1.IGetHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.igethubrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Hub](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.hub). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the Hub resource to get.
       */
      // const name = 'abc123'
    
      // Imports the Networkconnectivity library
      const {HubServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networkconnectivityClient = new [HubServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callGetHub() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await networkconnectivityClient.getHub(request);
        console.log(response);
      }
    
      callGetHub();
    
    

### getHub(request, options, callback)
    
    
    getHub(request: protos.google.cloud.networkconnectivity.v1alpha1.IGetHubRequest, options: CallOptions, callback: Callback<protos.google.cloud.networkconnectivity.v1alpha1.IHub, protos.google.cloud.networkconnectivity.v1alpha1.IGetHubRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.igethubrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.networkconnectivity.v1alpha1.IHub](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ihub), [protos.google.cloud.networkconnectivity.v1alpha1.IGetHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.igethubrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getHub(request, callback)
    
    
    getHub(request: protos.google.cloud.networkconnectivity.v1alpha1.IGetHubRequest, callback: Callback<protos.google.cloud.networkconnectivity.v1alpha1.IHub, protos.google.cloud.networkconnectivity.v1alpha1.IGetHubRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.igethubrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.networkconnectivity.v1alpha1.IHub](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ihub), [protos.google.cloud.networkconnectivity.v1alpha1.IGetHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.igethubrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### getSpoke(request, options)
    
    
    getSpoke(request?: protos.google.cloud.networkconnectivity.v1alpha1.IGetSpokeRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networkconnectivity.v1alpha1.ISpoke,
            (protos.google.cloud.networkconnectivity.v1alpha1.IGetSpokeRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single Spoke.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.igetspokerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networkconnectivity.v1alpha1.ISpoke](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ispoke), ([protos.google.cloud.networkconnectivity.v1alpha1.IGetSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.igetspokerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Spoke](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.spoke). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of Spoke resource.
       */
      // const name = 'abc123'
    
      // Imports the Networkconnectivity library
      const {HubServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networkconnectivityClient = new [HubServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callGetSpoke() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await networkconnectivityClient.getSpoke(request);
        console.log(response);
      }
    
      callGetSpoke();
    
    

### getSpoke(request, options, callback)
    
    
    getSpoke(request: protos.google.cloud.networkconnectivity.v1alpha1.IGetSpokeRequest, options: CallOptions, callback: Callback<protos.google.cloud.networkconnectivity.v1alpha1.ISpoke, protos.google.cloud.networkconnectivity.v1alpha1.IGetSpokeRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.igetspokerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.networkconnectivity.v1alpha1.ISpoke](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ispoke), [protos.google.cloud.networkconnectivity.v1alpha1.IGetSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.igetspokerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSpoke(request, callback)
    
    
    getSpoke(request: protos.google.cloud.networkconnectivity.v1alpha1.IGetSpokeRequest, callback: Callback<protos.google.cloud.networkconnectivity.v1alpha1.ISpoke, protos.google.cloud.networkconnectivity.v1alpha1.IGetSpokeRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.igetspokerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.networkconnectivity.v1alpha1.ISpoke](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ispoke), [protos.google.cloud.networkconnectivity.v1alpha1.IGetSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.igetspokerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
  
### instancePath(project, zone, instance)
    
    
    instancePath(project: string, zone: string, instance: string): string;

Return a fully-qualified instance resource name string.

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
  
### interconnectAttachmentPath(project, region, resourceId)
    
    
    interconnectAttachmentPath(project: string, region: string, resourceId: string): string;

Return a fully-qualified interconnectAttachment resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`region` |  `string`   
  
`resourceId` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### listHubs(request, options)
    
    
    listHubs(request?: protos.google.cloud.networkconnectivity.v1alpha1.IListHubsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networkconnectivity.v1alpha1.IHub[],
            protos.google.cloud.networkconnectivity.v1alpha1.IListHubsRequest | null,
            protos.google.cloud.networkconnectivity.v1alpha1.IListHubsResponse
        ]>;

Lists Hubs in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListHubsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilisthubsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networkconnectivity.v1alpha1.IHub](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ihub)[], [protos.google.cloud.networkconnectivity.v1alpha1.IListHubsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilisthubsrequest) | null, [protos.google.cloud.networkconnectivity.v1alpha1.IListHubsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilisthubsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Hub](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.hub). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listHubsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listHubs(request, options, callback)
    
    
    listHubs(request: protos.google.cloud.networkconnectivity.v1alpha1.IListHubsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.networkconnectivity.v1alpha1.IListHubsRequest, protos.google.cloud.networkconnectivity.v1alpha1.IListHubsResponse | null | undefined, protos.google.cloud.networkconnectivity.v1alpha1.IHub>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListHubsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilisthubsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networkconnectivity.v1alpha1.IListHubsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilisthubsrequest), [protos.google.cloud.networkconnectivity.v1alpha1.IListHubsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilisthubsresponse) | null | undefined, [protos.google.cloud.networkconnectivity.v1alpha1.IHub](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ihub)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listHubs(request, callback)
    
    
    listHubs(request: protos.google.cloud.networkconnectivity.v1alpha1.IListHubsRequest, callback: PaginationCallback<protos.google.cloud.networkconnectivity.v1alpha1.IListHubsRequest, protos.google.cloud.networkconnectivity.v1alpha1.IListHubsResponse | null | undefined, protos.google.cloud.networkconnectivity.v1alpha1.IHub>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListHubsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilisthubsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networkconnectivity.v1alpha1.IListHubsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilisthubsrequest), [protos.google.cloud.networkconnectivity.v1alpha1.IListHubsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilisthubsresponse) | null | undefined, [protos.google.cloud.networkconnectivity.v1alpha1.IHub](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ihub)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listHubsAsync(request, options)
    
    
    listHubsAsync(request?: protos.google.cloud.networkconnectivity.v1alpha1.IListHubsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.networkconnectivity.v1alpha1.IHub>;

Equivalent to `listHubs`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListHubsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilisthubsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.networkconnectivity.v1alpha1.IHub](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ihub)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Hub](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.hub). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource's name.
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of results per page that should be returned.
       */
      // const pageSize = 1234
      /**
       *  The page token.
       */
      // const pageToken = 'abc123'
      /**
       *  A filter expression that filters the results listed in the response.
       */
      // const filter = 'abc123'
      /**
       *  Sort the results by a certain order.
       */
      // const orderBy = 'abc123'
    
      // Imports the Networkconnectivity library
      const {HubServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networkconnectivityClient = new [HubServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callListHubs() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = networkconnectivityClient.listHubsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListHubs();
    
    

### listHubsStream(request, options)
    
    
    listHubsStream(request?: protos.google.cloud.networkconnectivity.v1alpha1.IListHubsRequest, options?: CallOptions): Transform;

Equivalent to `listHubs`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListHubsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilisthubsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Hub](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.hub) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listHubsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listSpokes(request, options)
    
    
    listSpokes(request?: protos.google.cloud.networkconnectivity.v1alpha1.IListSpokesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networkconnectivity.v1alpha1.ISpoke[],
            protos.google.cloud.networkconnectivity.v1alpha1.IListSpokesRequest | null,
            protos.google.cloud.networkconnectivity.v1alpha1.IListSpokesResponse
        ]>;

Lists Spokes in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSpokesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilistspokesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networkconnectivity.v1alpha1.ISpoke](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ispoke)[], [protos.google.cloud.networkconnectivity.v1alpha1.IListSpokesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilistspokesrequest) | null, [protos.google.cloud.networkconnectivity.v1alpha1.IListSpokesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilistspokesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Spoke](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.spoke). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listSpokesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listSpokes(request, options, callback)
    
    
    listSpokes(request: protos.google.cloud.networkconnectivity.v1alpha1.IListSpokesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.networkconnectivity.v1alpha1.IListSpokesRequest, protos.google.cloud.networkconnectivity.v1alpha1.IListSpokesResponse | null | undefined, protos.google.cloud.networkconnectivity.v1alpha1.ISpoke>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSpokesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilistspokesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networkconnectivity.v1alpha1.IListSpokesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilistspokesrequest), [protos.google.cloud.networkconnectivity.v1alpha1.IListSpokesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilistspokesresponse) | null | undefined, [protos.google.cloud.networkconnectivity.v1alpha1.ISpoke](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ispoke)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSpokes(request, callback)
    
    
    listSpokes(request: protos.google.cloud.networkconnectivity.v1alpha1.IListSpokesRequest, callback: PaginationCallback<protos.google.cloud.networkconnectivity.v1alpha1.IListSpokesRequest, protos.google.cloud.networkconnectivity.v1alpha1.IListSpokesResponse | null | undefined, protos.google.cloud.networkconnectivity.v1alpha1.ISpoke>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSpokesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilistspokesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networkconnectivity.v1alpha1.IListSpokesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilistspokesrequest), [protos.google.cloud.networkconnectivity.v1alpha1.IListSpokesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilistspokesresponse) | null | undefined, [protos.google.cloud.networkconnectivity.v1alpha1.ISpoke](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ispoke)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSpokesAsync(request, options)
    
    
    listSpokesAsync(request?: protos.google.cloud.networkconnectivity.v1alpha1.IListSpokesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.networkconnectivity.v1alpha1.ISpoke>;

Equivalent to `listSpokes`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSpokesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilistspokesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.networkconnectivity.v1alpha1.ISpoke](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ispoke)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Spoke](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.spoke). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent's resource name.
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of results per page that should be returned.
       */
      // const pageSize = 1234
      /**
       *  The page token.
       */
      // const pageToken = 'abc123'
      /**
       *  A filter expression that filters the results listed in the response.
       */
      // const filter = 'abc123'
      /**
       *  Sort the results by a certain order.
       */
      // const orderBy = 'abc123'
    
      // Imports the Networkconnectivity library
      const {HubServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networkconnectivityClient = new [HubServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callListSpokes() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = networkconnectivityClient.listSpokesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListSpokes();
    
    

### listSpokesStream(request, options)
    
    
    listSpokesStream(request?: protos.google.cloud.networkconnectivity.v1alpha1.IListSpokesRequest, options?: CallOptions): Transform;

Equivalent to `listSpokes`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSpokesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilistspokesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Spoke](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.spoke) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listSpokesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### matchProjectFromInterconnectAttachmentName(interconnectAttachmentName)
    
    
    matchProjectFromInterconnectAttachmentName(interconnectAttachmentName: string): string | number;

Parse the project from InterconnectAttachment resource.

**Parameter**  
---  
**Name** | **Description**  
`interconnectAttachmentName` |  `string`   
A fully-qualified path representing InterconnectAttachment resource.  
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
  
### matchProjectFromVpnTunnelName(vpnTunnelName)
    
    
    matchProjectFromVpnTunnelName(vpnTunnelName: string): string | number;

Parse the project from VpnTunnel resource.

**Parameter**  
---  
**Name** | **Description**  
`vpnTunnelName` |  `string`   
A fully-qualified path representing VpnTunnel resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchRegionFromInterconnectAttachmentName(interconnectAttachmentName)
    
    
    matchRegionFromInterconnectAttachmentName(interconnectAttachmentName: string): string | number;

Parse the region from InterconnectAttachment resource.

**Parameter**  
---  
**Name** | **Description**  
`interconnectAttachmentName` |  `string`   
A fully-qualified path representing InterconnectAttachment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the region.  
  
### matchRegionFromVpnTunnelName(vpnTunnelName)
    
    
    matchRegionFromVpnTunnelName(vpnTunnelName: string): string | number;

Parse the region from VpnTunnel resource.

**Parameter**  
---  
**Name** | **Description**  
`vpnTunnelName` |  `string`   
A fully-qualified path representing VpnTunnel resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the region.  
  
### matchResourceIdFromInterconnectAttachmentName(interconnectAttachmentName)
    
    
    matchResourceIdFromInterconnectAttachmentName(interconnectAttachmentName: string): string | number;

Parse the resource_id from InterconnectAttachment resource.

**Parameter**  
---  
**Name** | **Description**  
`interconnectAttachmentName` |  `string`   
A fully-qualified path representing InterconnectAttachment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the resource_id.  
  
### matchResourceIdFromVpnTunnelName(vpnTunnelName)
    
    
    matchResourceIdFromVpnTunnelName(vpnTunnelName: string): string | number;

Parse the resource_id from VpnTunnel resource.

**Parameter**  
---  
**Name** | **Description**  
`vpnTunnelName` |  `string`   
A fully-qualified path representing VpnTunnel resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the resource_id.  
  
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
  
### matchZoneFromInstanceName(instanceName)
    
    
    matchZoneFromInstanceName(instanceName: string): string | number;

Parse the zone from Instance resource.

**Parameter**  
---  
**Name** | **Description**  
`instanceName` |  `string`   
A fully-qualified path representing Instance resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the zone.  
  
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
  
### updateHub(request, options)
    
    
    updateHub(request?: protos.google.cloud.networkconnectivity.v1alpha1.IUpdateHubRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.networkconnectivity.v1alpha1.IHub, protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the parameters of a single Hub.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.iupdatehubrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.networkconnectivity.v1alpha1.IHub](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ihub), [protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Field mask is used to specify the fields to be overwritten in the
       *  Hub resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then all fields will be overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The state that the Hub should be in after the update.
       */
      // const hub = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {HubServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networkconnectivityClient = new [HubServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callUpdateHub() {
        // Construct request
        const request = {
          hub,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.updateHub(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateHub();
    
    

### updateHub(request, options, callback)
    
    
    updateHub(request: protos.google.cloud.networkconnectivity.v1alpha1.IUpdateHubRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.networkconnectivity.v1alpha1.IHub, protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.iupdatehubrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkconnectivity.v1alpha1.IHub](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ihub), [protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateHub(request, callback)
    
    
    updateHub(request: protos.google.cloud.networkconnectivity.v1alpha1.IUpdateHubRequest, callback: Callback<LROperation<protos.google.cloud.networkconnectivity.v1alpha1.IHub, protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.iupdatehubrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkconnectivity.v1alpha1.IHub](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ihub), [protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSpoke(request, options)
    
    
    updateSpoke(request?: protos.google.cloud.networkconnectivity.v1alpha1.IUpdateSpokeRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.networkconnectivity.v1alpha1.ISpoke, protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the parameters of a single Spoke.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.iupdatespokerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.networkconnectivity.v1alpha1.ISpoke](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ispoke), [protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Field mask is used to specify the fields to be overwritten in the
       *  Spoke resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then all fields will be overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The state that the Spoke should be in after the update.
       */
      // const spoke = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {HubServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networkconnectivityClient = new [HubServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callUpdateSpoke() {
        // Construct request
        const request = {
          spoke,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.updateSpoke(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateSpoke();
    
    

### updateSpoke(request, options, callback)
    
    
    updateSpoke(request: protos.google.cloud.networkconnectivity.v1alpha1.IUpdateSpokeRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.networkconnectivity.v1alpha1.ISpoke, protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.iupdatespokerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkconnectivity.v1alpha1.ISpoke](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ispoke), [protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSpoke(request, callback)
    
    
    updateSpoke(request: protos.google.cloud.networkconnectivity.v1alpha1.IUpdateSpokeRequest, callback: Callback<LROperation<protos.google.cloud.networkconnectivity.v1alpha1.ISpoke, protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.iupdatespokerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkconnectivity.v1alpha1.ISpoke](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ispoke), [protos.google.cloud.networkconnectivity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### vpnTunnelPath(project, region, resourceId)
    
    
    vpnTunnelPath(project: string, region: string, resourceId: string): string;

Return a fully-qualified vpnTunnel resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`region` |  `string`   
  
`resourceId` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
