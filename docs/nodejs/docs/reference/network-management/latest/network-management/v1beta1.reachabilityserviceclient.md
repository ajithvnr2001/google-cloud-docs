---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/v1beta1.reachabilityserviceclient
title: Class v1beta1.ReachabilityServiceClient (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:04:06.851071+00:00
---

# Class v1beta1.ReachabilityServiceClient (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/v1beta1.reachabilityserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.ReachabilityServiceClient (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.2.0  4.2.0  3.11.0  3.10.0  3.9.0  3.7.0  3.3.0  3.0.0  2.4.2  2.3.1  2.2.0  1.1.2  1.0.2 

The Reachability service in the Google Cloud Network Management API provides services that analyze the reachability within a single Google Virtual Private Cloud (VPC) network, between peered VPC networks, between VPC and on-premises networks, or between VPC networks and internet hosts. A reachability analysis is based on Google Cloud network configurations.

You can use the analysis results to verify these configurations and to troubleshoot connectivity issues. v1beta1

## Package

[@google-cloud/network-management](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of ReachabilityServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new ReachabilityServiceClient({fallback: true}, gax); ```  
  
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

### reachabilityServiceStub
    
    
    reachabilityServiceStub?: Promise<{
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

### cancelOperation(request, optionsOrCallback, callback)
    
    
    cancelOperation(request: protos.google.longrunning.CancelOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>, callback?: Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>): Promise<protos.google.protobuf.Empty>;

Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an value with a of 1, corresponding to `Code.CANCELLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### checkCreateConnectivityTestProgress(name)
    
    
    checkCreateConnectivityTestProgress(name: string): Promise<LROperation<protos.google.cloud.networkmanagement.v1beta1.ConnectivityTest, protos.google.cloud.networkmanagement.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `createConnectivityTest()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.networkmanagement.v1beta1.ConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.connectivitytest), [protos.google.cloud.networkmanagement.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource of the Connectivity Test to create:
       *      `projects/{project_id}/locations/global`
       */
      // const parent = 'abc123'
      /**
       *  Required. The logical name of the Connectivity Test in your project
       *  with the following restrictions:
       *  * Must contain only lowercase letters, numbers, and hyphens.
       *  * Must start with a letter.
       *  * Must be between 1-40 characters.
       *  * Must end with a number or a letter.
       *  * Must be unique within the customer project
       */
      // const testId = 'abc123'
      /**
       *  Required. A `ConnectivityTest` resource
       */
      // const resource = {}
    
      // Imports the Networkmanagement library
      const {ReachabilityServiceClient} = require('[@google-cloud/network-management](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networkmanagementClient = new [ReachabilityServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)();
    
      async function callCreateConnectivityTest() {
        // Construct request
        const request = {
          parent,
          testId,
          resource,
        };
    
        // Run request
        const [operation] = await networkmanagementClient.createConnectivityTest(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateConnectivityTest();
    
    

### checkDeleteConnectivityTestProgress(name)
    
    
    checkDeleteConnectivityTestProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.networkmanagement.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `deleteConnectivityTest()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.protobuf.empty), [protos.google.cloud.networkmanagement.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Connectivity Test resource name using the form:
       *      `projects/{project_id}/locations/global/connectivityTests/{test_id}`
       */
      // const name = 'abc123'
    
      // Imports the Networkmanagement library
      const {ReachabilityServiceClient} = require('[@google-cloud/network-management](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networkmanagementClient = new [ReachabilityServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)();
    
      async function callDeleteConnectivityTest() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networkmanagementClient.deleteConnectivityTest(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteConnectivityTest();
    
    

### checkRerunConnectivityTestProgress(name)
    
    
    checkRerunConnectivityTestProgress(name: string): Promise<LROperation<protos.google.cloud.networkmanagement.v1beta1.ConnectivityTest, protos.google.cloud.networkmanagement.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `rerunConnectivityTest()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.networkmanagement.v1beta1.ConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.connectivitytest), [protos.google.cloud.networkmanagement.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Connectivity Test resource name using the form:
       *      `projects/{project_id}/locations/global/connectivityTests/{test_id}`
       */
      // const name = 'abc123'
    
      // Imports the Networkmanagement library
      const {ReachabilityServiceClient} = require('[@google-cloud/network-management](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networkmanagementClient = new [ReachabilityServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)();
    
      async function callRerunConnectivityTest() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networkmanagementClient.rerunConnectivityTest(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callRerunConnectivityTest();
    
    

### checkUpdateConnectivityTestProgress(name)
    
    
    checkUpdateConnectivityTestProgress(name: string): Promise<LROperation<protos.google.cloud.networkmanagement.v1beta1.ConnectivityTest, protos.google.cloud.networkmanagement.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `updateConnectivityTest()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.networkmanagement.v1beta1.ConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.connectivitytest), [protos.google.cloud.networkmanagement.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Mask of fields to update. At least one path must be supplied in
       *  this field.
       */
      // const updateMask = {}
      /**
       *  Required. Only fields specified in update_mask are updated.
       */
      // const resource = {}
    
      // Imports the Networkmanagement library
      const {ReachabilityServiceClient} = require('[@google-cloud/network-management](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networkmanagementClient = new [ReachabilityServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)();
    
      async function callUpdateConnectivityTest() {
        // Construct request
        const request = {
          updateMask,
          resource,
        };
    
        // Run request
        const [operation] = await networkmanagementClient.updateConnectivityTest(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateConnectivityTest();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### connectivityTestPath(project, test)
    
    
    connectivityTestPath(project: string, test: string): string;

Return a fully-qualified connectivityTest resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`test` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### createConnectivityTest(request, options)
    
    
    createConnectivityTest(request?: protos.google.cloud.networkmanagement.v1beta1.ICreateConnectivityTestRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest, protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new Connectivity Test. After you create a test, the reachability analysis is performed as part of the long running operation, which completes when the analysis completes.

If the endpoint specifications in `ConnectivityTest` are invalid (for example, containing non-existent resources in the network, or you don't have read permissions to the network configurations of listed projects), then the reachability result returns a value of `UNKNOWN`.

If the endpoint specifications in `ConnectivityTest` are incomplete, the reachability result returns a value of `AMBIGUOUS`. For more information, see the Connectivity Test documentation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConnectivityTestRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.icreateconnectivitytestrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.iconnectivitytest), [protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource of the Connectivity Test to create:
       *      `projects/{project_id}/locations/global`
       */
      // const parent = 'abc123'
      /**
       *  Required. The logical name of the Connectivity Test in your project
       *  with the following restrictions:
       *  * Must contain only lowercase letters, numbers, and hyphens.
       *  * Must start with a letter.
       *  * Must be between 1-40 characters.
       *  * Must end with a number or a letter.
       *  * Must be unique within the customer project
       */
      // const testId = 'abc123'
      /**
       *  Required. A `ConnectivityTest` resource
       */
      // const resource = {}
    
      // Imports the Networkmanagement library
      const {ReachabilityServiceClient} = require('[@google-cloud/network-management](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networkmanagementClient = new [ReachabilityServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)();
    
      async function callCreateConnectivityTest() {
        // Construct request
        const request = {
          parent,
          testId,
          resource,
        };
    
        // Run request
        const [operation] = await networkmanagementClient.createConnectivityTest(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateConnectivityTest();
    
    

### createConnectivityTest(request, options, callback)
    
    
    createConnectivityTest(request: protos.google.cloud.networkmanagement.v1beta1.ICreateConnectivityTestRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest, protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConnectivityTestRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.icreateconnectivitytestrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.iconnectivitytest), [protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConnectivityTest(request, callback)
    
    
    createConnectivityTest(request: protos.google.cloud.networkmanagement.v1beta1.ICreateConnectivityTestRequest, callback: Callback<LROperation<protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest, protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConnectivityTestRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.icreateconnectivitytestrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.iconnectivitytest), [protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConnectivityTest(request, options)
    
    
    deleteConnectivityTest(request?: protos.google.cloud.networkmanagement.v1beta1.IDeleteConnectivityTestRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a specific `ConnectivityTest`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConnectivityTestRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ideleteconnectivitytestrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.protobuf.iempty), [protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Connectivity Test resource name using the form:
       *      `projects/{project_id}/locations/global/connectivityTests/{test_id}`
       */
      // const name = 'abc123'
    
      // Imports the Networkmanagement library
      const {ReachabilityServiceClient} = require('[@google-cloud/network-management](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networkmanagementClient = new [ReachabilityServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)();
    
      async function callDeleteConnectivityTest() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networkmanagementClient.deleteConnectivityTest(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteConnectivityTest();
    
    

### deleteConnectivityTest(request, options, callback)
    
    
    deleteConnectivityTest(request: protos.google.cloud.networkmanagement.v1beta1.IDeleteConnectivityTestRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConnectivityTestRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ideleteconnectivitytestrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.protobuf.iempty), [protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConnectivityTest(request, callback)
    
    
    deleteConnectivityTest(request: protos.google.cloud.networkmanagement.v1beta1.IDeleteConnectivityTestRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConnectivityTestRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ideleteconnectivitytestrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.protobuf.iempty), [protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### getConnectivityTest(request, options)
    
    
    getConnectivityTest(request?: protos.google.cloud.networkmanagement.v1beta1.IGetConnectivityTestRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest,
            (protos.google.cloud.networkmanagement.v1beta1.IGetConnectivityTestRequest | undefined),
            {} | undefined
        ]>;

Gets the details of a specific Connectivity Test.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectivityTestRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.igetconnectivitytestrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.iconnectivitytest), ([protos.google.cloud.networkmanagement.v1beta1.IGetConnectivityTestRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.igetconnectivitytestrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.connectivitytest). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. `ConnectivityTest` resource name using the form:
       *      `projects/{project_id}/locations/global/connectivityTests/{test_id}`
       */
      // const name = 'abc123'
    
      // Imports the Networkmanagement library
      const {ReachabilityServiceClient} = require('[@google-cloud/network-management](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networkmanagementClient = new [ReachabilityServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)();
    
      async function callGetConnectivityTest() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await networkmanagementClient.getConnectivityTest(request);
        console.log(response);
      }
    
      callGetConnectivityTest();
    
    

### getConnectivityTest(request, options, callback)
    
    
    getConnectivityTest(request: protos.google.cloud.networkmanagement.v1beta1.IGetConnectivityTestRequest, options: CallOptions, callback: Callback<protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest, protos.google.cloud.networkmanagement.v1beta1.IGetConnectivityTestRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectivityTestRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.igetconnectivitytestrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.iconnectivitytest), [protos.google.cloud.networkmanagement.v1beta1.IGetConnectivityTestRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.igetconnectivitytestrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConnectivityTest(request, callback)
    
    
    getConnectivityTest(request: protos.google.cloud.networkmanagement.v1beta1.IGetConnectivityTestRequest, callback: Callback<protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest, protos.google.cloud.networkmanagement.v1beta1.IGetConnectivityTestRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectivityTestRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.igetconnectivitytestrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.iconnectivitytest), [protos.google.cloud.networkmanagement.v1beta1.IGetConnectivityTestRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.igetconnectivitytestrequest) | null | undefined, {} | null | undefined>`   
  
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
    

### getOperation(request, optionsOrCallback, callback)
    
    
    getOperation(request: protos.google.longrunning.GetOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>, callback?: Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>): Promise<[protos.google.longrunning.Operation]>;

Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.operation)]>` |   
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
  
### listConnectivityTests(request, options)
    
    
    listConnectivityTests(request?: protos.google.cloud.networkmanagement.v1beta1.IListConnectivityTestsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest[],
            protos.google.cloud.networkmanagement.v1beta1.IListConnectivityTestsRequest | null,
            protos.google.cloud.networkmanagement.v1beta1.IListConnectivityTestsResponse
        ]>;

Lists all Connectivity Tests owned by a project.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConnectivityTestsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ilistconnectivitytestsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.iconnectivitytest)[], [protos.google.cloud.networkmanagement.v1beta1.IListConnectivityTestsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ilistconnectivitytestsrequest) | null, [protos.google.cloud.networkmanagement.v1beta1.IListConnectivityTestsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ilistconnectivitytestsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [ConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.connectivitytest). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listConnectivityTestsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listConnectivityTests(request, options, callback)
    
    
    listConnectivityTests(request: protos.google.cloud.networkmanagement.v1beta1.IListConnectivityTestsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.networkmanagement.v1beta1.IListConnectivityTestsRequest, protos.google.cloud.networkmanagement.v1beta1.IListConnectivityTestsResponse | null | undefined, protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConnectivityTestsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ilistconnectivitytestsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networkmanagement.v1beta1.IListConnectivityTestsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ilistconnectivitytestsrequest), [protos.google.cloud.networkmanagement.v1beta1.IListConnectivityTestsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ilistconnectivitytestsresponse) | null | undefined, [protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.iconnectivitytest)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConnectivityTests(request, callback)
    
    
    listConnectivityTests(request: protos.google.cloud.networkmanagement.v1beta1.IListConnectivityTestsRequest, callback: PaginationCallback<protos.google.cloud.networkmanagement.v1beta1.IListConnectivityTestsRequest, protos.google.cloud.networkmanagement.v1beta1.IListConnectivityTestsResponse | null | undefined, protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConnectivityTestsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ilistconnectivitytestsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networkmanagement.v1beta1.IListConnectivityTestsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ilistconnectivitytestsrequest), [protos.google.cloud.networkmanagement.v1beta1.IListConnectivityTestsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ilistconnectivitytestsresponse) | null | undefined, [protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.iconnectivitytest)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConnectivityTestsAsync(request, options)
    
    
    listConnectivityTestsAsync(request?: protos.google.cloud.networkmanagement.v1beta1.IListConnectivityTestsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest>;

Equivalent to `listConnectivityTests`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConnectivityTestsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ilistconnectivitytestsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.iconnectivitytest)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [ConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.connectivitytest). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource of the Connectivity Tests:
       *      `projects/{project_id}/locations/global`
       */
      // const parent = 'abc123'
      /**
       *  Number of `ConnectivityTests` to return.
       */
      // const pageSize = 1234
      /**
       *  Page token from an earlier query, as returned in `next_page_token`.
       */
      // const pageToken = 'abc123'
      /**
       *  Lists the `ConnectivityTests` that match the filter expression. A filter
       *  expression filters the resources listed in the response. The expression
       *  must be of the form `

### listConnectivityTestsStream(request, options)
    
    
    listConnectivityTestsStream(request?: protos.google.cloud.networkmanagement.v1beta1.IListConnectivityTestsRequest, options?: CallOptions): Transform;

Equivalent to `listConnectivityTests`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConnectivityTestsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ilistconnectivitytestsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [ConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.connectivitytest) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listConnectivityTestsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
**Example**
    
    
    const client = longrunning.operationsClient();
    for await (const response of client.listOperationsAsync(request));
    // doThingsWith(response)
    

### matchLocationFromOrganizationLocationVpcFlowLogsConfigsName(organizationLocationVpcFlowLogsConfigsName)
    
    
    matchLocationFromOrganizationLocationVpcFlowLogsConfigsName(organizationLocationVpcFlowLogsConfigsName: string): string | number;

Parse the location from OrganizationLocationVpcFlowLogsConfigs resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationLocationVpcFlowLogsConfigsName` |  `string`   
A fully-qualified path representing organization_location_vpcFlowLogsConfigs resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationVpcFlowLogsConfigsName(projectLocationVpcFlowLogsConfigsName)
    
    
    matchLocationFromProjectLocationVpcFlowLogsConfigsName(projectLocationVpcFlowLogsConfigsName: string): string | number;

Parse the location from ProjectLocationVpcFlowLogsConfigs resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationVpcFlowLogsConfigsName` |  `string`   
A fully-qualified path representing project_location_vpcFlowLogsConfigs resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchOrganizationFromOrganizationLocationVpcFlowLogsConfigsName(organizationLocationVpcFlowLogsConfigsName)
    
    
    matchOrganizationFromOrganizationLocationVpcFlowLogsConfigsName(organizationLocationVpcFlowLogsConfigsName: string): string | number;

Parse the organization from OrganizationLocationVpcFlowLogsConfigs resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationLocationVpcFlowLogsConfigsName` |  `string`   
A fully-qualified path representing organization_location_vpcFlowLogsConfigs resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the organization.  
  
### matchProjectFromConnectivityTestName(connectivityTestName)
    
    
    matchProjectFromConnectivityTestName(connectivityTestName: string): string | number;

Parse the project from ConnectivityTest resource.

**Parameter**  
---  
**Name** | **Description**  
`connectivityTestName` |  `string`   
A fully-qualified path representing ConnectivityTest resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationVpcFlowLogsConfigsName(projectLocationVpcFlowLogsConfigsName)
    
    
    matchProjectFromProjectLocationVpcFlowLogsConfigsName(projectLocationVpcFlowLogsConfigsName: string): string | number;

Parse the project from ProjectLocationVpcFlowLogsConfigs resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationVpcFlowLogsConfigsName` |  `string`   
A fully-qualified path representing project_location_vpcFlowLogsConfigs resource.  
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
  
### matchTestFromConnectivityTestName(connectivityTestName)
    
    
    matchTestFromConnectivityTestName(connectivityTestName: string): string | number;

Parse the test from ConnectivityTest resource.

**Parameter**  
---  
**Name** | **Description**  
`connectivityTestName` |  `string`   
A fully-qualified path representing ConnectivityTest resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the test.  
  
### matchVpcFlowLogsConfigFromOrganizationLocationVpcFlowLogsConfigsName(organizationLocationVpcFlowLogsConfigsName)
    
    
    matchVpcFlowLogsConfigFromOrganizationLocationVpcFlowLogsConfigsName(organizationLocationVpcFlowLogsConfigsName: string): string | number;

Parse the vpc_flow_logs_config from OrganizationLocationVpcFlowLogsConfigs resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationLocationVpcFlowLogsConfigsName` |  `string`   
A fully-qualified path representing organization_location_vpcFlowLogsConfigs resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the vpc_flow_logs_config.  
  
### matchVpcFlowLogsConfigFromProjectLocationVpcFlowLogsConfigsName(projectLocationVpcFlowLogsConfigsName)
    
    
    matchVpcFlowLogsConfigFromProjectLocationVpcFlowLogsConfigsName(projectLocationVpcFlowLogsConfigsName: string): string | number;

Parse the vpc_flow_logs_config from ProjectLocationVpcFlowLogsConfigs resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationVpcFlowLogsConfigsName` |  `string`   
A fully-qualified path representing project_location_vpcFlowLogsConfigs resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the vpc_flow_logs_config.  
  
### organizationLocationVpcFlowLogsConfigsPath(organization, location, vpcFlowLogsConfig)
    
    
    organizationLocationVpcFlowLogsConfigsPath(organization: string, location: string, vpcFlowLogsConfig: string): string;

Return a fully-qualified organizationLocationVpcFlowLogsConfigs resource name string.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`location` |  `string`   
  
`vpcFlowLogsConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationVpcFlowLogsConfigsPath(project, location, vpcFlowLogsConfig)
    
    
    projectLocationVpcFlowLogsConfigsPath(project: string, location: string, vpcFlowLogsConfig: string): string;

Return a fully-qualified projectLocationVpcFlowLogsConfigs resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`vpcFlowLogsConfig` |  `string`   
  
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
  
### rerunConnectivityTest(request, options)
    
    
    rerunConnectivityTest(request?: protos.google.cloud.networkmanagement.v1beta1.IRerunConnectivityTestRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest, protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Rerun an existing `ConnectivityTest`. After the user triggers the rerun, the reachability analysis is performed as part of the long running operation, which completes when the analysis completes.

Even though the test configuration remains the same, the reachability result may change due to underlying network configuration changes.

If the endpoint specifications in `ConnectivityTest` become invalid (for example, specified resources are deleted in the network, or you lost read permissions to the network configurations of listed projects), then the reachability result returns a value of `UNKNOWN`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRerunConnectivityTestRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.irerunconnectivitytestrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.iconnectivitytest), [protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Connectivity Test resource name using the form:
       *      `projects/{project_id}/locations/global/connectivityTests/{test_id}`
       */
      // const name = 'abc123'
    
      // Imports the Networkmanagement library
      const {ReachabilityServiceClient} = require('[@google-cloud/network-management](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networkmanagementClient = new [ReachabilityServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)();
    
      async function callRerunConnectivityTest() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networkmanagementClient.rerunConnectivityTest(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callRerunConnectivityTest();
    
    

### rerunConnectivityTest(request, options, callback)
    
    
    rerunConnectivityTest(request: protos.google.cloud.networkmanagement.v1beta1.IRerunConnectivityTestRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest, protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRerunConnectivityTestRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.irerunconnectivitytestrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.iconnectivitytest), [protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### rerunConnectivityTest(request, callback)
    
    
    rerunConnectivityTest(request: protos.google.cloud.networkmanagement.v1beta1.IRerunConnectivityTestRequest, callback: Callback<LROperation<protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest, protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRerunConnectivityTestRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.irerunconnectivitytestrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.iconnectivitytest), [protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
  
### updateConnectivityTest(request, options)
    
    
    updateConnectivityTest(request?: protos.google.cloud.networkmanagement.v1beta1.IUpdateConnectivityTestRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest, protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the configuration of an existing `ConnectivityTest`. After you update a test, the reachability analysis is performed as part of the long running operation, which completes when the analysis completes. The Reachability state in the test resource is updated with the new result.

If the endpoint specifications in `ConnectivityTest` are invalid (for example, they contain non-existent resources in the network, or the user does not have read permissions to the network configurations of listed projects), then the reachability result returns a value of `UNKNOWN`.

If the endpoint specifications in `ConnectivityTest` are incomplete, the reachability result returns a value of `AMBIGUOUS`. See the documentation in `ConnectivityTest` for more details.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConnectivityTestRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.iupdateconnectivitytestrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.iconnectivitytest), [protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Mask of fields to update. At least one path must be supplied in
       *  this field.
       */
      // const updateMask = {}
      /**
       *  Required. Only fields specified in update_mask are updated.
       */
      // const resource = {}
    
      // Imports the Networkmanagement library
      const {ReachabilityServiceClient} = require('[@google-cloud/network-management](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networkmanagementClient = new [ReachabilityServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)();
    
      async function callUpdateConnectivityTest() {
        // Construct request
        const request = {
          updateMask,
          resource,
        };
    
        // Run request
        const [operation] = await networkmanagementClient.updateConnectivityTest(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateConnectivityTest();
    
    

### updateConnectivityTest(request, options, callback)
    
    
    updateConnectivityTest(request: protos.google.cloud.networkmanagement.v1beta1.IUpdateConnectivityTestRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest, protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConnectivityTestRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.iupdateconnectivitytestrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.iconnectivitytest), [protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConnectivityTest(request, callback)
    
    
    updateConnectivityTest(request: protos.google.cloud.networkmanagement.v1beta1.IUpdateConnectivityTestRequest, callback: Callback<LROperation<protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest, protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConnectivityTestRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.iupdateconnectivitytestrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkmanagement.v1beta1.IConnectivityTest](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.iconnectivitytest), [protos.google.cloud.networkmanagement.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
