---
url: https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/v1p1beta1.speechclient-class
title: Class v1p1beta1.SpeechClient (8.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:52.221411+00:00
---

# Class v1p1beta1.SpeechClient (8.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/v1p1beta1.speechclient-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1p1beta1.SpeechClient (8.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  8.0.1  7.5.0  7.4.0  6.6.1  6.3.0  6.1.1  6.0.1  5.4.1  5.3.1  5.1.0  5.0.3  4.10.0  4.9.0  4.8.1  4.7.0  4.6.1  4.5.6  4.1.3 

Service that implements Google Cloud Speech API. v1p1beta1

## Package

[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of SpeechClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new SpeechClient({fallback: true}, gax); ```  
  
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

### speechStub
    
    
    speechStub?: Promise<{
            [name: string]: Function;
        }>;

### universeDomain
    
    
    get universeDomain(): string;

### warn
    
    
    warn: (code: string, message: string, warnType?: string) => void;

## Methods 

### _streamingRecognize(options)
    
    
    _streamingRecognize(options?: CallOptions): gax.CancellableStream;

Performs bidirectional streaming speech recognition: receive results while sending audio. This method is only available via the gRPC API (not REST).

**Parameter**  
---  
**Name** | **Description**  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`gax.CancellableStream` | {Stream} An object stream which is both readable and writable. It accepts objects representing [StreamingRecognizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.streamingrecognizerequest) for write() method, and will emit objects representing on 'data' event asynchronously. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#bi-directional-streaming) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Provides information to the recognizer that specifies how to process the
       *  request. The first `StreamingRecognizeRequest` message must contain a
       *  `streaming_config`  message.
       */
      // const streamingConfig = {}
      /**
       *  The audio data to be recognized. Sequential chunks of audio data are sent
       *  in sequential `StreamingRecognizeRequest` messages. The first
       *  `StreamingRecognizeRequest` message must not contain `audio_content` data
       *  and all subsequent `StreamingRecognizeRequest` messages must contain
       *  `audio_content` data. The audio bytes must be encoded as specified in
       *  `RecognitionConfig`. Note: as with all bytes fields, proto buffers use a
       *  pure binary representation (not base64). See
       *  content limits (https://cloud.google.com/speech-to-text/quotas#content).
       */
      // const audioContent = Buffer.from('string')
    
      // Imports the Speech library
      const {SpeechClient} = require('[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)').v1p1beta1;
    
      // Instantiates a client
      const speechClient = new [SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
      async function callStreamingRecognize() {
        // Construct request
        const request = {
        };
    
        // Run request
        const stream = await speechClient.streamingRecognize();
        stream.on('data', (response) => { console.log(response) });
        stream.on('error', (err) => { throw(err) });
        stream.on('end', () => { /* API call completed */ });
        stream.write(request);
        stream.end();
      }
    
      callStreamingRecognize();
    
    

### cancelOperation(request, optionsOrCallback, callback)
    
    
    cancelOperation(request: protos.google.longrunning.CancelOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>, callback?: Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>): Promise<protos.google.protobuf.Empty>;

Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an value with a of 1, corresponding to `Code.CANCELLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### checkLongRunningRecognizeProgress(name)
    
    
    checkLongRunningRecognizeProgress(name: string): Promise<LROperation<protos.google.cloud.speech.v1p1beta1.LongRunningRecognizeResponse, protos.google.cloud.speech.v1p1beta1.LongRunningRecognizeMetadata>>;

Check the status of the long running operation returned by `longRunningRecognize()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.speech.v1p1beta1.LongRunningRecognizeResponse](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.longrunningrecognizeresponse), [protos.google.cloud.speech.v1p1beta1.LongRunningRecognizeMetadata](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.longrunningrecognizemetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Provides information to the recognizer that specifies how to
       *  process the request.
       */
      // const config = {}
      /**
       *  Required. The audio data to be recognized.
       */
      // const audio = {}
      /**
       *  Optional. Specifies an optional destination for the recognition results.
       */
      // const outputConfig = {}
    
      // Imports the Speech library
      const {SpeechClient} = require('[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)').v1p1beta1;
    
      // Instantiates a client
      const speechClient = new [SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
      async function callLongRunningRecognize() {
        // Construct request
        const request = {
          config,
          audio,
        };
    
        // Run request
        const [operation] = await speechClient.longRunningRecognize(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callLongRunningRecognize();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### customClassPath(project, location, customClass)
    
    
    customClassPath(project: string, location: string, customClass: string): string;

Return a fully-qualified customClass resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`customClass` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### deleteOperation(request, optionsOrCallback, callback)
    
    
    deleteOperation(request: protos.google.longrunning.DeleteOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.protobuf.Empty, protos.google.longrunning.DeleteOperationRequest, {} | null | undefined>, callback?: Callback<protos.google.protobuf.Empty, protos.google.longrunning.DeleteOperationRequest, {} | null | undefined>): Promise<protos.google.protobuf.Empty>;

Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### getOperation(request, optionsOrCallback, callback)
    
    
    getOperation(request: protos.google.longrunning.GetOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>, callback?: Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>): Promise<[protos.google.longrunning.Operation]>;

Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.longrunning.operation)]>` |   
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
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
**Example**
    
    
    const client = longrunning.operationsClient();
    for await (const response of client.listOperationsAsync(request));
    // doThingsWith(response)
    

### longRunningRecognize(request, options)
    
    
    longRunningRecognize(request?: protos.google.cloud.speech.v1p1beta1.ILongRunningRecognizeRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.speech.v1p1beta1.ILongRunningRecognizeResponse, protos.google.cloud.speech.v1p1beta1.ILongRunningRecognizeMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Performs asynchronous speech recognition: receive results via the google.longrunning.Operations interface. Returns either an `Operation.error` or an `Operation.response` which contains a `LongRunningRecognizeResponse` message. For more information on asynchronous speech recognition, see the [how-to](<https://cloud.google.com/speech-to-text/docs/async-recognize>).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILongRunningRecognizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.ilongrunningrecognizerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.speech.v1p1beta1.ILongRunningRecognizeResponse](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.ilongrunningrecognizeresponse), [protos.google.cloud.speech.v1p1beta1.ILongRunningRecognizeMetadata](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.ilongrunningrecognizemetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Provides information to the recognizer that specifies how to
       *  process the request.
       */
      // const config = {}
      /**
       *  Required. The audio data to be recognized.
       */
      // const audio = {}
      /**
       *  Optional. Specifies an optional destination for the recognition results.
       */
      // const outputConfig = {}
    
      // Imports the Speech library
      const {SpeechClient} = require('[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)').v1p1beta1;
    
      // Instantiates a client
      const speechClient = new [SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
      async function callLongRunningRecognize() {
        // Construct request
        const request = {
          config,
          audio,
        };
    
        // Run request
        const [operation] = await speechClient.longRunningRecognize(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callLongRunningRecognize();
    
    

### longRunningRecognize(request, options, callback)
    
    
    longRunningRecognize(request: protos.google.cloud.speech.v1p1beta1.ILongRunningRecognizeRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.speech.v1p1beta1.ILongRunningRecognizeResponse, protos.google.cloud.speech.v1p1beta1.ILongRunningRecognizeMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILongRunningRecognizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.ilongrunningrecognizerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.speech.v1p1beta1.ILongRunningRecognizeResponse](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.ilongrunningrecognizeresponse), [protos.google.cloud.speech.v1p1beta1.ILongRunningRecognizeMetadata](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.ilongrunningrecognizemetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### longRunningRecognize(request, callback)
    
    
    longRunningRecognize(request: protos.google.cloud.speech.v1p1beta1.ILongRunningRecognizeRequest, callback: Callback<LROperation<protos.google.cloud.speech.v1p1beta1.ILongRunningRecognizeResponse, protos.google.cloud.speech.v1p1beta1.ILongRunningRecognizeMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILongRunningRecognizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.ilongrunningrecognizerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.speech.v1p1beta1.ILongRunningRecognizeResponse](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.ilongrunningrecognizeresponse), [protos.google.cloud.speech.v1p1beta1.ILongRunningRecognizeMetadata](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.ilongrunningrecognizemetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### matchCustomClassFromCustomClassName(customClassName)
    
    
    matchCustomClassFromCustomClassName(customClassName: string): string | number;

Parse the custom_class from CustomClass resource.

**Parameter**  
---  
**Name** | **Description**  
`customClassName` |  `string`   
A fully-qualified path representing CustomClass resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the custom_class.  
  
### matchLocationFromCustomClassName(customClassName)
    
    
    matchLocationFromCustomClassName(customClassName: string): string | number;

Parse the location from CustomClass resource.

**Parameter**  
---  
**Name** | **Description**  
`customClassName` |  `string`   
A fully-qualified path representing CustomClass resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromPhraseSetName(phraseSetName)
    
    
    matchLocationFromPhraseSetName(phraseSetName: string): string | number;

Parse the location from PhraseSet resource.

**Parameter**  
---  
**Name** | **Description**  
`phraseSetName` |  `string`   
A fully-qualified path representing PhraseSet resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchPhraseSetFromPhraseSetName(phraseSetName)
    
    
    matchPhraseSetFromPhraseSetName(phraseSetName: string): string | number;

Parse the phrase_set from PhraseSet resource.

**Parameter**  
---  
**Name** | **Description**  
`phraseSetName` |  `string`   
A fully-qualified path representing PhraseSet resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the phrase_set.  
  
### matchProjectFromCustomClassName(customClassName)
    
    
    matchProjectFromCustomClassName(customClassName: string): string | number;

Parse the project from CustomClass resource.

**Parameter**  
---  
**Name** | **Description**  
`customClassName` |  `string`   
A fully-qualified path representing CustomClass resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromPhraseSetName(phraseSetName)
    
    
    matchProjectFromPhraseSetName(phraseSetName: string): string | number;

Parse the project from PhraseSet resource.

**Parameter**  
---  
**Name** | **Description**  
`phraseSetName` |  `string`   
A fully-qualified path representing PhraseSet resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### phraseSetPath(project, location, phraseSet)
    
    
    phraseSetPath(project: string, location: string, phraseSet: string): string;

Return a fully-qualified phraseSet resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`phraseSet` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### recognize(request, options)
    
    
    recognize(request?: protos.google.cloud.speech.v1p1beta1.IRecognizeRequest, options?: CallOptions): Promise<[
            protos.google.cloud.speech.v1p1beta1.IRecognizeResponse,
            protos.google.cloud.speech.v1p1beta1.IRecognizeRequest | undefined,
            {} | undefined
        ]>;

Performs synchronous speech recognition: receive results after all audio has been sent and processed.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRecognizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.irecognizerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.speech.v1p1beta1.IRecognizeResponse](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.irecognizeresponse), [protos.google.cloud.speech.v1p1beta1.IRecognizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.irecognizerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [RecognizeResponse](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.recognizeresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Provides information to the recognizer that specifies how to
       *  process the request.
       */
      // const config = {}
      /**
       *  Required. The audio data to be recognized.
       */
      // const audio = {}
    
      // Imports the Speech library
      const {SpeechClient} = require('[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)').v1p1beta1;
    
      // Instantiates a client
      const speechClient = new [SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
      async function callRecognize() {
        // Construct request
        const request = {
          config,
          audio,
        };
    
        // Run request
        const response = await speechClient.recognize(request);
        console.log(response);
      }
    
      callRecognize();
    
    

### recognize(request, options, callback)
    
    
    recognize(request: protos.google.cloud.speech.v1p1beta1.IRecognizeRequest, options: CallOptions, callback: Callback<protos.google.cloud.speech.v1p1beta1.IRecognizeResponse, protos.google.cloud.speech.v1p1beta1.IRecognizeRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRecognizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.irecognizerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.speech.v1p1beta1.IRecognizeResponse](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.irecognizeresponse), [protos.google.cloud.speech.v1p1beta1.IRecognizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.irecognizerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### recognize(request, callback)
    
    
    recognize(request: protos.google.cloud.speech.v1p1beta1.IRecognizeRequest, callback: Callback<protos.google.cloud.speech.v1p1beta1.IRecognizeResponse, protos.google.cloud.speech.v1p1beta1.IRecognizeRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRecognizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.irecognizerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.speech.v1p1beta1.IRecognizeResponse](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.irecognizeresponse), [protos.google.cloud.speech.v1p1beta1.IRecognizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v1p1beta1.irecognizerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
