---
url: https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/v1p3beta1.videointelligenceserviceclient
title: Class v1p3beta1.VideoIntelligenceServiceClient (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:11.686218+00:00
---

# Class v1p3beta1.VideoIntelligenceServiceClient (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/v1p3beta1.videointelligenceserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1p3beta1.VideoIntelligenceServiceClient (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.1.0  5.0.2  4.2.2  4.1.1  3.4.1  3.3.6  3.1.0  3.0.0 

Service that implements the Video Intelligence API. v1p3beta1

## Package

[@google-cloud/video-intelligence](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of VideoIntelligenceServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new VideoIntelligenceServiceClient({fallback: true}, gax); ```  
  
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

### universeDomain
    
    
    get universeDomain(): string;

### videoIntelligenceServiceStub
    
    
    videoIntelligenceServiceStub?: Promise<{
            [name: string]: Function;
        }>;

### warn
    
    
    warn: (code: string, message: string, warnType?: string) => void;

## Methods 

### annotateVideo(request, options)
    
    
    annotateVideo(request?: protos.google.cloud.videointelligence.v1p3beta1.IAnnotateVideoRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.videointelligence.v1p3beta1.IAnnotateVideoResponse, protos.google.cloud.videointelligence.v1p3beta1.IAnnotateVideoProgress>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Performs asynchronous video annotation. Progress and results can be retrieved through the `google.longrunning.Operations` interface. `Operation.metadata` contains `AnnotateVideoProgress` (progress). `Operation.response` contains `AnnotateVideoResponse` (results).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnnotateVideoRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p3beta1.iannotatevideorequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.videointelligence.v1p3beta1.IAnnotateVideoResponse](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p3beta1.iannotatevideoresponse), [protos.google.cloud.videointelligence.v1p3beta1.IAnnotateVideoProgress](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p3beta1.iannotatevideoprogress)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Input video location. Currently, only
       *  Cloud Storage (https://cloud.google.com/storage/) URIs are
       *  supported. URIs must be specified in the following format:
       *  `gs://bucket-id/object-id` (other URI formats return
       *  google.rpc.Code.INVALID_ARGUMENT google.rpc.Code.INVALID_ARGUMENT). For
       *  more information, see Request
       *  URIs (https://cloud.google.com/storage/docs/request-endpoints). To identify
       *  multiple videos, a video URI may include wildcards in the `object-id`.
       *  Supported wildcards: '*' to match 0 or more characters;
       *  '?' to match 1 character. If unset, the input video should be embedded
       *  in the request as `input_content`. If set, `input_content` must be unset.
       */
      // const inputUri = 'abc123'
      /**
       *  The video data bytes.
       *  If unset, the input video(s) should be specified via the `input_uri`.
       *  If set, `input_uri` must be unset.
       */
      // const inputContent = Buffer.from('string')
      /**
       *  Required. Requested video annotation features.
       */
      // const features = [1,2,3,4]
      /**
       *  Additional video context and/or feature-specific parameters.
       */
      // const videoContext = {}
      /**
       *  Optional. Location where the output (in JSON format) should be stored.
       *  Currently, only Cloud Storage (https://cloud.google.com/storage/)
       *  URIs are supported. These must be specified in the following format:
       *  `gs://bucket-id/object-id` (other URI formats return
       *  google.rpc.Code.INVALID_ARGUMENT google.rpc.Code.INVALID_ARGUMENT). For
       *  more information, see Request
       *  URIs (https://cloud.google.com/storage/docs/request-endpoints).
       */
      // const outputUri = 'abc123'
      /**
       *  Optional. Cloud region where annotation should take place. Supported cloud
       *  regions are: `us-east1`, `us-west1`, `europe-west1`, `asia-east1`. If no
       *  region is specified, the region will be determined based on video file
       *  location.
       */
      // const locationId = 'abc123'
    
      // Imports the Videointelligence library
      const {VideoIntelligenceServiceClient} = require('[@google-cloud/video-intelligence](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)').v1p3beta1;
    
      // Instantiates a client
      const videointelligenceClient = new [VideoIntelligenceServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)();
    
      async function callAnnotateVideo() {
        // Construct request
        const request = {
          features,
        };
    
        // Run request
        const [operation] = await videointelligenceClient.annotateVideo(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callAnnotateVideo();
    
    

### annotateVideo(request, options, callback)
    
    
    annotateVideo(request: protos.google.cloud.videointelligence.v1p3beta1.IAnnotateVideoRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.videointelligence.v1p3beta1.IAnnotateVideoResponse, protos.google.cloud.videointelligence.v1p3beta1.IAnnotateVideoProgress>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnnotateVideoRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p3beta1.iannotatevideorequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.videointelligence.v1p3beta1.IAnnotateVideoResponse](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p3beta1.iannotatevideoresponse), [protos.google.cloud.videointelligence.v1p3beta1.IAnnotateVideoProgress](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p3beta1.iannotatevideoprogress)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### annotateVideo(request, callback)
    
    
    annotateVideo(request: protos.google.cloud.videointelligence.v1p3beta1.IAnnotateVideoRequest, callback: Callback<LROperation<protos.google.cloud.videointelligence.v1p3beta1.IAnnotateVideoResponse, protos.google.cloud.videointelligence.v1p3beta1.IAnnotateVideoProgress>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnnotateVideoRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p3beta1.iannotatevideorequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.videointelligence.v1p3beta1.IAnnotateVideoResponse](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p3beta1.iannotatevideoresponse), [protos.google.cloud.videointelligence.v1p3beta1.IAnnotateVideoProgress](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p3beta1.iannotatevideoprogress)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### checkAnnotateVideoProgress(name)
    
    
    checkAnnotateVideoProgress(name: string): Promise<LROperation<protos.google.cloud.videointelligence.v1p3beta1.AnnotateVideoResponse, protos.google.cloud.videointelligence.v1p3beta1.AnnotateVideoProgress>>;

Check the status of the long running operation returned by `annotateVideo()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.videointelligence.v1p3beta1.AnnotateVideoResponse](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p3beta1.annotatevideoresponse), [protos.google.cloud.videointelligence.v1p3beta1.AnnotateVideoProgress](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p3beta1.annotatevideoprogress)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Input video location. Currently, only
       *  Cloud Storage (https://cloud.google.com/storage/) URIs are
       *  supported. URIs must be specified in the following format:
       *  `gs://bucket-id/object-id` (other URI formats return
       *  google.rpc.Code.INVALID_ARGUMENT google.rpc.Code.INVALID_ARGUMENT). For
       *  more information, see Request
       *  URIs (https://cloud.google.com/storage/docs/request-endpoints). To identify
       *  multiple videos, a video URI may include wildcards in the `object-id`.
       *  Supported wildcards: '*' to match 0 or more characters;
       *  '?' to match 1 character. If unset, the input video should be embedded
       *  in the request as `input_content`. If set, `input_content` must be unset.
       */
      // const inputUri = 'abc123'
      /**
       *  The video data bytes.
       *  If unset, the input video(s) should be specified via the `input_uri`.
       *  If set, `input_uri` must be unset.
       */
      // const inputContent = Buffer.from('string')
      /**
       *  Required. Requested video annotation features.
       */
      // const features = [1,2,3,4]
      /**
       *  Additional video context and/or feature-specific parameters.
       */
      // const videoContext = {}
      /**
       *  Optional. Location where the output (in JSON format) should be stored.
       *  Currently, only Cloud Storage (https://cloud.google.com/storage/)
       *  URIs are supported. These must be specified in the following format:
       *  `gs://bucket-id/object-id` (other URI formats return
       *  google.rpc.Code.INVALID_ARGUMENT google.rpc.Code.INVALID_ARGUMENT). For
       *  more information, see Request
       *  URIs (https://cloud.google.com/storage/docs/request-endpoints).
       */
      // const outputUri = 'abc123'
      /**
       *  Optional. Cloud region where annotation should take place. Supported cloud
       *  regions are: `us-east1`, `us-west1`, `europe-west1`, `asia-east1`. If no
       *  region is specified, the region will be determined based on video file
       *  location.
       */
      // const locationId = 'abc123'
    
      // Imports the Videointelligence library
      const {VideoIntelligenceServiceClient} = require('[@google-cloud/video-intelligence](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)').v1p3beta1;
    
      // Instantiates a client
      const videointelligenceClient = new [VideoIntelligenceServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)();
    
      async function callAnnotateVideo() {
        // Construct request
        const request = {
          features,
        };
    
        // Run request
        const [operation] = await videointelligenceClient.annotateVideo(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callAnnotateVideo();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
