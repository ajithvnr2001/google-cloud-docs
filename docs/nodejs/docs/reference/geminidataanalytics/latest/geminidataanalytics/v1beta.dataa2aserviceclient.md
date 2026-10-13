---
url: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/v1beta.dataa2aserviceclient
title: Class v1beta.DataA2AServiceClient (0.13.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:37:24.609582+00:00
---

# Class v1beta.DataA2AServiceClient (0.13.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/v1beta.dataa2aserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.DataA2AServiceClient (0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.13.0  0.7.0  0.6.0  0.4.0  0.2.0 

DataA2AService defines the Agent-to-Agent (A2A) protocol service for Gemini Data Analytics. v1beta

## Package

[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of DataA2AServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new DataA2AServiceClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### dataA2AServiceStub
    
    
    dataA2AServiceStub?: Promise<{
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
  
### getAgentCard(request, options)
    
    
    getAgentCard(request?: protos.google.cloud.geminidataanalytics.v1beta.IGetAgentCardRequest, options?: CallOptions): Promise<[
            protos.google.cloud.geminidataanalytics.v1beta.IAgentCard,
            (protos.google.cloud.geminidataanalytics.v1beta.IGetAgentCardRequest | undefined),
            {} | undefined
        ]>;

GetAgentCard returns the agent card for the agent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAgentCardRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.igetagentcardrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.geminidataanalytics.v1beta.IAgentCard](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iagentcard), ([protos.google.cloud.geminidataanalytics.v1beta.IGetAgentCardRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.igetagentcardrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [AgentCard](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.agentcard). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Optional tenant, provided as a path parameter.
       */
      // const tenant = 'abc123'
    
      // Imports the Geminidataanalytics library
      const {DataA2AServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new DataA2AServiceClient();
    
      async function callGetAgentCard() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await geminidataanalyticsClient.getAgentCard(request);
        console.log(response);
      }
    
      callGetAgentCard();
    
    

### getAgentCard(request, options, callback)
    
    
    getAgentCard(request: protos.google.cloud.geminidataanalytics.v1beta.IGetAgentCardRequest, options: CallOptions, callback: Callback<protos.google.cloud.geminidataanalytics.v1beta.IAgentCard, protos.google.cloud.geminidataanalytics.v1beta.IGetAgentCardRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAgentCardRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.igetagentcardrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.geminidataanalytics.v1beta.IAgentCard](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iagentcard), [protos.google.cloud.geminidataanalytics.v1beta.IGetAgentCardRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.igetagentcardrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAgentCard(request, callback)
    
    
    getAgentCard(request: protos.google.cloud.geminidataanalytics.v1beta.IGetAgentCardRequest, callback: Callback<protos.google.cloud.geminidataanalytics.v1beta.IAgentCard, protos.google.cloud.geminidataanalytics.v1beta.IGetAgentCardRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAgentCardRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.igetagentcardrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.geminidataanalytics.v1beta.IAgentCard](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iagentcard), [protos.google.cloud.geminidataanalytics.v1beta.IGetAgentCardRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.igetagentcardrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### sendMessage(request, options)
    
    
    sendMessage(request?: protos.google.cloud.geminidataanalytics.v1beta.ISendMessageRequest, options?: CallOptions): Promise<[
            protos.google.cloud.geminidataanalytics.v1beta.ISendMessageResponse,
            (protos.google.cloud.geminidataanalytics.v1beta.ISendMessageRequest | undefined),
            {} | undefined
        ]>;

Send a message to the agent. This is a blocking call that will return the task once it is completed.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISendMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.isendmessagerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.geminidataanalytics.v1beta.ISendMessageResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.isendmessageresponse), ([protos.google.cloud.geminidataanalytics.v1beta.ISendMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.isendmessagerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [SendMessageResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.sendmessageresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The message to send to the agent.
       */
      // const message = {}
      /**
       *  Optional. Configuration for the send request.
       */
      // const configuration = {}
      /**
       *  Optional. Optional metadata for the request.
       */
      // const metadata = {}
      /**
       *  Optional. Optional tenant, provided as a path parameter.
       */
      // const tenant = 'abc123'
    
      // Imports the Geminidataanalytics library
      const {DataA2AServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new DataA2AServiceClient();
    
      async function callSendMessage() {
        // Construct request
        const request = {
          message,
        };
    
        // Run request
        const response = await geminidataanalyticsClient.sendMessage(request);
        console.log(response);
      }
    
      callSendMessage();
    
    

### sendMessage(request, options, callback)
    
    
    sendMessage(request: protos.google.cloud.geminidataanalytics.v1beta.ISendMessageRequest, options: CallOptions, callback: Callback<protos.google.cloud.geminidataanalytics.v1beta.ISendMessageResponse, protos.google.cloud.geminidataanalytics.v1beta.ISendMessageRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISendMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.isendmessagerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.geminidataanalytics.v1beta.ISendMessageResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.isendmessageresponse), [protos.google.cloud.geminidataanalytics.v1beta.ISendMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.isendmessagerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### sendMessage(request, callback)
    
    
    sendMessage(request: protos.google.cloud.geminidataanalytics.v1beta.ISendMessageRequest, callback: Callback<protos.google.cloud.geminidataanalytics.v1beta.ISendMessageResponse, protos.google.cloud.geminidataanalytics.v1beta.ISendMessageRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISendMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.isendmessagerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.geminidataanalytics.v1beta.ISendMessageResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.isendmessageresponse), [protos.google.cloud.geminidataanalytics.v1beta.ISendMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.isendmessagerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### sendStreamingMessage(request, options)
    
    
    sendStreamingMessage(request?: protos.google.cloud.geminidataanalytics.v1beta.ISendMessageRequest, options?: CallOptions): gax.CancellableStream;

SendStreamingMessage is a streaming call that will return a stream of task update events until the Task is in an interrupted or terminal state.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISendMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.isendmessagerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`gax.CancellableStream` | {Stream} An object stream which emits [StreamResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.streamresponse) on 'data' event. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#server-streaming) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The message to send to the agent.
       */
      // const message = {}
      /**
       *  Optional. Configuration for the send request.
       */
      // const configuration = {}
      /**
       *  Optional. Optional metadata for the request.
       */
      // const metadata = {}
      /**
       *  Optional. Optional tenant, provided as a path parameter.
       */
      // const tenant = 'abc123'
    
      // Imports the Geminidataanalytics library
      const {DataA2AServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new DataA2AServiceClient();
    
      async function callSendStreamingMessage() {
        // Construct request
        const request = {
          message,
        };
    
        // Run request
        const stream = await geminidataanalyticsClient.sendStreamingMessage(request);
        stream.on('data', (response) => { console.log(response) });
        stream.on('error', (err) => { throw(err) });
        stream.on('end', () => { /* API call completed */ });
      }
    
      callSendStreamingMessage();
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
