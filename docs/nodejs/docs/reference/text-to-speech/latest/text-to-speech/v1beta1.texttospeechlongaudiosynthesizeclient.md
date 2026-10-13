---
url: https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/v1beta1.texttospeechlongaudiosynthesizeclient
title: Class v1beta1.TextToSpeechLongAudioSynthesizeClient (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:08.706468+00:00
---

# Class v1beta1.TextToSpeechLongAudioSynthesizeClient (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/v1beta1.texttospeechlongaudiosynthesizeclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.TextToSpeechLongAudioSynthesizeClient (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  5.8.0  5.7.0  5.5.0  5.4.0  5.0.2  4.2.2  4.0.4  3.4.0  3.3.1  3.2.7 

Service that implements Google Cloud Text-to-Speech API. v1beta1

## Package

[@google-cloud/text-to-speech](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of TextToSpeechLongAudioSynthesizeClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new TextToSpeechLongAudioSynthesizeClient({fallback: true}, gax); ```  
  
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

### operationsClient
    
    
    operationsClient: gax.OperationsClient;

### port
    
    
    static get port(): number;

The port for this API service.

### scopes
    
    
    static get scopes(): string[];

The scopes needed to make gRPC calls for every method defined in this service.

### servicePath
    
    
    static get servicePath(): string;

The DNS address for this API service.

### textToSpeechLongAudioSynthesizeStub
    
    
    textToSpeechLongAudioSynthesizeStub?: Promise<{
            [name: string]: Function;
        }>;

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
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### checkSynthesizeLongAudioProgress(name)
    
    
    checkSynthesizeLongAudioProgress(name: string): Promise<LROperation<protos.google.cloud.texttospeech.v1beta1.SynthesizeLongAudioResponse, protos.google.cloud.texttospeech.v1beta1.SynthesizeLongAudioMetadata>>;

Check the status of the long running operation returned by `synthesizeLongAudio()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.texttospeech.v1beta1.SynthesizeLongAudioResponse](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1beta1.synthesizelongaudioresponse), [protos.google.cloud.texttospeech.v1beta1.SynthesizeLongAudioMetadata](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1beta1.synthesizelongaudiometadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource states of the request in the form of
       *  `projects/* /locations/*`.
       */
      // const parent = 'abc123'
      /**
       *  Required. The Synthesizer requires either plain text or SSML as input.
       */
      // const input = {}
      /**
       *  Required. The configuration of the synthesized audio.
       */
      // const audioConfig = {}
      /**
       *  Required. Specifies a Cloud Storage URI for the synthesis results. Must be
       *  specified in the format: `gs://bucket_name/object_name`, and the bucket
       *  must already exist.
       */
      // const outputGcsUri = 'abc123'
      /**
       *  Required. The desired voice of the synthesized audio.
       */
      // const voice = {}
    
      // Imports the Texttospeech library
      const {TextToSpeechLongAudioSynthesizeClient} = require('[@google-cloud/text-to-speech](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const texttospeechClient = new [TextToSpeechLongAudioSynthesizeClient](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/overview.html)();
    
      async function callSynthesizeLongAudio() {
        // Construct request
        const request = {
          input,
          audioConfig,
          outputGcsUri,
          voice,
        };
    
        // Run request
        const [operation] = await texttospeechClient.synthesizeLongAudio(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callSynthesizeLongAudio();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### deleteOperation(request, optionsOrCallback, callback)
    
    
    deleteOperation(request: protos.google.longrunning.DeleteOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.protobuf.Empty, protos.google.longrunning.DeleteOperationRequest, {} | null | undefined>, callback?: Callback<protos.google.protobuf.Empty, protos.google.longrunning.DeleteOperationRequest, {} | null | undefined>): Promise<protos.google.protobuf.Empty>;

Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### getOperation(request, optionsOrCallback, callback)
    
    
    getOperation(request: protos.google.longrunning.GetOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>, callback?: Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>): Promise<[protos.google.longrunning.Operation]>;

Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.longrunning.operation)]>` |   
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
  
### listOperationsAsync(request, options)
    
    
    listOperationsAsync(request: protos.google.longrunning.ListOperationsRequest, options?: gax.CallOptions): AsyncIterable<protos.google.longrunning.IOperation>;

Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. Returns an iterable object.

For-await-of syntax is used with the iterable to recursively get response element on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `gax.CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
**Example**
    
    
    const client = longrunning.operationsClient();
    for await (const response of client.listOperationsAsync(request));
    // doThingsWith(response)
    

### synthesizeLongAudio(request, options)
    
    
    synthesizeLongAudio(request?: protos.google.cloud.texttospeech.v1beta1.ISynthesizeLongAudioRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.texttospeech.v1beta1.ISynthesizeLongAudioResponse, protos.google.cloud.texttospeech.v1beta1.ISynthesizeLongAudioMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Synthesizes long form text asynchronously.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISynthesizeLongAudioRequest](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1beta1.isynthesizelongaudiorequest)`   
The request object that will be sent.  
`options` |  `gax.CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.texttospeech.v1beta1.ISynthesizeLongAudioResponse](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1beta1.isynthesizelongaudioresponse), [protos.google.cloud.texttospeech.v1beta1.ISynthesizeLongAudioMetadata](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1beta1.isynthesizelongaudiometadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The resource states of the request in the form of
       *  `projects/* /locations/*`.
       */
      // const parent = 'abc123'
      /**
       *  Required. The Synthesizer requires either plain text or SSML as input.
       */
      // const input = {}
      /**
       *  Required. The configuration of the synthesized audio.
       */
      // const audioConfig = {}
      /**
       *  Required. Specifies a Cloud Storage URI for the synthesis results. Must be
       *  specified in the format: `gs://bucket_name/object_name`, and the bucket
       *  must already exist.
       */
      // const outputGcsUri = 'abc123'
      /**
       *  Required. The desired voice of the synthesized audio.
       */
      // const voice = {}
    
      // Imports the Texttospeech library
      const {TextToSpeechLongAudioSynthesizeClient} = require('[@google-cloud/text-to-speech](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const texttospeechClient = new [TextToSpeechLongAudioSynthesizeClient](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/overview.html)();
    
      async function callSynthesizeLongAudio() {
        // Construct request
        const request = {
          input,
          audioConfig,
          outputGcsUri,
          voice,
        };
    
        // Run request
        const [operation] = await texttospeechClient.synthesizeLongAudio(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callSynthesizeLongAudio();
    
    

### synthesizeLongAudio(request, options, callback)
    
    
    synthesizeLongAudio(request: protos.google.cloud.texttospeech.v1beta1.ISynthesizeLongAudioRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.texttospeech.v1beta1.ISynthesizeLongAudioResponse, protos.google.cloud.texttospeech.v1beta1.ISynthesizeLongAudioMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISynthesizeLongAudioRequest](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1beta1.isynthesizelongaudiorequest)`   
  
`options` |  `gax.CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.texttospeech.v1beta1.ISynthesizeLongAudioResponse](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1beta1.isynthesizelongaudioresponse), [protos.google.cloud.texttospeech.v1beta1.ISynthesizeLongAudioMetadata](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1beta1.isynthesizelongaudiometadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### synthesizeLongAudio(request, callback)
    
    
    synthesizeLongAudio(request: protos.google.cloud.texttospeech.v1beta1.ISynthesizeLongAudioRequest, callback: Callback<LROperation<protos.google.cloud.texttospeech.v1beta1.ISynthesizeLongAudioResponse, protos.google.cloud.texttospeech.v1beta1.ISynthesizeLongAudioMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISynthesizeLongAudioRequest](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1beta1.isynthesizelongaudiorequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.texttospeech.v1beta1.ISynthesizeLongAudioResponse](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1beta1.isynthesizelongaudioresponse), [protos.google.cloud.texttospeech.v1beta1.ISynthesizeLongAudioMetadata](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1beta1.isynthesizelongaudiometadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
