---
url: https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/v1beta1.predictionserviceclient
title: Class v1beta1.PredictionServiceClient (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:26.683470+00:00
---

# Class v1beta1.PredictionServiceClient (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/v1beta1.predictionserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.PredictionServiceClient (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.1.3  4.0.1  3.1.2  2.5.2  2.4.5 

AutoML Prediction API.

On any input that is documented to expect a string parameter in snake_case or kebab-case, either of those cases is accepted. v1beta1

## Package

[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of PredictionServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new PredictionServiceClient({fallback: true}, gax); ```  
  
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

### predictionServiceStub
    
    
    predictionServiceStub?: Promise<{
            [name: string]: Function;
        }>;

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

### annotationSpecPath(project, location, dataset, annotationSpec)
    
    
    annotationSpecPath(project: string, location: string, dataset: string, annotationSpec: string): string;

Return a fully-qualified annotationSpec resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataset` |  `string`   
  
`annotationSpec` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### batchPredict(request, options)
    
    
    batchPredict(request?: protos.google.cloud.automl.v1beta1.IBatchPredictRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.automl.v1beta1.IBatchPredictResult, protos.google.cloud.automl.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Perform a batch prediction. Unlike the online , batch prediction result won't be immediately available in the response. Instead, a long running operation object is returned. User can poll the operation result via method. Once the operation is done, [BatchPredictResult](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.batchpredictresult) is returned in the [response](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation) field. Available for following ML problems: * Image Classification * Image Object Detection * Video Classification * Video Object Tracking * Text Extraction * Tables

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchPredictRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ibatchpredictrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.automl.v1beta1.IBatchPredictResult](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ibatchpredictresult), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the model requested to serve the batch prediction.
       */
      // const name = 'abc123'
      /**
       *  Required. The input configuration for batch prediction.
       */
      // const inputConfig = {}
      /**
       *  Required. The Configuration specifying where output predictions should
       *  be written.
       */
      // const outputConfig = {}
      /**
       *  Required. Additional domain-specific parameters for the predictions, any string must
       *  be up to 25000 characters long.
       *  *  For Text Classification:
       *     `score_threshold` - (float) A value from 0.0 to 1.0. When the model
       *          makes predictions for a text snippet, it will only produce results
       *          that have at least this confidence score. The default is 0.5.
       *  *  For Image Classification:
       *     `score_threshold` - (float) A value from 0.0 to 1.0. When the model
       *          makes predictions for an image, it will only produce results that
       *          have at least this confidence score. The default is 0.5.
       *  *  For Image Object Detection:
       *     `score_threshold` - (float) When Model detects objects on the image,
       *         it will only produce bounding boxes which have at least this
       *         confidence score. Value in 0 to 1 range, default is 0.5.
       *     `max_bounding_box_count` - (int64) No more than this number of bounding
       *         boxes will be produced per image. Default is 100, the
       *         requested value may be limited by server.
       *  *  For Video Classification :
       *     `score_threshold` - (float) A value from 0.0 to 1.0. When the model
       *         makes predictions for a video, it will only produce results that
       *         have at least this confidence score. The default is 0.5.
       *     `segment_classification` - (boolean) Set to true to request
       *         segment-level classification. AutoML Video Intelligence returns
       *         labels and their confidence scores for the entire segment of the
       *         video that user specified in the request configuration.
       *         The default is "true".
       *     `shot_classification` - (boolean) Set to true to request shot-level
       *         classification. AutoML Video Intelligence determines the boundaries
       *         for each camera shot in the entire segment of the video that user
       *         specified in the request configuration. AutoML Video Intelligence
       *         then returns labels and their confidence scores for each detected
       *         shot, along with the start and end time of the shot.
       *         WARNING: Model evaluation is not done for this classification type,
       *         the quality of it depends on training data, but there are no metrics
       *         provided to describe that quality. The default is "false".
       *     `1s_interval_classification` - (boolean) Set to true to request
       *         classification for a video at one-second intervals. AutoML Video
       *         Intelligence returns labels and their confidence scores for each
       *         second of the entire segment of the video that user specified in the
       *         request configuration.
       *         WARNING: Model evaluation is not done for this classification
       *         type, the quality of it depends on training data, but there are no
       *         metrics provided to describe that quality. The default is
       *         "false".
       *  *  For Tables:
       *     feature_importance - (boolean) Whether feature importance
       *         should be populated in the returned TablesAnnotations. The
       *         default is false.
       *  *  For Video Object Tracking:
       *     `score_threshold` - (float) When Model detects objects on video frames,
       *         it will only produce bounding boxes which have at least this
       *         confidence score. Value in 0 to 1 range, default is 0.5.
       *     `max_bounding_box_count` - (int64) No more than this number of bounding
       *         boxes will be returned per frame. Default is 100, the requested
       *         value may be limited by server.
       *     `min_bounding_box_size` - (float) Only bounding boxes with shortest edge
       *       at least that long as a relative value of video frame size will be
       *       returned. Value in 0 to 1 range. Default is 0.
       */
      // const params = [1,2,3,4]
    
      // Imports the Automl library
      const {PredictionServiceClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [PredictionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callBatchPredict() {
        // Construct request
        const request = {
          name,
          inputConfig,
          outputConfig,
          params,
        };
    
        // Run request
        const [operation] = await automlClient.batchPredict(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callBatchPredict();
    
    

### batchPredict(request, options, callback)
    
    
    batchPredict(request: protos.google.cloud.automl.v1beta1.IBatchPredictRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.automl.v1beta1.IBatchPredictResult, protos.google.cloud.automl.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchPredictRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ibatchpredictrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.automl.v1beta1.IBatchPredictResult](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ibatchpredictresult), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchPredict(request, callback)
    
    
    batchPredict(request: protos.google.cloud.automl.v1beta1.IBatchPredictRequest, callback: Callback<LROperation<protos.google.cloud.automl.v1beta1.IBatchPredictResult, protos.google.cloud.automl.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchPredictRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ibatchpredictrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.automl.v1beta1.IBatchPredictResult](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ibatchpredictresult), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### checkBatchPredictProgress(name)
    
    
    checkBatchPredictProgress(name: string): Promise<LROperation<protos.google.cloud.automl.v1beta1.BatchPredictResult, protos.google.cloud.automl.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `batchPredict()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.automl.v1beta1.BatchPredictResult](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.batchpredictresult), [protos.google.cloud.automl.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the model requested to serve the batch prediction.
       */
      // const name = 'abc123'
      /**
       *  Required. The input configuration for batch prediction.
       */
      // const inputConfig = {}
      /**
       *  Required. The Configuration specifying where output predictions should
       *  be written.
       */
      // const outputConfig = {}
      /**
       *  Required. Additional domain-specific parameters for the predictions, any string must
       *  be up to 25000 characters long.
       *  *  For Text Classification:
       *     `score_threshold` - (float) A value from 0.0 to 1.0. When the model
       *          makes predictions for a text snippet, it will only produce results
       *          that have at least this confidence score. The default is 0.5.
       *  *  For Image Classification:
       *     `score_threshold` - (float) A value from 0.0 to 1.0. When the model
       *          makes predictions for an image, it will only produce results that
       *          have at least this confidence score. The default is 0.5.
       *  *  For Image Object Detection:
       *     `score_threshold` - (float) When Model detects objects on the image,
       *         it will only produce bounding boxes which have at least this
       *         confidence score. Value in 0 to 1 range, default is 0.5.
       *     `max_bounding_box_count` - (int64) No more than this number of bounding
       *         boxes will be produced per image. Default is 100, the
       *         requested value may be limited by server.
       *  *  For Video Classification :
       *     `score_threshold` - (float) A value from 0.0 to 1.0. When the model
       *         makes predictions for a video, it will only produce results that
       *         have at least this confidence score. The default is 0.5.
       *     `segment_classification` - (boolean) Set to true to request
       *         segment-level classification. AutoML Video Intelligence returns
       *         labels and their confidence scores for the entire segment of the
       *         video that user specified in the request configuration.
       *         The default is "true".
       *     `shot_classification` - (boolean) Set to true to request shot-level
       *         classification. AutoML Video Intelligence determines the boundaries
       *         for each camera shot in the entire segment of the video that user
       *         specified in the request configuration. AutoML Video Intelligence
       *         then returns labels and their confidence scores for each detected
       *         shot, along with the start and end time of the shot.
       *         WARNING: Model evaluation is not done for this classification type,
       *         the quality of it depends on training data, but there are no metrics
       *         provided to describe that quality. The default is "false".
       *     `1s_interval_classification` - (boolean) Set to true to request
       *         classification for a video at one-second intervals. AutoML Video
       *         Intelligence returns labels and their confidence scores for each
       *         second of the entire segment of the video that user specified in the
       *         request configuration.
       *         WARNING: Model evaluation is not done for this classification
       *         type, the quality of it depends on training data, but there are no
       *         metrics provided to describe that quality. The default is
       *         "false".
       *  *  For Tables:
       *     feature_importance - (boolean) Whether feature importance
       *         should be populated in the returned TablesAnnotations. The
       *         default is false.
       *  *  For Video Object Tracking:
       *     `score_threshold` - (float) When Model detects objects on video frames,
       *         it will only produce bounding boxes which have at least this
       *         confidence score. Value in 0 to 1 range, default is 0.5.
       *     `max_bounding_box_count` - (int64) No more than this number of bounding
       *         boxes will be returned per frame. Default is 100, the requested
       *         value may be limited by server.
       *     `min_bounding_box_size` - (float) Only bounding boxes with shortest edge
       *       at least that long as a relative value of video frame size will be
       *       returned. Value in 0 to 1 range. Default is 0.
       */
      // const params = [1,2,3,4]
    
      // Imports the Automl library
      const {PredictionServiceClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [PredictionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callBatchPredict() {
        // Construct request
        const request = {
          name,
          inputConfig,
          outputConfig,
          params,
        };
    
        // Run request
        const [operation] = await automlClient.batchPredict(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callBatchPredict();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### columnSpecPath(project, location, dataset, tableSpec, columnSpec)
    
    
    columnSpecPath(project: string, location: string, dataset: string, tableSpec: string, columnSpec: string): string;

Return a fully-qualified columnSpec resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataset` |  `string`   
  
`tableSpec` |  `string`   
  
`columnSpec` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### datasetPath(project, location, dataset)
    
    
    datasetPath(project: string, location: string, dataset: string): string;

Return a fully-qualified dataset resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataset` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
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
  
### matchAnnotationSpecFromAnnotationSpecName(annotationSpecName)
    
    
    matchAnnotationSpecFromAnnotationSpecName(annotationSpecName: string): string | number;

Parse the annotation_spec from AnnotationSpec resource.

**Parameter**  
---  
**Name** | **Description**  
`annotationSpecName` |  `string`   
A fully-qualified path representing AnnotationSpec resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the annotation_spec.  
  
### matchColumnSpecFromColumnSpecName(columnSpecName)
    
    
    matchColumnSpecFromColumnSpecName(columnSpecName: string): string | number;

Parse the column_spec from ColumnSpec resource.

**Parameter**  
---  
**Name** | **Description**  
`columnSpecName` |  `string`   
A fully-qualified path representing ColumnSpec resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the column_spec.  
  
### matchDatasetFromAnnotationSpecName(annotationSpecName)
    
    
    matchDatasetFromAnnotationSpecName(annotationSpecName: string): string | number;

Parse the dataset from AnnotationSpec resource.

**Parameter**  
---  
**Name** | **Description**  
`annotationSpecName` |  `string`   
A fully-qualified path representing AnnotationSpec resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the dataset.  
  
### matchDatasetFromColumnSpecName(columnSpecName)
    
    
    matchDatasetFromColumnSpecName(columnSpecName: string): string | number;

Parse the dataset from ColumnSpec resource.

**Parameter**  
---  
**Name** | **Description**  
`columnSpecName` |  `string`   
A fully-qualified path representing ColumnSpec resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the dataset.  
  
### matchDatasetFromDatasetName(datasetName)
    
    
    matchDatasetFromDatasetName(datasetName: string): string | number;

Parse the dataset from Dataset resource.

**Parameter**  
---  
**Name** | **Description**  
`datasetName` |  `string`   
A fully-qualified path representing Dataset resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the dataset.  
  
### matchDatasetFromTableSpecName(tableSpecName)
    
    
    matchDatasetFromTableSpecName(tableSpecName: string): string | number;

Parse the dataset from TableSpec resource.

**Parameter**  
---  
**Name** | **Description**  
`tableSpecName` |  `string`   
A fully-qualified path representing TableSpec resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the dataset.  
  
### matchLocationFromAnnotationSpecName(annotationSpecName)
    
    
    matchLocationFromAnnotationSpecName(annotationSpecName: string): string | number;

Parse the location from AnnotationSpec resource.

**Parameter**  
---  
**Name** | **Description**  
`annotationSpecName` |  `string`   
A fully-qualified path representing AnnotationSpec resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromColumnSpecName(columnSpecName)
    
    
    matchLocationFromColumnSpecName(columnSpecName: string): string | number;

Parse the location from ColumnSpec resource.

**Parameter**  
---  
**Name** | **Description**  
`columnSpecName` |  `string`   
A fully-qualified path representing ColumnSpec resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromDatasetName(datasetName)
    
    
    matchLocationFromDatasetName(datasetName: string): string | number;

Parse the location from Dataset resource.

**Parameter**  
---  
**Name** | **Description**  
`datasetName` |  `string`   
A fully-qualified path representing Dataset resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromModelEvaluationName(modelEvaluationName)
    
    
    matchLocationFromModelEvaluationName(modelEvaluationName: string): string | number;

Parse the location from ModelEvaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`modelEvaluationName` |  `string`   
A fully-qualified path representing ModelEvaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromModelName(modelName)
    
    
    matchLocationFromModelName(modelName: string): string | number;

Parse the location from Model resource.

**Parameter**  
---  
**Name** | **Description**  
`modelName` |  `string`   
A fully-qualified path representing Model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTableSpecName(tableSpecName)
    
    
    matchLocationFromTableSpecName(tableSpecName: string): string | number;

Parse the location from TableSpec resource.

**Parameter**  
---  
**Name** | **Description**  
`tableSpecName` |  `string`   
A fully-qualified path representing TableSpec resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchModelEvaluationFromModelEvaluationName(modelEvaluationName)
    
    
    matchModelEvaluationFromModelEvaluationName(modelEvaluationName: string): string | number;

Parse the model_evaluation from ModelEvaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`modelEvaluationName` |  `string`   
A fully-qualified path representing ModelEvaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the model_evaluation.  
  
### matchModelFromModelEvaluationName(modelEvaluationName)
    
    
    matchModelFromModelEvaluationName(modelEvaluationName: string): string | number;

Parse the model from ModelEvaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`modelEvaluationName` |  `string`   
A fully-qualified path representing ModelEvaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the model.  
  
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
  
### matchProjectFromAnnotationSpecName(annotationSpecName)
    
    
    matchProjectFromAnnotationSpecName(annotationSpecName: string): string | number;

Parse the project from AnnotationSpec resource.

**Parameter**  
---  
**Name** | **Description**  
`annotationSpecName` |  `string`   
A fully-qualified path representing AnnotationSpec resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromColumnSpecName(columnSpecName)
    
    
    matchProjectFromColumnSpecName(columnSpecName: string): string | number;

Parse the project from ColumnSpec resource.

**Parameter**  
---  
**Name** | **Description**  
`columnSpecName` |  `string`   
A fully-qualified path representing ColumnSpec resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromDatasetName(datasetName)
    
    
    matchProjectFromDatasetName(datasetName: string): string | number;

Parse the project from Dataset resource.

**Parameter**  
---  
**Name** | **Description**  
`datasetName` |  `string`   
A fully-qualified path representing Dataset resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromModelEvaluationName(modelEvaluationName)
    
    
    matchProjectFromModelEvaluationName(modelEvaluationName: string): string | number;

Parse the project from ModelEvaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`modelEvaluationName` |  `string`   
A fully-qualified path representing ModelEvaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromModelName(modelName)
    
    
    matchProjectFromModelName(modelName: string): string | number;

Parse the project from Model resource.

**Parameter**  
---  
**Name** | **Description**  
`modelName` |  `string`   
A fully-qualified path representing Model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTableSpecName(tableSpecName)
    
    
    matchProjectFromTableSpecName(tableSpecName: string): string | number;

Parse the project from TableSpec resource.

**Parameter**  
---  
**Name** | **Description**  
`tableSpecName` |  `string`   
A fully-qualified path representing TableSpec resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchTableSpecFromColumnSpecName(columnSpecName)
    
    
    matchTableSpecFromColumnSpecName(columnSpecName: string): string | number;

Parse the table_spec from ColumnSpec resource.

**Parameter**  
---  
**Name** | **Description**  
`columnSpecName` |  `string`   
A fully-qualified path representing ColumnSpec resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the table_spec.  
  
### matchTableSpecFromTableSpecName(tableSpecName)
    
    
    matchTableSpecFromTableSpecName(tableSpecName: string): string | number;

Parse the table_spec from TableSpec resource.

**Parameter**  
---  
**Name** | **Description**  
`tableSpecName` |  `string`   
A fully-qualified path representing TableSpec resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the table_spec.  
  
### modelEvaluationPath(project, location, model, modelEvaluation)
    
    
    modelEvaluationPath(project: string, location: string, model: string, modelEvaluation: string): string;

Return a fully-qualified modelEvaluation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`model` |  `string`   
  
`modelEvaluation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### modelPath(project, location, model)
    
    
    modelPath(project: string, location: string, model: string): string;

Return a fully-qualified model resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`model` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### predict(request, options)
    
    
    predict(request?: protos.google.cloud.automl.v1beta1.IPredictRequest, options?: CallOptions): Promise<[
            protos.google.cloud.automl.v1beta1.IPredictResponse,
            protos.google.cloud.automl.v1beta1.IPredictRequest | undefined,
            {} | undefined
        ]>;

Perform an online prediction. The prediction result will be directly returned in the response. Available for following ML problems, and their expected request payloads: * Image Classification - Image in .JPEG, .GIF or .PNG format, image_bytes up to 30MB. * Image Object Detection - Image in .JPEG, .GIF or .PNG format, image_bytes up to 30MB. * Text Classification - TextSnippet, content up to 60,000 characters, UTF-8 encoded. * Text Extraction - TextSnippet, content up to 30,000 characters, UTF-8 NFC encoded. * Translation - TextSnippet, content up to 25,000 characters, UTF-8 encoded. * Tables - Row, with column values matching the columns of the model, up to 5MB. Not available for FORECASTING

. * Text Sentiment - TextSnippet, content up 500 characters, UTF-8 encoded.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPredictRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ipredictrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.automl.v1beta1.IPredictResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ipredictresponse), [protos.google.cloud.automl.v1beta1.IPredictRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ipredictrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [PredictResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.predictresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the model requested to serve the prediction.
       */
      // const name = 'abc123'
      /**
       *  Required. Payload to perform a prediction on. The payload must match the
       *  problem type that the model was trained to solve.
       */
      // const payload = {}
      /**
       *  Additional domain-specific parameters, any string must be up to 25000
       *  characters long.
       *  *  For Image Classification:
       *     `score_threshold` - (float) A value from 0.0 to 1.0. When the model
       *      makes predictions for an image, it will only produce results that have
       *      at least this confidence score. The default is 0.5.
       *   *  For Image Object Detection:
       *     `score_threshold` - (float) When Model detects objects on the image,
       *         it will only produce bounding boxes which have at least this
       *         confidence score. Value in 0 to 1 range, default is 0.5.
       *     `max_bounding_box_count` - (int64) No more than this number of bounding
       *         boxes will be returned in the response. Default is 100, the
       *         requested value may be limited by server.
       *  *  For Tables:
       *     feature_importance - (boolean) Whether feature importance
       *         should be populated in the returned TablesAnnotation.
       *         The default is false.
       */
      // const params = [1,2,3,4]
    
      // Imports the Automl library
      const {PredictionServiceClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [PredictionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callPredict() {
        // Construct request
        const request = {
          name,
          payload,
        };
    
        // Run request
        const response = await automlClient.predict(request);
        console.log(response);
      }
    
      callPredict();
    
    

### predict(request, options, callback)
    
    
    predict(request: protos.google.cloud.automl.v1beta1.IPredictRequest, options: CallOptions, callback: Callback<protos.google.cloud.automl.v1beta1.IPredictResponse, protos.google.cloud.automl.v1beta1.IPredictRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPredictRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ipredictrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.IPredictResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ipredictresponse), [protos.google.cloud.automl.v1beta1.IPredictRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ipredictrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### predict(request, callback)
    
    
    predict(request: protos.google.cloud.automl.v1beta1.IPredictRequest, callback: Callback<protos.google.cloud.automl.v1beta1.IPredictResponse, protos.google.cloud.automl.v1beta1.IPredictRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPredictRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ipredictrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.IPredictResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ipredictresponse), [protos.google.cloud.automl.v1beta1.IPredictRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ipredictrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### tableSpecPath(project, location, dataset, tableSpec)
    
    
    tableSpecPath(project: string, location: string, dataset: string, tableSpec: string): string;

Return a fully-qualified tableSpec resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataset` |  `string`   
  
`tableSpec` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
