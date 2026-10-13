---
url: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/v1beta.dataagentserviceclient
title: Class v1beta.DataAgentServiceClient (0.13.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:37:27.710899+00:00
---

# Class v1beta.DataAgentServiceClient (0.13.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/v1beta.dataagentserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.DataAgentServiceClient (0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.13.0  0.7.0  0.6.0  0.4.0  0.2.0 

Service describing handlers for resources. v1beta

## Package

[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of DataAgentServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new DataAgentServiceClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### dataAgentServiceStub
    
    
    dataAgentServiceStub?: Promise<{
            [name: string]: Function;
        }>;

### descriptors
    
    
    descriptors: Descriptors;

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
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### checkCreateDataAgentProgress(name)
    
    
    checkCreateDataAgentProgress(name: string): Promise<LROperation<protos.google.cloud.geminidataanalytics.v1beta.DataAgent, protos.google.cloud.geminidataanalytics.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `createDataAgent()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.geminidataanalytics.v1beta.DataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.dataagent), [protos.google.cloud.geminidataanalytics.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Value for parent.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Id of the requesting object. Must be unique within the parent.
       *  The allowed format is: `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`.
       *  If not provided, the server will auto-generate a value for the id.
       */
      // const dataAgentId = 'abc123'
      /**
       *  Required. The resource being created.
       */
      // const dataAgent = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and the
       *  request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Geminidataanalytics library
      const {DataAgentServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataAgentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callCreateDataAgent() {
        // Construct request
        const request = {
          parent,
          dataAgent,
        };
    
        // Run request
        const [operation] = await geminidataanalyticsClient.createDataAgent(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateDataAgent();
    
    

### checkDeleteDataAgentProgress(name)
    
    
    checkDeleteDataAgentProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.geminidataanalytics.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `deleteDataAgent()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.protobuf.empty), [protos.google.cloud.geminidataanalytics.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the resource.
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and the
       *  request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Geminidataanalytics library
      const {DataAgentServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataAgentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callDeleteDataAgent() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await geminidataanalyticsClient.deleteDataAgent(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteDataAgent();
    
    

### checkSetAgentOpsObservabilityProgress(name)
    
    
    checkSetAgentOpsObservabilityProgress(name: string): Promise<LROperation<protos.google.cloud.geminidataanalytics.v1beta.SetAgentOpsObservabilityResponse, protos.google.cloud.geminidataanalytics.v1beta.SetAgentOpsObservabilityMetadata>>;

Check the status of the long running operation returned by `setAgentOpsObservability()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.geminidataanalytics.v1beta.SetAgentOpsObservabilityResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.setagentopsobservabilityresponse), [protos.google.cloud.geminidataanalytics.v1beta.SetAgentOpsObservabilityMetadata](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.setagentopsobservabilitymetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent value for SetAgentOpsObservabilityRequest.
       *  Format: projects/{project}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Optional. Whether to enable or disable AgentOps observability.
       *  When update_mask is provided, this field is ignored unless specified in the
       *  mask.
       */
      // const telemetryEnabled = true
      /**
       *  Required. The data source type for which to set observability settings.
       *  Examples: "bigquery", "looker"
       */
      // const dataSourceType = 'abc123'
      /**
       *  Optional. Whether BigQuery Agent Analytics is enabled.
       *  Note: An explicit `update_mask` containing "bqaa_enabled" is required to
       *  modify this field. If `update_mask` is omitted, this field is ignored and
       *  an existing enabled setting cannot be disabled.
       *  This is a project-level setting and does not by itself enable trace
       *  logging for any individual agent. Per-agent trace logging is controlled
       *  by `DataAgent.bigquery_agent_analytics_enabled` together with
       *  `DataAgent.bigquery_agent_analytics_table`; an agent does not inherit
       *  this setting.
       */
      // const bqaaEnabled = true
      /**
       *  Optional. Field mask is used to specify the fields to be overwritten by the
       *  update. The fields specified in the update_mask are relative to the
       *  resource. A field will be overwritten if it is in the mask.
       *  If the user does not provide a mask, only `telemetry_enabled` will be
       *  updated (for backward compatibility with legacy callers). Note that
       *  disabling BigQuery Agent Analytics (`bqaa_enabled = false`) requires
       *  providing an explicit `update_mask` containing "bqaa_enabled".
       *  Per AIP-161:
       *  - The special wildcard value '*' is supported to update all fields.
       *  - Field paths should use snake_case, though camelCase equivalents
       *    (`telemetryEnabled`, `bqaaEnabled`) are accepted for REST/JSON
       *    transcoding compatibility.
       */
      // const updateMask = {}
    
      // Imports the Geminidataanalytics library
      const {DataAgentServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataAgentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callSetAgentOpsObservability() {
        // Construct request
        const request = {
          parent,
          dataSourceType,
        };
    
        // Run request
        const [operation] = await geminidataanalyticsClient.setAgentOpsObservability(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callSetAgentOpsObservability();
    
    

### checkUpdateDataAgentProgress(name)
    
    
    checkUpdateDataAgentProgress(name: string): Promise<LROperation<protos.google.cloud.geminidataanalytics.v1beta.DataAgent, protos.google.cloud.geminidataanalytics.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `updateDataAgent()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.geminidataanalytics.v1beta.DataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.dataagent), [protos.google.cloud.geminidataanalytics.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Field mask is used to specify the fields to be overwritten in the
       *  DataAgent resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then all fields with non-default values
       *  present in the request will be overwritten. If a wildcard mask is provided,
       *  all fields will be overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The resource being updated.
       */
      // const dataAgent = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and the
       *  request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Geminidataanalytics library
      const {DataAgentServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataAgentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callUpdateDataAgent() {
        // Construct request
        const request = {
          dataAgent,
        };
    
        // Run request
        const [operation] = await geminidataanalyticsClient.updateDataAgent(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateDataAgent();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### conversationPath(project, location, conversation)
    
    
    conversationPath(project: string, location: string, conversation: string): string;

Return a fully-qualified conversation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`conversation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### createDataAgent(request, options)
    
    
    createDataAgent(request?: protos.google.cloud.geminidataanalytics.v1beta.ICreateDataAgentRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.geminidataanalytics.v1beta.IDataAgent, protos.google.cloud.geminidataanalytics.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new DataAgent in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.icreatedataagentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent), [protos.google.cloud.geminidataanalytics.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Value for parent.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Id of the requesting object. Must be unique within the parent.
       *  The allowed format is: `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`.
       *  If not provided, the server will auto-generate a value for the id.
       */
      // const dataAgentId = 'abc123'
      /**
       *  Required. The resource being created.
       */
      // const dataAgent = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and the
       *  request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Geminidataanalytics library
      const {DataAgentServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataAgentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callCreateDataAgent() {
        // Construct request
        const request = {
          parent,
          dataAgent,
        };
    
        // Run request
        const [operation] = await geminidataanalyticsClient.createDataAgent(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateDataAgent();
    
    

### createDataAgent(request, options, callback)
    
    
    createDataAgent(request: protos.google.cloud.geminidataanalytics.v1beta.ICreateDataAgentRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.geminidataanalytics.v1beta.IDataAgent, protos.google.cloud.geminidataanalytics.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.icreatedataagentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent), [protos.google.cloud.geminidataanalytics.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataAgent(request, callback)
    
    
    createDataAgent(request: protos.google.cloud.geminidataanalytics.v1beta.ICreateDataAgentRequest, callback: Callback<LROperation<protos.google.cloud.geminidataanalytics.v1beta.IDataAgent, protos.google.cloud.geminidataanalytics.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.icreatedataagentrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent), [protos.google.cloud.geminidataanalytics.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataAgentSync(request, options)
    
    
    createDataAgentSync(request?: protos.google.cloud.geminidataanalytics.v1beta.ICreateDataAgentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.geminidataanalytics.v1beta.IDataAgent,
            (protos.google.cloud.geminidataanalytics.v1beta.ICreateDataAgentRequest | undefined),
            {} | undefined
        ]>;

Creates a new DataAgent in a given project and location synchronously.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.icreatedataagentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent), ([protos.google.cloud.geminidataanalytics.v1beta.ICreateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.icreatedataagentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [DataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.dataagent). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Value for parent.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Id of the requesting object. Must be unique within the parent.
       *  The allowed format is: `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`.
       *  If not provided, the server will auto-generate a value for the id.
       */
      // const dataAgentId = 'abc123'
      /**
       *  Required. The resource being created.
       */
      // const dataAgent = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and the
       *  request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Geminidataanalytics library
      const {DataAgentServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataAgentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callCreateDataAgentSync() {
        // Construct request
        const request = {
          parent,
          dataAgent,
        };
    
        // Run request
        const response = await geminidataanalyticsClient.createDataAgentSync(request);
        console.log(response);
      }
    
      callCreateDataAgentSync();
    
    

### createDataAgentSync(request, options, callback)
    
    
    createDataAgentSync(request: protos.google.cloud.geminidataanalytics.v1beta.ICreateDataAgentRequest, options: CallOptions, callback: Callback<protos.google.cloud.geminidataanalytics.v1beta.IDataAgent, protos.google.cloud.geminidataanalytics.v1beta.ICreateDataAgentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.icreatedataagentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent), [protos.google.cloud.geminidataanalytics.v1beta.ICreateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.icreatedataagentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataAgentSync(request, callback)
    
    
    createDataAgentSync(request: protos.google.cloud.geminidataanalytics.v1beta.ICreateDataAgentRequest, callback: Callback<protos.google.cloud.geminidataanalytics.v1beta.IDataAgent, protos.google.cloud.geminidataanalytics.v1beta.ICreateDataAgentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.icreatedataagentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent), [protos.google.cloud.geminidataanalytics.v1beta.ICreateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.icreatedataagentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### dataAgentPath(project, location, dataAgent)
    
    
    dataAgentPath(project: string, location: string, dataAgent: string): string;

Return a fully-qualified dataAgent resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataAgent` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### deleteDataAgent(request, options)
    
    
    deleteDataAgent(request?: protos.google.cloud.geminidataanalytics.v1beta.IDeleteDataAgentRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.geminidataanalytics.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a single DataAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ideletedataagentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.protobuf.iempty), [protos.google.cloud.geminidataanalytics.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the resource.
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and the
       *  request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Geminidataanalytics library
      const {DataAgentServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataAgentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callDeleteDataAgent() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await geminidataanalyticsClient.deleteDataAgent(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteDataAgent();
    
    

### deleteDataAgent(request, options, callback)
    
    
    deleteDataAgent(request: protos.google.cloud.geminidataanalytics.v1beta.IDeleteDataAgentRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.geminidataanalytics.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ideletedataagentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.protobuf.iempty), [protos.google.cloud.geminidataanalytics.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataAgent(request, callback)
    
    
    deleteDataAgent(request: protos.google.cloud.geminidataanalytics.v1beta.IDeleteDataAgentRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.geminidataanalytics.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ideletedataagentrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.protobuf.iempty), [protos.google.cloud.geminidataanalytics.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataAgentSync(request, options)
    
    
    deleteDataAgentSync(request?: protos.google.cloud.geminidataanalytics.v1beta.IDeleteDataAgentRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.geminidataanalytics.v1beta.IDeleteDataAgentRequest | undefined),
            {} | undefined
        ]>;

Deletes a single DataAgent synchronously.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ideletedataagentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.protobuf.iempty), ([protos.google.cloud.geminidataanalytics.v1beta.IDeleteDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ideletedataagentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the resource.
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and the
       *  request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Geminidataanalytics library
      const {DataAgentServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataAgentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callDeleteDataAgentSync() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await geminidataanalyticsClient.deleteDataAgentSync(request);
        console.log(response);
      }
    
      callDeleteDataAgentSync();
    
    

### deleteDataAgentSync(request, options, callback)
    
    
    deleteDataAgentSync(request: protos.google.cloud.geminidataanalytics.v1beta.IDeleteDataAgentRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.geminidataanalytics.v1beta.IDeleteDataAgentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ideletedataagentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.protobuf.iempty), [protos.google.cloud.geminidataanalytics.v1beta.IDeleteDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ideletedataagentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataAgentSync(request, callback)
    
    
    deleteDataAgentSync(request: protos.google.cloud.geminidataanalytics.v1beta.IDeleteDataAgentRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.geminidataanalytics.v1beta.IDeleteDataAgentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ideletedataagentrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.protobuf.iempty), [protos.google.cloud.geminidataanalytics.v1beta.IDeleteDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ideletedataagentrequest) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### getDataAgent(request, options)
    
    
    getDataAgent(request?: protos.google.cloud.geminidataanalytics.v1beta.IGetDataAgentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.geminidataanalytics.v1beta.IDataAgent,
            (protos.google.cloud.geminidataanalytics.v1beta.IGetDataAgentRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single DataAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.igetdataagentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent), ([protos.google.cloud.geminidataanalytics.v1beta.IGetDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.igetdataagentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [DataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.dataagent). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the resource.
       */
      // const name = 'abc123'
    
      // Imports the Geminidataanalytics library
      const {DataAgentServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataAgentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callGetDataAgent() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await geminidataanalyticsClient.getDataAgent(request);
        console.log(response);
      }
    
      callGetDataAgent();
    
    

### getDataAgent(request, options, callback)
    
    
    getDataAgent(request: protos.google.cloud.geminidataanalytics.v1beta.IGetDataAgentRequest, options: CallOptions, callback: Callback<protos.google.cloud.geminidataanalytics.v1beta.IDataAgent, protos.google.cloud.geminidataanalytics.v1beta.IGetDataAgentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.igetdataagentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent), [protos.google.cloud.geminidataanalytics.v1beta.IGetDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.igetdataagentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataAgent(request, callback)
    
    
    getDataAgent(request: protos.google.cloud.geminidataanalytics.v1beta.IGetDataAgentRequest, callback: Callback<protos.google.cloud.geminidataanalytics.v1beta.IDataAgent, protos.google.cloud.geminidataanalytics.v1beta.IGetDataAgentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.igetdataagentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent), [protos.google.cloud.geminidataanalytics.v1beta.IGetDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.igetdataagentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request, options)
    
    
    getIamPolicy(request?: protos.google.iam.v1.IGetIamPolicyRequest, options?: CallOptions): Promise<[
            protos.google.iam.v1.IPolicy,
            protos.google.iam.v1.IGetIamPolicyRequest | undefined,
            {} | undefined
        ]>;

Gets the IAM policy for DataAgent

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.igetiampolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.igetiampolicyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Policy](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.policy). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  REQUIRED: The resource for which the policy is being requested.
       *  See the operation documentation for the appropriate value for this field.
       */
      // const resource = 'abc123'
      /**
       *  OPTIONAL: A `GetPolicyOptions` object for specifying options to
       *  `GetIamPolicy`.
       */
      // const options = {}
    
      // Imports the Geminidataanalytics library
      const {DataAgentServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataAgentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callGetIamPolicy() {
        // Construct request
        const request = {
          resource,
        };
    
        // Run request
        const response = await geminidataanalyticsClient.getIamPolicy(request);
        console.log(response);
      }
    
      callGetIamPolicy();
    
    

### getIamPolicy(request, options, callback)
    
    
    getIamPolicy(request: protos.google.iam.v1.IGetIamPolicyRequest, options: CallOptions, callback: Callback<protos.google.iam.v1.IPolicy, protos.google.iam.v1.IGetIamPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.igetiampolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.igetiampolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request, callback)
    
    
    getIamPolicy(request: protos.google.iam.v1.IGetIamPolicyRequest, callback: Callback<protos.google.iam.v1.IPolicy, protos.google.iam.v1.IGetIamPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.igetiampolicyrequest)`   
  
`callback` |  `Callback<[protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.igetiampolicyrequest) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.operation)]>` |   
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
  
### listAccessibleDataAgents(request, options)
    
    
    listAccessibleDataAgents(request?: protos.google.cloud.geminidataanalytics.v1beta.IListAccessibleDataAgentsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.geminidataanalytics.v1beta.IDataAgent[],
            protos.google.cloud.geminidataanalytics.v1beta.IListAccessibleDataAgentsRequest | null,
            protos.google.cloud.geminidataanalytics.v1beta.IListAccessibleDataAgentsResponse
        ]>;

Lists DataAgents that are accessible to the caller in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccessibleDataAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistaccessibledataagentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent)[], [protos.google.cloud.geminidataanalytics.v1beta.IListAccessibleDataAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistaccessibledataagentsrequest) | null, [protos.google.cloud.geminidataanalytics.v1beta.IListAccessibleDataAgentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistaccessibledataagentsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [DataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.dataagent). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listAccessibleDataAgentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listAccessibleDataAgents(request, options, callback)
    
    
    listAccessibleDataAgents(request: protos.google.cloud.geminidataanalytics.v1beta.IListAccessibleDataAgentsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.geminidataanalytics.v1beta.IListAccessibleDataAgentsRequest, protos.google.cloud.geminidataanalytics.v1beta.IListAccessibleDataAgentsResponse | null | undefined, protos.google.cloud.geminidataanalytics.v1beta.IDataAgent>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccessibleDataAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistaccessibledataagentsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.geminidataanalytics.v1beta.IListAccessibleDataAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistaccessibledataagentsrequest), [protos.google.cloud.geminidataanalytics.v1beta.IListAccessibleDataAgentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistaccessibledataagentsresponse) | null | undefined, [protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAccessibleDataAgents(request, callback)
    
    
    listAccessibleDataAgents(request: protos.google.cloud.geminidataanalytics.v1beta.IListAccessibleDataAgentsRequest, callback: PaginationCallback<protos.google.cloud.geminidataanalytics.v1beta.IListAccessibleDataAgentsRequest, protos.google.cloud.geminidataanalytics.v1beta.IListAccessibleDataAgentsResponse | null | undefined, protos.google.cloud.geminidataanalytics.v1beta.IDataAgent>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccessibleDataAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistaccessibledataagentsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.geminidataanalytics.v1beta.IListAccessibleDataAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistaccessibledataagentsrequest), [protos.google.cloud.geminidataanalytics.v1beta.IListAccessibleDataAgentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistaccessibledataagentsresponse) | null | undefined, [protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAccessibleDataAgentsAsync(request, options)
    
    
    listAccessibleDataAgentsAsync(request?: protos.google.cloud.geminidataanalytics.v1beta.IListAccessibleDataAgentsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.geminidataanalytics.v1beta.IDataAgent>;

Equivalent to `listAccessibleDataAgents`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccessibleDataAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistaccessibledataagentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [DataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.dataagent). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent value for ListAccessibleDataAgentsRequest.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Server may return fewer items than requested.
       *  If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListAccessibleDataAgents`
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  `ListAccessibleDataAgents` must match the call that provided the page
       *  token. The service may return fewer than this value.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filtering results. See AIP-160 (https://google.aip.dev/160) for
       *  syntax.
       */
      // const filter = 'abc123'
      /**
       *  Optional. User specification for how to order the results.
       */
      // const orderBy = 'abc123'
      /**
       *  Optional. If true, the list results will include soft-deleted DataAgents.
       *  Defaults to false.
       */
      // const showDeleted = true
      /**
       *  Optional. Filter for the creator of the agent.
       */
      // const creatorFilter = {}
    
      // Imports the Geminidataanalytics library
      const {DataAgentServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataAgentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callListAccessibleDataAgents() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = geminidataanalyticsClient.listAccessibleDataAgentsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListAccessibleDataAgents();
    
    

### listAccessibleDataAgentsStream(request, options)
    
    
    listAccessibleDataAgentsStream(request?: protos.google.cloud.geminidataanalytics.v1beta.IListAccessibleDataAgentsRequest, options?: CallOptions): Transform;

Equivalent to `listAccessibleDataAgents`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccessibleDataAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistaccessibledataagentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [DataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.dataagent) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listAccessibleDataAgentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDataAgents(request, options)
    
    
    listDataAgents(request?: protos.google.cloud.geminidataanalytics.v1beta.IListDataAgentsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.geminidataanalytics.v1beta.IDataAgent[],
            protos.google.cloud.geminidataanalytics.v1beta.IListDataAgentsRequest | null,
            protos.google.cloud.geminidataanalytics.v1beta.IListDataAgentsResponse
        ]>;

Lists DataAgents in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistdataagentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent)[], [protos.google.cloud.geminidataanalytics.v1beta.IListDataAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistdataagentsrequest) | null, [protos.google.cloud.geminidataanalytics.v1beta.IListDataAgentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistdataagentsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [DataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.dataagent). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listDataAgentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDataAgents(request, options, callback)
    
    
    listDataAgents(request: protos.google.cloud.geminidataanalytics.v1beta.IListDataAgentsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.geminidataanalytics.v1beta.IListDataAgentsRequest, protos.google.cloud.geminidataanalytics.v1beta.IListDataAgentsResponse | null | undefined, protos.google.cloud.geminidataanalytics.v1beta.IDataAgent>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistdataagentsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.geminidataanalytics.v1beta.IListDataAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistdataagentsrequest), [protos.google.cloud.geminidataanalytics.v1beta.IListDataAgentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistdataagentsresponse) | null | undefined, [protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataAgents(request, callback)
    
    
    listDataAgents(request: protos.google.cloud.geminidataanalytics.v1beta.IListDataAgentsRequest, callback: PaginationCallback<protos.google.cloud.geminidataanalytics.v1beta.IListDataAgentsRequest, protos.google.cloud.geminidataanalytics.v1beta.IListDataAgentsResponse | null | undefined, protos.google.cloud.geminidataanalytics.v1beta.IDataAgent>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistdataagentsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.geminidataanalytics.v1beta.IListDataAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistdataagentsrequest), [protos.google.cloud.geminidataanalytics.v1beta.IListDataAgentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistdataagentsresponse) | null | undefined, [protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataAgentsAsync(request, options)
    
    
    listDataAgentsAsync(request?: protos.google.cloud.geminidataanalytics.v1beta.IListDataAgentsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.geminidataanalytics.v1beta.IDataAgent>;

Equivalent to `listDataAgents`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistdataagentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [DataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.dataagent). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent value for ListDataAgentsRequest.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Server may return fewer items than requested.
       *  If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListDataAgents` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListDataAgents` must
       *  match the call that provided the page token. The service may return fewer
       *  than this value.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filtering results. See AIP-160 (https://google.aip.dev/160) for
       *  syntax.
       */
      // const filter = 'abc123'
      /**
       *  Optional. User specification for how to order the results.
       */
      // const orderBy = 'abc123'
      /**
       *  Optional. If true, the list results will include soft-deleted DataAgents.
       *  Defaults to false.
       */
      // const showDeleted = true
      /**
       *  Optional. Filter for the creator of the agent.
       */
      // const creatorFilter = {}
    
      // Imports the Geminidataanalytics library
      const {DataAgentServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataAgentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callListDataAgents() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = geminidataanalyticsClient.listDataAgentsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListDataAgents();
    
    

### listDataAgentsStream(request, options)
    
    
    listDataAgentsStream(request?: protos.google.cloud.geminidataanalytics.v1beta.IListDataAgentsRequest, options?: CallOptions): Transform;

Equivalent to `listDataAgents`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistdataagentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [DataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.dataagent) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listDataAgentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
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
  
### matchDataAgentFromDataAgentName(dataAgentName)
    
    
    matchDataAgentFromDataAgentName(dataAgentName: string): string | number;

Parse the data_agent from DataAgent resource.

**Parameter**  
---  
**Name** | **Description**  
`dataAgentName` |  `string`   
A fully-qualified path representing DataAgent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_agent.  
  
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
  
### matchLocationFromDataAgentName(dataAgentName)
    
    
    matchLocationFromDataAgentName(dataAgentName: string): string | number;

Parse the location from DataAgent resource.

**Parameter**  
---  
**Name** | **Description**  
`dataAgentName` |  `string`   
A fully-qualified path representing DataAgent resource.  
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
  
### matchProjectFromDataAgentName(dataAgentName)
    
    
    matchProjectFromDataAgentName(dataAgentName: string): string | number;

Parse the project from DataAgent resource.

**Parameter**  
---  
**Name** | **Description**  
`dataAgentName` |  `string`   
A fully-qualified path representing DataAgent resource.  
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
  
### retrieveAgentOpsObservability(request, options)
    
    
    retrieveAgentOpsObservability(request?: protos.google.cloud.geminidataanalytics.v1beta.IRetrieveAgentOpsObservabilityRequest, options?: CallOptions): Promise<[
            protos.google.cloud.geminidataanalytics.v1beta.IRetrieveAgentOpsObservabilityResponse,
            (protos.google.cloud.geminidataanalytics.v1beta.IRetrieveAgentOpsObservabilityRequest | undefined),
            {} | undefined
        ]>;

Gets AgentOps observability settings and status of required services.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRetrieveAgentOpsObservabilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iretrieveagentopsobservabilityrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.geminidataanalytics.v1beta.IRetrieveAgentOpsObservabilityResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iretrieveagentopsobservabilityresponse), ([protos.google.cloud.geminidataanalytics.v1beta.IRetrieveAgentOpsObservabilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iretrieveagentopsobservabilityrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [RetrieveAgentOpsObservabilityResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.retrieveagentopsobservabilityresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent value for RetrieveAgentOpsObservabilityRequest.
       *  Format: projects/{project}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Required. The data source type for which to retrieve observability
       *  settings. Examples: "bigquery", "looker"
       */
      // const dataSourceType = 'abc123'
    
      // Imports the Geminidataanalytics library
      const {DataAgentServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataAgentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callRetrieveAgentOpsObservability() {
        // Construct request
        const request = {
          parent,
          dataSourceType,
        };
    
        // Run request
        const response = await geminidataanalyticsClient.retrieveAgentOpsObservability(request);
        console.log(response);
      }
    
      callRetrieveAgentOpsObservability();
    
    

### retrieveAgentOpsObservability(request, options, callback)
    
    
    retrieveAgentOpsObservability(request: protos.google.cloud.geminidataanalytics.v1beta.IRetrieveAgentOpsObservabilityRequest, options: CallOptions, callback: Callback<protos.google.cloud.geminidataanalytics.v1beta.IRetrieveAgentOpsObservabilityResponse, protos.google.cloud.geminidataanalytics.v1beta.IRetrieveAgentOpsObservabilityRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRetrieveAgentOpsObservabilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iretrieveagentopsobservabilityrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.geminidataanalytics.v1beta.IRetrieveAgentOpsObservabilityResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iretrieveagentopsobservabilityresponse), [protos.google.cloud.geminidataanalytics.v1beta.IRetrieveAgentOpsObservabilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iretrieveagentopsobservabilityrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### retrieveAgentOpsObservability(request, callback)
    
    
    retrieveAgentOpsObservability(request: protos.google.cloud.geminidataanalytics.v1beta.IRetrieveAgentOpsObservabilityRequest, callback: Callback<protos.google.cloud.geminidataanalytics.v1beta.IRetrieveAgentOpsObservabilityResponse, protos.google.cloud.geminidataanalytics.v1beta.IRetrieveAgentOpsObservabilityRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRetrieveAgentOpsObservabilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iretrieveagentopsobservabilityrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.geminidataanalytics.v1beta.IRetrieveAgentOpsObservabilityResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iretrieveagentopsobservabilityresponse), [protos.google.cloud.geminidataanalytics.v1beta.IRetrieveAgentOpsObservabilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iretrieveagentopsobservabilityrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setAgentOpsObservability(request, options)
    
    
    setAgentOpsObservability(request?: protos.google.cloud.geminidataanalytics.v1beta.ISetAgentOpsObservabilityRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.geminidataanalytics.v1beta.ISetAgentOpsObservabilityResponse, protos.google.cloud.geminidataanalytics.v1beta.ISetAgentOpsObservabilityMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Enables/Disables required GCP services and configures AgentOps observability settings calling the Admin Settings executable node to update the AgentOps Observability feature.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetAgentOpsObservabilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.isetagentopsobservabilityrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.geminidataanalytics.v1beta.ISetAgentOpsObservabilityResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.isetagentopsobservabilityresponse), [protos.google.cloud.geminidataanalytics.v1beta.ISetAgentOpsObservabilityMetadata](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.isetagentopsobservabilitymetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent value for SetAgentOpsObservabilityRequest.
       *  Format: projects/{project}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Optional. Whether to enable or disable AgentOps observability.
       *  When update_mask is provided, this field is ignored unless specified in the
       *  mask.
       */
      // const telemetryEnabled = true
      /**
       *  Required. The data source type for which to set observability settings.
       *  Examples: "bigquery", "looker"
       */
      // const dataSourceType = 'abc123'
      /**
       *  Optional. Whether BigQuery Agent Analytics is enabled.
       *  Note: An explicit `update_mask` containing "bqaa_enabled" is required to
       *  modify this field. If `update_mask` is omitted, this field is ignored and
       *  an existing enabled setting cannot be disabled.
       *  This is a project-level setting and does not by itself enable trace
       *  logging for any individual agent. Per-agent trace logging is controlled
       *  by `DataAgent.bigquery_agent_analytics_enabled` together with
       *  `DataAgent.bigquery_agent_analytics_table`; an agent does not inherit
       *  this setting.
       */
      // const bqaaEnabled = true
      /**
       *  Optional. Field mask is used to specify the fields to be overwritten by the
       *  update. The fields specified in the update_mask are relative to the
       *  resource. A field will be overwritten if it is in the mask.
       *  If the user does not provide a mask, only `telemetry_enabled` will be
       *  updated (for backward compatibility with legacy callers). Note that
       *  disabling BigQuery Agent Analytics (`bqaa_enabled = false`) requires
       *  providing an explicit `update_mask` containing "bqaa_enabled".
       *  Per AIP-161:
       *  - The special wildcard value '*' is supported to update all fields.
       *  - Field paths should use snake_case, though camelCase equivalents
       *    (`telemetryEnabled`, `bqaaEnabled`) are accepted for REST/JSON
       *    transcoding compatibility.
       */
      // const updateMask = {}
    
      // Imports the Geminidataanalytics library
      const {DataAgentServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataAgentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callSetAgentOpsObservability() {
        // Construct request
        const request = {
          parent,
          dataSourceType,
        };
    
        // Run request
        const [operation] = await geminidataanalyticsClient.setAgentOpsObservability(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callSetAgentOpsObservability();
    
    

### setAgentOpsObservability(request, options, callback)
    
    
    setAgentOpsObservability(request: protos.google.cloud.geminidataanalytics.v1beta.ISetAgentOpsObservabilityRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.geminidataanalytics.v1beta.ISetAgentOpsObservabilityResponse, protos.google.cloud.geminidataanalytics.v1beta.ISetAgentOpsObservabilityMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetAgentOpsObservabilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.isetagentopsobservabilityrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.geminidataanalytics.v1beta.ISetAgentOpsObservabilityResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.isetagentopsobservabilityresponse), [protos.google.cloud.geminidataanalytics.v1beta.ISetAgentOpsObservabilityMetadata](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.isetagentopsobservabilitymetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setAgentOpsObservability(request, callback)
    
    
    setAgentOpsObservability(request: protos.google.cloud.geminidataanalytics.v1beta.ISetAgentOpsObservabilityRequest, callback: Callback<LROperation<protos.google.cloud.geminidataanalytics.v1beta.ISetAgentOpsObservabilityResponse, protos.google.cloud.geminidataanalytics.v1beta.ISetAgentOpsObservabilityMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetAgentOpsObservabilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.isetagentopsobservabilityrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.geminidataanalytics.v1beta.ISetAgentOpsObservabilityResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.isetagentopsobservabilityresponse), [protos.google.cloud.geminidataanalytics.v1beta.ISetAgentOpsObservabilityMetadata](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.isetagentopsobservabilitymetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setIamPolicy(request, options)
    
    
    setIamPolicy(request?: protos.google.iam.v1.ISetIamPolicyRequest, options?: CallOptions): Promise<[
            protos.google.iam.v1.IPolicy,
            protos.google.iam.v1.ISetIamPolicyRequest | undefined,
            {} | undefined
        ]>;

Sets the IAM policy for a DataAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.isetiampolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.isetiampolicyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Policy](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.policy). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  REQUIRED: The resource for which the policy is being specified.
       *  See the operation documentation for the appropriate value for this field.
       */
      // const resource = 'abc123'
      /**
       *  REQUIRED: The complete policy to be applied to the `resource`. The size of
       *  the policy is limited to a few 10s of KB. An empty policy is a
       *  valid policy but certain Cloud Platform services (such as Projects)
       *  might reject them.
       */
      // const policy = {}
      /**
       *  OPTIONAL: A FieldMask specifying which fields of the policy to modify. Only
       *  the fields in the mask will be modified. If no mask is provided, the
       *  following default mask is used:
       *  `paths: "bindings, etag"`
       */
      // const updateMask = {}
    
      // Imports the Geminidataanalytics library
      const {DataAgentServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataAgentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callSetIamPolicy() {
        // Construct request
        const request = {
          resource,
          policy,
        };
    
        // Run request
        const response = await geminidataanalyticsClient.setIamPolicy(request);
        console.log(response);
      }
    
      callSetIamPolicy();
    
    

### setIamPolicy(request, options, callback)
    
    
    setIamPolicy(request: protos.google.iam.v1.ISetIamPolicyRequest, options: CallOptions, callback: Callback<protos.google.iam.v1.IPolicy, protos.google.iam.v1.ISetIamPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.isetiampolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.isetiampolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setIamPolicy(request, callback)
    
    
    setIamPolicy(request: protos.google.iam.v1.ISetIamPolicyRequest, callback: Callback<protos.google.iam.v1.IPolicy, protos.google.iam.v1.ISetIamPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.isetiampolicyrequest)`   
  
`callback` |  `Callback<[protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.isetiampolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataAgent(request, options)
    
    
    updateDataAgent(request?: protos.google.cloud.geminidataanalytics.v1beta.IUpdateDataAgentRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.geminidataanalytics.v1beta.IDataAgent, protos.google.cloud.geminidataanalytics.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the parameters of a single DataAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iupdatedataagentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent), [protos.google.cloud.geminidataanalytics.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Field mask is used to specify the fields to be overwritten in the
       *  DataAgent resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then all fields with non-default values
       *  present in the request will be overwritten. If a wildcard mask is provided,
       *  all fields will be overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The resource being updated.
       */
      // const dataAgent = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and the
       *  request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Geminidataanalytics library
      const {DataAgentServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataAgentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callUpdateDataAgent() {
        // Construct request
        const request = {
          dataAgent,
        };
    
        // Run request
        const [operation] = await geminidataanalyticsClient.updateDataAgent(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateDataAgent();
    
    

### updateDataAgent(request, options, callback)
    
    
    updateDataAgent(request: protos.google.cloud.geminidataanalytics.v1beta.IUpdateDataAgentRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.geminidataanalytics.v1beta.IDataAgent, protos.google.cloud.geminidataanalytics.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iupdatedataagentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent), [protos.google.cloud.geminidataanalytics.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataAgent(request, callback)
    
    
    updateDataAgent(request: protos.google.cloud.geminidataanalytics.v1beta.IUpdateDataAgentRequest, callback: Callback<LROperation<protos.google.cloud.geminidataanalytics.v1beta.IDataAgent, protos.google.cloud.geminidataanalytics.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iupdatedataagentrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent), [protos.google.cloud.geminidataanalytics.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataAgentSync(request, options)
    
    
    updateDataAgentSync(request?: protos.google.cloud.geminidataanalytics.v1beta.IUpdateDataAgentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.geminidataanalytics.v1beta.IDataAgent,
            (protos.google.cloud.geminidataanalytics.v1beta.IUpdateDataAgentRequest | undefined),
            {} | undefined
        ]>;

Updates the parameters of a single DataAgent synchronously.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iupdatedataagentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent), ([protos.google.cloud.geminidataanalytics.v1beta.IUpdateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iupdatedataagentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [DataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.dataagent). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Field mask is used to specify the fields to be overwritten in the
       *  DataAgent resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then all fields with non-default values
       *  present in the request will be overwritten. If a wildcard mask is provided,
       *  all fields will be overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The resource being updated.
       */
      // const dataAgent = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and the
       *  request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Geminidataanalytics library
      const {DataAgentServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataAgentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callUpdateDataAgentSync() {
        // Construct request
        const request = {
          dataAgent,
        };
    
        // Run request
        const response = await geminidataanalyticsClient.updateDataAgentSync(request);
        console.log(response);
      }
    
      callUpdateDataAgentSync();
    
    

### updateDataAgentSync(request, options, callback)
    
    
    updateDataAgentSync(request: protos.google.cloud.geminidataanalytics.v1beta.IUpdateDataAgentRequest, options: CallOptions, callback: Callback<protos.google.cloud.geminidataanalytics.v1beta.IDataAgent, protos.google.cloud.geminidataanalytics.v1beta.IUpdateDataAgentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iupdatedataagentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent), [protos.google.cloud.geminidataanalytics.v1beta.IUpdateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iupdatedataagentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataAgentSync(request, callback)
    
    
    updateDataAgentSync(request: protos.google.cloud.geminidataanalytics.v1beta.IUpdateDataAgentRequest, callback: Callback<protos.google.cloud.geminidataanalytics.v1beta.IDataAgent, protos.google.cloud.geminidataanalytics.v1beta.IUpdateDataAgentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iupdatedataagentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.geminidataanalytics.v1beta.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idataagent), [protos.google.cloud.geminidataanalytics.v1beta.IUpdateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iupdatedataagentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
