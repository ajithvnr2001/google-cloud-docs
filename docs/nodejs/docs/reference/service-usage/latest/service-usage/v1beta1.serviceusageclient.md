---
url: https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/v1beta1.serviceusageclient
title: Class v1beta1.ServiceUsageClient (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:10.821595+00:00
---

# Class v1beta1.ServiceUsageClient (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/v1beta1.serviceusageclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.ServiceUsageClient (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  3.3.0  2.2.2  2.1.2  1.2.1  1.1.4 

[Service Usage API](<https://cloud.google.com/service-usage/docs/overview>) v1beta1

## Package

[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of ServiceUsageClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new ServiceUsageClient({fallback: true}, gax); ```  
  
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

### port
    
    
    static get port(): number;

The port for this API service.

### scopes
    
    
    static get scopes(): string[];

The scopes needed to make gRPC calls for every method defined in this service.

### servicePath
    
    
    static get servicePath(): string;

The DNS address for this API service.

### serviceUsageStub
    
    
    serviceUsageStub?: Promise<{
            [name: string]: Function;
        }>;

### universeDomain
    
    
    get universeDomain(): string;

### warn
    
    
    warn: (code: string, message: string, warnType?: string) => void;

## Methods 

### batchEnableServices(request, options)
    
    
    batchEnableServices(request?: protos.google.api.serviceusage.v1beta1.IBatchEnableServicesRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.api.serviceusage.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Enables multiple services on a project. The operation is atomic: if enabling any service fails, then the entire batch fails, and no state changes occur.

Operation response type: `google.protobuf.Empty`

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchEnableServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ibatchenableservicesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.iempty), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Parent to enable services on.
       *  An example name would be:
       *  `projects/123`
       *  where `123` is the project number (not project ID).
       *  The `BatchEnableServices` method currently only supports projects.
       */
      // const parent = 'abc123'
      /**
       *  The identifiers of the services to enable on the project.
       *  A valid identifier would be:
       *  serviceusage.googleapis.com
       *  Enabling services requires that each service is public or is shared with
       *  the user enabling the service.
       *  Two or more services must be specified. To enable a single service,
       *  use the `EnableService` method instead.
       *  A single request can enable a maximum of 20 services at a time. If more
       *  than 20 services are specified, the request will fail, and no state changes
       *  will occur.
       */
      // const serviceIds = ['abc','def']
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callBatchEnableServices() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.batchEnableServices(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callBatchEnableServices();
    
    

### batchEnableServices(request, options, callback)
    
    
    batchEnableServices(request: protos.google.api.serviceusage.v1beta1.IBatchEnableServicesRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.api.serviceusage.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchEnableServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ibatchenableservicesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.iempty), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchEnableServices(request, callback)
    
    
    batchEnableServices(request: protos.google.api.serviceusage.v1beta1.IBatchEnableServicesRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.api.serviceusage.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchEnableServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ibatchenableservicesrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.iempty), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelOperation(request, optionsOrCallback, callback)
    
    
    cancelOperation(request: protos.google.longrunning.CancelOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>, callback?: Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>): Promise<protos.google.protobuf.Empty>;

Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an value with a of 1, corresponding to `Code.CANCELLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### checkBatchEnableServicesProgress(name)
    
    
    checkBatchEnableServicesProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.api.serviceusage.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `batchEnableServices()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.empty), [protos.google.api.serviceusage.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Parent to enable services on.
       *  An example name would be:
       *  `projects/123`
       *  where `123` is the project number (not project ID).
       *  The `BatchEnableServices` method currently only supports projects.
       */
      // const parent = 'abc123'
      /**
       *  The identifiers of the services to enable on the project.
       *  A valid identifier would be:
       *  serviceusage.googleapis.com
       *  Enabling services requires that each service is public or is shared with
       *  the user enabling the service.
       *  Two or more services must be specified. To enable a single service,
       *  use the `EnableService` method instead.
       *  A single request can enable a maximum of 20 services at a time. If more
       *  than 20 services are specified, the request will fail, and no state changes
       *  will occur.
       */
      // const serviceIds = ['abc','def']
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callBatchEnableServices() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.batchEnableServices(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callBatchEnableServices();
    
    

### checkCreateAdminOverrideProgress(name)
    
    
    checkCreateAdminOverrideProgress(name: string): Promise<LROperation<protos.google.api.serviceusage.v1beta1.QuotaOverride, protos.google.api.serviceusage.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `createAdminOverride()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.api.serviceusage.v1beta1.QuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.quotaoverride), [protos.google.api.serviceusage.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource name of the parent quota limit, returned by a
       *  ListConsumerQuotaMetrics or GetConsumerQuotaMetric call.
       *  An example name would be:
       *  `projects/123/services/compute.googleapis.com/consumerQuotaMetrics/compute.googleapis.com%2Fcpus/limits/%2Fproject%2Fregion`
       */
      // const parent = 'abc123'
      /**
       *  The admin override to create.
       */
      // const override = {}
      /**
       *  Whether to force the creation of the quota override.
       *  Setting the force parameter to 'true' ignores all quota safety checks that
       *  would fail the request. QuotaSafetyCheck lists all such validations.
       */
      // const force = true
      /**
       *  The list of quota safety checks to ignore before the override mutation.
       *  Unlike 'force' field that ignores all the quota safety checks, the
       *  'force_only' field ignores only the specified checks; other checks are
       *  still enforced. The 'force' and 'force_only' fields cannot both be set.
       */
      // const forceOnly = [1,2,3,4]
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callCreateAdminOverride() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.createAdminOverride(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateAdminOverride();
    
    

### checkCreateConsumerOverrideProgress(name)
    
    
    checkCreateConsumerOverrideProgress(name: string): Promise<LROperation<protos.google.api.serviceusage.v1beta1.QuotaOverride, protos.google.api.serviceusage.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `createConsumerOverride()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.api.serviceusage.v1beta1.QuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.quotaoverride), [protos.google.api.serviceusage.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource name of the parent quota limit, returned by a
       *  ListConsumerQuotaMetrics or GetConsumerQuotaMetric call.
       *  An example name would be:
       *  `projects/123/services/compute.googleapis.com/consumerQuotaMetrics/compute.googleapis.com%2Fcpus/limits/%2Fproject%2Fregion`
       */
      // const parent = 'abc123'
      /**
       *  The override to create.
       */
      // const override = {}
      /**
       *  Whether to force the creation of the quota override.
       *  Setting the force parameter to 'true' ignores all quota safety checks that
       *  would fail the request. QuotaSafetyCheck lists all such validations.
       */
      // const force = true
      /**
       *  The list of quota safety checks to ignore before the override mutation.
       *  Unlike 'force' field that ignores all the quota safety checks, the
       *  'force_only' field ignores only the specified checks; other checks are
       *  still enforced. The 'force' and 'force_only' fields cannot both be set.
       */
      // const forceOnly = [1,2,3,4]
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callCreateConsumerOverride() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.createConsumerOverride(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateConsumerOverride();
    
    

### checkDeleteAdminOverrideProgress(name)
    
    
    checkDeleteAdminOverrideProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.api.serviceusage.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `deleteAdminOverride()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.empty), [protos.google.api.serviceusage.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource name of the override to delete.
       *  An example name would be:
       *  `projects/123/services/compute.googleapis.com/consumerQuotaMetrics/compute.googleapis.com%2Fcpus/limits/%2Fproject%2Fregion/adminOverrides/4a3f2c1d`
       */
      // const name = 'abc123'
      /**
       *  Whether to force the deletion of the quota override.
       *  Setting the force parameter to 'true' ignores all quota safety checks that
       *  would fail the request. QuotaSafetyCheck lists all such validations.
       */
      // const force = true
      /**
       *  The list of quota safety checks to ignore before the override mutation.
       *  Unlike 'force' field that ignores all the quota safety checks, the
       *  'force_only' field ignores only the specified checks; other checks are
       *  still enforced. The 'force' and 'force_only' fields cannot both be set.
       */
      // const forceOnly = [1,2,3,4]
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callDeleteAdminOverride() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.deleteAdminOverride(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteAdminOverride();
    
    

### checkDeleteConsumerOverrideProgress(name)
    
    
    checkDeleteConsumerOverrideProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.api.serviceusage.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `deleteConsumerOverride()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.empty), [protos.google.api.serviceusage.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource name of the override to delete.
       *  An example name would be:
       *  `projects/123/services/compute.googleapis.com/consumerQuotaMetrics/compute.googleapis.com%2Fcpus/limits/%2Fproject%2Fregion/consumerOverrides/4a3f2c1d`
       */
      // const name = 'abc123'
      /**
       *  Whether to force the deletion of the quota override.
       *  Setting the force parameter to 'true' ignores all quota safety checks that
       *  would fail the request. QuotaSafetyCheck lists all such validations.
       */
      // const force = true
      /**
       *  The list of quota safety checks to ignore before the override mutation.
       *  Unlike 'force' field that ignores all the quota safety checks, the
       *  'force_only' field ignores only the specified checks; other checks are
       *  still enforced. The 'force' and 'force_only' fields cannot both be set.
       */
      // const forceOnly = [1,2,3,4]
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callDeleteConsumerOverride() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.deleteConsumerOverride(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteConsumerOverride();
    
    

### checkDisableServiceProgress(name)
    
    
    checkDisableServiceProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.api.serviceusage.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `disableService()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.empty), [protos.google.api.serviceusage.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Name of the consumer and service to disable the service on.
       *  The enable and disable methods currently only support projects.
       *  An example name would be:
       *  `projects/123/services/serviceusage.googleapis.com`
       *  where `123` is the project number (not project ID).
       */
      // const name = 'abc123'
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callDisableService() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.disableService(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDisableService();
    
    

### checkEnableServiceProgress(name)
    
    
    checkEnableServiceProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.api.serviceusage.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `enableService()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.empty), [protos.google.api.serviceusage.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Name of the consumer and service to enable the service on.
       *  The `EnableService` and `DisableService` methods currently only support
       *  projects.
       *  Enabling a service requires that the service is public or is shared with
       *  the user enabling the service.
       *  An example name would be:
       *  `projects/123/services/serviceusage.googleapis.com`
       *  where `123` is the project number (not project ID).
       */
      // const name = 'abc123'
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callEnableService() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.enableService(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callEnableService();
    
    

### checkGenerateServiceIdentityProgress(name)
    
    
    checkGenerateServiceIdentityProgress(name: string): Promise<LROperation<protos.google.api.serviceusage.v1beta1.ServiceIdentity, protos.google.protobuf.Empty>>;

Check the status of the long running operation returned by `generateServiceIdentity()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.api.serviceusage.v1beta1.ServiceIdentity](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.serviceidentity), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.empty)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Name of the consumer and service to generate an identity for.
       *  The `GenerateServiceIdentity` methods currently support projects, folders,
       *  organizations.
       *  Example parents would be:
       *  `projects/123/services/example.googleapis.com`
       *  `folders/123/services/example.googleapis.com`
       *  `organizations/123/services/example.googleapis.com`
       */
      // const parent = 'abc123'
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callGenerateServiceIdentity() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.generateServiceIdentity(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callGenerateServiceIdentity();
    
    

### checkImportAdminOverridesProgress(name)
    
    
    checkImportAdminOverridesProgress(name: string): Promise<LROperation<protos.google.api.serviceusage.v1beta1.ImportAdminOverridesResponse, protos.google.api.serviceusage.v1beta1.ImportAdminOverridesMetadata>>;

Check the status of the long running operation returned by `importAdminOverrides()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.api.serviceusage.v1beta1.ImportAdminOverridesResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.importadminoverridesresponse), [protos.google.api.serviceusage.v1beta1.ImportAdminOverridesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.importadminoverridesmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource name of the consumer.
       *  An example name would be:
       *  `projects/123/services/compute.googleapis.com`
       */
      // const parent = 'abc123'
      /**
       *  The import data is specified in the request message itself
       */
      // const inlineSource = {}
      /**
       *  Whether to force the creation of the quota overrides.
       *  Setting the force parameter to 'true' ignores all quota safety checks that
       *  would fail the request. QuotaSafetyCheck lists all such validations.
       */
      // const force = true
      /**
       *  The list of quota safety checks to ignore before the override mutation.
       *  Unlike 'force' field that ignores all the quota safety checks, the
       *  'force_only' field ignores only the specified checks; other checks are
       *  still enforced. The 'force' and 'force_only' fields cannot both be set.
       */
      // const forceOnly = [1,2,3,4]
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callImportAdminOverrides() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.importAdminOverrides(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callImportAdminOverrides();
    
    

### checkImportConsumerOverridesProgress(name)
    
    
    checkImportConsumerOverridesProgress(name: string): Promise<LROperation<protos.google.api.serviceusage.v1beta1.ImportConsumerOverridesResponse, protos.google.api.serviceusage.v1beta1.ImportConsumerOverridesMetadata>>;

Check the status of the long running operation returned by `importConsumerOverrides()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.api.serviceusage.v1beta1.ImportConsumerOverridesResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.importconsumeroverridesresponse), [protos.google.api.serviceusage.v1beta1.ImportConsumerOverridesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.importconsumeroverridesmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource name of the consumer.
       *  An example name would be:
       *  `projects/123/services/compute.googleapis.com`
       */
      // const parent = 'abc123'
      /**
       *  The import data is specified in the request message itself
       */
      // const inlineSource = {}
      /**
       *  Whether to force the creation of the quota overrides.
       *  Setting the force parameter to 'true' ignores all quota safety checks that
       *  would fail the request. QuotaSafetyCheck lists all such validations.
       */
      // const force = true
      /**
       *  The list of quota safety checks to ignore before the override mutation.
       *  Unlike 'force' field that ignores all the quota safety checks, the
       *  'force_only' field ignores only the specified checks; other checks are
       *  still enforced. The 'force' and 'force_only' fields cannot both be set.
       */
      // const forceOnly = [1,2,3,4]
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callImportConsumerOverrides() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.importConsumerOverrides(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callImportConsumerOverrides();
    
    

### checkUpdateAdminOverrideProgress(name)
    
    
    checkUpdateAdminOverrideProgress(name: string): Promise<LROperation<protos.google.api.serviceusage.v1beta1.QuotaOverride, protos.google.api.serviceusage.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `updateAdminOverride()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.api.serviceusage.v1beta1.QuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.quotaoverride), [protos.google.api.serviceusage.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource name of the override to update.
       *  An example name would be:
       *  `projects/123/services/compute.googleapis.com/consumerQuotaMetrics/compute.googleapis.com%2Fcpus/limits/%2Fproject%2Fregion/adminOverrides/4a3f2c1d`
       */
      // const name = 'abc123'
      /**
       *  The new override.
       *  Only the override_value is updated; all other fields are ignored.
       */
      // const override = {}
      /**
       *  Whether to force the update of the quota override.
       *  Setting the force parameter to 'true' ignores all quota safety checks that
       *  would fail the request. QuotaSafetyCheck lists all such validations.
       */
      // const force = true
      /**
       *  Update only the specified fields of the override.
       *  If unset, all fields will be updated.
       */
      // const updateMask = {}
      /**
       *  The list of quota safety checks to ignore before the override mutation.
       *  Unlike 'force' field that ignores all the quota safety checks, the
       *  'force_only' field ignores only the specified checks; other checks are
       *  still enforced. The 'force' and 'force_only' fields cannot both be set.
       */
      // const forceOnly = [1,2,3,4]
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callUpdateAdminOverride() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.updateAdminOverride(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateAdminOverride();
    
    

### checkUpdateConsumerOverrideProgress(name)
    
    
    checkUpdateConsumerOverrideProgress(name: string): Promise<LROperation<protos.google.api.serviceusage.v1beta1.QuotaOverride, protos.google.api.serviceusage.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `updateConsumerOverride()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.api.serviceusage.v1beta1.QuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.quotaoverride), [protos.google.api.serviceusage.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource name of the override to update.
       *  An example name would be:
       *  `projects/123/services/compute.googleapis.com/consumerQuotaMetrics/compute.googleapis.com%2Fcpus/limits/%2Fproject%2Fregion/consumerOverrides/4a3f2c1d`
       */
      // const name = 'abc123'
      /**
       *  The new override.
       *  Only the override_value is updated; all other fields are ignored.
       */
      // const override = {}
      /**
       *  Whether to force the update of the quota override.
       *  Setting the force parameter to 'true' ignores all quota safety checks that
       *  would fail the request. QuotaSafetyCheck lists all such validations.
       */
      // const force = true
      /**
       *  Update only the specified fields of the override.
       *  If unset, all fields will be updated.
       */
      // const updateMask = {}
      /**
       *  The list of quota safety checks to ignore before the override mutation.
       *  Unlike 'force' field that ignores all the quota safety checks, the
       *  'force_only' field ignores only the specified checks; other checks are
       *  still enforced. The 'force' and 'force_only' fields cannot both be set.
       */
      // const forceOnly = [1,2,3,4]
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callUpdateConsumerOverride() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.updateConsumerOverride(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateConsumerOverride();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### createAdminOverride(request, options)
    
    
    createAdminOverride(request?: protos.google.api.serviceusage.v1beta1.ICreateAdminOverrideRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.api.serviceusage.v1beta1.IQuotaOverride, protos.google.api.serviceusage.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates an admin override. An admin override is applied by an administrator of a parent folder or parent organization of the consumer receiving the override. An admin override is intended to limit the amount of quota the consumer can use out of the total quota pool allocated to all children of the folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAdminOverrideRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.icreateadminoverriderequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.api.serviceusage.v1beta1.IQuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iquotaoverride), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource name of the parent quota limit, returned by a
       *  ListConsumerQuotaMetrics or GetConsumerQuotaMetric call.
       *  An example name would be:
       *  `projects/123/services/compute.googleapis.com/consumerQuotaMetrics/compute.googleapis.com%2Fcpus/limits/%2Fproject%2Fregion`
       */
      // const parent = 'abc123'
      /**
       *  The admin override to create.
       */
      // const override = {}
      /**
       *  Whether to force the creation of the quota override.
       *  Setting the force parameter to 'true' ignores all quota safety checks that
       *  would fail the request. QuotaSafetyCheck lists all such validations.
       */
      // const force = true
      /**
       *  The list of quota safety checks to ignore before the override mutation.
       *  Unlike 'force' field that ignores all the quota safety checks, the
       *  'force_only' field ignores only the specified checks; other checks are
       *  still enforced. The 'force' and 'force_only' fields cannot both be set.
       */
      // const forceOnly = [1,2,3,4]
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callCreateAdminOverride() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.createAdminOverride(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateAdminOverride();
    
    

### createAdminOverride(request, options, callback)
    
    
    createAdminOverride(request: protos.google.api.serviceusage.v1beta1.ICreateAdminOverrideRequest, options: CallOptions, callback: Callback<LROperation<protos.google.api.serviceusage.v1beta1.IQuotaOverride, protos.google.api.serviceusage.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAdminOverrideRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.icreateadminoverriderequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.api.serviceusage.v1beta1.IQuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iquotaoverride), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAdminOverride(request, callback)
    
    
    createAdminOverride(request: protos.google.api.serviceusage.v1beta1.ICreateAdminOverrideRequest, callback: Callback<LROperation<protos.google.api.serviceusage.v1beta1.IQuotaOverride, protos.google.api.serviceusage.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAdminOverrideRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.icreateadminoverriderequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.api.serviceusage.v1beta1.IQuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iquotaoverride), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConsumerOverride(request, options)
    
    
    createConsumerOverride(request?: protos.google.api.serviceusage.v1beta1.ICreateConsumerOverrideRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.api.serviceusage.v1beta1.IQuotaOverride, protos.google.api.serviceusage.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a consumer override. A consumer override is applied to the consumer on its own authority to limit its own quota usage. Consumer overrides cannot be used to grant more quota than would be allowed by admin overrides, producer overrides, or the default limit of the service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConsumerOverrideRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.icreateconsumeroverriderequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.api.serviceusage.v1beta1.IQuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iquotaoverride), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource name of the parent quota limit, returned by a
       *  ListConsumerQuotaMetrics or GetConsumerQuotaMetric call.
       *  An example name would be:
       *  `projects/123/services/compute.googleapis.com/consumerQuotaMetrics/compute.googleapis.com%2Fcpus/limits/%2Fproject%2Fregion`
       */
      // const parent = 'abc123'
      /**
       *  The override to create.
       */
      // const override = {}
      /**
       *  Whether to force the creation of the quota override.
       *  Setting the force parameter to 'true' ignores all quota safety checks that
       *  would fail the request. QuotaSafetyCheck lists all such validations.
       */
      // const force = true
      /**
       *  The list of quota safety checks to ignore before the override mutation.
       *  Unlike 'force' field that ignores all the quota safety checks, the
       *  'force_only' field ignores only the specified checks; other checks are
       *  still enforced. The 'force' and 'force_only' fields cannot both be set.
       */
      // const forceOnly = [1,2,3,4]
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callCreateConsumerOverride() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.createConsumerOverride(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateConsumerOverride();
    
    

### createConsumerOverride(request, options, callback)
    
    
    createConsumerOverride(request: protos.google.api.serviceusage.v1beta1.ICreateConsumerOverrideRequest, options: CallOptions, callback: Callback<LROperation<protos.google.api.serviceusage.v1beta1.IQuotaOverride, protos.google.api.serviceusage.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConsumerOverrideRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.icreateconsumeroverriderequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.api.serviceusage.v1beta1.IQuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iquotaoverride), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConsumerOverride(request, callback)
    
    
    createConsumerOverride(request: protos.google.api.serviceusage.v1beta1.ICreateConsumerOverrideRequest, callback: Callback<LROperation<protos.google.api.serviceusage.v1beta1.IQuotaOverride, protos.google.api.serviceusage.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConsumerOverrideRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.icreateconsumeroverriderequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.api.serviceusage.v1beta1.IQuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iquotaoverride), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAdminOverride(request, options)
    
    
    deleteAdminOverride(request?: protos.google.api.serviceusage.v1beta1.IDeleteAdminOverrideRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.api.serviceusage.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes an admin override.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAdminOverrideRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ideleteadminoverriderequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.iempty), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource name of the override to delete.
       *  An example name would be:
       *  `projects/123/services/compute.googleapis.com/consumerQuotaMetrics/compute.googleapis.com%2Fcpus/limits/%2Fproject%2Fregion/adminOverrides/4a3f2c1d`
       */
      // const name = 'abc123'
      /**
       *  Whether to force the deletion of the quota override.
       *  Setting the force parameter to 'true' ignores all quota safety checks that
       *  would fail the request. QuotaSafetyCheck lists all such validations.
       */
      // const force = true
      /**
       *  The list of quota safety checks to ignore before the override mutation.
       *  Unlike 'force' field that ignores all the quota safety checks, the
       *  'force_only' field ignores only the specified checks; other checks are
       *  still enforced. The 'force' and 'force_only' fields cannot both be set.
       */
      // const forceOnly = [1,2,3,4]
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callDeleteAdminOverride() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.deleteAdminOverride(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteAdminOverride();
    
    

### deleteAdminOverride(request, options, callback)
    
    
    deleteAdminOverride(request: protos.google.api.serviceusage.v1beta1.IDeleteAdminOverrideRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.api.serviceusage.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAdminOverrideRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ideleteadminoverriderequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.iempty), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAdminOverride(request, callback)
    
    
    deleteAdminOverride(request: protos.google.api.serviceusage.v1beta1.IDeleteAdminOverrideRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.api.serviceusage.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAdminOverrideRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ideleteadminoverriderequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.iempty), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConsumerOverride(request, options)
    
    
    deleteConsumerOverride(request?: protos.google.api.serviceusage.v1beta1.IDeleteConsumerOverrideRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.api.serviceusage.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a consumer override.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConsumerOverrideRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ideleteconsumeroverriderequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.iempty), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource name of the override to delete.
       *  An example name would be:
       *  `projects/123/services/compute.googleapis.com/consumerQuotaMetrics/compute.googleapis.com%2Fcpus/limits/%2Fproject%2Fregion/consumerOverrides/4a3f2c1d`
       */
      // const name = 'abc123'
      /**
       *  Whether to force the deletion of the quota override.
       *  Setting the force parameter to 'true' ignores all quota safety checks that
       *  would fail the request. QuotaSafetyCheck lists all such validations.
       */
      // const force = true
      /**
       *  The list of quota safety checks to ignore before the override mutation.
       *  Unlike 'force' field that ignores all the quota safety checks, the
       *  'force_only' field ignores only the specified checks; other checks are
       *  still enforced. The 'force' and 'force_only' fields cannot both be set.
       */
      // const forceOnly = [1,2,3,4]
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callDeleteConsumerOverride() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.deleteConsumerOverride(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteConsumerOverride();
    
    

### deleteConsumerOverride(request, options, callback)
    
    
    deleteConsumerOverride(request: protos.google.api.serviceusage.v1beta1.IDeleteConsumerOverrideRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.api.serviceusage.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConsumerOverrideRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ideleteconsumeroverriderequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.iempty), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConsumerOverride(request, callback)
    
    
    deleteConsumerOverride(request: protos.google.api.serviceusage.v1beta1.IDeleteConsumerOverrideRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.api.serviceusage.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConsumerOverrideRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ideleteconsumeroverriderequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.iempty), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### disableService(request, options)
    
    
    disableService(request?: protos.google.api.serviceusage.v1beta1.IDisableServiceRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.api.serviceusage.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Disables a service so that it can no longer be used with a project. This prevents unintended usage that may cause unexpected billing charges or security leaks.

It is not valid to call the disable method on a service that is not currently enabled. Callers will receive a `FAILED_PRECONDITION` status if the target service is not currently enabled.

Operation response type: `google.protobuf.Empty`

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDisableServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.idisableservicerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.iempty), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Name of the consumer and service to disable the service on.
       *  The enable and disable methods currently only support projects.
       *  An example name would be:
       *  `projects/123/services/serviceusage.googleapis.com`
       *  where `123` is the project number (not project ID).
       */
      // const name = 'abc123'
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callDisableService() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.disableService(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDisableService();
    
    

### disableService(request, options, callback)
    
    
    disableService(request: protos.google.api.serviceusage.v1beta1.IDisableServiceRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.api.serviceusage.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDisableServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.idisableservicerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.iempty), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### disableService(request, callback)
    
    
    disableService(request: protos.google.api.serviceusage.v1beta1.IDisableServiceRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.api.serviceusage.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDisableServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.idisableservicerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.iempty), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### enableService(request, options)
    
    
    enableService(request?: protos.google.api.serviceusage.v1beta1.IEnableServiceRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.api.serviceusage.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Enables a service so that it can be used with a project.

Operation response type: `google.protobuf.Empty`

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEnableServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ienableservicerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.iempty), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Name of the consumer and service to enable the service on.
       *  The `EnableService` and `DisableService` methods currently only support
       *  projects.
       *  Enabling a service requires that the service is public or is shared with
       *  the user enabling the service.
       *  An example name would be:
       *  `projects/123/services/serviceusage.googleapis.com`
       *  where `123` is the project number (not project ID).
       */
      // const name = 'abc123'
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callEnableService() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.enableService(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callEnableService();
    
    

### enableService(request, options, callback)
    
    
    enableService(request: protos.google.api.serviceusage.v1beta1.IEnableServiceRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.api.serviceusage.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEnableServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ienableservicerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.iempty), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### enableService(request, callback)
    
    
    enableService(request: protos.google.api.serviceusage.v1beta1.IEnableServiceRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.api.serviceusage.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEnableServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ienableservicerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.iempty), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateServiceIdentity(request, options)
    
    
    generateServiceIdentity(request?: protos.google.api.serviceusage.v1beta1.IGenerateServiceIdentityRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.api.serviceusage.v1beta1.IServiceIdentity, protos.google.protobuf.IEmpty>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Generates service identity for service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateServiceIdentityRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.igenerateserviceidentityrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.api.serviceusage.v1beta1.IServiceIdentity](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iserviceidentity), [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.iempty)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Name of the consumer and service to generate an identity for.
       *  The `GenerateServiceIdentity` methods currently support projects, folders,
       *  organizations.
       *  Example parents would be:
       *  `projects/123/services/example.googleapis.com`
       *  `folders/123/services/example.googleapis.com`
       *  `organizations/123/services/example.googleapis.com`
       */
      // const parent = 'abc123'
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callGenerateServiceIdentity() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.generateServiceIdentity(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callGenerateServiceIdentity();
    
    

### generateServiceIdentity(request, options, callback)
    
    
    generateServiceIdentity(request: protos.google.api.serviceusage.v1beta1.IGenerateServiceIdentityRequest, options: CallOptions, callback: Callback<LROperation<protos.google.api.serviceusage.v1beta1.IServiceIdentity, protos.google.protobuf.IEmpty>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateServiceIdentityRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.igenerateserviceidentityrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.api.serviceusage.v1beta1.IServiceIdentity](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iserviceidentity), [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.iempty)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateServiceIdentity(request, callback)
    
    
    generateServiceIdentity(request: protos.google.api.serviceusage.v1beta1.IGenerateServiceIdentityRequest, callback: Callback<LROperation<protos.google.api.serviceusage.v1beta1.IServiceIdentity, protos.google.protobuf.IEmpty>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateServiceIdentityRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.igenerateserviceidentityrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.api.serviceusage.v1beta1.IServiceIdentity](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iserviceidentity), [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.protobuf.iempty)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConsumerQuotaLimit(request, options)
    
    
    getConsumerQuotaLimit(request?: protos.google.api.serviceusage.v1beta1.IGetConsumerQuotaLimitRequest, options?: CallOptions): Promise<[
            protos.google.api.serviceusage.v1beta1.IConsumerQuotaLimit,
            (protos.google.api.serviceusage.v1beta1.IGetConsumerQuotaLimitRequest | undefined),
            {} | undefined
        ]>;

Retrieves a summary of quota information for a specific quota limit.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConsumerQuotaLimitRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.igetconsumerquotalimitrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.api.serviceusage.v1beta1.IConsumerQuotaLimit](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iconsumerquotalimit), ([protos.google.api.serviceusage.v1beta1.IGetConsumerQuotaLimitRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.igetconsumerquotalimitrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ConsumerQuotaLimit](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.consumerquotalimit). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource name of the quota limit.
       *  Use the quota limit resource name returned by previous
       *  ListConsumerQuotaMetrics and GetConsumerQuotaMetric API calls.
       */
      // const name = 'abc123'
      /**
       *  Specifies the level of detail for quota information in the response.
       */
      // const view = {}
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callGetConsumerQuotaLimit() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await serviceusageClient.getConsumerQuotaLimit(request);
        console.log(response);
      }
    
      callGetConsumerQuotaLimit();
    
    

### getConsumerQuotaLimit(request, options, callback)
    
    
    getConsumerQuotaLimit(request: protos.google.api.serviceusage.v1beta1.IGetConsumerQuotaLimitRequest, options: CallOptions, callback: Callback<protos.google.api.serviceusage.v1beta1.IConsumerQuotaLimit, protos.google.api.serviceusage.v1beta1.IGetConsumerQuotaLimitRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConsumerQuotaLimitRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.igetconsumerquotalimitrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.api.serviceusage.v1beta1.IConsumerQuotaLimit](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iconsumerquotalimit), [protos.google.api.serviceusage.v1beta1.IGetConsumerQuotaLimitRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.igetconsumerquotalimitrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConsumerQuotaLimit(request, callback)
    
    
    getConsumerQuotaLimit(request: protos.google.api.serviceusage.v1beta1.IGetConsumerQuotaLimitRequest, callback: Callback<protos.google.api.serviceusage.v1beta1.IConsumerQuotaLimit, protos.google.api.serviceusage.v1beta1.IGetConsumerQuotaLimitRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConsumerQuotaLimitRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.igetconsumerquotalimitrequest)`   
  
`callback` |  `Callback<[protos.google.api.serviceusage.v1beta1.IConsumerQuotaLimit](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iconsumerquotalimit), [protos.google.api.serviceusage.v1beta1.IGetConsumerQuotaLimitRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.igetconsumerquotalimitrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConsumerQuotaMetric(request, options)
    
    
    getConsumerQuotaMetric(request?: protos.google.api.serviceusage.v1beta1.IGetConsumerQuotaMetricRequest, options?: CallOptions): Promise<[
            protos.google.api.serviceusage.v1beta1.IConsumerQuotaMetric,
            (protos.google.api.serviceusage.v1beta1.IGetConsumerQuotaMetricRequest | undefined),
            {} | undefined
        ]>;

Retrieves a summary of quota information for a specific quota metric

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConsumerQuotaMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.igetconsumerquotametricrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.api.serviceusage.v1beta1.IConsumerQuotaMetric](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iconsumerquotametric), ([protos.google.api.serviceusage.v1beta1.IGetConsumerQuotaMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.igetconsumerquotametricrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ConsumerQuotaMetric](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.consumerquotametric). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource name of the quota limit.
       *  An example name would be:
       *  `projects/123/services/serviceusage.googleapis.com/quotas/metrics/serviceusage.googleapis.com%2Fmutate_requests`
       */
      // const name = 'abc123'
      /**
       *  Specifies the level of detail for quota information in the response.
       */
      // const view = {}
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callGetConsumerQuotaMetric() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await serviceusageClient.getConsumerQuotaMetric(request);
        console.log(response);
      }
    
      callGetConsumerQuotaMetric();
    
    

### getConsumerQuotaMetric(request, options, callback)
    
    
    getConsumerQuotaMetric(request: protos.google.api.serviceusage.v1beta1.IGetConsumerQuotaMetricRequest, options: CallOptions, callback: Callback<protos.google.api.serviceusage.v1beta1.IConsumerQuotaMetric, protos.google.api.serviceusage.v1beta1.IGetConsumerQuotaMetricRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConsumerQuotaMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.igetconsumerquotametricrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.api.serviceusage.v1beta1.IConsumerQuotaMetric](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iconsumerquotametric), [protos.google.api.serviceusage.v1beta1.IGetConsumerQuotaMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.igetconsumerquotametricrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConsumerQuotaMetric(request, callback)
    
    
    getConsumerQuotaMetric(request: protos.google.api.serviceusage.v1beta1.IGetConsumerQuotaMetricRequest, callback: Callback<protos.google.api.serviceusage.v1beta1.IConsumerQuotaMetric, protos.google.api.serviceusage.v1beta1.IGetConsumerQuotaMetricRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConsumerQuotaMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.igetconsumerquotametricrequest)`   
  
`callback` |  `Callback<[protos.google.api.serviceusage.v1beta1.IConsumerQuotaMetric](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iconsumerquotametric), [protos.google.api.serviceusage.v1beta1.IGetConsumerQuotaMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.igetconsumerquotametricrequest) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.operation)]>` |   
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
  
### getService(request, options)
    
    
    getService(request?: protos.google.api.serviceusage.v1beta1.IGetServiceRequest, options?: CallOptions): Promise<[
            protos.google.api.serviceusage.v1beta1.IService,
            protos.google.api.serviceusage.v1beta1.IGetServiceRequest | undefined,
            {} | undefined
        ]>;

Returns the service configuration and enabled state for a given service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.igetservicerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.api.serviceusage.v1beta1.IService](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iservice), [protos.google.api.serviceusage.v1beta1.IGetServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.igetservicerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Service](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.service). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Name of the consumer and service to get the `ConsumerState` for.
       *  An example name would be:
       *  `projects/123/services/serviceusage.googleapis.com`
       *  where `123` is the project number (not project ID).
       */
      // const name = 'abc123'
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callGetService() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await serviceusageClient.getService(request);
        console.log(response);
      }
    
      callGetService();
    
    

### getService(request, options, callback)
    
    
    getService(request: protos.google.api.serviceusage.v1beta1.IGetServiceRequest, options: CallOptions, callback: Callback<protos.google.api.serviceusage.v1beta1.IService, protos.google.api.serviceusage.v1beta1.IGetServiceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.igetservicerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.api.serviceusage.v1beta1.IService](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iservice), [protos.google.api.serviceusage.v1beta1.IGetServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.igetservicerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getService(request, callback)
    
    
    getService(request: protos.google.api.serviceusage.v1beta1.IGetServiceRequest, callback: Callback<protos.google.api.serviceusage.v1beta1.IService, protos.google.api.serviceusage.v1beta1.IGetServiceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.igetservicerequest)`   
  
`callback` |  `Callback<[protos.google.api.serviceusage.v1beta1.IService](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iservice), [protos.google.api.serviceusage.v1beta1.IGetServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.igetservicerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importAdminOverrides(request, options)
    
    
    importAdminOverrides(request?: protos.google.api.serviceusage.v1beta1.IImportAdminOverridesRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.api.serviceusage.v1beta1.IImportAdminOverridesResponse, protos.google.api.serviceusage.v1beta1.IImportAdminOverridesMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates or updates multiple admin overrides atomically, all on the same consumer, but on many different metrics or limits. The name field in the quota override message should not be set.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportAdminOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iimportadminoverridesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.api.serviceusage.v1beta1.IImportAdminOverridesResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iimportadminoverridesresponse), [protos.google.api.serviceusage.v1beta1.IImportAdminOverridesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iimportadminoverridesmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource name of the consumer.
       *  An example name would be:
       *  `projects/123/services/compute.googleapis.com`
       */
      // const parent = 'abc123'
      /**
       *  The import data is specified in the request message itself
       */
      // const inlineSource = {}
      /**
       *  Whether to force the creation of the quota overrides.
       *  Setting the force parameter to 'true' ignores all quota safety checks that
       *  would fail the request. QuotaSafetyCheck lists all such validations.
       */
      // const force = true
      /**
       *  The list of quota safety checks to ignore before the override mutation.
       *  Unlike 'force' field that ignores all the quota safety checks, the
       *  'force_only' field ignores only the specified checks; other checks are
       *  still enforced. The 'force' and 'force_only' fields cannot both be set.
       */
      // const forceOnly = [1,2,3,4]
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callImportAdminOverrides() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.importAdminOverrides(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callImportAdminOverrides();
    
    

### importAdminOverrides(request, options, callback)
    
    
    importAdminOverrides(request: protos.google.api.serviceusage.v1beta1.IImportAdminOverridesRequest, options: CallOptions, callback: Callback<LROperation<protos.google.api.serviceusage.v1beta1.IImportAdminOverridesResponse, protos.google.api.serviceusage.v1beta1.IImportAdminOverridesMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportAdminOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iimportadminoverridesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.api.serviceusage.v1beta1.IImportAdminOverridesResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iimportadminoverridesresponse), [protos.google.api.serviceusage.v1beta1.IImportAdminOverridesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iimportadminoverridesmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importAdminOverrides(request, callback)
    
    
    importAdminOverrides(request: protos.google.api.serviceusage.v1beta1.IImportAdminOverridesRequest, callback: Callback<LROperation<protos.google.api.serviceusage.v1beta1.IImportAdminOverridesResponse, protos.google.api.serviceusage.v1beta1.IImportAdminOverridesMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportAdminOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iimportadminoverridesrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.api.serviceusage.v1beta1.IImportAdminOverridesResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iimportadminoverridesresponse), [protos.google.api.serviceusage.v1beta1.IImportAdminOverridesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iimportadminoverridesmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importConsumerOverrides(request, options)
    
    
    importConsumerOverrides(request?: protos.google.api.serviceusage.v1beta1.IImportConsumerOverridesRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.api.serviceusage.v1beta1.IImportConsumerOverridesResponse, protos.google.api.serviceusage.v1beta1.IImportConsumerOverridesMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates or updates multiple consumer overrides atomically, all on the same consumer, but on many different metrics or limits. The name field in the quota override message should not be set.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportConsumerOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iimportconsumeroverridesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.api.serviceusage.v1beta1.IImportConsumerOverridesResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iimportconsumeroverridesresponse), [protos.google.api.serviceusage.v1beta1.IImportConsumerOverridesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iimportconsumeroverridesmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource name of the consumer.
       *  An example name would be:
       *  `projects/123/services/compute.googleapis.com`
       */
      // const parent = 'abc123'
      /**
       *  The import data is specified in the request message itself
       */
      // const inlineSource = {}
      /**
       *  Whether to force the creation of the quota overrides.
       *  Setting the force parameter to 'true' ignores all quota safety checks that
       *  would fail the request. QuotaSafetyCheck lists all such validations.
       */
      // const force = true
      /**
       *  The list of quota safety checks to ignore before the override mutation.
       *  Unlike 'force' field that ignores all the quota safety checks, the
       *  'force_only' field ignores only the specified checks; other checks are
       *  still enforced. The 'force' and 'force_only' fields cannot both be set.
       */
      // const forceOnly = [1,2,3,4]
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callImportConsumerOverrides() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.importConsumerOverrides(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callImportConsumerOverrides();
    
    

### importConsumerOverrides(request, options, callback)
    
    
    importConsumerOverrides(request: protos.google.api.serviceusage.v1beta1.IImportConsumerOverridesRequest, options: CallOptions, callback: Callback<LROperation<protos.google.api.serviceusage.v1beta1.IImportConsumerOverridesResponse, protos.google.api.serviceusage.v1beta1.IImportConsumerOverridesMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportConsumerOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iimportconsumeroverridesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.api.serviceusage.v1beta1.IImportConsumerOverridesResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iimportconsumeroverridesresponse), [protos.google.api.serviceusage.v1beta1.IImportConsumerOverridesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iimportconsumeroverridesmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importConsumerOverrides(request, callback)
    
    
    importConsumerOverrides(request: protos.google.api.serviceusage.v1beta1.IImportConsumerOverridesRequest, callback: Callback<LROperation<protos.google.api.serviceusage.v1beta1.IImportConsumerOverridesResponse, protos.google.api.serviceusage.v1beta1.IImportConsumerOverridesMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportConsumerOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iimportconsumeroverridesrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.api.serviceusage.v1beta1.IImportConsumerOverridesResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iimportconsumeroverridesresponse), [protos.google.api.serviceusage.v1beta1.IImportConsumerOverridesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iimportconsumeroverridesmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
  
### listAdminOverrides(request, options)
    
    
    listAdminOverrides(request?: protos.google.api.serviceusage.v1beta1.IListAdminOverridesRequest, options?: CallOptions): Promise<[
            protos.google.api.serviceusage.v1beta1.IQuotaOverride[],
            protos.google.api.serviceusage.v1beta1.IListAdminOverridesRequest | null,
            protos.google.api.serviceusage.v1beta1.IListAdminOverridesResponse
        ]>;

Lists all admin overrides on this limit.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAdminOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistadminoverridesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.api.serviceusage.v1beta1.IQuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iquotaoverride)[], [protos.google.api.serviceusage.v1beta1.IListAdminOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistadminoverridesrequest) | null, [protos.google.api.serviceusage.v1beta1.IListAdminOverridesResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistadminoverridesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [QuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.quotaoverride). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listAdminOverridesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listAdminOverrides(request, options, callback)
    
    
    listAdminOverrides(request: protos.google.api.serviceusage.v1beta1.IListAdminOverridesRequest, options: CallOptions, callback: PaginationCallback<protos.google.api.serviceusage.v1beta1.IListAdminOverridesRequest, protos.google.api.serviceusage.v1beta1.IListAdminOverridesResponse | null | undefined, protos.google.api.serviceusage.v1beta1.IQuotaOverride>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAdminOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistadminoverridesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.api.serviceusage.v1beta1.IListAdminOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistadminoverridesrequest), [protos.google.api.serviceusage.v1beta1.IListAdminOverridesResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistadminoverridesresponse) | null | undefined, [protos.google.api.serviceusage.v1beta1.IQuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iquotaoverride)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAdminOverrides(request, callback)
    
    
    listAdminOverrides(request: protos.google.api.serviceusage.v1beta1.IListAdminOverridesRequest, callback: PaginationCallback<protos.google.api.serviceusage.v1beta1.IListAdminOverridesRequest, protos.google.api.serviceusage.v1beta1.IListAdminOverridesResponse | null | undefined, protos.google.api.serviceusage.v1beta1.IQuotaOverride>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAdminOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistadminoverridesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.api.serviceusage.v1beta1.IListAdminOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistadminoverridesrequest), [protos.google.api.serviceusage.v1beta1.IListAdminOverridesResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistadminoverridesresponse) | null | undefined, [protos.google.api.serviceusage.v1beta1.IQuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iquotaoverride)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAdminOverridesAsync(request, options)
    
    
    listAdminOverridesAsync(request?: protos.google.api.serviceusage.v1beta1.IListAdminOverridesRequest, options?: CallOptions): AsyncIterable<protos.google.api.serviceusage.v1beta1.IQuotaOverride>;

Equivalent to `listAdminOverrides`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAdminOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistadminoverridesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.api.serviceusage.v1beta1.IQuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iquotaoverride)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [QuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.quotaoverride). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource name of the parent quota limit, returned by a
       *  ListConsumerQuotaMetrics or GetConsumerQuotaMetric call.
       *  An example name would be:
       *  `projects/123/services/compute.googleapis.com/consumerQuotaMetrics/compute.googleapis.com%2Fcpus/limits/%2Fproject%2Fregion`
       */
      // const parent = 'abc123'
      /**
       *  Requested size of the next page of data.
       */
      // const pageSize = 1234
      /**
       *  Token identifying which result to start with; returned by a previous list
       *  call.
       */
      // const pageToken = 'abc123'
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callListAdminOverrides() {
        // Construct request
        const request = {
        };
    
        // Run request
        const iterable = serviceusageClient.[listAdminOverridesAsync](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/v1beta1.serviceusageclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListAdminOverrides();
    
    

### listAdminOverridesStream(request, options)
    
    
    listAdminOverridesStream(request?: protos.google.api.serviceusage.v1beta1.IListAdminOverridesRequest, options?: CallOptions): Transform;

Equivalent to `listAdminOverrides`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAdminOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistadminoverridesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [QuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.quotaoverride) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listAdminOverridesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listConsumerOverrides(request, options)
    
    
    listConsumerOverrides(request?: protos.google.api.serviceusage.v1beta1.IListConsumerOverridesRequest, options?: CallOptions): Promise<[
            protos.google.api.serviceusage.v1beta1.IQuotaOverride[],
            protos.google.api.serviceusage.v1beta1.IListConsumerOverridesRequest | null,
            protos.google.api.serviceusage.v1beta1.IListConsumerOverridesResponse
        ]>;

Lists all consumer overrides on this limit.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConsumerOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumeroverridesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.api.serviceusage.v1beta1.IQuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iquotaoverride)[], [protos.google.api.serviceusage.v1beta1.IListConsumerOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumeroverridesrequest) | null, [protos.google.api.serviceusage.v1beta1.IListConsumerOverridesResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumeroverridesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [QuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.quotaoverride). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listConsumerOverridesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listConsumerOverrides(request, options, callback)
    
    
    listConsumerOverrides(request: protos.google.api.serviceusage.v1beta1.IListConsumerOverridesRequest, options: CallOptions, callback: PaginationCallback<protos.google.api.serviceusage.v1beta1.IListConsumerOverridesRequest, protos.google.api.serviceusage.v1beta1.IListConsumerOverridesResponse | null | undefined, protos.google.api.serviceusage.v1beta1.IQuotaOverride>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConsumerOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumeroverridesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.api.serviceusage.v1beta1.IListConsumerOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumeroverridesrequest), [protos.google.api.serviceusage.v1beta1.IListConsumerOverridesResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumeroverridesresponse) | null | undefined, [protos.google.api.serviceusage.v1beta1.IQuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iquotaoverride)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConsumerOverrides(request, callback)
    
    
    listConsumerOverrides(request: protos.google.api.serviceusage.v1beta1.IListConsumerOverridesRequest, callback: PaginationCallback<protos.google.api.serviceusage.v1beta1.IListConsumerOverridesRequest, protos.google.api.serviceusage.v1beta1.IListConsumerOverridesResponse | null | undefined, protos.google.api.serviceusage.v1beta1.IQuotaOverride>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConsumerOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumeroverridesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.api.serviceusage.v1beta1.IListConsumerOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumeroverridesrequest), [protos.google.api.serviceusage.v1beta1.IListConsumerOverridesResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumeroverridesresponse) | null | undefined, [protos.google.api.serviceusage.v1beta1.IQuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iquotaoverride)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConsumerOverridesAsync(request, options)
    
    
    listConsumerOverridesAsync(request?: protos.google.api.serviceusage.v1beta1.IListConsumerOverridesRequest, options?: CallOptions): AsyncIterable<protos.google.api.serviceusage.v1beta1.IQuotaOverride>;

Equivalent to `listConsumerOverrides`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConsumerOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumeroverridesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.api.serviceusage.v1beta1.IQuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iquotaoverride)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [QuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.quotaoverride). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource name of the parent quota limit, returned by a
       *  ListConsumerQuotaMetrics or GetConsumerQuotaMetric call.
       *  An example name would be:
       *  `projects/123/services/compute.googleapis.com/consumerQuotaMetrics/compute.googleapis.com%2Fcpus/limits/%2Fproject%2Fregion`
       */
      // const parent = 'abc123'
      /**
       *  Requested size of the next page of data.
       */
      // const pageSize = 1234
      /**
       *  Token identifying which result to start with; returned by a previous list
       *  call.
       */
      // const pageToken = 'abc123'
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callListConsumerOverrides() {
        // Construct request
        const request = {
        };
    
        // Run request
        const iterable = serviceusageClient.[listConsumerOverridesAsync](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/v1beta1.serviceusageclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListConsumerOverrides();
    
    

### listConsumerOverridesStream(request, options)
    
    
    listConsumerOverridesStream(request?: protos.google.api.serviceusage.v1beta1.IListConsumerOverridesRequest, options?: CallOptions): Transform;

Equivalent to `listConsumerOverrides`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConsumerOverridesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumeroverridesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [QuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.quotaoverride) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listConsumerOverridesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listConsumerQuotaMetrics(request, options)
    
    
    listConsumerQuotaMetrics(request?: protos.google.api.serviceusage.v1beta1.IListConsumerQuotaMetricsRequest, options?: CallOptions): Promise<[
            protos.google.api.serviceusage.v1beta1.IConsumerQuotaMetric[],
            protos.google.api.serviceusage.v1beta1.IListConsumerQuotaMetricsRequest | null,
            protos.google.api.serviceusage.v1beta1.IListConsumerQuotaMetricsResponse
        ]>;

Retrieves a summary of all quota information visible to the service consumer, organized by service metric. Each metric includes information about all of its defined limits. Each limit includes the limit configuration (quota unit, preciseness, default value), the current effective limit value, and all of the overrides applied to the limit.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConsumerQuotaMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumerquotametricsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.api.serviceusage.v1beta1.IConsumerQuotaMetric](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iconsumerquotametric)[], [protos.google.api.serviceusage.v1beta1.IListConsumerQuotaMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumerquotametricsrequest) | null, [protos.google.api.serviceusage.v1beta1.IListConsumerQuotaMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumerquotametricsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [ConsumerQuotaMetric](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.consumerquotametric). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listConsumerQuotaMetricsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listConsumerQuotaMetrics(request, options, callback)
    
    
    listConsumerQuotaMetrics(request: protos.google.api.serviceusage.v1beta1.IListConsumerQuotaMetricsRequest, options: CallOptions, callback: PaginationCallback<protos.google.api.serviceusage.v1beta1.IListConsumerQuotaMetricsRequest, protos.google.api.serviceusage.v1beta1.IListConsumerQuotaMetricsResponse | null | undefined, protos.google.api.serviceusage.v1beta1.IConsumerQuotaMetric>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConsumerQuotaMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumerquotametricsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.api.serviceusage.v1beta1.IListConsumerQuotaMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumerquotametricsrequest), [protos.google.api.serviceusage.v1beta1.IListConsumerQuotaMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumerquotametricsresponse) | null | undefined, [protos.google.api.serviceusage.v1beta1.IConsumerQuotaMetric](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iconsumerquotametric)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConsumerQuotaMetrics(request, callback)
    
    
    listConsumerQuotaMetrics(request: protos.google.api.serviceusage.v1beta1.IListConsumerQuotaMetricsRequest, callback: PaginationCallback<protos.google.api.serviceusage.v1beta1.IListConsumerQuotaMetricsRequest, protos.google.api.serviceusage.v1beta1.IListConsumerQuotaMetricsResponse | null | undefined, protos.google.api.serviceusage.v1beta1.IConsumerQuotaMetric>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConsumerQuotaMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumerquotametricsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.api.serviceusage.v1beta1.IListConsumerQuotaMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumerquotametricsrequest), [protos.google.api.serviceusage.v1beta1.IListConsumerQuotaMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumerquotametricsresponse) | null | undefined, [protos.google.api.serviceusage.v1beta1.IConsumerQuotaMetric](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iconsumerquotametric)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConsumerQuotaMetricsAsync(request, options)
    
    
    listConsumerQuotaMetricsAsync(request?: protos.google.api.serviceusage.v1beta1.IListConsumerQuotaMetricsRequest, options?: CallOptions): AsyncIterable<protos.google.api.serviceusage.v1beta1.IConsumerQuotaMetric>;

Equivalent to `listConsumerQuotaMetrics`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConsumerQuotaMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumerquotametricsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.api.serviceusage.v1beta1.IConsumerQuotaMetric](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iconsumerquotametric)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [ConsumerQuotaMetric](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.consumerquotametric). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Parent of the quotas resource.
       *  Some example names would be:
       *  `projects/123/services/serviceconsumermanagement.googleapis.com`
       *  `folders/345/services/serviceconsumermanagement.googleapis.com`
       *  `organizations/456/services/serviceconsumermanagement.googleapis.com`
       */
      // const parent = 'abc123'
      /**
       *  Requested size of the next page of data.
       */
      // const pageSize = 1234
      /**
       *  Token identifying which result to start with; returned by a previous list
       *  call.
       */
      // const pageToken = 'abc123'
      /**
       *  Specifies the level of detail for quota information in the response.
       */
      // const view = {}
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callListConsumerQuotaMetrics() {
        // Construct request
        const request = {
        };
    
        // Run request
        const iterable = serviceusageClient.[listConsumerQuotaMetricsAsync](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/v1beta1.serviceusageclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListConsumerQuotaMetrics();
    
    

### listConsumerQuotaMetricsStream(request, options)
    
    
    listConsumerQuotaMetricsStream(request?: protos.google.api.serviceusage.v1beta1.IListConsumerQuotaMetricsRequest, options?: CallOptions): Transform;

Equivalent to `listConsumerQuotaMetrics`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConsumerQuotaMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistconsumerquotametricsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [ConsumerQuotaMetric](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.consumerquotametric) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listConsumerQuotaMetricsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listOperationsAsync(request, options)
    
    
    listOperationsAsync(request: protos.google.longrunning.ListOperationsRequest, options?: gax.CallOptions): AsyncIterable<protos.google.longrunning.IOperation>;

Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. Returns an iterable object.

For-await-of syntax is used with the iterable to recursively get response element on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
**Example**
    
    
    const client = longrunning.operationsClient();
    for await (const response of client.listOperationsAsync(request));
    // doThingsWith(response)
    

### listServices(request, options)
    
    
    listServices(request?: protos.google.api.serviceusage.v1beta1.IListServicesRequest, options?: CallOptions): Promise<[
            protos.google.api.serviceusage.v1beta1.IService[],
            protos.google.api.serviceusage.v1beta1.IListServicesRequest | null,
            protos.google.api.serviceusage.v1beta1.IListServicesResponse
        ]>;

Lists all services available to the specified project, and the current state of those services with respect to the project. The list includes all public services, all services for which the calling user has the `servicemanagement.services.bind` permission, and all services that have already been enabled on the project. The list can be filtered to only include services in a specific state, for example to only include services enabled on the project.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistservicesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.api.serviceusage.v1beta1.IService](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iservice)[], [protos.google.api.serviceusage.v1beta1.IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistservicesrequest) | null, [protos.google.api.serviceusage.v1beta1.IListServicesResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistservicesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Service](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.service). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listServicesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listServices(request, options, callback)
    
    
    listServices(request: protos.google.api.serviceusage.v1beta1.IListServicesRequest, options: CallOptions, callback: PaginationCallback<protos.google.api.serviceusage.v1beta1.IListServicesRequest, protos.google.api.serviceusage.v1beta1.IListServicesResponse | null | undefined, protos.google.api.serviceusage.v1beta1.IService>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistservicesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.api.serviceusage.v1beta1.IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistservicesrequest), [protos.google.api.serviceusage.v1beta1.IListServicesResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistservicesresponse) | null | undefined, [protos.google.api.serviceusage.v1beta1.IService](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iservice)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listServices(request, callback)
    
    
    listServices(request: protos.google.api.serviceusage.v1beta1.IListServicesRequest, callback: PaginationCallback<protos.google.api.serviceusage.v1beta1.IListServicesRequest, protos.google.api.serviceusage.v1beta1.IListServicesResponse | null | undefined, protos.google.api.serviceusage.v1beta1.IService>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistservicesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.api.serviceusage.v1beta1.IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistservicesrequest), [protos.google.api.serviceusage.v1beta1.IListServicesResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistservicesresponse) | null | undefined, [protos.google.api.serviceusage.v1beta1.IService](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iservice)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listServicesAsync(request, options)
    
    
    listServicesAsync(request?: protos.google.api.serviceusage.v1beta1.IListServicesRequest, options?: CallOptions): AsyncIterable<protos.google.api.serviceusage.v1beta1.IService>;

Equivalent to `listServices`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistservicesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.api.serviceusage.v1beta1.IService](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iservice)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Service](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.service). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Parent to search for services on.
       *  An example name would be:
       *  `projects/123`
       *  where `123` is the project number (not project ID).
       */
      // const parent = 'abc123'
      /**
       *  Requested size of the next page of data.
       *  Requested page size cannot exceed 200.
       *   If not set, the default page size is 50.
       */
      // const pageSize = 1234
      /**
       *  Token identifying which result to start with, which is returned by a
       *  previous list call.
       */
      // const pageToken = 'abc123'
      /**
       *  Only list services that conform to the given filter.
       *  The allowed filter strings are `state:ENABLED` and `state:DISABLED`.
       */
      // const filter = 'abc123'
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callListServices() {
        // Construct request
        const request = {
        };
    
        // Run request
        const iterable = serviceusageClient.listServicesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListServices();
    
    

### listServicesStream(request, options)
    
    
    listServicesStream(request?: protos.google.api.serviceusage.v1beta1.IListServicesRequest, options?: CallOptions): Transform;

Equivalent to `listServices`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ilistservicesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Service](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.service) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listServicesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### updateAdminOverride(request, options)
    
    
    updateAdminOverride(request?: protos.google.api.serviceusage.v1beta1.IUpdateAdminOverrideRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.api.serviceusage.v1beta1.IQuotaOverride, protos.google.api.serviceusage.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates an admin override.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAdminOverrideRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iupdateadminoverriderequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.api.serviceusage.v1beta1.IQuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iquotaoverride), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource name of the override to update.
       *  An example name would be:
       *  `projects/123/services/compute.googleapis.com/consumerQuotaMetrics/compute.googleapis.com%2Fcpus/limits/%2Fproject%2Fregion/adminOverrides/4a3f2c1d`
       */
      // const name = 'abc123'
      /**
       *  The new override.
       *  Only the override_value is updated; all other fields are ignored.
       */
      // const override = {}
      /**
       *  Whether to force the update of the quota override.
       *  Setting the force parameter to 'true' ignores all quota safety checks that
       *  would fail the request. QuotaSafetyCheck lists all such validations.
       */
      // const force = true
      /**
       *  Update only the specified fields of the override.
       *  If unset, all fields will be updated.
       */
      // const updateMask = {}
      /**
       *  The list of quota safety checks to ignore before the override mutation.
       *  Unlike 'force' field that ignores all the quota safety checks, the
       *  'force_only' field ignores only the specified checks; other checks are
       *  still enforced. The 'force' and 'force_only' fields cannot both be set.
       */
      // const forceOnly = [1,2,3,4]
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callUpdateAdminOverride() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.updateAdminOverride(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateAdminOverride();
    
    

### updateAdminOverride(request, options, callback)
    
    
    updateAdminOverride(request: protos.google.api.serviceusage.v1beta1.IUpdateAdminOverrideRequest, options: CallOptions, callback: Callback<LROperation<protos.google.api.serviceusage.v1beta1.IQuotaOverride, protos.google.api.serviceusage.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAdminOverrideRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iupdateadminoverriderequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.api.serviceusage.v1beta1.IQuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iquotaoverride), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAdminOverride(request, callback)
    
    
    updateAdminOverride(request: protos.google.api.serviceusage.v1beta1.IUpdateAdminOverrideRequest, callback: Callback<LROperation<protos.google.api.serviceusage.v1beta1.IQuotaOverride, protos.google.api.serviceusage.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAdminOverrideRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iupdateadminoverriderequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.api.serviceusage.v1beta1.IQuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iquotaoverride), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConsumerOverride(request, options)
    
    
    updateConsumerOverride(request?: protos.google.api.serviceusage.v1beta1.IUpdateConsumerOverrideRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.api.serviceusage.v1beta1.IQuotaOverride, protos.google.api.serviceusage.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates a consumer override.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConsumerOverrideRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iupdateconsumeroverriderequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.api.serviceusage.v1beta1.IQuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iquotaoverride), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource name of the override to update.
       *  An example name would be:
       *  `projects/123/services/compute.googleapis.com/consumerQuotaMetrics/compute.googleapis.com%2Fcpus/limits/%2Fproject%2Fregion/consumerOverrides/4a3f2c1d`
       */
      // const name = 'abc123'
      /**
       *  The new override.
       *  Only the override_value is updated; all other fields are ignored.
       */
      // const override = {}
      /**
       *  Whether to force the update of the quota override.
       *  Setting the force parameter to 'true' ignores all quota safety checks that
       *  would fail the request. QuotaSafetyCheck lists all such validations.
       */
      // const force = true
      /**
       *  Update only the specified fields of the override.
       *  If unset, all fields will be updated.
       */
      // const updateMask = {}
      /**
       *  The list of quota safety checks to ignore before the override mutation.
       *  Unlike 'force' field that ignores all the quota safety checks, the
       *  'force_only' field ignores only the specified checks; other checks are
       *  still enforced. The 'force' and 'force_only' fields cannot both be set.
       */
      // const forceOnly = [1,2,3,4]
    
      // Imports the Serviceusage library
      const {ServiceUsageClient} = require('[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const serviceusageClient = new [ServiceUsageClient](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)();
    
      async function callUpdateConsumerOverride() {
        // Construct request
        const request = {
        };
    
        // Run request
        const [operation] = await serviceusageClient.updateConsumerOverride(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateConsumerOverride();
    
    

### updateConsumerOverride(request, options, callback)
    
    
    updateConsumerOverride(request: protos.google.api.serviceusage.v1beta1.IUpdateConsumerOverrideRequest, options: CallOptions, callback: Callback<LROperation<protos.google.api.serviceusage.v1beta1.IQuotaOverride, protos.google.api.serviceusage.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConsumerOverrideRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iupdateconsumeroverriderequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.api.serviceusage.v1beta1.IQuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iquotaoverride), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConsumerOverride(request, callback)
    
    
    updateConsumerOverride(request: protos.google.api.serviceusage.v1beta1.IUpdateConsumerOverrideRequest, callback: Callback<LROperation<protos.google.api.serviceusage.v1beta1.IQuotaOverride, protos.google.api.serviceusage.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConsumerOverrideRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iupdateconsumeroverriderequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.api.serviceusage.v1beta1.IQuotaOverride](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.iquotaoverride), [protos.google.api.serviceusage.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.serviceusage.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
