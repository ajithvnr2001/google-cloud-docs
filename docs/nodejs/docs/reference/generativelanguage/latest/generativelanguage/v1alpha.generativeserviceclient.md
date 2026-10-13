---
url: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/v1alpha.generativeserviceclient
title: Class v1alpha.GenerativeServiceClient (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:52.530653+00:00
---

# Class v1alpha.GenerativeServiceClient (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/v1alpha.generativeserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1alpha.GenerativeServiceClient (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  4.1.0  3.7.0  3.6.0  2.9.0  2.8.0  2.7.0  2.6.0  2.4.0  2.3.0 

API for using Large Models that generate multimodal content and have additional capabilities beyond text generation. v1alpha

## Package

[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of GenerativeServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new GenerativeServiceClient({fallback: true}, gax); ```  
  
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

### generativeServiceStub
    
    
    generativeServiceStub?: Promise<{
            [name: string]: Function;
        }>;

### innerApiCalls
    
    
    innerApiCalls: {
            [name: string]: Function;
        };

### pathTemplates
    
    
    pathTemplates: {
            [name: string]: gax.PathTemplate;
        };

### port
    
    
    static get port(): number;

The port for this API service.

### scopes
    
    
    static get scopes(): never[];

The scopes needed to make gRPC calls for every method defined in this service.

### servicePath
    
    
    static get servicePath(): string;

The DNS address for this API service.

### universeDomain
    
    
    get universeDomain(): string;

### warn
    
    
    warn: (code: string, message: string, warnType?: string) => void;

## Methods 

### batchEmbedContents(request, options)
    
    
    batchEmbedContents(request?: protos.google.ai.generativelanguage.v1alpha.IBatchEmbedContentsRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.IBatchEmbedContentsResponse,
            (protos.google.ai.generativelanguage.v1alpha.IBatchEmbedContentsRequest | undefined),
            {} | undefined
        ]>;

Generates multiple embedding vectors from the input `Content` which consists of a batch of strings represented as `EmbedContentRequest` objects.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchEmbedContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchembedcontentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.IBatchEmbedContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchembedcontentsresponse), ([protos.google.ai.generativelanguage.v1alpha.IBatchEmbedContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchembedcontentsrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [BatchEmbedContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.batchembedcontentsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The model's resource name. This serves as an ID for the Model to
       *  use.
       *  This name should match a model name returned by the `ListModels` method.
       *  Format: `models/{model}`
       */
      // const model = 'abc123'
      /**
       *  Required. Embed requests for the batch. The model in each of these requests
       *  must match the model specified `BatchEmbedContentsRequest.model`.
       */
      // const requests = [1,2,3,4]
    
      // Imports the Generativelanguage library
      const {GenerativeServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [GenerativeServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callBatchEmbedContents() {
        // Construct request
        const request = {
          model,
          requests,
        };
    
        // Run request
        const response = await generativelanguageClient.batchEmbedContents(request);
        console.log(response);
      }
    
      callBatchEmbedContents();
    
    

### batchEmbedContents(request, options, callback)
    
    
    batchEmbedContents(request: protos.google.ai.generativelanguage.v1alpha.IBatchEmbedContentsRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IBatchEmbedContentsResponse, protos.google.ai.generativelanguage.v1alpha.IBatchEmbedContentsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchEmbedContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchembedcontentsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IBatchEmbedContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchembedcontentsresponse), [protos.google.ai.generativelanguage.v1alpha.IBatchEmbedContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchembedcontentsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchEmbedContents(request, callback)
    
    
    batchEmbedContents(request: protos.google.ai.generativelanguage.v1alpha.IBatchEmbedContentsRequest, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IBatchEmbedContentsResponse, protos.google.ai.generativelanguage.v1alpha.IBatchEmbedContentsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchEmbedContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchembedcontentsrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IBatchEmbedContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchembedcontentsresponse), [protos.google.ai.generativelanguage.v1alpha.IBatchEmbedContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchembedcontentsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### bidiGenerateContent(options)
    
    
    bidiGenerateContent(options?: CallOptions): gax.CancellableStream;

Low-Latency bidirectional streaming API that supports audio and video streaming inputs can produce multimodal output streams (audio and text).

**Parameter**  
---  
**Name** | **Description**  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`gax.CancellableStream` | {Stream} An object stream which is both readable and writable. It accepts objects representing [BidiGenerateContentClientMessage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.bidigeneratecontentclientmessage) for write() method, and will emit objects representing [BidiGenerateContentServerMessage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.bidigeneratecontentservermessage) on 'data' event asynchronously. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#bi-directional-streaming) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Session configuration sent in the first and only first client
       *  message.
       */
      // const setup = {}
      /**
       *  Optional. Incremental update of the current conversation delivered from
       *  the client.
       */
      // const clientContent = {}
      /**
       *  Optional. User input that is sent in real time.
       */
      // const realtimeInput = {}
      /**
       *  Optional. Response to a `ToolCallMessage` received from the server.
       */
      // const toolResponse = {}
    
      // Imports the Generativelanguage library
      const {GenerativeServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [GenerativeServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callBidiGenerateContent() {
        // Construct request
        const request = {
        };
    
        // Run request
        const stream = await generativelanguageClient.bidiGenerateContent();
        stream.on('data', (response) => { console.log(response) });
        stream.on('error', (err) => { throw(err) });
        stream.on('end', () => { /* API call completed */ });
        stream.write(request);
        stream.end();
      }
    
      callBidiGenerateContent();
    
    

### cachedContentPath(id)
    
    
    cachedContentPath(id: string): string;

Return a fully-qualified cachedContent resource name string.

**Parameter**  
---  
**Name** | **Description**  
`id` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### chunkPath(corpus, document, chunk)
    
    
    chunkPath(corpus: string, document: string, chunk: string): string;

Return a fully-qualified chunk resource name string.

**Parameters**  
---  
**Name** | **Description**  
`corpus` |  `string`   
  
`document` |  `string`   
  
`chunk` |  `string`   
  
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
  
### corpusPath(corpus)
    
    
    corpusPath(corpus: string): string;

Return a fully-qualified corpus resource name string.

**Parameter**  
---  
**Name** | **Description**  
`corpus` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### corpusPermissionsPath(corpus, permission)
    
    
    corpusPermissionsPath(corpus: string, permission: string): string;

Return a fully-qualified corpusPermissions resource name string.

**Parameters**  
---  
**Name** | **Description**  
`corpus` |  `string`   
  
`permission` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### countTokens(request, options)
    
    
    countTokens(request?: protos.google.ai.generativelanguage.v1alpha.ICountTokensRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.ICountTokensResponse,
            (protos.google.ai.generativelanguage.v1alpha.ICountTokensRequest | undefined),
            {} | undefined
        ]>;

Runs a model's tokenizer on input `Content` and returns the token count. Refer to the [tokens guide](<https://ai.google.dev/gemini-api/docs/tokens>) to learn more about tokens.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICountTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icounttokensrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.ICountTokensResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icounttokensresponse), ([protos.google.ai.generativelanguage.v1alpha.ICountTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icounttokensrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [CountTokensResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.counttokensresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The model's resource name. This serves as an ID for the Model to
       *  use.
       *  This name should match a model name returned by the `ListModels` method.
       *  Format: `models/{model}`
       */
      // const model = 'abc123'
      /**
       *  Optional. The input given to the model as a prompt. This field is ignored
       *  when `generate_content_request` is set.
       */
      // const contents = [1,2,3,4]
      /**
       *  Optional. The overall input given to the `Model`. This includes the prompt
       *  as well as other model steering information like system
       *  instructions (https://ai.google.dev/gemini-api/docs/system-instructions),
       *  and/or function declarations for function
       *  calling (https://ai.google.dev/gemini-api/docs/function-calling).
       *  `Model`s/`Content`s and `generate_content_request`s are mutually
       *  exclusive. You can either send `Model` + `Content`s or a
       *  `generate_content_request`, but never both.
       */
      // const generateContentRequest = {}
    
      // Imports the Generativelanguage library
      const {GenerativeServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [GenerativeServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callCountTokens() {
        // Construct request
        const request = {
          model,
        };
    
        // Run request
        const response = await generativelanguageClient.countTokens(request);
        console.log(response);
      }
    
      callCountTokens();
    
    

### countTokens(request, options, callback)
    
    
    countTokens(request: protos.google.ai.generativelanguage.v1alpha.ICountTokensRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1alpha.ICountTokensResponse, protos.google.ai.generativelanguage.v1alpha.ICountTokensRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICountTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icounttokensrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.ICountTokensResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icounttokensresponse), [protos.google.ai.generativelanguage.v1alpha.ICountTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icounttokensrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### countTokens(request, callback)
    
    
    countTokens(request: protos.google.ai.generativelanguage.v1alpha.ICountTokensRequest, callback: Callback<protos.google.ai.generativelanguage.v1alpha.ICountTokensResponse, protos.google.ai.generativelanguage.v1alpha.ICountTokensRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICountTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icounttokensrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.ICountTokensResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icounttokensresponse), [protos.google.ai.generativelanguage.v1alpha.ICountTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icounttokensrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### documentPath(corpus, document)
    
    
    documentPath(corpus: string, document: string): string;

Return a fully-qualified document resource name string.

**Parameters**  
---  
**Name** | **Description**  
`corpus` |  `string`   
  
`document` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### embedContent(request, options)
    
    
    embedContent(request?: protos.google.ai.generativelanguage.v1alpha.IEmbedContentRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.IEmbedContentResponse,
            (protos.google.ai.generativelanguage.v1alpha.IEmbedContentRequest | undefined),
            {} | undefined
        ]>;

Generates a text embedding vector from the input `Content` using the specified [Gemini Embedding model](https://ai.google.dev/gemini-api/docs/models/gemini#text-embedding).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEmbedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iembedcontentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.IEmbedContentResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iembedcontentresponse), ([protos.google.ai.generativelanguage.v1alpha.IEmbedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iembedcontentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [EmbedContentResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.embedcontentresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The model's resource name. This serves as an ID for the Model to
       *  use.
       *  This name should match a model name returned by the `ListModels` method.
       *  Format: `models/{model}`
       */
      // const model = 'abc123'
      /**
       *  Required. The content to embed. Only the `parts.text` fields will be
       *  counted.
       */
      // const content = {}
      /**
       *  Optional. Optional task type for which the embeddings will be used. Can
       *  only be set for `models/embedding-001`.
       */
      // const taskType = {}
      /**
       *  Optional. An optional title for the text. Only applicable when TaskType is
       *  `RETRIEVAL_DOCUMENT`.
       *  Note: Specifying a `title` for `RETRIEVAL_DOCUMENT` provides better quality
       *  embeddings for retrieval.
       */
      // const title = 'abc123'
      /**
       *  Optional. Optional reduced dimension for the output embedding. If set,
       *  excessive values in the output embedding are truncated from the end.
       *  Supported by newer models since 2024 only. You cannot set this value if
       *  using the earlier model (`models/embedding-001`).
       */
      // const outputDimensionality = 1234
    
      // Imports the Generativelanguage library
      const {GenerativeServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [GenerativeServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callEmbedContent() {
        // Construct request
        const request = {
          model,
          content,
        };
    
        // Run request
        const response = await generativelanguageClient.embedContent(request);
        console.log(response);
      }
    
      callEmbedContent();
    
    

### embedContent(request, options, callback)
    
    
    embedContent(request: protos.google.ai.generativelanguage.v1alpha.IEmbedContentRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IEmbedContentResponse, protos.google.ai.generativelanguage.v1alpha.IEmbedContentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEmbedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iembedcontentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IEmbedContentResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iembedcontentresponse), [protos.google.ai.generativelanguage.v1alpha.IEmbedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iembedcontentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### embedContent(request, callback)
    
    
    embedContent(request: protos.google.ai.generativelanguage.v1alpha.IEmbedContentRequest, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IEmbedContentResponse, protos.google.ai.generativelanguage.v1alpha.IEmbedContentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEmbedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iembedcontentrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IEmbedContentResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iembedcontentresponse), [protos.google.ai.generativelanguage.v1alpha.IEmbedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iembedcontentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### filePath(file)
    
    
    filePath(file: string): string;

Return a fully-qualified file resource name string.

**Parameter**  
---  
**Name** | **Description**  
`file` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### generateAnswer(request, options)
    
    
    generateAnswer(request?: protos.google.ai.generativelanguage.v1alpha.IGenerateAnswerRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.IGenerateAnswerResponse,
            (protos.google.ai.generativelanguage.v1alpha.IGenerateAnswerRequest | undefined),
            {} | undefined
        ]>;

Generates a grounded answer from the model given an input `GenerateAnswerRequest`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateAnswerRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igenerateanswerrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.IGenerateAnswerResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igenerateanswerresponse), ([protos.google.ai.generativelanguage.v1alpha.IGenerateAnswerRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igenerateanswerrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Passages provided inline with the request.
       */
      // const inlinePassages = {}
      /**
       *  Content retrieved from resources created via the Semantic Retriever
       *  API.
       */
      // const semanticRetriever = {}
      /**
       *  Required. The name of the `Model` to use for generating the grounded
       *  response.
       *  Format: `model=models/{model}`.
       */
      // const model = 'abc123'
      /**
       *  Required. The content of the current conversation with the `Model`. For
       *  single-turn queries, this is a single question to answer. For multi-turn
       *  queries, this is a repeated field that contains conversation history and
       *  the last `Content` in the list containing the question.
       *  Note: `GenerateAnswer` only supports queries in English.
       */
      // const contents = [1,2,3,4]
      /**
       *  Required. Style in which answers should be returned.
       */
      // const answerStyle = {}
      /**
       *  Optional. A list of unique `SafetySetting` instances for blocking unsafe
       *  content.
       *  This will be enforced on the `GenerateAnswerRequest.contents` and
       *  `GenerateAnswerResponse.candidate`. There should not be more than one
       *  setting for each `SafetyCategory` type. The API will block any contents and
       *  responses that fail to meet the thresholds set by these settings. This list
       *  overrides the default settings for each `SafetyCategory` specified in the
       *  safety_settings. If there is no `SafetySetting` for a given
       *  `SafetyCategory` provided in the list, the API will use the default safety
       *  setting for that category. Harm categories HARM_CATEGORY_HATE_SPEECH,
       *  HARM_CATEGORY_SEXUALLY_EXPLICIT, HARM_CATEGORY_DANGEROUS_CONTENT,
       *  HARM_CATEGORY_HARASSMENT are supported.
       *  Refer to the
       *  guide (https://ai.google.dev/gemini-api/docs/safety-settings)
       *  for detailed information on available safety settings. Also refer to the
       *  Safety guidance (https://ai.google.dev/gemini-api/docs/safety-guidance) to
       *  learn how to incorporate safety considerations in your AI applications.
       */
      // const safetySettings = [1,2,3,4]
      /**
       *  Optional. Controls the randomness of the output.
       *  Values can range from 0.0,1.0, inclusive. A value closer to 1.0 will
       *  produce responses that are more varied and creative, while a value closer
       *  to 0.0 will typically result in more straightforward responses from the
       *  model. A low temperature (~0.2) is usually recommended for
       *  Attributed-Question-Answering use cases.
       */
      // const temperature = 1234
    
      // Imports the Generativelanguage library
      const {GenerativeServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [GenerativeServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callGenerateAnswer() {
        // Construct request
        const request = {
          model,
          contents,
          answerStyle,
        };
    
        // Run request
        const response = await generativelanguageClient.generateAnswer(request);
        console.log(response);
      }
    
      callGenerateAnswer();
    
    

### generateAnswer(request, options, callback)
    
    
    generateAnswer(request: protos.google.ai.generativelanguage.v1alpha.IGenerateAnswerRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IGenerateAnswerResponse, protos.google.ai.generativelanguage.v1alpha.IGenerateAnswerRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateAnswerRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igenerateanswerrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IGenerateAnswerResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igenerateanswerresponse), [protos.google.ai.generativelanguage.v1alpha.IGenerateAnswerRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igenerateanswerrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateAnswer(request, callback)
    
    
    generateAnswer(request: protos.google.ai.generativelanguage.v1alpha.IGenerateAnswerRequest, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IGenerateAnswerResponse, protos.google.ai.generativelanguage.v1alpha.IGenerateAnswerRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateAnswerRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igenerateanswerrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IGenerateAnswerResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igenerateanswerresponse), [protos.google.ai.generativelanguage.v1alpha.IGenerateAnswerRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igenerateanswerrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateContent(request, options)
    
    
    generateContent(request?: protos.google.ai.generativelanguage.v1alpha.IGenerateContentRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.IGenerateContentResponse,
            (protos.google.ai.generativelanguage.v1alpha.IGenerateContentRequest | undefined),
            {} | undefined
        ]>;

Generates a model response given an input `GenerateContentRequest`. Refer to the [text generation guide](<https://ai.google.dev/gemini-api/docs/text-generation>) for detailed usage information. Input capabilities differ between models, including tuned models. Refer to the [model guide](<https://ai.google.dev/gemini-api/docs/models/gemini>) and [tuning guide](<https://ai.google.dev/gemini-api/docs/model-tuning>) for details.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igeneratecontentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.IGenerateContentResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igeneratecontentresponse), ([protos.google.ai.generativelanguage.v1alpha.IGenerateContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igeneratecontentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `Model` to use for generating the completion.
       *  Format: `models/{model}`.
       */
      // const model = 'abc123'
      /**
       *  Optional. Developer set system
       *  instruction(s) (https://ai.google.dev/gemini-api/docs/system-instructions).
       *  Currently, text only.
       */
      // const systemInstruction = {}
      /**
       *  Required. The content of the current conversation with the model.
       *  For single-turn queries, this is a single instance. For multi-turn queries
       *  like chat (https://ai.google.dev/gemini-api/docs/text-generation#chat),
       *  this is a repeated field that contains the conversation history and the
       *  latest request.
       */
      // const contents = [1,2,3,4]
      /**
       *  Optional. A list of `Tools` the `Model` may use to generate the next
       *  response.
       *  A `Tool` is a piece of code that enables the system to interact with
       *  external systems to perform an action, or set of actions, outside of
       *  knowledge and scope of the `Model`. Supported `Tool`s are `Function` and
       *  `code_execution`. Refer to the Function
       *  calling (https://ai.google.dev/gemini-api/docs/function-calling) and the
       *  Code execution (https://ai.google.dev/gemini-api/docs/code-execution)
       *  guides to learn more.
       */
      // const tools = [1,2,3,4]
      /**
       *  Optional. Tool configuration for any `Tool` specified in the request. Refer
       *  to the Function calling
       *  guide (https://ai.google.dev/gemini-api/docs/function-calling#function_calling_mode)
       *  for a usage example.
       */
      // const toolConfig = {}
      /**
       *  Optional. A list of unique `SafetySetting` instances for blocking unsafe
       *  content.
       *  This will be enforced on the `GenerateContentRequest.contents` and
       *  `GenerateContentResponse.candidates`. There should not be more than one
       *  setting for each `SafetyCategory` type. The API will block any contents and
       *  responses that fail to meet the thresholds set by these settings. This list
       *  overrides the default settings for each `SafetyCategory` specified in the
       *  safety_settings. If there is no `SafetySetting` for a given
       *  `SafetyCategory` provided in the list, the API will use the default safety
       *  setting for that category. Harm categories HARM_CATEGORY_HATE_SPEECH,
       *  HARM_CATEGORY_SEXUALLY_EXPLICIT, HARM_CATEGORY_DANGEROUS_CONTENT,
       *  HARM_CATEGORY_HARASSMENT, HARM_CATEGORY_CIVIC_INTEGRITY are supported.
       *  Refer to the guide (https://ai.google.dev/gemini-api/docs/safety-settings)
       *  for detailed information on available safety settings. Also refer to the
       *  Safety guidance (https://ai.google.dev/gemini-api/docs/safety-guidance) to
       *  learn how to incorporate safety considerations in your AI applications.
       */
      // const safetySettings = [1,2,3,4]
      /**
       *  Optional. Configuration options for model generation and outputs.
       */
      // const generationConfig = {}
      /**
       *  Optional. The name of the content
       *  cached (https://ai.google.dev/gemini-api/docs/caching) to use as context
       *  to serve the prediction. Format: `cachedContents/{cachedContent}`
       */
      // const cachedContent = 'abc123'
    
      // Imports the Generativelanguage library
      const {GenerativeServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [GenerativeServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callGenerateContent() {
        // Construct request
        const request = {
          model,
          contents,
        };
    
        // Run request
        const response = await generativelanguageClient.generateContent(request);
        console.log(response);
      }
    
      callGenerateContent();
    
    

### generateContent(request, options, callback)
    
    
    generateContent(request: protos.google.ai.generativelanguage.v1alpha.IGenerateContentRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IGenerateContentResponse, protos.google.ai.generativelanguage.v1alpha.IGenerateContentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igeneratecontentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IGenerateContentResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igeneratecontentresponse), [protos.google.ai.generativelanguage.v1alpha.IGenerateContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igeneratecontentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateContent(request, callback)
    
    
    generateContent(request: protos.google.ai.generativelanguage.v1alpha.IGenerateContentRequest, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IGenerateContentResponse, protos.google.ai.generativelanguage.v1alpha.IGenerateContentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igeneratecontentrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IGenerateContentResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igeneratecontentresponse), [protos.google.ai.generativelanguage.v1alpha.IGenerateContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igeneratecontentrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### matchChunkFromChunkName(chunkName)
    
    
    matchChunkFromChunkName(chunkName: string): string | number;

Parse the chunk from Chunk resource.

**Parameter**  
---  
**Name** | **Description**  
`chunkName` |  `string`   
A fully-qualified path representing Chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the chunk.  
  
### matchCorpusFromChunkName(chunkName)
    
    
    matchCorpusFromChunkName(chunkName: string): string | number;

Parse the corpus from Chunk resource.

**Parameter**  
---  
**Name** | **Description**  
`chunkName` |  `string`   
A fully-qualified path representing Chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the corpus.  
  
### matchCorpusFromCorpusName(corpusName)
    
    
    matchCorpusFromCorpusName(corpusName: string): string | number;

Parse the corpus from Corpus resource.

**Parameter**  
---  
**Name** | **Description**  
`corpusName` |  `string`   
A fully-qualified path representing Corpus resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the corpus.  
  
### matchCorpusFromCorpusPermissionsName(corpusPermissionsName)
    
    
    matchCorpusFromCorpusPermissionsName(corpusPermissionsName: string): string | number;

Parse the corpus from CorpusPermissions resource.

**Parameter**  
---  
**Name** | **Description**  
`corpusPermissionsName` |  `string`   
A fully-qualified path representing corpus_permissions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the corpus.  
  
### matchCorpusFromDocumentName(documentName)
    
    
    matchCorpusFromDocumentName(documentName: string): string | number;

Parse the corpus from Document resource.

**Parameter**  
---  
**Name** | **Description**  
`documentName` |  `string`   
A fully-qualified path representing Document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the corpus.  
  
### matchDocumentFromChunkName(chunkName)
    
    
    matchDocumentFromChunkName(chunkName: string): string | number;

Parse the document from Chunk resource.

**Parameter**  
---  
**Name** | **Description**  
`chunkName` |  `string`   
A fully-qualified path representing Chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchDocumentFromDocumentName(documentName)
    
    
    matchDocumentFromDocumentName(documentName: string): string | number;

Parse the document from Document resource.

**Parameter**  
---  
**Name** | **Description**  
`documentName` |  `string`   
A fully-qualified path representing Document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchFileFromFileName(fileName)
    
    
    matchFileFromFileName(fileName: string): string | number;

Parse the file from File resource.

**Parameter**  
---  
**Name** | **Description**  
`fileName` |  `string`   
A fully-qualified path representing File resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the file.  
  
### matchIdFromCachedContentName(cachedContentName)
    
    
    matchIdFromCachedContentName(cachedContentName: string): string | number;

Parse the id from CachedContent resource.

**Parameter**  
---  
**Name** | **Description**  
`cachedContentName` |  `string`   
A fully-qualified path representing CachedContent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the id.  
  
### matchModelFromModelName(modelName)
    
    
    matchModelFromModelName(modelName: string): string | number;

Parse the model from Model resource.

**Parameter**  
---  
**Name** | **Description**  
`modelName` |  `string`   
A fully-qualified path representing Model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the model.  
  
### matchPermissionFromCorpusPermissionsName(corpusPermissionsName)
    
    
    matchPermissionFromCorpusPermissionsName(corpusPermissionsName: string): string | number;

Parse the permission from CorpusPermissions resource.

**Parameter**  
---  
**Name** | **Description**  
`corpusPermissionsName` |  `string`   
A fully-qualified path representing corpus_permissions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the permission.  
  
### matchPermissionFromTunedModelPermissionsName(tunedModelPermissionsName)
    
    
    matchPermissionFromTunedModelPermissionsName(tunedModelPermissionsName: string): string | number;

Parse the permission from TunedModelPermissions resource.

**Parameter**  
---  
**Name** | **Description**  
`tunedModelPermissionsName` |  `string`   
A fully-qualified path representing tuned_model_permissions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the permission.  
  
### matchTunedModelFromTunedModelName(tunedModelName)
    
    
    matchTunedModelFromTunedModelName(tunedModelName: string): string | number;

Parse the tuned_model from TunedModel resource.

**Parameter**  
---  
**Name** | **Description**  
`tunedModelName` |  `string`   
A fully-qualified path representing TunedModel resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tuned_model.  
  
### matchTunedModelFromTunedModelPermissionsName(tunedModelPermissionsName)
    
    
    matchTunedModelFromTunedModelPermissionsName(tunedModelPermissionsName: string): string | number;

Parse the tuned_model from TunedModelPermissions resource.

**Parameter**  
---  
**Name** | **Description**  
`tunedModelPermissionsName` |  `string`   
A fully-qualified path representing tuned_model_permissions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tuned_model.  
  
### modelPath(model)
    
    
    modelPath(model: string): string;

Return a fully-qualified model resource name string.

**Parameter**  
---  
**Name** | **Description**  
`model` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### streamGenerateContent(request, options)
    
    
    streamGenerateContent(request?: protos.google.ai.generativelanguage.v1alpha.IGenerateContentRequest, options?: CallOptions): gax.CancellableStream;

Generates a [streamed response](https://ai.google.dev/gemini-api/docs/text-generation?lang=python#generate-a-text-stream) from the model given an input `GenerateContentRequest`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igeneratecontentrequest)`   
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
       *  Required. The name of the `Model` to use for generating the completion.
       *  Format: `models/{model}`.
       */
      // const model = 'abc123'
      /**
       *  Optional. Developer set system
       *  instruction(s) (https://ai.google.dev/gemini-api/docs/system-instructions).
       *  Currently, text only.
       */
      // const systemInstruction = {}
      /**
       *  Required. The content of the current conversation with the model.
       *  For single-turn queries, this is a single instance. For multi-turn queries
       *  like chat (https://ai.google.dev/gemini-api/docs/text-generation#chat),
       *  this is a repeated field that contains the conversation history and the
       *  latest request.
       */
      // const contents = [1,2,3,4]
      /**
       *  Optional. A list of `Tools` the `Model` may use to generate the next
       *  response.
       *  A `Tool` is a piece of code that enables the system to interact with
       *  external systems to perform an action, or set of actions, outside of
       *  knowledge and scope of the `Model`. Supported `Tool`s are `Function` and
       *  `code_execution`. Refer to the Function
       *  calling (https://ai.google.dev/gemini-api/docs/function-calling) and the
       *  Code execution (https://ai.google.dev/gemini-api/docs/code-execution)
       *  guides to learn more.
       */
      // const tools = [1,2,3,4]
      /**
       *  Optional. Tool configuration for any `Tool` specified in the request. Refer
       *  to the Function calling
       *  guide (https://ai.google.dev/gemini-api/docs/function-calling#function_calling_mode)
       *  for a usage example.
       */
      // const toolConfig = {}
      /**
       *  Optional. A list of unique `SafetySetting` instances for blocking unsafe
       *  content.
       *  This will be enforced on the `GenerateContentRequest.contents` and
       *  `GenerateContentResponse.candidates`. There should not be more than one
       *  setting for each `SafetyCategory` type. The API will block any contents and
       *  responses that fail to meet the thresholds set by these settings. This list
       *  overrides the default settings for each `SafetyCategory` specified in the
       *  safety_settings. If there is no `SafetySetting` for a given
       *  `SafetyCategory` provided in the list, the API will use the default safety
       *  setting for that category. Harm categories HARM_CATEGORY_HATE_SPEECH,
       *  HARM_CATEGORY_SEXUALLY_EXPLICIT, HARM_CATEGORY_DANGEROUS_CONTENT,
       *  HARM_CATEGORY_HARASSMENT, HARM_CATEGORY_CIVIC_INTEGRITY are supported.
       *  Refer to the guide (https://ai.google.dev/gemini-api/docs/safety-settings)
       *  for detailed information on available safety settings. Also refer to the
       *  Safety guidance (https://ai.google.dev/gemini-api/docs/safety-guidance) to
       *  learn how to incorporate safety considerations in your AI applications.
       */
      // const safetySettings = [1,2,3,4]
      /**
       *  Optional. Configuration options for model generation and outputs.
       */
      // const generationConfig = {}
      /**
       *  Optional. The name of the content
       *  cached (https://ai.google.dev/gemini-api/docs/caching) to use as context
       *  to serve the prediction. Format: `cachedContents/{cachedContent}`
       */
      // const cachedContent = 'abc123'
    
      // Imports the Generativelanguage library
      const {GenerativeServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [GenerativeServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callStreamGenerateContent() {
        // Construct request
        const request = {
          model,
          contents,
        };
    
        // Run request
        const stream = await generativelanguageClient.streamGenerateContent(request);
        stream.on('data', (response) => { console.log(response) });
        stream.on('error', (err) => { throw(err) });
        stream.on('end', () => { /* API call completed */ });
      }
    
      callStreamGenerateContent();
    
    

### tunedModelPath(tunedModel)
    
    
    tunedModelPath(tunedModel: string): string;

Return a fully-qualified tunedModel resource name string.

**Parameter**  
---  
**Name** | **Description**  
`tunedModel` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### tunedModelPermissionsPath(tunedModel, permission)
    
    
    tunedModelPermissionsPath(tunedModel: string, permission: string): string;

Return a fully-qualified tunedModelPermissions resource name string.

**Parameters**  
---  
**Name** | **Description**  
`tunedModel` |  `string`   
  
`permission` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
