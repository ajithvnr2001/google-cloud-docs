---
url: https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient
title: Class v1beta.WorkloadIdentityPoolsClient (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:15:28.868013+00:00
---

# Class v1beta.WorkloadIdentityPoolsClient (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.WorkloadIdentityPoolsClient (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.2.0  0.3.2  0.2.2 

Manages WorkloadIdentityPools. v1beta

## Package

[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of WorkloadIdentityPoolsClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new WorkloadIdentityPoolsClient({fallback: true}, gax); ```  
  
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

### workloadIdentityPoolsStub
    
    
    workloadIdentityPoolsStub?: Promise<{
            [name: string]: Function;
        }>;

## Methods 

### checkCreateWorkloadIdentityPoolProgress(name)
    
    
    checkCreateWorkloadIdentityPoolProgress(name: string): Promise<LROperation<protos.google.iam.v1beta.WorkloadIdentityPool, protos.google.iam.v1beta.WorkloadIdentityPoolOperationMetadata>>;

Check the status of the long running operation returned by `createWorkloadIdentityPool()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.iam.v1beta.WorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.workloadidentitypool-class), [protos.google.iam.v1beta.WorkloadIdentityPoolOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.workloadidentitypooloperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource to create the pool in. The only supported
       *  location is `global`.
       */
      // const parent = 'abc123'
      /**
       *  Required. The pool to create.
       */
      // const workloadIdentityPool = {}
      /**
       *  Required. The ID to use for the pool, which becomes the
       *  final component of the resource name. This value should be 4-32 characters,
       *  and may contain the characters a-z0-9-. The prefix `gcp-` is
       *  reserved for use by Google, and may not be specified.
       */
      // const workloadIdentityPoolId = 'abc123'
    
      // Imports the Iam library
      const {WorkloadIdentityPoolsClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const iamClient = new [WorkloadIdentityPoolsClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)();
    
      async function callCreateWorkloadIdentityPool() {
        // Construct request
        const request = {
          parent,
          workloadIdentityPool,
          workloadIdentityPoolId,
        };
    
        // Run request
        const [operation] = await iamClient.createWorkloadIdentityPool(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateWorkloadIdentityPool();
    
    

### checkCreateWorkloadIdentityPoolProviderProgress(name)
    
    
    checkCreateWorkloadIdentityPoolProviderProgress(name: string): Promise<LROperation<protos.google.iam.v1beta.WorkloadIdentityPoolProvider, protos.google.iam.v1beta.WorkloadIdentityPoolProviderOperationMetadata>>;

Check the status of the long running operation returned by `createWorkloadIdentityPoolProvider()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.iam.v1beta.WorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.workloadidentitypoolprovider-class), [protos.google.iam.v1beta.WorkloadIdentityPoolProviderOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.workloadidentitypoolprovideroperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The pool to create this provider in.
       */
      // const parent = 'abc123'
      /**
       *  Required. The provider to create.
       */
      // const workloadIdentityPoolProvider = {}
      /**
       *  Required. The ID for the provider, which becomes the
       *  final component of the resource name. This value must be 4-32 characters,
       *  and may contain the characters a-z0-9-. The prefix `gcp-` is
       *  reserved for use by Google, and may not be specified.
       */
      // const workloadIdentityPoolProviderId = 'abc123'
    
      // Imports the Iam library
      const {WorkloadIdentityPoolsClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const iamClient = new [WorkloadIdentityPoolsClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)();
    
      async function callCreateWorkloadIdentityPoolProvider() {
        // Construct request
        const request = {
          parent,
          workloadIdentityPoolProvider,
          workloadIdentityPoolProviderId,
        };
    
        // Run request
        const [operation] = await iamClient.createWorkloadIdentityPoolProvider(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateWorkloadIdentityPoolProvider();
    
    

### checkDeleteWorkloadIdentityPoolProgress(name)
    
    
    checkDeleteWorkloadIdentityPoolProgress(name: string): Promise<LROperation<protos.google.iam.v1beta.WorkloadIdentityPool, protos.google.iam.v1beta.WorkloadIdentityPoolOperationMetadata>>;

Check the status of the long running operation returned by `deleteWorkloadIdentityPool()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.iam.v1beta.WorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.workloadidentitypool-class), [protos.google.iam.v1beta.WorkloadIdentityPoolOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.workloadidentitypooloperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the pool to delete.
       */
      // const name = 'abc123'
    
      // Imports the Iam library
      const {WorkloadIdentityPoolsClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const iamClient = new [WorkloadIdentityPoolsClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)();
    
      async function callDeleteWorkloadIdentityPool() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await iamClient.deleteWorkloadIdentityPool(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteWorkloadIdentityPool();
    
    

### checkDeleteWorkloadIdentityPoolProviderProgress(name)
    
    
    checkDeleteWorkloadIdentityPoolProviderProgress(name: string): Promise<LROperation<protos.google.iam.v1beta.WorkloadIdentityPoolProvider, protos.google.iam.v1beta.WorkloadIdentityPoolProviderOperationMetadata>>;

Check the status of the long running operation returned by `deleteWorkloadIdentityPoolProvider()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.iam.v1beta.WorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.workloadidentitypoolprovider-class), [protos.google.iam.v1beta.WorkloadIdentityPoolProviderOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.workloadidentitypoolprovideroperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the provider to delete.
       */
      // const name = 'abc123'
    
      // Imports the Iam library
      const {WorkloadIdentityPoolsClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const iamClient = new [WorkloadIdentityPoolsClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)();
    
      async function callDeleteWorkloadIdentityPoolProvider() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await iamClient.deleteWorkloadIdentityPoolProvider(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteWorkloadIdentityPoolProvider();
    
    

### checkUndeleteWorkloadIdentityPoolProgress(name)
    
    
    checkUndeleteWorkloadIdentityPoolProgress(name: string): Promise<LROperation<protos.google.iam.v1beta.WorkloadIdentityPool, protos.google.iam.v1beta.WorkloadIdentityPoolOperationMetadata>>;

Check the status of the long running operation returned by `undeleteWorkloadIdentityPool()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.iam.v1beta.WorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.workloadidentitypool-class), [protos.google.iam.v1beta.WorkloadIdentityPoolOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.workloadidentitypooloperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the pool to undelete.
       */
      // const name = 'abc123'
    
      // Imports the Iam library
      const {WorkloadIdentityPoolsClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const iamClient = new [WorkloadIdentityPoolsClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)();
    
      async function callUndeleteWorkloadIdentityPool() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await iamClient.undeleteWorkloadIdentityPool(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUndeleteWorkloadIdentityPool();
    
    

### checkUndeleteWorkloadIdentityPoolProviderProgress(name)
    
    
    checkUndeleteWorkloadIdentityPoolProviderProgress(name: string): Promise<LROperation<protos.google.iam.v1beta.WorkloadIdentityPoolProvider, protos.google.iam.v1beta.WorkloadIdentityPoolProviderOperationMetadata>>;

Check the status of the long running operation returned by `undeleteWorkloadIdentityPoolProvider()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.iam.v1beta.WorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.workloadidentitypoolprovider-class), [protos.google.iam.v1beta.WorkloadIdentityPoolProviderOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.workloadidentitypoolprovideroperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the provider to undelete.
       */
      // const name = 'abc123'
    
      // Imports the Iam library
      const {WorkloadIdentityPoolsClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const iamClient = new [WorkloadIdentityPoolsClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)();
    
      async function callUndeleteWorkloadIdentityPoolProvider() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await iamClient.undeleteWorkloadIdentityPoolProvider(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUndeleteWorkloadIdentityPoolProvider();
    
    

### checkUpdateWorkloadIdentityPoolProgress(name)
    
    
    checkUpdateWorkloadIdentityPoolProgress(name: string): Promise<LROperation<protos.google.iam.v1beta.WorkloadIdentityPool, protos.google.iam.v1beta.WorkloadIdentityPoolOperationMetadata>>;

Check the status of the long running operation returned by `updateWorkloadIdentityPool()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.iam.v1beta.WorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.workloadidentitypool-class), [protos.google.iam.v1beta.WorkloadIdentityPoolOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.workloadidentitypooloperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The pool to update. The `name` field is used to identify the pool.
       */
      // const workloadIdentityPool = {}
      /**
       *  Required. The list of fields update.
       */
      // const updateMask = {}
    
      // Imports the Iam library
      const {WorkloadIdentityPoolsClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const iamClient = new [WorkloadIdentityPoolsClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)();
    
      async function callUpdateWorkloadIdentityPool() {
        // Construct request
        const request = {
          workloadIdentityPool,
          updateMask,
        };
    
        // Run request
        const [operation] = await iamClient.updateWorkloadIdentityPool(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateWorkloadIdentityPool();
    
    

### checkUpdateWorkloadIdentityPoolProviderProgress(name)
    
    
    checkUpdateWorkloadIdentityPoolProviderProgress(name: string): Promise<LROperation<protos.google.iam.v1beta.WorkloadIdentityPoolProvider, protos.google.iam.v1beta.WorkloadIdentityPoolProviderOperationMetadata>>;

Check the status of the long running operation returned by `updateWorkloadIdentityPoolProvider()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.iam.v1beta.WorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.workloadidentitypoolprovider-class), [protos.google.iam.v1beta.WorkloadIdentityPoolProviderOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.workloadidentitypoolprovideroperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The provider to update.
       */
      // const workloadIdentityPoolProvider = {}
      /**
       *  Required. The list of fields to update.
       */
      // const updateMask = {}
    
      // Imports the Iam library
      const {WorkloadIdentityPoolsClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const iamClient = new [WorkloadIdentityPoolsClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)();
    
      async function callUpdateWorkloadIdentityPoolProvider() {
        // Construct request
        const request = {
          workloadIdentityPoolProvider,
          updateMask,
        };
    
        // Run request
        const [operation] = await iamClient.updateWorkloadIdentityPoolProvider(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateWorkloadIdentityPoolProvider();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### createWorkloadIdentityPool(request, options)
    
    
    createWorkloadIdentityPool(request?: protos.google.iam.v1beta.ICreateWorkloadIdentityPoolRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.iam.v1beta.IWorkloadIdentityPool, protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new .

You cannot reuse the name of a deleted pool until 30 days after deletion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkloadIdentityPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.icreateworkloadidentitypoolrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypool), [protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypooloperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource to create the pool in. The only supported
       *  location is `global`.
       */
      // const parent = 'abc123'
      /**
       *  Required. The pool to create.
       */
      // const workloadIdentityPool = {}
      /**
       *  Required. The ID to use for the pool, which becomes the
       *  final component of the resource name. This value should be 4-32 characters,
       *  and may contain the characters a-z0-9-. The prefix `gcp-` is
       *  reserved for use by Google, and may not be specified.
       */
      // const workloadIdentityPoolId = 'abc123'
    
      // Imports the Iam library
      const {WorkloadIdentityPoolsClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const iamClient = new [WorkloadIdentityPoolsClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)();
    
      async function callCreateWorkloadIdentityPool() {
        // Construct request
        const request = {
          parent,
          workloadIdentityPool,
          workloadIdentityPoolId,
        };
    
        // Run request
        const [operation] = await iamClient.createWorkloadIdentityPool(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateWorkloadIdentityPool();
    
    

### createWorkloadIdentityPool(request, options, callback)
    
    
    createWorkloadIdentityPool(request: protos.google.iam.v1beta.ICreateWorkloadIdentityPoolRequest, options: CallOptions, callback: Callback<LROperation<protos.google.iam.v1beta.IWorkloadIdentityPool, protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkloadIdentityPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.icreateworkloadidentitypoolrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypool), [protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypooloperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createWorkloadIdentityPool(request, callback)
    
    
    createWorkloadIdentityPool(request: protos.google.iam.v1beta.ICreateWorkloadIdentityPoolRequest, callback: Callback<LROperation<protos.google.iam.v1beta.IWorkloadIdentityPool, protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkloadIdentityPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.icreateworkloadidentitypoolrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypool), [protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypooloperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createWorkloadIdentityPoolProvider(request, options)
    
    
    createWorkloadIdentityPoolProvider(request?: protos.google.iam.v1beta.ICreateWorkloadIdentityPoolProviderRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.iam.v1beta.IWorkloadIdentityPoolProvider, protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new in a .

You cannot reuse the name of a deleted provider until 30 days after deletion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkloadIdentityPoolProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.icreateworkloadidentitypoolproviderrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovider), [protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovideroperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The pool to create this provider in.
       */
      // const parent = 'abc123'
      /**
       *  Required. The provider to create.
       */
      // const workloadIdentityPoolProvider = {}
      /**
       *  Required. The ID for the provider, which becomes the
       *  final component of the resource name. This value must be 4-32 characters,
       *  and may contain the characters a-z0-9-. The prefix `gcp-` is
       *  reserved for use by Google, and may not be specified.
       */
      // const workloadIdentityPoolProviderId = 'abc123'
    
      // Imports the Iam library
      const {WorkloadIdentityPoolsClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const iamClient = new [WorkloadIdentityPoolsClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)();
    
      async function callCreateWorkloadIdentityPoolProvider() {
        // Construct request
        const request = {
          parent,
          workloadIdentityPoolProvider,
          workloadIdentityPoolProviderId,
        };
    
        // Run request
        const [operation] = await iamClient.createWorkloadIdentityPoolProvider(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateWorkloadIdentityPoolProvider();
    
    

### createWorkloadIdentityPoolProvider(request, options, callback)
    
    
    createWorkloadIdentityPoolProvider(request: protos.google.iam.v1beta.ICreateWorkloadIdentityPoolProviderRequest, options: CallOptions, callback: Callback<LROperation<protos.google.iam.v1beta.IWorkloadIdentityPoolProvider, protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkloadIdentityPoolProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.icreateworkloadidentitypoolproviderrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovider), [protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovideroperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createWorkloadIdentityPoolProvider(request, callback)
    
    
    createWorkloadIdentityPoolProvider(request: protos.google.iam.v1beta.ICreateWorkloadIdentityPoolProviderRequest, callback: Callback<LROperation<protos.google.iam.v1beta.IWorkloadIdentityPoolProvider, protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkloadIdentityPoolProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.icreateworkloadidentitypoolproviderrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovider), [protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovideroperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteWorkloadIdentityPool(request, options)
    
    
    deleteWorkloadIdentityPool(request?: protos.google.iam.v1beta.IDeleteWorkloadIdentityPoolRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.iam.v1beta.IWorkloadIdentityPool, protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a .

You cannot use a deleted pool to exchange external credentials for Google Cloud credentials. However, deletion does not revoke credentials that have already been issued. Credentials issued for a deleted pool do not grant access to resources. If the pool is undeleted, and the credentials are not expired, they grant access again. You can undelete a pool for 30 days. After 30 days, deletion is permanent. You cannot update deleted pools. However, you can view and list them.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkloadIdentityPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ideleteworkloadidentitypoolrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypool), [protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypooloperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the pool to delete.
       */
      // const name = 'abc123'
    
      // Imports the Iam library
      const {WorkloadIdentityPoolsClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const iamClient = new [WorkloadIdentityPoolsClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)();
    
      async function callDeleteWorkloadIdentityPool() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await iamClient.deleteWorkloadIdentityPool(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteWorkloadIdentityPool();
    
    

### deleteWorkloadIdentityPool(request, options, callback)
    
    
    deleteWorkloadIdentityPool(request: protos.google.iam.v1beta.IDeleteWorkloadIdentityPoolRequest, options: CallOptions, callback: Callback<LROperation<protos.google.iam.v1beta.IWorkloadIdentityPool, protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkloadIdentityPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ideleteworkloadidentitypoolrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypool), [protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypooloperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteWorkloadIdentityPool(request, callback)
    
    
    deleteWorkloadIdentityPool(request: protos.google.iam.v1beta.IDeleteWorkloadIdentityPoolRequest, callback: Callback<LROperation<protos.google.iam.v1beta.IWorkloadIdentityPool, protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkloadIdentityPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ideleteworkloadidentitypoolrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypool), [protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypooloperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteWorkloadIdentityPoolProvider(request, options)
    
    
    deleteWorkloadIdentityPoolProvider(request?: protos.google.iam.v1beta.IDeleteWorkloadIdentityPoolProviderRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.iam.v1beta.IWorkloadIdentityPoolProvider, protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a . Deleting a provider does not revoke credentials that have already been issued; they continue to grant access. You can undelete a provider for 30 days. After 30 days, deletion is permanent. You cannot update deleted providers. However, you can view and list them.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkloadIdentityPoolProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ideleteworkloadidentitypoolproviderrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovider), [protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovideroperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the provider to delete.
       */
      // const name = 'abc123'
    
      // Imports the Iam library
      const {WorkloadIdentityPoolsClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const iamClient = new [WorkloadIdentityPoolsClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)();
    
      async function callDeleteWorkloadIdentityPoolProvider() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await iamClient.deleteWorkloadIdentityPoolProvider(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteWorkloadIdentityPoolProvider();
    
    

### deleteWorkloadIdentityPoolProvider(request, options, callback)
    
    
    deleteWorkloadIdentityPoolProvider(request: protos.google.iam.v1beta.IDeleteWorkloadIdentityPoolProviderRequest, options: CallOptions, callback: Callback<LROperation<protos.google.iam.v1beta.IWorkloadIdentityPoolProvider, protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkloadIdentityPoolProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ideleteworkloadidentitypoolproviderrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovider), [protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovideroperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteWorkloadIdentityPoolProvider(request, callback)
    
    
    deleteWorkloadIdentityPoolProvider(request: protos.google.iam.v1beta.IDeleteWorkloadIdentityPoolProviderRequest, callback: Callback<LROperation<protos.google.iam.v1beta.IWorkloadIdentityPoolProvider, protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkloadIdentityPoolProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ideleteworkloadidentitypoolproviderrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovider), [protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovideroperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
  
### getWorkloadIdentityPool(request, options)
    
    
    getWorkloadIdentityPool(request?: protos.google.iam.v1beta.IGetWorkloadIdentityPoolRequest, options?: CallOptions): Promise<[
            protos.google.iam.v1beta.IWorkloadIdentityPool,
            protos.google.iam.v1beta.IGetWorkloadIdentityPoolRequest | undefined,
            {} | undefined
        ]>;

Gets an individual .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkloadIdentityPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.igetworkloadidentitypoolrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.iam.v1beta.IWorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypool), [protos.google.iam.v1beta.IGetWorkloadIdentityPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.igetworkloadidentitypoolrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the pool to retrieve.
       */
      // const name = 'abc123'
    
      // Imports the Iam library
      const {WorkloadIdentityPoolsClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const iamClient = new [WorkloadIdentityPoolsClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)();
    
      async function callGetWorkloadIdentityPool() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await iamClient.getWorkloadIdentityPool(request);
        console.log(response);
      }
    
      callGetWorkloadIdentityPool();
    
    

### getWorkloadIdentityPool(request, options, callback)
    
    
    getWorkloadIdentityPool(request: protos.google.iam.v1beta.IGetWorkloadIdentityPoolRequest, options: CallOptions, callback: Callback<protos.google.iam.v1beta.IWorkloadIdentityPool, protos.google.iam.v1beta.IGetWorkloadIdentityPoolRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkloadIdentityPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.igetworkloadidentitypoolrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.iam.v1beta.IWorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypool), [protos.google.iam.v1beta.IGetWorkloadIdentityPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.igetworkloadidentitypoolrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getWorkloadIdentityPool(request, callback)
    
    
    getWorkloadIdentityPool(request: protos.google.iam.v1beta.IGetWorkloadIdentityPoolRequest, callback: Callback<protos.google.iam.v1beta.IWorkloadIdentityPool, protos.google.iam.v1beta.IGetWorkloadIdentityPoolRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkloadIdentityPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.igetworkloadidentitypoolrequest)`   
  
`callback` |  `Callback<[protos.google.iam.v1beta.IWorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypool), [protos.google.iam.v1beta.IGetWorkloadIdentityPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.igetworkloadidentitypoolrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getWorkloadIdentityPoolProvider(request, options)
    
    
    getWorkloadIdentityPoolProvider(request?: protos.google.iam.v1beta.IGetWorkloadIdentityPoolProviderRequest, options?: CallOptions): Promise<[
            protos.google.iam.v1beta.IWorkloadIdentityPoolProvider,
            (protos.google.iam.v1beta.IGetWorkloadIdentityPoolProviderRequest | undefined),
            {} | undefined
        ]>;

Gets an individual .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkloadIdentityPoolProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.igetworkloadidentitypoolproviderrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.iam.v1beta.IWorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovider), ([protos.google.iam.v1beta.IGetWorkloadIdentityPoolProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.igetworkloadidentitypoolproviderrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the provider to retrieve.
       */
      // const name = 'abc123'
    
      // Imports the Iam library
      const {WorkloadIdentityPoolsClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const iamClient = new [WorkloadIdentityPoolsClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)();
    
      async function callGetWorkloadIdentityPoolProvider() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await iamClient.getWorkloadIdentityPoolProvider(request);
        console.log(response);
      }
    
      callGetWorkloadIdentityPoolProvider();
    
    

### getWorkloadIdentityPoolProvider(request, options, callback)
    
    
    getWorkloadIdentityPoolProvider(request: protos.google.iam.v1beta.IGetWorkloadIdentityPoolProviderRequest, options: CallOptions, callback: Callback<protos.google.iam.v1beta.IWorkloadIdentityPoolProvider, protos.google.iam.v1beta.IGetWorkloadIdentityPoolProviderRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkloadIdentityPoolProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.igetworkloadidentitypoolproviderrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.iam.v1beta.IWorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovider), [protos.google.iam.v1beta.IGetWorkloadIdentityPoolProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.igetworkloadidentitypoolproviderrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getWorkloadIdentityPoolProvider(request, callback)
    
    
    getWorkloadIdentityPoolProvider(request: protos.google.iam.v1beta.IGetWorkloadIdentityPoolProviderRequest, callback: Callback<protos.google.iam.v1beta.IWorkloadIdentityPoolProvider, protos.google.iam.v1beta.IGetWorkloadIdentityPoolProviderRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkloadIdentityPoolProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.igetworkloadidentitypoolproviderrequest)`   
  
`callback` |  `Callback<[protos.google.iam.v1beta.IWorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovider), [protos.google.iam.v1beta.IGetWorkloadIdentityPoolProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.igetworkloadidentitypoolproviderrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listWorkloadIdentityPoolProviders(request, options)
    
    
    listWorkloadIdentityPoolProviders(request?: protos.google.iam.v1beta.IListWorkloadIdentityPoolProvidersRequest, options?: CallOptions): Promise<[
            protos.google.iam.v1beta.IWorkloadIdentityPoolProvider[],
            protos.google.iam.v1beta.IListWorkloadIdentityPoolProvidersRequest | null,
            protos.google.iam.v1beta.IListWorkloadIdentityPoolProvidersResponse
        ]>;

Lists all non-deleted s in a . If `show_deleted` is set to `true`, then deleted providers are also listed.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkloadIdentityPoolProvidersRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolprovidersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.iam.v1beta.IWorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovider)[], [protos.google.iam.v1beta.IListWorkloadIdentityPoolProvidersRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolprovidersrequest) | null, [protos.google.iam.v1beta.IListWorkloadIdentityPoolProvidersResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolprovidersresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listWorkloadIdentityPoolProvidersAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listWorkloadIdentityPoolProviders(request, options, callback)
    
    
    listWorkloadIdentityPoolProviders(request: protos.google.iam.v1beta.IListWorkloadIdentityPoolProvidersRequest, options: CallOptions, callback: PaginationCallback<protos.google.iam.v1beta.IListWorkloadIdentityPoolProvidersRequest, protos.google.iam.v1beta.IListWorkloadIdentityPoolProvidersResponse | null | undefined, protos.google.iam.v1beta.IWorkloadIdentityPoolProvider>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkloadIdentityPoolProvidersRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolprovidersrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.iam.v1beta.IListWorkloadIdentityPoolProvidersRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolprovidersrequest), [protos.google.iam.v1beta.IListWorkloadIdentityPoolProvidersResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolprovidersresponse) | null | undefined, [protos.google.iam.v1beta.IWorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovider)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listWorkloadIdentityPoolProviders(request, callback)
    
    
    listWorkloadIdentityPoolProviders(request: protos.google.iam.v1beta.IListWorkloadIdentityPoolProvidersRequest, callback: PaginationCallback<protos.google.iam.v1beta.IListWorkloadIdentityPoolProvidersRequest, protos.google.iam.v1beta.IListWorkloadIdentityPoolProvidersResponse | null | undefined, protos.google.iam.v1beta.IWorkloadIdentityPoolProvider>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkloadIdentityPoolProvidersRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolprovidersrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.iam.v1beta.IListWorkloadIdentityPoolProvidersRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolprovidersrequest), [protos.google.iam.v1beta.IListWorkloadIdentityPoolProvidersResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolprovidersresponse) | null | undefined, [protos.google.iam.v1beta.IWorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovider)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listWorkloadIdentityPoolProvidersAsync(request, options)
    
    
    listWorkloadIdentityPoolProvidersAsync(request?: protos.google.iam.v1beta.IListWorkloadIdentityPoolProvidersRequest, options?: CallOptions): AsyncIterable<protos.google.iam.v1beta.IWorkloadIdentityPoolProvider>;

Equivalent to `listWorkloadIdentityPoolProviders`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkloadIdentityPoolProvidersRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolprovidersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.iam.v1beta.IWorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovider)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The pool to list providers for.
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of providers to return.
       *  If unspecified, at most 50 providers are returned.
       *  The maximum value is 100; values above 100 are truncated to 100.
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous
       *  `ListWorkloadIdentityPoolProviders` call. Provide this to retrieve the
       *  subsequent page.
       */
      // const pageToken = 'abc123'
      /**
       *  Whether to return soft-deleted providers.
       */
      // const showDeleted = true
    
      // Imports the Iam library
      const {WorkloadIdentityPoolsClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const iamClient = new [WorkloadIdentityPoolsClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)();
    
      async function callListWorkloadIdentityPoolProviders() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = iamClient.[listWorkloadIdentityPoolProvidersAsync](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListWorkloadIdentityPoolProviders();
    
    

### listWorkloadIdentityPoolProvidersStream(request, options)
    
    
    listWorkloadIdentityPoolProvidersStream(request?: protos.google.iam.v1beta.IListWorkloadIdentityPoolProvidersRequest, options?: CallOptions): Transform;

Equivalent to `listWorkloadIdentityPoolProviders`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkloadIdentityPoolProvidersRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolprovidersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listWorkloadIdentityPoolProvidersAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listWorkloadIdentityPools(request, options)
    
    
    listWorkloadIdentityPools(request?: protos.google.iam.v1beta.IListWorkloadIdentityPoolsRequest, options?: CallOptions): Promise<[
            protos.google.iam.v1beta.IWorkloadIdentityPool[],
            protos.google.iam.v1beta.IListWorkloadIdentityPoolsRequest | null,
            protos.google.iam.v1beta.IListWorkloadIdentityPoolsResponse
        ]>;

Lists all non-deleted s in a project. If `show_deleted` is set to `true`, then deleted pools are also listed.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkloadIdentityPoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.iam.v1beta.IWorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypool)[], [protos.google.iam.v1beta.IListWorkloadIdentityPoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolsrequest) | null, [protos.google.iam.v1beta.IListWorkloadIdentityPoolsResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listWorkloadIdentityPoolsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listWorkloadIdentityPools(request, options, callback)
    
    
    listWorkloadIdentityPools(request: protos.google.iam.v1beta.IListWorkloadIdentityPoolsRequest, options: CallOptions, callback: PaginationCallback<protos.google.iam.v1beta.IListWorkloadIdentityPoolsRequest, protos.google.iam.v1beta.IListWorkloadIdentityPoolsResponse | null | undefined, protos.google.iam.v1beta.IWorkloadIdentityPool>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkloadIdentityPoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.iam.v1beta.IListWorkloadIdentityPoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolsrequest), [protos.google.iam.v1beta.IListWorkloadIdentityPoolsResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolsresponse) | null | undefined, [protos.google.iam.v1beta.IWorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypool)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listWorkloadIdentityPools(request, callback)
    
    
    listWorkloadIdentityPools(request: protos.google.iam.v1beta.IListWorkloadIdentityPoolsRequest, callback: PaginationCallback<protos.google.iam.v1beta.IListWorkloadIdentityPoolsRequest, protos.google.iam.v1beta.IListWorkloadIdentityPoolsResponse | null | undefined, protos.google.iam.v1beta.IWorkloadIdentityPool>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkloadIdentityPoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.iam.v1beta.IListWorkloadIdentityPoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolsrequest), [protos.google.iam.v1beta.IListWorkloadIdentityPoolsResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolsresponse) | null | undefined, [protos.google.iam.v1beta.IWorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypool)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listWorkloadIdentityPoolsAsync(request, options)
    
    
    listWorkloadIdentityPoolsAsync(request?: protos.google.iam.v1beta.IListWorkloadIdentityPoolsRequest, options?: CallOptions): AsyncIterable<protos.google.iam.v1beta.IWorkloadIdentityPool>;

Equivalent to `listWorkloadIdentityPools`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkloadIdentityPoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.iam.v1beta.IWorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypool)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource to list pools for.
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of pools to return.
       *  If unspecified, at most 50 pools are returned.
       *  The maximum value is 1000; values above are 1000 truncated to 1000.
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous `ListWorkloadIdentityPools`
       *  call. Provide this to retrieve the subsequent page.
       */
      // const pageToken = 'abc123'
      /**
       *  Whether to return soft-deleted pools.
       */
      // const showDeleted = true
    
      // Imports the Iam library
      const {WorkloadIdentityPoolsClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const iamClient = new [WorkloadIdentityPoolsClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)();
    
      async function callListWorkloadIdentityPools() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = iamClient.[listWorkloadIdentityPoolsAsync](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListWorkloadIdentityPools();
    
    

### listWorkloadIdentityPoolsStream(request, options)
    
    
    listWorkloadIdentityPoolsStream(request?: protos.google.iam.v1beta.IListWorkloadIdentityPoolsRequest, options?: CallOptions): Transform;

Equivalent to `listWorkloadIdentityPools`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkloadIdentityPoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.ilistworkloadidentitypoolsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listWorkloadIdentityPoolsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### matchLocationFromWorkloadIdentityPoolName(workloadIdentityPoolName)
    
    
    matchLocationFromWorkloadIdentityPoolName(workloadIdentityPoolName: string): string | number;

Parse the location from WorkloadIdentityPool resource.

**Parameter**  
---  
**Name** | **Description**  
`workloadIdentityPoolName` |  `string`   
A fully-qualified path representing WorkloadIdentityPool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromWorkloadIdentityPoolProviderName(workloadIdentityPoolProviderName)
    
    
    matchLocationFromWorkloadIdentityPoolProviderName(workloadIdentityPoolProviderName: string): string | number;

Parse the location from WorkloadIdentityPoolProvider resource.

**Parameter**  
---  
**Name** | **Description**  
`workloadIdentityPoolProviderName` |  `string`   
A fully-qualified path representing WorkloadIdentityPoolProvider resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
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
  
### matchProjectFromWorkloadIdentityPoolName(workloadIdentityPoolName)
    
    
    matchProjectFromWorkloadIdentityPoolName(workloadIdentityPoolName: string): string | number;

Parse the project from WorkloadIdentityPool resource.

**Parameter**  
---  
**Name** | **Description**  
`workloadIdentityPoolName` |  `string`   
A fully-qualified path representing WorkloadIdentityPool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromWorkloadIdentityPoolProviderName(workloadIdentityPoolProviderName)
    
    
    matchProjectFromWorkloadIdentityPoolProviderName(workloadIdentityPoolProviderName: string): string | number;

Parse the project from WorkloadIdentityPoolProvider resource.

**Parameter**  
---  
**Name** | **Description**  
`workloadIdentityPoolProviderName` |  `string`   
A fully-qualified path representing WorkloadIdentityPoolProvider resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchWorkloadIdentityPoolFromWorkloadIdentityPoolName(workloadIdentityPoolName)
    
    
    matchWorkloadIdentityPoolFromWorkloadIdentityPoolName(workloadIdentityPoolName: string): string | number;

Parse the workload_identity_pool from WorkloadIdentityPool resource.

**Parameter**  
---  
**Name** | **Description**  
`workloadIdentityPoolName` |  `string`   
A fully-qualified path representing WorkloadIdentityPool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the workload_identity_pool.  
  
### matchWorkloadIdentityPoolFromWorkloadIdentityPoolProviderName(workloadIdentityPoolProviderName)
    
    
    matchWorkloadIdentityPoolFromWorkloadIdentityPoolProviderName(workloadIdentityPoolProviderName: string): string | number;

Parse the workload_identity_pool from WorkloadIdentityPoolProvider resource.

**Parameter**  
---  
**Name** | **Description**  
`workloadIdentityPoolProviderName` |  `string`   
A fully-qualified path representing WorkloadIdentityPoolProvider resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the workload_identity_pool.  
  
### matchWorkloadIdentityPoolProviderFromWorkloadIdentityPoolProviderName(workloadIdentityPoolProviderName)
    
    
    matchWorkloadIdentityPoolProviderFromWorkloadIdentityPoolProviderName(workloadIdentityPoolProviderName: string): string | number;

Parse the workload_identity_pool_provider from WorkloadIdentityPoolProvider resource.

**Parameter**  
---  
**Name** | **Description**  
`workloadIdentityPoolProviderName` |  `string`   
A fully-qualified path representing WorkloadIdentityPoolProvider resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the workload_identity_pool_provider.  
  
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
  
### undeleteWorkloadIdentityPool(request, options)
    
    
    undeleteWorkloadIdentityPool(request?: protos.google.iam.v1beta.IUndeleteWorkloadIdentityPoolRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.iam.v1beta.IWorkloadIdentityPool, protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Undeletes a , as long as it was deleted fewer than 30 days ago.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUndeleteWorkloadIdentityPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iundeleteworkloadidentitypoolrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypool), [protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypooloperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the pool to undelete.
       */
      // const name = 'abc123'
    
      // Imports the Iam library
      const {WorkloadIdentityPoolsClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const iamClient = new [WorkloadIdentityPoolsClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)();
    
      async function callUndeleteWorkloadIdentityPool() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await iamClient.undeleteWorkloadIdentityPool(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUndeleteWorkloadIdentityPool();
    
    

### undeleteWorkloadIdentityPool(request, options, callback)
    
    
    undeleteWorkloadIdentityPool(request: protos.google.iam.v1beta.IUndeleteWorkloadIdentityPoolRequest, options: CallOptions, callback: Callback<LROperation<protos.google.iam.v1beta.IWorkloadIdentityPool, protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUndeleteWorkloadIdentityPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iundeleteworkloadidentitypoolrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypool), [protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypooloperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### undeleteWorkloadIdentityPool(request, callback)
    
    
    undeleteWorkloadIdentityPool(request: protos.google.iam.v1beta.IUndeleteWorkloadIdentityPoolRequest, callback: Callback<LROperation<protos.google.iam.v1beta.IWorkloadIdentityPool, protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUndeleteWorkloadIdentityPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iundeleteworkloadidentitypoolrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypool), [protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypooloperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### undeleteWorkloadIdentityPoolProvider(request, options)
    
    
    undeleteWorkloadIdentityPoolProvider(request?: protos.google.iam.v1beta.IUndeleteWorkloadIdentityPoolProviderRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.iam.v1beta.IWorkloadIdentityPoolProvider, protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Undeletes a , as long as it was deleted fewer than 30 days ago.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUndeleteWorkloadIdentityPoolProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iundeleteworkloadidentitypoolproviderrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovider), [protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovideroperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the provider to undelete.
       */
      // const name = 'abc123'
    
      // Imports the Iam library
      const {WorkloadIdentityPoolsClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const iamClient = new [WorkloadIdentityPoolsClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)();
    
      async function callUndeleteWorkloadIdentityPoolProvider() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await iamClient.undeleteWorkloadIdentityPoolProvider(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUndeleteWorkloadIdentityPoolProvider();
    
    

### undeleteWorkloadIdentityPoolProvider(request, options, callback)
    
    
    undeleteWorkloadIdentityPoolProvider(request: protos.google.iam.v1beta.IUndeleteWorkloadIdentityPoolProviderRequest, options: CallOptions, callback: Callback<LROperation<protos.google.iam.v1beta.IWorkloadIdentityPoolProvider, protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUndeleteWorkloadIdentityPoolProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iundeleteworkloadidentitypoolproviderrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovider), [protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovideroperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### undeleteWorkloadIdentityPoolProvider(request, callback)
    
    
    undeleteWorkloadIdentityPoolProvider(request: protos.google.iam.v1beta.IUndeleteWorkloadIdentityPoolProviderRequest, callback: Callback<LROperation<protos.google.iam.v1beta.IWorkloadIdentityPoolProvider, protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUndeleteWorkloadIdentityPoolProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iundeleteworkloadidentitypoolproviderrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovider), [protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovideroperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateWorkloadIdentityPool(request, options)
    
    
    updateWorkloadIdentityPool(request?: protos.google.iam.v1beta.IUpdateWorkloadIdentityPoolRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.iam.v1beta.IWorkloadIdentityPool, protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates an existing .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateWorkloadIdentityPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iupdateworkloadidentitypoolrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypool), [protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypooloperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The pool to update. The `name` field is used to identify the pool.
       */
      // const workloadIdentityPool = {}
      /**
       *  Required. The list of fields update.
       */
      // const updateMask = {}
    
      // Imports the Iam library
      const {WorkloadIdentityPoolsClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const iamClient = new [WorkloadIdentityPoolsClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)();
    
      async function callUpdateWorkloadIdentityPool() {
        // Construct request
        const request = {
          workloadIdentityPool,
          updateMask,
        };
    
        // Run request
        const [operation] = await iamClient.updateWorkloadIdentityPool(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateWorkloadIdentityPool();
    
    

### updateWorkloadIdentityPool(request, options, callback)
    
    
    updateWorkloadIdentityPool(request: protos.google.iam.v1beta.IUpdateWorkloadIdentityPoolRequest, options: CallOptions, callback: Callback<LROperation<protos.google.iam.v1beta.IWorkloadIdentityPool, protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateWorkloadIdentityPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iupdateworkloadidentitypoolrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypool), [protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypooloperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateWorkloadIdentityPool(request, callback)
    
    
    updateWorkloadIdentityPool(request: protos.google.iam.v1beta.IUpdateWorkloadIdentityPoolRequest, callback: Callback<LROperation<protos.google.iam.v1beta.IWorkloadIdentityPool, protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateWorkloadIdentityPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iupdateworkloadidentitypoolrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPool](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypool), [protos.google.iam.v1beta.IWorkloadIdentityPoolOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypooloperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateWorkloadIdentityPoolProvider(request, options)
    
    
    updateWorkloadIdentityPoolProvider(request?: protos.google.iam.v1beta.IUpdateWorkloadIdentityPoolProviderRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.iam.v1beta.IWorkloadIdentityPoolProvider, protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates an existing .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateWorkloadIdentityPoolProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iupdateworkloadidentitypoolproviderrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovider), [protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovideroperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The provider to update.
       */
      // const workloadIdentityPoolProvider = {}
      /**
       *  Required. The list of fields to update.
       */
      // const updateMask = {}
    
      // Imports the Iam library
      const {WorkloadIdentityPoolsClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const iamClient = new [WorkloadIdentityPoolsClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/v1beta.workloadidentitypoolsclient.html)();
    
      async function callUpdateWorkloadIdentityPoolProvider() {
        // Construct request
        const request = {
          workloadIdentityPoolProvider,
          updateMask,
        };
    
        // Run request
        const [operation] = await iamClient.updateWorkloadIdentityPoolProvider(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateWorkloadIdentityPoolProvider();
    
    

### updateWorkloadIdentityPoolProvider(request, options, callback)
    
    
    updateWorkloadIdentityPoolProvider(request: protos.google.iam.v1beta.IUpdateWorkloadIdentityPoolProviderRequest, options: CallOptions, callback: Callback<LROperation<protos.google.iam.v1beta.IWorkloadIdentityPoolProvider, protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateWorkloadIdentityPoolProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iupdateworkloadidentitypoolproviderrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovider), [protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovideroperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateWorkloadIdentityPoolProvider(request, callback)
    
    
    updateWorkloadIdentityPoolProvider(request: protos.google.iam.v1beta.IUpdateWorkloadIdentityPoolProviderRequest, callback: Callback<LROperation<protos.google.iam.v1beta.IWorkloadIdentityPoolProvider, protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateWorkloadIdentityPoolProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iupdateworkloadidentitypoolproviderrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.iam.v1beta.IWorkloadIdentityPoolProvider](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovider), [protos.google.iam.v1beta.IWorkloadIdentityPoolProviderOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v1beta.iworkloadidentitypoolprovideroperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### workloadIdentityPoolPath(project, location, workloadIdentityPool)
    
    
    workloadIdentityPoolPath(project: string, location: string, workloadIdentityPool: string): string;

Return a fully-qualified workloadIdentityPool resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`workloadIdentityPool` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### workloadIdentityPoolProviderPath(project, location, workloadIdentityPool, workloadIdentityPoolProvider)
    
    
    workloadIdentityPoolProviderPath(project: string, location: string, workloadIdentityPool: string, workloadIdentityPoolProvider: string): string;

Return a fully-qualified workloadIdentityPoolProvider resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`workloadIdentityPool` |  `string`   
  
`workloadIdentityPoolProvider` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
