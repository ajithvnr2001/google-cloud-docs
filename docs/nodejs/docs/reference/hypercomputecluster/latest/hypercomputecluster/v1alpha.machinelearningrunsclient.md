---
url: https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient
title: Class v1alpha.MachineLearningRunsClient (0.5.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:07:11.511462+00:00
---

# Class v1alpha.MachineLearningRunsClient (0.5.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1alpha.MachineLearningRunsClient (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.2.0  0.1.0 

Service for managing Machine Learning Runs. v1alpha

## Package

[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of MachineLearningRunsClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new MachineLearningRunsClient({fallback: true}, gax); ```  
  
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

### locationsClient
    
    
    locationsClient: LocationsClient;

### machineLearningRunsStub
    
    
    machineLearningRunsStub?: Promise<{
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
    

### checkCreateMachineLearningRunProgress(name)
    
    
    checkCreateMachineLearningRunProgress(name: string): Promise<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.MachineLearningRun, protos.google.cloud.hypercomputecluster.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `createMachineLearningRun()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.MachineLearningRun](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.machinelearningrun-class), [protos.google.cloud.hypercomputecluster.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent format: projects/{project}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Required. The Machine Learning Run to create.
       */
      // const machineLearningRun = {}
      /**
       *  Optional. The ID of the Machine Learning Run to create.
       */
      // const machineLearningRunId = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callCreateMachineLearningRun() {
        // Construct request
        const request = {
          parent,
          machineLearningRun,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.createMachineLearningRun(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateMachineLearningRun();
    
    

### checkCreateMonitoredEventProgress(name)
    
    
    checkCreateMonitoredEventProgress(name: string): Promise<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.MonitoredEvent, protos.google.cloud.hypercomputecluster.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `createMonitoredEvent()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.MonitoredEvent](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.monitoredevent-class), [protos.google.cloud.hypercomputecluster.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent resource where the event will be created.
       *  Format:
       *  projects/{project}/locations/{location}/machineLearningRuns/{machine_learning_run}
       */
      // const parent = 'abc123'
      /**
       *  Required. The event resource to create.
       */
      // const monitoredEvent = {}
      /**
       *  Optional. Optional ID for the event.
       */
      // const monitoredEventId = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callCreateMonitoredEvent() {
        // Construct request
        const request = {
          parent,
          monitoredEvent,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.createMonitoredEvent(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateMonitoredEvent();
    
    

### checkCreateProfilerSessionProgress(name)
    
    
    checkCreateProfilerSessionProgress(name: string): Promise<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.ProfilerSession, protos.google.cloud.hypercomputecluster.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `createProfilerSession()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.ProfilerSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.profilersession-class), [protos.google.cloud.hypercomputecluster.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required.
       *  projects/{project}/locations/{location}/machineLearningRuns/{machine_learning_run}
       */
      // const parent = 'abc123'
      /**
       *  Optional. ID for the profiler session.
       */
      // const profilerSessionId = 'abc123'
      /**
       *  Required. The Profiler Session to create.
       */
      // const profilerSession = {}
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callCreateProfilerSession() {
        // Construct request
        const request = {
          parent,
          profilerSession,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.createProfilerSession(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateProfilerSession();
    
    

### checkCreateProfilerTargetProgress(name)
    
    
    checkCreateProfilerTargetProgress(name: string): Promise<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.ProfilerTarget, protos.google.cloud.hypercomputecluster.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `createProfilerTarget()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.ProfilerTarget](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.profilertarget), [protos.google.cloud.hypercomputecluster.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required.
       *  projects/{project}/locations/{location}/machineLearningRuns/{machine_learning_run}
       */
      // const parent = 'abc123'
      /**
       *  Required. The Profiler Target to create.
       */
      // const profilerTarget = {}
      /**
       *  Optional. If not provided, the server will generate an ID based on hostname
       *  and node_index. Example: "myhost-0"
       */
      // const profilerTargetId = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callCreateProfilerTarget() {
        // Construct request
        const request = {
          parent,
          profilerTarget,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.createProfilerTarget(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateProfilerTarget();
    
    

### checkDeleteMachineLearningRunProgress(name)
    
    
    checkDeleteMachineLearningRunProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.hypercomputecluster.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `deleteMachineLearningRun()`.

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
       *  Required.
       *  projects/{project}/locations/{location}/machineLearningRuns/{machineLearningRun}
       */
      // const name = 'abc123'
      /**
       *  Optional. If force=false and if a user tries to delete an ml run resource
       *  that still has child resources (e.g., ProfilerTarget), the request should
       *  fail with a FAILED_PRECONDITION error. If force=true, the delete request
       *  should delete both parent and child resources that exist.
       */
      // const force = true
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callDeleteMachineLearningRun() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.deleteMachineLearningRun(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteMachineLearningRun();
    
    

### checkDeleteMonitoredEventProgress(name)
    
    
    checkDeleteMonitoredEventProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.hypercomputecluster.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `deleteMonitoredEvent()`.

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
       *  Required. The name of the monitored event to delete.
       *  Format:
       *  projects/{project}/locations/{location}/machineLearningRuns/{machine_learning_run}/monitoredEvents/{monitored_event}
       */
      // const name = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callDeleteMonitoredEvent() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.deleteMonitoredEvent(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteMonitoredEvent();
    
    

### checkUpdateMachineLearningRunProgress(name)
    
    
    checkUpdateMachineLearningRunProgress(name: string): Promise<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.MachineLearningRun, protos.google.cloud.hypercomputecluster.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `updateMachineLearningRun()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.MachineLearningRun](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.machinelearningrun-class), [protos.google.cloud.hypercomputecluster.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Machine Learning Run to update.
       */
      // const machineLearningRun = {}
      /**
       *  Optional. Used to identify fields to be updated. Allowed fields is *, we
       *  don't support partial updates.
       */
      // const updateMask = {}
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callUpdateMachineLearningRun() {
        // Construct request
        const request = {
          machineLearningRun,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.updateMachineLearningRun(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateMachineLearningRun();
    
    

### checkUpdateMonitoredEventProgress(name)
    
    
    checkUpdateMonitoredEventProgress(name: string): Promise<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.MonitoredEvent, protos.google.cloud.hypercomputecluster.v1alpha.OperationMetadata>>;

Check the status of the long running operation returned by `updateMonitoredEvent()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.MonitoredEvent](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.monitoredevent-class), [protos.google.cloud.hypercomputecluster.v1alpha.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The monitored event to update.
       *  The event's `name` field is used to identify the event to be updated.
       */
      // const monitoredEvent = {}
      /**
       *  Optional. The list of fields to be updated.
       */
      // const updateMask = {}
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callUpdateMonitoredEvent() {
        // Construct request
        const request = {
          monitoredEvent,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.updateMonitoredEvent(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateMonitoredEvent();
    
    

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
  
### createMachineLearningRun(request, options)
    
    
    createMachineLearningRun(request?: protos.google.cloud.hypercomputecluster.v1alpha.ICreateMachineLearningRunRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a Machine Learning Run.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMachineLearningRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icreatemachinelearningrunrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imachinelearningrun), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent format: projects/{project}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Required. The Machine Learning Run to create.
       */
      // const machineLearningRun = {}
      /**
       *  Optional. The ID of the Machine Learning Run to create.
       */
      // const machineLearningRunId = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callCreateMachineLearningRun() {
        // Construct request
        const request = {
          parent,
          machineLearningRun,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.createMachineLearningRun(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateMachineLearningRun();
    
    

### createMachineLearningRun(request, options, callback)
    
    
    createMachineLearningRun(request: protos.google.cloud.hypercomputecluster.v1alpha.ICreateMachineLearningRunRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMachineLearningRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icreatemachinelearningrunrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imachinelearningrun), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMachineLearningRun(request, callback)
    
    
    createMachineLearningRun(request: protos.google.cloud.hypercomputecluster.v1alpha.ICreateMachineLearningRunRequest, callback: Callback<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMachineLearningRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icreatemachinelearningrunrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imachinelearningrun), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMonitoredEvent(request, options)
    
    
    createMonitoredEvent(request?: protos.google.cloud.hypercomputecluster.v1alpha.ICreateMonitoredEventRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a Monitored Event.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMonitoredEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icreatemonitoredeventrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imonitoredevent), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent resource where the event will be created.
       *  Format:
       *  projects/{project}/locations/{location}/machineLearningRuns/{machine_learning_run}
       */
      // const parent = 'abc123'
      /**
       *  Required. The event resource to create.
       */
      // const monitoredEvent = {}
      /**
       *  Optional. Optional ID for the event.
       */
      // const monitoredEventId = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callCreateMonitoredEvent() {
        // Construct request
        const request = {
          parent,
          monitoredEvent,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.createMonitoredEvent(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateMonitoredEvent();
    
    

### createMonitoredEvent(request, options, callback)
    
    
    createMonitoredEvent(request: protos.google.cloud.hypercomputecluster.v1alpha.ICreateMonitoredEventRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMonitoredEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icreatemonitoredeventrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imonitoredevent), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMonitoredEvent(request, callback)
    
    
    createMonitoredEvent(request: protos.google.cloud.hypercomputecluster.v1alpha.ICreateMonitoredEventRequest, callback: Callback<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMonitoredEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icreatemonitoredeventrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imonitoredevent), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createProfilerSession(request, options)
    
    
    createProfilerSession(request?: protos.google.cloud.hypercomputecluster.v1alpha.ICreateProfilerSessionRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.hypercomputecluster.v1alpha.IProfilerSession, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Create a Profiler Session.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateProfilerSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icreateprofilersessionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.IProfilerSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilersession), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required.
       *  projects/{project}/locations/{location}/machineLearningRuns/{machine_learning_run}
       */
      // const parent = 'abc123'
      /**
       *  Optional. ID for the profiler session.
       */
      // const profilerSessionId = 'abc123'
      /**
       *  Required. The Profiler Session to create.
       */
      // const profilerSession = {}
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callCreateProfilerSession() {
        // Construct request
        const request = {
          parent,
          profilerSession,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.createProfilerSession(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateProfilerSession();
    
    

### createProfilerSession(request, options, callback)
    
    
    createProfilerSession(request: protos.google.cloud.hypercomputecluster.v1alpha.ICreateProfilerSessionRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.IProfilerSession, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateProfilerSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icreateprofilersessionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.IProfilerSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilersession), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createProfilerSession(request, callback)
    
    
    createProfilerSession(request: protos.google.cloud.hypercomputecluster.v1alpha.ICreateProfilerSessionRequest, callback: Callback<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.IProfilerSession, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateProfilerSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icreateprofilersessionrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.IProfilerSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilersession), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createProfilerTarget(request, options)
    
    
    createProfilerTarget(request?: protos.google.cloud.hypercomputecluster.v1alpha.ICreateProfilerTargetRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.hypercomputecluster.v1alpha.IProfilerTarget, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a Profiler Target.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateProfilerTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icreateprofilertargetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.IProfilerTarget](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilertarget), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required.
       *  projects/{project}/locations/{location}/machineLearningRuns/{machine_learning_run}
       */
      // const parent = 'abc123'
      /**
       *  Required. The Profiler Target to create.
       */
      // const profilerTarget = {}
      /**
       *  Optional. If not provided, the server will generate an ID based on hostname
       *  and node_index. Example: "myhost-0"
       */
      // const profilerTargetId = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callCreateProfilerTarget() {
        // Construct request
        const request = {
          parent,
          profilerTarget,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.createProfilerTarget(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateProfilerTarget();
    
    

### createProfilerTarget(request, options, callback)
    
    
    createProfilerTarget(request: protos.google.cloud.hypercomputecluster.v1alpha.ICreateProfilerTargetRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.IProfilerTarget, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateProfilerTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icreateprofilertargetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.IProfilerTarget](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilertarget), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createProfilerTarget(request, callback)
    
    
    createProfilerTarget(request: protos.google.cloud.hypercomputecluster.v1alpha.ICreateProfilerTargetRequest, callback: Callback<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.IProfilerTarget, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateProfilerTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icreateprofilertargetrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.IProfilerTarget](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilertarget), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMachineLearningRun(request, options)
    
    
    deleteMachineLearningRun(request?: protos.google.cloud.hypercomputecluster.v1alpha.IDeleteMachineLearningRunRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a Machine Learning Run.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMachineLearningRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ideletemachinelearningrunrequest)`   
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
       *  Required.
       *  projects/{project}/locations/{location}/machineLearningRuns/{machineLearningRun}
       */
      // const name = 'abc123'
      /**
       *  Optional. If force=false and if a user tries to delete an ml run resource
       *  that still has child resources (e.g., ProfilerTarget), the request should
       *  fail with a FAILED_PRECONDITION error. If force=true, the delete request
       *  should delete both parent and child resources that exist.
       */
      // const force = true
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callDeleteMachineLearningRun() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.deleteMachineLearningRun(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteMachineLearningRun();
    
    

### deleteMachineLearningRun(request, options, callback)
    
    
    deleteMachineLearningRun(request: protos.google.cloud.hypercomputecluster.v1alpha.IDeleteMachineLearningRunRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMachineLearningRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ideletemachinelearningrunrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.iempty), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMachineLearningRun(request, callback)
    
    
    deleteMachineLearningRun(request: protos.google.cloud.hypercomputecluster.v1alpha.IDeleteMachineLearningRunRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMachineLearningRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ideletemachinelearningrunrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.iempty), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMonitoredEvent(request, options)
    
    
    deleteMonitoredEvent(request?: protos.google.cloud.hypercomputecluster.v1alpha.IDeleteMonitoredEventRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a Monitored Event.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMonitoredEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ideletemonitoredeventrequest)`   
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
       *  Required. The name of the monitored event to delete.
       *  Format:
       *  projects/{project}/locations/{location}/machineLearningRuns/{machine_learning_run}/monitoredEvents/{monitored_event}
       */
      // const name = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callDeleteMonitoredEvent() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.deleteMonitoredEvent(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteMonitoredEvent();
    
    

### deleteMonitoredEvent(request, options, callback)
    
    
    deleteMonitoredEvent(request: protos.google.cloud.hypercomputecluster.v1alpha.IDeleteMonitoredEventRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMonitoredEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ideletemonitoredeventrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.iempty), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMonitoredEvent(request, callback)
    
    
    deleteMonitoredEvent(request: protos.google.cloud.hypercomputecluster.v1alpha.IDeleteMonitoredEventRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMonitoredEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ideletemonitoredeventrequest)`   
  
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
    

### deleteProfilerSession(request, options)
    
    
    deleteProfilerSession(request?: protos.google.cloud.hypercomputecluster.v1alpha.IDeleteProfilerSessionRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.hypercomputecluster.v1alpha.IDeleteProfilerSessionRequest | undefined),
            {} | undefined
        ]>;

Delete a Profiler Session.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProfilerSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ideleteprofilersessionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.iempty), ([protos.google.cloud.hypercomputecluster.v1alpha.IDeleteProfilerSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ideleteprofilersessionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the profiler session to delete.
       *  Format:
       *  projects/{project}/locations/{location}/machineLearningRuns/{machine_learning_run}/profilerSessions/{profiler_session}
       */
      // const name = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callDeleteProfilerSession() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await hypercomputeclusterClient.deleteProfilerSession(request);
        console.log(response);
      }
    
      callDeleteProfilerSession();
    
    

### deleteProfilerSession(request, options, callback)
    
    
    deleteProfilerSession(request: protos.google.cloud.hypercomputecluster.v1alpha.IDeleteProfilerSessionRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.hypercomputecluster.v1alpha.IDeleteProfilerSessionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProfilerSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ideleteprofilersessionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.iempty), [protos.google.cloud.hypercomputecluster.v1alpha.IDeleteProfilerSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ideleteprofilersessionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteProfilerSession(request, callback)
    
    
    deleteProfilerSession(request: protos.google.cloud.hypercomputecluster.v1alpha.IDeleteProfilerSessionRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.hypercomputecluster.v1alpha.IDeleteProfilerSessionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProfilerSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ideleteprofilersessionrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.iempty), [protos.google.cloud.hypercomputecluster.v1alpha.IDeleteProfilerSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ideleteprofilersessionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteProfilerTarget(request, options)
    
    
    deleteProfilerTarget(request?: protos.google.cloud.hypercomputecluster.v1alpha.IDeleteProfilerTargetRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.hypercomputecluster.v1alpha.IDeleteProfilerTargetRequest | undefined),
            {} | undefined
        ]>;

Delete a Profiler Target.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProfilerTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ideleteprofilertargetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.iempty), ([protos.google.cloud.hypercomputecluster.v1alpha.IDeleteProfilerTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ideleteprofilertargetrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the profiler target to delete.
       *  Format:
       *  projects/{project}/locations/{location}/machineLearningRuns/{machine_learning_run}/profilerTargets/{profiler_target}
       */
      // const name = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callDeleteProfilerTarget() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await hypercomputeclusterClient.deleteProfilerTarget(request);
        console.log(response);
      }
    
      callDeleteProfilerTarget();
    
    

### deleteProfilerTarget(request, options, callback)
    
    
    deleteProfilerTarget(request: protos.google.cloud.hypercomputecluster.v1alpha.IDeleteProfilerTargetRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.hypercomputecluster.v1alpha.IDeleteProfilerTargetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProfilerTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ideleteprofilertargetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.iempty), [protos.google.cloud.hypercomputecluster.v1alpha.IDeleteProfilerTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ideleteprofilertargetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteProfilerTarget(request, callback)
    
    
    deleteProfilerTarget(request: protos.google.cloud.hypercomputecluster.v1alpha.IDeleteProfilerTargetRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.hypercomputecluster.v1alpha.IDeleteProfilerTargetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProfilerTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ideleteprofilertargetrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.protobuf.iempty), [protos.google.cloud.hypercomputecluster.v1alpha.IDeleteProfilerTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ideleteprofilertargetrequest) | null | undefined, {} | null | undefined>`   
  
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
    

### getMachineLearningRun(request, options)
    
    
    getMachineLearningRun(request?: protos.google.cloud.hypercomputecluster.v1alpha.IGetMachineLearningRunRequest, options?: CallOptions): Promise<[
            protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun,
            (protos.google.cloud.hypercomputecluster.v1alpha.IGetMachineLearningRunRequest | undefined),
            {} | undefined
        ]>;

Gets a Machine Learning Run.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMachineLearningRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetmachinelearningrunrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imachinelearningrun), ([protos.google.cloud.hypercomputecluster.v1alpha.IGetMachineLearningRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetmachinelearningrunrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required.
       *  projects/{project}/locations/{location}/machineLearningRuns/{machine_learning_run}
       */
      // const name = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callGetMachineLearningRun() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await hypercomputeclusterClient.getMachineLearningRun(request);
        console.log(response);
      }
    
      callGetMachineLearningRun();
    
    

### getMachineLearningRun(request, options, callback)
    
    
    getMachineLearningRun(request: protos.google.cloud.hypercomputecluster.v1alpha.IGetMachineLearningRunRequest, options: CallOptions, callback: Callback<protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun, protos.google.cloud.hypercomputecluster.v1alpha.IGetMachineLearningRunRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMachineLearningRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetmachinelearningrunrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imachinelearningrun), [protos.google.cloud.hypercomputecluster.v1alpha.IGetMachineLearningRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetmachinelearningrunrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMachineLearningRun(request, callback)
    
    
    getMachineLearningRun(request: protos.google.cloud.hypercomputecluster.v1alpha.IGetMachineLearningRunRequest, callback: Callback<protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun, protos.google.cloud.hypercomputecluster.v1alpha.IGetMachineLearningRunRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMachineLearningRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetmachinelearningrunrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imachinelearningrun), [protos.google.cloud.hypercomputecluster.v1alpha.IGetMachineLearningRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetmachinelearningrunrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMonitoredEvent(request, options)
    
    
    getMonitoredEvent(request?: protos.google.cloud.hypercomputecluster.v1alpha.IGetMonitoredEventRequest, options?: CallOptions): Promise<[
            protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent,
            (protos.google.cloud.hypercomputecluster.v1alpha.IGetMonitoredEventRequest | undefined),
            {} | undefined
        ]>;

Gets a specific Monitored Event.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMonitoredEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetmonitoredeventrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imonitoredevent), ([protos.google.cloud.hypercomputecluster.v1alpha.IGetMonitoredEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetmonitoredeventrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the monitored event to retrieve.
       *  Format:
       *  projects/{project}/locations/{location}/machineLearningRuns/{machine_learning_run}/monitoredEvents/{monitored_event}
       */
      // const name = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callGetMonitoredEvent() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await hypercomputeclusterClient.getMonitoredEvent(request);
        console.log(response);
      }
    
      callGetMonitoredEvent();
    
    

### getMonitoredEvent(request, options, callback)
    
    
    getMonitoredEvent(request: protos.google.cloud.hypercomputecluster.v1alpha.IGetMonitoredEventRequest, options: CallOptions, callback: Callback<protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent, protos.google.cloud.hypercomputecluster.v1alpha.IGetMonitoredEventRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMonitoredEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetmonitoredeventrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imonitoredevent), [protos.google.cloud.hypercomputecluster.v1alpha.IGetMonitoredEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetmonitoredeventrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMonitoredEvent(request, callback)
    
    
    getMonitoredEvent(request: protos.google.cloud.hypercomputecluster.v1alpha.IGetMonitoredEventRequest, callback: Callback<protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent, protos.google.cloud.hypercomputecluster.v1alpha.IGetMonitoredEventRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMonitoredEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetmonitoredeventrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imonitoredevent), [protos.google.cloud.hypercomputecluster.v1alpha.IGetMonitoredEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetmonitoredeventrequest) | null | undefined, {} | null | undefined>`   
  
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
    

### getProfilerSession(request, options)
    
    
    getProfilerSession(request?: protos.google.cloud.hypercomputecluster.v1alpha.IGetProfilerSessionRequest, options?: CallOptions): Promise<[
            protos.google.cloud.hypercomputecluster.v1alpha.IProfilerSession,
            (protos.google.cloud.hypercomputecluster.v1alpha.IGetProfilerSessionRequest | undefined),
            {} | undefined
        ]>;

Get Profiler Session.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProfilerSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetprofilersessionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.hypercomputecluster.v1alpha.IProfilerSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilersession), ([protos.google.cloud.hypercomputecluster.v1alpha.IGetProfilerSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetprofilersessionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required.
       *  projects/{project}/locations/{location}/machineLearningRuns/{machine_learning_run}/profilerSessions/{profiler_session}
       */
      // const name = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callGetProfilerSession() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await hypercomputeclusterClient.getProfilerSession(request);
        console.log(response);
      }
    
      callGetProfilerSession();
    
    

### getProfilerSession(request, options, callback)
    
    
    getProfilerSession(request: protos.google.cloud.hypercomputecluster.v1alpha.IGetProfilerSessionRequest, options: CallOptions, callback: Callback<protos.google.cloud.hypercomputecluster.v1alpha.IProfilerSession, protos.google.cloud.hypercomputecluster.v1alpha.IGetProfilerSessionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProfilerSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetprofilersessionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.hypercomputecluster.v1alpha.IProfilerSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilersession), [protos.google.cloud.hypercomputecluster.v1alpha.IGetProfilerSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetprofilersessionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProfilerSession(request, callback)
    
    
    getProfilerSession(request: protos.google.cloud.hypercomputecluster.v1alpha.IGetProfilerSessionRequest, callback: Callback<protos.google.cloud.hypercomputecluster.v1alpha.IProfilerSession, protos.google.cloud.hypercomputecluster.v1alpha.IGetProfilerSessionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProfilerSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetprofilersessionrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.hypercomputecluster.v1alpha.IProfilerSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilersession), [protos.google.cloud.hypercomputecluster.v1alpha.IGetProfilerSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetprofilersessionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProfilerTarget(request, options)
    
    
    getProfilerTarget(request?: protos.google.cloud.hypercomputecluster.v1alpha.IGetProfilerTargetRequest, options?: CallOptions): Promise<[
            protos.google.cloud.hypercomputecluster.v1alpha.IProfilerTarget,
            (protos.google.cloud.hypercomputecluster.v1alpha.IGetProfilerTargetRequest | undefined),
            {} | undefined
        ]>;

Gets a Profiler Target.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProfilerTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetprofilertargetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.hypercomputecluster.v1alpha.IProfilerTarget](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilertarget), ([protos.google.cloud.hypercomputecluster.v1alpha.IGetProfilerTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetprofilertargetrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ProfilerTarget](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.profilertarget). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required.
       *  projects/{project}/locations/{location}/machineLearningRuns/{machine_learning_run}/profilerTargets/{profiler_target}
       */
      // const name = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callGetProfilerTarget() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await hypercomputeclusterClient.getProfilerTarget(request);
        console.log(response);
      }
    
      callGetProfilerTarget();
    
    

### getProfilerTarget(request, options, callback)
    
    
    getProfilerTarget(request: protos.google.cloud.hypercomputecluster.v1alpha.IGetProfilerTargetRequest, options: CallOptions, callback: Callback<protos.google.cloud.hypercomputecluster.v1alpha.IProfilerTarget, protos.google.cloud.hypercomputecluster.v1alpha.IGetProfilerTargetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProfilerTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetprofilertargetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.hypercomputecluster.v1alpha.IProfilerTarget](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilertarget), [protos.google.cloud.hypercomputecluster.v1alpha.IGetProfilerTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetprofilertargetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProfilerTarget(request, callback)
    
    
    getProfilerTarget(request: protos.google.cloud.hypercomputecluster.v1alpha.IGetProfilerTargetRequest, callback: Callback<protos.google.cloud.hypercomputecluster.v1alpha.IProfilerTarget, protos.google.cloud.hypercomputecluster.v1alpha.IGetProfilerTargetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProfilerTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetprofilertargetrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.hypercomputecluster.v1alpha.IProfilerTarget](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilertarget), [protos.google.cloud.hypercomputecluster.v1alpha.IGetProfilerTargetRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetprofilertargetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProfileSession(request, options)
    
    
    getProfileSession(request?: protos.google.cloud.hypercomputecluster.v1alpha.IGetProfileSessionRequest, options?: CallOptions): Promise<[
            protos.google.cloud.hypercomputecluster.v1alpha.IProfileSession,
            (protos.google.cloud.hypercomputecluster.v1alpha.IGetProfileSessionRequest | undefined),
            {} | undefined
        ]>;

Deprecated: Use `GetProfilerSession` instead. Gets a Profile Session.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProfileSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetprofilesessionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.hypercomputecluster.v1alpha.IProfileSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilesession), ([protos.google.cloud.hypercomputecluster.v1alpha.IGetProfileSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetprofilesessionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ProfileSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.profilesession). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required.
       *  projects/{project}/locations/{location}/machineLearningRuns/{machine_learning_run}/profileSessions/{profileSession}
       */
      // const name = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callGetProfileSession() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await hypercomputeclusterClient.getProfileSession(request);
        console.log(response);
      }
    
      callGetProfileSession();
    
    

### getProfileSession(request, options, callback)
    
    
    getProfileSession(request: protos.google.cloud.hypercomputecluster.v1alpha.IGetProfileSessionRequest, options: CallOptions, callback: Callback<protos.google.cloud.hypercomputecluster.v1alpha.IProfileSession, protos.google.cloud.hypercomputecluster.v1alpha.IGetProfileSessionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProfileSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetprofilesessionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.hypercomputecluster.v1alpha.IProfileSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilesession), [protos.google.cloud.hypercomputecluster.v1alpha.IGetProfileSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetprofilesessionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProfileSession(request, callback)
    
    
    getProfileSession(request: protos.google.cloud.hypercomputecluster.v1alpha.IGetProfileSessionRequest, callback: Callback<protos.google.cloud.hypercomputecluster.v1alpha.IProfileSession, protos.google.cloud.hypercomputecluster.v1alpha.IGetProfileSessionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProfileSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetprofilesessionrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.hypercomputecluster.v1alpha.IProfileSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilesession), [protos.google.cloud.hypercomputecluster.v1alpha.IGetProfileSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.igetprofilesessionrequest) | null | undefined, {} | null | undefined>`   
  
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
    

### listMachineLearningRuns(request, options)
    
    
    listMachineLearningRuns(request?: protos.google.cloud.hypercomputecluster.v1alpha.IListMachineLearningRunsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun[],
            protos.google.cloud.hypercomputecluster.v1alpha.IListMachineLearningRunsRequest | null,
            protos.google.cloud.hypercomputecluster.v1alpha.IListMachineLearningRunsResponse
        ]>;

Lists Machine Learning Runs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMachineLearningRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmachinelearningrunsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imachinelearningrun)[], [protos.google.cloud.hypercomputecluster.v1alpha.IListMachineLearningRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmachinelearningrunsrequest) | null, [protos.google.cloud.hypercomputecluster.v1alpha.IListMachineLearningRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmachinelearningrunsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listMachineLearningRunsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listMachineLearningRuns(request, options, callback)
    
    
    listMachineLearningRuns(request: protos.google.cloud.hypercomputecluster.v1alpha.IListMachineLearningRunsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.hypercomputecluster.v1alpha.IListMachineLearningRunsRequest, protos.google.cloud.hypercomputecluster.v1alpha.IListMachineLearningRunsResponse | null | undefined, protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMachineLearningRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmachinelearningrunsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.hypercomputecluster.v1alpha.IListMachineLearningRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmachinelearningrunsrequest), [protos.google.cloud.hypercomputecluster.v1alpha.IListMachineLearningRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmachinelearningrunsresponse) | null | undefined, [protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imachinelearningrun)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMachineLearningRuns(request, callback)
    
    
    listMachineLearningRuns(request: protos.google.cloud.hypercomputecluster.v1alpha.IListMachineLearningRunsRequest, callback: PaginationCallback<protos.google.cloud.hypercomputecluster.v1alpha.IListMachineLearningRunsRequest, protos.google.cloud.hypercomputecluster.v1alpha.IListMachineLearningRunsResponse | null | undefined, protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMachineLearningRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmachinelearningrunsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.hypercomputecluster.v1alpha.IListMachineLearningRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmachinelearningrunsrequest), [protos.google.cloud.hypercomputecluster.v1alpha.IListMachineLearningRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmachinelearningrunsresponse) | null | undefined, [protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imachinelearningrun)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMachineLearningRunsAsync(request, options)
    
    
    listMachineLearningRunsAsync(request?: protos.google.cloud.hypercomputecluster.v1alpha.IListMachineLearningRunsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun>;

Equivalent to `listMachineLearningRuns`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMachineLearningRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmachinelearningrunsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imachinelearningrun)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. projects/{project}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of Machine Learning Runs to return. The
       *  service may return fewer than this value. If unspecified, at most 10
       *  Machine Learning Runs will be returned. The maximum value is 1000; values
       *  above 1000 will be coerced to 1000. Please refer to
       *  https://google.aip.dev/158 for more details.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListMachineLearningRuns`
       *  call. Provide this to retrieve the subsequent page. Please refer to
       *  https://google.aip.dev/158 for more details.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. An expression for filtering the results of the request.
       *  Supported filter fields are:
       *  - run_id (string): The ID of the run (e.g., "run-1").
       *  - run_set (string): The run set (e.g., "run-set-1").
       *  - display_name (string): The display name of the run (e.g.,
       *  "display-name-1").
       *  - state (enum): The state of the run (e.g., "STATE_COMPLETED").
       *  - region (string): The region of the run (e.g., "us-central1").
       *  - orchestrator (enum): The orchestrator used for the run (e.g.,
       *  "ORCHESTRATOR_GKE").
       *  - create_time (timestamp): The creation timestamp of the run.
       *  - update_time (timestamp): The last update timestamp of the run.
       *  - etag (string): The ETag of the run.
       *  Filter expressions can be combined using "AND" and "OR" operators.
       *  Examples:
       *  To filter by a single field:
       *    `run_set = "run-set-1"`
       *    `state = "STATE_ACTIVE"`
       *  To filter by multiple fields:
       *    `run_set = "run-set-1" AND state = "STATE_ACTIVE"`
       *    `region = "us-central1" AND orchestrator = "ORCHESTRATOR_GKE"`
       *  To filter by timestamp:
       *    `create_time > "2025-05-26T10:00:00Z"`
       */
      // const filter = 'abc123'
      /**
       *  Optional. A comma-separated list of fields to order by, sorted in ascending
       *  order. Use "desc" after a field name for descending.
       *  Supported fields:
       *    * `run_id`
       *    * `run_set`
       *    * `display_name`
       *    * `region`
       *    * `orchestrator`
       *    * `state`
       *    * `create_time`
       *    * `update_time`
       *  Example: `update_time desc, create_time`.
       */
      // const orderBy = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callListMachineLearningRuns() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = hypercomputeclusterClient.[listMachineLearningRunsAsync](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListMachineLearningRuns();
    
    

### listMachineLearningRunsStream(request, options)
    
    
    listMachineLearningRunsStream(request?: protos.google.cloud.hypercomputecluster.v1alpha.IListMachineLearningRunsRequest, options?: CallOptions): Transform;

Equivalent to `listMachineLearningRuns`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMachineLearningRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmachinelearningrunsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listMachineLearningRunsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listMonitoredEvents(request, options)
    
    
    listMonitoredEvents(request?: protos.google.cloud.hypercomputecluster.v1alpha.IListMonitoredEventsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent[],
            protos.google.cloud.hypercomputecluster.v1alpha.IListMonitoredEventsRequest | null,
            protos.google.cloud.hypercomputecluster.v1alpha.IListMonitoredEventsResponse
        ]>;

Lists Monitored Events for a run.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMonitoredEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmonitoredeventsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imonitoredevent)[], [protos.google.cloud.hypercomputecluster.v1alpha.IListMonitoredEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmonitoredeventsrequest) | null, [protos.google.cloud.hypercomputecluster.v1alpha.IListMonitoredEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmonitoredeventsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listMonitoredEventsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listMonitoredEvents(request, options, callback)
    
    
    listMonitoredEvents(request: protos.google.cloud.hypercomputecluster.v1alpha.IListMonitoredEventsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.hypercomputecluster.v1alpha.IListMonitoredEventsRequest, protos.google.cloud.hypercomputecluster.v1alpha.IListMonitoredEventsResponse | null | undefined, protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMonitoredEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmonitoredeventsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.hypercomputecluster.v1alpha.IListMonitoredEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmonitoredeventsrequest), [protos.google.cloud.hypercomputecluster.v1alpha.IListMonitoredEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmonitoredeventsresponse) | null | undefined, [protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imonitoredevent)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMonitoredEvents(request, callback)
    
    
    listMonitoredEvents(request: protos.google.cloud.hypercomputecluster.v1alpha.IListMonitoredEventsRequest, callback: PaginationCallback<protos.google.cloud.hypercomputecluster.v1alpha.IListMonitoredEventsRequest, protos.google.cloud.hypercomputecluster.v1alpha.IListMonitoredEventsResponse | null | undefined, protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMonitoredEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmonitoredeventsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.hypercomputecluster.v1alpha.IListMonitoredEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmonitoredeventsrequest), [protos.google.cloud.hypercomputecluster.v1alpha.IListMonitoredEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmonitoredeventsresponse) | null | undefined, [protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imonitoredevent)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMonitoredEventsAsync(request, options)
    
    
    listMonitoredEventsAsync(request?: protos.google.cloud.hypercomputecluster.v1alpha.IListMonitoredEventsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent>;

Equivalent to `listMonitoredEvents`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMonitoredEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmonitoredeventsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imonitoredevent)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent resource to list events from.
       *  Format:
       *  projects/{project}/locations/{location}/machineLearningRuns/{machine_learning_run}
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of events to return. The service may return
       *  fewer than this value. If unspecified, at most 50 events will be returned.
       *  The maximum value is 1000; values above 1000 will be coerced to 1000.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListMonitoredEvents`
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListMonitoredEvents`
       *  must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. A filter expression for filtering results.
       */
      // const filter = 'abc123'
      /**
       *  Optional. Order by field for sorting results.
       */
      // const orderBy = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callListMonitoredEvents() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = hypercomputeclusterClient.[listMonitoredEventsAsync](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListMonitoredEvents();
    
    

### listMonitoredEventsStream(request, options)
    
    
    listMonitoredEventsStream(request?: protos.google.cloud.hypercomputecluster.v1alpha.IListMonitoredEventsRequest, options?: CallOptions): Transform;

Equivalent to `listMonitoredEvents`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMonitoredEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistmonitoredeventsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listMonitoredEventsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
    

### listProfilerSessions(request, options)
    
    
    listProfilerSessions(request?: protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerSessionsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.hypercomputecluster.v1alpha.IProfilerSession[],
            protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerSessionsRequest | null,
            protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerSessionsResponse
        ]>;

Lists Profiler Sessions for a Machine Learning Run.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProfilerSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilersessionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.hypercomputecluster.v1alpha.IProfilerSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilersession)[], [protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilersessionsrequest) | null, [protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerSessionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilersessionsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listProfilerSessionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listProfilerSessions(request, options, callback)
    
    
    listProfilerSessions(request: protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerSessionsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerSessionsRequest, protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerSessionsResponse | null | undefined, protos.google.cloud.hypercomputecluster.v1alpha.IProfilerSession>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProfilerSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilersessionsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilersessionsrequest), [protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerSessionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilersessionsresponse) | null | undefined, [protos.google.cloud.hypercomputecluster.v1alpha.IProfilerSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilersession)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProfilerSessions(request, callback)
    
    
    listProfilerSessions(request: protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerSessionsRequest, callback: PaginationCallback<protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerSessionsRequest, protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerSessionsResponse | null | undefined, protos.google.cloud.hypercomputecluster.v1alpha.IProfilerSession>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProfilerSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilersessionsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilersessionsrequest), [protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerSessionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilersessionsresponse) | null | undefined, [protos.google.cloud.hypercomputecluster.v1alpha.IProfilerSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilersession)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProfilerSessionsAsync(request, options)
    
    
    listProfilerSessionsAsync(request?: protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerSessionsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.hypercomputecluster.v1alpha.IProfilerSession>;

Equivalent to `listProfilerSessions`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProfilerSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilersessionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.hypercomputecluster.v1alpha.IProfilerSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilersession)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required.
       *  projects/{project}/locations/{location}/machineLearningRuns/{machine_learning_run}
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of profiler sessions to return. The service
       *  may return fewer than this value. If unspecified, at most 10 profiler
       *  sessions will be returned. The maximum value is 1000; values above 1000
       *  will be coerced to 1000. Please refer to https://google.aip.dev/158 for
       *  more details.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListProfilerSessions`
       *  call. Provide this to retrieve the subsequent page. Please refer to
       *  https://google.aip.dev/158 for more details.
       */
      // const pageToken = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callListProfilerSessions() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = hypercomputeclusterClient.[listProfilerSessionsAsync](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListProfilerSessions();
    
    

### listProfilerSessionsStream(request, options)
    
    
    listProfilerSessionsStream(request?: protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerSessionsRequest, options?: CallOptions): Transform;

Equivalent to `listProfilerSessions`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProfilerSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilersessionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listProfilerSessionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listProfilerTargets(request, options)
    
    
    listProfilerTargets(request?: protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerTargetsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.hypercomputecluster.v1alpha.IProfilerTarget[],
            protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerTargetsRequest | null,
            protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerTargetsResponse
        ]>;

List Profiler Targets for a Machine Learning Run.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProfilerTargetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilertargetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.hypercomputecluster.v1alpha.IProfilerTarget](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilertarget)[], [protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerTargetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilertargetsrequest) | null, [protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerTargetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilertargetsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [ProfilerTarget](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.profilertarget). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listProfilerTargetsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listProfilerTargets(request, options, callback)
    
    
    listProfilerTargets(request: protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerTargetsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerTargetsRequest, protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerTargetsResponse | null | undefined, protos.google.cloud.hypercomputecluster.v1alpha.IProfilerTarget>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProfilerTargetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilertargetsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerTargetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilertargetsrequest), [protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerTargetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilertargetsresponse) | null | undefined, [protos.google.cloud.hypercomputecluster.v1alpha.IProfilerTarget](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilertarget)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProfilerTargets(request, callback)
    
    
    listProfilerTargets(request: protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerTargetsRequest, callback: PaginationCallback<protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerTargetsRequest, protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerTargetsResponse | null | undefined, protos.google.cloud.hypercomputecluster.v1alpha.IProfilerTarget>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProfilerTargetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilertargetsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerTargetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilertargetsrequest), [protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerTargetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilertargetsresponse) | null | undefined, [protos.google.cloud.hypercomputecluster.v1alpha.IProfilerTarget](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilertarget)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProfilerTargetsAsync(request, options)
    
    
    listProfilerTargetsAsync(request?: protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerTargetsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.hypercomputecluster.v1alpha.IProfilerTarget>;

Equivalent to `listProfilerTargets`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProfilerTargetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilertargetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.hypercomputecluster.v1alpha.IProfilerTarget](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilertarget)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [ProfilerTarget](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.profilertarget). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required.
       *  projects/{project}/locations/{location}/machineLearningRuns/{machine_learning_run}
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of profiler targets to return. The service may
       *  return fewer than this value. If unspecified, at most 10 profiler targets
       *  will be returned. The maximum value is 1000; values above 1000 will be
       *  coerced to 1000. Please refer to https://google.aip.dev/158 for more
       *  details.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListProfilerTargets`
       *  call. Provide this to retrieve the subsequent page. Please refer to
       *  https://google.aip.dev/158 for more details.
       */
      // const pageToken = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callListProfilerTargets() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = hypercomputeclusterClient.[listProfilerTargetsAsync](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListProfilerTargets();
    
    

### listProfilerTargetsStream(request, options)
    
    
    listProfilerTargetsStream(request?: protos.google.cloud.hypercomputecluster.v1alpha.IListProfilerTargetsRequest, options?: CallOptions): Transform;

Equivalent to `listProfilerTargets`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProfilerTargetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilertargetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [ProfilerTarget](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.profilertarget) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listProfilerTargetsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listProfileSessions(request, options)
    
    
    listProfileSessions(request?: protos.google.cloud.hypercomputecluster.v1alpha.IListProfileSessionsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.hypercomputecluster.v1alpha.IProfileSession[],
            protos.google.cloud.hypercomputecluster.v1alpha.IListProfileSessionsRequest | null,
            protos.google.cloud.hypercomputecluster.v1alpha.IListProfileSessionsResponse
        ]>;

Deprecated: Use `ListProfilerSessions` instead. Lists Profile Sessions for a Machine Learning Run.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProfileSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilesessionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.hypercomputecluster.v1alpha.IProfileSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilesession)[], [protos.google.cloud.hypercomputecluster.v1alpha.IListProfileSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilesessionsrequest) | null, [protos.google.cloud.hypercomputecluster.v1alpha.IListProfileSessionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilesessionsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [ProfileSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.profilesession). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listProfileSessionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listProfileSessions(request, options, callback)
    
    
    listProfileSessions(request: protos.google.cloud.hypercomputecluster.v1alpha.IListProfileSessionsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.hypercomputecluster.v1alpha.IListProfileSessionsRequest, protos.google.cloud.hypercomputecluster.v1alpha.IListProfileSessionsResponse | null | undefined, protos.google.cloud.hypercomputecluster.v1alpha.IProfileSession>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProfileSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilesessionsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.hypercomputecluster.v1alpha.IListProfileSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilesessionsrequest), [protos.google.cloud.hypercomputecluster.v1alpha.IListProfileSessionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilesessionsresponse) | null | undefined, [protos.google.cloud.hypercomputecluster.v1alpha.IProfileSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilesession)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProfileSessions(request, callback)
    
    
    listProfileSessions(request: protos.google.cloud.hypercomputecluster.v1alpha.IListProfileSessionsRequest, callback: PaginationCallback<protos.google.cloud.hypercomputecluster.v1alpha.IListProfileSessionsRequest, protos.google.cloud.hypercomputecluster.v1alpha.IListProfileSessionsResponse | null | undefined, protos.google.cloud.hypercomputecluster.v1alpha.IProfileSession>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProfileSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilesessionsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.hypercomputecluster.v1alpha.IListProfileSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilesessionsrequest), [protos.google.cloud.hypercomputecluster.v1alpha.IListProfileSessionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilesessionsresponse) | null | undefined, [protos.google.cloud.hypercomputecluster.v1alpha.IProfileSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilesession)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProfileSessionsAsync(request, options)
    
    
    listProfileSessionsAsync(request?: protos.google.cloud.hypercomputecluster.v1alpha.IListProfileSessionsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.hypercomputecluster.v1alpha.IProfileSession>;

Equivalent to `listProfileSessions`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProfileSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilesessionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.hypercomputecluster.v1alpha.IProfileSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iprofilesession)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [ProfileSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.profilesession). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent format:
       *  projects/{project}/locations/{location}/machineLearningRuns/{machine_learning_run}
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of Profile Sessions to return. The service may
       *  return fewer than this value.
       *  If unspecified, at most 50 Profile Sessions will be returned.
       *  The maximum value is 1000; values above 1000 will be coerced to 1000.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListProfileSessions`
       *  call. Provide this to retrieve the subsequent page.
       */
      // const pageToken = 'abc123'
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callListProfileSessions() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = hypercomputeclusterClient.[listProfileSessionsAsync](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListProfileSessions();
    
    

### listProfileSessionsStream(request, options)
    
    
    listProfileSessionsStream(request?: protos.google.cloud.hypercomputecluster.v1alpha.IListProfileSessionsRequest, options?: CallOptions): Transform;

Equivalent to `listProfileSessions`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProfileSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ilistprofilesessionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [ProfileSession](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.profilesession) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listProfileSessionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### updateMachineLearningRun(request, options)
    
    
    updateMachineLearningRun(request?: protos.google.cloud.hypercomputecluster.v1alpha.IUpdateMachineLearningRunRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates an Machine Learning Run.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMachineLearningRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iupdatemachinelearningrunrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imachinelearningrun), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Machine Learning Run to update.
       */
      // const machineLearningRun = {}
      /**
       *  Optional. Used to identify fields to be updated. Allowed fields is *, we
       *  don't support partial updates.
       */
      // const updateMask = {}
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callUpdateMachineLearningRun() {
        // Construct request
        const request = {
          machineLearningRun,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.updateMachineLearningRun(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateMachineLearningRun();
    
    

### updateMachineLearningRun(request, options, callback)
    
    
    updateMachineLearningRun(request: protos.google.cloud.hypercomputecluster.v1alpha.IUpdateMachineLearningRunRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMachineLearningRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iupdatemachinelearningrunrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imachinelearningrun), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMachineLearningRun(request, callback)
    
    
    updateMachineLearningRun(request: protos.google.cloud.hypercomputecluster.v1alpha.IUpdateMachineLearningRunRequest, callback: Callback<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMachineLearningRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iupdatemachinelearningrunrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.IMachineLearningRun](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imachinelearningrun), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMonitoredEvent(request, options)
    
    
    updateMonitoredEvent(request?: protos.google.cloud.hypercomputecluster.v1alpha.IUpdateMonitoredEventRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates a Monitored Event.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMonitoredEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iupdatemonitoredeventrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imonitoredevent), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The monitored event to update.
       *  The event's `name` field is used to identify the event to be updated.
       */
      // const monitoredEvent = {}
      /**
       *  Optional. The list of fields to be updated.
       */
      // const updateMask = {}
    
      // Imports the Hypercomputecluster library
      const {MachineLearningRunsClient} = require('[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const hypercomputeclusterClient = new [MachineLearningRunsClient](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/v1alpha.machinelearningrunsclient.html)();
    
      async function callUpdateMonitoredEvent() {
        // Construct request
        const request = {
          monitoredEvent,
        };
    
        // Run request
        const [operation] = await hypercomputeclusterClient.updateMonitoredEvent(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateMonitoredEvent();
    
    

### updateMonitoredEvent(request, options, callback)
    
    
    updateMonitoredEvent(request: protos.google.cloud.hypercomputecluster.v1alpha.IUpdateMonitoredEventRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMonitoredEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iupdatemonitoredeventrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imonitoredevent), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMonitoredEvent(request, callback)
    
    
    updateMonitoredEvent(request: protos.google.cloud.hypercomputecluster.v1alpha.IUpdateMonitoredEventRequest, callback: Callback<LROperation<protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent, protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMonitoredEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.iupdatemonitoredeventrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.hypercomputecluster.v1alpha.IMonitoredEvent](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.imonitoredevent), [protos.google.cloud.hypercomputecluster.v1alpha.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
