---
url: https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/v1alpha.gdchardwaremanagementclient
title: Class v1alpha.GDCHardwareManagementClient (0.12.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:32.229708+00:00
---

# Class v1alpha.GDCHardwareManagementClient (0.12.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/v1alpha.gdchardwaremanagementclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1alpha.GDCHardwareManagementClient (0.12.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.1 (latest)  0.10.0  0.7.0  0.5.1  0.4.0  0.2.0 

The GDC Hardware Management service. v1alpha

## Package

[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of GDCHardwareManagementClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new GDCHardwareManagementClient({fallback: true}, gax); ```  
  
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

### gDCHardwareManagementStub
    
    
    gDCHardwareManagementStub?: Promise<{
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

### cancelOperation(request, optionsOrCallback, callback)
    
    
    cancelOperation(request: protos.google.longrunning.CancelOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>, callback?: Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>): Promise<protos.google.protobuf.Empty>;

Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an value with a of 1, corresponding to `Code.CANCELLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### cancelOrder(request, options)
    
    
    cancelOrder(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.ICancelOrderRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Cancels an order.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelOrderRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icancelorderrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the order.
       *  Format: `projects/{project}/locations/{location}/orders/{order}`
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callCancelOrder() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.cancelOrder(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCancelOrder();
    
    

### cancelOrder(request, options, callback)
    
    
    cancelOrder(request: protos.google.cloud.gdchardwaremanagement.v1alpha.ICancelOrderRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelOrderRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icancelorderrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelOrder(request, callback)
    
    
    cancelOrder(request: protos.google.cloud.gdchardwaremanagement.v1alpha.ICancelOrderRequest, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelOrderRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icancelorderrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### changeLogEntryPath(project, location, order, changeLogEntry)
    
    
    changeLogEntryPath(project: string, location: string, order: string, changeLogEntry: string): string;

Return a fully-qualified changeLogEntry resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`order` |  `string`   
  
`changeLogEntry` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### checkCancelOrderProgress(name)
    
    
    checkCancelOrderProgress(name: string): Promise<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.Order, protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `cancelOrder()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.Order](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.order-class), [protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the order.
       *  Format: `projects/{project}/locations/{location}/orders/{order}`
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callCancelOrder() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.cancelOrder(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCancelOrder();
    
    

### checkCreateCommentProgress(name)
    
    
    checkCreateCommentProgress(name: string): Promise<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.Comment, protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `createComment()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.Comment](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.comment), [protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The order to create the comment on.
       *  Format: `projects/{project}/locations/{location}/orders/{order}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. ID used to uniquely identify the Comment within its parent scope.
       *  This field should contain at most 63 characters and must start with
       *  lowercase characters.
       *  Only lowercase characters, numbers and `-` are accepted.
       *  The `-` character cannot be the first or the last one.
       *  A system generated ID will be used if the field is not set.
       *  The comment.name field in the request will be ignored.
       */
      // const commentId = 'abc123'
      /**
       *  Required. The comment to create.
       */
      // const comment = {}
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callCreateComment() {
        // Construct request
        const request = {
          parent,
          comment,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.createComment(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateComment();
    
    

### checkCreateHardwareGroupProgress(name)
    
    
    checkCreateHardwareGroupProgress(name: string): Promise<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup, protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `createHardwareGroup()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.hardwaregroup-class), [protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The order to create the hardware group in.
       *  Format: `projects/{project}/locations/{location}/orders/{order}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. ID used to uniquely identify the HardwareGroup within its parent
       *  scope. This field should contain at most 63 characters and must start with
       *  lowercase characters.
       *  Only lowercase characters, numbers and `-` are accepted.
       *  The `-` character cannot be the first or the last one.
       *  A system generated ID will be used if the field is not set.
       *  The hardware_group.name field in the request will be ignored.
       */
      // const hardwareGroupId = 'abc123'
      /**
       *  Required. The hardware group to create.
       */
      // const hardwareGroup = {}
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callCreateHardwareGroup() {
        // Construct request
        const request = {
          parent,
          hardwareGroup,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.createHardwareGroup(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateHardwareGroup();
    
    

### checkCreateHardwareProgress(name)
    
    
    checkCreateHardwareProgress(name: string): Promise<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.Hardware, protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `createHardware()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.Hardware](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.hardware-class), [protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location to create hardware in.
       *  Format: `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. ID used to uniquely identify the Hardware within its parent
       *  scope. This field should contain at most 63 characters and must start with
       *  lowercase characters.
       *  Only lowercase characters, numbers and `-` are accepted.
       *  The `-` character cannot be the first or the last one.
       *  A system generated ID will be used if the field is not set.
       *  The hardware.name field in the request will be ignored.
       */
      // const hardwareId = 'abc123'
      /**
       *  Required. The resource to create.
       */
      // const hardware = {}
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callCreateHardware() {
        // Construct request
        const request = {
          parent,
          hardware,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.createHardware(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateHardware();
    
    

### checkCreateOrderProgress(name)
    
    
    checkCreateOrderProgress(name: string): Promise<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.Order, protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `createOrder()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.Order](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.order-class), [protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location to create the order in.
       *  Format: `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. ID used to uniquely identify the Order within its parent scope.
       *  This field should contain at most 63 characters and must start with
       *  lowercase characters.
       *  Only lowercase characters, numbers and `-` are accepted.
       *  The `-` character cannot be the first or the last one.
       *  A system generated ID will be used if the field is not set.
       *  The order.name field in the request will be ignored.
       */
      // const orderId = 'abc123'
      /**
       *  Required. The order to create.
       */
      // const order = {}
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callCreateOrder() {
        // Construct request
        const request = {
          parent,
          order,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.createOrder(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateOrder();
    
    

### checkCreateSiteProgress(name)
    
    
    checkCreateSiteProgress(name: string): Promise<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.Site, protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `createSite()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.Site](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.site), [protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location to create the site in.
       *  Format: `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. ID used to uniquely identify the Site within its parent scope.
       *  This field should contain at most 63 characters and must start with
       *  lowercase characters.
       *  Only lowercase characters, numbers and `-` are accepted.
       *  The `-` character cannot be the first or the last one.
       *  A system generated ID will be used if the field is not set.
       *  The site.name field in the request will be ignored.
       */
      // const siteId = 'abc123'
      /**
       *  Required. The site to create.
       */
      // const site = {}
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callCreateSite() {
        // Construct request
        const request = {
          parent,
          site,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.createSite(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateSite();
    
    

### checkCreateZoneProgress(name)
    
    
    checkCreateZoneProgress(name: string): Promise<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.Zone, protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `createZone()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.Zone](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.zone-class), [protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location to create the zone in.
       *  Format: `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. ID used to uniquely identify the Zone within its parent scope.
       *  This field should contain at most 63 characters and must start with
       *  lowercase characters.
       *  Only lowercase characters, numbers and `-` are accepted.
       *  The `-` character cannot be the first or the last one.
       *  A system generated ID will be used if the field is not set.
       *  The zone.name field in the request will be ignored.
       */
      // const zoneId = 'abc123'
      /**
       *  Required. The zone to create.
       */
      // const zone = {}
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callCreateZone() {
        // Construct request
        const request = {
          parent,
          zone,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.createZone(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateZone();
    
    

### checkDeleteHardwareGroupProgress(name)
    
    
    checkDeleteHardwareGroupProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `deleteHardwareGroup()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.empty), [protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the hardware group.
       *  Format:
       *  `projects/{project}/locations/{location}/orders/{order}/hardwareGroups/{hardware_group}`
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callDeleteHardwareGroup() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.deleteHardwareGroup(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteHardwareGroup();
    
    

### checkDeleteHardwareProgress(name)
    
    
    checkDeleteHardwareProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `deleteHardware()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.empty), [protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the hardware.
       *  Format: `projects/{project}/locations/{location}/hardware/{hardware}`
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callDeleteHardware() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.deleteHardware(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteHardware();
    
    

### checkDeleteOrderProgress(name)
    
    
    checkDeleteOrderProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `deleteOrder()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.empty), [protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the order.
       *  Format: `projects/{project}/locations/{location}/orders/{order}`
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. An option to delete any nested resources in the Order, such as a
       *  HardwareGroup. If true, any nested resources for this Order will also be
       *  deleted. Otherwise, the request will only succeed if the Order has no
       *  nested resources.
       */
      // const force = true
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callDeleteOrder() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.deleteOrder(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteOrder();
    
    

### checkDeleteSiteProgress(name)
    
    
    checkDeleteSiteProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `deleteSite()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.empty), [protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the site.
       *  Format: `projects/{project}/locations/{location}/sites/{site}`
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callDeleteSite() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.deleteSite(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteSite();
    
    

### checkDeleteZoneProgress(name)
    
    
    checkDeleteZoneProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `deleteZone()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.empty), [protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the zone.
       *  Format: `projects/{project}/locations/{location}/zones/{zone}`
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callDeleteZone() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.deleteZone(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteZone();
    
    

### checkRequestOrderDateChangeProgress(name)
    
    
    checkRequestOrderDateChangeProgress(name: string): Promise<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.Order, protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `requestOrderDateChange()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.Order](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.order-class), [protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the order to update.
       *  Format: projects/{project}/locations/{location}/orders/{order}
       */
      // const name = 'abc123'
      /**
       *  Required. The date to which the customer or Google wants to set the
       *  scheduled installation date.
       */
      // const requestedDate = {}
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callRequestOrderDateChange() {
        // Construct request
        const request = {
          name,
          requestedDate,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.requestOrderDateChange(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callRequestOrderDateChange();
    
    

### checkSignalZoneStateProgress(name)
    
    
    checkSignalZoneStateProgress(name: string): Promise<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.Zone, protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `signalZoneState()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.Zone](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.zone-class), [protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the zone.
       *  Format: `projects/{project}/locations/{location}/zones/{zone}`
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. The state signal to send for this zone. Either state_signal or
       *  provisioning_state_signal must be set, but not both.
       */
      // const stateSignal = {}
      /**
       *  Optional. The provisioning state signal to send for this zone. Either
       *  state_signal or provisioning_state_signal must be set, but not both.
       */
      // const provisioningStateSignal = {}
      /**
       *  Optional. The step being executed. Provides a finer grained status when the
       *  state_signal is FACTORY_TURNUP_CHECKS_STARTED or
       *  FACTORY_TURNUP_CHECKS_FAILED.
       */
      // const step = 'abc123'
      /**
       *  Optional. Additional details, such as an error message when state_signal is
       *  FACTORY_TURNUP_CHECKS_FAILED.
       */
      // const details = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callSignalZoneState() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.signalZoneState(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callSignalZoneState();
    
    

### checkSubmitOrderProgress(name)
    
    
    checkSubmitOrderProgress(name: string): Promise<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.Order, protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `submitOrder()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.Order](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.order-class), [protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the order.
       *  Format: `projects/{project}/locations/{location}/orders/{order}`
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. Type of this request. If unset, the request type is assumed to be
       *  `INFO_PENDING`.
       */
      // const type = {}
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callSubmitOrder() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.submitOrder(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callSubmitOrder();
    
    

### checkUpdateHardwareGroupProgress(name)
    
    
    checkUpdateHardwareGroupProgress(name: string): Promise<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup, protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `updateHardwareGroup()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.hardwaregroup-class), [protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A mask to specify the fields in the HardwareGroup to overwrite
       *  with this update. The fields specified in the update_mask are relative to
       *  the hardware group, not the full request. A field will be overwritten if it
       *  is in the mask. If you don't provide a mask then all fields will be
       *  overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The hardware group to update.
       */
      // const hardwareGroup = {}
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callUpdateHardwareGroup() {
        // Construct request
        const request = {
          updateMask,
          hardwareGroup,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.updateHardwareGroup(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateHardwareGroup();
    
    

### checkUpdateHardwareProgress(name)
    
    
    checkUpdateHardwareProgress(name: string): Promise<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.Hardware, protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `updateHardware()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.Hardware](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.hardware-class), [protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A mask to specify the fields in the Hardware to overwrite with
       *  this update. The fields specified in the update_mask are relative to the
       *  hardware, not the full request. A field will be overwritten if it is in the
       *  mask. If you don't provide a mask then all fields will be overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The hardware to update.
       */
      // const hardware = {}
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callUpdateHardware() {
        // Construct request
        const request = {
          updateMask,
          hardware,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.updateHardware(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateHardware();
    
    

### checkUpdateOrderProgress(name)
    
    
    checkUpdateOrderProgress(name: string): Promise<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.Order, protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `updateOrder()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.Order](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.order-class), [protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A mask to specify the fields in the Order to overwrite with this
       *  update. The fields specified in the update_mask are relative to the order,
       *  not the full request. A field will be overwritten if it is in the mask. If
       *  you don't provide a mask then all fields will be overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The order to update.
       */
      // const order = {}
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callUpdateOrder() {
        // Construct request
        const request = {
          updateMask,
          order,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.updateOrder(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateOrder();
    
    

### checkUpdateSiteProgress(name)
    
    
    checkUpdateSiteProgress(name: string): Promise<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.Site, protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `updateSite()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.Site](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.site), [protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A mask to specify the fields in the Site to overwrite with this
       *  update. The fields specified in the update_mask are relative to the site,
       *  not the full request. A field will be overwritten if it is in the mask. If
       *  you don't provide a mask then all fields will be overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The site to update.
       */
      // const site = {}
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callUpdateSite() {
        // Construct request
        const request = {
          updateMask,
          site,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.updateSite(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateSite();
    
    

### checkUpdateZoneProgress(name)
    
    
    checkUpdateZoneProgress(name: string): Promise<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.Zone, protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `updateZone()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.Zone](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.zone-class), [protos.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A mask to specify the fields in the Zone to overwrite with this
       *  update. The fields specified in the update_mask are relative to the zone,
       *  not the full request. A field will be overwritten if it is in the mask. If
       *  you don't provide a mask then all fields will be overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The zone to update.
       */
      // const zone = {}
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callUpdateZone() {
        // Construct request
        const request = {
          updateMask,
          zone,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.updateZone(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateZone();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### commentPath(project, location, order, comment)
    
    
    commentPath(project: string, location: string, order: string, comment: string): string;

Return a fully-qualified comment resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`order` |  `string`   
  
`comment` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### createComment(request, options)
    
    
    createComment(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.ICreateCommentRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IComment, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new comment on an order.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCommentRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icreatecommentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IComment](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icomment), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The order to create the comment on.
       *  Format: `projects/{project}/locations/{location}/orders/{order}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. ID used to uniquely identify the Comment within its parent scope.
       *  This field should contain at most 63 characters and must start with
       *  lowercase characters.
       *  Only lowercase characters, numbers and `-` are accepted.
       *  The `-` character cannot be the first or the last one.
       *  A system generated ID will be used if the field is not set.
       *  The comment.name field in the request will be ignored.
       */
      // const commentId = 'abc123'
      /**
       *  Required. The comment to create.
       */
      // const comment = {}
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callCreateComment() {
        // Construct request
        const request = {
          parent,
          comment,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.createComment(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateComment();
    
    

### createComment(request, options, callback)
    
    
    createComment(request: protos.google.cloud.gdchardwaremanagement.v1alpha.ICreateCommentRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IComment, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCommentRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icreatecommentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IComment](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icomment), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createComment(request, callback)
    
    
    createComment(request: protos.google.cloud.gdchardwaremanagement.v1alpha.ICreateCommentRequest, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IComment, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCommentRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icreatecommentrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IComment](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icomment), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createHardware(request, options)
    
    
    createHardware(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.ICreateHardwareRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates new hardware in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icreatehardwarerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardware), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location to create hardware in.
       *  Format: `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. ID used to uniquely identify the Hardware within its parent
       *  scope. This field should contain at most 63 characters and must start with
       *  lowercase characters.
       *  Only lowercase characters, numbers and `-` are accepted.
       *  The `-` character cannot be the first or the last one.
       *  A system generated ID will be used if the field is not set.
       *  The hardware.name field in the request will be ignored.
       */
      // const hardwareId = 'abc123'
      /**
       *  Required. The resource to create.
       */
      // const hardware = {}
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callCreateHardware() {
        // Construct request
        const request = {
          parent,
          hardware,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.createHardware(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateHardware();
    
    

### createHardware(request, options, callback)
    
    
    createHardware(request: protos.google.cloud.gdchardwaremanagement.v1alpha.ICreateHardwareRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icreatehardwarerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardware), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createHardware(request, callback)
    
    
    createHardware(request: protos.google.cloud.gdchardwaremanagement.v1alpha.ICreateHardwareRequest, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icreatehardwarerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardware), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createHardwareGroup(request, options)
    
    
    createHardwareGroup(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.ICreateHardwareGroupRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new hardware group in a given order.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateHardwareGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icreatehardwaregrouprequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardwaregroup), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The order to create the hardware group in.
       *  Format: `projects/{project}/locations/{location}/orders/{order}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. ID used to uniquely identify the HardwareGroup within its parent
       *  scope. This field should contain at most 63 characters and must start with
       *  lowercase characters.
       *  Only lowercase characters, numbers and `-` are accepted.
       *  The `-` character cannot be the first or the last one.
       *  A system generated ID will be used if the field is not set.
       *  The hardware_group.name field in the request will be ignored.
       */
      // const hardwareGroupId = 'abc123'
      /**
       *  Required. The hardware group to create.
       */
      // const hardwareGroup = {}
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callCreateHardwareGroup() {
        // Construct request
        const request = {
          parent,
          hardwareGroup,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.createHardwareGroup(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateHardwareGroup();
    
    

### createHardwareGroup(request, options, callback)
    
    
    createHardwareGroup(request: protos.google.cloud.gdchardwaremanagement.v1alpha.ICreateHardwareGroupRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateHardwareGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icreatehardwaregrouprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardwaregroup), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createHardwareGroup(request, callback)
    
    
    createHardwareGroup(request: protos.google.cloud.gdchardwaremanagement.v1alpha.ICreateHardwareGroupRequest, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateHardwareGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icreatehardwaregrouprequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardwaregroup), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createOrder(request, options)
    
    
    createOrder(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.ICreateOrderRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new order in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateOrderRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icreateorderrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location to create the order in.
       *  Format: `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. ID used to uniquely identify the Order within its parent scope.
       *  This field should contain at most 63 characters and must start with
       *  lowercase characters.
       *  Only lowercase characters, numbers and `-` are accepted.
       *  The `-` character cannot be the first or the last one.
       *  A system generated ID will be used if the field is not set.
       *  The order.name field in the request will be ignored.
       */
      // const orderId = 'abc123'
      /**
       *  Required. The order to create.
       */
      // const order = {}
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callCreateOrder() {
        // Construct request
        const request = {
          parent,
          order,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.createOrder(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateOrder();
    
    

### createOrder(request, options, callback)
    
    
    createOrder(request: protos.google.cloud.gdchardwaremanagement.v1alpha.ICreateOrderRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateOrderRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icreateorderrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createOrder(request, callback)
    
    
    createOrder(request: protos.google.cloud.gdchardwaremanagement.v1alpha.ICreateOrderRequest, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateOrderRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icreateorderrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSite(request, options)
    
    
    createSite(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.ICreateSiteRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.ISite, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new site in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icreatesiterequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.ISite](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isite), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location to create the site in.
       *  Format: `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. ID used to uniquely identify the Site within its parent scope.
       *  This field should contain at most 63 characters and must start with
       *  lowercase characters.
       *  Only lowercase characters, numbers and `-` are accepted.
       *  The `-` character cannot be the first or the last one.
       *  A system generated ID will be used if the field is not set.
       *  The site.name field in the request will be ignored.
       */
      // const siteId = 'abc123'
      /**
       *  Required. The site to create.
       */
      // const site = {}
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callCreateSite() {
        // Construct request
        const request = {
          parent,
          site,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.createSite(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateSite();
    
    

### createSite(request, options, callback)
    
    
    createSite(request: protos.google.cloud.gdchardwaremanagement.v1alpha.ICreateSiteRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.ISite, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icreatesiterequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.ISite](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isite), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSite(request, callback)
    
    
    createSite(request: protos.google.cloud.gdchardwaremanagement.v1alpha.ICreateSiteRequest, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.ISite, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icreatesiterequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.ISite](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isite), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createZone(request, options)
    
    
    createZone(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.ICreateZoneRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IZone, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new zone in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icreatezonerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IZone](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.izone), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location to create the zone in.
       *  Format: `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. ID used to uniquely identify the Zone within its parent scope.
       *  This field should contain at most 63 characters and must start with
       *  lowercase characters.
       *  Only lowercase characters, numbers and `-` are accepted.
       *  The `-` character cannot be the first or the last one.
       *  A system generated ID will be used if the field is not set.
       *  The zone.name field in the request will be ignored.
       */
      // const zoneId = 'abc123'
      /**
       *  Required. The zone to create.
       */
      // const zone = {}
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callCreateZone() {
        // Construct request
        const request = {
          parent,
          zone,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.createZone(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateZone();
    
    

### createZone(request, options, callback)
    
    
    createZone(request: protos.google.cloud.gdchardwaremanagement.v1alpha.ICreateZoneRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IZone, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icreatezonerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IZone](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.izone), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createZone(request, callback)
    
    
    createZone(request: protos.google.cloud.gdchardwaremanagement.v1alpha.ICreateZoneRequest, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IZone, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icreatezonerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IZone](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.izone), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteHardware(request, options)
    
    
    deleteHardware(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IDeleteHardwareRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes hardware.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ideletehardwarerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.iempty), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the hardware.
       *  Format: `projects/{project}/locations/{location}/hardware/{hardware}`
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callDeleteHardware() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.deleteHardware(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteHardware();
    
    

### deleteHardware(request, options, callback)
    
    
    deleteHardware(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IDeleteHardwareRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ideletehardwarerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.iempty), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteHardware(request, callback)
    
    
    deleteHardware(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IDeleteHardwareRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ideletehardwarerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.iempty), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteHardwareGroup(request, options)
    
    
    deleteHardwareGroup(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IDeleteHardwareGroupRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a hardware group.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteHardwareGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ideletehardwaregrouprequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.iempty), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the hardware group.
       *  Format:
       *  `projects/{project}/locations/{location}/orders/{order}/hardwareGroups/{hardware_group}`
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callDeleteHardwareGroup() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.deleteHardwareGroup(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteHardwareGroup();
    
    

### deleteHardwareGroup(request, options, callback)
    
    
    deleteHardwareGroup(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IDeleteHardwareGroupRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteHardwareGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ideletehardwaregrouprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.iempty), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteHardwareGroup(request, callback)
    
    
    deleteHardwareGroup(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IDeleteHardwareGroupRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteHardwareGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ideletehardwaregrouprequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.iempty), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### deleteOrder(request, options)
    
    
    deleteOrder(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IDeleteOrderRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes an order.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteOrderRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ideleteorderrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.iempty), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the order.
       *  Format: `projects/{project}/locations/{location}/orders/{order}`
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. An option to delete any nested resources in the Order, such as a
       *  HardwareGroup. If true, any nested resources for this Order will also be
       *  deleted. Otherwise, the request will only succeed if the Order has no
       *  nested resources.
       */
      // const force = true
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callDeleteOrder() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.deleteOrder(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteOrder();
    
    

### deleteOrder(request, options, callback)
    
    
    deleteOrder(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IDeleteOrderRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteOrderRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ideleteorderrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.iempty), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteOrder(request, callback)
    
    
    deleteOrder(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IDeleteOrderRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteOrderRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ideleteorderrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.iempty), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSite(request, options)
    
    
    deleteSite(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IDeleteSiteRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a site.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ideletesiterequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.iempty), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the site.
       *  Format: `projects/{project}/locations/{location}/sites/{site}`
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callDeleteSite() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.deleteSite(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteSite();
    
    

### deleteSite(request, options, callback)
    
    
    deleteSite(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IDeleteSiteRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ideletesiterequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.iempty), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSite(request, callback)
    
    
    deleteSite(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IDeleteSiteRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ideletesiterequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.iempty), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteZone(request, options)
    
    
    deleteZone(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IDeleteZoneRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a zone.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ideletezonerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.iempty), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the zone.
       *  Format: `projects/{project}/locations/{location}/zones/{zone}`
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callDeleteZone() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.deleteZone(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteZone();
    
    

### deleteZone(request, options, callback)
    
    
    deleteZone(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IDeleteZoneRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ideletezonerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.iempty), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteZone(request, callback)
    
    
    deleteZone(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IDeleteZoneRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ideletezonerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.protobuf.iempty), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getChangeLogEntry(request, options)
    
    
    getChangeLogEntry(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetChangeLogEntryRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gdchardwaremanagement.v1alpha.IChangeLogEntry,
            (protos.google.cloud.gdchardwaremanagement.v1alpha.IGetChangeLogEntryRequest | undefined),
            {} | undefined
        ]>;

Gets details of a change to an order.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetChangeLogEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetchangelogentryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gdchardwaremanagement.v1alpha.IChangeLogEntry](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ichangelogentry), ([protos.google.cloud.gdchardwaremanagement.v1alpha.IGetChangeLogEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetchangelogentryrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ChangeLogEntry](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.changelogentry). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the change log entry.
       *  Format:
       *  `projects/{project}/locations/{location}/orders/{order}/changeLogEntries/{change_log_entry}`
       */
      // const name = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callGetChangeLogEntry() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await gdchardwaremanagementClient.getChangeLogEntry(request);
        console.log(response);
      }
    
      callGetChangeLogEntry();
    
    

### getChangeLogEntry(request, options, callback)
    
    
    getChangeLogEntry(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetChangeLogEntryRequest, options: CallOptions, callback: Callback<protos.google.cloud.gdchardwaremanagement.v1alpha.IChangeLogEntry, protos.google.cloud.gdchardwaremanagement.v1alpha.IGetChangeLogEntryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetChangeLogEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetchangelogentryrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IChangeLogEntry](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ichangelogentry), [protos.google.cloud.gdchardwaremanagement.v1alpha.IGetChangeLogEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetchangelogentryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getChangeLogEntry(request, callback)
    
    
    getChangeLogEntry(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetChangeLogEntryRequest, callback: Callback<protos.google.cloud.gdchardwaremanagement.v1alpha.IChangeLogEntry, protos.google.cloud.gdchardwaremanagement.v1alpha.IGetChangeLogEntryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetChangeLogEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetchangelogentryrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IChangeLogEntry](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ichangelogentry), [protos.google.cloud.gdchardwaremanagement.v1alpha.IGetChangeLogEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetchangelogentryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getComment(request, options)
    
    
    getComment(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetCommentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gdchardwaremanagement.v1alpha.IComment,
            (protos.google.cloud.gdchardwaremanagement.v1alpha.IGetCommentRequest | undefined),
            {} | undefined
        ]>;

Gets the content of a comment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCommentRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetcommentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gdchardwaremanagement.v1alpha.IComment](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icomment), ([protos.google.cloud.gdchardwaremanagement.v1alpha.IGetCommentRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetcommentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Comment](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.comment). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the comment.
       *  Format:
       *  `projects/{project}/locations/{location}/orders/{order}/comments/{comment}`
       */
      // const name = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callGetComment() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await gdchardwaremanagementClient.getComment(request);
        console.log(response);
      }
    
      callGetComment();
    
    

### getComment(request, options, callback)
    
    
    getComment(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetCommentRequest, options: CallOptions, callback: Callback<protos.google.cloud.gdchardwaremanagement.v1alpha.IComment, protos.google.cloud.gdchardwaremanagement.v1alpha.IGetCommentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCommentRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetcommentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IComment](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icomment), [protos.google.cloud.gdchardwaremanagement.v1alpha.IGetCommentRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetcommentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getComment(request, callback)
    
    
    getComment(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetCommentRequest, callback: Callback<protos.google.cloud.gdchardwaremanagement.v1alpha.IComment, protos.google.cloud.gdchardwaremanagement.v1alpha.IGetCommentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCommentRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetcommentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IComment](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icomment), [protos.google.cloud.gdchardwaremanagement.v1alpha.IGetCommentRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetcommentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getHardware(request, options)
    
    
    getHardware(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetHardwareRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware,
            (protos.google.cloud.gdchardwaremanagement.v1alpha.IGetHardwareRequest | undefined),
            {} | undefined
        ]>;

Gets hardware details.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igethardwarerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardware), ([protos.google.cloud.gdchardwaremanagement.v1alpha.IGetHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igethardwarerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the hardware.
       *  Format: `projects/{project}/locations/{location}/hardware/{hardware}`
       */
      // const name = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callGetHardware() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await gdchardwaremanagementClient.getHardware(request);
        console.log(response);
      }
    
      callGetHardware();
    
    

### getHardware(request, options, callback)
    
    
    getHardware(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetHardwareRequest, options: CallOptions, callback: Callback<protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware, protos.google.cloud.gdchardwaremanagement.v1alpha.IGetHardwareRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igethardwarerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardware), [protos.google.cloud.gdchardwaremanagement.v1alpha.IGetHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igethardwarerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getHardware(request, callback)
    
    
    getHardware(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetHardwareRequest, callback: Callback<protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware, protos.google.cloud.gdchardwaremanagement.v1alpha.IGetHardwareRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igethardwarerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardware), [protos.google.cloud.gdchardwaremanagement.v1alpha.IGetHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igethardwarerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getHardwareGroup(request, options)
    
    
    getHardwareGroup(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetHardwareGroupRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup,
            (protos.google.cloud.gdchardwaremanagement.v1alpha.IGetHardwareGroupRequest | undefined),
            {} | undefined
        ]>;

Gets details of a hardware group.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetHardwareGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igethardwaregrouprequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardwaregroup), ([protos.google.cloud.gdchardwaremanagement.v1alpha.IGetHardwareGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igethardwaregrouprequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the hardware group.
       *  Format:
       *  `projects/{project}/locations/{location}/orders/{order}/hardwareGroups/{hardware_group}`
       */
      // const name = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callGetHardwareGroup() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await gdchardwaremanagementClient.getHardwareGroup(request);
        console.log(response);
      }
    
      callGetHardwareGroup();
    
    

### getHardwareGroup(request, options, callback)
    
    
    getHardwareGroup(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetHardwareGroupRequest, options: CallOptions, callback: Callback<protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup, protos.google.cloud.gdchardwaremanagement.v1alpha.IGetHardwareGroupRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetHardwareGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igethardwaregrouprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardwaregroup), [protos.google.cloud.gdchardwaremanagement.v1alpha.IGetHardwareGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igethardwaregrouprequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getHardwareGroup(request, callback)
    
    
    getHardwareGroup(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetHardwareGroupRequest, callback: Callback<protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup, protos.google.cloud.gdchardwaremanagement.v1alpha.IGetHardwareGroupRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetHardwareGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igethardwaregrouprequest)`   
  
`callback` |  `Callback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardwaregroup), [protos.google.cloud.gdchardwaremanagement.v1alpha.IGetHardwareGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igethardwaregrouprequest) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.operation)]>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    const name = '';
    const [response] = await client.getOperation({name});
    // doThingsWith(response)
    

### getOrder(request, options)
    
    
    getOrder(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetOrderRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder,
            (protos.google.cloud.gdchardwaremanagement.v1alpha.IGetOrderRequest | undefined),
            {} | undefined
        ]>;

Gets details of an order.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetOrderRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetorderrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder), ([protos.google.cloud.gdchardwaremanagement.v1alpha.IGetOrderRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetorderrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the resource
       */
      // const name = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callGetOrder() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await gdchardwaremanagementClient.getOrder(request);
        console.log(response);
      }
    
      callGetOrder();
    
    

### getOrder(request, options, callback)
    
    
    getOrder(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetOrderRequest, options: CallOptions, callback: Callback<protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder, protos.google.cloud.gdchardwaremanagement.v1alpha.IGetOrderRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetOrderRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetorderrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder), [protos.google.cloud.gdchardwaremanagement.v1alpha.IGetOrderRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetorderrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getOrder(request, callback)
    
    
    getOrder(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetOrderRequest, callback: Callback<protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder, protos.google.cloud.gdchardwaremanagement.v1alpha.IGetOrderRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetOrderRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetorderrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder), [protos.google.cloud.gdchardwaremanagement.v1alpha.IGetOrderRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetorderrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### getSite(request, options)
    
    
    getSite(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetSiteRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gdchardwaremanagement.v1alpha.ISite,
            (protos.google.cloud.gdchardwaremanagement.v1alpha.IGetSiteRequest | undefined),
            {} | undefined
        ]>;

Gets details of a site.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetsiterequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gdchardwaremanagement.v1alpha.ISite](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isite), ([protos.google.cloud.gdchardwaremanagement.v1alpha.IGetSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetsiterequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Site](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.site). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the site.
       *  Format: `projects/{project}/locations/{location}/sites/{site}`
       */
      // const name = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callGetSite() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await gdchardwaremanagementClient.getSite(request);
        console.log(response);
      }
    
      callGetSite();
    
    

### getSite(request, options, callback)
    
    
    getSite(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetSiteRequest, options: CallOptions, callback: Callback<protos.google.cloud.gdchardwaremanagement.v1alpha.ISite, protos.google.cloud.gdchardwaremanagement.v1alpha.IGetSiteRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetsiterequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.gdchardwaremanagement.v1alpha.ISite](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isite), [protos.google.cloud.gdchardwaremanagement.v1alpha.IGetSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetsiterequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSite(request, callback)
    
    
    getSite(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetSiteRequest, callback: Callback<protos.google.cloud.gdchardwaremanagement.v1alpha.ISite, protos.google.cloud.gdchardwaremanagement.v1alpha.IGetSiteRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetsiterequest)`   
  
`callback` |  `Callback<[protos.google.cloud.gdchardwaremanagement.v1alpha.ISite](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isite), [protos.google.cloud.gdchardwaremanagement.v1alpha.IGetSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetsiterequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSku(request, options)
    
    
    getSku(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetSkuRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gdchardwaremanagement.v1alpha.ISku,
            (protos.google.cloud.gdchardwaremanagement.v1alpha.IGetSkuRequest | undefined),
            {} | undefined
        ]>;

Gets details of an SKU.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSkuRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetskurequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gdchardwaremanagement.v1alpha.ISku](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isku), ([protos.google.cloud.gdchardwaremanagement.v1alpha.IGetSkuRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetskurequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the SKU.
       *  Format: `projects/{project}/locations/{location}/skus/{sku}`
       */
      // const name = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callGetSku() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await gdchardwaremanagementClient.getSku(request);
        console.log(response);
      }
    
      callGetSku();
    
    

### getSku(request, options, callback)
    
    
    getSku(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetSkuRequest, options: CallOptions, callback: Callback<protos.google.cloud.gdchardwaremanagement.v1alpha.ISku, protos.google.cloud.gdchardwaremanagement.v1alpha.IGetSkuRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSkuRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetskurequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.gdchardwaremanagement.v1alpha.ISku](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isku), [protos.google.cloud.gdchardwaremanagement.v1alpha.IGetSkuRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetskurequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSku(request, callback)
    
    
    getSku(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetSkuRequest, callback: Callback<protos.google.cloud.gdchardwaremanagement.v1alpha.ISku, protos.google.cloud.gdchardwaremanagement.v1alpha.IGetSkuRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSkuRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetskurequest)`   
  
`callback` |  `Callback<[protos.google.cloud.gdchardwaremanagement.v1alpha.ISku](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isku), [protos.google.cloud.gdchardwaremanagement.v1alpha.IGetSkuRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetskurequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getZone(request, options)
    
    
    getZone(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetZoneRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gdchardwaremanagement.v1alpha.IZone,
            (protos.google.cloud.gdchardwaremanagement.v1alpha.IGetZoneRequest | undefined),
            {} | undefined
        ]>;

Gets details of a zone.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetzonerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gdchardwaremanagement.v1alpha.IZone](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.izone), ([protos.google.cloud.gdchardwaremanagement.v1alpha.IGetZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetzonerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the zone.
       *  Format: `projects/{project}/locations/{location}/zones/{zone}`
       */
      // const name = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callGetZone() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await gdchardwaremanagementClient.getZone(request);
        console.log(response);
      }
    
      callGetZone();
    
    

### getZone(request, options, callback)
    
    
    getZone(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetZoneRequest, options: CallOptions, callback: Callback<protos.google.cloud.gdchardwaremanagement.v1alpha.IZone, protos.google.cloud.gdchardwaremanagement.v1alpha.IGetZoneRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetzonerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IZone](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.izone), [protos.google.cloud.gdchardwaremanagement.v1alpha.IGetZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetzonerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getZone(request, callback)
    
    
    getZone(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IGetZoneRequest, callback: Callback<protos.google.cloud.gdchardwaremanagement.v1alpha.IZone, protos.google.cloud.gdchardwaremanagement.v1alpha.IGetZoneRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetzonerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IZone](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.izone), [protos.google.cloud.gdchardwaremanagement.v1alpha.IGetZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.igetzonerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### hardwareGroupPath(project, location, order, hardwareGroup)
    
    
    hardwareGroupPath(project: string, location: string, order: string, hardwareGroup: string): string;

Return a fully-qualified hardwareGroup resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`order` |  `string`   
  
`hardwareGroup` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### hardwarePath(project, location, hardware)
    
    
    hardwarePath(project: string, location: string, hardware: string): string;

Return a fully-qualified hardware resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`hardware` |  `string`   
  
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
  
### listChangeLogEntries(request, options)
    
    
    listChangeLogEntries(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListChangeLogEntriesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gdchardwaremanagement.v1alpha.IChangeLogEntry[],
            protos.google.cloud.gdchardwaremanagement.v1alpha.IListChangeLogEntriesRequest | null,
            protos.google.cloud.gdchardwaremanagement.v1alpha.IListChangeLogEntriesResponse
        ]>;

Lists the changes made to an order.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListChangeLogEntriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistchangelogentriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gdchardwaremanagement.v1alpha.IChangeLogEntry](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ichangelogentry)[], [protos.google.cloud.gdchardwaremanagement.v1alpha.IListChangeLogEntriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistchangelogentriesrequest) | null, [protos.google.cloud.gdchardwaremanagement.v1alpha.IListChangeLogEntriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistchangelogentriesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [ChangeLogEntry](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.changelogentry). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listChangeLogEntriesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listChangeLogEntries(request, options, callback)
    
    
    listChangeLogEntries(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IListChangeLogEntriesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.gdchardwaremanagement.v1alpha.IListChangeLogEntriesRequest, protos.google.cloud.gdchardwaremanagement.v1alpha.IListChangeLogEntriesResponse | null | undefined, protos.google.cloud.gdchardwaremanagement.v1alpha.IChangeLogEntry>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListChangeLogEntriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistchangelogentriesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IListChangeLogEntriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistchangelogentriesrequest), [protos.google.cloud.gdchardwaremanagement.v1alpha.IListChangeLogEntriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistchangelogentriesresponse) | null | undefined, [protos.google.cloud.gdchardwaremanagement.v1alpha.IChangeLogEntry](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ichangelogentry)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listChangeLogEntries(request, callback)
    
    
    listChangeLogEntries(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IListChangeLogEntriesRequest, callback: PaginationCallback<protos.google.cloud.gdchardwaremanagement.v1alpha.IListChangeLogEntriesRequest, protos.google.cloud.gdchardwaremanagement.v1alpha.IListChangeLogEntriesResponse | null | undefined, protos.google.cloud.gdchardwaremanagement.v1alpha.IChangeLogEntry>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListChangeLogEntriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistchangelogentriesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IListChangeLogEntriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistchangelogentriesrequest), [protos.google.cloud.gdchardwaremanagement.v1alpha.IListChangeLogEntriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistchangelogentriesresponse) | null | undefined, [protos.google.cloud.gdchardwaremanagement.v1alpha.IChangeLogEntry](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ichangelogentry)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listChangeLogEntriesAsync(request, options)
    
    
    listChangeLogEntriesAsync(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListChangeLogEntriesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.gdchardwaremanagement.v1alpha.IChangeLogEntry>;

Equivalent to `listChangeLogEntries`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListChangeLogEntriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistchangelogentriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.gdchardwaremanagement.v1alpha.IChangeLogEntry](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ichangelogentry)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [ChangeLogEntry](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.changelogentry). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The order to list change log entries for.
       *  Format: `projects/{project}/locations/{location}/orders/{order}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results the server should return.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filtering condition. See AIP-160 (https://google.aip.dev/160).
       */
      // const filter = 'abc123'
      /**
       *  Optional. Hint for how to order the results.
       */
      // const orderBy = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callListChangeLogEntries() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = gdchardwaremanagementClient.[listChangeLogEntriesAsync](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/v1alpha.gdchardwaremanagementclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListChangeLogEntries();
    
    

### listChangeLogEntriesStream(request, options)
    
    
    listChangeLogEntriesStream(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListChangeLogEntriesRequest, options?: CallOptions): Transform;

Equivalent to `listChangeLogEntries`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListChangeLogEntriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistchangelogentriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [ChangeLogEntry](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.changelogentry) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listChangeLogEntriesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listComments(request, options)
    
    
    listComments(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListCommentsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gdchardwaremanagement.v1alpha.IComment[],
            protos.google.cloud.gdchardwaremanagement.v1alpha.IListCommentsRequest | null,
            protos.google.cloud.gdchardwaremanagement.v1alpha.IListCommentsResponse
        ]>;

Lists the comments on an order.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCommentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistcommentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gdchardwaremanagement.v1alpha.IComment](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icomment)[], [protos.google.cloud.gdchardwaremanagement.v1alpha.IListCommentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistcommentsrequest) | null, [protos.google.cloud.gdchardwaremanagement.v1alpha.IListCommentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistcommentsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Comment](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.comment). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listCommentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listComments(request, options, callback)
    
    
    listComments(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IListCommentsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.gdchardwaremanagement.v1alpha.IListCommentsRequest, protos.google.cloud.gdchardwaremanagement.v1alpha.IListCommentsResponse | null | undefined, protos.google.cloud.gdchardwaremanagement.v1alpha.IComment>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCommentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistcommentsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IListCommentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistcommentsrequest), [protos.google.cloud.gdchardwaremanagement.v1alpha.IListCommentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistcommentsresponse) | null | undefined, [protos.google.cloud.gdchardwaremanagement.v1alpha.IComment](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icomment)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listComments(request, callback)
    
    
    listComments(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IListCommentsRequest, callback: PaginationCallback<protos.google.cloud.gdchardwaremanagement.v1alpha.IListCommentsRequest, protos.google.cloud.gdchardwaremanagement.v1alpha.IListCommentsResponse | null | undefined, protos.google.cloud.gdchardwaremanagement.v1alpha.IComment>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCommentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistcommentsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IListCommentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistcommentsrequest), [protos.google.cloud.gdchardwaremanagement.v1alpha.IListCommentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistcommentsresponse) | null | undefined, [protos.google.cloud.gdchardwaremanagement.v1alpha.IComment](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icomment)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCommentsAsync(request, options)
    
    
    listCommentsAsync(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListCommentsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.gdchardwaremanagement.v1alpha.IComment>;

Equivalent to `listComments`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCommentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistcommentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.gdchardwaremanagement.v1alpha.IComment](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icomment)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Comment](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.comment). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The order to list comments on.
       *  Format: `projects/{project}/locations/{location}/orders/{order}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results the server should return.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filtering condition. See AIP-160 (https://google.aip.dev/160).
       */
      // const filter = 'abc123'
      /**
       *  Optional. Hint for how to order the results.
       */
      // const orderBy = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callListComments() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = gdchardwaremanagementClient.[listCommentsAsync](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/v1alpha.gdchardwaremanagementclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListComments();
    
    

### listCommentsStream(request, options)
    
    
    listCommentsStream(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListCommentsRequest, options?: CallOptions): Transform;

Equivalent to `listComments`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCommentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistcommentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Comment](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.comment) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listCommentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listHardware(request, options)
    
    
    listHardware(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware[],
            protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareRequest | null,
            protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareResponse
        ]>;

Lists hardware in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwarerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardware)[], [protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwarerequest) | null, [protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwareresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listHardwareAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listHardware(request, options, callback)
    
    
    listHardware(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareRequest, protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareResponse | null | undefined, protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwarerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwarerequest), [protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwareresponse) | null | undefined, [protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardware)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listHardware(request, callback)
    
    
    listHardware(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareRequest, callback: PaginationCallback<protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareRequest, protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareResponse | null | undefined, protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwarerequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwarerequest), [protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwareresponse) | null | undefined, [protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardware)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listHardwareAsync(request, options)
    
    
    listHardwareAsync(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware>;

Equivalent to `listHardware`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwarerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardware)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location to list hardware in.
       *  Format: `projects/{project}/locations/{location}`
       *  To list hardware across all locations, substitute `-` (the hyphen or
       *  dash character) for the location and check the unreachable field in
       *  the response message.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results the server should return.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filtering condition. See AIP-160 (https://google.aip.dev/160).
       */
      // const filter = 'abc123'
      /**
       *  Optional. Hint for how to order the results.
       */
      // const orderBy = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callListHardware() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = gdchardwaremanagementClient.[listHardwareAsync](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/v1alpha.gdchardwaremanagementclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListHardware();
    
    

### listHardwareGroups(request, options)
    
    
    listHardwareGroups(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareGroupsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup[],
            protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareGroupsRequest | null,
            protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareGroupsResponse
        ]>;

Lists hardware groups in a given order.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListHardwareGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwaregroupsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardwaregroup)[], [protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwaregroupsrequest) | null, [protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwaregroupsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listHardwareGroupsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listHardwareGroups(request, options, callback)
    
    
    listHardwareGroups(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareGroupsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareGroupsRequest, protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareGroupsResponse | null | undefined, protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListHardwareGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwaregroupsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwaregroupsrequest), [protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwaregroupsresponse) | null | undefined, [protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardwaregroup)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listHardwareGroups(request, callback)
    
    
    listHardwareGroups(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareGroupsRequest, callback: PaginationCallback<protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareGroupsRequest, protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareGroupsResponse | null | undefined, protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListHardwareGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwaregroupsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwaregroupsrequest), [protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwaregroupsresponse) | null | undefined, [protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardwaregroup)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listHardwareGroupsAsync(request, options)
    
    
    listHardwareGroupsAsync(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareGroupsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup>;

Equivalent to `listHardwareGroups`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListHardwareGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwaregroupsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardwaregroup)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The order to list hardware groups in.
       *  Format: `projects/{project}/locations/{location}/orders/{order}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results the server should return.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filtering condition. See AIP-160 (https://google.aip.dev/160).
       */
      // const filter = 'abc123'
      /**
       *  Optional. Hint for how to order the results.
       */
      // const orderBy = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callListHardwareGroups() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = gdchardwaremanagementClient.[listHardwareGroupsAsync](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/v1alpha.gdchardwaremanagementclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListHardwareGroups();
    
    

### listHardwareGroupsStream(request, options)
    
    
    listHardwareGroupsStream(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareGroupsRequest, options?: CallOptions): Transform;

Equivalent to `listHardwareGroups`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListHardwareGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwaregroupsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listHardwareGroupsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listHardwareStream(request, options)
    
    
    listHardwareStream(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListHardwareRequest, options?: CallOptions): Transform;

Equivalent to `listHardware`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilisthardwarerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listHardwareAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
**Example**
    
    
    const client = longrunning.operationsClient();
    for await (const response of client.listOperationsAsync(request));
    // doThingsWith(response)
    

### listOrders(request, options)
    
    
    listOrders(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListOrdersRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder[],
            protos.google.cloud.gdchardwaremanagement.v1alpha.IListOrdersRequest | null,
            protos.google.cloud.gdchardwaremanagement.v1alpha.IListOrdersResponse
        ]>;

Lists orders in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOrdersRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistordersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder)[], [protos.google.cloud.gdchardwaremanagement.v1alpha.IListOrdersRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistordersrequest) | null, [protos.google.cloud.gdchardwaremanagement.v1alpha.IListOrdersResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistordersresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listOrdersAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listOrders(request, options, callback)
    
    
    listOrders(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IListOrdersRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.gdchardwaremanagement.v1alpha.IListOrdersRequest, protos.google.cloud.gdchardwaremanagement.v1alpha.IListOrdersResponse | null | undefined, protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOrdersRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistordersrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IListOrdersRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistordersrequest), [protos.google.cloud.gdchardwaremanagement.v1alpha.IListOrdersResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistordersresponse) | null | undefined, [protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listOrders(request, callback)
    
    
    listOrders(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IListOrdersRequest, callback: PaginationCallback<protos.google.cloud.gdchardwaremanagement.v1alpha.IListOrdersRequest, protos.google.cloud.gdchardwaremanagement.v1alpha.IListOrdersResponse | null | undefined, protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOrdersRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistordersrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IListOrdersRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistordersrequest), [protos.google.cloud.gdchardwaremanagement.v1alpha.IListOrdersResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistordersresponse) | null | undefined, [protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listOrdersAsync(request, options)
    
    
    listOrdersAsync(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListOrdersRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder>;

Equivalent to `listOrders`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOrdersRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistordersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location to list orders in.
       *  Format: `projects/{project}/locations/{location}`
       *  To list orders across all locations, substitute `-` (the hyphen or
       *  dash character) for the location and check the unreachable field in
       *  the response message.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results the server should return.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filtering condition. See AIP-160 (https://google.aip.dev/160).
       */
      // const filter = 'abc123'
      /**
       *  Optional. Hint for how to order the results.
       */
      // const orderBy = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callListOrders() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = gdchardwaremanagementClient.[listOrdersAsync](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/v1alpha.gdchardwaremanagementclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListOrders();
    
    

### listOrdersStream(request, options)
    
    
    listOrdersStream(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListOrdersRequest, options?: CallOptions): Transform;

Equivalent to `listOrders`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOrdersRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistordersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listOrdersAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listSites(request, options)
    
    
    listSites(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListSitesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gdchardwaremanagement.v1alpha.ISite[],
            protos.google.cloud.gdchardwaremanagement.v1alpha.IListSitesRequest | null,
            protos.google.cloud.gdchardwaremanagement.v1alpha.IListSitesResponse
        ]>;

Lists sites in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistsitesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gdchardwaremanagement.v1alpha.ISite](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isite)[], [protos.google.cloud.gdchardwaremanagement.v1alpha.IListSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistsitesrequest) | null, [protos.google.cloud.gdchardwaremanagement.v1alpha.IListSitesResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistsitesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Site](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.site). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listSitesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listSites(request, options, callback)
    
    
    listSites(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IListSitesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.gdchardwaremanagement.v1alpha.IListSitesRequest, protos.google.cloud.gdchardwaremanagement.v1alpha.IListSitesResponse | null | undefined, protos.google.cloud.gdchardwaremanagement.v1alpha.ISite>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistsitesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IListSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistsitesrequest), [protos.google.cloud.gdchardwaremanagement.v1alpha.IListSitesResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistsitesresponse) | null | undefined, [protos.google.cloud.gdchardwaremanagement.v1alpha.ISite](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isite)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSites(request, callback)
    
    
    listSites(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IListSitesRequest, callback: PaginationCallback<protos.google.cloud.gdchardwaremanagement.v1alpha.IListSitesRequest, protos.google.cloud.gdchardwaremanagement.v1alpha.IListSitesResponse | null | undefined, protos.google.cloud.gdchardwaremanagement.v1alpha.ISite>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistsitesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IListSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistsitesrequest), [protos.google.cloud.gdchardwaremanagement.v1alpha.IListSitesResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistsitesresponse) | null | undefined, [protos.google.cloud.gdchardwaremanagement.v1alpha.ISite](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isite)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSitesAsync(request, options)
    
    
    listSitesAsync(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListSitesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.gdchardwaremanagement.v1alpha.ISite>;

Equivalent to `listSites`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistsitesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.gdchardwaremanagement.v1alpha.ISite](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isite)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Site](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.site). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location to list sites in.
       *  Format: `projects/{project}/locations/{location}`
       *  To list sites across all locations, substitute `-` (the hyphen or
       *  dash character) for the location and check the unreachable field in
       *  the response message.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results the server should return.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filtering condition. See AIP-160 (https://google.aip.dev/160).
       */
      // const filter = 'abc123'
      /**
       *  Optional. Hint for how to order the results.
       */
      // const orderBy = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callListSites() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = gdchardwaremanagementClient.[listSitesAsync](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/v1alpha.gdchardwaremanagementclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListSites();
    
    

### listSitesStream(request, options)
    
    
    listSitesStream(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListSitesRequest, options?: CallOptions): Transform;

Equivalent to `listSites`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistsitesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Site](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.site) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listSitesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listSkus(request, options)
    
    
    listSkus(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListSkusRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gdchardwaremanagement.v1alpha.ISku[],
            protos.google.cloud.gdchardwaremanagement.v1alpha.IListSkusRequest | null,
            protos.google.cloud.gdchardwaremanagement.v1alpha.IListSkusResponse
        ]>;

Lists SKUs for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistskusrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gdchardwaremanagement.v1alpha.ISku](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isku)[], [protos.google.cloud.gdchardwaremanagement.v1alpha.IListSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistskusrequest) | null, [protos.google.cloud.gdchardwaremanagement.v1alpha.IListSkusResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistskusresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listSkusAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listSkus(request, options, callback)
    
    
    listSkus(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IListSkusRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.gdchardwaremanagement.v1alpha.IListSkusRequest, protos.google.cloud.gdchardwaremanagement.v1alpha.IListSkusResponse | null | undefined, protos.google.cloud.gdchardwaremanagement.v1alpha.ISku>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistskusrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IListSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistskusrequest), [protos.google.cloud.gdchardwaremanagement.v1alpha.IListSkusResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistskusresponse) | null | undefined, [protos.google.cloud.gdchardwaremanagement.v1alpha.ISku](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isku)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSkus(request, callback)
    
    
    listSkus(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IListSkusRequest, callback: PaginationCallback<protos.google.cloud.gdchardwaremanagement.v1alpha.IListSkusRequest, protos.google.cloud.gdchardwaremanagement.v1alpha.IListSkusResponse | null | undefined, protos.google.cloud.gdchardwaremanagement.v1alpha.ISku>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistskusrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IListSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistskusrequest), [protos.google.cloud.gdchardwaremanagement.v1alpha.IListSkusResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistskusresponse) | null | undefined, [protos.google.cloud.gdchardwaremanagement.v1alpha.ISku](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isku)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSkusAsync(request, options)
    
    
    listSkusAsync(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListSkusRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.gdchardwaremanagement.v1alpha.ISku>;

Equivalent to `listSkus`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistskusrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.gdchardwaremanagement.v1alpha.ISku](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isku)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location to list SKUs in.
       *  Format: `projects/{project}/locations/{location}`
       *  To list SKUs across all locations, substitute `-` (the hyphen or
       *  dash character) for the location and check the unreachable field in
       *  the response message.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results the server should return.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filtering condition. See AIP-160 (https://google.aip.dev/160).
       */
      // const filter = 'abc123'
      /**
       *  Optional. Hint for how to order the results.
       */
      // const orderBy = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callListSkus() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = gdchardwaremanagementClient.[listSkusAsync](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/v1alpha.gdchardwaremanagementclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListSkus();
    
    

### listSkusStream(request, options)
    
    
    listSkusStream(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListSkusRequest, options?: CallOptions): Transform;

Equivalent to `listSkus`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistskusrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listSkusAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listZones(request, options)
    
    
    listZones(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListZonesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gdchardwaremanagement.v1alpha.IZone[],
            protos.google.cloud.gdchardwaremanagement.v1alpha.IListZonesRequest | null,
            protos.google.cloud.gdchardwaremanagement.v1alpha.IListZonesResponse
        ]>;

Lists zones in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListZonesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistzonesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gdchardwaremanagement.v1alpha.IZone](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.izone)[], [protos.google.cloud.gdchardwaremanagement.v1alpha.IListZonesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistzonesrequest) | null, [protos.google.cloud.gdchardwaremanagement.v1alpha.IListZonesResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistzonesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listZonesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listZones(request, options, callback)
    
    
    listZones(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IListZonesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.gdchardwaremanagement.v1alpha.IListZonesRequest, protos.google.cloud.gdchardwaremanagement.v1alpha.IListZonesResponse | null | undefined, protos.google.cloud.gdchardwaremanagement.v1alpha.IZone>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListZonesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistzonesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IListZonesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistzonesrequest), [protos.google.cloud.gdchardwaremanagement.v1alpha.IListZonesResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistzonesresponse) | null | undefined, [protos.google.cloud.gdchardwaremanagement.v1alpha.IZone](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.izone)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listZones(request, callback)
    
    
    listZones(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IListZonesRequest, callback: PaginationCallback<protos.google.cloud.gdchardwaremanagement.v1alpha.IListZonesRequest, protos.google.cloud.gdchardwaremanagement.v1alpha.IListZonesResponse | null | undefined, protos.google.cloud.gdchardwaremanagement.v1alpha.IZone>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListZonesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistzonesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IListZonesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistzonesrequest), [protos.google.cloud.gdchardwaremanagement.v1alpha.IListZonesResponse](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistzonesresponse) | null | undefined, [protos.google.cloud.gdchardwaremanagement.v1alpha.IZone](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.izone)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listZonesAsync(request, options)
    
    
    listZonesAsync(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListZonesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.gdchardwaremanagement.v1alpha.IZone>;

Equivalent to `listZones`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListZonesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistzonesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.gdchardwaremanagement.v1alpha.IZone](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.izone)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location to list zones in.
       *  Format: `projects/{project}/locations/{location}`
       *  To list zones across all locations, substitute `-` (the hyphen or
       *  dash character) for the location and check the unreachable field in
       *  the response message.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results the server should return.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filtering condition. See AIP-160 (https://google.aip.dev/160).
       */
      // const filter = 'abc123'
      /**
       *  Optional. Hint for how to order the results.
       */
      // const orderBy = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callListZones() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = gdchardwaremanagementClient.[listZonesAsync](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/v1alpha.gdchardwaremanagementclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListZones();
    
    

### listZonesStream(request, options)
    
    
    listZonesStream(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IListZonesRequest, options?: CallOptions): Transform;

Equivalent to `listZones`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListZonesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ilistzonesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listZonesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### matchChangeLogEntryFromChangeLogEntryName(changeLogEntryName)
    
    
    matchChangeLogEntryFromChangeLogEntryName(changeLogEntryName: string): string | number;

Parse the change_log_entry from ChangeLogEntry resource.

**Parameter**  
---  
**Name** | **Description**  
`changeLogEntryName` |  `string`   
A fully-qualified path representing ChangeLogEntry resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the change_log_entry.  
  
### matchCommentFromCommentName(commentName)
    
    
    matchCommentFromCommentName(commentName: string): string | number;

Parse the comment from Comment resource.

**Parameter**  
---  
**Name** | **Description**  
`commentName` |  `string`   
A fully-qualified path representing Comment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the comment.  
  
### matchHardwareFromHardwareName(hardwareName)
    
    
    matchHardwareFromHardwareName(hardwareName: string): string | number;

Parse the hardware from Hardware resource.

**Parameter**  
---  
**Name** | **Description**  
`hardwareName` |  `string`   
A fully-qualified path representing Hardware resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the hardware.  
  
### matchHardwareGroupFromHardwareGroupName(hardwareGroupName)
    
    
    matchHardwareGroupFromHardwareGroupName(hardwareGroupName: string): string | number;

Parse the hardware_group from HardwareGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`hardwareGroupName` |  `string`   
A fully-qualified path representing HardwareGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the hardware_group.  
  
### matchLocationFromChangeLogEntryName(changeLogEntryName)
    
    
    matchLocationFromChangeLogEntryName(changeLogEntryName: string): string | number;

Parse the location from ChangeLogEntry resource.

**Parameter**  
---  
**Name** | **Description**  
`changeLogEntryName` |  `string`   
A fully-qualified path representing ChangeLogEntry resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromCommentName(commentName)
    
    
    matchLocationFromCommentName(commentName: string): string | number;

Parse the location from Comment resource.

**Parameter**  
---  
**Name** | **Description**  
`commentName` |  `string`   
A fully-qualified path representing Comment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromHardwareGroupName(hardwareGroupName)
    
    
    matchLocationFromHardwareGroupName(hardwareGroupName: string): string | number;

Parse the location from HardwareGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`hardwareGroupName` |  `string`   
A fully-qualified path representing HardwareGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromHardwareName(hardwareName)
    
    
    matchLocationFromHardwareName(hardwareName: string): string | number;

Parse the location from Hardware resource.

**Parameter**  
---  
**Name** | **Description**  
`hardwareName` |  `string`   
A fully-qualified path representing Hardware resource.  
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
  
### matchLocationFromOrderName(orderName)
    
    
    matchLocationFromOrderName(orderName: string): string | number;

Parse the location from Order resource.

**Parameter**  
---  
**Name** | **Description**  
`orderName` |  `string`   
A fully-qualified path representing Order resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSiteName(siteName)
    
    
    matchLocationFromSiteName(siteName: string): string | number;

Parse the location from Site resource.

**Parameter**  
---  
**Name** | **Description**  
`siteName` |  `string`   
A fully-qualified path representing Site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSkuName(skuName)
    
    
    matchLocationFromSkuName(skuName: string): string | number;

Parse the location from Sku resource.

**Parameter**  
---  
**Name** | **Description**  
`skuName` |  `string`   
A fully-qualified path representing Sku resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromZoneName(zoneName)
    
    
    matchLocationFromZoneName(zoneName: string): string | number;

Parse the location from Zone resource.

**Parameter**  
---  
**Name** | **Description**  
`zoneName` |  `string`   
A fully-qualified path representing Zone resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchOrderFromChangeLogEntryName(changeLogEntryName)
    
    
    matchOrderFromChangeLogEntryName(changeLogEntryName: string): string | number;

Parse the order from ChangeLogEntry resource.

**Parameter**  
---  
**Name** | **Description**  
`changeLogEntryName` |  `string`   
A fully-qualified path representing ChangeLogEntry resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the order.  
  
### matchOrderFromCommentName(commentName)
    
    
    matchOrderFromCommentName(commentName: string): string | number;

Parse the order from Comment resource.

**Parameter**  
---  
**Name** | **Description**  
`commentName` |  `string`   
A fully-qualified path representing Comment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the order.  
  
### matchOrderFromHardwareGroupName(hardwareGroupName)
    
    
    matchOrderFromHardwareGroupName(hardwareGroupName: string): string | number;

Parse the order from HardwareGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`hardwareGroupName` |  `string`   
A fully-qualified path representing HardwareGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the order.  
  
### matchOrderFromOrderName(orderName)
    
    
    matchOrderFromOrderName(orderName: string): string | number;

Parse the order from Order resource.

**Parameter**  
---  
**Name** | **Description**  
`orderName` |  `string`   
A fully-qualified path representing Order resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the order.  
  
### matchProjectFromChangeLogEntryName(changeLogEntryName)
    
    
    matchProjectFromChangeLogEntryName(changeLogEntryName: string): string | number;

Parse the project from ChangeLogEntry resource.

**Parameter**  
---  
**Name** | **Description**  
`changeLogEntryName` |  `string`   
A fully-qualified path representing ChangeLogEntry resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromCommentName(commentName)
    
    
    matchProjectFromCommentName(commentName: string): string | number;

Parse the project from Comment resource.

**Parameter**  
---  
**Name** | **Description**  
`commentName` |  `string`   
A fully-qualified path representing Comment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromHardwareGroupName(hardwareGroupName)
    
    
    matchProjectFromHardwareGroupName(hardwareGroupName: string): string | number;

Parse the project from HardwareGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`hardwareGroupName` |  `string`   
A fully-qualified path representing HardwareGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromHardwareName(hardwareName)
    
    
    matchProjectFromHardwareName(hardwareName: string): string | number;

Parse the project from Hardware resource.

**Parameter**  
---  
**Name** | **Description**  
`hardwareName` |  `string`   
A fully-qualified path representing Hardware resource.  
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
  
### matchProjectFromOrderName(orderName)
    
    
    matchProjectFromOrderName(orderName: string): string | number;

Parse the project from Order resource.

**Parameter**  
---  
**Name** | **Description**  
`orderName` |  `string`   
A fully-qualified path representing Order resource.  
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
  
### matchProjectFromSiteName(siteName)
    
    
    matchProjectFromSiteName(siteName: string): string | number;

Parse the project from Site resource.

**Parameter**  
---  
**Name** | **Description**  
`siteName` |  `string`   
A fully-qualified path representing Site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSkuName(skuName)
    
    
    matchProjectFromSkuName(skuName: string): string | number;

Parse the project from Sku resource.

**Parameter**  
---  
**Name** | **Description**  
`skuName` |  `string`   
A fully-qualified path representing Sku resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromZoneName(zoneName)
    
    
    matchProjectFromZoneName(zoneName: string): string | number;

Parse the project from Zone resource.

**Parameter**  
---  
**Name** | **Description**  
`zoneName` |  `string`   
A fully-qualified path representing Zone resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchSiteFromSiteName(siteName)
    
    
    matchSiteFromSiteName(siteName: string): string | number;

Parse the site from Site resource.

**Parameter**  
---  
**Name** | **Description**  
`siteName` |  `string`   
A fully-qualified path representing Site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the site.  
  
### matchSkuFromSkuName(skuName)
    
    
    matchSkuFromSkuName(skuName: string): string | number;

Parse the sku from Sku resource.

**Parameter**  
---  
**Name** | **Description**  
`skuName` |  `string`   
A fully-qualified path representing Sku resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sku.  
  
### matchZoneFromZoneName(zoneName)
    
    
    matchZoneFromZoneName(zoneName: string): string | number;

Parse the zone from Zone resource.

**Parameter**  
---  
**Name** | **Description**  
`zoneName` |  `string`   
A fully-qualified path representing Zone resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the zone.  
  
### orderPath(project, location, order)
    
    
    orderPath(project: string, location: string, order: string): string;

Return a fully-qualified order resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`order` |  `string`   
  
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
  
### recordActionOnComment(request, options)
    
    
    recordActionOnComment(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IRecordActionOnCommentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gdchardwaremanagement.v1alpha.IComment,
            (protos.google.cloud.gdchardwaremanagement.v1alpha.IRecordActionOnCommentRequest | undefined),
            {} | undefined
        ]>;

Record Action on a Comment. If the Action specified in the request is READ, the viewed time in the comment is set to the time the request was received. If the comment is already marked as read, subsequent calls will be ignored. If the Action is UNREAD, the viewed time is cleared from the comment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRecordActionOnCommentRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.irecordactiononcommentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gdchardwaremanagement.v1alpha.IComment](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icomment), ([protos.google.cloud.gdchardwaremanagement.v1alpha.IRecordActionOnCommentRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.irecordactiononcommentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Comment](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.comment). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the comment.
       *  Format:
       *  `projects/{project}/locations/{location}/orders/{order}/comments/{comment}`
       */
      // const name = 'abc123'
      /**
       *  Required. The action type of the recorded action.
       */
      // const actionType = {}
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callRecordActionOnComment() {
        // Construct request
        const request = {
          name,
          actionType,
        };
    
        // Run request
        const response = await gdchardwaremanagementClient.recordActionOnComment(request);
        console.log(response);
      }
    
      callRecordActionOnComment();
    
    

### recordActionOnComment(request, options, callback)
    
    
    recordActionOnComment(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IRecordActionOnCommentRequest, options: CallOptions, callback: Callback<protos.google.cloud.gdchardwaremanagement.v1alpha.IComment, protos.google.cloud.gdchardwaremanagement.v1alpha.IRecordActionOnCommentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRecordActionOnCommentRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.irecordactiononcommentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IComment](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icomment), [protos.google.cloud.gdchardwaremanagement.v1alpha.IRecordActionOnCommentRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.irecordactiononcommentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### recordActionOnComment(request, callback)
    
    
    recordActionOnComment(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IRecordActionOnCommentRequest, callback: Callback<protos.google.cloud.gdchardwaremanagement.v1alpha.IComment, protos.google.cloud.gdchardwaremanagement.v1alpha.IRecordActionOnCommentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRecordActionOnCommentRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.irecordactiononcommentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.gdchardwaremanagement.v1alpha.IComment](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.icomment), [protos.google.cloud.gdchardwaremanagement.v1alpha.IRecordActionOnCommentRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.irecordactiononcommentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### requestOrderDateChange(request, options)
    
    
    requestOrderDateChange(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IRequestOrderDateChangeRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the requested date change of a single Order.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRequestOrderDateChangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.irequestorderdatechangerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the order to update.
       *  Format: projects/{project}/locations/{location}/orders/{order}
       */
      // const name = 'abc123'
      /**
       *  Required. The date to which the customer or Google wants to set the
       *  scheduled installation date.
       */
      // const requestedDate = {}
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callRequestOrderDateChange() {
        // Construct request
        const request = {
          name,
          requestedDate,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.requestOrderDateChange(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callRequestOrderDateChange();
    
    

### requestOrderDateChange(request, options, callback)
    
    
    requestOrderDateChange(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IRequestOrderDateChangeRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRequestOrderDateChangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.irequestorderdatechangerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### requestOrderDateChange(request, callback)
    
    
    requestOrderDateChange(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IRequestOrderDateChangeRequest, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRequestOrderDateChangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.irequestorderdatechangerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### signalZoneState(request, options)
    
    
    signalZoneState(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.ISignalZoneStateRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IZone, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Signals the state of a zone.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISignalZoneStateRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isignalzonestaterequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IZone](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.izone), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the zone.
       *  Format: `projects/{project}/locations/{location}/zones/{zone}`
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. The state signal to send for this zone. Either state_signal or
       *  provisioning_state_signal must be set, but not both.
       */
      // const stateSignal = {}
      /**
       *  Optional. The provisioning state signal to send for this zone. Either
       *  state_signal or provisioning_state_signal must be set, but not both.
       */
      // const provisioningStateSignal = {}
      /**
       *  Optional. The step being executed. Provides a finer grained status when the
       *  state_signal is FACTORY_TURNUP_CHECKS_STARTED or
       *  FACTORY_TURNUP_CHECKS_FAILED.
       */
      // const step = 'abc123'
      /**
       *  Optional. Additional details, such as an error message when state_signal is
       *  FACTORY_TURNUP_CHECKS_FAILED.
       */
      // const details = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callSignalZoneState() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.signalZoneState(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callSignalZoneState();
    
    

### signalZoneState(request, options, callback)
    
    
    signalZoneState(request: protos.google.cloud.gdchardwaremanagement.v1alpha.ISignalZoneStateRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IZone, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISignalZoneStateRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isignalzonestaterequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IZone](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.izone), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### signalZoneState(request, callback)
    
    
    signalZoneState(request: protos.google.cloud.gdchardwaremanagement.v1alpha.ISignalZoneStateRequest, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IZone, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISignalZoneStateRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isignalzonestaterequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IZone](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.izone), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### sitePath(project, location, site)
    
    
    sitePath(project: string, location: string, site: string): string;

Return a fully-qualified site resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`site` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### skuPath(project, location, sku)
    
    
    skuPath(project: string, location: string, sku: string): string;

Return a fully-qualified sku resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`sku` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### submitOrder(request, options)
    
    
    submitOrder(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.ISubmitOrderRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Submits an order.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISubmitOrderRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isubmitorderrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the order.
       *  Format: `projects/{project}/locations/{location}/orders/{order}`
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. Type of this request. If unset, the request type is assumed to be
       *  `INFO_PENDING`.
       */
      // const type = {}
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callSubmitOrder() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.submitOrder(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callSubmitOrder();
    
    

### submitOrder(request, options, callback)
    
    
    submitOrder(request: protos.google.cloud.gdchardwaremanagement.v1alpha.ISubmitOrderRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISubmitOrderRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isubmitorderrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### submitOrder(request, callback)
    
    
    submitOrder(request: protos.google.cloud.gdchardwaremanagement.v1alpha.ISubmitOrderRequest, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISubmitOrderRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isubmitorderrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateHardware(request, options)
    
    
    updateHardware(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IUpdateHardwareRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates hardware parameters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iupdatehardwarerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardware), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A mask to specify the fields in the Hardware to overwrite with
       *  this update. The fields specified in the update_mask are relative to the
       *  hardware, not the full request. A field will be overwritten if it is in the
       *  mask. If you don't provide a mask then all fields will be overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The hardware to update.
       */
      // const hardware = {}
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callUpdateHardware() {
        // Construct request
        const request = {
          updateMask,
          hardware,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.updateHardware(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateHardware();
    
    

### updateHardware(request, options, callback)
    
    
    updateHardware(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IUpdateHardwareRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iupdatehardwarerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardware), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateHardware(request, callback)
    
    
    updateHardware(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IUpdateHardwareRequest, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateHardwareRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iupdatehardwarerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IHardware](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardware), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateHardwareGroup(request, options)
    
    
    updateHardwareGroup(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IUpdateHardwareGroupRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the parameters of a hardware group.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateHardwareGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iupdatehardwaregrouprequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardwaregroup), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A mask to specify the fields in the HardwareGroup to overwrite
       *  with this update. The fields specified in the update_mask are relative to
       *  the hardware group, not the full request. A field will be overwritten if it
       *  is in the mask. If you don't provide a mask then all fields will be
       *  overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The hardware group to update.
       */
      // const hardwareGroup = {}
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callUpdateHardwareGroup() {
        // Construct request
        const request = {
          updateMask,
          hardwareGroup,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.updateHardwareGroup(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateHardwareGroup();
    
    

### updateHardwareGroup(request, options, callback)
    
    
    updateHardwareGroup(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IUpdateHardwareGroupRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateHardwareGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iupdatehardwaregrouprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardwaregroup), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateHardwareGroup(request, callback)
    
    
    updateHardwareGroup(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IUpdateHardwareGroupRequest, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateHardwareGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iupdatehardwaregrouprequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IHardwareGroup](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ihardwaregroup), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateOrder(request, options)
    
    
    updateOrder(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IUpdateOrderRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the parameters of an order.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateOrderRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iupdateorderrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A mask to specify the fields in the Order to overwrite with this
       *  update. The fields specified in the update_mask are relative to the order,
       *  not the full request. A field will be overwritten if it is in the mask. If
       *  you don't provide a mask then all fields will be overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The order to update.
       */
      // const order = {}
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callUpdateOrder() {
        // Construct request
        const request = {
          updateMask,
          order,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.updateOrder(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateOrder();
    
    

### updateOrder(request, options, callback)
    
    
    updateOrder(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IUpdateOrderRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateOrderRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iupdateorderrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateOrder(request, callback)
    
    
    updateOrder(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IUpdateOrderRequest, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateOrderRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iupdateorderrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IOrder](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iorder), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSite(request, options)
    
    
    updateSite(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IUpdateSiteRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.ISite, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the parameters of a site.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iupdatesiterequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.ISite](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isite), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A mask to specify the fields in the Site to overwrite with this
       *  update. The fields specified in the update_mask are relative to the site,
       *  not the full request. A field will be overwritten if it is in the mask. If
       *  you don't provide a mask then all fields will be overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The site to update.
       */
      // const site = {}
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callUpdateSite() {
        // Construct request
        const request = {
          updateMask,
          site,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.updateSite(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateSite();
    
    

### updateSite(request, options, callback)
    
    
    updateSite(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IUpdateSiteRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.ISite, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iupdatesiterequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.ISite](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isite), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSite(request, callback)
    
    
    updateSite(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IUpdateSiteRequest, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.ISite, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iupdatesiterequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.ISite](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.isite), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateZone(request, options)
    
    
    updateZone(request?: protos.google.cloud.gdchardwaremanagement.v1alpha.IUpdateZoneRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IZone, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the parameters of a zone.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iupdatezonerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IZone](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.izone), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A mask to specify the fields in the Zone to overwrite with this
       *  update. The fields specified in the update_mask are relative to the zone,
       *  not the full request. A field will be overwritten if it is in the mask. If
       *  you don't provide a mask then all fields will be overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The zone to update.
       */
      // const zone = {}
      /**
       *  Optional. An optional unique identifier for this request. See
       *  AIP-155 (https://google.aip.dev/155).
       */
      // const requestId = 'abc123'
    
      // Imports the Gdchardwaremanagement library
      const {GDCHardwareManagementClient} = require('[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const gdchardwaremanagementClient = new [GDCHardwareManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)();
    
      async function callUpdateZone() {
        // Construct request
        const request = {
          updateMask,
          zone,
        };
    
        // Run request
        const [operation] = await gdchardwaremanagementClient.updateZone(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateZone();
    
    

### updateZone(request, options, callback)
    
    
    updateZone(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IUpdateZoneRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IZone, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iupdatezonerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IZone](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.izone), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateZone(request, callback)
    
    
    updateZone(request: protos.google.cloud.gdchardwaremanagement.v1alpha.IUpdateZoneRequest, callback: Callback<LROperation<protos.google.cloud.gdchardwaremanagement.v1alpha.IZone, protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.iupdatezonerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gdchardwaremanagement.v1alpha.IZone](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.izone), [protos.google.cloud.gdchardwaremanagement.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### zonePath(project, location, zone)
    
    
    zonePath(project: string, location: string, zone: string): string;

Return a fully-qualified zone resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`zone` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
