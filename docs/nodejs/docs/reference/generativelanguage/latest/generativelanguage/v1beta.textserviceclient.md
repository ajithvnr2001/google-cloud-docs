---
url: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/v1beta.textserviceclient
title: Class v1beta.TextServiceClient (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:59.146100+00:00
---

# Class v1beta.TextServiceClient (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/v1beta.textserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.TextServiceClient (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  4.1.0  3.7.0  3.6.0  2.9.0  2.8.0  2.7.0  2.6.0  2.4.0  2.3.0 

API for using Generative Language Models (GLMs) trained to generate text.

Also known as Large Language Models (LLM)s, these generate text given an input prompt from the user. v1beta

## Package

[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of TextServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new TextServiceClient({fallback: true}, gax); ```  
  
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

### textServiceStub
    
    
    textServiceStub?: Promise<{
            [name: string]: Function;
        }>;

### universeDomain
    
    
    get universeDomain(): string;

### warn
    
    
    warn: (code: string, message: string, warnType?: string) => void;

## Methods 

### batchEmbedText(request, options)
    
    
    batchEmbedText(request?: protos.google.ai.generativelanguage.v1beta.IBatchEmbedTextRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1beta.IBatchEmbedTextResponse,
            (protos.google.ai.generativelanguage.v1beta.IBatchEmbedTextRequest | undefined),
            {} | undefined
        ]>;

Generates multiple embeddings from the model given input text in a synchronous call.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchEmbedTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ibatchembedtextrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1beta.IBatchEmbedTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ibatchembedtextresponse), ([protos.google.ai.generativelanguage.v1beta.IBatchEmbedTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ibatchembedtextrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [BatchEmbedTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.batchembedtextresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `Model` to use for generating the embedding.
       *  Examples:
       *   models/embedding-gecko-001
       */
      // const model = 'abc123'
      /**
       *  Optional. The free-form input texts that the model will turn into an
       *  embedding. The current limit is 100 texts, over which an error will be
       *  thrown.
       */
      // const texts = ['abc','def']
      /**
       *  Optional. Embed requests for the batch. Only one of `texts` or `requests`
       *  can be set.
       */
      // const requests = [1,2,3,4]
    
      // Imports the Generativelanguage library
      const {TextServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const generativelanguageClient = new [TextServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callBatchEmbedText() {
        // Construct request
        const request = {
          model,
        };
    
        // Run request
        const response = await generativelanguageClient.batchEmbedText(request);
        console.log(response);
      }
    
      callBatchEmbedText();
    
    

### batchEmbedText(request, options, callback)
    
    
    batchEmbedText(request: protos.google.ai.generativelanguage.v1beta.IBatchEmbedTextRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1beta.IBatchEmbedTextResponse, protos.google.ai.generativelanguage.v1beta.IBatchEmbedTextRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchEmbedTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ibatchembedtextrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta.IBatchEmbedTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ibatchembedtextresponse), [protos.google.ai.generativelanguage.v1beta.IBatchEmbedTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ibatchembedtextrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchEmbedText(request, callback)
    
    
    batchEmbedText(request: protos.google.ai.generativelanguage.v1beta.IBatchEmbedTextRequest, callback: Callback<protos.google.ai.generativelanguage.v1beta.IBatchEmbedTextResponse, protos.google.ai.generativelanguage.v1beta.IBatchEmbedTextRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchEmbedTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ibatchembedtextrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta.IBatchEmbedTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ibatchembedtextresponse), [protos.google.ai.generativelanguage.v1beta.IBatchEmbedTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ibatchembedtextrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
  
### countTextTokens(request, options)
    
    
    countTextTokens(request?: protos.google.ai.generativelanguage.v1beta.ICountTextTokensRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1beta.ICountTextTokensResponse,
            (protos.google.ai.generativelanguage.v1beta.ICountTextTokensRequest | undefined),
            {} | undefined
        ]>;

Runs a model's tokenizer on a text and returns the token count.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICountTextTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icounttexttokensrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1beta.ICountTextTokensResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icounttexttokensresponse), ([protos.google.ai.generativelanguage.v1beta.ICountTextTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icounttexttokensrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [CountTextTokensResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.counttexttokensresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
       *  Required. The free-form input text given to the model as a prompt.
       */
      // const prompt = {}
    
      // Imports the Generativelanguage library
      const {TextServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const generativelanguageClient = new [TextServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callCountTextTokens() {
        // Construct request
        const request = {
          model,
          prompt,
        };
    
        // Run request
        const response = await generativelanguageClient.countTextTokens(request);
        console.log(response);
      }
    
      callCountTextTokens();
    
    

### countTextTokens(request, options, callback)
    
    
    countTextTokens(request: protos.google.ai.generativelanguage.v1beta.ICountTextTokensRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1beta.ICountTextTokensResponse, protos.google.ai.generativelanguage.v1beta.ICountTextTokensRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICountTextTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icounttexttokensrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta.ICountTextTokensResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icounttexttokensresponse), [protos.google.ai.generativelanguage.v1beta.ICountTextTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icounttexttokensrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### countTextTokens(request, callback)
    
    
    countTextTokens(request: protos.google.ai.generativelanguage.v1beta.ICountTextTokensRequest, callback: Callback<protos.google.ai.generativelanguage.v1beta.ICountTextTokensResponse, protos.google.ai.generativelanguage.v1beta.ICountTextTokensRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICountTextTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icounttexttokensrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta.ICountTextTokensResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icounttexttokensresponse), [protos.google.ai.generativelanguage.v1beta.ICountTextTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icounttexttokensrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### embedText(request, options)
    
    
    embedText(request?: protos.google.ai.generativelanguage.v1beta.IEmbedTextRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1beta.IEmbedTextResponse,
            protos.google.ai.generativelanguage.v1beta.IEmbedTextRequest | undefined,
            {} | undefined
        ]>;

Generates an embedding from the model given an input message.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEmbedTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.iembedtextrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1beta.IEmbedTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.iembedtextresponse), [protos.google.ai.generativelanguage.v1beta.IEmbedTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.iembedtextrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [EmbedTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.embedtextresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The model name to use with the format model=models/{model}.
       */
      // const model = 'abc123'
      /**
       *  Optional. The free-form input text that the model will turn into an
       *  embedding.
       */
      // const text = 'abc123'
    
      // Imports the Generativelanguage library
      const {TextServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const generativelanguageClient = new [TextServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callEmbedText() {
        // Construct request
        const request = {
          model,
        };
    
        // Run request
        const response = await generativelanguageClient.embedText(request);
        console.log(response);
      }
    
      callEmbedText();
    
    

### embedText(request, options, callback)
    
    
    embedText(request: protos.google.ai.generativelanguage.v1beta.IEmbedTextRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1beta.IEmbedTextResponse, protos.google.ai.generativelanguage.v1beta.IEmbedTextRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEmbedTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.iembedtextrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta.IEmbedTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.iembedtextresponse), [protos.google.ai.generativelanguage.v1beta.IEmbedTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.iembedtextrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### embedText(request, callback)
    
    
    embedText(request: protos.google.ai.generativelanguage.v1beta.IEmbedTextRequest, callback: Callback<protos.google.ai.generativelanguage.v1beta.IEmbedTextResponse, protos.google.ai.generativelanguage.v1beta.IEmbedTextRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEmbedTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.iembedtextrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta.IEmbedTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.iembedtextresponse), [protos.google.ai.generativelanguage.v1beta.IEmbedTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.iembedtextrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### generateText(request, options)
    
    
    generateText(request?: protos.google.ai.generativelanguage.v1beta.IGenerateTextRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1beta.IGenerateTextResponse,
            (protos.google.ai.generativelanguage.v1beta.IGenerateTextRequest | undefined),
            {} | undefined
        ]>;

Generates a response from the model given an input message.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igeneratetextrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1beta.IGenerateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igeneratetextresponse), ([protos.google.ai.generativelanguage.v1beta.IGenerateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igeneratetextrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [GenerateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.generatetextresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `Model` or `TunedModel` to use for generating the
       *  completion.
       *  Examples:
       *   models/text-bison-001
       *   tunedModels/sentence-translator-u3b7m
       */
      // const model = 'abc123'
      /**
       *  Required. The free-form input text given to the model as a prompt.
       *  Given a prompt, the model will generate a TextCompletion response it
       *  predicts as the completion of the input text.
       */
      // const prompt = {}
      /**
       *  Optional. Controls the randomness of the output.
       *  Note: The default value varies by model, see the `Model.temperature`
       *  attribute of the `Model` returned the `getModel` function.
       *  Values can range from 0.0,1.0,
       *  inclusive. A value closer to 1.0 will produce responses that are more
       *  varied and creative, while a value closer to 0.0 will typically result in
       *  more straightforward responses from the model.
       */
      // const temperature = 1234
      /**
       *  Optional. Number of generated responses to return.
       *  This value must be between 1, 8, inclusive. If unset, this will default
       *  to 1.
       */
      // const candidateCount = 1234
      /**
       *  Optional. The maximum number of tokens to include in a candidate.
       *  If unset, this will default to output_token_limit specified in the `Model`
       *  specification.
       */
      // const maxOutputTokens = 1234
      /**
       *  Optional. The maximum cumulative probability of tokens to consider when
       *  sampling.
       *  The model uses combined Top-k and nucleus sampling.
       *  Tokens are sorted based on their assigned probabilities so that only the
       *  most likely tokens are considered. Top-k sampling directly limits the
       *  maximum number of tokens to consider, while Nucleus sampling limits number
       *  of tokens based on the cumulative probability.
       *  Note: The default value varies by model, see the `Model.top_p`
       *  attribute of the `Model` returned the `getModel` function.
       */
      // const topP = 1234
      /**
       *  Optional. The maximum number of tokens to consider when sampling.
       *  The model uses combined Top-k and nucleus sampling.
       *  Top-k sampling considers the set of `top_k` most probable tokens.
       *  Defaults to 40.
       *  Note: The default value varies by model, see the `Model.top_k`
       *  attribute of the `Model` returned the `getModel` function.
       */
      // const topK = 1234
      /**
       *  Optional. A list of unique `SafetySetting` instances for blocking unsafe
       *  content.
       *  that will be enforced on the `GenerateTextRequest.prompt` and
       *  `GenerateTextResponse.candidates`. There should not be more than one
       *  setting for each `SafetyCategory` type. The API will block any prompts and
       *  responses that fail to meet the thresholds set by these settings. This list
       *  overrides the default settings for each `SafetyCategory` specified in the
       *  safety_settings. If there is no `SafetySetting` for a given
       *  `SafetyCategory` provided in the list, the API will use the default safety
       *  setting for that category. Harm categories HARM_CATEGORY_DEROGATORY,
       *  HARM_CATEGORY_TOXICITY, HARM_CATEGORY_VIOLENCE, HARM_CATEGORY_SEXUAL,
       *  HARM_CATEGORY_MEDICAL, HARM_CATEGORY_DANGEROUS are supported in text
       *  service.
       */
      // const safetySettings = [1,2,3,4]
      /**
       *  The set of character sequences (up to 5) that will stop output generation.
       *  If specified, the API will stop at the first appearance of a stop
       *  sequence. The stop sequence will not be included as part of the response.
       */
      // const stopSequences = ['abc','def']
    
      // Imports the Generativelanguage library
      const {TextServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const generativelanguageClient = new [TextServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callGenerateText() {
        // Construct request
        const request = {
          model,
          prompt,
        };
    
        // Run request
        const response = await generativelanguageClient.generateText(request);
        console.log(response);
      }
    
      callGenerateText();
    
    

### generateText(request, options, callback)
    
    
    generateText(request: protos.google.ai.generativelanguage.v1beta.IGenerateTextRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1beta.IGenerateTextResponse, protos.google.ai.generativelanguage.v1beta.IGenerateTextRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igeneratetextrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta.IGenerateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igeneratetextresponse), [protos.google.ai.generativelanguage.v1beta.IGenerateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igeneratetextrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateText(request, callback)
    
    
    generateText(request: protos.google.ai.generativelanguage.v1beta.IGenerateTextRequest, callback: Callback<protos.google.ai.generativelanguage.v1beta.IGenerateTextResponse, protos.google.ai.generativelanguage.v1beta.IGenerateTextRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igeneratetextrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta.IGenerateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igeneratetextresponse), [protos.google.ai.generativelanguage.v1beta.IGenerateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igeneratetextrequest) | null | undefined, {} | null | undefined>`   
  
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
