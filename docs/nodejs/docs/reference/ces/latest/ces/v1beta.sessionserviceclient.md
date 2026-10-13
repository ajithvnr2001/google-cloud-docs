---
url: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.sessionserviceclient
title: Class v1beta.SessionServiceClient (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:05:48.338005+00:00
---

# Class v1beta.SessionServiceClient (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/v1beta.sessionserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.SessionServiceClient (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0 

Session service provides APIs for interacting with CES agents. v1beta

## Package

[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of SessionServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new SessionServiceClient({fallback: true}, gax); ```  
  
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

### sessionServiceStub
    
    
    sessionServiceStub?: Promise<{
            [name: string]: Function;
        }>;

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
  
### bidiRunSession(options)
    
    
    bidiRunSession(options?: CallOptions): gax.CancellableStream;

Establishes a bidirectional streaming connection with the CES agent. The agent processes continuous multimodal inputs (e.g., text, audio) and generates real-time multimodal output streams.

\--- Client Request Stream --- The client streams requests in the following order:

  1. Initialization: The first message must contain [SessionConfig](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.bidisessionclientmessage). For audio sessions, this should also include and to define audio processing and synthesis parameters.

  2. Interaction: Subsequent messages stream containing real-time user input data.

  3. Termination: The client should half-close the stream when there is no more user input. It should also half-close upon receiving or from the agent.




\--- Server Response Stream --- For each interaction turn, the agent streams messages in the following sequence:

  1. Speech Recognition (First N messages): Contains representing the concatenated user speech segments captured so far. This is only populated for audio sessions.

  2. Response (Next M messages): Contains delivering the agent's response in various modalities (e.g., text, audio).

  3. Turn Completion (Final message of the turn): Contains with set to true. This signals the end of the current turn and includes with execution details.




\--- Audio Best Practices --- 1. Streaming: Stream [audio data](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.sessioninput) **CONTINUOUSLY**, even during silence. Recommended chunk size: 40-120ms (balances latency vs. efficiency).

  1. Playback & Interruption: Play upon receipt. Stop playback immediately if an is received (e.g., user barge-in or new agent response).



**Parameter**  
---  
**Name** | **Description**  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`gax.CancellableStream` | {Stream} An object stream which is both readable and writable. It accepts objects representing [BidiSessionClientMessage](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.bidisessionclientmessage) for write() method, and will emit objects representing [BidiSessionServerMessage](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.bidisessionservermessage) on 'data' event asynchronously. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#bi-directional-streaming) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. The initial config message for the session.
       */
      // const config = {}
      /**
       *  Optional. Realtime input for the session.
       */
      // const realtimeInput = {}
    
      // Imports the Ces library
      const {SessionServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [SessionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)();
    
      async function callBidiRunSession() {
        // Construct request
        const request = {
        };
    
        // Run request
        const stream = await cesClient.bidiRunSession();
        stream.on('data', (response) => { console.log(response) });
        stream.on('error', (err) => { throw(err) });
        stream.on('end', () => { /* API call completed */ });
        stream.write(request);
        stream.end();
      }
    
      callBidiRunSession();
    
    

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
  
### matchAppFromSessionName(sessionName)
    
    
    matchAppFromSessionName(sessionName: string): string | number;

Parse the app from Session resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionName` |  `string`   
A fully-qualified path representing Session resource.  
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
  
### matchLocationFromSessionName(sessionName)
    
    
    matchLocationFromSessionName(sessionName: string): string | number;

Parse the location from Session resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionName` |  `string`   
A fully-qualified path representing Session resource.  
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
  
### matchProjectFromSessionName(sessionName)
    
    
    matchProjectFromSessionName(sessionName: string): string | number;

Parse the project from Session resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionName` |  `string`   
A fully-qualified path representing Session resource.  
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
  
### matchSessionFromSessionName(sessionName)
    
    
    matchSessionFromSessionName(sessionName: string): string | number;

Parse the session from Session resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionName` |  `string`   
A fully-qualified path representing Session resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
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
  
### runSession(request, options)
    
    
    runSession(request?: protos.google.cloud.ces.v1beta.IRunSessionRequest, options?: CallOptions): Promise<[
            protos.google.cloud.ces.v1beta.IRunSessionResponse,
            protos.google.cloud.ces.v1beta.IRunSessionRequest | undefined,
            {} | undefined
        ]>;

Initiates a single-turn interaction with the CES agent within a session.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunsessionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.ces.v1beta.IRunSessionResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunsessionresponse), [protos.google.cloud.ces.v1beta.IRunSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunsessionrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [RunSessionResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.runsessionresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The configuration for the session.
       */
      // const config = {}
      /**
       *  Required. Inputs for the session.
       */
      // const inputs = [1,2,3,4]
    
      // Imports the Ces library
      const {SessionServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [SessionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)();
    
      async function callRunSession() {
        // Construct request
        const request = {
          config,
          inputs,
        };
    
        // Run request
        const response = await cesClient.runSession(request);
        console.log(response);
      }
    
      callRunSession();
    
    

### runSession(request, options, callback)
    
    
    runSession(request: protos.google.cloud.ces.v1beta.IRunSessionRequest, options: CallOptions, callback: Callback<protos.google.cloud.ces.v1beta.IRunSessionResponse, protos.google.cloud.ces.v1beta.IRunSessionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunsessionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IRunSessionResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunsessionresponse), [protos.google.cloud.ces.v1beta.IRunSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunsessionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### runSession(request, callback)
    
    
    runSession(request: protos.google.cloud.ces.v1beta.IRunSessionRequest, callback: Callback<protos.google.cloud.ces.v1beta.IRunSessionResponse, protos.google.cloud.ces.v1beta.IRunSessionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunsessionrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.ces.v1beta.IRunSessionResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunsessionresponse), [protos.google.cloud.ces.v1beta.IRunSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunsessionrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### sessionPath(project, location, app, session)
    
    
    sessionPath(project: string, location: string, app: string, session: string): string;

Return a fully-qualified session resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`app` |  `string`   
  
`session` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### streamRunSession(request, options)
    
    
    streamRunSession(request?: protos.google.cloud.ces.v1beta.IRunSessionRequest, options?: CallOptions): gax.CancellableStream;

Initiates a single-turn interaction with the CES agent. Uses server-side streaming to deliver incremental results and partial responses as they are generated.

By default, complete responses (e.g., messages from callbacks or full LLM responses) are sent to the client as soon as they are available. To enable streaming individual text chunks directly from the model, set to true.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.irunsessionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`gax.CancellableStream` | {Stream} An object stream which emits [RunSessionResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.runsessionresponse) on 'data' event. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#server-streaming) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The configuration for the session.
       */
      // const config = {}
      /**
       *  Required. Inputs for the session.
       */
      // const inputs = [1,2,3,4]
    
      // Imports the Ces library
      const {SessionServiceClient} = require('[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const cesClient = new [SessionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)();
    
      async function callStreamRunSession() {
        // Construct request
        const request = {
          config,
          inputs,
        };
    
        // Run request
        const stream = await cesClient.streamRunSession(request);
        stream.on('data', (response) => { console.log(response) });
        stream.on('error', (err) => { throw(err) });
        stream.on('end', () => { /* API call completed */ });
      }
    
      callStreamRunSession();
    
    

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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
