---
url: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient
title: Class v1beta.EvaluationServiceClient (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:18.395566+00:00
---

# Class v1beta.EvaluationServiceClient (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.EvaluationServiceClient (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0 

EvaluationService exposes methods to perform evaluation for the CES app. v1beta

## Package

[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of EvaluationServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new EvaluationServiceClient({fallback: true}, gax); ```  
  
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

### evaluationServiceStub
    
    
    evaluationServiceStub?: Promise<{
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

### agentPath(project, location, app, agent)
    
    
    agentPath(project: string, location: string, app: string, agent: string): string;

Return a fully-qualified agent resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`app` |  `string`   
  
`agent` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### appPath(project, location, app)
    
    
    appPath(project: string, location: string, app: string): string;

Return a fully-qualified app resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`app` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### appVersionPath(project, location, app, version)
    
    
    appVersionPath(project: string, location: string, app: string, version: string): string;

Return a fully-qualified appVersion resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`app` |  `string`   
  
`version` |  `string`   
  
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
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### changelogPath(project, location, app, changelog)
    
    
    changelogPath(project: string, location: string, app: string, changelog: string): string;

Return a fully-qualified changelog resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`app` |  `string`   
  
`changelog` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### checkDeleteEvaluationRunProgress(name)
    
    
    checkDeleteEvaluationRunProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.ces.v1beta.DeleteEvaluationRunOperationMetadata>>;

Check the status of the long running operation returned by `deleteEvaluationRun()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.empty), [protos.google.cloud.ces.v1beta.DeleteEvaluationRunOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.deleteevaluationrunoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the evaluation run to delete.
       */
      // const name = 'abc123'
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callDeleteEvaluationRun() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await cesClient.deleteEvaluationRun(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteEvaluationRun();
    
    

### checkExportEvaluationResultsProgress(name)
    
    
    checkExportEvaluationResultsProgress(name: string): Promise<LROperation<protos.google.cloud.ces.v1beta.ExportEvaluationResultsResponse, protos.google.cloud.ces.v1beta.ExportEvaluationResultsOperationMetadata>>;

Check the status of the long running operation returned by `exportEvaluationResults()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.ces.v1beta.ExportEvaluationResultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.exportevaluationresultsresponse), [protos.google.cloud.ces.v1beta.ExportEvaluationResultsOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.exportevaluationresultsoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the evaluation to export evaluation results
       *  from. Format:
       *  `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The resource names of the evaluation results to export.
       */
      // const names = ['abc','def']
      /**
       *  Optional. The export options for the evaluation results.
       */
      // const exportOptions = {}
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callExportEvaluationResults() {
        // Construct request
        const request = {
          parent,
          names,
        };
    
        // Run request
        const [operation] = await cesClient.exportEvaluationResults(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportEvaluationResults();
    
    

### checkExportEvaluationRunsProgress(name)
    
    
    checkExportEvaluationRunsProgress(name: string): Promise<LROperation<protos.google.cloud.ces.v1beta.ExportEvaluationRunsResponse, protos.google.cloud.ces.v1beta.ExportEvaluationRunsOperationMetadata>>;

Check the status of the long running operation returned by `exportEvaluationRuns()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.ces.v1beta.ExportEvaluationRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.exportevaluationrunsresponse), [protos.google.cloud.ces.v1beta.ExportEvaluationRunsOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.exportevaluationrunsoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the app to export evaluation runs from.
       *  Format: `projects/{project}/locations/{location}/apps/{app}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The resource names of the evaluation runs to export.
       */
      // const names = ['abc','def']
      /**
       *  Optional. The export options for the evaluation runs.
       */
      // const exportOptions = {}
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callExportEvaluationRuns() {
        // Construct request
        const request = {
          parent,
          names,
        };
    
        // Run request
        const [operation] = await cesClient.exportEvaluationRuns(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportEvaluationRuns();
    
    

### checkExportEvaluationsProgress(name)
    
    
    checkExportEvaluationsProgress(name: string): Promise<LROperation<protos.google.cloud.ces.v1beta.ExportEvaluationsResponse, protos.google.cloud.ces.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `exportEvaluations()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.ces.v1beta.ExportEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.exportevaluationsresponse), [protos.google.cloud.ces.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the app to export evaluations from.
       *  Format: `projects/{project}/locations/{location}/apps/{app}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The resource names of the evaluations to export.
       */
      // const names = ['abc','def']
      /**
       *  Optional. The export options for the evaluations.
       */
      // const exportOptions = {}
      /**
       *  Optional. Includes evaluation results in the export. At least one of
       *  include_evaluation_results or include_evaluations must be set.
       */
      // const includeEvaluationResults = true
      /**
       *  Optional. Includes evaluations in the export. At least one of
       *  include_evaluation_results or include_evaluations must be set.
       */
      // const includeEvaluations = true
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callExportEvaluations() {
        // Construct request
        const request = {
          parent,
          names,
        };
    
        // Run request
        const [operation] = await cesClient.exportEvaluations(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportEvaluations();
    
    

### checkGenerateEvaluationProgress(name)
    
    
    checkGenerateEvaluationProgress(name: string): Promise<LROperation<protos.google.cloud.ces.v1beta.Evaluation, protos.google.cloud.ces.v1beta.GenerateEvaluationOperationMetadata>>;

Check the status of the long running operation returned by `generateEvaluation()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.ces.v1beta.Evaluation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluation-class), [protos.google.cloud.ces.v1beta.GenerateEvaluationOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.generateevaluationoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The conversation to create the golden evaluation for.
       *  Format:
       *  `projects/{project}/locations/{location}/apps/{app}/conversations/{conversation}`
       */
      // const conversation = 'abc123'
      /**
       *  Optional. Indicate the source of the conversation. If not set, all sources
       *  will be searched.
       */
      // const source = {}
      /**
       *  Optional. The type of evaluation to generate. Defaults to GOLDEN if
       *  unspecified.
       */
      // const evaluationType = {}
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callGenerateEvaluation() {
        // Construct request
        const request = {
          conversation,
        };
    
        // Run request
        const [operation] = await cesClient.generateEvaluation(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callGenerateEvaluation();
    
    

### checkImportEvaluationsProgress(name)
    
    
    checkImportEvaluationsProgress(name: string): Promise<LROperation<protos.google.cloud.ces.v1beta.ImportEvaluationsResponse, protos.google.cloud.ces.v1beta.ImportEvaluationsOperationMetadata>>;

Check the status of the long running operation returned by `importEvaluations()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.ces.v1beta.ImportEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.importevaluationsresponse), [protos.google.cloud.ces.v1beta.ImportEvaluationsOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.importevaluationsoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The conversations to import the evaluations from.
       */
      // const conversationList = {}
      /**
       *  The Google Cloud Storage (https://cloud.google.com/storage/docs/) URI
       *  from which to import evaluations. The format of this URI must be
       *  `gs://

### checkRunEvaluationProgress(name)
    
    
    checkRunEvaluationProgress(name: string): Promise<LROperation<protos.google.cloud.ces.v1beta.RunEvaluationResponse, protos.google.cloud.ces.v1beta.RunEvaluationOperationMetadata>>;

Check the status of the long running operation returned by `runEvaluation()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.ces.v1beta.RunEvaluationResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.runevaluationresponse), [protos.google.cloud.ces.v1beta.RunEvaluationOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.runevaluationoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The app to evaluate.
       *  Format:
       *  `projects/{project}/locations/{location}/apps/{app}`
       */
      // const app = 'abc123'
      /**
       *  Optional. List of evaluations to run.
       *  Format:
       *  `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}`
       */
      // const evaluations = ['abc','def']
      /**
       *  Optional. An evaluation dataset to run.
       *  Format:
       *  `projects/{project}/locations/{location}/apps/{app}/evaluationDatasets/{evaluationDataset}`
       */
      // const evaluationDataset = 'abc123'
      /**
       *  Optional. The display name of the evaluation run.
       */
      // const displayName = 'abc123'
      /**
       *  Optional. The app version to evaluate.
       *  Format:
       *  `projects/{project}/locations/{location}/apps/{app}/versions/{version}`
       */
      // const appVersion = 'abc123'
      /**
       *  Optional. The configuration to use for the run.
       */
      // const config = {}
      /**
       *  Optional. The number of times to run the evaluation. If not set, the
       *  default value is 1 per golden, and 5 per scenario.
       */
      // const runCount = 1234
      /**
       *  Optional. The configuration to use for the run per persona.
       */
      // const personaRunConfigs = [1,2,3,4]
      /**
       *  Optional. Configuration for running the optimization step after the
       *  evaluation run. If not set, the optimization step will not be run.
       */
      // const optimizationConfig = {}
      /**
       *  Optional. The resource name of the `ScheduledEvaluationRun` that is
       *  triggering this evaluation run.
       *  If this field is set, the `scheduled_evaluation_run` field on the created
       *  `EvaluationRun` resource will be populated from this value.
       *  Format:
       *  `projects/{project}/locations/{location}/apps/{app}/scheduledEvaluationRuns/{scheduled_evaluation_run}`
       */
      // const scheduledEvaluationRun = 'abc123'
      /**
       *  Optional. The method to run the evaluation if it is a golden evaluation. If
       *  not set, default to STABLE.
       */
      // const goldenRunMethod = {}
      /**
       *  Optional. Whether to generate a latency report for the evaluation run.
       */
      // const generateLatencyReport = true
      /**
       *  Optional. The caching settings to use for the evaluation run.
       */
      // const evaluationRunCachingSettings = {}
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callRunEvaluation() {
        // Construct request
        const request = {
          app,
        };
    
        // Run request
        const [operation] = await cesClient.runEvaluation(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callRunEvaluation();
    
    

### checkRunEvaluationResultMetricsProgress(name)
    
    
    checkRunEvaluationResultMetricsProgress(name: string): Promise<LROperation<protos.google.cloud.ces.v1beta.RunEvaluationResultMetricsResponse, protos.google.cloud.ces.v1beta.RunEvaluationResultMetricsOperationMetadata>>;

Check the status of the long running operation returned by `runEvaluationResultMetrics()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.ces.v1beta.RunEvaluationResultMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.runevaluationresultmetricsresponse), [protos.google.cloud.ces.v1beta.RunEvaluationResultMetricsOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.runevaluationresultmetricsoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The evaluation result to run metrics for.
       *  Format:
       *  `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}/results/{evaluation_result_id}`
       */
      // const evaluationResultId = 'abc123'
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callRunEvaluationResultMetrics() {
        // Construct request
        const request = {
          evaluationResultId,
        };
    
        // Run request
        const [operation] = await cesClient.runEvaluationResultMetrics(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callRunEvaluationResultMetrics();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### conversationPath(project, location, app, conversation)
    
    
    conversationPath(project: string, location: string, app: string, conversation: string): string;

Return a fully-qualified conversation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`app` |  `string`   
  
`conversation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### createEvaluation(request, options)
    
    
    createEvaluation(request?: protos.google.cloud.ces.v1beta.ICreateEvaluationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IEvaluation,
            protos.google.cloud.ces.v1beta.ICreateEvaluationRequest | undefined,
            {} | undefined
        ]>;

Creates an evaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreateevaluationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluation), [protos.google.cloud.ces.v1beta.ICreateEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreateevaluationrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The app to create the evaluation for.
       *  Format:
       *  `projects/{project}/locations/{location}/apps/{app}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. The ID to use for the evaluation, which will become the final
       *  component of the evaluation's resource name. If not provided, a unique ID
       *  will be automatically assigned for the evaluation.
       */
      // const evaluationId = 'abc123'
      /**
       *  Required. The evaluation to create.
       */
      // const evaluation = {}
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callCreateEvaluation() {
        // Construct request
        const request = {
          parent,
          evaluation,
        };
    
        // Run request
        const response = await cesClient.createEvaluation(request);
        console.log(response);
      }
    
      callCreateEvaluation();
    
    

### createEvaluation(request, options, callback)
    
    
    createEvaluation(request: protos.google.cloud.ces.v1beta.ICreateEvaluationRequest, options: CallOptions, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluation, protos.google.cloud.ces.v1beta.ICreateEvaluationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreateevaluationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluation), [protos.google.cloud.ces.v1beta.ICreateEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreateevaluationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEvaluation(request, callback)
    
    
    createEvaluation(request: protos.google.cloud.ces.v1beta.ICreateEvaluationRequest, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluation, protos.google.cloud.ces.v1beta.ICreateEvaluationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreateevaluationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluation), [protos.google.cloud.ces.v1beta.ICreateEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreateevaluationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEvaluationDataset(request, options)
    
    
    createEvaluationDataset(request?: protos.google.cloud.ces.v1beta.ICreateEvaluationDatasetRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IEvaluationDataset,
            (protos.google.cloud.ces.v1beta.ICreateEvaluationDatasetRequest | undefined),
            {} | undefined
        ]>;

Creates an evaluation dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreateevaluationdatasetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IEvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationdataset), ([protos.google.cloud.ces.v1beta.ICreateEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreateevaluationdatasetrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [EvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluationdataset). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The app to create the evaluation for.
       *  Format:
       *  `projects/{project}/locations/{location}/apps/{app}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. The ID to use for the evaluation dataset, which will become the
       *  final component of the evaluation dataset's resource name. If not provided,
       *  a unique ID will be automatically assigned for the evaluation.
       */
      // const evaluationDatasetId = 'abc123'
      /**
       *  Required. The evaluation dataset to create.
       */
      // const evaluationDataset = {}
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callCreateEvaluationDataset() {
        // Construct request
        const request = {
          parent,
          evaluationDataset,
        };
    
        // Run request
        const response = await cesClient.createEvaluationDataset(request);
        console.log(response);
      }
    
      callCreateEvaluationDataset();
    
    

### createEvaluationDataset(request, options, callback)
    
    
    createEvaluationDataset(request: protos.google.cloud.ces.v1beta.ICreateEvaluationDatasetRequest, options: CallOptions, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluationDataset, protos.google.cloud.ces.v1beta.ICreateEvaluationDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreateevaluationdatasetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationdataset), [protos.google.cloud.ces.v1beta.ICreateEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreateevaluationdatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEvaluationDataset(request, callback)
    
    
    createEvaluationDataset(request: protos.google.cloud.ces.v1beta.ICreateEvaluationDatasetRequest, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluationDataset, protos.google.cloud.ces.v1beta.ICreateEvaluationDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreateevaluationdatasetrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationdataset), [protos.google.cloud.ces.v1beta.ICreateEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreateevaluationdatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEvaluationExpectation(request, options)
    
    
    createEvaluationExpectation(request?: protos.google.cloud.ces.v1beta.ICreateEvaluationExpectationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IEvaluationExpectation,
            (protos.google.cloud.ces.v1beta.ICreateEvaluationExpectationRequest | undefined),
            {} | undefined
        ]>;

Creates an evaluation expectation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreateevaluationexpectationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IEvaluationExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationexpectation), ([protos.google.cloud.ces.v1beta.ICreateEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreateevaluationexpectationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The app to create the evaluation expectation for.
       *  Format:
       *  `projects/{project}/locations/{location}/apps/{app}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. The ID to use for the evaluation expectation, which will become
       *  the final component of the evaluation expectation's resource name. If not
       *  provided, a unique ID will be automatically assigned for the evaluation
       *  expectation.
       */
      // const evaluationExpectationId = 'abc123'
      /**
       *  Required. The evaluation expectation to create.
       */
      // const evaluationExpectation = {}
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callCreateEvaluationExpectation() {
        // Construct request
        const request = {
          parent,
          evaluationExpectation,
        };
    
        // Run request
        const response = await cesClient.createEvaluationExpectation(request);
        console.log(response);
      }
    
      callCreateEvaluationExpectation();
    
    

### createEvaluationExpectation(request, options, callback)
    
    
    createEvaluationExpectation(request: protos.google.cloud.ces.v1beta.ICreateEvaluationExpectationRequest, options: CallOptions, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluationExpectation, protos.google.cloud.ces.v1beta.ICreateEvaluationExpectationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreateevaluationexpectationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluationExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationexpectation), [protos.google.cloud.ces.v1beta.ICreateEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreateevaluationexpectationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEvaluationExpectation(request, callback)
    
    
    createEvaluationExpectation(request: protos.google.cloud.ces.v1beta.ICreateEvaluationExpectationRequest, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluationExpectation, protos.google.cloud.ces.v1beta.ICreateEvaluationExpectationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreateevaluationexpectationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluationExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationexpectation), [protos.google.cloud.ces.v1beta.ICreateEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreateevaluationexpectationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createScheduledEvaluationRun(request, options)
    
    
    createScheduledEvaluationRun(request?: protos.google.cloud.ces.v1beta.ICreateScheduledEvaluationRunRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IScheduledEvaluationRun,
            (protos.google.cloud.ces.v1beta.ICreateScheduledEvaluationRunRequest | undefined),
            {} | undefined
        ]>;

Creates a scheduled evaluation run.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreatescheduledevaluationrunrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IScheduledEvaluationRun](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ischeduledevaluationrun), ([protos.google.cloud.ces.v1beta.ICreateScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreatescheduledevaluationrunrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The app to create the scheduled evaluation run for.
       *  Format:
       *  `projects/{project}/locations/{location}/apps/{app}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. The ID to use for the scheduled evaluation run, which will become
       *  the final component of the scheduled evaluation run's resource name. If not
       *  provided, a unique ID will be automatically assigned.
       */
      // const scheduledEvaluationRunId = 'abc123'
      /**
       *  Required. The scheduled evaluation run to create.
       */
      // const scheduledEvaluationRun = {}
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callCreateScheduledEvaluationRun() {
        // Construct request
        const request = {
          parent,
          scheduledEvaluationRun,
        };
    
        // Run request
        const response = await cesClient.createScheduledEvaluationRun(request);
        console.log(response);
      }
    
      callCreateScheduledEvaluationRun();
    
    

### createScheduledEvaluationRun(request, options, callback)
    
    
    createScheduledEvaluationRun(request: protos.google.cloud.ces.v1beta.ICreateScheduledEvaluationRunRequest, options: CallOptions, callback: Callback<protos.google.cloud.ces.v1beta.IScheduledEvaluationRun, protos.google.cloud.ces.v1beta.ICreateScheduledEvaluationRunRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreatescheduledevaluationrunrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IScheduledEvaluationRun](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ischeduledevaluationrun), [protos.google.cloud.ces.v1beta.ICreateScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreatescheduledevaluationrunrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createScheduledEvaluationRun(request, callback)
    
    
    createScheduledEvaluationRun(request: protos.google.cloud.ces.v1beta.ICreateScheduledEvaluationRunRequest, callback: Callback<protos.google.cloud.ces.v1beta.IScheduledEvaluationRun, protos.google.cloud.ces.v1beta.ICreateScheduledEvaluationRunRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreatescheduledevaluationrunrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IScheduledEvaluationRun](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ischeduledevaluationrun), [protos.google.cloud.ces.v1beta.ICreateScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.icreatescheduledevaluationrunrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEvaluation(request, options)
    
    
    deleteEvaluation(request?: protos.google.cloud.ces.v1beta.IDeleteEvaluationRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.cloud.ces.v1beta.IDeleteEvaluationRequest | undefined,
            {} | undefined
        ]>;

Deletes an evaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.iempty), [protos.google.cloud.ces.v1beta.IDeleteEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the evaluation to delete.
       */
      // const name = 'abc123'
      /**
       *  Optional. Indicates whether to forcefully delete the evaluation, even if it
       *  is still referenced by evaluation datasets.
       *  *  If `force = false`, the deletion will fail if any datasets still
       *  reference the evaluation.
       *  *  If `force = true`, all existing references from datasets will be removed
       *  and the evaluation will be deleted.
       */
      // const force = true
      /**
       *  Optional. The current etag of the evaluation. If an etag is not provided,
       *  the deletion will overwrite any concurrent changes. If an etag is provided
       *  and does not match the current etag of the evaluation, deletion will be
       *  blocked and an ABORTED error will be returned.
       */
      // const etag = 'abc123'
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callDeleteEvaluation() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await cesClient.deleteEvaluation(request);
        console.log(response);
      }
    
      callDeleteEvaluation();
    
    

### deleteEvaluation(request, options, callback)
    
    
    deleteEvaluation(request: protos.google.cloud.ces.v1beta.IDeleteEvaluationRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.ces.v1beta.IDeleteEvaluationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.iempty), [protos.google.cloud.ces.v1beta.IDeleteEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEvaluation(request, callback)
    
    
    deleteEvaluation(request: protos.google.cloud.ces.v1beta.IDeleteEvaluationRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.ces.v1beta.IDeleteEvaluationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.iempty), [protos.google.cloud.ces.v1beta.IDeleteEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEvaluationDataset(request, options)
    
    
    deleteEvaluationDataset(request?: protos.google.cloud.ces.v1beta.IDeleteEvaluationDatasetRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.ces.v1beta.IDeleteEvaluationDatasetRequest | undefined),
            {} | undefined
        ]>;

Deletes an evaluation dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationdatasetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.iempty), ([protos.google.cloud.ces.v1beta.IDeleteEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationdatasetrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the evaluation dataset to delete.
       */
      // const name = 'abc123'
      /**
       *  Optional. The current etag of the evaluation dataset. If an etag is not
       *  provided, the deletion will overwrite any concurrent changes. If an etag is
       *  provided and does not match the current etag of the evaluation dataset,
       *  deletion will be blocked and an ABORTED error will be returned.
       */
      // const etag = 'abc123'
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callDeleteEvaluationDataset() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await cesClient.deleteEvaluationDataset(request);
        console.log(response);
      }
    
      callDeleteEvaluationDataset();
    
    

### deleteEvaluationDataset(request, options, callback)
    
    
    deleteEvaluationDataset(request: protos.google.cloud.ces.v1beta.IDeleteEvaluationDatasetRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.ces.v1beta.IDeleteEvaluationDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationdatasetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.iempty), [protos.google.cloud.ces.v1beta.IDeleteEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationdatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEvaluationDataset(request, callback)
    
    
    deleteEvaluationDataset(request: protos.google.cloud.ces.v1beta.IDeleteEvaluationDatasetRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.ces.v1beta.IDeleteEvaluationDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationdatasetrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.iempty), [protos.google.cloud.ces.v1beta.IDeleteEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationdatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEvaluationExpectation(request, options)
    
    
    deleteEvaluationExpectation(request?: protos.google.cloud.ces.v1beta.IDeleteEvaluationExpectationRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.ces.v1beta.IDeleteEvaluationExpectationRequest | undefined),
            {} | undefined
        ]>;

Deletes an evaluation expectation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationexpectationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.iempty), ([protos.google.cloud.ces.v1beta.IDeleteEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationexpectationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the evaluation expectation to delete.
       */
      // const name = 'abc123'
      /**
       *  Optional. The current etag of the evaluation expectation. If an etag is not
       *  provided, the deletion will overwrite any concurrent changes. If an etag is
       *  provided and does not match the current etag of the evaluation expectation,
       *  deletion will be blocked and an ABORTED error will be returned.
       */
      // const etag = 'abc123'
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callDeleteEvaluationExpectation() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await cesClient.deleteEvaluationExpectation(request);
        console.log(response);
      }
    
      callDeleteEvaluationExpectation();
    
    

### deleteEvaluationExpectation(request, options, callback)
    
    
    deleteEvaluationExpectation(request: protos.google.cloud.ces.v1beta.IDeleteEvaluationExpectationRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.ces.v1beta.IDeleteEvaluationExpectationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationexpectationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.iempty), [protos.google.cloud.ces.v1beta.IDeleteEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationexpectationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEvaluationExpectation(request, callback)
    
    
    deleteEvaluationExpectation(request: protos.google.cloud.ces.v1beta.IDeleteEvaluationExpectationRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.ces.v1beta.IDeleteEvaluationExpectationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationexpectationrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.iempty), [protos.google.cloud.ces.v1beta.IDeleteEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationexpectationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEvaluationResult(request, options)
    
    
    deleteEvaluationResult(request?: protos.google.cloud.ces.v1beta.IDeleteEvaluationResultRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.cloud.ces.v1beta.IDeleteEvaluationResultRequest | undefined,
            {} | undefined
        ]>;

Deletes an evaluation result.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEvaluationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationresultrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.iempty), [protos.google.cloud.ces.v1beta.IDeleteEvaluationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationresultrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the evaluation result to delete.
       */
      // const name = 'abc123'
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callDeleteEvaluationResult() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await cesClient.deleteEvaluationResult(request);
        console.log(response);
      }
    
      callDeleteEvaluationResult();
    
    

### deleteEvaluationResult(request, options, callback)
    
    
    deleteEvaluationResult(request: protos.google.cloud.ces.v1beta.IDeleteEvaluationResultRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.ces.v1beta.IDeleteEvaluationResultRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEvaluationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationresultrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.iempty), [protos.google.cloud.ces.v1beta.IDeleteEvaluationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationresultrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEvaluationResult(request, callback)
    
    
    deleteEvaluationResult(request: protos.google.cloud.ces.v1beta.IDeleteEvaluationResultRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.ces.v1beta.IDeleteEvaluationResultRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEvaluationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationresultrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.iempty), [protos.google.cloud.ces.v1beta.IDeleteEvaluationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationresultrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEvaluationRun(request, options)
    
    
    deleteEvaluationRun(request?: protos.google.cloud.ces.v1beta.IDeleteEvaluationRunRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.ces.v1beta.IDeleteEvaluationRunOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes an evaluation run.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationrunrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.iempty), [protos.google.cloud.ces.v1beta.IDeleteEvaluationRunOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationrunoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the evaluation run to delete.
       */
      // const name = 'abc123'
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callDeleteEvaluationRun() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await cesClient.deleteEvaluationRun(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteEvaluationRun();
    
    

### deleteEvaluationRun(request, options, callback)
    
    
    deleteEvaluationRun(request: protos.google.cloud.ces.v1beta.IDeleteEvaluationRunRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.ces.v1beta.IDeleteEvaluationRunOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationrunrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.iempty), [protos.google.cloud.ces.v1beta.IDeleteEvaluationRunOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationrunoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEvaluationRun(request, callback)
    
    
    deleteEvaluationRun(request: protos.google.cloud.ces.v1beta.IDeleteEvaluationRunRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.ces.v1beta.IDeleteEvaluationRunOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationrunrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.iempty), [protos.google.cloud.ces.v1beta.IDeleteEvaluationRunOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideleteevaluationrunoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### deleteScheduledEvaluationRun(request, options)
    
    
    deleteScheduledEvaluationRun(request?: protos.google.cloud.ces.v1beta.IDeleteScheduledEvaluationRunRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.ces.v1beta.IDeleteScheduledEvaluationRunRequest | undefined),
            {} | undefined
        ]>;

Deletes a scheduled evaluation run.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideletescheduledevaluationrunrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.iempty), ([protos.google.cloud.ces.v1beta.IDeleteScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideletescheduledevaluationrunrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the scheduled evaluation run to delete.
       */
      // const name = 'abc123'
      /**
       *  Optional. The etag of the ScheduledEvaluationRun.
       *  If provided, it must match the server's etag.
       */
      // const etag = 'abc123'
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callDeleteScheduledEvaluationRun() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await cesClient.deleteScheduledEvaluationRun(request);
        console.log(response);
      }
    
      callDeleteScheduledEvaluationRun();
    
    

### deleteScheduledEvaluationRun(request, options, callback)
    
    
    deleteScheduledEvaluationRun(request: protos.google.cloud.ces.v1beta.IDeleteScheduledEvaluationRunRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.ces.v1beta.IDeleteScheduledEvaluationRunRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideletescheduledevaluationrunrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.iempty), [protos.google.cloud.ces.v1beta.IDeleteScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideletescheduledevaluationrunrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteScheduledEvaluationRun(request, callback)
    
    
    deleteScheduledEvaluationRun(request: protos.google.cloud.ces.v1beta.IDeleteScheduledEvaluationRunRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.ces.v1beta.IDeleteScheduledEvaluationRunRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideletescheduledevaluationrunrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.iempty), [protos.google.cloud.ces.v1beta.IDeleteScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ideletescheduledevaluationrunrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deploymentPath(project, location, app, deployment)
    
    
    deploymentPath(project: string, location: string, app: string, deployment: string): string;

Return a fully-qualified deployment resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`app` |  `string`   
  
`deployment` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### evaluationDatasetPath(project, location, app, evaluationDataset)
    
    
    evaluationDatasetPath(project: string, location: string, app: string, evaluationDataset: string): string;

Return a fully-qualified evaluationDataset resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`app` |  `string`   
  
`evaluationDataset` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### evaluationExpectationPath(project, location, app, evaluationExpectation)
    
    
    evaluationExpectationPath(project: string, location: string, app: string, evaluationExpectation: string): string;

Return a fully-qualified evaluationExpectation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`app` |  `string`   
  
`evaluationExpectation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### evaluationPath(project, location, app, evaluation)
    
    
    evaluationPath(project: string, location: string, app: string, evaluation: string): string;

Return a fully-qualified evaluation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`app` |  `string`   
  
`evaluation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### evaluationResultPath(project, location, app, evaluation, evaluationResult)
    
    
    evaluationResultPath(project: string, location: string, app: string, evaluation: string, evaluationResult: string): string;

Return a fully-qualified evaluationResult resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`app` |  `string`   
  
`evaluation` |  `string`   
  
`evaluationResult` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### evaluationRunPath(project, location, app, evaluationRun)
    
    
    evaluationRunPath(project: string, location: string, app: string, evaluationRun: string): string;

Return a fully-qualified evaluationRun resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`app` |  `string`   
  
`evaluationRun` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### examplePath(project, location, app, example)
    
    
    examplePath(project: string, location: string, app: string, example: string): string;

Return a fully-qualified example resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`app` |  `string`   
  
`example` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### exportEvaluationResults(request, options)
    
    
    exportEvaluationResults(request?: protos.google.cloud.ces.v1beta.IExportEvaluationResultsRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.ces.v1beta.IExportEvaluationResultsResponse, protos.google.cloud.ces.v1beta.IExportEvaluationResultsOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Exports evaluations results.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportEvaluationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationresultsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.ces.v1beta.IExportEvaluationResultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationresultsresponse), [protos.google.cloud.ces.v1beta.IExportEvaluationResultsOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationresultsoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the evaluation to export evaluation results
       *  from. Format:
       *  `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The resource names of the evaluation results to export.
       */
      // const names = ['abc','def']
      /**
       *  Optional. The export options for the evaluation results.
       */
      // const exportOptions = {}
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callExportEvaluationResults() {
        // Construct request
        const request = {
          parent,
          names,
        };
    
        // Run request
        const [operation] = await cesClient.exportEvaluationResults(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportEvaluationResults();
    
    

### exportEvaluationResults(request, options, callback)
    
    
    exportEvaluationResults(request: protos.google.cloud.ces.v1beta.IExportEvaluationResultsRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.ces.v1beta.IExportEvaluationResultsResponse, protos.google.cloud.ces.v1beta.IExportEvaluationResultsOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportEvaluationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationresultsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.ces.v1beta.IExportEvaluationResultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationresultsresponse), [protos.google.cloud.ces.v1beta.IExportEvaluationResultsOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationresultsoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportEvaluationResults(request, callback)
    
    
    exportEvaluationResults(request: protos.google.cloud.ces.v1beta.IExportEvaluationResultsRequest, callback: Callback<LROperation<protos.google.cloud.ces.v1beta.IExportEvaluationResultsResponse, protos.google.cloud.ces.v1beta.IExportEvaluationResultsOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportEvaluationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationresultsrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.ces.v1beta.IExportEvaluationResultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationresultsresponse), [protos.google.cloud.ces.v1beta.IExportEvaluationResultsOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationresultsoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportEvaluationRuns(request, options)
    
    
    exportEvaluationRuns(request?: protos.google.cloud.ces.v1beta.IExportEvaluationRunsRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.ces.v1beta.IExportEvaluationRunsResponse, protos.google.cloud.ces.v1beta.IExportEvaluationRunsOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Exports evaluations runs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportEvaluationRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationrunsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.ces.v1beta.IExportEvaluationRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationrunsresponse), [protos.google.cloud.ces.v1beta.IExportEvaluationRunsOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationrunsoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the app to export evaluation runs from.
       *  Format: `projects/{project}/locations/{location}/apps/{app}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The resource names of the evaluation runs to export.
       */
      // const names = ['abc','def']
      /**
       *  Optional. The export options for the evaluation runs.
       */
      // const exportOptions = {}
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callExportEvaluationRuns() {
        // Construct request
        const request = {
          parent,
          names,
        };
    
        // Run request
        const [operation] = await cesClient.exportEvaluationRuns(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportEvaluationRuns();
    
    

### exportEvaluationRuns(request, options, callback)
    
    
    exportEvaluationRuns(request: protos.google.cloud.ces.v1beta.IExportEvaluationRunsRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.ces.v1beta.IExportEvaluationRunsResponse, protos.google.cloud.ces.v1beta.IExportEvaluationRunsOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportEvaluationRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationrunsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.ces.v1beta.IExportEvaluationRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationrunsresponse), [protos.google.cloud.ces.v1beta.IExportEvaluationRunsOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationrunsoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportEvaluationRuns(request, callback)
    
    
    exportEvaluationRuns(request: protos.google.cloud.ces.v1beta.IExportEvaluationRunsRequest, callback: Callback<LROperation<protos.google.cloud.ces.v1beta.IExportEvaluationRunsResponse, protos.google.cloud.ces.v1beta.IExportEvaluationRunsOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportEvaluationRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationrunsrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.ces.v1beta.IExportEvaluationRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationrunsresponse), [protos.google.cloud.ces.v1beta.IExportEvaluationRunsOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationrunsoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportEvaluations(request, options)
    
    
    exportEvaluations(request?: protos.google.cloud.ces.v1beta.IExportEvaluationsRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.ces.v1beta.IExportEvaluationsResponse, protos.google.cloud.ces.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Exports evaluations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.ces.v1beta.IExportEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationsresponse), [protos.google.cloud.ces.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the app to export evaluations from.
       *  Format: `projects/{project}/locations/{location}/apps/{app}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The resource names of the evaluations to export.
       */
      // const names = ['abc','def']
      /**
       *  Optional. The export options for the evaluations.
       */
      // const exportOptions = {}
      /**
       *  Optional. Includes evaluation results in the export. At least one of
       *  include_evaluation_results or include_evaluations must be set.
       */
      // const includeEvaluationResults = true
      /**
       *  Optional. Includes evaluations in the export. At least one of
       *  include_evaluation_results or include_evaluations must be set.
       */
      // const includeEvaluations = true
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callExportEvaluations() {
        // Construct request
        const request = {
          parent,
          names,
        };
    
        // Run request
        const [operation] = await cesClient.exportEvaluations(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportEvaluations();
    
    

### exportEvaluations(request, options, callback)
    
    
    exportEvaluations(request: protos.google.cloud.ces.v1beta.IExportEvaluationsRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.ces.v1beta.IExportEvaluationsResponse, protos.google.cloud.ces.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.ces.v1beta.IExportEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationsresponse), [protos.google.cloud.ces.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportEvaluations(request, callback)
    
    
    exportEvaluations(request: protos.google.cloud.ces.v1beta.IExportEvaluationsRequest, callback: Callback<LROperation<protos.google.cloud.ces.v1beta.IExportEvaluationsResponse, protos.google.cloud.ces.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationsrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.ces.v1beta.IExportEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iexportevaluationsresponse), [protos.google.cloud.ces.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateEvaluation(request, options)
    
    
    generateEvaluation(request?: protos.google.cloud.ces.v1beta.IGenerateEvaluationRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.ces.v1beta.IEvaluation, protos.google.cloud.ces.v1beta.IGenerateEvaluationOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a golden evaluation from a conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igenerateevaluationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.ces.v1beta.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluation), [protos.google.cloud.ces.v1beta.IGenerateEvaluationOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igenerateevaluationoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The conversation to create the golden evaluation for.
       *  Format:
       *  `projects/{project}/locations/{location}/apps/{app}/conversations/{conversation}`
       */
      // const conversation = 'abc123'
      /**
       *  Optional. Indicate the source of the conversation. If not set, all sources
       *  will be searched.
       */
      // const source = {}
      /**
       *  Optional. The type of evaluation to generate. Defaults to GOLDEN if
       *  unspecified.
       */
      // const evaluationType = {}
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callGenerateEvaluation() {
        // Construct request
        const request = {
          conversation,
        };
    
        // Run request
        const [operation] = await cesClient.generateEvaluation(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callGenerateEvaluation();
    
    

### generateEvaluation(request, options, callback)
    
    
    generateEvaluation(request: protos.google.cloud.ces.v1beta.IGenerateEvaluationRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.ces.v1beta.IEvaluation, protos.google.cloud.ces.v1beta.IGenerateEvaluationOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igenerateevaluationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.ces.v1beta.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluation), [protos.google.cloud.ces.v1beta.IGenerateEvaluationOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igenerateevaluationoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateEvaluation(request, callback)
    
    
    generateEvaluation(request: protos.google.cloud.ces.v1beta.IGenerateEvaluationRequest, callback: Callback<LROperation<protos.google.cloud.ces.v1beta.IEvaluation, protos.google.cloud.ces.v1beta.IGenerateEvaluationOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igenerateevaluationrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.ces.v1beta.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluation), [protos.google.cloud.ces.v1beta.IGenerateEvaluationOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igenerateevaluationoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEvaluation(request, options)
    
    
    getEvaluation(request?: protos.google.cloud.ces.v1beta.IGetEvaluationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IEvaluation,
            protos.google.cloud.ces.v1beta.IGetEvaluationRequest | undefined,
            {} | undefined
        ]>;

Gets details of the specified evaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluation), [protos.google.cloud.ces.v1beta.IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the evaluation to retrieve.
       */
      // const name = 'abc123'
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callGetEvaluation() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await cesClient.getEvaluation(request);
        console.log(response);
      }
    
      callGetEvaluation();
    
    

### getEvaluation(request, options, callback)
    
    
    getEvaluation(request: protos.google.cloud.ces.v1beta.IGetEvaluationRequest, options: CallOptions, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluation, protos.google.cloud.ces.v1beta.IGetEvaluationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluation), [protos.google.cloud.ces.v1beta.IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEvaluation(request, callback)
    
    
    getEvaluation(request: protos.google.cloud.ces.v1beta.IGetEvaluationRequest, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluation, protos.google.cloud.ces.v1beta.IGetEvaluationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluation), [protos.google.cloud.ces.v1beta.IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEvaluationDataset(request, options)
    
    
    getEvaluationDataset(request?: protos.google.cloud.ces.v1beta.IGetEvaluationDatasetRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IEvaluationDataset,
            protos.google.cloud.ces.v1beta.IGetEvaluationDatasetRequest | undefined,
            {} | undefined
        ]>;

Gets details of the specified evaluation dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationdatasetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IEvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationdataset), [protos.google.cloud.ces.v1beta.IGetEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationdatasetrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [EvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluationdataset). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the evaluation dataset to retrieve.
       */
      // const name = 'abc123'
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callGetEvaluationDataset() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await cesClient.getEvaluationDataset(request);
        console.log(response);
      }
    
      callGetEvaluationDataset();
    
    

### getEvaluationDataset(request, options, callback)
    
    
    getEvaluationDataset(request: protos.google.cloud.ces.v1beta.IGetEvaluationDatasetRequest, options: CallOptions, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluationDataset, protos.google.cloud.ces.v1beta.IGetEvaluationDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationdatasetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationdataset), [protos.google.cloud.ces.v1beta.IGetEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationdatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEvaluationDataset(request, callback)
    
    
    getEvaluationDataset(request: protos.google.cloud.ces.v1beta.IGetEvaluationDatasetRequest, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluationDataset, protos.google.cloud.ces.v1beta.IGetEvaluationDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationdatasetrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationdataset), [protos.google.cloud.ces.v1beta.IGetEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationdatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEvaluationExpectation(request, options)
    
    
    getEvaluationExpectation(request?: protos.google.cloud.ces.v1beta.IGetEvaluationExpectationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IEvaluationExpectation,
            (protos.google.cloud.ces.v1beta.IGetEvaluationExpectationRequest | undefined),
            {} | undefined
        ]>;

Gets details of the specified evaluation expectation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationexpectationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IEvaluationExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationexpectation), ([protos.google.cloud.ces.v1beta.IGetEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationexpectationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the evaluation expectation to retrieve.
       */
      // const name = 'abc123'
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callGetEvaluationExpectation() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await cesClient.getEvaluationExpectation(request);
        console.log(response);
      }
    
      callGetEvaluationExpectation();
    
    

### getEvaluationExpectation(request, options, callback)
    
    
    getEvaluationExpectation(request: protos.google.cloud.ces.v1beta.IGetEvaluationExpectationRequest, options: CallOptions, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluationExpectation, protos.google.cloud.ces.v1beta.IGetEvaluationExpectationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationexpectationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluationExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationexpectation), [protos.google.cloud.ces.v1beta.IGetEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationexpectationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEvaluationExpectation(request, callback)
    
    
    getEvaluationExpectation(request: protos.google.cloud.ces.v1beta.IGetEvaluationExpectationRequest, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluationExpectation, protos.google.cloud.ces.v1beta.IGetEvaluationExpectationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationexpectationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluationExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationexpectation), [protos.google.cloud.ces.v1beta.IGetEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationexpectationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEvaluationResult(request, options)
    
    
    getEvaluationResult(request?: protos.google.cloud.ces.v1beta.IGetEvaluationResultRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IEvaluationResult,
            protos.google.cloud.ces.v1beta.IGetEvaluationResultRequest | undefined,
            {} | undefined
        ]>;

Gets details of the specified evaluation result.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationresultrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IEvaluationResult](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationresult), [protos.google.cloud.ces.v1beta.IGetEvaluationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationresultrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the evaluation result to retrieve.
       */
      // const name = 'abc123'
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callGetEvaluationResult() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await cesClient.getEvaluationResult(request);
        console.log(response);
      }
    
      callGetEvaluationResult();
    
    

### getEvaluationResult(request, options, callback)
    
    
    getEvaluationResult(request: protos.google.cloud.ces.v1beta.IGetEvaluationResultRequest, options: CallOptions, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluationResult, protos.google.cloud.ces.v1beta.IGetEvaluationResultRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationresultrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluationResult](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationresult), [protos.google.cloud.ces.v1beta.IGetEvaluationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationresultrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEvaluationResult(request, callback)
    
    
    getEvaluationResult(request: protos.google.cloud.ces.v1beta.IGetEvaluationResultRequest, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluationResult, protos.google.cloud.ces.v1beta.IGetEvaluationResultRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationresultrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluationResult](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationresult), [protos.google.cloud.ces.v1beta.IGetEvaluationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationresultrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEvaluationRun(request, options)
    
    
    getEvaluationRun(request?: protos.google.cloud.ces.v1beta.IGetEvaluationRunRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IEvaluationRun,
            protos.google.cloud.ces.v1beta.IGetEvaluationRunRequest | undefined,
            {} | undefined
        ]>;

Gets details of the specified evaluation run.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationrunrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IEvaluationRun](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationrun), [protos.google.cloud.ces.v1beta.IGetEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationrunrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the evaluation run to retrieve.
       */
      // const name = 'abc123'
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callGetEvaluationRun() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await cesClient.getEvaluationRun(request);
        console.log(response);
      }
    
      callGetEvaluationRun();
    
    

### getEvaluationRun(request, options, callback)
    
    
    getEvaluationRun(request: protos.google.cloud.ces.v1beta.IGetEvaluationRunRequest, options: CallOptions, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluationRun, protos.google.cloud.ces.v1beta.IGetEvaluationRunRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationrunrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluationRun](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationrun), [protos.google.cloud.ces.v1beta.IGetEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationrunrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEvaluationRun(request, callback)
    
    
    getEvaluationRun(request: protos.google.cloud.ces.v1beta.IGetEvaluationRunRequest, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluationRun, protos.google.cloud.ces.v1beta.IGetEvaluationRunRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationrunrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluationRun](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationrun), [protos.google.cloud.ces.v1beta.IGetEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetevaluationrunrequest) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.operation)]>` |   
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
  
### getScheduledEvaluationRun(request, options)
    
    
    getScheduledEvaluationRun(request?: protos.google.cloud.ces.v1beta.IGetScheduledEvaluationRunRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IScheduledEvaluationRun,
            (protos.google.cloud.ces.v1beta.IGetScheduledEvaluationRunRequest | undefined),
            {} | undefined
        ]>;

Gets details of the specified scheduled evaluation run.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetscheduledevaluationrunrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IScheduledEvaluationRun](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ischeduledevaluationrun), ([protos.google.cloud.ces.v1beta.IGetScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetscheduledevaluationrunrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the scheduled evaluation run to retrieve.
       */
      // const name = 'abc123'
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callGetScheduledEvaluationRun() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await cesClient.getScheduledEvaluationRun(request);
        console.log(response);
      }
    
      callGetScheduledEvaluationRun();
    
    

### getScheduledEvaluationRun(request, options, callback)
    
    
    getScheduledEvaluationRun(request: protos.google.cloud.ces.v1beta.IGetScheduledEvaluationRunRequest, options: CallOptions, callback: Callback<protos.google.cloud.ces.v1beta.IScheduledEvaluationRun, protos.google.cloud.ces.v1beta.IGetScheduledEvaluationRunRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetscheduledevaluationrunrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IScheduledEvaluationRun](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ischeduledevaluationrun), [protos.google.cloud.ces.v1beta.IGetScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetscheduledevaluationrunrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getScheduledEvaluationRun(request, callback)
    
    
    getScheduledEvaluationRun(request: protos.google.cloud.ces.v1beta.IGetScheduledEvaluationRunRequest, callback: Callback<protos.google.cloud.ces.v1beta.IScheduledEvaluationRun, protos.google.cloud.ces.v1beta.IGetScheduledEvaluationRunRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetscheduledevaluationrunrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IScheduledEvaluationRun](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ischeduledevaluationrun), [protos.google.cloud.ces.v1beta.IGetScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.igetscheduledevaluationrunrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### guardrailPath(project, location, app, guardrail)
    
    
    guardrailPath(project: string, location: string, app: string, guardrail: string): string;

Return a fully-qualified guardrail resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`app` |  `string`   
  
`guardrail` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### importEvaluations(request, options)
    
    
    importEvaluations(request?: protos.google.cloud.ces.v1beta.IImportEvaluationsRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.ces.v1beta.IImportEvaluationsResponse, protos.google.cloud.ces.v1beta.IImportEvaluationsOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Imports evaluations into the app.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iimportevaluationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.ces.v1beta.IImportEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iimportevaluationsresponse), [protos.google.cloud.ces.v1beta.IImportEvaluationsOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iimportevaluationsoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The conversations to import the evaluations from.
       */
      // const conversationList = {}
      /**
       *  The Google Cloud Storage (https://cloud.google.com/storage/docs/) URI
       *  from which to import evaluations. The format of this URI must be
       *  `gs://

### importEvaluations(request, options, callback)
    
    
    importEvaluations(request: protos.google.cloud.ces.v1beta.IImportEvaluationsRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.ces.v1beta.IImportEvaluationsResponse, protos.google.cloud.ces.v1beta.IImportEvaluationsOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iimportevaluationsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.ces.v1beta.IImportEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iimportevaluationsresponse), [protos.google.cloud.ces.v1beta.IImportEvaluationsOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iimportevaluationsoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importEvaluations(request, callback)
    
    
    importEvaluations(request: protos.google.cloud.ces.v1beta.IImportEvaluationsRequest, callback: Callback<LROperation<protos.google.cloud.ces.v1beta.IImportEvaluationsResponse, protos.google.cloud.ces.v1beta.IImportEvaluationsOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iimportevaluationsrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.ces.v1beta.IImportEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iimportevaluationsresponse), [protos.google.cloud.ces.v1beta.IImportEvaluationsOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iimportevaluationsoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
  
### listEvaluationDatasets(request, options)
    
    
    listEvaluationDatasets(request?: protos.google.cloud.ces.v1beta.IListEvaluationDatasetsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IEvaluationDataset[],
            protos.google.cloud.ces.v1beta.IListEvaluationDatasetsRequest | null,
            protos.google.cloud.ces.v1beta.IListEvaluationDatasetsResponse
        ]>;

Lists all evaluation datasets in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationdatasetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IEvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationdataset)[], [protos.google.cloud.ces.v1beta.IListEvaluationDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationdatasetsrequest) | null, [protos.google.cloud.ces.v1beta.IListEvaluationDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationdatasetsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [EvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluationdataset). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listEvaluationDatasetsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listEvaluationDatasets(request, options, callback)
    
    
    listEvaluationDatasets(request: protos.google.cloud.ces.v1beta.IListEvaluationDatasetsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.ces.v1beta.IListEvaluationDatasetsRequest, protos.google.cloud.ces.v1beta.IListEvaluationDatasetsResponse | null | undefined, protos.google.cloud.ces.v1beta.IEvaluationDataset>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationdatasetsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.ces.v1beta.IListEvaluationDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationdatasetsrequest), [protos.google.cloud.ces.v1beta.IListEvaluationDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationdatasetsresponse) | null | undefined, [protos.google.cloud.ces.v1beta.IEvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationdataset)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEvaluationDatasets(request, callback)
    
    
    listEvaluationDatasets(request: protos.google.cloud.ces.v1beta.IListEvaluationDatasetsRequest, callback: PaginationCallback<protos.google.cloud.ces.v1beta.IListEvaluationDatasetsRequest, protos.google.cloud.ces.v1beta.IListEvaluationDatasetsResponse | null | undefined, protos.google.cloud.ces.v1beta.IEvaluationDataset>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationdatasetsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.ces.v1beta.IListEvaluationDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationdatasetsrequest), [protos.google.cloud.ces.v1beta.IListEvaluationDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationdatasetsresponse) | null | undefined, [protos.google.cloud.ces.v1beta.IEvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationdataset)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEvaluationDatasetsAsync(request, options)
    
    
    listEvaluationDatasetsAsync(request?: protos.google.cloud.ces.v1beta.IListEvaluationDatasetsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.ces.v1beta.IEvaluationDataset>;

Equivalent to `listEvaluationDatasets`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationdatasetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.ces.v1beta.IEvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationdataset)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [EvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluationdataset). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the app to list evaluation datasets from.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. The
       *  next_page_token google.cloud.ces.v1beta.ListEvaluationDatasetsResponse.next_page_token 
       *  value returned from a previous list
       *  EvaluationService.ListEvaluationDatasets google.cloud.ces.v1beta.EvaluationService.ListEvaluationDatasets 
       *  call.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filter to be applied when listing the evaluation datasets.
       *  See https://google.aip.dev/160 for more details.
       */
      // const filter = 'abc123'
      /**
       *  Optional. Field to sort by. Only "name" and "create_time", and
       *  "update_time" are supported. Time fields are ordered in descending order,
       *  and the name field is ordered in ascending order. If not included,
       *  "update_time" will be the default. See https://google.aip.dev/132#ordering
       *  for more details.
       */
      // const orderBy = 'abc123'
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callListEvaluationDatasets() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = cesClient.[listEvaluationDatasetsAsync](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListEvaluationDatasets();
    
    

### listEvaluationDatasetsStream(request, options)
    
    
    listEvaluationDatasetsStream(request?: protos.google.cloud.ces.v1beta.IListEvaluationDatasetsRequest, options?: CallOptions): Transform;

Equivalent to `listEvaluationDatasets`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationdatasetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [EvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluationdataset) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listEvaluationDatasetsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listEvaluationExpectations(request, options)
    
    
    listEvaluationExpectations(request?: protos.google.cloud.ces.v1beta.IListEvaluationExpectationsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IEvaluationExpectation[],
            protos.google.cloud.ces.v1beta.IListEvaluationExpectationsRequest | null,
            protos.google.cloud.ces.v1beta.IListEvaluationExpectationsResponse
        ]>;

Lists all evaluation expectations in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationExpectationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationexpectationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IEvaluationExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationexpectation)[], [protos.google.cloud.ces.v1beta.IListEvaluationExpectationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationexpectationsrequest) | null, [protos.google.cloud.ces.v1beta.IListEvaluationExpectationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationexpectationsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listEvaluationExpectationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listEvaluationExpectations(request, options, callback)
    
    
    listEvaluationExpectations(request: protos.google.cloud.ces.v1beta.IListEvaluationExpectationsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.ces.v1beta.IListEvaluationExpectationsRequest, protos.google.cloud.ces.v1beta.IListEvaluationExpectationsResponse | null | undefined, protos.google.cloud.ces.v1beta.IEvaluationExpectation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationExpectationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationexpectationsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.ces.v1beta.IListEvaluationExpectationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationexpectationsrequest), [protos.google.cloud.ces.v1beta.IListEvaluationExpectationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationexpectationsresponse) | null | undefined, [protos.google.cloud.ces.v1beta.IEvaluationExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationexpectation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEvaluationExpectations(request, callback)
    
    
    listEvaluationExpectations(request: protos.google.cloud.ces.v1beta.IListEvaluationExpectationsRequest, callback: PaginationCallback<protos.google.cloud.ces.v1beta.IListEvaluationExpectationsRequest, protos.google.cloud.ces.v1beta.IListEvaluationExpectationsResponse | null | undefined, protos.google.cloud.ces.v1beta.IEvaluationExpectation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationExpectationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationexpectationsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.ces.v1beta.IListEvaluationExpectationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationexpectationsrequest), [protos.google.cloud.ces.v1beta.IListEvaluationExpectationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationexpectationsresponse) | null | undefined, [protos.google.cloud.ces.v1beta.IEvaluationExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationexpectation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEvaluationExpectationsAsync(request, options)
    
    
    listEvaluationExpectationsAsync(request?: protos.google.cloud.ces.v1beta.IListEvaluationExpectationsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.ces.v1beta.IEvaluationExpectation>;

Equivalent to `listEvaluationExpectations`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationExpectationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationexpectationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.ces.v1beta.IEvaluationExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationexpectation)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the app to list evaluation expectations
       *  from.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. The
       *  next_page_token google.cloud.ces.v1beta.ListEvaluationExpectationsResponse.next_page_token 
       *  value returned from a previous list
       *  EvaluationService.ListEvaluationExpectations google.cloud.ces.v1beta.EvaluationService.ListEvaluationExpectations 
       *  call.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filter to be applied when listing the evaluation expectations.
       *  See https://google.aip.dev/160 for more details.
       */
      // const filter = 'abc123'
      /**
       *  Optional. Field to sort by. Only "name" and "create_time", and
       *  "update_time" are supported. Time fields are ordered in descending order,
       *  and the name field is ordered in ascending order. If not included,
       *  "update_time" will be the default. See https://google.aip.dev/132#ordering
       *  for more details.
       */
      // const orderBy = 'abc123'
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callListEvaluationExpectations() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = cesClient.[listEvaluationExpectationsAsync](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListEvaluationExpectations();
    
    

### listEvaluationExpectationsStream(request, options)
    
    
    listEvaluationExpectationsStream(request?: protos.google.cloud.ces.v1beta.IListEvaluationExpectationsRequest, options?: CallOptions): Transform;

Equivalent to `listEvaluationExpectations`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationExpectationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationexpectationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listEvaluationExpectationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listEvaluationResults(request, options)
    
    
    listEvaluationResults(request?: protos.google.cloud.ces.v1beta.IListEvaluationResultsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IEvaluationResult[],
            protos.google.cloud.ces.v1beta.IListEvaluationResultsRequest | null,
            protos.google.cloud.ces.v1beta.IListEvaluationResultsResponse
        ]>;

Lists all evaluation results for a given evaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationresultsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IEvaluationResult](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationresult)[], [protos.google.cloud.ces.v1beta.IListEvaluationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationresultsrequest) | null, [protos.google.cloud.ces.v1beta.IListEvaluationResultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationresultsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listEvaluationResultsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listEvaluationResults(request, options, callback)
    
    
    listEvaluationResults(request: protos.google.cloud.ces.v1beta.IListEvaluationResultsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.ces.v1beta.IListEvaluationResultsRequest, protos.google.cloud.ces.v1beta.IListEvaluationResultsResponse | null | undefined, protos.google.cloud.ces.v1beta.IEvaluationResult>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationresultsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.ces.v1beta.IListEvaluationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationresultsrequest), [protos.google.cloud.ces.v1beta.IListEvaluationResultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationresultsresponse) | null | undefined, [protos.google.cloud.ces.v1beta.IEvaluationResult](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationresult)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEvaluationResults(request, callback)
    
    
    listEvaluationResults(request: protos.google.cloud.ces.v1beta.IListEvaluationResultsRequest, callback: PaginationCallback<protos.google.cloud.ces.v1beta.IListEvaluationResultsRequest, protos.google.cloud.ces.v1beta.IListEvaluationResultsResponse | null | undefined, protos.google.cloud.ces.v1beta.IEvaluationResult>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationresultsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.ces.v1beta.IListEvaluationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationresultsrequest), [protos.google.cloud.ces.v1beta.IListEvaluationResultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationresultsresponse) | null | undefined, [protos.google.cloud.ces.v1beta.IEvaluationResult](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationresult)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEvaluationResultsAsync(request, options)
    
    
    listEvaluationResultsAsync(request?: protos.google.cloud.ces.v1beta.IListEvaluationResultsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.ces.v1beta.IEvaluationResult>;

Equivalent to `listEvaluationResults`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationresultsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.ces.v1beta.IEvaluationResult](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationresult)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the evaluation to list evaluation results
       *  from. To filter by evaluation run, use `-` as the evaluation ID and specify
       *  the evaluation run ID in the filter. For example:
       *  `projects/{project}/locations/{location}/apps/{app}/evaluations/-`
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. The
       *  next_page_token google.cloud.ces.v1beta.ListEvaluationResultsResponse.next_page_token 
       *  value returned from a previous list
       *  EvaluationService.ListEvaluationResults google.cloud.ces.v1beta.EvaluationService.ListEvaluationResults 
       *  call.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filter to be applied when listing the evaluation results.
       *  See https://google.aip.dev/160 for more details.
       */
      // const filter = 'abc123'
      /**
       *  Optional. Field to sort by. Only "name" and "create_time", and
       *  "update_time" are supported. Time fields are ordered in descending order,
       *  and the name field is ordered in ascending order. If not included,
       *  "update_time" will be the default. See https://google.aip.dev/132#ordering
       *  for more details.
       */
      // const orderBy = 'abc123'
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callListEvaluationResults() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = cesClient.[listEvaluationResultsAsync](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListEvaluationResults();
    
    

### listEvaluationResultsStream(request, options)
    
    
    listEvaluationResultsStream(request?: protos.google.cloud.ces.v1beta.IListEvaluationResultsRequest, options?: CallOptions): Transform;

Equivalent to `listEvaluationResults`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationresultsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listEvaluationResultsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listEvaluationRuns(request, options)
    
    
    listEvaluationRuns(request?: protos.google.cloud.ces.v1beta.IListEvaluationRunsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IEvaluationRun[],
            protos.google.cloud.ces.v1beta.IListEvaluationRunsRequest | null,
            protos.google.cloud.ces.v1beta.IListEvaluationRunsResponse
        ]>;

Lists all evaluation runs in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationrunsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IEvaluationRun](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationrun)[], [protos.google.cloud.ces.v1beta.IListEvaluationRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationrunsrequest) | null, [protos.google.cloud.ces.v1beta.IListEvaluationRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationrunsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listEvaluationRunsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listEvaluationRuns(request, options, callback)
    
    
    listEvaluationRuns(request: protos.google.cloud.ces.v1beta.IListEvaluationRunsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.ces.v1beta.IListEvaluationRunsRequest, protos.google.cloud.ces.v1beta.IListEvaluationRunsResponse | null | undefined, protos.google.cloud.ces.v1beta.IEvaluationRun>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationrunsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.ces.v1beta.IListEvaluationRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationrunsrequest), [protos.google.cloud.ces.v1beta.IListEvaluationRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationrunsresponse) | null | undefined, [protos.google.cloud.ces.v1beta.IEvaluationRun](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationrun)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEvaluationRuns(request, callback)
    
    
    listEvaluationRuns(request: protos.google.cloud.ces.v1beta.IListEvaluationRunsRequest, callback: PaginationCallback<protos.google.cloud.ces.v1beta.IListEvaluationRunsRequest, protos.google.cloud.ces.v1beta.IListEvaluationRunsResponse | null | undefined, protos.google.cloud.ces.v1beta.IEvaluationRun>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationrunsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.ces.v1beta.IListEvaluationRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationrunsrequest), [protos.google.cloud.ces.v1beta.IListEvaluationRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationrunsresponse) | null | undefined, [protos.google.cloud.ces.v1beta.IEvaluationRun](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationrun)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEvaluationRunsAsync(request, options)
    
    
    listEvaluationRunsAsync(request?: protos.google.cloud.ces.v1beta.IListEvaluationRunsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.ces.v1beta.IEvaluationRun>;

Equivalent to `listEvaluationRuns`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationrunsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.ces.v1beta.IEvaluationRun](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationrun)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the app to list evaluation runs from.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. The
       *  next_page_token google.cloud.ces.v1beta.ListEvaluationRunsResponse.next_page_token 
       *  value returned from a previous list
       *  EvaluationService.ListEvaluationRuns google.cloud.ces.v1beta.EvaluationService.ListEvaluationRuns 
       *  call.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filter to be applied when listing the evaluation runs.
       *  See https://google.aip.dev/160 for more details.
       */
      // const filter = 'abc123'
      /**
       *  Optional. Field to sort by. Only "name" and "create_time", and
       *  "update_time" are supported. Time fields are ordered in descending order,
       *  and the name field is ordered in ascending order. If not included,
       *  "update_time" will be the default. See https://google.aip.dev/132#ordering
       *  for more details.
       */
      // const orderBy = 'abc123'
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callListEvaluationRuns() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = cesClient.[listEvaluationRunsAsync](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListEvaluationRuns();
    
    

### listEvaluationRunsStream(request, options)
    
    
    listEvaluationRunsStream(request?: protos.google.cloud.ces.v1beta.IListEvaluationRunsRequest, options?: CallOptions): Transform;

Equivalent to `listEvaluationRuns`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationrunsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listEvaluationRunsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listEvaluations(request, options)
    
    
    listEvaluations(request?: protos.google.cloud.ces.v1beta.IListEvaluationsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IEvaluation[],
            protos.google.cloud.ces.v1beta.IListEvaluationsRequest | null,
            protos.google.cloud.ces.v1beta.IListEvaluationsResponse
        ]>;

Lists all evaluations in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluation)[], [protos.google.cloud.ces.v1beta.IListEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationsrequest) | null, [protos.google.cloud.ces.v1beta.IListEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listEvaluationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listEvaluations(request, options, callback)
    
    
    listEvaluations(request: protos.google.cloud.ces.v1beta.IListEvaluationsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.ces.v1beta.IListEvaluationsRequest, protos.google.cloud.ces.v1beta.IListEvaluationsResponse | null | undefined, protos.google.cloud.ces.v1beta.IEvaluation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.ces.v1beta.IListEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationsrequest), [protos.google.cloud.ces.v1beta.IListEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationsresponse) | null | undefined, [protos.google.cloud.ces.v1beta.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEvaluations(request, callback)
    
    
    listEvaluations(request: protos.google.cloud.ces.v1beta.IListEvaluationsRequest, callback: PaginationCallback<protos.google.cloud.ces.v1beta.IListEvaluationsRequest, protos.google.cloud.ces.v1beta.IListEvaluationsResponse | null | undefined, protos.google.cloud.ces.v1beta.IEvaluation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.ces.v1beta.IListEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationsrequest), [protos.google.cloud.ces.v1beta.IListEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationsresponse) | null | undefined, [protos.google.cloud.ces.v1beta.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEvaluationsAsync(request, options)
    
    
    listEvaluationsAsync(request?: protos.google.cloud.ces.v1beta.IListEvaluationsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.ces.v1beta.IEvaluation>;

Equivalent to `listEvaluations`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.ces.v1beta.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluation)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the app to list evaluations from.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. The
       *  next_page_token google.cloud.ces.v1beta.ListEvaluationsResponse.next_page_token 
       *  value returned from a previous list
       *  EvaluationService.ListEvaluations google.cloud.ces.v1beta.EvaluationService.ListEvaluations 
       *  call.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filter to be applied on the evaluation when listing the
       *  evaluations. See https://google.aip.dev/160 for more details. Supported
       *  fields: evaluation_datasets
       */
      // const evaluationFilter = 'abc123'
      /**
       *  Optional. Filter string for fields on the associated EvaluationRun
       *  resources. See https://google.aip.dev/160 for more details. Supported
       *  fields: create_time, initiated_by, app_version_display_name
       */
      // const evaluationRunFilter = 'abc123'
      /**
       *  Optional. Field to sort by. Only "name" and "create_time", and
       *  "update_time" are supported. Time fields are ordered in descending order,
       *  and the name field is ordered in ascending order. If not included,
       *  "update_time" will be the default. See https://google.aip.dev/132#ordering
       *  for more details.
       */
      // const orderBy = 'abc123'
      /**
       *  Optional. Whether to include the last 10 evaluation results for each
       *  evaluation in the response.
       */
      // const lastTenResults = true
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callListEvaluations() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = cesClient.[listEvaluationsAsync](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListEvaluations();
    
    

### listEvaluationsStream(request, options)
    
    
    listEvaluationsStream(request?: protos.google.cloud.ces.v1beta.IListEvaluationsRequest, options?: CallOptions): Transform;

Equivalent to `listEvaluations`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistevaluationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listEvaluationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
**Example**
    
    
    const client = longrunning.operationsClient();
    for await (const response of client.listOperationsAsync(request));
    // doThingsWith(response)
    

### listScheduledEvaluationRuns(request, options)
    
    
    listScheduledEvaluationRuns(request?: protos.google.cloud.ces.v1beta.IListScheduledEvaluationRunsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IScheduledEvaluationRun[],
            protos.google.cloud.ces.v1beta.IListScheduledEvaluationRunsRequest | null,
            protos.google.cloud.ces.v1beta.IListScheduledEvaluationRunsResponse
        ]>;

Lists all scheduled evaluation runs in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListScheduledEvaluationRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistscheduledevaluationrunsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IScheduledEvaluationRun](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ischeduledevaluationrun)[], [protos.google.cloud.ces.v1beta.IListScheduledEvaluationRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistscheduledevaluationrunsrequest) | null, [protos.google.cloud.ces.v1beta.IListScheduledEvaluationRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistscheduledevaluationrunsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listScheduledEvaluationRunsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listScheduledEvaluationRuns(request, options, callback)
    
    
    listScheduledEvaluationRuns(request: protos.google.cloud.ces.v1beta.IListScheduledEvaluationRunsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.ces.v1beta.IListScheduledEvaluationRunsRequest, protos.google.cloud.ces.v1beta.IListScheduledEvaluationRunsResponse | null | undefined, protos.google.cloud.ces.v1beta.IScheduledEvaluationRun>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListScheduledEvaluationRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistscheduledevaluationrunsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.ces.v1beta.IListScheduledEvaluationRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistscheduledevaluationrunsrequest), [protos.google.cloud.ces.v1beta.IListScheduledEvaluationRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistscheduledevaluationrunsresponse) | null | undefined, [protos.google.cloud.ces.v1beta.IScheduledEvaluationRun](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ischeduledevaluationrun)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listScheduledEvaluationRuns(request, callback)
    
    
    listScheduledEvaluationRuns(request: protos.google.cloud.ces.v1beta.IListScheduledEvaluationRunsRequest, callback: PaginationCallback<protos.google.cloud.ces.v1beta.IListScheduledEvaluationRunsRequest, protos.google.cloud.ces.v1beta.IListScheduledEvaluationRunsResponse | null | undefined, protos.google.cloud.ces.v1beta.IScheduledEvaluationRun>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListScheduledEvaluationRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistscheduledevaluationrunsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.ces.v1beta.IListScheduledEvaluationRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistscheduledevaluationrunsrequest), [protos.google.cloud.ces.v1beta.IListScheduledEvaluationRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistscheduledevaluationrunsresponse) | null | undefined, [protos.google.cloud.ces.v1beta.IScheduledEvaluationRun](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ischeduledevaluationrun)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listScheduledEvaluationRunsAsync(request, options)
    
    
    listScheduledEvaluationRunsAsync(request?: protos.google.cloud.ces.v1beta.IListScheduledEvaluationRunsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.ces.v1beta.IScheduledEvaluationRun>;

Equivalent to `listScheduledEvaluationRuns`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListScheduledEvaluationRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistscheduledevaluationrunsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.ces.v1beta.IScheduledEvaluationRun](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ischeduledevaluationrun)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the app to list scheduled evaluation runs
       *  from.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. The
       *  next_page_token google.cloud.ces.v1beta.ListScheduledEvaluationRunsResponse.next_page_token 
       *  value returned from a previous list
       *  EvaluationService.ListScheduledEvaluationRuns google.cloud.ces.v1beta.EvaluationService.ListScheduledEvaluationRuns 
       *  call.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filter to be applied when listing the scheduled evaluation runs.
       *  See https://google.aip.dev/160 for more details.
       *  Currently supports filtering by:
       *  * request.evaluations:evaluation_id
       *  * request.evaluation_dataset:evaluation_dataset_id
       */
      // const filter = 'abc123'
      /**
       *  Optional. Field to sort by. Supported fields are:
       *  "name" (ascending), "create_time" (descending), "update_time" (descending),
       *  "next_scheduled_execution" (ascending), and
       *  "last_completed_run.create_time" (descending).
       *  If not included, "update_time" will be the default.
       *  See https://google.aip.dev/132#ordering for more details.
       */
      // const orderBy = 'abc123'
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callListScheduledEvaluationRuns() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = cesClient.[listScheduledEvaluationRunsAsync](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListScheduledEvaluationRuns();
    
    

### listScheduledEvaluationRunsStream(request, options)
    
    
    listScheduledEvaluationRunsStream(request?: protos.google.cloud.ces.v1beta.IListScheduledEvaluationRunsRequest, options?: CallOptions): Transform;

Equivalent to `listScheduledEvaluationRuns`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListScheduledEvaluationRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ilistscheduledevaluationrunsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listScheduledEvaluationRunsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### matchAppFromAgentName(agentName)
    
    
    matchAppFromAgentName(agentName: string): string | number;

Parse the app from Agent resource.

**Parameter**  
---  
**Name** | **Description**  
`agentName` |  `string`   
A fully-qualified path representing Agent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the app.  
  
### matchAppFromAppName(appName)
    
    
    matchAppFromAppName(appName: string): string | number;

Parse the app from App resource.

**Parameter**  
---  
**Name** | **Description**  
`appName` |  `string`   
A fully-qualified path representing App resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the app.  
  
### matchAppFromAppVersionName(appVersionName)
    
    
    matchAppFromAppVersionName(appVersionName: string): string | number;

Parse the app from AppVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`appVersionName` |  `string`   
A fully-qualified path representing AppVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the app.  
  
### matchAppFromChangelogName(changelogName)
    
    
    matchAppFromChangelogName(changelogName: string): string | number;

Parse the app from Changelog resource.

**Parameter**  
---  
**Name** | **Description**  
`changelogName` |  `string`   
A fully-qualified path representing Changelog resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the app.  
  
### matchAppFromConversationName(conversationName)
    
    
    matchAppFromConversationName(conversationName: string): string | number;

Parse the app from Conversation resource.

**Parameter**  
---  
**Name** | **Description**  
`conversationName` |  `string`   
A fully-qualified path representing Conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the app.  
  
### matchAppFromDeploymentName(deploymentName)
    
    
    matchAppFromDeploymentName(deploymentName: string): string | number;

Parse the app from Deployment resource.

**Parameter**  
---  
**Name** | **Description**  
`deploymentName` |  `string`   
A fully-qualified path representing Deployment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the app.  
  
### matchAppFromEvaluationDatasetName(evaluationDatasetName)
    
    
    matchAppFromEvaluationDatasetName(evaluationDatasetName: string): string | number;

Parse the app from EvaluationDataset resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationDatasetName` |  `string`   
A fully-qualified path representing EvaluationDataset resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the app.  
  
### matchAppFromEvaluationExpectationName(evaluationExpectationName)
    
    
    matchAppFromEvaluationExpectationName(evaluationExpectationName: string): string | number;

Parse the app from EvaluationExpectation resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationExpectationName` |  `string`   
A fully-qualified path representing EvaluationExpectation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the app.  
  
### matchAppFromEvaluationName(evaluationName)
    
    
    matchAppFromEvaluationName(evaluationName: string): string | number;

Parse the app from Evaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationName` |  `string`   
A fully-qualified path representing Evaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the app.  
  
### matchAppFromEvaluationResultName(evaluationResultName)
    
    
    matchAppFromEvaluationResultName(evaluationResultName: string): string | number;

Parse the app from EvaluationResult resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationResultName` |  `string`   
A fully-qualified path representing EvaluationResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the app.  
  
### matchAppFromEvaluationRunName(evaluationRunName)
    
    
    matchAppFromEvaluationRunName(evaluationRunName: string): string | number;

Parse the app from EvaluationRun resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationRunName` |  `string`   
A fully-qualified path representing EvaluationRun resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the app.  
  
### matchAppFromExampleName(exampleName)
    
    
    matchAppFromExampleName(exampleName: string): string | number;

Parse the app from Example resource.

**Parameter**  
---  
**Name** | **Description**  
`exampleName` |  `string`   
A fully-qualified path representing Example resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the app.  
  
### matchAppFromGuardrailName(guardrailName)
    
    
    matchAppFromGuardrailName(guardrailName: string): string | number;

Parse the app from Guardrail resource.

**Parameter**  
---  
**Name** | **Description**  
`guardrailName` |  `string`   
A fully-qualified path representing Guardrail resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the app.  
  
### matchAppFromScheduledEvaluationRunName(scheduledEvaluationRunName)
    
    
    matchAppFromScheduledEvaluationRunName(scheduledEvaluationRunName: string): string | number;

Parse the app from ScheduledEvaluationRun resource.

**Parameter**  
---  
**Name** | **Description**  
`scheduledEvaluationRunName` |  `string`   
A fully-qualified path representing ScheduledEvaluationRun resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the app.  
  
### matchAppFromToolName(toolName)
    
    
    matchAppFromToolName(toolName: string): string | number;

Parse the app from Tool resource.

**Parameter**  
---  
**Name** | **Description**  
`toolName` |  `string`   
A fully-qualified path representing Tool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the app.  
  
### matchAppFromToolsetName(toolsetName)
    
    
    matchAppFromToolsetName(toolsetName: string): string | number;

Parse the app from Toolset resource.

**Parameter**  
---  
**Name** | **Description**  
`toolsetName` |  `string`   
A fully-qualified path representing Toolset resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the app.  
  
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
  
### matchEvaluationDatasetFromEvaluationDatasetName(evaluationDatasetName)
    
    
    matchEvaluationDatasetFromEvaluationDatasetName(evaluationDatasetName: string): string | number;

Parse the evaluation_dataset from EvaluationDataset resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationDatasetName` |  `string`   
A fully-qualified path representing EvaluationDataset resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the evaluation_dataset.  
  
### matchEvaluationExpectationFromEvaluationExpectationName(evaluationExpectationName)
    
    
    matchEvaluationExpectationFromEvaluationExpectationName(evaluationExpectationName: string): string | number;

Parse the evaluation_expectation from EvaluationExpectation resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationExpectationName` |  `string`   
A fully-qualified path representing EvaluationExpectation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the evaluation_expectation.  
  
### matchEvaluationFromEvaluationName(evaluationName)
    
    
    matchEvaluationFromEvaluationName(evaluationName: string): string | number;

Parse the evaluation from Evaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationName` |  `string`   
A fully-qualified path representing Evaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the evaluation.  
  
### matchEvaluationFromEvaluationResultName(evaluationResultName)
    
    
    matchEvaluationFromEvaluationResultName(evaluationResultName: string): string | number;

Parse the evaluation from EvaluationResult resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationResultName` |  `string`   
A fully-qualified path representing EvaluationResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the evaluation.  
  
### matchEvaluationResultFromEvaluationResultName(evaluationResultName)
    
    
    matchEvaluationResultFromEvaluationResultName(evaluationResultName: string): string | number;

Parse the evaluation_result from EvaluationResult resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationResultName` |  `string`   
A fully-qualified path representing EvaluationResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the evaluation_result.  
  
### matchEvaluationRunFromEvaluationRunName(evaluationRunName)
    
    
    matchEvaluationRunFromEvaluationRunName(evaluationRunName: string): string | number;

Parse the evaluation_run from EvaluationRun resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationRunName` |  `string`   
A fully-qualified path representing EvaluationRun resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the evaluation_run.  
  
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
  
### matchGuardrailFromGuardrailName(guardrailName)
    
    
    matchGuardrailFromGuardrailName(guardrailName: string): string | number;

Parse the guardrail from Guardrail resource.

**Parameter**  
---  
**Name** | **Description**  
`guardrailName` |  `string`   
A fully-qualified path representing Guardrail resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the guardrail.  
  
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
  
### matchLocationFromAppName(appName)
    
    
    matchLocationFromAppName(appName: string): string | number;

Parse the location from App resource.

**Parameter**  
---  
**Name** | **Description**  
`appName` |  `string`   
A fully-qualified path representing App resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromAppVersionName(appVersionName)
    
    
    matchLocationFromAppVersionName(appVersionName: string): string | number;

Parse the location from AppVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`appVersionName` |  `string`   
A fully-qualified path representing AppVersion resource.  
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
  
### matchLocationFromEvaluationDatasetName(evaluationDatasetName)
    
    
    matchLocationFromEvaluationDatasetName(evaluationDatasetName: string): string | number;

Parse the location from EvaluationDataset resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationDatasetName` |  `string`   
A fully-qualified path representing EvaluationDataset resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromEvaluationExpectationName(evaluationExpectationName)
    
    
    matchLocationFromEvaluationExpectationName(evaluationExpectationName: string): string | number;

Parse the location from EvaluationExpectation resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationExpectationName` |  `string`   
A fully-qualified path representing EvaluationExpectation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromEvaluationName(evaluationName)
    
    
    matchLocationFromEvaluationName(evaluationName: string): string | number;

Parse the location from Evaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationName` |  `string`   
A fully-qualified path representing Evaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromEvaluationResultName(evaluationResultName)
    
    
    matchLocationFromEvaluationResultName(evaluationResultName: string): string | number;

Parse the location from EvaluationResult resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationResultName` |  `string`   
A fully-qualified path representing EvaluationResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromEvaluationRunName(evaluationRunName)
    
    
    matchLocationFromEvaluationRunName(evaluationRunName: string): string | number;

Parse the location from EvaluationRun resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationRunName` |  `string`   
A fully-qualified path representing EvaluationRun resource.  
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
  
### matchLocationFromGuardrailName(guardrailName)
    
    
    matchLocationFromGuardrailName(guardrailName: string): string | number;

Parse the location from Guardrail resource.

**Parameter**  
---  
**Name** | **Description**  
`guardrailName` |  `string`   
A fully-qualified path representing Guardrail resource.  
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
  
### matchLocationFromOmnichannelName(omnichannelName)
    
    
    matchLocationFromOmnichannelName(omnichannelName: string): string | number;

Parse the location from Omnichannel resource.

**Parameter**  
---  
**Name** | **Description**  
`omnichannelName` |  `string`   
A fully-qualified path representing Omnichannel resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromScheduledEvaluationRunName(scheduledEvaluationRunName)
    
    
    matchLocationFromScheduledEvaluationRunName(scheduledEvaluationRunName: string): string | number;

Parse the location from ScheduledEvaluationRun resource.

**Parameter**  
---  
**Name** | **Description**  
`scheduledEvaluationRunName` |  `string`   
A fully-qualified path representing ScheduledEvaluationRun resource.  
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
  
### matchLocationFromToolsetName(toolsetName)
    
    
    matchLocationFromToolsetName(toolsetName: string): string | number;

Parse the location from Toolset resource.

**Parameter**  
---  
**Name** | **Description**  
`toolsetName` |  `string`   
A fully-qualified path representing Toolset resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchOmnichannelFromOmnichannelName(omnichannelName)
    
    
    matchOmnichannelFromOmnichannelName(omnichannelName: string): string | number;

Parse the omnichannel from Omnichannel resource.

**Parameter**  
---  
**Name** | **Description**  
`omnichannelName` |  `string`   
A fully-qualified path representing Omnichannel resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the omnichannel.  
  
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
  
### matchProjectFromAppName(appName)
    
    
    matchProjectFromAppName(appName: string): string | number;

Parse the project from App resource.

**Parameter**  
---  
**Name** | **Description**  
`appName` |  `string`   
A fully-qualified path representing App resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromAppVersionName(appVersionName)
    
    
    matchProjectFromAppVersionName(appVersionName: string): string | number;

Parse the project from AppVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`appVersionName` |  `string`   
A fully-qualified path representing AppVersion resource.  
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
  
### matchProjectFromEvaluationDatasetName(evaluationDatasetName)
    
    
    matchProjectFromEvaluationDatasetName(evaluationDatasetName: string): string | number;

Parse the project from EvaluationDataset resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationDatasetName` |  `string`   
A fully-qualified path representing EvaluationDataset resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromEvaluationExpectationName(evaluationExpectationName)
    
    
    matchProjectFromEvaluationExpectationName(evaluationExpectationName: string): string | number;

Parse the project from EvaluationExpectation resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationExpectationName` |  `string`   
A fully-qualified path representing EvaluationExpectation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromEvaluationName(evaluationName)
    
    
    matchProjectFromEvaluationName(evaluationName: string): string | number;

Parse the project from Evaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationName` |  `string`   
A fully-qualified path representing Evaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromEvaluationResultName(evaluationResultName)
    
    
    matchProjectFromEvaluationResultName(evaluationResultName: string): string | number;

Parse the project from EvaluationResult resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationResultName` |  `string`   
A fully-qualified path representing EvaluationResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromEvaluationRunName(evaluationRunName)
    
    
    matchProjectFromEvaluationRunName(evaluationRunName: string): string | number;

Parse the project from EvaluationRun resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationRunName` |  `string`   
A fully-qualified path representing EvaluationRun resource.  
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
  
### matchProjectFromGuardrailName(guardrailName)
    
    
    matchProjectFromGuardrailName(guardrailName: string): string | number;

Parse the project from Guardrail resource.

**Parameter**  
---  
**Name** | **Description**  
`guardrailName` |  `string`   
A fully-qualified path representing Guardrail resource.  
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
  
### matchProjectFromOmnichannelName(omnichannelName)
    
    
    matchProjectFromOmnichannelName(omnichannelName: string): string | number;

Parse the project from Omnichannel resource.

**Parameter**  
---  
**Name** | **Description**  
`omnichannelName` |  `string`   
A fully-qualified path representing Omnichannel resource.  
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
  
### matchProjectFromScheduledEvaluationRunName(scheduledEvaluationRunName)
    
    
    matchProjectFromScheduledEvaluationRunName(scheduledEvaluationRunName: string): string | number;

Parse the project from ScheduledEvaluationRun resource.

**Parameter**  
---  
**Name** | **Description**  
`scheduledEvaluationRunName` |  `string`   
A fully-qualified path representing ScheduledEvaluationRun resource.  
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
  
### matchProjectFromToolsetName(toolsetName)
    
    
    matchProjectFromToolsetName(toolsetName: string): string | number;

Parse the project from Toolset resource.

**Parameter**  
---  
**Name** | **Description**  
`toolsetName` |  `string`   
A fully-qualified path representing Toolset resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchScheduledEvaluationRunFromScheduledEvaluationRunName(scheduledEvaluationRunName)
    
    
    matchScheduledEvaluationRunFromScheduledEvaluationRunName(scheduledEvaluationRunName: string): string | number;

Parse the scheduled_evaluation_run from ScheduledEvaluationRun resource.

**Parameter**  
---  
**Name** | **Description**  
`scheduledEvaluationRunName` |  `string`   
A fully-qualified path representing ScheduledEvaluationRun resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the scheduled_evaluation_run.  
  
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
  
### matchToolsetFromToolsetName(toolsetName)
    
    
    matchToolsetFromToolsetName(toolsetName: string): string | number;

Parse the toolset from Toolset resource.

**Parameter**  
---  
**Name** | **Description**  
`toolsetName` |  `string`   
A fully-qualified path representing Toolset resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the toolset.  
  
### matchVersionFromAppVersionName(appVersionName)
    
    
    matchVersionFromAppVersionName(appVersionName: string): string | number;

Parse the version from AppVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`appVersionName` |  `string`   
A fully-qualified path representing AppVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the version.  
  
### omnichannelPath(project, location, omnichannel)
    
    
    omnichannelPath(project: string, location: string, omnichannel: string): string;

Return a fully-qualified omnichannel resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`omnichannel` |  `string`   
  
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
  
### runEvaluation(request, options)
    
    
    runEvaluation(request?: protos.google.cloud.ces.v1beta.IRunEvaluationRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.ces.v1beta.IRunEvaluationResponse, protos.google.cloud.ces.v1beta.IRunEvaluationOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Runs an evaluation of the app.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunevaluationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.ces.v1beta.IRunEvaluationResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunevaluationresponse), [protos.google.cloud.ces.v1beta.IRunEvaluationOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunevaluationoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The app to evaluate.
       *  Format:
       *  `projects/{project}/locations/{location}/apps/{app}`
       */
      // const app = 'abc123'
      /**
       *  Optional. List of evaluations to run.
       *  Format:
       *  `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}`
       */
      // const evaluations = ['abc','def']
      /**
       *  Optional. An evaluation dataset to run.
       *  Format:
       *  `projects/{project}/locations/{location}/apps/{app}/evaluationDatasets/{evaluationDataset}`
       */
      // const evaluationDataset = 'abc123'
      /**
       *  Optional. The display name of the evaluation run.
       */
      // const displayName = 'abc123'
      /**
       *  Optional. The app version to evaluate.
       *  Format:
       *  `projects/{project}/locations/{location}/apps/{app}/versions/{version}`
       */
      // const appVersion = 'abc123'
      /**
       *  Optional. The configuration to use for the run.
       */
      // const config = {}
      /**
       *  Optional. The number of times to run the evaluation. If not set, the
       *  default value is 1 per golden, and 5 per scenario.
       */
      // const runCount = 1234
      /**
       *  Optional. The configuration to use for the run per persona.
       */
      // const personaRunConfigs = [1,2,3,4]
      /**
       *  Optional. Configuration for running the optimization step after the
       *  evaluation run. If not set, the optimization step will not be run.
       */
      // const optimizationConfig = {}
      /**
       *  Optional. The resource name of the `ScheduledEvaluationRun` that is
       *  triggering this evaluation run.
       *  If this field is set, the `scheduled_evaluation_run` field on the created
       *  `EvaluationRun` resource will be populated from this value.
       *  Format:
       *  `projects/{project}/locations/{location}/apps/{app}/scheduledEvaluationRuns/{scheduled_evaluation_run}`
       */
      // const scheduledEvaluationRun = 'abc123'
      /**
       *  Optional. The method to run the evaluation if it is a golden evaluation. If
       *  not set, default to STABLE.
       */
      // const goldenRunMethod = {}
      /**
       *  Optional. Whether to generate a latency report for the evaluation run.
       */
      // const generateLatencyReport = true
      /**
       *  Optional. The caching settings to use for the evaluation run.
       */
      // const evaluationRunCachingSettings = {}
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callRunEvaluation() {
        // Construct request
        const request = {
          app,
        };
    
        // Run request
        const [operation] = await cesClient.runEvaluation(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callRunEvaluation();
    
    

### runEvaluation(request, options, callback)
    
    
    runEvaluation(request: protos.google.cloud.ces.v1beta.IRunEvaluationRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.ces.v1beta.IRunEvaluationResponse, protos.google.cloud.ces.v1beta.IRunEvaluationOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunevaluationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.ces.v1beta.IRunEvaluationResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunevaluationresponse), [protos.google.cloud.ces.v1beta.IRunEvaluationOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunevaluationoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### runEvaluation(request, callback)
    
    
    runEvaluation(request: protos.google.cloud.ces.v1beta.IRunEvaluationRequest, callback: Callback<LROperation<protos.google.cloud.ces.v1beta.IRunEvaluationResponse, protos.google.cloud.ces.v1beta.IRunEvaluationOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunevaluationrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.ces.v1beta.IRunEvaluationResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunevaluationresponse), [protos.google.cloud.ces.v1beta.IRunEvaluationOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunevaluationoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### runEvaluationResultMetrics(request, options)
    
    
    runEvaluationResultMetrics(request?: protos.google.cloud.ces.v1beta.IRunEvaluationResultMetricsRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.ces.v1beta.IRunEvaluationResultMetricsResponse, protos.google.cloud.ces.v1beta.IRunEvaluationResultMetricsOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Runs metrics on an existing evaluation result.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunEvaluationResultMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunevaluationresultmetricsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.ces.v1beta.IRunEvaluationResultMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunevaluationresultmetricsresponse), [protos.google.cloud.ces.v1beta.IRunEvaluationResultMetricsOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunevaluationresultmetricsoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The evaluation result to run metrics for.
       *  Format:
       *  `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}/results/{evaluation_result_id}`
       */
      // const evaluationResultId = 'abc123'
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callRunEvaluationResultMetrics() {
        // Construct request
        const request = {
          evaluationResultId,
        };
    
        // Run request
        const [operation] = await cesClient.runEvaluationResultMetrics(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callRunEvaluationResultMetrics();
    
    

### runEvaluationResultMetrics(request, options, callback)
    
    
    runEvaluationResultMetrics(request: protos.google.cloud.ces.v1beta.IRunEvaluationResultMetricsRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.ces.v1beta.IRunEvaluationResultMetricsResponse, protos.google.cloud.ces.v1beta.IRunEvaluationResultMetricsOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunEvaluationResultMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunevaluationresultmetricsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.ces.v1beta.IRunEvaluationResultMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunevaluationresultmetricsresponse), [protos.google.cloud.ces.v1beta.IRunEvaluationResultMetricsOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunevaluationresultmetricsoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### runEvaluationResultMetrics(request, callback)
    
    
    runEvaluationResultMetrics(request: protos.google.cloud.ces.v1beta.IRunEvaluationResultMetricsRequest, callback: Callback<LROperation<protos.google.cloud.ces.v1beta.IRunEvaluationResultMetricsResponse, protos.google.cloud.ces.v1beta.IRunEvaluationResultMetricsOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunEvaluationResultMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunevaluationresultmetricsrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.ces.v1beta.IRunEvaluationResultMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunevaluationresultmetricsresponse), [protos.google.cloud.ces.v1beta.IRunEvaluationResultMetricsOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunevaluationresultmetricsoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### scheduledEvaluationRunPath(project, location, app, scheduledEvaluationRun)
    
    
    scheduledEvaluationRunPath(project: string, location: string, app: string, scheduledEvaluationRun: string): string;

Return a fully-qualified scheduledEvaluationRun resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`app` |  `string`   
  
`scheduledEvaluationRun` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### securitySettingsPath(project, location)
    
    
    securitySettingsPath(project: string, location: string): string;

Return a fully-qualified securitySettings resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### testPersonaVoice(request, options)
    
    
    testPersonaVoice(request?: protos.google.cloud.ces.v1beta.ITestPersonaVoiceRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.ITestPersonaVoiceResponse,
            protos.google.cloud.ces.v1beta.ITestPersonaVoiceRequest | undefined,
            {} | undefined
        ]>;

Tests the voice of a persona. Also accepts a default persona.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestPersonaVoiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.itestpersonavoicerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.ITestPersonaVoiceResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.itestpersonavoiceresponse), [protos.google.cloud.ces.v1beta.ITestPersonaVoiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.itestpersonavoicerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [TestPersonaVoiceResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.testpersonavoiceresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. the resource name of the app to test the persona voice for.
       *  Format:
       *  `projects/{project}/locations/{location}/apps/{app}`
       */
      // const app = 'abc123'
      /**
       *  Required. The persona ID to test the voice for. Also accepts "default".
       */
      // const personaId = 'abc123'
      /**
       *  Required. The text to test the voice for.
       */
      // const text = 'abc123'
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callTestPersonaVoice() {
        // Construct request
        const request = {
          app,
          personaId,
          text,
        };
    
        // Run request
        const response = await cesClient.testPersonaVoice(request);
        console.log(response);
      }
    
      callTestPersonaVoice();
    
    

### testPersonaVoice(request, options, callback)
    
    
    testPersonaVoice(request: protos.google.cloud.ces.v1beta.ITestPersonaVoiceRequest, options: CallOptions, callback: Callback<protos.google.cloud.ces.v1beta.ITestPersonaVoiceResponse, protos.google.cloud.ces.v1beta.ITestPersonaVoiceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestPersonaVoiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.itestpersonavoicerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.ITestPersonaVoiceResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.itestpersonavoiceresponse), [protos.google.cloud.ces.v1beta.ITestPersonaVoiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.itestpersonavoicerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testPersonaVoice(request, callback)
    
    
    testPersonaVoice(request: protos.google.cloud.ces.v1beta.ITestPersonaVoiceRequest, callback: Callback<protos.google.cloud.ces.v1beta.ITestPersonaVoiceResponse, protos.google.cloud.ces.v1beta.ITestPersonaVoiceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestPersonaVoiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.itestpersonavoicerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.ITestPersonaVoiceResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.itestpersonavoiceresponse), [protos.google.cloud.ces.v1beta.ITestPersonaVoiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.itestpersonavoicerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### toolPath(project, location, app, tool)
    
    
    toolPath(project: string, location: string, app: string, tool: string): string;

Return a fully-qualified tool resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`app` |  `string`   
  
`tool` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### toolsetPath(project, location, app, toolset)
    
    
    toolsetPath(project: string, location: string, app: string, toolset: string): string;

Return a fully-qualified toolset resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`app` |  `string`   
  
`toolset` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### updateEvaluation(request, options)
    
    
    updateEvaluation(request?: protos.google.cloud.ces.v1beta.IUpdateEvaluationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IEvaluation,
            protos.google.cloud.ces.v1beta.IUpdateEvaluationRequest | undefined,
            {} | undefined
        ]>;

Updates an evaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdateevaluationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluation), [protos.google.cloud.ces.v1beta.IUpdateEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdateevaluationrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The evaluation to update.
       */
      // const evaluation = {}
      /**
       *  Optional. Field mask is used to control which fields get updated. If the
       *  mask is not present, all fields will be updated.
       */
      // const updateMask = {}
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callUpdateEvaluation() {
        // Construct request
        const request = {
          evaluation,
        };
    
        // Run request
        const response = await cesClient.updateEvaluation(request);
        console.log(response);
      }
    
      callUpdateEvaluation();
    
    

### updateEvaluation(request, options, callback)
    
    
    updateEvaluation(request: protos.google.cloud.ces.v1beta.IUpdateEvaluationRequest, options: CallOptions, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluation, protos.google.cloud.ces.v1beta.IUpdateEvaluationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdateevaluationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluation), [protos.google.cloud.ces.v1beta.IUpdateEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdateevaluationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEvaluation(request, callback)
    
    
    updateEvaluation(request: protos.google.cloud.ces.v1beta.IUpdateEvaluationRequest, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluation, protos.google.cloud.ces.v1beta.IUpdateEvaluationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdateevaluationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluation), [protos.google.cloud.ces.v1beta.IUpdateEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdateevaluationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEvaluationDataset(request, options)
    
    
    updateEvaluationDataset(request?: protos.google.cloud.ces.v1beta.IUpdateEvaluationDatasetRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IEvaluationDataset,
            (protos.google.cloud.ces.v1beta.IUpdateEvaluationDatasetRequest | undefined),
            {} | undefined
        ]>;

Updates an evaluation dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdateevaluationdatasetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IEvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationdataset), ([protos.google.cloud.ces.v1beta.IUpdateEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdateevaluationdatasetrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [EvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluationdataset). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The evaluation dataset to update.
       */
      // const evaluationDataset = {}
      /**
       *  Optional. Field mask is used to control which fields get updated. If the
       *  mask is not present, all fields will be updated.
       */
      // const updateMask = {}
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callUpdateEvaluationDataset() {
        // Construct request
        const request = {
          evaluationDataset,
        };
    
        // Run request
        const response = await cesClient.updateEvaluationDataset(request);
        console.log(response);
      }
    
      callUpdateEvaluationDataset();
    
    

### updateEvaluationDataset(request, options, callback)
    
    
    updateEvaluationDataset(request: protos.google.cloud.ces.v1beta.IUpdateEvaluationDatasetRequest, options: CallOptions, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluationDataset, protos.google.cloud.ces.v1beta.IUpdateEvaluationDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdateevaluationdatasetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationdataset), [protos.google.cloud.ces.v1beta.IUpdateEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdateevaluationdatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEvaluationDataset(request, callback)
    
    
    updateEvaluationDataset(request: protos.google.cloud.ces.v1beta.IUpdateEvaluationDatasetRequest, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluationDataset, protos.google.cloud.ces.v1beta.IUpdateEvaluationDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdateevaluationdatasetrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationdataset), [protos.google.cloud.ces.v1beta.IUpdateEvaluationDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdateevaluationdatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEvaluationExpectation(request, options)
    
    
    updateEvaluationExpectation(request?: protos.google.cloud.ces.v1beta.IUpdateEvaluationExpectationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IEvaluationExpectation,
            (protos.google.cloud.ces.v1beta.IUpdateEvaluationExpectationRequest | undefined),
            {} | undefined
        ]>;

Updates an evaluation expectation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdateevaluationexpectationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IEvaluationExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationexpectation), ([protos.google.cloud.ces.v1beta.IUpdateEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdateevaluationexpectationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The evaluation expectation to update.
       */
      // const evaluationExpectation = {}
      /**
       *  Optional. Field mask is used to control which fields get updated. If the
       *  mask is not present, all fields will be updated.
       */
      // const updateMask = {}
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callUpdateEvaluationExpectation() {
        // Construct request
        const request = {
          evaluationExpectation,
        };
    
        // Run request
        const response = await cesClient.updateEvaluationExpectation(request);
        console.log(response);
      }
    
      callUpdateEvaluationExpectation();
    
    

### updateEvaluationExpectation(request, options, callback)
    
    
    updateEvaluationExpectation(request: protos.google.cloud.ces.v1beta.IUpdateEvaluationExpectationRequest, options: CallOptions, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluationExpectation, protos.google.cloud.ces.v1beta.IUpdateEvaluationExpectationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdateevaluationexpectationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluationExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationexpectation), [protos.google.cloud.ces.v1beta.IUpdateEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdateevaluationexpectationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEvaluationExpectation(request, callback)
    
    
    updateEvaluationExpectation(request: protos.google.cloud.ces.v1beta.IUpdateEvaluationExpectationRequest, callback: Callback<protos.google.cloud.ces.v1beta.IEvaluationExpectation, protos.google.cloud.ces.v1beta.IUpdateEvaluationExpectationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdateevaluationexpectationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IEvaluationExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationexpectation), [protos.google.cloud.ces.v1beta.IUpdateEvaluationExpectationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdateevaluationexpectationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateScheduledEvaluationRun(request, options)
    
    
    updateScheduledEvaluationRun(request?: protos.google.cloud.ces.v1beta.IUpdateScheduledEvaluationRunRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IScheduledEvaluationRun,
            (protos.google.cloud.ces.v1beta.IUpdateScheduledEvaluationRunRequest | undefined),
            {} | undefined
        ]>;

Updates a scheduled evaluation run.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdatescheduledevaluationrunrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IScheduledEvaluationRun](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ischeduledevaluationrun), ([protos.google.cloud.ces.v1beta.IUpdateScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdatescheduledevaluationrunrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The scheduled evaluation run to update.
       */
      // const scheduledEvaluationRun = {}
      /**
       *  Optional. Field mask is used to control which fields get updated. If the
       *  mask is not present, all fields will be updated.
       */
      // const updateMask = {}
    
      // Imports the Ces library
      const {EvaluationServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [EvaluationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.evaluationserviceclient.html)();
    
      async function callUpdateScheduledEvaluationRun() {
        // Construct request
        const request = {
          scheduledEvaluationRun,
        };
    
        // Run request
        const response = await cesClient.updateScheduledEvaluationRun(request);
        console.log(response);
      }
    
      callUpdateScheduledEvaluationRun();
    
    

### updateScheduledEvaluationRun(request, options, callback)
    
    
    updateScheduledEvaluationRun(request: protos.google.cloud.ces.v1beta.IUpdateScheduledEvaluationRunRequest, options: CallOptions, callback: Callback<protos.google.cloud.ces.v1beta.IScheduledEvaluationRun, protos.google.cloud.ces.v1beta.IUpdateScheduledEvaluationRunRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdatescheduledevaluationrunrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IScheduledEvaluationRun](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ischeduledevaluationrun), [protos.google.cloud.ces.v1beta.IUpdateScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdatescheduledevaluationrunrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateScheduledEvaluationRun(request, callback)
    
    
    updateScheduledEvaluationRun(request: protos.google.cloud.ces.v1beta.IUpdateScheduledEvaluationRunRequest, callback: Callback<protos.google.cloud.ces.v1beta.IScheduledEvaluationRun, protos.google.cloud.ces.v1beta.IUpdateScheduledEvaluationRunRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdatescheduledevaluationrunrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IScheduledEvaluationRun](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ischeduledevaluationrun), [protos.google.cloud.ces.v1beta.IUpdateScheduledEvaluationRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iupdatescheduledevaluationrunrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### uploadEvaluationAudio(request, options)
    
    
    uploadEvaluationAudio(request?: protos.google.cloud.ces.v1beta.IUploadEvaluationAudioRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IUploadEvaluationAudioResponse,
            protos.google.cloud.ces.v1beta.IUploadEvaluationAudioRequest | undefined,
            {} | undefined
        ]>;

Uploads audio for use in Golden Evaluations. Stores the audio in the Cloud Storage bucket defined in 'App.logging_settings.evaluation_audio_recording_config.gcs_bucket' and returns a transcript.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUploadEvaluationAudioRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iuploadevaluationaudiorequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IUploadEvaluationAudioResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iuploadevaluationaudioresponse), [protos.google.cloud.ces.v1beta.IUploadEvaluationAudioRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iuploadevaluationaudiorequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [UploadEvaluationAudioResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.uploadevaluationaudioresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Evaluation for which to upload the
       *  evaluation audio. Format:
       *  `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}`
       */
      // const name = 'abc123'
      /**
       *  Required. The raw audio bytes.
       *  The format of the audio must be single-channel LINEAR16 with a sample
       *  rate of 16kHz (default InputAudioConfig).
       */
      // const audioContent = Buffer.from('string')
      /**
       *  Optional. The Google Cloud Storage URI of the previously uploaded audio
       *  file to be deleted. Format: `gs://

### uploadEvaluationAudio(request, options, callback)
    
    
    uploadEvaluationAudio(request: protos.google.cloud.ces.v1beta.IUploadEvaluationAudioRequest, options: CallOptions, callback: Callback<protos.google.cloud.ces.v1beta.IUploadEvaluationAudioResponse, protos.google.cloud.ces.v1beta.IUploadEvaluationAudioRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUploadEvaluationAudioRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iuploadevaluationaudiorequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IUploadEvaluationAudioResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iuploadevaluationaudioresponse), [protos.google.cloud.ces.v1beta.IUploadEvaluationAudioRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iuploadevaluationaudiorequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### uploadEvaluationAudio(request, callback)
    
    
    uploadEvaluationAudio(request: protos.google.cloud.ces.v1beta.IUploadEvaluationAudioRequest, callback: Callback<protos.google.cloud.ces.v1beta.IUploadEvaluationAudioResponse, protos.google.cloud.ces.v1beta.IUploadEvaluationAudioRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUploadEvaluationAudioRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iuploadevaluationaudiorequest)`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IUploadEvaluationAudioResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iuploadevaluationaudioresponse), [protos.google.cloud.ces.v1beta.IUploadEvaluationAudioRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.iuploadevaluationaudiorequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
