---
url: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/v1beta3.discussserviceclient
title: Class v1beta3.DiscussServiceClient (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:48.891055+00:00
---

# Class v1beta3.DiscussServiceClient (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/v1beta3.discussserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta3.DiscussServiceClient (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  4.1.0  3.7.0  3.6.0  2.9.0  2.8.0  2.7.0  2.6.0  2.4.0  2.3.0 

An API for using Generative Language Models (GLMs) in dialog applications.

Also known as large language models (LLMs), this API provides models that are trained for multi-turn dialog. v1beta3

## Package

[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of DiscussServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new DiscussServiceClient({fallback: true}, gax); ```  
  
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

### discussServiceStub
    
    
    discussServiceStub?: Promise<{
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

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### countMessageTokens(request, options)
    
    
    countMessageTokens(request?: protos.google.ai.generativelanguage.v1beta3.ICountMessageTokensRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1beta3.ICountMessageTokensResponse,
            (protos.google.ai.generativelanguage.v1beta3.ICountMessageTokensRequest | undefined),
            {} | undefined
        ]>;

Runs a model's tokenizer on a string and returns the token count.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICountMessageTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta3.icountmessagetokensrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1beta3.ICountMessageTokensResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta3.icountmessagetokensresponse), ([protos.google.ai.generativelanguage.v1beta3.ICountMessageTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta3.icountmessagetokensrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [CountMessageTokensResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta3.countmessagetokensresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
       *  Required. The prompt, whose token count is to be returned.
       */
      // const prompt = {}
    
      // Imports the Generativelanguage library
      const {DiscussServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1beta3;
    
      // Instantiates a client
      const generativelanguageClient = new [DiscussServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callCountMessageTokens() {
        // Construct request
        const request = {
          model,
          prompt,
        };
    
        // Run request
        const response = await generativelanguageClient.countMessageTokens(request);
        console.log(response);
      }
    
      callCountMessageTokens();
    
    

### countMessageTokens(request, options, callback)
    
    
    countMessageTokens(request: protos.google.ai.generativelanguage.v1beta3.ICountMessageTokensRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1beta3.ICountMessageTokensResponse, protos.google.ai.generativelanguage.v1beta3.ICountMessageTokensRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICountMessageTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta3.icountmessagetokensrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta3.ICountMessageTokensResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta3.icountmessagetokensresponse), [protos.google.ai.generativelanguage.v1beta3.ICountMessageTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta3.icountmessagetokensrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### countMessageTokens(request, callback)
    
    
    countMessageTokens(request: protos.google.ai.generativelanguage.v1beta3.ICountMessageTokensRequest, callback: Callback<protos.google.ai.generativelanguage.v1beta3.ICountMessageTokensResponse, protos.google.ai.generativelanguage.v1beta3.ICountMessageTokensRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICountMessageTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta3.icountmessagetokensrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta3.ICountMessageTokensResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta3.icountmessagetokensresponse), [protos.google.ai.generativelanguage.v1beta3.ICountMessageTokensRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta3.icountmessagetokensrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateMessage(request, options)
    
    
    generateMessage(request?: protos.google.ai.generativelanguage.v1beta3.IGenerateMessageRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1beta3.IGenerateMessageResponse,
            (protos.google.ai.generativelanguage.v1beta3.IGenerateMessageRequest | undefined),
            {} | undefined
        ]>;

Generates a response from the model given an input `MessagePrompt`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta3.igeneratemessagerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1beta3.IGenerateMessageResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta3.igeneratemessageresponse), ([protos.google.ai.generativelanguage.v1beta3.IGenerateMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta3.igeneratemessagerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [GenerateMessageResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta3.generatemessageresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the model to use.
       *  Format: `name=models/{model}`.
       */
      // const model = 'abc123'
      /**
       *  Required. The structured textual input given to the model as a prompt.
       *  Given a
       *  prompt, the model will return what it predicts is the next message in the
       *  discussion.
       */
      // const prompt = {}
      /**
       *  Optional. Controls the randomness of the output.
       *  Values can range over `[0.0,1.0]`,
       *  inclusive. A value closer to `1.0` will produce responses that are more
       *  varied, while a value closer to `0.0` will typically result in
       *  less surprising responses from the model.
       */
      // const temperature = 1234
      /**
       *  Optional. The number of generated response messages to return.
       *  This value must be between
       *  `[1, 8]`, inclusive. If unset, this will default to `1`.
       */
      // const candidateCount = 1234
      /**
       *  Optional. The maximum cumulative probability of tokens to consider when
       *  sampling.
       *  The model uses combined Top-k and nucleus sampling.
       *  Nucleus sampling considers the smallest set of tokens whose probability
       *  sum is at least `top_p`.
       */
      // const topP = 1234
      /**
       *  Optional. The maximum number of tokens to consider when sampling.
       *  The model uses combined Top-k and nucleus sampling.
       *  Top-k sampling considers the set of `top_k` most probable tokens.
       */
      // const topK = 1234
    
      // Imports the Generativelanguage library
      const {DiscussServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1beta3;
    
      // Instantiates a client
      const generativelanguageClient = new [DiscussServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callGenerateMessage() {
        // Construct request
        const request = {
          model,
          prompt,
        };
    
        // Run request
        const response = await generativelanguageClient.generateMessage(request);
        console.log(response);
      }
    
      callGenerateMessage();
    
    

### generateMessage(request, options, callback)
    
    
    generateMessage(request: protos.google.ai.generativelanguage.v1beta3.IGenerateMessageRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1beta3.IGenerateMessageResponse, protos.google.ai.generativelanguage.v1beta3.IGenerateMessageRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta3.igeneratemessagerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta3.IGenerateMessageResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta3.igeneratemessageresponse), [protos.google.ai.generativelanguage.v1beta3.IGenerateMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta3.igeneratemessagerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateMessage(request, callback)
    
    
    generateMessage(request: protos.google.ai.generativelanguage.v1beta3.IGenerateMessageRequest, callback: Callback<protos.google.ai.generativelanguage.v1beta3.IGenerateMessageResponse, protos.google.ai.generativelanguage.v1beta3.IGenerateMessageRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta3.igeneratemessagerequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta3.IGenerateMessageResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta3.igeneratemessageresponse), [protos.google.ai.generativelanguage.v1beta3.IGenerateMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta3.igeneratemessagerequest) | null | undefined, {} | null | undefined>`   
  
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
  
### matchPermissionFromPermissionName(permissionName)
    
    
    matchPermissionFromPermissionName(permissionName: string): string | number;

Parse the permission from Permission resource.

**Parameter**  
---  
**Name** | **Description**  
`permissionName` |  `string`   
A fully-qualified path representing Permission resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the permission.  
  
### matchTunedModelFromPermissionName(permissionName)
    
    
    matchTunedModelFromPermissionName(permissionName: string): string | number;

Parse the tuned_model from Permission resource.

**Parameter**  
---  
**Name** | **Description**  
`permissionName` |  `string`   
A fully-qualified path representing Permission resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tuned_model.  
  
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
  
### permissionPath(tunedModel, permission)
    
    
    permissionPath(tunedModel: string, permission: string): string;

Return a fully-qualified permission resource name string.

**Parameters**  
---  
**Name** | **Description**  
`tunedModel` |  `string`   
  
`permission` |  `string`   
  
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
