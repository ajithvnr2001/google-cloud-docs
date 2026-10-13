---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/v3beta1.flowsclient
title: Class v3beta1.FlowsClient (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:52:14.000761+00:00
---

# Class v3beta1.FlowsClient (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/v3beta1.flowsclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v3beta1.FlowsClient (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.6.0  5.5.0  5.1.0  5.0.1  4.10.0  4.9.0  4.8.0  4.6.0  4.3.1  4.2.0  4.0.0  3.4.2  3.2.1  3.1.2  2.15.0  2.14.0  2.13.0  2.12.1 

Service for managing . v3beta1

## Package

[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of FlowsClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new FlowsClient({fallback: true}, gax); ```  
  
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

### flowsStub
    
    
    flowsStub?: Promise<{
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
  
### checkExportFlowProgress(name)
    
    
    checkExportFlowProgress(name: string): Promise<LROperation<protos.google.cloud.dialogflow.cx.v3beta1.ExportFlowResponse, protos.google.protobuf.Struct>>;

Check the status of the long running operation returned by `exportFlow()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.ExportFlowResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.exportflowresponse), [protos.google.protobuf.Struct](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.struct)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the flow to export.
       *  Format:
       *  `projects/

### checkImportFlowProgress(name)
    
    
    checkImportFlowProgress(name: string): Promise<LROperation<protos.google.cloud.dialogflow.cx.v3beta1.ImportFlowResponse, protos.google.protobuf.Struct>>;

Check the status of the long running operation returned by `importFlow()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.ImportFlowResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.importflowresponse), [protos.google.protobuf.Struct](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.struct)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The agent to import the flow into.
       *  Format: `projects/

### checkTrainFlowProgress(name)
    
    
    checkTrainFlowProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.protobuf.Struct>>;

Check the status of the long running operation returned by `trainFlow()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.empty), [protos.google.protobuf.Struct](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.struct)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The flow to train.
       *  Format:
       *  `projects/

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
  
### createFlow(request, options)
    
    
    createFlow(request?: protos.google.cloud.dialogflow.cx.v3beta1.ICreateFlowRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dialogflow.cx.v3beta1.IFlow,
            protos.google.cloud.dialogflow.cx.v3beta1.ICreateFlowRequest | undefined,
            {} | undefined
        ]>;

Creates a flow in the specified agent.

Note: You should always train a flow prior to sending it queries. See the [training documentation](<https://cloud.google.com/dialogflow/cx/docs/concept/training>).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.icreateflowrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dialogflow.cx.v3beta1.IFlow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iflow), [protos.google.cloud.dialogflow.cx.v3beta1.ICreateFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.icreateflowrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The agent to create a flow for.
       *  Format: `projects/

### createFlow(request, options, callback)
    
    
    createFlow(request: protos.google.cloud.dialogflow.cx.v3beta1.ICreateFlowRequest, options: CallOptions, callback: Callback<protos.google.cloud.dialogflow.cx.v3beta1.IFlow, protos.google.cloud.dialogflow.cx.v3beta1.ICreateFlowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.icreateflowrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.cx.v3beta1.IFlow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iflow), [protos.google.cloud.dialogflow.cx.v3beta1.ICreateFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.icreateflowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFlow(request, callback)
    
    
    createFlow(request: protos.google.cloud.dialogflow.cx.v3beta1.ICreateFlowRequest, callback: Callback<protos.google.cloud.dialogflow.cx.v3beta1.IFlow, protos.google.cloud.dialogflow.cx.v3beta1.ICreateFlowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.icreateflowrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.cx.v3beta1.IFlow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iflow), [protos.google.cloud.dialogflow.cx.v3beta1.ICreateFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.icreateflowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFlow(request, options)
    
    
    deleteFlow(request?: protos.google.cloud.dialogflow.cx.v3beta1.IDeleteFlowRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.cloud.dialogflow.cx.v3beta1.IDeleteFlowRequest | undefined,
            {} | undefined
        ]>;

Deletes a specified flow.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideleteflowrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.iempty), [protos.google.cloud.dialogflow.cx.v3beta1.IDeleteFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideleteflowrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the flow to delete.
       *  Format:
       *  `projects/

### deleteFlow(request, options, callback)
    
    
    deleteFlow(request: protos.google.cloud.dialogflow.cx.v3beta1.IDeleteFlowRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dialogflow.cx.v3beta1.IDeleteFlowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideleteflowrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.iempty), [protos.google.cloud.dialogflow.cx.v3beta1.IDeleteFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideleteflowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFlow(request, callback)
    
    
    deleteFlow(request: protos.google.cloud.dialogflow.cx.v3beta1.IDeleteFlowRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dialogflow.cx.v3beta1.IDeleteFlowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideleteflowrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.iempty), [protos.google.cloud.dialogflow.cx.v3beta1.IDeleteFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ideleteflowrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### exportFlow(request, options)
    
    
    exportFlow(request?: protos.google.cloud.dialogflow.cx.v3beta1.IExportFlowRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.dialogflow.cx.v3beta1.IExportFlowResponse, protos.google.protobuf.IStruct>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Exports the specified flow to a binary file.

This method is a [long-running operation](<https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: [ExportFlowResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.exportflowresponse)



Note that resources (e.g. intents, entities, webhooks) that the flow references will also be exported.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iexportflowrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.IExportFlowResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iexportflowresponse), [protos.google.protobuf.IStruct](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.istruct)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the flow to export.
       *  Format:
       *  `projects/

### exportFlow(request, options, callback)
    
    
    exportFlow(request: protos.google.cloud.dialogflow.cx.v3beta1.IExportFlowRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.dialogflow.cx.v3beta1.IExportFlowResponse, protos.google.protobuf.IStruct>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iexportflowrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.IExportFlowResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iexportflowresponse), [protos.google.protobuf.IStruct](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.istruct)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportFlow(request, callback)
    
    
    exportFlow(request: protos.google.cloud.dialogflow.cx.v3beta1.IExportFlowRequest, callback: Callback<LROperation<protos.google.cloud.dialogflow.cx.v3beta1.IExportFlowResponse, protos.google.protobuf.IStruct>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iexportflowrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.IExportFlowResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iexportflowresponse), [protos.google.protobuf.IStruct](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.istruct)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
  
### getFlow(request, options)
    
    
    getFlow(request?: protos.google.cloud.dialogflow.cx.v3beta1.IGetFlowRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dialogflow.cx.v3beta1.IFlow,
            protos.google.cloud.dialogflow.cx.v3beta1.IGetFlowRequest | undefined,
            {} | undefined
        ]>;

Retrieves the specified flow.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.igetflowrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dialogflow.cx.v3beta1.IFlow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iflow), [protos.google.cloud.dialogflow.cx.v3beta1.IGetFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.igetflowrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the flow to get.
       *  Format:
       *  `projects/

### getFlow(request, options, callback)
    
    
    getFlow(request: protos.google.cloud.dialogflow.cx.v3beta1.IGetFlowRequest, options: CallOptions, callback: Callback<protos.google.cloud.dialogflow.cx.v3beta1.IFlow, protos.google.cloud.dialogflow.cx.v3beta1.IGetFlowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.igetflowrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.cx.v3beta1.IFlow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iflow), [protos.google.cloud.dialogflow.cx.v3beta1.IGetFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.igetflowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFlow(request, callback)
    
    
    getFlow(request: protos.google.cloud.dialogflow.cx.v3beta1.IGetFlowRequest, callback: Callback<protos.google.cloud.dialogflow.cx.v3beta1.IFlow, protos.google.cloud.dialogflow.cx.v3beta1.IGetFlowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.igetflowrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.cx.v3beta1.IFlow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iflow), [protos.google.cloud.dialogflow.cx.v3beta1.IGetFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.igetflowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFlowValidationResult(request, options)
    
    
    getFlowValidationResult(request?: protos.google.cloud.dialogflow.cx.v3beta1.IGetFlowValidationResultRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dialogflow.cx.v3beta1.IFlowValidationResult,
            (protos.google.cloud.dialogflow.cx.v3beta1.IGetFlowValidationResultRequest | undefined),
            {} | undefined
        ]>;

Gets the latest flow validation result. Flow validation is performed when ValidateFlow is called.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFlowValidationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.igetflowvalidationresultrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dialogflow.cx.v3beta1.IFlowValidationResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iflowvalidationresult), ([protos.google.cloud.dialogflow.cx.v3beta1.IGetFlowValidationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.igetflowvalidationresultrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [FlowValidationResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.flowvalidationresult). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The flow name.
       *  Format:
       *  `projects/

### getFlowValidationResult(request, options, callback)
    
    
    getFlowValidationResult(request: protos.google.cloud.dialogflow.cx.v3beta1.IGetFlowValidationResultRequest, options: CallOptions, callback: Callback<protos.google.cloud.dialogflow.cx.v3beta1.IFlowValidationResult, protos.google.cloud.dialogflow.cx.v3beta1.IGetFlowValidationResultRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFlowValidationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.igetflowvalidationresultrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.cx.v3beta1.IFlowValidationResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iflowvalidationresult), [protos.google.cloud.dialogflow.cx.v3beta1.IGetFlowValidationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.igetflowvalidationresultrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFlowValidationResult(request, callback)
    
    
    getFlowValidationResult(request: protos.google.cloud.dialogflow.cx.v3beta1.IGetFlowValidationResultRequest, callback: Callback<protos.google.cloud.dialogflow.cx.v3beta1.IFlowValidationResult, protos.google.cloud.dialogflow.cx.v3beta1.IGetFlowValidationResultRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFlowValidationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.igetflowvalidationresultrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.cx.v3beta1.IFlowValidationResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iflowvalidationresult), [protos.google.cloud.dialogflow.cx.v3beta1.IGetFlowValidationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.igetflowvalidationresultrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### importFlow(request, options)
    
    
    importFlow(request?: protos.google.cloud.dialogflow.cx.v3beta1.IImportFlowRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.dialogflow.cx.v3beta1.IImportFlowResponse, protos.google.protobuf.IStruct>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Imports the specified flow to the specified agent from a binary file.

This method is a [long-running operation](<https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: [ImportFlowResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.importflowresponse)



Note: You should always train a flow prior to sending it queries. See the [training documentation](<https://cloud.google.com/dialogflow/cx/docs/concept/training>).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iimportflowrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.IImportFlowResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iimportflowresponse), [protos.google.protobuf.IStruct](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.istruct)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The agent to import the flow into.
       *  Format: `projects/

### importFlow(request, options, callback)
    
    
    importFlow(request: protos.google.cloud.dialogflow.cx.v3beta1.IImportFlowRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.dialogflow.cx.v3beta1.IImportFlowResponse, protos.google.protobuf.IStruct>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iimportflowrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.IImportFlowResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iimportflowresponse), [protos.google.protobuf.IStruct](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.istruct)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importFlow(request, callback)
    
    
    importFlow(request: protos.google.cloud.dialogflow.cx.v3beta1.IImportFlowRequest, callback: Callback<LROperation<protos.google.cloud.dialogflow.cx.v3beta1.IImportFlowResponse, protos.google.protobuf.IStruct>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iimportflowrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.dialogflow.cx.v3beta1.IImportFlowResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iimportflowresponse), [protos.google.protobuf.IStruct](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.istruct)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
  
### listFlows(request, options)
    
    
    listFlows(request?: protos.google.cloud.dialogflow.cx.v3beta1.IListFlowsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dialogflow.cx.v3beta1.IFlow[],
            protos.google.cloud.dialogflow.cx.v3beta1.IListFlowsRequest | null,
            protos.google.cloud.dialogflow.cx.v3beta1.IListFlowsResponse
        ]>;

Returns the list of all flows in the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFlowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistflowsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dialogflow.cx.v3beta1.IFlow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iflow)[], [protos.google.cloud.dialogflow.cx.v3beta1.IListFlowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistflowsrequest) | null, [protos.google.cloud.dialogflow.cx.v3beta1.IListFlowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistflowsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listFlowsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listFlows(request, options, callback)
    
    
    listFlows(request: protos.google.cloud.dialogflow.cx.v3beta1.IListFlowsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dialogflow.cx.v3beta1.IListFlowsRequest, protos.google.cloud.dialogflow.cx.v3beta1.IListFlowsResponse | null | undefined, protos.google.cloud.dialogflow.cx.v3beta1.IFlow>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFlowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistflowsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dialogflow.cx.v3beta1.IListFlowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistflowsrequest), [protos.google.cloud.dialogflow.cx.v3beta1.IListFlowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistflowsresponse) | null | undefined, [protos.google.cloud.dialogflow.cx.v3beta1.IFlow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iflow)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFlows(request, callback)
    
    
    listFlows(request: protos.google.cloud.dialogflow.cx.v3beta1.IListFlowsRequest, callback: PaginationCallback<protos.google.cloud.dialogflow.cx.v3beta1.IListFlowsRequest, protos.google.cloud.dialogflow.cx.v3beta1.IListFlowsResponse | null | undefined, protos.google.cloud.dialogflow.cx.v3beta1.IFlow>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFlowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistflowsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dialogflow.cx.v3beta1.IListFlowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistflowsrequest), [protos.google.cloud.dialogflow.cx.v3beta1.IListFlowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistflowsresponse) | null | undefined, [protos.google.cloud.dialogflow.cx.v3beta1.IFlow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iflow)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFlowsAsync(request, options)
    
    
    listFlowsAsync(request?: protos.google.cloud.dialogflow.cx.v3beta1.IListFlowsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dialogflow.cx.v3beta1.IFlow>;

Equivalent to `listFlows`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFlowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistflowsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dialogflow.cx.v3beta1.IFlow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iflow)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The agent containing the flows.
       *  Format: `projects/

### listFlowsStream(request, options)
    
    
    listFlowsStream(request?: protos.google.cloud.dialogflow.cx.v3beta1.IListFlowsRequest, options?: CallOptions): Transform;

Equivalent to `listFlows`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFlowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ilistflowsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listFlowsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### trainFlow(request, options)
    
    
    trainFlow(request?: protos.google.cloud.dialogflow.cx.v3beta1.ITrainFlowRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.protobuf.IStruct>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Trains the specified flow. Note that only the flow in 'draft' environment is trained.

This method is a [long-running operation](<https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



Note: You should always train a flow prior to sending it queries. See the [training documentation](<https://cloud.google.com/dialogflow/cx/docs/concept/training>).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITrainFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.itrainflowrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.iempty), [protos.google.protobuf.IStruct](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.istruct)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The flow to train.
       *  Format:
       *  `projects/

### trainFlow(request, options, callback)
    
    
    trainFlow(request: protos.google.cloud.dialogflow.cx.v3beta1.ITrainFlowRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.protobuf.IStruct>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITrainFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.itrainflowrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.iempty), [protos.google.protobuf.IStruct](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.istruct)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### trainFlow(request, callback)
    
    
    trainFlow(request: protos.google.cloud.dialogflow.cx.v3beta1.ITrainFlowRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.protobuf.IStruct>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITrainFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.itrainflowrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.iempty), [protos.google.protobuf.IStruct](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.istruct)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFlow(request, options)
    
    
    updateFlow(request?: protos.google.cloud.dialogflow.cx.v3beta1.IUpdateFlowRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dialogflow.cx.v3beta1.IFlow,
            protos.google.cloud.dialogflow.cx.v3beta1.IUpdateFlowRequest | undefined,
            {} | undefined
        ]>;

Updates the specified flow.

Note: You should always train a flow prior to sending it queries. See the [training documentation](<https://cloud.google.com/dialogflow/cx/docs/concept/training>).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iupdateflowrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dialogflow.cx.v3beta1.IFlow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iflow), [protos.google.cloud.dialogflow.cx.v3beta1.IUpdateFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iupdateflowrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The flow to update.
       */
      // const flow = {}
      /**
       *  The mask to control which fields get updated. If the mask is not present,
       *  all fields will be updated.
       */
      // const updateMask = {}
      /**
       *  The language of the following fields in `flow`:
       *  *  `Flow.event_handlers.trigger_fulfillment.messages`
       *  *  `Flow.event_handlers.trigger_fulfillment.conditional_cases`
       *  *  `Flow.transition_routes.trigger_fulfillment.messages`
       *  *  `Flow.transition_routes.trigger_fulfillment.conditional_cases`
       *  If not specified, the agent's default language is used.
       *  Many
       *  languages (https://cloud.google.com/dialogflow/cx/docs/reference/language)
       *  are supported.
       *  Note: languages must be enabled in the agent before they can be used.
       */
      // const languageCode = 'abc123'
    
      // Imports the Cx library
      const {FlowsClient} = require('[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)').v3beta1;
    
      // Instantiates a client
      const cxClient = new [FlowsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)();
    
      async function callUpdateFlow() {
        // Construct request
        const request = {
          flow,
        };
    
        // Run request
        const response = await cxClient.updateFlow(request);
        console.log(response);
      }
    
      callUpdateFlow();
    
    

### updateFlow(request, options, callback)
    
    
    updateFlow(request: protos.google.cloud.dialogflow.cx.v3beta1.IUpdateFlowRequest, options: CallOptions, callback: Callback<protos.google.cloud.dialogflow.cx.v3beta1.IFlow, protos.google.cloud.dialogflow.cx.v3beta1.IUpdateFlowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iupdateflowrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.cx.v3beta1.IFlow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iflow), [protos.google.cloud.dialogflow.cx.v3beta1.IUpdateFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iupdateflowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFlow(request, callback)
    
    
    updateFlow(request: protos.google.cloud.dialogflow.cx.v3beta1.IUpdateFlowRequest, callback: Callback<protos.google.cloud.dialogflow.cx.v3beta1.IFlow, protos.google.cloud.dialogflow.cx.v3beta1.IUpdateFlowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iupdateflowrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.cx.v3beta1.IFlow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iflow), [protos.google.cloud.dialogflow.cx.v3beta1.IUpdateFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iupdateflowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### validateFlow(request, options)
    
    
    validateFlow(request?: protos.google.cloud.dialogflow.cx.v3beta1.IValidateFlowRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dialogflow.cx.v3beta1.IFlowValidationResult,
            (protos.google.cloud.dialogflow.cx.v3beta1.IValidateFlowRequest | undefined),
            {} | undefined
        ]>;

Validates the specified flow and creates or updates validation results. Please call this API after the training is completed to get the complete validation results.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IValidateFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ivalidateflowrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dialogflow.cx.v3beta1.IFlowValidationResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iflowvalidationresult), ([protos.google.cloud.dialogflow.cx.v3beta1.IValidateFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ivalidateflowrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [FlowValidationResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.flowvalidationresult). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The flow to validate.
       *  Format:
       *  `projects/

### validateFlow(request, options, callback)
    
    
    validateFlow(request: protos.google.cloud.dialogflow.cx.v3beta1.IValidateFlowRequest, options: CallOptions, callback: Callback<protos.google.cloud.dialogflow.cx.v3beta1.IFlowValidationResult, protos.google.cloud.dialogflow.cx.v3beta1.IValidateFlowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IValidateFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ivalidateflowrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.cx.v3beta1.IFlowValidationResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iflowvalidationresult), [protos.google.cloud.dialogflow.cx.v3beta1.IValidateFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ivalidateflowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### validateFlow(request, callback)
    
    
    validateFlow(request: protos.google.cloud.dialogflow.cx.v3beta1.IValidateFlowRequest, callback: Callback<protos.google.cloud.dialogflow.cx.v3beta1.IFlowValidationResult, protos.google.cloud.dialogflow.cx.v3beta1.IValidateFlowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IValidateFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ivalidateflowrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.cx.v3beta1.IFlowValidationResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.iflowvalidationresult), [protos.google.cloud.dialogflow.cx.v3beta1.IValidateFlowRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ivalidateflowrequest) | null | undefined, {} | null | undefined>`   
  
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
