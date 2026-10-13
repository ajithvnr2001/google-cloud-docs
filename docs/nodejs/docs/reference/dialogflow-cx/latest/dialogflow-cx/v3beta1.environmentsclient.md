---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/v3beta1.environmentsclient
title: Class v3beta1.EnvironmentsClient (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:52:05.296972+00:00
---

# Class v3beta1.EnvironmentsClient (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/v3beta1.environmentsclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v3beta1.EnvironmentsClient (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.6.0  5.5.0  5.1.0  5.0.1  4.10.0  4.9.0  4.8.0  4.6.0  4.3.1  4.2.0  4.0.0  3.4.2  3.2.1  3.1.2  2.15.0  2.14.0  2.13.0  2.12.1 

Service for managing . v3beta1

## Package

[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of EnvironmentsClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new EnvironmentsClient({fallback: true}, gax); ```  
  
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

### environmentsStub
    
    
    environmentsStub?: Promise<{
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

### agentGenerativeSettingsPath(project, location, agent)
    
    
    agentGenerativeSettingsPath(project: string, location: string, agent: string): string;

Return a fully-qualified agentGenerativeSettings resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### agentPath(project, location, agent)
    
    
    agentPath(project: string, location: string, agent: string): string;

Return a fully-qualified agent resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### agentValidationResultPath(project, location, agent)
    
    
    agentValidationResultPath(project: string, location: string, agent: string): string;

Return a fully-qualified agentValidationResult resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
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
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### changelogPath(project, location, agent, changelog)
    
    
    changelogPath(project: string, location: string, agent: string, changelog: string): string;

Return a fully-qualified changelog resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`changelog` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### checkCreateEnvironmentProgress(name)
    
    
    checkCreateEnvironmentProgress(name: string): Promise<LROperation<protos.google.cloud.dialogflow.cx.v3beta1.Environment, protos.google.protobuf.Struct>>;

Check the status of the long running operation returned by `createEnvironment()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.Environment](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.environment-class), [protos.google.protobuf.Struct](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.struct)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Agent google.cloud.dialogflow.cx.v3beta1.Agent  to create
       *  an Environment google.cloud.dialogflow.cx.v3beta1.Environment  for.
       *  Format: `projects/

### checkDeployFlowProgress(name)
    
    
    checkDeployFlowProgress(name: string): Promise<LROperation<protos.google.cloud.dialogflow.cx.v3beta1.DeployFlowResponse, protos.google.cloud.dialogflow.cx.v3beta1.DeployFlowMetadata>>;

Check the status of the long running operation returned by `deployFlow()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.DeployFlowResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.deployflowresponse), [protos.google.cloud.dialogflow.cx.v3beta1.DeployFlowMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.deployflowmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The environment to deploy the flow to.
       *  Format:
       *  `projects/

### checkRunContinuousTestProgress(name)
    
    
    checkRunContinuousTestProgress(name: string): Promise<LROperation<protos.google.cloud.dialogflow.cx.v3beta1.RunContinuousTestResponse, protos.google.cloud.dialogflow.cx.v3beta1.RunContinuousTestMetadata>>;

Check the status of the long running operation returned by `runContinuousTest()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.RunContinuousTestResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.runcontinuoustestresponse), [protos.google.cloud.dialogflow.cx.v3beta1.RunContinuousTestMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.runcontinuoustestmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Format:
       *  `projects/

### checkUpdateEnvironmentProgress(name)
    
    
    checkUpdateEnvironmentProgress(name: string): Promise<LROperation<protos.google.cloud.dialogflow.cx.v3beta1.Environment, protos.google.protobuf.Struct>>;

Check the status of the long running operation returned by `updateEnvironment()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.Environment](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.environment-class), [protos.google.protobuf.Struct](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.struct)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The environment to update.
       */
      // const environment = {}
      /**
       *  Required. The mask to control which fields get updated.
       */
      // const updateMask = {}
    
      // Imports the Cx library
      const {EnvironmentsClient} = require('[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)').v3beta1;
    
      // Instantiates a client
      const cxClient = new [EnvironmentsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)();
    
      async function callUpdateEnvironment() {
        // Construct request
        const request = {
          environment,
          updateMask,
        };
    
        // Run request
        const [operation] = await cxClient.updateEnvironment(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateEnvironment();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### continuousTestResultPath(project, location, agent, environment, continuousTestResult)
    
    
    continuousTestResultPath(project: string, location: string, agent: string, environment: string, continuousTestResult: string): string;

Return a fully-qualified continuousTestResult resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`environment` |  `string`   
  
`continuousTestResult` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### conversationPath(project, location, agent, conversation)
    
    
    conversationPath(project: string, location: string, agent: string, conversation: string): string;

Return a fully-qualified conversation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`conversation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### createEnvironment(request, options)
    
    
    createEnvironment(request?: protos.google.cloud.dialogflow.cx.v3beta1.ICreateEnvironmentRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment, protos.google.protobuf.IStruct>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates an in the specified .

This method is a [long-running operation](<https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`:



**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEnvironmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.icreateenvironmentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ienvironment), [protos.google.protobuf.IStruct](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.istruct)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Agent google.cloud.dialogflow.cx.v3beta1.Agent  to create
       *  an Environment google.cloud.dialogflow.cx.v3beta1.Environment  for.
       *  Format: `projects/

### createEnvironment(request, options, callback)
    
    
    createEnvironment(request: protos.google.cloud.dialogflow.cx.v3beta1.ICreateEnvironmentRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment, protos.google.protobuf.IStruct>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEnvironmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.icreateenvironmentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ienvironment), [protos.google.protobuf.IStruct](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.istruct)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEnvironment(request, callback)
    
    
    createEnvironment(request: protos.google.cloud.dialogflow.cx.v3beta1.ICreateEnvironmentRequest, callback: Callback<LROperation<protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment, protos.google.protobuf.IStruct>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEnvironmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.icreateenvironmentrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ienvironment), [protos.google.protobuf.IStruct](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.istruct)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEnvironment(request, options)
    
    
    deleteEnvironment(request?: protos.google.cloud.dialogflow.cx.v3beta1.IDeleteEnvironmentRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.dialogflow.cx.v3beta1.IDeleteEnvironmentRequest | undefined),
            {} | undefined
        ]>;

Deletes the specified .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEnvironmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideleteenvironmentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.iempty), ([protos.google.cloud.dialogflow.cx.v3beta1.IDeleteEnvironmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideleteenvironmentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the
       *  Environment google.cloud.dialogflow.cx.v3beta1.Environment  to delete.
       *  Format:
       *  `projects/

### deleteEnvironment(request, options, callback)
    
    
    deleteEnvironment(request: protos.google.cloud.dialogflow.cx.v3beta1.IDeleteEnvironmentRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dialogflow.cx.v3beta1.IDeleteEnvironmentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEnvironmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideleteenvironmentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.iempty), [protos.google.cloud.dialogflow.cx.v3beta1.IDeleteEnvironmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideleteenvironmentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEnvironment(request, callback)
    
    
    deleteEnvironment(request: protos.google.cloud.dialogflow.cx.v3beta1.IDeleteEnvironmentRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dialogflow.cx.v3beta1.IDeleteEnvironmentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEnvironmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideleteenvironmentrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.iempty), [protos.google.cloud.dialogflow.cx.v3beta1.IDeleteEnvironmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideleteenvironmentrequest) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### deployFlow(request, options)
    
    
    deployFlow(request?: protos.google.cloud.dialogflow.cx.v3beta1.IDeployFlowRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.dialogflow.cx.v3beta1.IDeployFlowResponse, protos.google.cloud.dialogflow.cx.v3beta1.IDeployFlowMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deploys a flow to the specified .

This method is a [long-running operation](<https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned `Operation` type has the following method-specific fields:

  * `metadata`: [DeployFlowMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.deployflowmetadata) \- `response`: [DeployFlowResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.deployflowresponse)



**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeployFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideployflowrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.IDeployFlowResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideployflowresponse), [protos.google.cloud.dialogflow.cx.v3beta1.IDeployFlowMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideployflowmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The environment to deploy the flow to.
       *  Format:
       *  `projects/

### deployFlow(request, options, callback)
    
    
    deployFlow(request: protos.google.cloud.dialogflow.cx.v3beta1.IDeployFlowRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.dialogflow.cx.v3beta1.IDeployFlowResponse, protos.google.cloud.dialogflow.cx.v3beta1.IDeployFlowMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeployFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideployflowrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.IDeployFlowResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideployflowresponse), [protos.google.cloud.dialogflow.cx.v3beta1.IDeployFlowMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideployflowmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deployFlow(request, callback)
    
    
    deployFlow(request: protos.google.cloud.dialogflow.cx.v3beta1.IDeployFlowRequest, callback: Callback<LROperation<protos.google.cloud.dialogflow.cx.v3beta1.IDeployFlowResponse, protos.google.cloud.dialogflow.cx.v3beta1.IDeployFlowMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeployFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideployflowrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.IDeployFlowResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideployflowresponse), [protos.google.cloud.dialogflow.cx.v3beta1.IDeployFlowMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideployflowmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deploymentPath(project, location, agent, environment, deployment)
    
    
    deploymentPath(project: string, location: string, agent: string, environment: string, deployment: string): string;

Return a fully-qualified deployment resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`environment` |  `string`   
  
`deployment` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### entityTypePath(project, location, agent, entityType)
    
    
    entityTypePath(project: string, location: string, agent: string, entityType: string): string;

Return a fully-qualified entityType resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`entityType` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### environmentPath(project, location, agent, environment)
    
    
    environmentPath(project: string, location: string, agent: string, environment: string): string;

Return a fully-qualified environment resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`environment` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### examplePath(project, location, agent, playbook, example)
    
    
    examplePath(project: string, location: string, agent: string, playbook: string, example: string): string;

Return a fully-qualified example resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`playbook` |  `string`   
  
`example` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### experimentPath(project, location, agent, environment, experiment)
    
    
    experimentPath(project: string, location: string, agent: string, environment: string, experiment: string): string;

Return a fully-qualified experiment resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`environment` |  `string`   
  
`experiment` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### flowPath(project, location, agent, flow)
    
    
    flowPath(project: string, location: string, agent: string, flow: string): string;

Return a fully-qualified flow resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`flow` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### flowValidationResultPath(project, location, agent, flow)
    
    
    flowValidationResultPath(project: string, location: string, agent: string, flow: string): string;

Return a fully-qualified flowValidationResult resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`flow` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### generatorPath(project, location, agent, generator)
    
    
    generatorPath(project: string, location: string, agent: string, generator: string): string;

Return a fully-qualified generator resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`generator` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### getEnvironment(request, options)
    
    
    getEnvironment(request?: protos.google.cloud.dialogflow.cx.v3beta1.IGetEnvironmentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment,
            (protos.google.cloud.dialogflow.cx.v3beta1.IGetEnvironmentRequest | undefined),
            {} | undefined
        ]>;

Retrieves the specified .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEnvironmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.igetenvironmentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ienvironment), ([protos.google.cloud.dialogflow.cx.v3beta1.IGetEnvironmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.igetenvironmentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the
       *  Environment google.cloud.dialogflow.cx.v3beta1.Environment. Format:
       *  `projects/

### getEnvironment(request, options, callback)
    
    
    getEnvironment(request: protos.google.cloud.dialogflow.cx.v3beta1.IGetEnvironmentRequest, options: CallOptions, callback: Callback<protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment, protos.google.cloud.dialogflow.cx.v3beta1.IGetEnvironmentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEnvironmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.igetenvironmentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ienvironment), [protos.google.cloud.dialogflow.cx.v3beta1.IGetEnvironmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.igetenvironmentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEnvironment(request, callback)
    
    
    getEnvironment(request: protos.google.cloud.dialogflow.cx.v3beta1.IGetEnvironmentRequest, callback: Callback<protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment, protos.google.cloud.dialogflow.cx.v3beta1.IGetEnvironmentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEnvironmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.igetenvironmentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ienvironment), [protos.google.cloud.dialogflow.cx.v3beta1.IGetEnvironmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.igetenvironmentrequest) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.operation)]>` |   
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
  
### intentPath(project, location, agent, intent)
    
    
    intentPath(project: string, location: string, agent: string, intent: string): string;

Return a fully-qualified intent resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`intent` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### listContinuousTestResults(request, options)
    
    
    listContinuousTestResults(request?: protos.google.cloud.dialogflow.cx.v3beta1.IListContinuousTestResultsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dialogflow.cx.v3beta1.IContinuousTestResult[],
            protos.google.cloud.dialogflow.cx.v3beta1.IListContinuousTestResultsRequest | null,
            protos.google.cloud.dialogflow.cx.v3beta1.IListContinuousTestResultsResponse
        ]>;

Fetches a list of continuous test results for a given environment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListContinuousTestResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistcontinuoustestresultsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dialogflow.cx.v3beta1.IContinuousTestResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.icontinuoustestresult)[], [protos.google.cloud.dialogflow.cx.v3beta1.IListContinuousTestResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistcontinuoustestresultsrequest) | null, [protos.google.cloud.dialogflow.cx.v3beta1.IListContinuousTestResultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistcontinuoustestresultsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listContinuousTestResultsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listContinuousTestResults(request, options, callback)
    
    
    listContinuousTestResults(request: protos.google.cloud.dialogflow.cx.v3beta1.IListContinuousTestResultsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dialogflow.cx.v3beta1.IListContinuousTestResultsRequest, protos.google.cloud.dialogflow.cx.v3beta1.IListContinuousTestResultsResponse | null | undefined, protos.google.cloud.dialogflow.cx.v3beta1.IContinuousTestResult>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListContinuousTestResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistcontinuoustestresultsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dialogflow.cx.v3beta1.IListContinuousTestResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistcontinuoustestresultsrequest), [protos.google.cloud.dialogflow.cx.v3beta1.IListContinuousTestResultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistcontinuoustestresultsresponse) | null | undefined, [protos.google.cloud.dialogflow.cx.v3beta1.IContinuousTestResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.icontinuoustestresult)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listContinuousTestResults(request, callback)
    
    
    listContinuousTestResults(request: protos.google.cloud.dialogflow.cx.v3beta1.IListContinuousTestResultsRequest, callback: PaginationCallback<protos.google.cloud.dialogflow.cx.v3beta1.IListContinuousTestResultsRequest, protos.google.cloud.dialogflow.cx.v3beta1.IListContinuousTestResultsResponse | null | undefined, protos.google.cloud.dialogflow.cx.v3beta1.IContinuousTestResult>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListContinuousTestResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistcontinuoustestresultsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dialogflow.cx.v3beta1.IListContinuousTestResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistcontinuoustestresultsrequest), [protos.google.cloud.dialogflow.cx.v3beta1.IListContinuousTestResultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistcontinuoustestresultsresponse) | null | undefined, [protos.google.cloud.dialogflow.cx.v3beta1.IContinuousTestResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.icontinuoustestresult)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listContinuousTestResultsAsync(request, options)
    
    
    listContinuousTestResultsAsync(request?: protos.google.cloud.dialogflow.cx.v3beta1.IListContinuousTestResultsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dialogflow.cx.v3beta1.IContinuousTestResult>;

Equivalent to `listContinuousTestResults`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListContinuousTestResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistcontinuoustestresultsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dialogflow.cx.v3beta1.IContinuousTestResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.icontinuoustestresult)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The environment to list results for.
       *  Format:
       *  `projects/

### listContinuousTestResultsStream(request, options)
    
    
    listContinuousTestResultsStream(request?: protos.google.cloud.dialogflow.cx.v3beta1.IListContinuousTestResultsRequest, options?: CallOptions): Transform;

Equivalent to `listContinuousTestResults`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListContinuousTestResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistcontinuoustestresultsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listContinuousTestResultsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listEnvironments(request, options)
    
    
    listEnvironments(request?: protos.google.cloud.dialogflow.cx.v3beta1.IListEnvironmentsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment[],
            protos.google.cloud.dialogflow.cx.v3beta1.IListEnvironmentsRequest | null,
            protos.google.cloud.dialogflow.cx.v3beta1.IListEnvironmentsResponse
        ]>;

Returns the list of all environments in the specified .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEnvironmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistenvironmentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ienvironment)[], [protos.google.cloud.dialogflow.cx.v3beta1.IListEnvironmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistenvironmentsrequest) | null, [protos.google.cloud.dialogflow.cx.v3beta1.IListEnvironmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistenvironmentsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listEnvironmentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listEnvironments(request, options, callback)
    
    
    listEnvironments(request: protos.google.cloud.dialogflow.cx.v3beta1.IListEnvironmentsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dialogflow.cx.v3beta1.IListEnvironmentsRequest, protos.google.cloud.dialogflow.cx.v3beta1.IListEnvironmentsResponse | null | undefined, protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEnvironmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistenvironmentsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dialogflow.cx.v3beta1.IListEnvironmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistenvironmentsrequest), [protos.google.cloud.dialogflow.cx.v3beta1.IListEnvironmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistenvironmentsresponse) | null | undefined, [protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ienvironment)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEnvironments(request, callback)
    
    
    listEnvironments(request: protos.google.cloud.dialogflow.cx.v3beta1.IListEnvironmentsRequest, callback: PaginationCallback<protos.google.cloud.dialogflow.cx.v3beta1.IListEnvironmentsRequest, protos.google.cloud.dialogflow.cx.v3beta1.IListEnvironmentsResponse | null | undefined, protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEnvironmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistenvironmentsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dialogflow.cx.v3beta1.IListEnvironmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistenvironmentsrequest), [protos.google.cloud.dialogflow.cx.v3beta1.IListEnvironmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistenvironmentsresponse) | null | undefined, [protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ienvironment)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEnvironmentsAsync(request, options)
    
    
    listEnvironmentsAsync(request?: protos.google.cloud.dialogflow.cx.v3beta1.IListEnvironmentsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment>;

Equivalent to `listEnvironments`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEnvironmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistenvironmentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ienvironment)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Agent google.cloud.dialogflow.cx.v3beta1.Agent  to list all
       *  environments for. Format:
       *  `projects/

### listEnvironmentsStream(request, options)
    
    
    listEnvironmentsStream(request?: protos.google.cloud.dialogflow.cx.v3beta1.IListEnvironmentsRequest, options?: CallOptions): Transform;

Equivalent to `listEnvironments`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEnvironmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistenvironmentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listEnvironmentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
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
  
### lookupEnvironmentHistory(request, options)
    
    
    lookupEnvironmentHistory(request?: protos.google.cloud.dialogflow.cx.v3beta1.ILookupEnvironmentHistoryRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment[],
            protos.google.cloud.dialogflow.cx.v3beta1.ILookupEnvironmentHistoryRequest | null,
            protos.google.cloud.dialogflow.cx.v3beta1.ILookupEnvironmentHistoryResponse
        ]>;

Looks up the history of the specified .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILookupEnvironmentHistoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilookupenvironmenthistoryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ienvironment)[], [protos.google.cloud.dialogflow.cx.v3beta1.ILookupEnvironmentHistoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilookupenvironmenthistoryrequest) | null, [protos.google.cloud.dialogflow.cx.v3beta1.ILookupEnvironmentHistoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilookupenvironmenthistoryresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `lookupEnvironmentHistoryAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### lookupEnvironmentHistory(request, options, callback)
    
    
    lookupEnvironmentHistory(request: protos.google.cloud.dialogflow.cx.v3beta1.ILookupEnvironmentHistoryRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dialogflow.cx.v3beta1.ILookupEnvironmentHistoryRequest, protos.google.cloud.dialogflow.cx.v3beta1.ILookupEnvironmentHistoryResponse | null | undefined, protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILookupEnvironmentHistoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilookupenvironmenthistoryrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dialogflow.cx.v3beta1.ILookupEnvironmentHistoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilookupenvironmenthistoryrequest), [protos.google.cloud.dialogflow.cx.v3beta1.ILookupEnvironmentHistoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilookupenvironmenthistoryresponse) | null | undefined, [protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ienvironment)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### lookupEnvironmentHistory(request, callback)
    
    
    lookupEnvironmentHistory(request: protos.google.cloud.dialogflow.cx.v3beta1.ILookupEnvironmentHistoryRequest, callback: PaginationCallback<protos.google.cloud.dialogflow.cx.v3beta1.ILookupEnvironmentHistoryRequest, protos.google.cloud.dialogflow.cx.v3beta1.ILookupEnvironmentHistoryResponse | null | undefined, protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILookupEnvironmentHistoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilookupenvironmenthistoryrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dialogflow.cx.v3beta1.ILookupEnvironmentHistoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilookupenvironmenthistoryrequest), [protos.google.cloud.dialogflow.cx.v3beta1.ILookupEnvironmentHistoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilookupenvironmenthistoryresponse) | null | undefined, [protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ienvironment)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### lookupEnvironmentHistoryAsync(request, options)
    
    
    lookupEnvironmentHistoryAsync(request?: protos.google.cloud.dialogflow.cx.v3beta1.ILookupEnvironmentHistoryRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment>;

Equivalent to `lookupEnvironmentHistory`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILookupEnvironmentHistoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilookupenvironmenthistoryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ienvironment)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name of the environment to look up the history for.
       *  Format:
       *  `projects/

### lookupEnvironmentHistoryStream(request, options)
    
    
    lookupEnvironmentHistoryStream(request?: protos.google.cloud.dialogflow.cx.v3beta1.ILookupEnvironmentHistoryRequest, options?: CallOptions): Transform;

Equivalent to `lookupEnvironmentHistory`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILookupEnvironmentHistoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilookupenvironmenthistoryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `lookupEnvironmentHistoryAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### matchAgentFromAgentGenerativeSettingsName(agentGenerativeSettingsName)
    
    
    matchAgentFromAgentGenerativeSettingsName(agentGenerativeSettingsName: string): string | number;

Parse the agent from AgentGenerativeSettings resource.

**Parameter**  
---  
**Name** | **Description**  
`agentGenerativeSettingsName` |  `string`   
A fully-qualified path representing AgentGenerativeSettings resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromAgentName(agentName)
    
    
    matchAgentFromAgentName(agentName: string): string | number;

Parse the agent from Agent resource.

**Parameter**  
---  
**Name** | **Description**  
`agentName` |  `string`   
A fully-qualified path representing Agent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromAgentValidationResultName(agentValidationResultName)
    
    
    matchAgentFromAgentValidationResultName(agentValidationResultName: string): string | number;

Parse the agent from AgentValidationResult resource.

**Parameter**  
---  
**Name** | **Description**  
`agentValidationResultName` |  `string`   
A fully-qualified path representing AgentValidationResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromChangelogName(changelogName)
    
    
    matchAgentFromChangelogName(changelogName: string): string | number;

Parse the agent from Changelog resource.

**Parameter**  
---  
**Name** | **Description**  
`changelogName` |  `string`   
A fully-qualified path representing Changelog resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromContinuousTestResultName(continuousTestResultName)
    
    
    matchAgentFromContinuousTestResultName(continuousTestResultName: string): string | number;

Parse the agent from ContinuousTestResult resource.

**Parameter**  
---  
**Name** | **Description**  
`continuousTestResultName` |  `string`   
A fully-qualified path representing ContinuousTestResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromConversationName(conversationName)
    
    
    matchAgentFromConversationName(conversationName: string): string | number;

Parse the agent from Conversation resource.

**Parameter**  
---  
**Name** | **Description**  
`conversationName` |  `string`   
A fully-qualified path representing Conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromDeploymentName(deploymentName)
    
    
    matchAgentFromDeploymentName(deploymentName: string): string | number;

Parse the agent from Deployment resource.

**Parameter**  
---  
**Name** | **Description**  
`deploymentName` |  `string`   
A fully-qualified path representing Deployment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromEntityTypeName(entityTypeName)
    
    
    matchAgentFromEntityTypeName(entityTypeName: string): string | number;

Parse the agent from EntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`entityTypeName` |  `string`   
A fully-qualified path representing EntityType resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromEnvironmentName(environmentName)
    
    
    matchAgentFromEnvironmentName(environmentName: string): string | number;

Parse the agent from Environment resource.

**Parameter**  
---  
**Name** | **Description**  
`environmentName` |  `string`   
A fully-qualified path representing Environment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromExampleName(exampleName)
    
    
    matchAgentFromExampleName(exampleName: string): string | number;

Parse the agent from Example resource.

**Parameter**  
---  
**Name** | **Description**  
`exampleName` |  `string`   
A fully-qualified path representing Example resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromExperimentName(experimentName)
    
    
    matchAgentFromExperimentName(experimentName: string): string | number;

Parse the agent from Experiment resource.

**Parameter**  
---  
**Name** | **Description**  
`experimentName` |  `string`   
A fully-qualified path representing Experiment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromFlowName(flowName)
    
    
    matchAgentFromFlowName(flowName: string): string | number;

Parse the agent from Flow resource.

**Parameter**  
---  
**Name** | **Description**  
`flowName` |  `string`   
A fully-qualified path representing Flow resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromFlowValidationResultName(flowValidationResultName)
    
    
    matchAgentFromFlowValidationResultName(flowValidationResultName: string): string | number;

Parse the agent from FlowValidationResult resource.

**Parameter**  
---  
**Name** | **Description**  
`flowValidationResultName` |  `string`   
A fully-qualified path representing FlowValidationResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromGeneratorName(generatorName)
    
    
    matchAgentFromGeneratorName(generatorName: string): string | number;

Parse the agent from Generator resource.

**Parameter**  
---  
**Name** | **Description**  
`generatorName` |  `string`   
A fully-qualified path representing Generator resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromIntentName(intentName)
    
    
    matchAgentFromIntentName(intentName: string): string | number;

Parse the agent from Intent resource.

**Parameter**  
---  
**Name** | **Description**  
`intentName` |  `string`   
A fully-qualified path representing Intent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromPageName(pageName)
    
    
    matchAgentFromPageName(pageName: string): string | number;

Parse the agent from Page resource.

**Parameter**  
---  
**Name** | **Description**  
`pageName` |  `string`   
A fully-qualified path representing Page resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromPlaybookName(playbookName)
    
    
    matchAgentFromPlaybookName(playbookName: string): string | number;

Parse the agent from Playbook resource.

**Parameter**  
---  
**Name** | **Description**  
`playbookName` |  `string`   
A fully-qualified path representing Playbook resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromPlaybookVersionName(playbookVersionName)
    
    
    matchAgentFromPlaybookVersionName(playbookVersionName: string): string | number;

Parse the agent from PlaybookVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`playbookVersionName` |  `string`   
A fully-qualified path representing PlaybookVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromProjectLocationAgentEnvironmentSessionEntityTypeName(projectLocationAgentEnvironmentSessionEntityTypeName)
    
    
    matchAgentFromProjectLocationAgentEnvironmentSessionEntityTypeName(projectLocationAgentEnvironmentSessionEntityTypeName: string): string | number;

Parse the agent from ProjectLocationAgentEnvironmentSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_environment_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromProjectLocationAgentFlowTransitionRouteGroupsName(projectLocationAgentFlowTransitionRouteGroupsName)
    
    
    matchAgentFromProjectLocationAgentFlowTransitionRouteGroupsName(projectLocationAgentFlowTransitionRouteGroupsName: string): string | number;

Parse the agent from ProjectLocationAgentFlowTransitionRouteGroups resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentFlowTransitionRouteGroupsName` |  `string`   
A fully-qualified path representing project_location_agent_flow_transitionRouteGroups resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromProjectLocationAgentSessionEntityTypeName(projectLocationAgentSessionEntityTypeName)
    
    
    matchAgentFromProjectLocationAgentSessionEntityTypeName(projectLocationAgentSessionEntityTypeName: string): string | number;

Parse the agent from ProjectLocationAgentSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromProjectLocationAgentTransitionRouteGroupsName(projectLocationAgentTransitionRouteGroupsName)
    
    
    matchAgentFromProjectLocationAgentTransitionRouteGroupsName(projectLocationAgentTransitionRouteGroupsName: string): string | number;

Parse the agent from ProjectLocationAgentTransitionRouteGroups resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentTransitionRouteGroupsName` |  `string`   
A fully-qualified path representing project_location_agent_transitionRouteGroups resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromTestCaseName(testCaseName)
    
    
    matchAgentFromTestCaseName(testCaseName: string): string | number;

Parse the agent from TestCase resource.

**Parameter**  
---  
**Name** | **Description**  
`testCaseName` |  `string`   
A fully-qualified path representing TestCase resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromTestCaseResultName(testCaseResultName)
    
    
    matchAgentFromTestCaseResultName(testCaseResultName: string): string | number;

Parse the agent from TestCaseResult resource.

**Parameter**  
---  
**Name** | **Description**  
`testCaseResultName` |  `string`   
A fully-qualified path representing TestCaseResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromToolName(toolName)
    
    
    matchAgentFromToolName(toolName: string): string | number;

Parse the agent from Tool resource.

**Parameter**  
---  
**Name** | **Description**  
`toolName` |  `string`   
A fully-qualified path representing Tool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromToolVersionName(toolVersionName)
    
    
    matchAgentFromToolVersionName(toolVersionName: string): string | number;

Parse the agent from ToolVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`toolVersionName` |  `string`   
A fully-qualified path representing ToolVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromVersionName(versionName)
    
    
    matchAgentFromVersionName(versionName: string): string | number;

Parse the agent from Version resource.

**Parameter**  
---  
**Name** | **Description**  
`versionName` |  `string`   
A fully-qualified path representing Version resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchAgentFromWebhookName(webhookName)
    
    
    matchAgentFromWebhookName(webhookName: string): string | number;

Parse the agent from Webhook resource.

**Parameter**  
---  
**Name** | **Description**  
`webhookName` |  `string`   
A fully-qualified path representing Webhook resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the agent.  
  
### matchChangelogFromChangelogName(changelogName)
    
    
    matchChangelogFromChangelogName(changelogName: string): string | number;

Parse the changelog from Changelog resource.

**Parameter**  
---  
**Name** | **Description**  
`changelogName` |  `string`   
A fully-qualified path representing Changelog resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the changelog.  
  
### matchContinuousTestResultFromContinuousTestResultName(continuousTestResultName)
    
    
    matchContinuousTestResultFromContinuousTestResultName(continuousTestResultName: string): string | number;

Parse the continuous_test_result from ContinuousTestResult resource.

**Parameter**  
---  
**Name** | **Description**  
`continuousTestResultName` |  `string`   
A fully-qualified path representing ContinuousTestResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the continuous_test_result.  
  
### matchConversationFromConversationName(conversationName)
    
    
    matchConversationFromConversationName(conversationName: string): string | number;

Parse the conversation from Conversation resource.

**Parameter**  
---  
**Name** | **Description**  
`conversationName` |  `string`   
A fully-qualified path representing Conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversation.  
  
### matchDeploymentFromDeploymentName(deploymentName)
    
    
    matchDeploymentFromDeploymentName(deploymentName: string): string | number;

Parse the deployment from Deployment resource.

**Parameter**  
---  
**Name** | **Description**  
`deploymentName` |  `string`   
A fully-qualified path representing Deployment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the deployment.  
  
### matchEntityTypeFromEntityTypeName(entityTypeName)
    
    
    matchEntityTypeFromEntityTypeName(entityTypeName: string): string | number;

Parse the entity_type from EntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`entityTypeName` |  `string`   
A fully-qualified path representing EntityType resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the entity_type.  
  
### matchEntityTypeFromProjectLocationAgentEnvironmentSessionEntityTypeName(projectLocationAgentEnvironmentSessionEntityTypeName)
    
    
    matchEntityTypeFromProjectLocationAgentEnvironmentSessionEntityTypeName(projectLocationAgentEnvironmentSessionEntityTypeName: string): string | number;

Parse the entity_type from ProjectLocationAgentEnvironmentSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_environment_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the entity_type.  
  
### matchEntityTypeFromProjectLocationAgentSessionEntityTypeName(projectLocationAgentSessionEntityTypeName)
    
    
    matchEntityTypeFromProjectLocationAgentSessionEntityTypeName(projectLocationAgentSessionEntityTypeName: string): string | number;

Parse the entity_type from ProjectLocationAgentSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the entity_type.  
  
### matchEnvironmentFromContinuousTestResultName(continuousTestResultName)
    
    
    matchEnvironmentFromContinuousTestResultName(continuousTestResultName: string): string | number;

Parse the environment from ContinuousTestResult resource.

**Parameter**  
---  
**Name** | **Description**  
`continuousTestResultName` |  `string`   
A fully-qualified path representing ContinuousTestResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the environment.  
  
### matchEnvironmentFromDeploymentName(deploymentName)
    
    
    matchEnvironmentFromDeploymentName(deploymentName: string): string | number;

Parse the environment from Deployment resource.

**Parameter**  
---  
**Name** | **Description**  
`deploymentName` |  `string`   
A fully-qualified path representing Deployment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the environment.  
  
### matchEnvironmentFromEnvironmentName(environmentName)
    
    
    matchEnvironmentFromEnvironmentName(environmentName: string): string | number;

Parse the environment from Environment resource.

**Parameter**  
---  
**Name** | **Description**  
`environmentName` |  `string`   
A fully-qualified path representing Environment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the environment.  
  
### matchEnvironmentFromExperimentName(experimentName)
    
    
    matchEnvironmentFromExperimentName(experimentName: string): string | number;

Parse the environment from Experiment resource.

**Parameter**  
---  
**Name** | **Description**  
`experimentName` |  `string`   
A fully-qualified path representing Experiment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the environment.  
  
### matchEnvironmentFromProjectLocationAgentEnvironmentSessionEntityTypeName(projectLocationAgentEnvironmentSessionEntityTypeName)
    
    
    matchEnvironmentFromProjectLocationAgentEnvironmentSessionEntityTypeName(projectLocationAgentEnvironmentSessionEntityTypeName: string): string | number;

Parse the environment from ProjectLocationAgentEnvironmentSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_environment_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the environment.  
  
### matchExampleFromExampleName(exampleName)
    
    
    matchExampleFromExampleName(exampleName: string): string | number;

Parse the example from Example resource.

**Parameter**  
---  
**Name** | **Description**  
`exampleName` |  `string`   
A fully-qualified path representing Example resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the example.  
  
### matchExperimentFromExperimentName(experimentName)
    
    
    matchExperimentFromExperimentName(experimentName: string): string | number;

Parse the experiment from Experiment resource.

**Parameter**  
---  
**Name** | **Description**  
`experimentName` |  `string`   
A fully-qualified path representing Experiment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the experiment.  
  
### matchFlowFromFlowName(flowName)
    
    
    matchFlowFromFlowName(flowName: string): string | number;

Parse the flow from Flow resource.

**Parameter**  
---  
**Name** | **Description**  
`flowName` |  `string`   
A fully-qualified path representing Flow resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the flow.  
  
### matchFlowFromFlowValidationResultName(flowValidationResultName)
    
    
    matchFlowFromFlowValidationResultName(flowValidationResultName: string): string | number;

Parse the flow from FlowValidationResult resource.

**Parameter**  
---  
**Name** | **Description**  
`flowValidationResultName` |  `string`   
A fully-qualified path representing FlowValidationResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the flow.  
  
### matchFlowFromPageName(pageName)
    
    
    matchFlowFromPageName(pageName: string): string | number;

Parse the flow from Page resource.

**Parameter**  
---  
**Name** | **Description**  
`pageName` |  `string`   
A fully-qualified path representing Page resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the flow.  
  
### matchFlowFromProjectLocationAgentFlowTransitionRouteGroupsName(projectLocationAgentFlowTransitionRouteGroupsName)
    
    
    matchFlowFromProjectLocationAgentFlowTransitionRouteGroupsName(projectLocationAgentFlowTransitionRouteGroupsName: string): string | number;

Parse the flow from ProjectLocationAgentFlowTransitionRouteGroups resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentFlowTransitionRouteGroupsName` |  `string`   
A fully-qualified path representing project_location_agent_flow_transitionRouteGroups resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the flow.  
  
### matchFlowFromVersionName(versionName)
    
    
    matchFlowFromVersionName(versionName: string): string | number;

Parse the flow from Version resource.

**Parameter**  
---  
**Name** | **Description**  
`versionName` |  `string`   
A fully-qualified path representing Version resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the flow.  
  
### matchGeneratorFromGeneratorName(generatorName)
    
    
    matchGeneratorFromGeneratorName(generatorName: string): string | number;

Parse the generator from Generator resource.

**Parameter**  
---  
**Name** | **Description**  
`generatorName` |  `string`   
A fully-qualified path representing Generator resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the generator.  
  
### matchIntentFromIntentName(intentName)
    
    
    matchIntentFromIntentName(intentName: string): string | number;

Parse the intent from Intent resource.

**Parameter**  
---  
**Name** | **Description**  
`intentName` |  `string`   
A fully-qualified path representing Intent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the intent.  
  
### matchLocationFromAgentGenerativeSettingsName(agentGenerativeSettingsName)
    
    
    matchLocationFromAgentGenerativeSettingsName(agentGenerativeSettingsName: string): string | number;

Parse the location from AgentGenerativeSettings resource.

**Parameter**  
---  
**Name** | **Description**  
`agentGenerativeSettingsName` |  `string`   
A fully-qualified path representing AgentGenerativeSettings resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromAgentName(agentName)
    
    
    matchLocationFromAgentName(agentName: string): string | number;

Parse the location from Agent resource.

**Parameter**  
---  
**Name** | **Description**  
`agentName` |  `string`   
A fully-qualified path representing Agent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromAgentValidationResultName(agentValidationResultName)
    
    
    matchLocationFromAgentValidationResultName(agentValidationResultName: string): string | number;

Parse the location from AgentValidationResult resource.

**Parameter**  
---  
**Name** | **Description**  
`agentValidationResultName` |  `string`   
A fully-qualified path representing AgentValidationResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromChangelogName(changelogName)
    
    
    matchLocationFromChangelogName(changelogName: string): string | number;

Parse the location from Changelog resource.

**Parameter**  
---  
**Name** | **Description**  
`changelogName` |  `string`   
A fully-qualified path representing Changelog resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromContinuousTestResultName(continuousTestResultName)
    
    
    matchLocationFromContinuousTestResultName(continuousTestResultName: string): string | number;

Parse the location from ContinuousTestResult resource.

**Parameter**  
---  
**Name** | **Description**  
`continuousTestResultName` |  `string`   
A fully-qualified path representing ContinuousTestResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromConversationName(conversationName)
    
    
    matchLocationFromConversationName(conversationName: string): string | number;

Parse the location from Conversation resource.

**Parameter**  
---  
**Name** | **Description**  
`conversationName` |  `string`   
A fully-qualified path representing Conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromDeploymentName(deploymentName)
    
    
    matchLocationFromDeploymentName(deploymentName: string): string | number;

Parse the location from Deployment resource.

**Parameter**  
---  
**Name** | **Description**  
`deploymentName` |  `string`   
A fully-qualified path representing Deployment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromEntityTypeName(entityTypeName)
    
    
    matchLocationFromEntityTypeName(entityTypeName: string): string | number;

Parse the location from EntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`entityTypeName` |  `string`   
A fully-qualified path representing EntityType resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromEnvironmentName(environmentName)
    
    
    matchLocationFromEnvironmentName(environmentName: string): string | number;

Parse the location from Environment resource.

**Parameter**  
---  
**Name** | **Description**  
`environmentName` |  `string`   
A fully-qualified path representing Environment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromExampleName(exampleName)
    
    
    matchLocationFromExampleName(exampleName: string): string | number;

Parse the location from Example resource.

**Parameter**  
---  
**Name** | **Description**  
`exampleName` |  `string`   
A fully-qualified path representing Example resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromExperimentName(experimentName)
    
    
    matchLocationFromExperimentName(experimentName: string): string | number;

Parse the location from Experiment resource.

**Parameter**  
---  
**Name** | **Description**  
`experimentName` |  `string`   
A fully-qualified path representing Experiment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromFlowName(flowName)
    
    
    matchLocationFromFlowName(flowName: string): string | number;

Parse the location from Flow resource.

**Parameter**  
---  
**Name** | **Description**  
`flowName` |  `string`   
A fully-qualified path representing Flow resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromFlowValidationResultName(flowValidationResultName)
    
    
    matchLocationFromFlowValidationResultName(flowValidationResultName: string): string | number;

Parse the location from FlowValidationResult resource.

**Parameter**  
---  
**Name** | **Description**  
`flowValidationResultName` |  `string`   
A fully-qualified path representing FlowValidationResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromGeneratorName(generatorName)
    
    
    matchLocationFromGeneratorName(generatorName: string): string | number;

Parse the location from Generator resource.

**Parameter**  
---  
**Name** | **Description**  
`generatorName` |  `string`   
A fully-qualified path representing Generator resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromIntentName(intentName)
    
    
    matchLocationFromIntentName(intentName: string): string | number;

Parse the location from Intent resource.

**Parameter**  
---  
**Name** | **Description**  
`intentName` |  `string`   
A fully-qualified path representing Intent resource.  
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
  
### matchLocationFromPageName(pageName)
    
    
    matchLocationFromPageName(pageName: string): string | number;

Parse the location from Page resource.

**Parameter**  
---  
**Name** | **Description**  
`pageName` |  `string`   
A fully-qualified path representing Page resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromPlaybookName(playbookName)
    
    
    matchLocationFromPlaybookName(playbookName: string): string | number;

Parse the location from Playbook resource.

**Parameter**  
---  
**Name** | **Description**  
`playbookName` |  `string`   
A fully-qualified path representing Playbook resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromPlaybookVersionName(playbookVersionName)
    
    
    matchLocationFromPlaybookVersionName(playbookVersionName: string): string | number;

Parse the location from PlaybookVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`playbookVersionName` |  `string`   
A fully-qualified path representing PlaybookVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationAgentEnvironmentSessionEntityTypeName(projectLocationAgentEnvironmentSessionEntityTypeName)
    
    
    matchLocationFromProjectLocationAgentEnvironmentSessionEntityTypeName(projectLocationAgentEnvironmentSessionEntityTypeName: string): string | number;

Parse the location from ProjectLocationAgentEnvironmentSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_environment_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationAgentFlowTransitionRouteGroupsName(projectLocationAgentFlowTransitionRouteGroupsName)
    
    
    matchLocationFromProjectLocationAgentFlowTransitionRouteGroupsName(projectLocationAgentFlowTransitionRouteGroupsName: string): string | number;

Parse the location from ProjectLocationAgentFlowTransitionRouteGroups resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentFlowTransitionRouteGroupsName` |  `string`   
A fully-qualified path representing project_location_agent_flow_transitionRouteGroups resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationAgentSessionEntityTypeName(projectLocationAgentSessionEntityTypeName)
    
    
    matchLocationFromProjectLocationAgentSessionEntityTypeName(projectLocationAgentSessionEntityTypeName: string): string | number;

Parse the location from ProjectLocationAgentSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationAgentTransitionRouteGroupsName(projectLocationAgentTransitionRouteGroupsName)
    
    
    matchLocationFromProjectLocationAgentTransitionRouteGroupsName(projectLocationAgentTransitionRouteGroupsName: string): string | number;

Parse the location from ProjectLocationAgentTransitionRouteGroups resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentTransitionRouteGroupsName` |  `string`   
A fully-qualified path representing project_location_agent_transitionRouteGroups resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSecuritySettingsName(securitySettingsName)
    
    
    matchLocationFromSecuritySettingsName(securitySettingsName: string): string | number;

Parse the location from SecuritySettings resource.

**Parameter**  
---  
**Name** | **Description**  
`securitySettingsName` |  `string`   
A fully-qualified path representing SecuritySettings resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTestCaseName(testCaseName)
    
    
    matchLocationFromTestCaseName(testCaseName: string): string | number;

Parse the location from TestCase resource.

**Parameter**  
---  
**Name** | **Description**  
`testCaseName` |  `string`   
A fully-qualified path representing TestCase resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTestCaseResultName(testCaseResultName)
    
    
    matchLocationFromTestCaseResultName(testCaseResultName: string): string | number;

Parse the location from TestCaseResult resource.

**Parameter**  
---  
**Name** | **Description**  
`testCaseResultName` |  `string`   
A fully-qualified path representing TestCaseResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromToolName(toolName)
    
    
    matchLocationFromToolName(toolName: string): string | number;

Parse the location from Tool resource.

**Parameter**  
---  
**Name** | **Description**  
`toolName` |  `string`   
A fully-qualified path representing Tool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromToolVersionName(toolVersionName)
    
    
    matchLocationFromToolVersionName(toolVersionName: string): string | number;

Parse the location from ToolVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`toolVersionName` |  `string`   
A fully-qualified path representing ToolVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromVersionName(versionName)
    
    
    matchLocationFromVersionName(versionName: string): string | number;

Parse the location from Version resource.

**Parameter**  
---  
**Name** | **Description**  
`versionName` |  `string`   
A fully-qualified path representing Version resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromWebhookName(webhookName)
    
    
    matchLocationFromWebhookName(webhookName: string): string | number;

Parse the location from Webhook resource.

**Parameter**  
---  
**Name** | **Description**  
`webhookName` |  `string`   
A fully-qualified path representing Webhook resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchPageFromPageName(pageName)
    
    
    matchPageFromPageName(pageName: string): string | number;

Parse the page from Page resource.

**Parameter**  
---  
**Name** | **Description**  
`pageName` |  `string`   
A fully-qualified path representing Page resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the page.  
  
### matchPlaybookFromExampleName(exampleName)
    
    
    matchPlaybookFromExampleName(exampleName: string): string | number;

Parse the playbook from Example resource.

**Parameter**  
---  
**Name** | **Description**  
`exampleName` |  `string`   
A fully-qualified path representing Example resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the playbook.  
  
### matchPlaybookFromPlaybookName(playbookName)
    
    
    matchPlaybookFromPlaybookName(playbookName: string): string | number;

Parse the playbook from Playbook resource.

**Parameter**  
---  
**Name** | **Description**  
`playbookName` |  `string`   
A fully-qualified path representing Playbook resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the playbook.  
  
### matchPlaybookFromPlaybookVersionName(playbookVersionName)
    
    
    matchPlaybookFromPlaybookVersionName(playbookVersionName: string): string | number;

Parse the playbook from PlaybookVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`playbookVersionName` |  `string`   
A fully-qualified path representing PlaybookVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the playbook.  
  
### matchProjectFromAgentGenerativeSettingsName(agentGenerativeSettingsName)
    
    
    matchProjectFromAgentGenerativeSettingsName(agentGenerativeSettingsName: string): string | number;

Parse the project from AgentGenerativeSettings resource.

**Parameter**  
---  
**Name** | **Description**  
`agentGenerativeSettingsName` |  `string`   
A fully-qualified path representing AgentGenerativeSettings resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromAgentName(agentName)
    
    
    matchProjectFromAgentName(agentName: string): string | number;

Parse the project from Agent resource.

**Parameter**  
---  
**Name** | **Description**  
`agentName` |  `string`   
A fully-qualified path representing Agent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromAgentValidationResultName(agentValidationResultName)
    
    
    matchProjectFromAgentValidationResultName(agentValidationResultName: string): string | number;

Parse the project from AgentValidationResult resource.

**Parameter**  
---  
**Name** | **Description**  
`agentValidationResultName` |  `string`   
A fully-qualified path representing AgentValidationResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromChangelogName(changelogName)
    
    
    matchProjectFromChangelogName(changelogName: string): string | number;

Parse the project from Changelog resource.

**Parameter**  
---  
**Name** | **Description**  
`changelogName` |  `string`   
A fully-qualified path representing Changelog resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromContinuousTestResultName(continuousTestResultName)
    
    
    matchProjectFromContinuousTestResultName(continuousTestResultName: string): string | number;

Parse the project from ContinuousTestResult resource.

**Parameter**  
---  
**Name** | **Description**  
`continuousTestResultName` |  `string`   
A fully-qualified path representing ContinuousTestResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromConversationName(conversationName)
    
    
    matchProjectFromConversationName(conversationName: string): string | number;

Parse the project from Conversation resource.

**Parameter**  
---  
**Name** | **Description**  
`conversationName` |  `string`   
A fully-qualified path representing Conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromDeploymentName(deploymentName)
    
    
    matchProjectFromDeploymentName(deploymentName: string): string | number;

Parse the project from Deployment resource.

**Parameter**  
---  
**Name** | **Description**  
`deploymentName` |  `string`   
A fully-qualified path representing Deployment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromEntityTypeName(entityTypeName)
    
    
    matchProjectFromEntityTypeName(entityTypeName: string): string | number;

Parse the project from EntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`entityTypeName` |  `string`   
A fully-qualified path representing EntityType resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromEnvironmentName(environmentName)
    
    
    matchProjectFromEnvironmentName(environmentName: string): string | number;

Parse the project from Environment resource.

**Parameter**  
---  
**Name** | **Description**  
`environmentName` |  `string`   
A fully-qualified path representing Environment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromExampleName(exampleName)
    
    
    matchProjectFromExampleName(exampleName: string): string | number;

Parse the project from Example resource.

**Parameter**  
---  
**Name** | **Description**  
`exampleName` |  `string`   
A fully-qualified path representing Example resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromExperimentName(experimentName)
    
    
    matchProjectFromExperimentName(experimentName: string): string | number;

Parse the project from Experiment resource.

**Parameter**  
---  
**Name** | **Description**  
`experimentName` |  `string`   
A fully-qualified path representing Experiment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromFlowName(flowName)
    
    
    matchProjectFromFlowName(flowName: string): string | number;

Parse the project from Flow resource.

**Parameter**  
---  
**Name** | **Description**  
`flowName` |  `string`   
A fully-qualified path representing Flow resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromFlowValidationResultName(flowValidationResultName)
    
    
    matchProjectFromFlowValidationResultName(flowValidationResultName: string): string | number;

Parse the project from FlowValidationResult resource.

**Parameter**  
---  
**Name** | **Description**  
`flowValidationResultName` |  `string`   
A fully-qualified path representing FlowValidationResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromGeneratorName(generatorName)
    
    
    matchProjectFromGeneratorName(generatorName: string): string | number;

Parse the project from Generator resource.

**Parameter**  
---  
**Name** | **Description**  
`generatorName` |  `string`   
A fully-qualified path representing Generator resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromIntentName(intentName)
    
    
    matchProjectFromIntentName(intentName: string): string | number;

Parse the project from Intent resource.

**Parameter**  
---  
**Name** | **Description**  
`intentName` |  `string`   
A fully-qualified path representing Intent resource.  
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
  
### matchProjectFromPageName(pageName)
    
    
    matchProjectFromPageName(pageName: string): string | number;

Parse the project from Page resource.

**Parameter**  
---  
**Name** | **Description**  
`pageName` |  `string`   
A fully-qualified path representing Page resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromPlaybookName(playbookName)
    
    
    matchProjectFromPlaybookName(playbookName: string): string | number;

Parse the project from Playbook resource.

**Parameter**  
---  
**Name** | **Description**  
`playbookName` |  `string`   
A fully-qualified path representing Playbook resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromPlaybookVersionName(playbookVersionName)
    
    
    matchProjectFromPlaybookVersionName(playbookVersionName: string): string | number;

Parse the project from PlaybookVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`playbookVersionName` |  `string`   
A fully-qualified path representing PlaybookVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationAgentEnvironmentSessionEntityTypeName(projectLocationAgentEnvironmentSessionEntityTypeName)
    
    
    matchProjectFromProjectLocationAgentEnvironmentSessionEntityTypeName(projectLocationAgentEnvironmentSessionEntityTypeName: string): string | number;

Parse the project from ProjectLocationAgentEnvironmentSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_environment_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationAgentFlowTransitionRouteGroupsName(projectLocationAgentFlowTransitionRouteGroupsName)
    
    
    matchProjectFromProjectLocationAgentFlowTransitionRouteGroupsName(projectLocationAgentFlowTransitionRouteGroupsName: string): string | number;

Parse the project from ProjectLocationAgentFlowTransitionRouteGroups resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentFlowTransitionRouteGroupsName` |  `string`   
A fully-qualified path representing project_location_agent_flow_transitionRouteGroups resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationAgentSessionEntityTypeName(projectLocationAgentSessionEntityTypeName)
    
    
    matchProjectFromProjectLocationAgentSessionEntityTypeName(projectLocationAgentSessionEntityTypeName: string): string | number;

Parse the project from ProjectLocationAgentSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationAgentTransitionRouteGroupsName(projectLocationAgentTransitionRouteGroupsName)
    
    
    matchProjectFromProjectLocationAgentTransitionRouteGroupsName(projectLocationAgentTransitionRouteGroupsName: string): string | number;

Parse the project from ProjectLocationAgentTransitionRouteGroups resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentTransitionRouteGroupsName` |  `string`   
A fully-qualified path representing project_location_agent_transitionRouteGroups resource.  
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
  
### matchProjectFromSecuritySettingsName(securitySettingsName)
    
    
    matchProjectFromSecuritySettingsName(securitySettingsName: string): string | number;

Parse the project from SecuritySettings resource.

**Parameter**  
---  
**Name** | **Description**  
`securitySettingsName` |  `string`   
A fully-qualified path representing SecuritySettings resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTestCaseName(testCaseName)
    
    
    matchProjectFromTestCaseName(testCaseName: string): string | number;

Parse the project from TestCase resource.

**Parameter**  
---  
**Name** | **Description**  
`testCaseName` |  `string`   
A fully-qualified path representing TestCase resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTestCaseResultName(testCaseResultName)
    
    
    matchProjectFromTestCaseResultName(testCaseResultName: string): string | number;

Parse the project from TestCaseResult resource.

**Parameter**  
---  
**Name** | **Description**  
`testCaseResultName` |  `string`   
A fully-qualified path representing TestCaseResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromToolName(toolName)
    
    
    matchProjectFromToolName(toolName: string): string | number;

Parse the project from Tool resource.

**Parameter**  
---  
**Name** | **Description**  
`toolName` |  `string`   
A fully-qualified path representing Tool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromToolVersionName(toolVersionName)
    
    
    matchProjectFromToolVersionName(toolVersionName: string): string | number;

Parse the project from ToolVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`toolVersionName` |  `string`   
A fully-qualified path representing ToolVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromVersionName(versionName)
    
    
    matchProjectFromVersionName(versionName: string): string | number;

Parse the project from Version resource.

**Parameter**  
---  
**Name** | **Description**  
`versionName` |  `string`   
A fully-qualified path representing Version resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromWebhookName(webhookName)
    
    
    matchProjectFromWebhookName(webhookName: string): string | number;

Parse the project from Webhook resource.

**Parameter**  
---  
**Name** | **Description**  
`webhookName` |  `string`   
A fully-qualified path representing Webhook resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchResultFromTestCaseResultName(testCaseResultName)
    
    
    matchResultFromTestCaseResultName(testCaseResultName: string): string | number;

Parse the result from TestCaseResult resource.

**Parameter**  
---  
**Name** | **Description**  
`testCaseResultName` |  `string`   
A fully-qualified path representing TestCaseResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the result.  
  
### matchSecuritySettingsFromSecuritySettingsName(securitySettingsName)
    
    
    matchSecuritySettingsFromSecuritySettingsName(securitySettingsName: string): string | number;

Parse the security_settings from SecuritySettings resource.

**Parameter**  
---  
**Name** | **Description**  
`securitySettingsName` |  `string`   
A fully-qualified path representing SecuritySettings resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the security_settings.  
  
### matchSessionFromProjectLocationAgentEnvironmentSessionEntityTypeName(projectLocationAgentEnvironmentSessionEntityTypeName)
    
    
    matchSessionFromProjectLocationAgentEnvironmentSessionEntityTypeName(projectLocationAgentEnvironmentSessionEntityTypeName: string): string | number;

Parse the session from ProjectLocationAgentEnvironmentSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_environment_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationAgentSessionEntityTypeName(projectLocationAgentSessionEntityTypeName)
    
    
    matchSessionFromProjectLocationAgentSessionEntityTypeName(projectLocationAgentSessionEntityTypeName: string): string | number;

Parse the session from ProjectLocationAgentSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchTestCaseFromTestCaseName(testCaseName)
    
    
    matchTestCaseFromTestCaseName(testCaseName: string): string | number;

Parse the test_case from TestCase resource.

**Parameter**  
---  
**Name** | **Description**  
`testCaseName` |  `string`   
A fully-qualified path representing TestCase resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the test_case.  
  
### matchTestCaseFromTestCaseResultName(testCaseResultName)
    
    
    matchTestCaseFromTestCaseResultName(testCaseResultName: string): string | number;

Parse the test_case from TestCaseResult resource.

**Parameter**  
---  
**Name** | **Description**  
`testCaseResultName` |  `string`   
A fully-qualified path representing TestCaseResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the test_case.  
  
### matchToolFromToolName(toolName)
    
    
    matchToolFromToolName(toolName: string): string | number;

Parse the tool from Tool resource.

**Parameter**  
---  
**Name** | **Description**  
`toolName` |  `string`   
A fully-qualified path representing Tool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tool.  
  
### matchToolFromToolVersionName(toolVersionName)
    
    
    matchToolFromToolVersionName(toolVersionName: string): string | number;

Parse the tool from ToolVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`toolVersionName` |  `string`   
A fully-qualified path representing ToolVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tool.  
  
### matchTransitionRouteGroupFromProjectLocationAgentFlowTransitionRouteGroupsName(projectLocationAgentFlowTransitionRouteGroupsName)
    
    
    matchTransitionRouteGroupFromProjectLocationAgentFlowTransitionRouteGroupsName(projectLocationAgentFlowTransitionRouteGroupsName: string): string | number;

Parse the transition_route_group from ProjectLocationAgentFlowTransitionRouteGroups resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentFlowTransitionRouteGroupsName` |  `string`   
A fully-qualified path representing project_location_agent_flow_transitionRouteGroups resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the transition_route_group.  
  
### matchTransitionRouteGroupFromProjectLocationAgentTransitionRouteGroupsName(projectLocationAgentTransitionRouteGroupsName)
    
    
    matchTransitionRouteGroupFromProjectLocationAgentTransitionRouteGroupsName(projectLocationAgentTransitionRouteGroupsName: string): string | number;

Parse the transition_route_group from ProjectLocationAgentTransitionRouteGroups resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentTransitionRouteGroupsName` |  `string`   
A fully-qualified path representing project_location_agent_transitionRouteGroups resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the transition_route_group.  
  
### matchVersionFromPlaybookVersionName(playbookVersionName)
    
    
    matchVersionFromPlaybookVersionName(playbookVersionName: string): string | number;

Parse the version from PlaybookVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`playbookVersionName` |  `string`   
A fully-qualified path representing PlaybookVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the version.  
  
### matchVersionFromToolVersionName(toolVersionName)
    
    
    matchVersionFromToolVersionName(toolVersionName: string): string | number;

Parse the version from ToolVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`toolVersionName` |  `string`   
A fully-qualified path representing ToolVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the version.  
  
### matchVersionFromVersionName(versionName)
    
    
    matchVersionFromVersionName(versionName: string): string | number;

Parse the version from Version resource.

**Parameter**  
---  
**Name** | **Description**  
`versionName` |  `string`   
A fully-qualified path representing Version resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the version.  
  
### matchWebhookFromWebhookName(webhookName)
    
    
    matchWebhookFromWebhookName(webhookName: string): string | number;

Parse the webhook from Webhook resource.

**Parameter**  
---  
**Name** | **Description**  
`webhookName` |  `string`   
A fully-qualified path representing Webhook resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the webhook.  
  
### pagePath(project, location, agent, flow, page)
    
    
    pagePath(project: string, location: string, agent: string, flow: string, page: string): string;

Return a fully-qualified page resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`flow` |  `string`   
  
`page` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### playbookPath(project, location, agent, playbook)
    
    
    playbookPath(project: string, location: string, agent: string, playbook: string): string;

Return a fully-qualified playbook resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`playbook` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### playbookVersionPath(project, location, agent, playbook, version)
    
    
    playbookVersionPath(project: string, location: string, agent: string, playbook: string, version: string): string;

Return a fully-qualified playbookVersion resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`playbook` |  `string`   
  
`version` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationAgentEnvironmentSessionEntityTypePath(project, location, agent, environment, session, entityType)
    
    
    projectLocationAgentEnvironmentSessionEntityTypePath(project: string, location: string, agent: string, environment: string, session: string, entityType: string): string;

Return a fully-qualified projectLocationAgentEnvironmentSessionEntityType resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`environment` |  `string`   
  
`session` |  `string`   
  
`entityType` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationAgentFlowTransitionRouteGroupsPath(project, location, agent, flow, transitionRouteGroup)
    
    
    projectLocationAgentFlowTransitionRouteGroupsPath(project: string, location: string, agent: string, flow: string, transitionRouteGroup: string): string;

Return a fully-qualified projectLocationAgentFlowTransitionRouteGroups resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`flow` |  `string`   
  
`transitionRouteGroup` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationAgentSessionEntityTypePath(project, location, agent, session, entityType)
    
    
    projectLocationAgentSessionEntityTypePath(project: string, location: string, agent: string, session: string, entityType: string): string;

Return a fully-qualified projectLocationAgentSessionEntityType resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`session` |  `string`   
  
`entityType` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationAgentTransitionRouteGroupsPath(project, location, agent, transitionRouteGroup)
    
    
    projectLocationAgentTransitionRouteGroupsPath(project: string, location: string, agent: string, transitionRouteGroup: string): string;

Return a fully-qualified projectLocationAgentTransitionRouteGroups resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`transitionRouteGroup` |  `string`   
  
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
  
### runContinuousTest(request, options)
    
    
    runContinuousTest(request?: protos.google.cloud.dialogflow.cx.v3beta1.IRunContinuousTestRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.dialogflow.cx.v3beta1.IRunContinuousTestResponse, protos.google.cloud.dialogflow.cx.v3beta1.IRunContinuousTestMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Kicks off a continuous test under the specified .

This method is a [long-running operation](<https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned `Operation` type has the following method-specific fields:

  * `metadata`: [RunContinuousTestMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.runcontinuoustestmetadata) \- `response`: [RunContinuousTestResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.runcontinuoustestresponse)



**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunContinuousTestRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iruncontinuoustestrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.IRunContinuousTestResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iruncontinuoustestresponse), [protos.google.cloud.dialogflow.cx.v3beta1.IRunContinuousTestMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iruncontinuoustestmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Format:
       *  `projects/

### runContinuousTest(request, options, callback)
    
    
    runContinuousTest(request: protos.google.cloud.dialogflow.cx.v3beta1.IRunContinuousTestRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.dialogflow.cx.v3beta1.IRunContinuousTestResponse, protos.google.cloud.dialogflow.cx.v3beta1.IRunContinuousTestMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunContinuousTestRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iruncontinuoustestrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.IRunContinuousTestResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iruncontinuoustestresponse), [protos.google.cloud.dialogflow.cx.v3beta1.IRunContinuousTestMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iruncontinuoustestmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### runContinuousTest(request, callback)
    
    
    runContinuousTest(request: protos.google.cloud.dialogflow.cx.v3beta1.IRunContinuousTestRequest, callback: Callback<LROperation<protos.google.cloud.dialogflow.cx.v3beta1.IRunContinuousTestResponse, protos.google.cloud.dialogflow.cx.v3beta1.IRunContinuousTestMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunContinuousTestRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iruncontinuoustestrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.IRunContinuousTestResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iruncontinuoustestresponse), [protos.google.cloud.dialogflow.cx.v3beta1.IRunContinuousTestMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iruncontinuoustestmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### securitySettingsPath(project, location, securitySettings)
    
    
    securitySettingsPath(project: string, location: string, securitySettings: string): string;

Return a fully-qualified securitySettings resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`securitySettings` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### testCasePath(project, location, agent, testCase)
    
    
    testCasePath(project: string, location: string, agent: string, testCase: string): string;

Return a fully-qualified testCase resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`testCase` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### testCaseResultPath(project, location, agent, testCase, result)
    
    
    testCaseResultPath(project: string, location: string, agent: string, testCase: string, result: string): string;

Return a fully-qualified testCaseResult resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`testCase` |  `string`   
  
`result` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### toolPath(project, location, agent, tool)
    
    
    toolPath(project: string, location: string, agent: string, tool: string): string;

Return a fully-qualified tool resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`tool` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### toolVersionPath(project, location, agent, tool, version)
    
    
    toolVersionPath(project: string, location: string, agent: string, tool: string, version: string): string;

Return a fully-qualified toolVersion resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`tool` |  `string`   
  
`version` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### updateEnvironment(request, options)
    
    
    updateEnvironment(request?: protos.google.cloud.dialogflow.cx.v3beta1.IUpdateEnvironmentRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment, protos.google.protobuf.IStruct>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the specified .

This method is a [long-running operation](<https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`:



**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEnvironmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iupdateenvironmentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ienvironment), [protos.google.protobuf.IStruct](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.istruct)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The environment to update.
       */
      // const environment = {}
      /**
       *  Required. The mask to control which fields get updated.
       */
      // const updateMask = {}
    
      // Imports the Cx library
      const {EnvironmentsClient} = require('[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)').v3beta1;
    
      // Instantiates a client
      const cxClient = new [EnvironmentsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)();
    
      async function callUpdateEnvironment() {
        // Construct request
        const request = {
          environment,
          updateMask,
        };
    
        // Run request
        const [operation] = await cxClient.updateEnvironment(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateEnvironment();
    
    

### updateEnvironment(request, options, callback)
    
    
    updateEnvironment(request: protos.google.cloud.dialogflow.cx.v3beta1.IUpdateEnvironmentRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment, protos.google.protobuf.IStruct>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEnvironmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iupdateenvironmentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ienvironment), [protos.google.protobuf.IStruct](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.istruct)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEnvironment(request, callback)
    
    
    updateEnvironment(request: protos.google.cloud.dialogflow.cx.v3beta1.IUpdateEnvironmentRequest, callback: Callback<LROperation<protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment, protos.google.protobuf.IStruct>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEnvironmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iupdateenvironmentrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.IEnvironment](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ienvironment), [protos.google.protobuf.IStruct](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.istruct)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### versionPath(project, location, agent, flow, version)
    
    
    versionPath(project: string, location: string, agent: string, flow: string, version: string): string;

Return a fully-qualified version resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`flow` |  `string`   
  
`version` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### webhookPath(project, location, agent, webhook)
    
    
    webhookPath(project: string, location: string, agent: string, webhook: string): string;

Return a fully-qualified webhook resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`webhook` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
