---
url: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/v1beta.datachatserviceclient
title: Class v1beta.DataChatServiceClient (0.13.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:37:28.132001+00:00
---

# Class v1beta.DataChatServiceClient (0.13.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/v1beta.datachatserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.DataChatServiceClient (0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.13.0  0.7.0  0.6.0  0.4.0  0.2.0 

Service to ask a natural language question on top of BigQuery and Looker Studio datasources to get back streamed responses of various kinds to help provide a rich conversational answer. v1beta

## Package

[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of DataChatServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new DataChatServiceClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### dataChatServiceStub
    
    
    dataChatServiceStub?: Promise<{
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

### chat(request, options)
    
    
    chat(request?: protos.google.cloud.geminidataanalytics.v1beta.IChatRequest, options?: CallOptions): gax.CancellableStream;

Answers a data question by generating a stream of [Message](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.message) objects.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IChatRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ichatrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`gax.CancellableStream` | {Stream} An object stream which emits [Message](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.message) on 'data' event. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#server-streaming) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Inline context for the chat request. Use this to chat
       *  statelessly (without managed conversation persistence and without an
       *  Agent) by passing all context inline.
       */
      // const inlineContext = {}
      /**
       *  Optional. Reference to a persisted conversation and agent context.
       *  Use this to chat with an Agent using managed conversation persistence.
       */
      // const conversationReference = {}
      /**
       *  Optional. Context for the chat request. Use this to chat with an Agent
       *  statelessly, without managed conversation persistence.
       */
      // const dataAgentContext = {}
      /**
       *  Optional. Context with client managed resources.
       *  Some clients may not use GDA managed resources including
       *  conversations and agents, instead they create and manage their own
       *  conversations and agents resources.
       */
      // const clientManagedResourceContext = {}
      /**
       *  Optional. Looker specific settings.
       */
      // const lookerSettings = {}
      /**
       *  Required. The parent value for chat request.
       *  Pattern: `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Required. Content of current conversation.
       */
      // const messages = [1,2,3,4]
      /**
       *  Optional. The credentials to use when calling the data source(s) specified
       *  in the context.
       *  This field can be used to provide credentials for various data sources.
       *  For example, when connecting to Looker, it currently supports both OAuth
       *  token and API key-based credentials, as described in
       *  Authentication with an
       *  SDK (https://cloud.google.com/looker/docs/api-auth#authentication_with_an_sdk).
       */
      // const credentials = {}
      /**
       *  Optional. The thinking mode to use for the agent loop.
       *  Defaults to THINKING_MODE_UNSPECIFIED if not specified.
       */
      // const thinkingMode = {}
      /**
       *  Optional. The model to use for the agent loop when processing the request.
       *  This setting only has an effect when context.options.model is not set.
       */
      // const model = {}
    
      // Imports the Geminidataanalytics library
      const {DataChatServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataChatServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callChat() {
        // Construct request
        const request = {
          parent,
          messages,
        };
    
        // Run request
        const stream = await geminidataanalyticsClient.chat(request);
        stream.on('data', (response) => { console.log(response) });
        stream.on('error', (err) => { throw(err) });
        stream.on('end', () => { /* API call completed */ });
      }
    
      callChat();
    
    

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
  
### createConversation(request, options)
    
    
    createConversation(request?: protos.google.cloud.geminidataanalytics.v1beta.ICreateConversationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.geminidataanalytics.v1beta.IConversation,
            (protos.google.cloud.geminidataanalytics.v1beta.ICreateConversationRequest | undefined),
            {} | undefined
        ]>;

Creates a new conversation to persist the conversation history. Each conversation will have multiple messages associated with it.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.icreateconversationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.geminidataanalytics.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iconversation), ([protos.google.cloud.geminidataanalytics.v1beta.ICreateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.icreateconversationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Conversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.conversation). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent value for CreateConversationRequest.
       *  Format: `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. The conversation id of the conversation to create.
       *  Must be unique within the parent.
       *  The allowed format is: `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`.
       *  If not provided, the server will auto-generate a value for the id.
       */
      // const conversationId = 'abc123'
      /**
       *  Required. The conversation to create.
       */
      // const conversation = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       */
      // const requestId = 'abc123'
    
      // Imports the Geminidataanalytics library
      const {DataChatServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataChatServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callCreateConversation() {
        // Construct request
        const request = {
          parent,
          conversation,
        };
    
        // Run request
        const response = await geminidataanalyticsClient.createConversation(request);
        console.log(response);
      }
    
      callCreateConversation();
    
    

### createConversation(request, options, callback)
    
    
    createConversation(request: protos.google.cloud.geminidataanalytics.v1beta.ICreateConversationRequest, options: CallOptions, callback: Callback<protos.google.cloud.geminidataanalytics.v1beta.IConversation, protos.google.cloud.geminidataanalytics.v1beta.ICreateConversationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.icreateconversationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.geminidataanalytics.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iconversation), [protos.google.cloud.geminidataanalytics.v1beta.ICreateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.icreateconversationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConversation(request, callback)
    
    
    createConversation(request: protos.google.cloud.geminidataanalytics.v1beta.ICreateConversationRequest, callback: Callback<protos.google.cloud.geminidataanalytics.v1beta.IConversation, protos.google.cloud.geminidataanalytics.v1beta.ICreateConversationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.icreateconversationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.geminidataanalytics.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iconversation), [protos.google.cloud.geminidataanalytics.v1beta.ICreateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.icreateconversationrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### deleteConversation(request, options)
    
    
    deleteConversation(request?: protos.google.cloud.geminidataanalytics.v1beta.IDeleteConversationRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.geminidataanalytics.v1beta.IDeleteConversationRequest | undefined),
            {} | undefined
        ]>;

Deletes a conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ideleteconversationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.protobuf.iempty), ([protos.google.cloud.geminidataanalytics.v1beta.IDeleteConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ideleteconversationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the resource.
       *  Format:
       *  `projects/{project}/locations/{location}/conversations/{conversation}`
       */
      // const name = 'abc123'
    
      // Imports the Geminidataanalytics library
      const {DataChatServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataChatServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callDeleteConversation() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await geminidataanalyticsClient.deleteConversation(request);
        console.log(response);
      }
    
      callDeleteConversation();
    
    

### deleteConversation(request, options, callback)
    
    
    deleteConversation(request: protos.google.cloud.geminidataanalytics.v1beta.IDeleteConversationRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.geminidataanalytics.v1beta.IDeleteConversationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ideleteconversationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.protobuf.iempty), [protos.google.cloud.geminidataanalytics.v1beta.IDeleteConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ideleteconversationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConversation(request, callback)
    
    
    deleteConversation(request: protos.google.cloud.geminidataanalytics.v1beta.IDeleteConversationRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.geminidataanalytics.v1beta.IDeleteConversationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ideleteconversationrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.protobuf.iempty), [protos.google.cloud.geminidataanalytics.v1beta.IDeleteConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ideleteconversationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConversation(request, options)
    
    
    getConversation(request?: protos.google.cloud.geminidataanalytics.v1beta.IGetConversationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.geminidataanalytics.v1beta.IConversation,
            (protos.google.cloud.geminidataanalytics.v1beta.IGetConversationRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single conversation by using conversation id and parent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.igetconversationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.geminidataanalytics.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iconversation), ([protos.google.cloud.geminidataanalytics.v1beta.IGetConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.igetconversationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Conversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.conversation). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the resource.
       *  Format:
       *  `projects/{project}/locations/{location}/conversations/{conversation}`
       */
      // const name = 'abc123'
    
      // Imports the Geminidataanalytics library
      const {DataChatServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataChatServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callGetConversation() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await geminidataanalyticsClient.getConversation(request);
        console.log(response);
      }
    
      callGetConversation();
    
    

### getConversation(request, options, callback)
    
    
    getConversation(request: protos.google.cloud.geminidataanalytics.v1beta.IGetConversationRequest, options: CallOptions, callback: Callback<protos.google.cloud.geminidataanalytics.v1beta.IConversation, protos.google.cloud.geminidataanalytics.v1beta.IGetConversationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.igetconversationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.geminidataanalytics.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iconversation), [protos.google.cloud.geminidataanalytics.v1beta.IGetConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.igetconversationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConversation(request, callback)
    
    
    getConversation(request: protos.google.cloud.geminidataanalytics.v1beta.IGetConversationRequest, callback: Callback<protos.google.cloud.geminidataanalytics.v1beta.IConversation, protos.google.cloud.geminidataanalytics.v1beta.IGetConversationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.igetconversationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.geminidataanalytics.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iconversation), [protos.google.cloud.geminidataanalytics.v1beta.IGetConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.igetconversationrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listConversations(request, options)
    
    
    listConversations(request?: protos.google.cloud.geminidataanalytics.v1beta.IListConversationsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.geminidataanalytics.v1beta.IConversation[],
            protos.google.cloud.geminidataanalytics.v1beta.IListConversationsRequest | null,
            protos.google.cloud.geminidataanalytics.v1beta.IListConversationsResponse
        ]>;

Lists all conversations for a given parent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistconversationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.geminidataanalytics.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iconversation)[], [protos.google.cloud.geminidataanalytics.v1beta.IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistconversationsrequest) | null, [protos.google.cloud.geminidataanalytics.v1beta.IListConversationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistconversationsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Conversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.conversation). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listConversationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listConversations(request, options, callback)
    
    
    listConversations(request: protos.google.cloud.geminidataanalytics.v1beta.IListConversationsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.geminidataanalytics.v1beta.IListConversationsRequest, protos.google.cloud.geminidataanalytics.v1beta.IListConversationsResponse | null | undefined, protos.google.cloud.geminidataanalytics.v1beta.IConversation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistconversationsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.geminidataanalytics.v1beta.IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistconversationsrequest), [protos.google.cloud.geminidataanalytics.v1beta.IListConversationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistconversationsresponse) | null | undefined, [protos.google.cloud.geminidataanalytics.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iconversation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConversations(request, callback)
    
    
    listConversations(request: protos.google.cloud.geminidataanalytics.v1beta.IListConversationsRequest, callback: PaginationCallback<protos.google.cloud.geminidataanalytics.v1beta.IListConversationsRequest, protos.google.cloud.geminidataanalytics.v1beta.IListConversationsResponse | null | undefined, protos.google.cloud.geminidataanalytics.v1beta.IConversation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistconversationsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.geminidataanalytics.v1beta.IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistconversationsrequest), [protos.google.cloud.geminidataanalytics.v1beta.IListConversationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistconversationsresponse) | null | undefined, [protos.google.cloud.geminidataanalytics.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iconversation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConversationsAsync(request, options)
    
    
    listConversationsAsync(request?: protos.google.cloud.geminidataanalytics.v1beta.IListConversationsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.geminidataanalytics.v1beta.IConversation>;

Equivalent to `listConversations`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistconversationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.geminidataanalytics.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iconversation)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Conversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.conversation). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent value for ListConversationsRequest.
       *  Format: `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. The max page size is `100`. All larger page sizes will be
       *  coerced to `100`. If unspecified, server will pick `50` as an appropriate
       *  default.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results the server should return.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Returned conversations will match criteria specified within the
       *  filter. ListConversations allows filtering by:
       *   * agents
       *   * labels
       */
      // const filter = 'abc123'
    
      // Imports the Geminidataanalytics library
      const {DataChatServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataChatServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callListConversations() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = geminidataanalyticsClient.listConversationsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListConversations();
    
    

### listConversationsStream(request, options)
    
    
    listConversationsStream(request?: protos.google.cloud.geminidataanalytics.v1beta.IListConversationsRequest, options?: CallOptions): Transform;

Equivalent to `listConversations`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistconversationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Conversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.conversation) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listConversationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
    

### listMessages(request, options)
    
    
    listMessages(request?: protos.google.cloud.geminidataanalytics.v1beta.IListMessagesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.geminidataanalytics.v1beta.IStorageMessage[],
            protos.google.cloud.geminidataanalytics.v1beta.IListMessagesRequest | null,
            protos.google.cloud.geminidataanalytics.v1beta.IListMessagesResponse
        ]>;

Lists all messages for a given conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMessagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistmessagesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.geminidataanalytics.v1beta.IStorageMessage](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.istoragemessage)[], [protos.google.cloud.geminidataanalytics.v1beta.IListMessagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistmessagesrequest) | null, [protos.google.cloud.geminidataanalytics.v1beta.IListMessagesResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistmessagesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [StorageMessage](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.storagemessage). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listMessagesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listMessages(request, options, callback)
    
    
    listMessages(request: protos.google.cloud.geminidataanalytics.v1beta.IListMessagesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.geminidataanalytics.v1beta.IListMessagesRequest, protos.google.cloud.geminidataanalytics.v1beta.IListMessagesResponse | null | undefined, protos.google.cloud.geminidataanalytics.v1beta.IStorageMessage>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMessagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistmessagesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.geminidataanalytics.v1beta.IListMessagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistmessagesrequest), [protos.google.cloud.geminidataanalytics.v1beta.IListMessagesResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistmessagesresponse) | null | undefined, [protos.google.cloud.geminidataanalytics.v1beta.IStorageMessage](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.istoragemessage)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMessages(request, callback)
    
    
    listMessages(request: protos.google.cloud.geminidataanalytics.v1beta.IListMessagesRequest, callback: PaginationCallback<protos.google.cloud.geminidataanalytics.v1beta.IListMessagesRequest, protos.google.cloud.geminidataanalytics.v1beta.IListMessagesResponse | null | undefined, protos.google.cloud.geminidataanalytics.v1beta.IStorageMessage>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMessagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistmessagesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.geminidataanalytics.v1beta.IListMessagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistmessagesrequest), [protos.google.cloud.geminidataanalytics.v1beta.IListMessagesResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistmessagesresponse) | null | undefined, [protos.google.cloud.geminidataanalytics.v1beta.IStorageMessage](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.istoragemessage)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMessagesAsync(request, options)
    
    
    listMessagesAsync(request?: protos.google.cloud.geminidataanalytics.v1beta.IListMessagesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.geminidataanalytics.v1beta.IStorageMessage>;

Equivalent to `listMessages`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMessagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistmessagesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.geminidataanalytics.v1beta.IStorageMessage](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.istoragemessage)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [StorageMessage](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.storagemessage). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The conversation to list messages under.
       *  Format:
       *  `projects/{project}/locations/{location}/conversations/{conversation_id}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. The max page size is `100`. All larger page sizes will be
       *  coerced to `100`. If unspecified, server will pick `50` as an appropriate
       *  default.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results the server should return.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filtering results. See AIP-160 (https://google.aip.dev/160) for
       *  syntax.
       *  ListMessages allows filtering by:
       *   * create_time (e.g., `createTime > "2025-01-28T06:51:56-08:00"`)
       *   * update_time
       */
      // const filter = 'abc123'
    
      // Imports the Geminidataanalytics library
      const {DataChatServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataChatServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callListMessages() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = geminidataanalyticsClient.listMessagesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListMessages();
    
    

### listMessagesStream(request, options)
    
    
    listMessagesStream(request?: protos.google.cloud.geminidataanalytics.v1beta.IListMessagesRequest, options?: CallOptions): Transform;

Equivalent to `listMessages`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMessagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.ilistmessagesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [StorageMessage](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.storagemessage) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listMessagesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### queryData(request, options)
    
    
    queryData(request?: protos.google.cloud.geminidataanalytics.v1beta.IQueryDataRequest, options?: CallOptions): Promise<[
            protos.google.cloud.geminidataanalytics.v1beta.IQueryDataResponse,
            (protos.google.cloud.geminidataanalytics.v1beta.IQueryDataRequest | undefined),
            {} | undefined
        ]>;

Queries data from a natural language user query.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iquerydatarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.geminidataanalytics.v1beta.IQueryDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iquerydataresponse), ([protos.google.cloud.geminidataanalytics.v1beta.IQueryDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iquerydatarequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [QueryDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.querydataresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource to generate the query for.
       *  Format: projects/{project}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Required. The natural language query for which to generate query.
       *  Example: "What are the top 5 best selling products this month?"
       */
      // const prompt = 'abc123'
      /**
       *  Required. The context for the data query, including the data sources to
       *  use.
       */
      // const context = {}
      /**
       *  Optional. Options to control query generation and execution behavior.
       */
      // const generationOptions = {}
    
      // Imports the Geminidataanalytics library
      const {DataChatServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataChatServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callQueryData() {
        // Construct request
        const request = {
          parent,
          prompt,
          context,
        };
    
        // Run request
        const response = await geminidataanalyticsClient.queryData(request);
        console.log(response);
      }
    
      callQueryData();
    
    

### queryData(request, options, callback)
    
    
    queryData(request: protos.google.cloud.geminidataanalytics.v1beta.IQueryDataRequest, options: CallOptions, callback: Callback<protos.google.cloud.geminidataanalytics.v1beta.IQueryDataResponse, protos.google.cloud.geminidataanalytics.v1beta.IQueryDataRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iquerydatarequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.geminidataanalytics.v1beta.IQueryDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iquerydataresponse), [protos.google.cloud.geminidataanalytics.v1beta.IQueryDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iquerydatarequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryData(request, callback)
    
    
    queryData(request: protos.google.cloud.geminidataanalytics.v1beta.IQueryDataRequest, callback: Callback<protos.google.cloud.geminidataanalytics.v1beta.IQueryDataResponse, protos.google.cloud.geminidataanalytics.v1beta.IQueryDataRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iquerydatarequest)`   
  
`callback` |  `Callback<[protos.google.cloud.geminidataanalytics.v1beta.IQueryDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iquerydataresponse), [protos.google.cloud.geminidataanalytics.v1beta.IQueryDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iquerydatarequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConversation(request, options)
    
    
    updateConversation(request?: protos.google.cloud.geminidataanalytics.v1beta.IUpdateConversationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.geminidataanalytics.v1beta.IConversation,
            (protos.google.cloud.geminidataanalytics.v1beta.IUpdateConversationRequest | undefined),
            {} | undefined
        ]>;

Updates a conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iupdateconversationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.geminidataanalytics.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iconversation), ([protos.google.cloud.geminidataanalytics.v1beta.IUpdateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iupdateconversationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Conversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.conversation). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource being updated.
       */
      // const conversation = {}
      /**
       *  Optional. Field mask is used to specify the fields to be overwritten in the
       *  Conversation resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then all fields with non-default values
       *  present in the request will be overwritten. If a wildcard mask is provided,
       *  all fields will be overwritten.
       */
      // const updateMask = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       */
      // const requestId = 'abc123'
    
      // Imports the Geminidataanalytics library
      const {DataChatServiceClient} = require('[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const geminidataanalyticsClient = new [DataChatServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)();
    
      async function callUpdateConversation() {
        // Construct request
        const request = {
          conversation,
        };
    
        // Run request
        const response = await geminidataanalyticsClient.updateConversation(request);
        console.log(response);
      }
    
      callUpdateConversation();
    
    

### updateConversation(request, options, callback)
    
    
    updateConversation(request: protos.google.cloud.geminidataanalytics.v1beta.IUpdateConversationRequest, options: CallOptions, callback: Callback<protos.google.cloud.geminidataanalytics.v1beta.IConversation, protos.google.cloud.geminidataanalytics.v1beta.IUpdateConversationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iupdateconversationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.geminidataanalytics.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iconversation), [protos.google.cloud.geminidataanalytics.v1beta.IUpdateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iupdateconversationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConversation(request, callback)
    
    
    updateConversation(request: protos.google.cloud.geminidataanalytics.v1beta.IUpdateConversationRequest, callback: Callback<protos.google.cloud.geminidataanalytics.v1beta.IConversation, protos.google.cloud.geminidataanalytics.v1beta.IUpdateConversationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iupdateconversationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.geminidataanalytics.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iconversation), [protos.google.cloud.geminidataanalytics.v1beta.IUpdateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.iupdateconversationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
