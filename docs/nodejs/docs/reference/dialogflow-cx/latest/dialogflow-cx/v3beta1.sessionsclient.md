---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/v3beta1.sessionsclient
title: Class v3beta1.SessionsClient (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:52:33.283372+00:00
---

# Class v3beta1.SessionsClient (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/v3beta1.sessionsclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v3beta1.SessionsClient (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.6.0  5.5.0  5.1.0  5.0.1  4.10.0  4.9.0  4.8.0  4.6.0  4.3.1  4.2.0  4.0.0  3.4.2  3.2.1  3.1.2  2.15.0  2.14.0  2.13.0  2.12.1 

A session represents an interaction with a user. You retrieve user input and pass it to the method to determine user intent and respond. v3beta1

## Package

[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of SessionsClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new SessionsClient({fallback: true}, gax); ```  
  
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

### sessionsStub
    
    
    sessionsStub?: Promise<{
            [name: string]: Function;
        }>;

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
  
### detectIntent(request, options)
    
    
    detectIntent(request?: protos.google.cloud.dialogflow.cx.v3beta1.IDetectIntentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dialogflow.cx.v3beta1.IDetectIntentResponse,
            (protos.google.cloud.dialogflow.cx.v3beta1.IDetectIntentRequest | undefined),
            {} | undefined
        ]>;

Processes a natural language query and returns structured, actionable data as a result. This method is not idempotent, because it may cause session entity types to be updated, which in turn might affect results of future queries.

Note: Always use agent versions for production traffic. See [Versions and environments](<https://cloud.google.com/dialogflow/cx/docs/concept/version>).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDetectIntentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.idetectintentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dialogflow.cx.v3beta1.IDetectIntentResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.idetectintentresponse), ([protos.google.cloud.dialogflow.cx.v3beta1.IDetectIntentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.idetectintentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the session this query is sent to.
       *  Format:
       *  `projects/

### detectIntent(request, options, callback)
    
    
    detectIntent(request: protos.google.cloud.dialogflow.cx.v3beta1.IDetectIntentRequest, options: CallOptions, callback: Callback<protos.google.cloud.dialogflow.cx.v3beta1.IDetectIntentResponse, protos.google.cloud.dialogflow.cx.v3beta1.IDetectIntentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDetectIntentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.idetectintentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.cx.v3beta1.IDetectIntentResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.idetectintentresponse), [protos.google.cloud.dialogflow.cx.v3beta1.IDetectIntentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.idetectintentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### detectIntent(request, callback)
    
    
    detectIntent(request: protos.google.cloud.dialogflow.cx.v3beta1.IDetectIntentRequest, callback: Callback<protos.google.cloud.dialogflow.cx.v3beta1.IDetectIntentResponse, protos.google.cloud.dialogflow.cx.v3beta1.IDetectIntentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDetectIntentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.idetectintentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.cx.v3beta1.IDetectIntentResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.idetectintentresponse), [protos.google.cloud.dialogflow.cx.v3beta1.IDetectIntentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.idetectintentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
  
### fulfillIntent(request, options)
    
    
    fulfillIntent(request?: protos.google.cloud.dialogflow.cx.v3beta1.IFulfillIntentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dialogflow.cx.v3beta1.IFulfillIntentResponse,
            (protos.google.cloud.dialogflow.cx.v3beta1.IFulfillIntentRequest | undefined),
            {} | undefined
        ]>;

Fulfills a matched intent returned by . Must be called after , with input from [MatchIntentResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.matchintentresponse). Otherwise, the behavior is undefined.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFulfillIntentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ifulfillintentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dialogflow.cx.v3beta1.IFulfillIntentResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ifulfillintentresponse), ([protos.google.cloud.dialogflow.cx.v3beta1.IFulfillIntentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ifulfillintentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [FulfillIntentResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.fulfillintentresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Must be same as the corresponding MatchIntent request, otherwise the
       *  behavior is undefined.
       */
      // const matchIntentRequest = {}
      /**
       *  The matched intent/event to fulfill.
       */
      // const match = {}
      /**
       *  Instructs the speech synthesizer how to generate output audio.
       */
      // const outputAudioConfig = {}
    
      // Imports the Cx library
      const {SessionsClient} = require('[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)').v3beta1;
    
      // Instantiates a client
      const cxClient = new [SessionsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)();
    
      async function callFulfillIntent() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await cxClient.fulfillIntent(request);
        console.log(response);
      }
    
      callFulfillIntent();
    
    

### fulfillIntent(request, options, callback)
    
    
    fulfillIntent(request: protos.google.cloud.dialogflow.cx.v3beta1.IFulfillIntentRequest, options: CallOptions, callback: Callback<protos.google.cloud.dialogflow.cx.v3beta1.IFulfillIntentResponse, protos.google.cloud.dialogflow.cx.v3beta1.IFulfillIntentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFulfillIntentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ifulfillintentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.cx.v3beta1.IFulfillIntentResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ifulfillintentresponse), [protos.google.cloud.dialogflow.cx.v3beta1.IFulfillIntentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ifulfillintentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fulfillIntent(request, callback)
    
    
    fulfillIntent(request: protos.google.cloud.dialogflow.cx.v3beta1.IFulfillIntentRequest, callback: Callback<protos.google.cloud.dialogflow.cx.v3beta1.IFulfillIntentResponse, protos.google.cloud.dialogflow.cx.v3beta1.IFulfillIntentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFulfillIntentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ifulfillintentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.cx.v3beta1.IFulfillIntentResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ifulfillintentresponse), [protos.google.cloud.dialogflow.cx.v3beta1.IFulfillIntentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ifulfillintentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
  
### matchAgentFromProjectLocationAgentEnvironmentSessionName(projectLocationAgentEnvironmentSessionName)
    
    
    matchAgentFromProjectLocationAgentEnvironmentSessionName(projectLocationAgentEnvironmentSessionName: string): string | number;

Parse the agent from ProjectLocationAgentEnvironmentSession resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentSessionName` |  `string`   
A fully-qualified path representing project_location_agent_environment_session resource.  
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
  
### matchAgentFromProjectLocationAgentSessionName(projectLocationAgentSessionName)
    
    
    matchAgentFromProjectLocationAgentSessionName(projectLocationAgentSessionName: string): string | number;

Parse the agent from ProjectLocationAgentSession resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentSessionName` |  `string`   
A fully-qualified path representing project_location_agent_session resource.  
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
  
### matchCollectionFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreName` |  `string`   
A fully-qualified path representing project_location_collection_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
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
  
### matchDataStoreFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreName` |  `string`   
A fully-qualified path representing project_location_collection_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreName(projectLocationDataStoreName)
    
    
    matchDataStoreFromProjectLocationDataStoreName(projectLocationDataStoreName: string): string | number;

Parse the data_store from ProjectLocationDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreName` |  `string`   
A fully-qualified path representing project_location_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
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
  
### matchEnvironmentFromProjectLocationAgentEnvironmentSessionName(projectLocationAgentEnvironmentSessionName)
    
    
    matchEnvironmentFromProjectLocationAgentEnvironmentSessionName(projectLocationAgentEnvironmentSessionName: string): string | number;

Parse the environment from ProjectLocationAgentEnvironmentSession resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentSessionName` |  `string`   
A fully-qualified path representing project_location_agent_environment_session resource.  
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
  
### matchIntent(request, options)
    
    
    matchIntent(request?: protos.google.cloud.dialogflow.cx.v3beta1.IMatchIntentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dialogflow.cx.v3beta1.IMatchIntentResponse,
            protos.google.cloud.dialogflow.cx.v3beta1.IMatchIntentRequest | undefined,
            {} | undefined
        ]>;

Returns preliminary intent match results, doesn't change the session status.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMatchIntentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.imatchintentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dialogflow.cx.v3beta1.IMatchIntentResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.imatchintentresponse), [protos.google.cloud.dialogflow.cx.v3beta1.IMatchIntentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.imatchintentrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [MatchIntentResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.matchintentresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the session this query is sent to.
       *  Format:
       *  `projects/

### matchIntent(request, options, callback)
    
    
    matchIntent(request: protos.google.cloud.dialogflow.cx.v3beta1.IMatchIntentRequest, options: CallOptions, callback: Callback<protos.google.cloud.dialogflow.cx.v3beta1.IMatchIntentResponse, protos.google.cloud.dialogflow.cx.v3beta1.IMatchIntentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMatchIntentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.imatchintentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.cx.v3beta1.IMatchIntentResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.imatchintentresponse), [protos.google.cloud.dialogflow.cx.v3beta1.IMatchIntentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.imatchintentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### matchIntent(request, callback)
    
    
    matchIntent(request: protos.google.cloud.dialogflow.cx.v3beta1.IMatchIntentRequest, callback: Callback<protos.google.cloud.dialogflow.cx.v3beta1.IMatchIntentResponse, protos.google.cloud.dialogflow.cx.v3beta1.IMatchIntentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMatchIntentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.imatchintentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.cx.v3beta1.IMatchIntentResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.imatchintentresponse), [protos.google.cloud.dialogflow.cx.v3beta1.IMatchIntentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.imatchintentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
  
### matchLocationFromProjectLocationAgentEnvironmentSessionName(projectLocationAgentEnvironmentSessionName)
    
    
    matchLocationFromProjectLocationAgentEnvironmentSessionName(projectLocationAgentEnvironmentSessionName: string): string | number;

Parse the location from ProjectLocationAgentEnvironmentSession resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentSessionName` |  `string`   
A fully-qualified path representing project_location_agent_environment_session resource.  
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
  
### matchLocationFromProjectLocationAgentSessionName(projectLocationAgentSessionName)
    
    
    matchLocationFromProjectLocationAgentSessionName(projectLocationAgentSessionName: string): string | number;

Parse the location from ProjectLocationAgentSession resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentSessionName` |  `string`   
A fully-qualified path representing project_location_agent_session resource.  
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
  
### matchLocationFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName: string): string | number;

Parse the location from ProjectLocationCollectionDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreName` |  `string`   
A fully-qualified path representing project_location_collection_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreName(projectLocationDataStoreName)
    
    
    matchLocationFromProjectLocationDataStoreName(projectLocationDataStoreName: string): string | number;

Parse the location from ProjectLocationDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreName` |  `string`   
A fully-qualified path representing project_location_data_store resource.  
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
  
### matchProjectFromProjectLocationAgentEnvironmentSessionName(projectLocationAgentEnvironmentSessionName)
    
    
    matchProjectFromProjectLocationAgentEnvironmentSessionName(projectLocationAgentEnvironmentSessionName: string): string | number;

Parse the project from ProjectLocationAgentEnvironmentSession resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentSessionName` |  `string`   
A fully-qualified path representing project_location_agent_environment_session resource.  
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
  
### matchProjectFromProjectLocationAgentSessionName(projectLocationAgentSessionName)
    
    
    matchProjectFromProjectLocationAgentSessionName(projectLocationAgentSessionName: string): string | number;

Parse the project from ProjectLocationAgentSession resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentSessionName` |  `string`   
A fully-qualified path representing project_location_agent_session resource.  
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
  
### matchProjectFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName: string): string | number;

Parse the project from ProjectLocationCollectionDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreName` |  `string`   
A fully-qualified path representing project_location_collection_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreName(projectLocationDataStoreName)
    
    
    matchProjectFromProjectLocationDataStoreName(projectLocationDataStoreName: string): string | number;

Parse the project from ProjectLocationDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreName` |  `string`   
A fully-qualified path representing project_location_data_store resource.  
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
  
### matchSessionFromProjectLocationAgentEnvironmentSessionName(projectLocationAgentEnvironmentSessionName)
    
    
    matchSessionFromProjectLocationAgentEnvironmentSessionName(projectLocationAgentEnvironmentSessionName: string): string | number;

Parse the session from ProjectLocationAgentEnvironmentSession resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentSessionName` |  `string`   
A fully-qualified path representing project_location_agent_environment_session resource.  
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
  
### matchSessionFromProjectLocationAgentSessionName(projectLocationAgentSessionName)
    
    
    matchSessionFromProjectLocationAgentSessionName(projectLocationAgentSessionName: string): string | number;

Parse the session from ProjectLocationAgentSession resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentSessionName` |  `string`   
A fully-qualified path representing project_location_agent_session resource.  
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
  
### projectLocationAgentEnvironmentSessionPath(project, location, agent, environment, session)
    
    
    projectLocationAgentEnvironmentSessionPath(project: string, location: string, agent: string, environment: string, session: string): string;

Return a fully-qualified projectLocationAgentEnvironmentSession resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`environment` |  `string`   
  
`session` |  `string`   
  
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
  
### projectLocationAgentSessionPath(project, location, agent, session)
    
    
    projectLocationAgentSessionPath(project: string, location: string, agent: string, session: string): string;

Return a fully-qualified projectLocationAgentSession resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`agent` |  `string`   
  
`session` |  `string`   
  
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
  
### projectLocationCollectionDataStorePath(project, location, collection, dataStore)
    
    
    projectLocationCollectionDataStorePath(project: string, location: string, collection: string, dataStore: string): string;

Return a fully-qualified projectLocationCollectionDataStore resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStorePath(project, location, dataStore)
    
    
    projectLocationDataStorePath(project: string, location: string, dataStore: string): string;

Return a fully-qualified projectLocationDataStore resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
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
  
### serverStreamingDetectIntent(request, options)
    
    
    serverStreamingDetectIntent(request?: protos.google.cloud.dialogflow.cx.v3beta1.IDetectIntentRequest, options?: CallOptions): gax.CancellableStream;

Processes a natural language query and returns structured, actionable data as a result through server-side streaming. Server-side streaming allows Dialogflow to send [partial responses](https://cloud.google.com/dialogflow/cx/docs/concept/fulfillment#partial-response) earlier in a single request.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDetectIntentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.idetectintentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`gax.CancellableStream` | {Stream} An object stream which emits on 'data' event. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#server-streaming) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the session this query is sent to.
       *  Format:
       *  `projects/

### streamingDetectIntent(options)
    
    
    streamingDetectIntent(options?: CallOptions): gax.CancellableStream;

Processes a natural language query in audio format in a streaming fashion and returns structured, actionable data as a result. This method is only available via the gRPC API (not REST).

Note: Always use agent versions for production traffic. See [Versions and environments](<https://cloud.google.com/dialogflow/cx/docs/concept/version>).

**Parameter**  
---  
**Name** | **Description**  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`gax.CancellableStream` | {Stream} An object stream which is both readable and writable. It accepts objects representing [StreamingDetectIntentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.streamingdetectintentrequest) for write() method, and will emit objects representing [StreamingDetectIntentResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.streamingdetectintentresponse) on 'data' event asynchronously. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#bi-directional-streaming) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The name of the session this query is sent to.
       *  Format:
       *  `projects/

### submitAnswerFeedback(request, options)
    
    
    submitAnswerFeedback(request?: protos.google.cloud.dialogflow.cx.v3beta1.ISubmitAnswerFeedbackRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dialogflow.cx.v3beta1.IAnswerFeedback,
            (protos.google.cloud.dialogflow.cx.v3beta1.ISubmitAnswerFeedbackRequest | undefined),
            {} | undefined
        ]>;

Updates the feedback received from the user for a single turn of the bot response.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISubmitAnswerFeedbackRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.isubmitanswerfeedbackrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dialogflow.cx.v3beta1.IAnswerFeedback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ianswerfeedback), ([protos.google.cloud.dialogflow.cx.v3beta1.ISubmitAnswerFeedbackRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.isubmitanswerfeedbackrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the session the feedback was sent to.
       */
      // const session = 'abc123'
      /**
       *  Required. ID of the response to update its feedback. This is the same as
       *  DetectIntentResponse.response_id.
       */
      // const responseId = 'abc123'
      /**
       *  Required. Feedback provided for a bot answer.
       */
      // const answerFeedback = {}
      /**
       *  Optional. The mask to control which fields to update. If the mask is not
       *  present, all fields will be updated.
       */
      // const updateMask = {}
    
      // Imports the Cx library
      const {SessionsClient} = require('[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)').v3beta1;
    
      // Instantiates a client
      const cxClient = new [SessionsClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)();
    
      async function callSubmitAnswerFeedback() {
        // Construct request
        const request = {
          session,
          responseId,
          answerFeedback,
        };
    
        // Run request
        const response = await cxClient.submitAnswerFeedback(request);
        console.log(response);
      }
    
      callSubmitAnswerFeedback();
    
    

### submitAnswerFeedback(request, options, callback)
    
    
    submitAnswerFeedback(request: protos.google.cloud.dialogflow.cx.v3beta1.ISubmitAnswerFeedbackRequest, options: CallOptions, callback: Callback<protos.google.cloud.dialogflow.cx.v3beta1.IAnswerFeedback, protos.google.cloud.dialogflow.cx.v3beta1.ISubmitAnswerFeedbackRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISubmitAnswerFeedbackRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.isubmitanswerfeedbackrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.cx.v3beta1.IAnswerFeedback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ianswerfeedback), [protos.google.cloud.dialogflow.cx.v3beta1.ISubmitAnswerFeedbackRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.isubmitanswerfeedbackrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### submitAnswerFeedback(request, callback)
    
    
    submitAnswerFeedback(request: protos.google.cloud.dialogflow.cx.v3beta1.ISubmitAnswerFeedbackRequest, callback: Callback<protos.google.cloud.dialogflow.cx.v3beta1.IAnswerFeedback, protos.google.cloud.dialogflow.cx.v3beta1.ISubmitAnswerFeedbackRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISubmitAnswerFeedbackRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.isubmitanswerfeedbackrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.cx.v3beta1.IAnswerFeedback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.ianswerfeedback), [protos.google.cloud.dialogflow.cx.v3beta1.ISubmitAnswerFeedbackRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3beta1.isubmitanswerfeedbackrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
