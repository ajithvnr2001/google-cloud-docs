---
url: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/v1beta.conversationalsearchserviceclient
title: Class v1beta.ConversationalSearchServiceClient (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:01:01.935306+00:00
---

# Class v1beta.ConversationalSearchServiceClient (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/v1beta.conversationalsearchserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.ConversationalSearchServiceClient (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  3.3.0  3.1.0  2.9.0  2.8.0  2.6.0  2.2.0  2.0.1  1.14.0  1.10.0  1.9.0  1.7.0  1.6.0  1.4.1  1.3.1  1.2.0  1.0.0  0.6.0  0.5.0  0.3.1  0.2.0 

Service for conversational search. v1beta

## Package

[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of ConversationalSearchServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new ConversationalSearchServiceClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### conversationalSearchServiceStub
    
    
    conversationalSearchServiceStub?: Promise<{
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

### aclConfigPath(project, location)
    
    
    aclConfigPath(project: string, location: string): string;

Return a fully-qualified aclConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### answerQuery(request, options)
    
    
    answerQuery(request?: protos.google.cloud.discoveryengine.v1beta.IAnswerQueryRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1beta.IAnswerQueryResponse,
            (protos.google.cloud.discoveryengine.v1beta.IAnswerQueryRequest | undefined),
            {} | undefined
        ]>;

Answer query method.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnswerQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ianswerqueryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1beta.IAnswerQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ianswerqueryresponse), ([protos.google.cloud.discoveryengine.v1beta.IAnswerQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ianswerqueryrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [AnswerQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.answerqueryresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Search serving config, such as
       *  `projects/* /locations/global/collections/default_collection/engines/* /servingConfigs/default_serving_config`,
       *  or
       *  `projects/* /locations/global/collections/default_collection/dataStores/* /servingConfigs/default_serving_config`.
       *  Or the resource name of the agent engine serving config, such as:
       *  `projects/* /locations/global/collections/default_collection/engines/* /servingConfigs/default_agent_answer`.
       *  (use when `enable_agent_invocation` set to true, and you have custom
       *  `AI_MODE` agent engine configured)
       *  This field is used to identify the serving configuration name, set
       *  of models used to make the search.
       */
      // const servingConfig = 'abc123'
      /**
       *  Required. Current user query.
       */
      // const query = {}
      /**
       *  The session resource name. Not required.
       *  When session field is not set, the API is in sessionless mode.
       *  We support auto session mode: users can use the wildcard symbol `-` as
       *  session ID.  A new ID will be automatically generated and assigned.
       */
      // const session = 'abc123'
      /**
       *  Model specification.
       */
      // const safetySpec = {}
      /**
       *  Related questions specification.
       */
      // const relatedQuestionsSpec = {}
      /**
       *  Optional. Grounding specification.
       */
      // const groundingSpec = {}
      /**
       *  Answer generation specification.
       */
      // const answerGenerationSpec = {}
      /**
       *  Search specification.
       */
      // const searchSpec = {}
      /**
       *  Query understanding specification.
       */
      // const queryUnderstandingSpec = {}
      /**
       *  A unique identifier for tracking visitors. For example, this could be
       *  implemented with an HTTP cookie, which should be able to uniquely identify
       *  a visitor on a single device. This unique identifier should not change if
       *  the visitor logs in or out of the website.
       *  This field should NOT have a fixed value such as `unknown_visitor`.
       *  The field must be a UTF-8 encoded string with a length limit of 128
       *  characters. Otherwise, an  `INVALID_ARGUMENT`  error is returned.
       */
      // const userPseudoId = 'abc123'
      /**
       *  The user labels applied to a resource must meet the following requirements:
       *  * Each resource can have multiple labels, up to a maximum of 64.
       *  * Each label must be a key-value pair.
       *  * Keys have a minimum length of 1 character and a maximum length of 63
       *    characters and cannot be empty. Values can be empty and have a maximum
       *    length of 63 characters.
       *  * Keys and values can contain only lowercase letters, numeric characters,
       *    underscores, and dashes. All characters must use UTF-8 encoding, and
       *    international characters are allowed.
       *  * The key portion of a label must be unique. However, you can use the same
       *    key with multiple resources.
       *  * Keys must start with a lowercase letter or international character.
       *  See Google Cloud
       *  Document (https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements)
       *  for more details.
       */
      // const userLabels = [1,2,3,4]
      /**
       *  Optional. End user specification.
       */
      // const endUserSpec = {}
    
      // Imports the Discoveryengine library
      const {ConversationalSearchServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [ConversationalSearchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callAnswerQuery() {
        // Construct request
        const request = {
          servingConfig,
          query,
        };
    
        // Run request
        const response = await discoveryengineClient.answerQuery(request);
        console.log(response);
      }
    
      callAnswerQuery();
    
    

### answerQuery(request, options, callback)
    
    
    answerQuery(request: protos.google.cloud.discoveryengine.v1beta.IAnswerQueryRequest, options: CallOptions, callback: Callback<protos.google.cloud.discoveryengine.v1beta.IAnswerQueryResponse, protos.google.cloud.discoveryengine.v1beta.IAnswerQueryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnswerQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ianswerqueryrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.IAnswerQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ianswerqueryresponse), [protos.google.cloud.discoveryengine.v1beta.IAnswerQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ianswerqueryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### answerQuery(request, callback)
    
    
    answerQuery(request: protos.google.cloud.discoveryengine.v1beta.IAnswerQueryRequest, callback: Callback<protos.google.cloud.discoveryengine.v1beta.IAnswerQueryResponse, protos.google.cloud.discoveryengine.v1beta.IAnswerQueryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnswerQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ianswerqueryrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.IAnswerQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ianswerqueryresponse), [protos.google.cloud.discoveryengine.v1beta.IAnswerQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ianswerqueryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### assistAnswerPath(project, location, collection, engine, session, assistAnswer)
    
    
    assistAnswerPath(project: string, location: string, collection: string, engine: string, session: string, assistAnswer: string): string;

Return a fully-qualified assistAnswer resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`session` |  `string`   
  
`assistAnswer` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### assistantPath(project, location, collection, engine, assistant)
    
    
    assistantPath(project: string, location: string, collection: string, engine: string, assistant: string): string;

Return a fully-qualified assistant resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`assistant` |  `string`   
  
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
  
### converseConversation(request, options)
    
    
    converseConversation(request?: protos.google.cloud.discoveryengine.v1beta.IConverseConversationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1beta.IConverseConversationResponse,
            (protos.google.cloud.discoveryengine.v1beta.IConverseConversationRequest | undefined),
            {} | undefined
        ]>;

Converses a conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IConverseConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconverseconversationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1beta.IConverseConversationResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconverseconversationresponse), ([protos.google.cloud.discoveryengine.v1beta.IConverseConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconverseconversationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ConverseConversationResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.converseconversationresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Conversation to get. Format:
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/{conversation_id}`.
       *  Use
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/-`
       *  to activate auto session mode, which automatically creates a new
       *  conversation inside a ConverseConversation session.
       */
      // const name = 'abc123'
      /**
       *  Required. Current user input.
       */
      // const query = {}
      /**
       *  The resource name of the Serving Config to use. Format:
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/servingConfigs/{serving_config_id}`
       *  If this is not set, the default serving config will be used.
       */
      // const servingConfig = 'abc123'
      /**
       *  The conversation to be used by auto session only. The name field will be
       *  ignored as we automatically assign new name for the conversation in auto
       *  session.
       */
      // const conversation = {}
      /**
       *  Whether to turn on safe search.
       */
      // const safeSearch = true
      /**
       *  The user labels applied to a resource must meet the following requirements:
       *  * Each resource can have multiple labels, up to a maximum of 64.
       *  * Each label must be a key-value pair.
       *  * Keys have a minimum length of 1 character and a maximum length of 63
       *    characters and cannot be empty. Values can be empty and have a maximum
       *    length of 63 characters.
       *  * Keys and values can contain only lowercase letters, numeric characters,
       *    underscores, and dashes. All characters must use UTF-8 encoding, and
       *    international characters are allowed.
       *  * The key portion of a label must be unique. However, you can use the same
       *    key with multiple resources.
       *  * Keys must start with a lowercase letter or international character.
       *  See Google Cloud
       *  Document (https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements)
       *  for more details.
       */
      // const userLabels = [1,2,3,4]
      /**
       *  A specification for configuring the summary returned in the response.
       */
      // const summarySpec = {}
      /**
       *  The filter syntax consists of an expression language for constructing a
       *  predicate from one or more fields of the documents being filtered. Filter
       *  expression is case-sensitive. This will be used to filter search results
       *  which may affect the summary response.
       *  If this field is unrecognizable, an  `INVALID_ARGUMENT`  is returned.
       *  Filtering in Vertex AI Search is done by mapping the LHS filter key to a
       *  key property defined in the Vertex AI Search backend -- this mapping is
       *  defined by the customer in their schema. For example a media customer might
       *  have a field 'name' in their schema. In this case the filter would look
       *  like this: filter --> name:'ANY("king kong")'
       *  For more information about filtering including syntax and filter
       *  operators, see
       *  Filter (https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata)
       */
      // const filter = 'abc123'
      /**
       *  Boost specification to boost certain documents in search results which may
       *  affect the converse response. For more information on boosting, see
       *  Boosting (https://cloud.google.com/retail/docs/boosting#boost)
       */
      // const boostSpec = {}
    
      // Imports the Discoveryengine library
      const {ConversationalSearchServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [ConversationalSearchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callConverseConversation() {
        // Construct request
        const request = {
          name,
          query,
        };
    
        // Run request
        const response = await discoveryengineClient.converseConversation(request);
        console.log(response);
      }
    
      callConverseConversation();
    
    

### converseConversation(request, options, callback)
    
    
    converseConversation(request: protos.google.cloud.discoveryengine.v1beta.IConverseConversationRequest, options: CallOptions, callback: Callback<protos.google.cloud.discoveryengine.v1beta.IConverseConversationResponse, protos.google.cloud.discoveryengine.v1beta.IConverseConversationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IConverseConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconverseconversationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.IConverseConversationResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconverseconversationresponse), [protos.google.cloud.discoveryengine.v1beta.IConverseConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconverseconversationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### converseConversation(request, callback)
    
    
    converseConversation(request: protos.google.cloud.discoveryengine.v1beta.IConverseConversationRequest, callback: Callback<protos.google.cloud.discoveryengine.v1beta.IConverseConversationResponse, protos.google.cloud.discoveryengine.v1beta.IConverseConversationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IConverseConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconverseconversationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.IConverseConversationResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconverseconversationresponse), [protos.google.cloud.discoveryengine.v1beta.IConverseConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconverseconversationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConversation(request, options)
    
    
    createConversation(request?: protos.google.cloud.discoveryengine.v1beta.ICreateConversationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1beta.IConversation,
            (protos.google.cloud.discoveryengine.v1beta.ICreateConversationRequest | undefined),
            {} | undefined
        ]>;

Creates a Conversation.

If the to create already exists, an ALREADY_EXISTS error is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreateconversationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconversation), ([protos.google.cloud.discoveryengine.v1beta.ICreateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreateconversationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of parent data store. Format:
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The conversation to create.
       */
      // const conversation = {}
    
      // Imports the Discoveryengine library
      const {ConversationalSearchServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [ConversationalSearchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callCreateConversation() {
        // Construct request
        const request = {
          parent,
          conversation,
        };
    
        // Run request
        const response = await discoveryengineClient.createConversation(request);
        console.log(response);
      }
    
      callCreateConversation();
    
    

### createConversation(request, options, callback)
    
    
    createConversation(request: protos.google.cloud.discoveryengine.v1beta.ICreateConversationRequest, options: CallOptions, callback: Callback<protos.google.cloud.discoveryengine.v1beta.IConversation, protos.google.cloud.discoveryengine.v1beta.ICreateConversationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreateconversationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconversation), [protos.google.cloud.discoveryengine.v1beta.ICreateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreateconversationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConversation(request, callback)
    
    
    createConversation(request: protos.google.cloud.discoveryengine.v1beta.ICreateConversationRequest, callback: Callback<protos.google.cloud.discoveryengine.v1beta.IConversation, protos.google.cloud.discoveryengine.v1beta.ICreateConversationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreateconversationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconversation), [protos.google.cloud.discoveryengine.v1beta.ICreateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreateconversationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSession(request, options)
    
    
    createSession(request?: protos.google.cloud.discoveryengine.v1beta.ICreateSessionRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1beta.ISession,
            (protos.google.cloud.discoveryengine.v1beta.ICreateSessionRequest | undefined),
            {} | undefined
        ]>;

Creates a Session.

If the to create already exists, an ALREADY_EXISTS error is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreatesessionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1beta.ISession](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.isession), ([protos.google.cloud.discoveryengine.v1beta.ICreateSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreatesessionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of parent data store. Format:
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The session to create.
       */
      // const session = {}
      /**
       *  Optional. The ID to use for the session, which will become the final
       *  component of the session's resource name.
       *  This value should be 1-63 characters, and valid characters
       *  are /[a-z0-9][a-z0-9-]{0,61}[a-z0-9]/. If not specified, a unique ID will
       *  be generated.
       */
      // const sessionId = 'abc123'
    
      // Imports the Discoveryengine library
      const {ConversationalSearchServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [ConversationalSearchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callCreateSession() {
        // Construct request
        const request = {
          parent,
          session,
        };
    
        // Run request
        const response = await discoveryengineClient.createSession(request);
        console.log(response);
      }
    
      callCreateSession();
    
    

### createSession(request, options, callback)
    
    
    createSession(request: protos.google.cloud.discoveryengine.v1beta.ICreateSessionRequest, options: CallOptions, callback: Callback<protos.google.cloud.discoveryengine.v1beta.ISession, protos.google.cloud.discoveryengine.v1beta.ICreateSessionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreatesessionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.ISession](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.isession), [protos.google.cloud.discoveryengine.v1beta.ICreateSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreatesessionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSession(request, callback)
    
    
    createSession(request: protos.google.cloud.discoveryengine.v1beta.ICreateSessionRequest, callback: Callback<protos.google.cloud.discoveryengine.v1beta.ISession, protos.google.cloud.discoveryengine.v1beta.ICreateSessionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreatesessionrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.ISession](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.isession), [protos.google.cloud.discoveryengine.v1beta.ICreateSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreatesessionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConversation(request, options)
    
    
    deleteConversation(request?: protos.google.cloud.discoveryengine.v1beta.IDeleteConversationRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.discoveryengine.v1beta.IDeleteConversationRequest | undefined),
            {} | undefined
        ]>;

Deletes a Conversation.

If the to delete does not exist, a NOT_FOUND error is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ideleteconversationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.iempty), ([protos.google.cloud.discoveryengine.v1beta.IDeleteConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ideleteconversationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Conversation to delete. Format:
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/{conversation_id}`
       */
      // const name = 'abc123'
    
      // Imports the Discoveryengine library
      const {ConversationalSearchServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [ConversationalSearchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callDeleteConversation() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await discoveryengineClient.deleteConversation(request);
        console.log(response);
      }
    
      callDeleteConversation();
    
    

### deleteConversation(request, options, callback)
    
    
    deleteConversation(request: protos.google.cloud.discoveryengine.v1beta.IDeleteConversationRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.discoveryengine.v1beta.IDeleteConversationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ideleteconversationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.iempty), [protos.google.cloud.discoveryengine.v1beta.IDeleteConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ideleteconversationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConversation(request, callback)
    
    
    deleteConversation(request: protos.google.cloud.discoveryengine.v1beta.IDeleteConversationRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.discoveryengine.v1beta.IDeleteConversationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ideleteconversationrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.iempty), [protos.google.cloud.discoveryengine.v1beta.IDeleteConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ideleteconversationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSession(request, options)
    
    
    deleteSession(request?: protos.google.cloud.discoveryengine.v1beta.IDeleteSessionRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.discoveryengine.v1beta.IDeleteSessionRequest | undefined),
            {} | undefined
        ]>;

Deletes a Session.

If the to delete does not exist, a NOT_FOUND error is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ideletesessionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.iempty), ([protos.google.cloud.discoveryengine.v1beta.IDeleteSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ideletesessionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Session to delete. Format:
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/sessions/{session_id}`
       */
      // const name = 'abc123'
    
      // Imports the Discoveryengine library
      const {ConversationalSearchServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [ConversationalSearchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callDeleteSession() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await discoveryengineClient.deleteSession(request);
        console.log(response);
      }
    
      callDeleteSession();
    
    

### deleteSession(request, options, callback)
    
    
    deleteSession(request: protos.google.cloud.discoveryengine.v1beta.IDeleteSessionRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.discoveryengine.v1beta.IDeleteSessionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ideletesessionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.iempty), [protos.google.cloud.discoveryengine.v1beta.IDeleteSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ideletesessionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSession(request, callback)
    
    
    deleteSession(request: protos.google.cloud.discoveryengine.v1beta.IDeleteSessionRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.discoveryengine.v1beta.IDeleteSessionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ideletesessionrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.iempty), [protos.google.cloud.discoveryengine.v1beta.IDeleteSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ideletesessionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### enginePath(project, location, collection, engine)
    
    
    enginePath(project: string, location: string, collection: string, engine: string): string;

Return a fully-qualified engine resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### evaluationPath(project, location, evaluation)
    
    
    evaluationPath(project: string, location: string, evaluation: string): string;

Return a fully-qualified evaluation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`evaluation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### getAnswer(request, options)
    
    
    getAnswer(request?: protos.google.cloud.discoveryengine.v1beta.IGetAnswerRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1beta.IAnswer,
            protos.google.cloud.discoveryengine.v1beta.IGetAnswerRequest | undefined,
            {} | undefined
        ]>;

Gets a Answer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnswerRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetanswerrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1beta.IAnswer](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ianswer), [protos.google.cloud.discoveryengine.v1beta.IGetAnswerRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetanswerrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Answer to get. Format:
       *  `projects/{project}/locations/{location}/collections/{collection}/engines/{engine_id}/sessions/{session_id}/answers/{answer_id}`
       */
      // const name = 'abc123'
    
      // Imports the Discoveryengine library
      const {ConversationalSearchServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [ConversationalSearchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callGetAnswer() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await discoveryengineClient.getAnswer(request);
        console.log(response);
      }
    
      callGetAnswer();
    
    

### getAnswer(request, options, callback)
    
    
    getAnswer(request: protos.google.cloud.discoveryengine.v1beta.IGetAnswerRequest, options: CallOptions, callback: Callback<protos.google.cloud.discoveryengine.v1beta.IAnswer, protos.google.cloud.discoveryengine.v1beta.IGetAnswerRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnswerRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetanswerrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.IAnswer](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ianswer), [protos.google.cloud.discoveryengine.v1beta.IGetAnswerRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetanswerrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAnswer(request, callback)
    
    
    getAnswer(request: protos.google.cloud.discoveryengine.v1beta.IGetAnswerRequest, callback: Callback<protos.google.cloud.discoveryengine.v1beta.IAnswer, protos.google.cloud.discoveryengine.v1beta.IGetAnswerRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnswerRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetanswerrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.IAnswer](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ianswer), [protos.google.cloud.discoveryengine.v1beta.IGetAnswerRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetanswerrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConversation(request, options)
    
    
    getConversation(request?: protos.google.cloud.discoveryengine.v1beta.IGetConversationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1beta.IConversation,
            (protos.google.cloud.discoveryengine.v1beta.IGetConversationRequest | undefined),
            {} | undefined
        ]>;

Gets a Conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetconversationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconversation), ([protos.google.cloud.discoveryengine.v1beta.IGetConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetconversationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Conversation to get. Format:
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/{conversation_id}`
       */
      // const name = 'abc123'
    
      // Imports the Discoveryengine library
      const {ConversationalSearchServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [ConversationalSearchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callGetConversation() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await discoveryengineClient.getConversation(request);
        console.log(response);
      }
    
      callGetConversation();
    
    

### getConversation(request, options, callback)
    
    
    getConversation(request: protos.google.cloud.discoveryengine.v1beta.IGetConversationRequest, options: CallOptions, callback: Callback<protos.google.cloud.discoveryengine.v1beta.IConversation, protos.google.cloud.discoveryengine.v1beta.IGetConversationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetconversationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconversation), [protos.google.cloud.discoveryengine.v1beta.IGetConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetconversationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConversation(request, callback)
    
    
    getConversation(request: protos.google.cloud.discoveryengine.v1beta.IGetConversationRequest, callback: Callback<protos.google.cloud.discoveryengine.v1beta.IConversation, protos.google.cloud.discoveryengine.v1beta.IGetConversationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetconversationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconversation), [protos.google.cloud.discoveryengine.v1beta.IGetConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetconversationrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### getSession(request, options)
    
    
    getSession(request?: protos.google.cloud.discoveryengine.v1beta.IGetSessionRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1beta.ISession,
            protos.google.cloud.discoveryengine.v1beta.IGetSessionRequest | undefined,
            {} | undefined
        ]>;

Gets a Session.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetsessionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1beta.ISession](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.isession), [protos.google.cloud.discoveryengine.v1beta.IGetSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetsessionrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Session to get. Format:
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/sessions/{session_id}`
       */
      // const name = 'abc123'
      /**
       *  Optional. If set to true, the full session including all answer details
       *  will be returned.
       */
      // const includeAnswerDetails = true
    
      // Imports the Discoveryengine library
      const {ConversationalSearchServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [ConversationalSearchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callGetSession() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await discoveryengineClient.getSession(request);
        console.log(response);
      }
    
      callGetSession();
    
    

### getSession(request, options, callback)
    
    
    getSession(request: protos.google.cloud.discoveryengine.v1beta.IGetSessionRequest, options: CallOptions, callback: Callback<protos.google.cloud.discoveryengine.v1beta.ISession, protos.google.cloud.discoveryengine.v1beta.IGetSessionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetsessionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.ISession](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.isession), [protos.google.cloud.discoveryengine.v1beta.IGetSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetsessionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSession(request, callback)
    
    
    getSession(request: protos.google.cloud.discoveryengine.v1beta.IGetSessionRequest, callback: Callback<protos.google.cloud.discoveryengine.v1beta.ISession, protos.google.cloud.discoveryengine.v1beta.IGetSessionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetsessionrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.ISession](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.isession), [protos.google.cloud.discoveryengine.v1beta.IGetSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetsessionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### groundingConfigPath(project, location, groundingConfig)
    
    
    groundingConfigPath(project: string, location: string, groundingConfig: string): string;

Return a fully-qualified groundingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`groundingConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### identityMappingStorePath(project, location, identityMappingStore)
    
    
    identityMappingStorePath(project: string, location: string, identityMappingStore: string): string;

Return a fully-qualified identityMappingStore resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`identityMappingStore` |  `string`   
  
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
  
### licenseConfigPath(project, location, licenseConfig)
    
    
    licenseConfigPath(project: string, location: string, licenseConfig: string): string;

Return a fully-qualified licenseConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`licenseConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### listConversations(request, options)
    
    
    listConversations(request?: protos.google.cloud.discoveryengine.v1beta.IListConversationsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1beta.IConversation[],
            protos.google.cloud.discoveryengine.v1beta.IListConversationsRequest | null,
            protos.google.cloud.discoveryengine.v1beta.IListConversationsResponse
        ]>;

Lists all Conversations by their parent .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistconversationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconversation)[], [protos.google.cloud.discoveryengine.v1beta.IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistconversationsrequest) | null, [protos.google.cloud.discoveryengine.v1beta.IListConversationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistconversationsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listConversationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listConversations(request, options, callback)
    
    
    listConversations(request: protos.google.cloud.discoveryengine.v1beta.IListConversationsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.discoveryengine.v1beta.IListConversationsRequest, protos.google.cloud.discoveryengine.v1beta.IListConversationsResponse | null | undefined, protos.google.cloud.discoveryengine.v1beta.IConversation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistconversationsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.discoveryengine.v1beta.IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistconversationsrequest), [protos.google.cloud.discoveryengine.v1beta.IListConversationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistconversationsresponse) | null | undefined, [protos.google.cloud.discoveryengine.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconversation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConversations(request, callback)
    
    
    listConversations(request: protos.google.cloud.discoveryengine.v1beta.IListConversationsRequest, callback: PaginationCallback<protos.google.cloud.discoveryengine.v1beta.IListConversationsRequest, protos.google.cloud.discoveryengine.v1beta.IListConversationsResponse | null | undefined, protos.google.cloud.discoveryengine.v1beta.IConversation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistconversationsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.discoveryengine.v1beta.IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistconversationsrequest), [protos.google.cloud.discoveryengine.v1beta.IListConversationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistconversationsresponse) | null | undefined, [protos.google.cloud.discoveryengine.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconversation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConversationsAsync(request, options)
    
    
    listConversationsAsync(request?: protos.google.cloud.discoveryengine.v1beta.IListConversationsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.discoveryengine.v1beta.IConversation>;

Equivalent to `listConversations`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistconversationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.discoveryengine.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconversation)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The data store resource name. Format:
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}`
       */
      // const parent = 'abc123'
      /**
       *  Maximum number of results to return. If unspecified, defaults
       *  to 50. Max allowed value is 1000.
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous `ListConversations` call.
       *  Provide this to retrieve the subsequent page.
       */
      // const pageToken = 'abc123'
      /**
       *  A filter to apply on the list results. The supported features are:
       *  user_pseudo_id, state.
       *  Example:
       *  "user_pseudo_id = some_id"
       */
      // const filter = 'abc123'
      /**
       *  A comma-separated list of fields to order by, sorted in ascending order.
       *  Use "desc" after a field name for descending.
       *  Supported fields:
       *    * `update_time`
       *    * `create_time`
       *    * `conversation_name`
       *  Example:
       *  "update_time desc"
       *  "create_time"
       */
      // const orderBy = 'abc123'
    
      // Imports the Discoveryengine library
      const {ConversationalSearchServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [ConversationalSearchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callListConversations() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = discoveryengineClient.listConversationsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListConversations();
    
    

### listConversationsStream(request, options)
    
    
    listConversationsStream(request?: protos.google.cloud.discoveryengine.v1beta.IListConversationsRequest, options?: CallOptions): Transform;

Equivalent to `listConversations`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistconversationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listConversationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
    

### listSessions(request, options)
    
    
    listSessions(request?: protos.google.cloud.discoveryengine.v1beta.IListSessionsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1beta.ISession[],
            protos.google.cloud.discoveryengine.v1beta.IListSessionsRequest | null,
            protos.google.cloud.discoveryengine.v1beta.IListSessionsResponse
        ]>;

Lists all Sessions by their parent .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistsessionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1beta.ISession](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.isession)[], [protos.google.cloud.discoveryengine.v1beta.IListSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistsessionsrequest) | null, [protos.google.cloud.discoveryengine.v1beta.IListSessionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistsessionsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listSessionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listSessions(request, options, callback)
    
    
    listSessions(request: protos.google.cloud.discoveryengine.v1beta.IListSessionsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.discoveryengine.v1beta.IListSessionsRequest, protos.google.cloud.discoveryengine.v1beta.IListSessionsResponse | null | undefined, protos.google.cloud.discoveryengine.v1beta.ISession>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistsessionsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.discoveryengine.v1beta.IListSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistsessionsrequest), [protos.google.cloud.discoveryengine.v1beta.IListSessionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistsessionsresponse) | null | undefined, [protos.google.cloud.discoveryengine.v1beta.ISession](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.isession)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSessions(request, callback)
    
    
    listSessions(request: protos.google.cloud.discoveryengine.v1beta.IListSessionsRequest, callback: PaginationCallback<protos.google.cloud.discoveryengine.v1beta.IListSessionsRequest, protos.google.cloud.discoveryengine.v1beta.IListSessionsResponse | null | undefined, protos.google.cloud.discoveryengine.v1beta.ISession>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistsessionsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.discoveryengine.v1beta.IListSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistsessionsrequest), [protos.google.cloud.discoveryengine.v1beta.IListSessionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistsessionsresponse) | null | undefined, [protos.google.cloud.discoveryengine.v1beta.ISession](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.isession)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSessionsAsync(request, options)
    
    
    listSessionsAsync(request?: protos.google.cloud.discoveryengine.v1beta.IListSessionsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.discoveryengine.v1beta.ISession>;

Equivalent to `listSessions`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistsessionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.discoveryengine.v1beta.ISession](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.isession)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The data store resource name. Format:
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}`
       */
      // const parent = 'abc123'
      /**
       *  Maximum number of results to return. If unspecified, defaults
       *  to 50. Max allowed value is 1000.
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous `ListSessions` call.
       *  Provide this to retrieve the subsequent page.
       */
      // const pageToken = 'abc123'
      /**
       *  A comma-separated list of fields to filter by, in EBNF grammar.
       *  The supported fields are:
       *  * `user_pseudo_id`
       *  * `state`
       *  * `display_name`
       *  * `starred`
       *  * `is_pinned`
       *  * `labels`
       *  * `create_time`
       *  * `update_time`
       *  * `collaborative_project`
       *  Examples:
       *  * `user_pseudo_id = some_id`
       *  * `display_name = "some_name"`
       *  * `starred = true`
       *  * `is_pinned=true AND (NOT labels:hidden)`
       *  * `create_time > "1970-01-01T12:00:00Z"`
       *  * `collaborative_project =
       *       "projects/123/locations/global/collections/default_collection/engines/"
       *       "default_engine/collaborative_projects/cp1"`
       */
      // const filter = 'abc123'
      /**
       *  A comma-separated list of fields to order by, sorted in ascending order.
       *  Use "desc" after a field name for descending.
       *  Supported fields:
       *    * `update_time`
       *    * `create_time`
       *    * `session_name`
       *    * `is_pinned`
       *    * `display_name`
       *  Example:
       *  * `update_time desc`
       *  * `create_time`
       *  * `is_pinned desc,update_time desc`: list sessions by is_pinned first, then
       *     by update_time.
       */
      // const orderBy = 'abc123'
    
      // Imports the Discoveryengine library
      const {ConversationalSearchServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [ConversationalSearchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callListSessions() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = discoveryengineClient.listSessionsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListSessions();
    
    

### listSessionsStream(request, options)
    
    
    listSessionsStream(request?: protos.google.cloud.discoveryengine.v1beta.IListSessionsRequest, options?: CallOptions): Transform;

Equivalent to `listSessions`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistsessionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listSessionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### matchAnswerFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchAnswerFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the answer from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the answer.  
  
### matchAnswerFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchAnswerFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the answer from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the answer.  
  
### matchAnswerFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName)
    
    
    matchAnswerFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName: string): string | number;

Parse the answer from ProjectLocationDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the answer.  
  
### matchAssistAnswerFromAssistAnswerName(assistAnswerName)
    
    
    matchAssistAnswerFromAssistAnswerName(assistAnswerName: string): string | number;

Parse the assist_answer from AssistAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`assistAnswerName` |  `string`   
A fully-qualified path representing AssistAnswer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the assist_answer.  
  
### matchAssistantFromAssistantName(assistantName)
    
    
    matchAssistantFromAssistantName(assistantName: string): string | number;

Parse the assistant from Assistant resource.

**Parameter**  
---  
**Name** | **Description**  
`assistantName` |  `string`   
A fully-qualified path representing Assistant resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the assistant.  
  
### matchBranchFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchBranchFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the branch from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchBranchFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchBranchFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the branch from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchBranchFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchBranchFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the branch from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchBranchFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName)
    
    
    matchBranchFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName: string): string | number;

Parse the branch from ProjectLocationDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchChunkFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchChunkFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the chunk from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the chunk.  
  
### matchChunkFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchChunkFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the chunk from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the chunk.  
  
### matchCmekConfigFromProjectLocationCmekConfigsName(projectLocationCmekConfigsName)
    
    
    matchCmekConfigFromProjectLocationCmekConfigsName(projectLocationCmekConfigsName: string): string | number;

Parse the cmek_config from ProjectLocationCmekConfigs resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCmekConfigsName` |  `string`   
A fully-qualified path representing project_location_cmekConfigs resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the cmek_config.  
  
### matchCollaborativeProjectFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName)
    
    
    matchCollaborativeProjectFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName: string): string | number;

Parse the collaborative_project from ProjectLocationCollectionEngineCollaborativeProjectSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineCollaborativeProjectSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_collaborative_project_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collaborative_project.  
  
### matchCollectionFromAssistAnswerName(assistAnswerName)
    
    
    matchCollectionFromAssistAnswerName(assistAnswerName: string): string | number;

Parse the collection from AssistAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`assistAnswerName` |  `string`   
A fully-qualified path representing AssistAnswer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromAssistantName(assistantName)
    
    
    matchCollectionFromAssistantName(assistantName: string): string | number;

Parse the collection from Assistant resource.

**Parameter**  
---  
**Name** | **Description**  
`assistantName` |  `string`   
A fully-qualified path representing Assistant resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromEngineName(engineName)
    
    
    matchCollectionFromEngineName(engineName: string): string | number;

Parse the collection from Engine resource.

**Parameter**  
---  
**Name** | **Description**  
`engineName` |  `string`   
A fully-qualified path representing Engine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
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
  
### matchCollectionFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreSiteSearchEngineSitemapName(projectLocationCollectionDataStoreSiteSearchEngineSitemapName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSiteSearchEngineSitemapName(projectLocationCollectionDataStoreSiteSearchEngineSitemapName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSiteSearchEngineSitemap resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineSitemapName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_sitemap resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName)
    
    
    matchCollectionFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineCollaborativeProjectSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineCollaborativeProjectSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_collaborative_project_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName)
    
    
    matchCollectionFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineControlName` |  `string`   
A fully-qualified path representing project_location_collection_engine_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName)
    
    
    matchCollectionFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineConversationName` |  `string`   
A fully-qualified path representing project_location_collection_engine_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName)
    
    
    matchCollectionFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_engine_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchCollectionFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName)
    
    
    matchCollectionFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchControlFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName)
    
    
    matchControlFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName: string): string | number;

Parse the control from ProjectLocationCollectionDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the control.  
  
### matchControlFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName)
    
    
    matchControlFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName: string): string | number;

Parse the control from ProjectLocationCollectionEngineControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineControlName` |  `string`   
A fully-qualified path representing project_location_collection_engine_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the control.  
  
### matchControlFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName)
    
    
    matchControlFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName: string): string | number;

Parse the control from ProjectLocationDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the control.  
  
### matchConversationFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName)
    
    
    matchConversationFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName: string): string | number;

Parse the conversation from ProjectLocationCollectionDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversation.  
  
### matchConversationFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName)
    
    
    matchConversationFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName: string): string | number;

Parse the conversation from ProjectLocationCollectionEngineConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineConversationName` |  `string`   
A fully-qualified path representing project_location_collection_engine_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversation.  
  
### matchConversationFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName)
    
    
    matchConversationFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName: string): string | number;

Parse the conversation from ProjectLocationDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversation.  
  
### matchCustomTuningModelFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName)
    
    
    matchCustomTuningModelFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName: string): string | number;

Parse the custom_tuning_model from ProjectLocationCollectionDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the custom_tuning_model.  
  
### matchCustomTuningModelFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName)
    
    
    matchCustomTuningModelFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName: string): string | number;

Parse the custom_tuning_model from ProjectLocationDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the custom_tuning_model.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
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
  
### matchDataStoreFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreSiteSearchEngineSitemapName(projectLocationCollectionDataStoreSiteSearchEngineSitemapName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSiteSearchEngineSitemapName(projectLocationCollectionDataStoreSiteSearchEngineSitemapName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSiteSearchEngineSitemap resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineSitemapName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_sitemap resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchDataStoreFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the data_store from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName)
    
    
    matchDataStoreFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName: string): string | number;

Parse the data_store from ProjectLocationDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName)
    
    
    matchDataStoreFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName: string): string | number;

Parse the data_store from ProjectLocationDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName)
    
    
    matchDataStoreFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName: string): string | number;

Parse the data_store from ProjectLocationDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName)
    
    
    matchDataStoreFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName: string): string | number;

Parse the data_store from ProjectLocationDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName)
    
    
    matchDataStoreFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName: string): string | number;

Parse the data_store from ProjectLocationDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_documentProcessingConfig resource.  
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
  
### matchDataStoreFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName)
    
    
    matchDataStoreFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName)
    
    
    matchDataStoreFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName: string): string | number;

Parse the data_store from ProjectLocationDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName)
    
    
    matchDataStoreFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName)
    
    
    matchDataStoreFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName)
    
    
    matchDataStoreFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreSiteSearchEngineSitemapName(projectLocationDataStoreSiteSearchEngineSitemapName)
    
    
    matchDataStoreFromProjectLocationDataStoreSiteSearchEngineSitemapName(projectLocationDataStoreSiteSearchEngineSitemapName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSiteSearchEngineSitemap resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineSitemapName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_sitemap resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchDataStoreFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDocumentFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchDocumentFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the document from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchDocumentFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchDocumentFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the document from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchDocumentFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchDocumentFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the document from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchDocumentFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName)
    
    
    matchDocumentFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName: string): string | number;

Parse the document from ProjectLocationDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchEngineFromAssistAnswerName(assistAnswerName)
    
    
    matchEngineFromAssistAnswerName(assistAnswerName: string): string | number;

Parse the engine from AssistAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`assistAnswerName` |  `string`   
A fully-qualified path representing AssistAnswer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromAssistantName(assistantName)
    
    
    matchEngineFromAssistantName(assistantName: string): string | number;

Parse the engine from Assistant resource.

**Parameter**  
---  
**Name** | **Description**  
`assistantName` |  `string`   
A fully-qualified path representing Assistant resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromEngineName(engineName)
    
    
    matchEngineFromEngineName(engineName: string): string | number;

Parse the engine from Engine resource.

**Parameter**  
---  
**Name** | **Description**  
`engineName` |  `string`   
A fully-qualified path representing Engine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName)
    
    
    matchEngineFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineCollaborativeProjectSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineCollaborativeProjectSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_collaborative_project_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName)
    
    
    matchEngineFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineControlName` |  `string`   
A fully-qualified path representing project_location_collection_engine_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName)
    
    
    matchEngineFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineConversationName` |  `string`   
A fully-qualified path representing project_location_collection_engine_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName)
    
    
    matchEngineFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_engine_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchEngineFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName)
    
    
    matchEngineFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
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
  
### matchGroundingConfigFromGroundingConfigName(groundingConfigName)
    
    
    matchGroundingConfigFromGroundingConfigName(groundingConfigName: string): string | number;

Parse the grounding_config from GroundingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`groundingConfigName` |  `string`   
A fully-qualified path representing GroundingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the grounding_config.  
  
### matchIdentityMappingStoreFromIdentityMappingStoreName(identityMappingStoreName)
    
    
    matchIdentityMappingStoreFromIdentityMappingStoreName(identityMappingStoreName: string): string | number;

Parse the identity_mapping_store from IdentityMappingStore resource.

**Parameter**  
---  
**Name** | **Description**  
`identityMappingStoreName` |  `string`   
A fully-qualified path representing IdentityMappingStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the identity_mapping_store.  
  
### matchLicenseConfigFromLicenseConfigName(licenseConfigName)
    
    
    matchLicenseConfigFromLicenseConfigName(licenseConfigName: string): string | number;

Parse the license_config from LicenseConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`licenseConfigName` |  `string`   
A fully-qualified path representing LicenseConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the license_config.  
  
### matchLocationFromAclConfigName(aclConfigName)
    
    
    matchLocationFromAclConfigName(aclConfigName: string): string | number;

Parse the location from AclConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`aclConfigName` |  `string`   
A fully-qualified path representing AclConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromAssistAnswerName(assistAnswerName)
    
    
    matchLocationFromAssistAnswerName(assistAnswerName: string): string | number;

Parse the location from AssistAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`assistAnswerName` |  `string`   
A fully-qualified path representing AssistAnswer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromAssistantName(assistantName)
    
    
    matchLocationFromAssistantName(assistantName: string): string | number;

Parse the location from Assistant resource.

**Parameter**  
---  
**Name** | **Description**  
`assistantName` |  `string`   
A fully-qualified path representing Assistant resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromEngineName(engineName)
    
    
    matchLocationFromEngineName(engineName: string): string | number;

Parse the location from Engine resource.

**Parameter**  
---  
**Name** | **Description**  
`engineName` |  `string`   
A fully-qualified path representing Engine resource.  
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
  
### matchLocationFromGroundingConfigName(groundingConfigName)
    
    
    matchLocationFromGroundingConfigName(groundingConfigName: string): string | number;

Parse the location from GroundingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`groundingConfigName` |  `string`   
A fully-qualified path representing GroundingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromIdentityMappingStoreName(identityMappingStoreName)
    
    
    matchLocationFromIdentityMappingStoreName(identityMappingStoreName: string): string | number;

Parse the location from IdentityMappingStore resource.

**Parameter**  
---  
**Name** | **Description**  
`identityMappingStoreName` |  `string`   
A fully-qualified path representing IdentityMappingStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromLicenseConfigName(licenseConfigName)
    
    
    matchLocationFromLicenseConfigName(licenseConfigName: string): string | number;

Parse the location from LicenseConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`licenseConfigName` |  `string`   
A fully-qualified path representing LicenseConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCmekConfigName(projectLocationCmekConfigName)
    
    
    matchLocationFromProjectLocationCmekConfigName(projectLocationCmekConfigName: string): string | number;

Parse the location from ProjectLocationCmekConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCmekConfigName` |  `string`   
A fully-qualified path representing project_location_cmekConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCmekConfigsName(projectLocationCmekConfigsName)
    
    
    matchLocationFromProjectLocationCmekConfigsName(projectLocationCmekConfigsName: string): string | number;

Parse the location from ProjectLocationCmekConfigs resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCmekConfigsName` |  `string`   
A fully-qualified path representing project_location_cmekConfigs resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_documentProcessingConfig resource.  
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
  
### matchLocationFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreSiteSearchEngineSitemapName(projectLocationCollectionDataStoreSiteSearchEngineSitemapName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSiteSearchEngineSitemapName(projectLocationCollectionDataStoreSiteSearchEngineSitemapName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSiteSearchEngineSitemap resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineSitemapName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_sitemap resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName)
    
    
    matchLocationFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName: string): string | number;

Parse the location from ProjectLocationCollectionEngineCollaborativeProjectSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineCollaborativeProjectSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_collaborative_project_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName)
    
    
    matchLocationFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName: string): string | number;

Parse the location from ProjectLocationCollectionEngineControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineControlName` |  `string`   
A fully-qualified path representing project_location_collection_engine_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName)
    
    
    matchLocationFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName: string): string | number;

Parse the location from ProjectLocationCollectionEngineConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineConversationName` |  `string`   
A fully-qualified path representing project_location_collection_engine_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName)
    
    
    matchLocationFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName: string): string | number;

Parse the location from ProjectLocationCollectionEngineServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_engine_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchLocationFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the location from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName)
    
    
    matchLocationFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName: string): string | number;

Parse the location from ProjectLocationCollectionEngineSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchLocationFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the location from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName)
    
    
    matchLocationFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName: string): string | number;

Parse the location from ProjectLocationDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName)
    
    
    matchLocationFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName: string): string | number;

Parse the location from ProjectLocationDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName)
    
    
    matchLocationFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName: string): string | number;

Parse the location from ProjectLocationDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName)
    
    
    matchLocationFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName: string): string | number;

Parse the location from ProjectLocationDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName)
    
    
    matchLocationFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName: string): string | number;

Parse the location from ProjectLocationDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_documentProcessingConfig resource.  
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
  
### matchLocationFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName)
    
    
    matchLocationFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName: string): string | number;

Parse the location from ProjectLocationDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName)
    
    
    matchLocationFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName: string): string | number;

Parse the location from ProjectLocationDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName)
    
    
    matchLocationFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName: string): string | number;

Parse the location from ProjectLocationDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName)
    
    
    matchLocationFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName: string): string | number;

Parse the location from ProjectLocationDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName)
    
    
    matchLocationFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName: string): string | number;

Parse the location from ProjectLocationDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreSiteSearchEngineSitemapName(projectLocationDataStoreSiteSearchEngineSitemapName)
    
    
    matchLocationFromProjectLocationDataStoreSiteSearchEngineSitemapName(projectLocationDataStoreSiteSearchEngineSitemapName: string): string | number;

Parse the location from ProjectLocationDataStoreSiteSearchEngineSitemap resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineSitemapName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_sitemap resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchLocationFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the location from ProjectLocationDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSampleQueryName(sampleQueryName)
    
    
    matchLocationFromSampleQueryName(sampleQueryName: string): string | number;

Parse the location from SampleQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQueryName` |  `string`   
A fully-qualified path representing SampleQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSampleQuerySetName(sampleQuerySetName)
    
    
    matchLocationFromSampleQuerySetName(sampleQuerySetName: string): string | number;

Parse the location from SampleQuerySet resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQuerySetName` |  `string`   
A fully-qualified path representing SampleQuerySet resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromUserStoreName(userStoreName)
    
    
    matchLocationFromUserStoreName(userStoreName: string): string | number;

Parse the location from UserStore resource.

**Parameter**  
---  
**Name** | **Description**  
`userStoreName` |  `string`   
A fully-qualified path representing UserStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchProjectFromAclConfigName(aclConfigName)
    
    
    matchProjectFromAclConfigName(aclConfigName: string): string | number;

Parse the project from AclConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`aclConfigName` |  `string`   
A fully-qualified path representing AclConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromAssistAnswerName(assistAnswerName)
    
    
    matchProjectFromAssistAnswerName(assistAnswerName: string): string | number;

Parse the project from AssistAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`assistAnswerName` |  `string`   
A fully-qualified path representing AssistAnswer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromAssistantName(assistantName)
    
    
    matchProjectFromAssistantName(assistantName: string): string | number;

Parse the project from Assistant resource.

**Parameter**  
---  
**Name** | **Description**  
`assistantName` |  `string`   
A fully-qualified path representing Assistant resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromEngineName(engineName)
    
    
    matchProjectFromEngineName(engineName: string): string | number;

Parse the project from Engine resource.

**Parameter**  
---  
**Name** | **Description**  
`engineName` |  `string`   
A fully-qualified path representing Engine resource.  
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
  
### matchProjectFromGroundingConfigName(groundingConfigName)
    
    
    matchProjectFromGroundingConfigName(groundingConfigName: string): string | number;

Parse the project from GroundingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`groundingConfigName` |  `string`   
A fully-qualified path representing GroundingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromIdentityMappingStoreName(identityMappingStoreName)
    
    
    matchProjectFromIdentityMappingStoreName(identityMappingStoreName: string): string | number;

Parse the project from IdentityMappingStore resource.

**Parameter**  
---  
**Name** | **Description**  
`identityMappingStoreName` |  `string`   
A fully-qualified path representing IdentityMappingStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromLicenseConfigName(licenseConfigName)
    
    
    matchProjectFromLicenseConfigName(licenseConfigName: string): string | number;

Parse the project from LicenseConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`licenseConfigName` |  `string`   
A fully-qualified path representing LicenseConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCmekConfigName(projectLocationCmekConfigName)
    
    
    matchProjectFromProjectLocationCmekConfigName(projectLocationCmekConfigName: string): string | number;

Parse the project from ProjectLocationCmekConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCmekConfigName` |  `string`   
A fully-qualified path representing project_location_cmekConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCmekConfigsName(projectLocationCmekConfigsName)
    
    
    matchProjectFromProjectLocationCmekConfigsName(projectLocationCmekConfigsName: string): string | number;

Parse the project from ProjectLocationCmekConfigs resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCmekConfigsName` |  `string`   
A fully-qualified path representing project_location_cmekConfigs resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_documentProcessingConfig resource.  
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
  
### matchProjectFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreSiteSearchEngineSitemapName(projectLocationCollectionDataStoreSiteSearchEngineSitemapName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSiteSearchEngineSitemapName(projectLocationCollectionDataStoreSiteSearchEngineSitemapName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSiteSearchEngineSitemap resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineSitemapName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_sitemap resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName)
    
    
    matchProjectFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName: string): string | number;

Parse the project from ProjectLocationCollectionEngineCollaborativeProjectSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineCollaborativeProjectSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_collaborative_project_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName)
    
    
    matchProjectFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName: string): string | number;

Parse the project from ProjectLocationCollectionEngineControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineControlName` |  `string`   
A fully-qualified path representing project_location_collection_engine_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName)
    
    
    matchProjectFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName: string): string | number;

Parse the project from ProjectLocationCollectionEngineConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineConversationName` |  `string`   
A fully-qualified path representing project_location_collection_engine_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName)
    
    
    matchProjectFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName: string): string | number;

Parse the project from ProjectLocationCollectionEngineServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_engine_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchProjectFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the project from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName)
    
    
    matchProjectFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName: string): string | number;

Parse the project from ProjectLocationCollectionEngineSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchProjectFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the project from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName)
    
    
    matchProjectFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName: string): string | number;

Parse the project from ProjectLocationDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName)
    
    
    matchProjectFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName: string): string | number;

Parse the project from ProjectLocationDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName)
    
    
    matchProjectFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName: string): string | number;

Parse the project from ProjectLocationDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName)
    
    
    matchProjectFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName: string): string | number;

Parse the project from ProjectLocationDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName)
    
    
    matchProjectFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName: string): string | number;

Parse the project from ProjectLocationDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_documentProcessingConfig resource.  
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
  
### matchProjectFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName)
    
    
    matchProjectFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName: string): string | number;

Parse the project from ProjectLocationDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName)
    
    
    matchProjectFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName: string): string | number;

Parse the project from ProjectLocationDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName)
    
    
    matchProjectFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName: string): string | number;

Parse the project from ProjectLocationDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName)
    
    
    matchProjectFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName: string): string | number;

Parse the project from ProjectLocationDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName)
    
    
    matchProjectFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName: string): string | number;

Parse the project from ProjectLocationDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreSiteSearchEngineSitemapName(projectLocationDataStoreSiteSearchEngineSitemapName)
    
    
    matchProjectFromProjectLocationDataStoreSiteSearchEngineSitemapName(projectLocationDataStoreSiteSearchEngineSitemapName: string): string | number;

Parse the project from ProjectLocationDataStoreSiteSearchEngineSitemap resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineSitemapName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_sitemap resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchProjectFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the project from ProjectLocationDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_target_site resource.  
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
  
### matchProjectFromSampleQueryName(sampleQueryName)
    
    
    matchProjectFromSampleQueryName(sampleQueryName: string): string | number;

Parse the project from SampleQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQueryName` |  `string`   
A fully-qualified path representing SampleQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSampleQuerySetName(sampleQuerySetName)
    
    
    matchProjectFromSampleQuerySetName(sampleQuerySetName: string): string | number;

Parse the project from SampleQuerySet resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQuerySetName` |  `string`   
A fully-qualified path representing SampleQuerySet resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromUserStoreName(userStoreName)
    
    
    matchProjectFromUserStoreName(userStoreName: string): string | number;

Parse the project from UserStore resource.

**Parameter**  
---  
**Name** | **Description**  
`userStoreName` |  `string`   
A fully-qualified path representing UserStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchSampleQueryFromSampleQueryName(sampleQueryName)
    
    
    matchSampleQueryFromSampleQueryName(sampleQueryName: string): string | number;

Parse the sample_query from SampleQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQueryName` |  `string`   
A fully-qualified path representing SampleQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sample_query.  
  
### matchSampleQuerySetFromSampleQueryName(sampleQueryName)
    
    
    matchSampleQuerySetFromSampleQueryName(sampleQueryName: string): string | number;

Parse the sample_query_set from SampleQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQueryName` |  `string`   
A fully-qualified path representing SampleQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sample_query_set.  
  
### matchSampleQuerySetFromSampleQuerySetName(sampleQuerySetName)
    
    
    matchSampleQuerySetFromSampleQuerySetName(sampleQuerySetName: string): string | number;

Parse the sample_query_set from SampleQuerySet resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQuerySetName` |  `string`   
A fully-qualified path representing SampleQuerySet resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sample_query_set.  
  
### matchSchemaFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName)
    
    
    matchSchemaFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName: string): string | number;

Parse the schema from ProjectLocationCollectionDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the schema.  
  
### matchSchemaFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName)
    
    
    matchSchemaFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName: string): string | number;

Parse the schema from ProjectLocationDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the schema.  
  
### matchServingConfigFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName)
    
    
    matchServingConfigFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName: string): string | number;

Parse the serving_config from ProjectLocationCollectionDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the serving_config.  
  
### matchServingConfigFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName)
    
    
    matchServingConfigFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName: string): string | number;

Parse the serving_config from ProjectLocationCollectionEngineServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_engine_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the serving_config.  
  
### matchServingConfigFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName)
    
    
    matchServingConfigFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName: string): string | number;

Parse the serving_config from ProjectLocationDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the serving_config.  
  
### matchSessionFromAssistAnswerName(assistAnswerName)
    
    
    matchSessionFromAssistAnswerName(assistAnswerName: string): string | number;

Parse the session from AssistAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`assistAnswerName` |  `string`   
A fully-qualified path representing AssistAnswer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchSessionFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the session from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName)
    
    
    matchSessionFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName: string): string | number;

Parse the session from ProjectLocationCollectionDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName)
    
    
    matchSessionFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName: string): string | number;

Parse the session from ProjectLocationCollectionEngineCollaborativeProjectSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineCollaborativeProjectSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_collaborative_project_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchSessionFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the session from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName)
    
    
    matchSessionFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName: string): string | number;

Parse the session from ProjectLocationCollectionEngineSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName)
    
    
    matchSessionFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName: string): string | number;

Parse the session from ProjectLocationDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName)
    
    
    matchSessionFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName: string): string | number;

Parse the session from ProjectLocationDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSitemapFromProjectLocationCollectionDataStoreSiteSearchEngineSitemapName(projectLocationCollectionDataStoreSiteSearchEngineSitemapName)
    
    
    matchSitemapFromProjectLocationCollectionDataStoreSiteSearchEngineSitemapName(projectLocationCollectionDataStoreSiteSearchEngineSitemapName: string): string | number;

Parse the sitemap from ProjectLocationCollectionDataStoreSiteSearchEngineSitemap resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineSitemapName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_sitemap resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sitemap.  
  
### matchSitemapFromProjectLocationDataStoreSiteSearchEngineSitemapName(projectLocationDataStoreSiteSearchEngineSitemapName)
    
    
    matchSitemapFromProjectLocationDataStoreSiteSearchEngineSitemapName(projectLocationDataStoreSiteSearchEngineSitemapName: string): string | number;

Parse the sitemap from ProjectLocationDataStoreSiteSearchEngineSitemap resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineSitemapName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_sitemap resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sitemap.  
  
### matchTargetSiteFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchTargetSiteFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the target_site from ProjectLocationCollectionDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the target_site.  
  
### matchTargetSiteFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchTargetSiteFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the target_site from ProjectLocationDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the target_site.  
  
### matchUserStoreFromUserStoreName(userStoreName)
    
    
    matchUserStoreFromUserStoreName(userStoreName: string): string | number;

Parse the user_store from UserStore resource.

**Parameter**  
---  
**Name** | **Description**  
`userStoreName` |  `string`   
A fully-qualified path representing UserStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the user_store.  
  
### projectLocationCmekConfigPath(project, location)
    
    
    projectLocationCmekConfigPath(project: string, location: string): string;

Return a fully-qualified projectLocationCmekConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCmekConfigsPath(project, location, cmekConfig)
    
    
    projectLocationCmekConfigsPath(project: string, location: string, cmekConfig: string): string;

Return a fully-qualified projectLocationCmekConfigs resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`cmekConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreBranchDocumentChunkPath(project, location, collection, dataStore, branch, document, chunk)
    
    
    projectLocationCollectionDataStoreBranchDocumentChunkPath(project: string, location: string, collection: string, dataStore: string, branch: string, document: string, chunk: string): string;

Return a fully-qualified projectLocationCollectionDataStoreBranchDocumentChunk resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`branch` |  `string`   
  
`document` |  `string`   
  
`chunk` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreBranchDocumentPath(project, location, collection, dataStore, branch, document)
    
    
    projectLocationCollectionDataStoreBranchDocumentPath(project: string, location: string, collection: string, dataStore: string, branch: string, document: string): string;

Return a fully-qualified projectLocationCollectionDataStoreBranchDocument resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`branch` |  `string`   
  
`document` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreControlPath(project, location, collection, dataStore, control)
    
    
    projectLocationCollectionDataStoreControlPath(project: string, location: string, collection: string, dataStore: string, control: string): string;

Return a fully-qualified projectLocationCollectionDataStoreControl resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`control` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreConversationPath(project, location, collection, dataStore, conversation)
    
    
    projectLocationCollectionDataStoreConversationPath(project: string, location: string, collection: string, dataStore: string, conversation: string): string;

Return a fully-qualified projectLocationCollectionDataStoreConversation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`conversation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreCustomTuningModelPath(project, location, collection, dataStore, customTuningModel)
    
    
    projectLocationCollectionDataStoreCustomTuningModelPath(project: string, location: string, collection: string, dataStore: string, customTuningModel: string): string;

Return a fully-qualified projectLocationCollectionDataStoreCustomTuningModel resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`customTuningModel` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreDocumentProcessingConfigPath(project, location, collection, dataStore)
    
    
    projectLocationCollectionDataStoreDocumentProcessingConfigPath(project: string, location: string, collection: string, dataStore: string): string;

Return a fully-qualified projectLocationCollectionDataStoreDocumentProcessingConfig resource name string.

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
  
### projectLocationCollectionDataStoreSchemaPath(project, location, collection, dataStore, schema)
    
    
    projectLocationCollectionDataStoreSchemaPath(project: string, location: string, collection: string, dataStore: string, schema: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSchema resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`schema` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreServingConfigPath(project, location, collection, dataStore, servingConfig)
    
    
    projectLocationCollectionDataStoreServingConfigPath(project: string, location: string, collection: string, dataStore: string, servingConfig: string): string;

Return a fully-qualified projectLocationCollectionDataStoreServingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`servingConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreSessionAnswerPath(project, location, collection, dataStore, session, answer)
    
    
    projectLocationCollectionDataStoreSessionAnswerPath(project: string, location: string, collection: string, dataStore: string, session: string, answer: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSessionAnswer resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`session` |  `string`   
  
`answer` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreSessionsPath(project, location, collection, dataStore, session)
    
    
    projectLocationCollectionDataStoreSessionsPath(project: string, location: string, collection: string, dataStore: string, session: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSessions resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`session` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreSiteSearchEnginePath(project, location, collection, dataStore)
    
    
    projectLocationCollectionDataStoreSiteSearchEnginePath(project: string, location: string, collection: string, dataStore: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSiteSearchEngine resource name string.

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
  
### projectLocationCollectionDataStoreSiteSearchEngineSitemapPath(project, location, collection, dataStore, sitemap)
    
    
    projectLocationCollectionDataStoreSiteSearchEngineSitemapPath(project: string, location: string, collection: string, dataStore: string, sitemap: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSiteSearchEngineSitemap resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`sitemap` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreSiteSearchEngineTargetSitePath(project, location, collection, dataStore, targetSite)
    
    
    projectLocationCollectionDataStoreSiteSearchEngineTargetSitePath(project: string, location: string, collection: string, dataStore: string, targetSite: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSiteSearchEngineTargetSite resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`targetSite` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionEngineCollaborativeProjectSessionsPath(project, location, collection, engine, collaborativeProject, session)
    
    
    projectLocationCollectionEngineCollaborativeProjectSessionsPath(project: string, location: string, collection: string, engine: string, collaborativeProject: string, session: string): string;

Return a fully-qualified projectLocationCollectionEngineCollaborativeProjectSessions resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`collaborativeProject` |  `string`   
  
`session` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionEngineControlPath(project, location, collection, engine, control)
    
    
    projectLocationCollectionEngineControlPath(project: string, location: string, collection: string, engine: string, control: string): string;

Return a fully-qualified projectLocationCollectionEngineControl resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`control` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionEngineConversationPath(project, location, collection, engine, conversation)
    
    
    projectLocationCollectionEngineConversationPath(project: string, location: string, collection: string, engine: string, conversation: string): string;

Return a fully-qualified projectLocationCollectionEngineConversation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`conversation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionEngineServingConfigPath(project, location, collection, engine, servingConfig)
    
    
    projectLocationCollectionEngineServingConfigPath(project: string, location: string, collection: string, engine: string, servingConfig: string): string;

Return a fully-qualified projectLocationCollectionEngineServingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`servingConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionEngineSessionAnswerPath(project, location, collection, engine, session, answer)
    
    
    projectLocationCollectionEngineSessionAnswerPath(project: string, location: string, collection: string, engine: string, session: string, answer: string): string;

Return a fully-qualified projectLocationCollectionEngineSessionAnswer resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`session` |  `string`   
  
`answer` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionEngineSessionsPath(project, location, collection, engine, session)
    
    
    projectLocationCollectionEngineSessionsPath(project: string, location: string, collection: string, engine: string, session: string): string;

Return a fully-qualified projectLocationCollectionEngineSessions resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`session` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreBranchDocumentChunkPath(project, location, dataStore, branch, document, chunk)
    
    
    projectLocationDataStoreBranchDocumentChunkPath(project: string, location: string, dataStore: string, branch: string, document: string, chunk: string): string;

Return a fully-qualified projectLocationDataStoreBranchDocumentChunk resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`branch` |  `string`   
  
`document` |  `string`   
  
`chunk` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreBranchDocumentPath(project, location, dataStore, branch, document)
    
    
    projectLocationDataStoreBranchDocumentPath(project: string, location: string, dataStore: string, branch: string, document: string): string;

Return a fully-qualified projectLocationDataStoreBranchDocument resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`branch` |  `string`   
  
`document` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreControlPath(project, location, dataStore, control)
    
    
    projectLocationDataStoreControlPath(project: string, location: string, dataStore: string, control: string): string;

Return a fully-qualified projectLocationDataStoreControl resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`control` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreConversationPath(project, location, dataStore, conversation)
    
    
    projectLocationDataStoreConversationPath(project: string, location: string, dataStore: string, conversation: string): string;

Return a fully-qualified projectLocationDataStoreConversation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`conversation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreCustomTuningModelPath(project, location, dataStore, customTuningModel)
    
    
    projectLocationDataStoreCustomTuningModelPath(project: string, location: string, dataStore: string, customTuningModel: string): string;

Return a fully-qualified projectLocationDataStoreCustomTuningModel resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`customTuningModel` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreDocumentProcessingConfigPath(project, location, dataStore)
    
    
    projectLocationDataStoreDocumentProcessingConfigPath(project: string, location: string, dataStore: string): string;

Return a fully-qualified projectLocationDataStoreDocumentProcessingConfig resource name string.

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
  
### projectLocationDataStoreSchemaPath(project, location, dataStore, schema)
    
    
    projectLocationDataStoreSchemaPath(project: string, location: string, dataStore: string, schema: string): string;

Return a fully-qualified projectLocationDataStoreSchema resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`schema` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreServingConfigPath(project, location, dataStore, servingConfig)
    
    
    projectLocationDataStoreServingConfigPath(project: string, location: string, dataStore: string, servingConfig: string): string;

Return a fully-qualified projectLocationDataStoreServingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`servingConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreSessionAnswerPath(project, location, dataStore, session, answer)
    
    
    projectLocationDataStoreSessionAnswerPath(project: string, location: string, dataStore: string, session: string, answer: string): string;

Return a fully-qualified projectLocationDataStoreSessionAnswer resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`session` |  `string`   
  
`answer` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreSessionsPath(project, location, dataStore, session)
    
    
    projectLocationDataStoreSessionsPath(project: string, location: string, dataStore: string, session: string): string;

Return a fully-qualified projectLocationDataStoreSessions resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`session` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreSiteSearchEnginePath(project, location, dataStore)
    
    
    projectLocationDataStoreSiteSearchEnginePath(project: string, location: string, dataStore: string): string;

Return a fully-qualified projectLocationDataStoreSiteSearchEngine resource name string.

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
  
### projectLocationDataStoreSiteSearchEngineSitemapPath(project, location, dataStore, sitemap)
    
    
    projectLocationDataStoreSiteSearchEngineSitemapPath(project: string, location: string, dataStore: string, sitemap: string): string;

Return a fully-qualified projectLocationDataStoreSiteSearchEngineSitemap resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`sitemap` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreSiteSearchEngineTargetSitePath(project, location, dataStore, targetSite)
    
    
    projectLocationDataStoreSiteSearchEngineTargetSitePath(project: string, location: string, dataStore: string, targetSite: string): string;

Return a fully-qualified projectLocationDataStoreSiteSearchEngineTargetSite resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`targetSite` |  `string`   
  
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
  
### sampleQueryPath(project, location, sampleQuerySet, sampleQuery)
    
    
    sampleQueryPath(project: string, location: string, sampleQuerySet: string, sampleQuery: string): string;

Return a fully-qualified sampleQuery resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`sampleQuerySet` |  `string`   
  
`sampleQuery` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### sampleQuerySetPath(project, location, sampleQuerySet)
    
    
    sampleQuerySetPath(project: string, location: string, sampleQuerySet: string): string;

Return a fully-qualified sampleQuerySet resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`sampleQuerySet` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### streamAnswerQuery(request, options)
    
    
    streamAnswerQuery(request?: protos.google.cloud.discoveryengine.v1beta.IAnswerQueryRequest, options?: CallOptions): gax.CancellableStream;

Answer query method (streaming).

It takes one and returns multiple [AnswerQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.answerqueryresponse) messages in a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnswerQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ianswerqueryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`gax.CancellableStream` | {Stream} An object stream which emits [AnswerQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.answerqueryresponse) on 'data' event. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#server-streaming) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Search serving config, such as
       *  `projects/* /locations/global/collections/default_collection/engines/* /servingConfigs/default_serving_config`,
       *  or
       *  `projects/* /locations/global/collections/default_collection/dataStores/* /servingConfigs/default_serving_config`.
       *  Or the resource name of the agent engine serving config, such as:
       *  `projects/* /locations/global/collections/default_collection/engines/* /servingConfigs/default_agent_answer`.
       *  (use when `enable_agent_invocation` set to true, and you have custom
       *  `AI_MODE` agent engine configured)
       *  This field is used to identify the serving configuration name, set
       *  of models used to make the search.
       */
      // const servingConfig = 'abc123'
      /**
       *  Required. Current user query.
       */
      // const query = {}
      /**
       *  The session resource name. Not required.
       *  When session field is not set, the API is in sessionless mode.
       *  We support auto session mode: users can use the wildcard symbol `-` as
       *  session ID.  A new ID will be automatically generated and assigned.
       */
      // const session = 'abc123'
      /**
       *  Model specification.
       */
      // const safetySpec = {}
      /**
       *  Related questions specification.
       */
      // const relatedQuestionsSpec = {}
      /**
       *  Optional. Grounding specification.
       */
      // const groundingSpec = {}
      /**
       *  Answer generation specification.
       */
      // const answerGenerationSpec = {}
      /**
       *  Search specification.
       */
      // const searchSpec = {}
      /**
       *  Query understanding specification.
       */
      // const queryUnderstandingSpec = {}
      /**
       *  A unique identifier for tracking visitors. For example, this could be
       *  implemented with an HTTP cookie, which should be able to uniquely identify
       *  a visitor on a single device. This unique identifier should not change if
       *  the visitor logs in or out of the website.
       *  This field should NOT have a fixed value such as `unknown_visitor`.
       *  The field must be a UTF-8 encoded string with a length limit of 128
       *  characters. Otherwise, an  `INVALID_ARGUMENT`  error is returned.
       */
      // const userPseudoId = 'abc123'
      /**
       *  The user labels applied to a resource must meet the following requirements:
       *  * Each resource can have multiple labels, up to a maximum of 64.
       *  * Each label must be a key-value pair.
       *  * Keys have a minimum length of 1 character and a maximum length of 63
       *    characters and cannot be empty. Values can be empty and have a maximum
       *    length of 63 characters.
       *  * Keys and values can contain only lowercase letters, numeric characters,
       *    underscores, and dashes. All characters must use UTF-8 encoding, and
       *    international characters are allowed.
       *  * The key portion of a label must be unique. However, you can use the same
       *    key with multiple resources.
       *  * Keys must start with a lowercase letter or international character.
       *  See Google Cloud
       *  Document (https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements)
       *  for more details.
       */
      // const userLabels = [1,2,3,4]
      /**
       *  Optional. End user specification.
       */
      // const endUserSpec = {}
    
      // Imports the Discoveryengine library
      const {ConversationalSearchServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [ConversationalSearchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callStreamAnswerQuery() {
        // Construct request
        const request = {
          servingConfig,
          query,
        };
    
        // Run request
        const stream = await discoveryengineClient.streamAnswerQuery(request);
        stream.on('data', (response) => { console.log(response) });
        stream.on('error', (err) => { throw(err) });
        stream.on('end', () => { /* API call completed */ });
      }
    
      callStreamAnswerQuery();
    
    

### updateConversation(request, options)
    
    
    updateConversation(request?: protos.google.cloud.discoveryengine.v1beta.IUpdateConversationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1beta.IConversation,
            (protos.google.cloud.discoveryengine.v1beta.IUpdateConversationRequest | undefined),
            {} | undefined
        ]>;

Updates a Conversation.

action type cannot be changed. If the to update does not exist, a NOT_FOUND error is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iupdateconversationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconversation), ([protos.google.cloud.discoveryengine.v1beta.IUpdateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iupdateconversationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Conversation to update.
       */
      // const conversation = {}
      /**
       *  Indicates which fields in the provided
       *  Conversation google.cloud.discoveryengine.v1beta.Conversation  to update.
       *  The following are NOT supported:
       *  * Conversation.name google.cloud.discoveryengine.v1beta.Conversation.name 
       *  If not set or empty, all supported fields are updated.
       */
      // const updateMask = {}
    
      // Imports the Discoveryengine library
      const {ConversationalSearchServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [ConversationalSearchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callUpdateConversation() {
        // Construct request
        const request = {
          conversation,
        };
    
        // Run request
        const response = await discoveryengineClient.updateConversation(request);
        console.log(response);
      }
    
      callUpdateConversation();
    
    

### updateConversation(request, options, callback)
    
    
    updateConversation(request: protos.google.cloud.discoveryengine.v1beta.IUpdateConversationRequest, options: CallOptions, callback: Callback<protos.google.cloud.discoveryengine.v1beta.IConversation, protos.google.cloud.discoveryengine.v1beta.IUpdateConversationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iupdateconversationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconversation), [protos.google.cloud.discoveryengine.v1beta.IUpdateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iupdateconversationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConversation(request, callback)
    
    
    updateConversation(request: protos.google.cloud.discoveryengine.v1beta.IUpdateConversationRequest, callback: Callback<protos.google.cloud.discoveryengine.v1beta.IConversation, protos.google.cloud.discoveryengine.v1beta.IUpdateConversationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iupdateconversationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iconversation), [protos.google.cloud.discoveryengine.v1beta.IUpdateConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iupdateconversationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSession(request, options)
    
    
    updateSession(request?: protos.google.cloud.discoveryengine.v1beta.IUpdateSessionRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1beta.ISession,
            (protos.google.cloud.discoveryengine.v1beta.IUpdateSessionRequest | undefined),
            {} | undefined
        ]>;

Updates a Session.

action type cannot be changed. If the to update does not exist, a NOT_FOUND error is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iupdatesessionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1beta.ISession](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.isession), ([protos.google.cloud.discoveryengine.v1beta.IUpdateSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iupdatesessionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Session to update.
       */
      // const session = {}
      /**
       *  Indicates which fields in the provided
       *  Session google.cloud.discoveryengine.v1beta.Session  to update. The
       *  following are NOT supported:
       *  * Session.name google.cloud.discoveryengine.v1beta.Session.name 
       *  If not set or empty, all supported fields are updated.
       */
      // const updateMask = {}
    
      // Imports the Discoveryengine library
      const {ConversationalSearchServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [ConversationalSearchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callUpdateSession() {
        // Construct request
        const request = {
          session,
        };
    
        // Run request
        const response = await discoveryengineClient.updateSession(request);
        console.log(response);
      }
    
      callUpdateSession();
    
    

### updateSession(request, options, callback)
    
    
    updateSession(request: protos.google.cloud.discoveryengine.v1beta.IUpdateSessionRequest, options: CallOptions, callback: Callback<protos.google.cloud.discoveryengine.v1beta.ISession, protos.google.cloud.discoveryengine.v1beta.IUpdateSessionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iupdatesessionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.ISession](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.isession), [protos.google.cloud.discoveryengine.v1beta.IUpdateSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iupdatesessionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSession(request, callback)
    
    
    updateSession(request: protos.google.cloud.discoveryengine.v1beta.IUpdateSessionRequest, callback: Callback<protos.google.cloud.discoveryengine.v1beta.ISession, protos.google.cloud.discoveryengine.v1beta.IUpdateSessionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iupdatesessionrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.ISession](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.isession), [protos.google.cloud.discoveryengine.v1beta.IUpdateSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iupdatesessionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### userStorePath(project, location, userStore)
    
    
    userStorePath(project: string, location: string, userStore: string): string;

Return a fully-qualified userStore resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`userStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
