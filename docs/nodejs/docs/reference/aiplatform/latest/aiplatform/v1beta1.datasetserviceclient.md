---
url: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/v1beta1.datasetserviceclient
title: Class v1beta1.DatasetServiceClient (7.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:12:06.291158+00:00
---

# Class v1beta1.DatasetServiceClient (7.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/v1beta1.datasetserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.DatasetServiceClient (7.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.4.1 (latest)  7.3.0  6.10.0  6.9.0  6.8.1  6.6.0  6.4.0  6.3.0  6.2.0  6.1.0  6.0.0  5.14.0  5.13.0  3.15.0  3.13.0  3.11.0  3.10.1  3.9.0  3.7.0  3.6.0  3.4.0  3.3.0  3.0.0  2.12.0  2.11.0  2.10.0  2.7.0  2.6.1  2.5.0  2.3.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0  1.11.0  1.7.2 

The service that manages Vertex AI Dataset and its child resources. v1beta1

## Package

[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of DatasetServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new DatasetServiceClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### datasetServiceStub
    
    
    datasetServiceStub?: Promise<{
            [name: string]: Function;
        }>;

### descriptors
    
    
    descriptors: Descriptors;

### iamClient
    
    
    iamClient: IamClient;

### innerApiCalls
    
    
    innerApiCalls: {
            [name: string]: Function;
        };

### locationsClient
    
    
    locationsClient: LocationsClient;

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

### universeDomain
    
    
    get universeDomain(): string;

### warn
    
    
    warn: (code: string, message: string, warnType?: string) => void;

## Methods 

### annotationPath(project, location, dataset, dataItem, annotation)
    
    
    annotationPath(project: string, location: string, dataset: string, dataItem: string, annotation: string): string;

Return a fully-qualified annotation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataset` |  `string`   
  
`dataItem` |  `string`   
  
`annotation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
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
  
### artifactPath(project, location, metadataStore, artifact)
    
    
    artifactPath(project: string, location: string, metadataStore: string, artifact: string): string;

Return a fully-qualified artifact resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`metadataStore` |  `string`   
  
`artifact` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### assembleData(request, options)
    
    
    assembleData(request?: protos.google.cloud.aiplatform.v1beta1.IAssembleDataRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.aiplatform.v1beta1.IAssembleDataResponse, protos.google.cloud.aiplatform.v1beta1.IAssembleDataOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Assembles each row of a multimodal dataset and writes the result into a BigQuery table.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAssembleDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassembledatarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.aiplatform.v1beta1.IAssembleDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassembledataresponse), [protos.google.cloud.aiplatform.v1beta1.IAssembleDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassembledataoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Dataset resource (used only for MULTIMODAL
       *  datasets). Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}`
       */
      // const name = 'abc123'
      /**
       *  Optional. The read config for the dataset.
       */
      // const geminiRequestReadConfig = {}
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callAssembleData() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.assembleData(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callAssembleData();
    
    

### assembleData(request, options, callback)
    
    
    assembleData(request: protos.google.cloud.aiplatform.v1beta1.IAssembleDataRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IAssembleDataResponse, protos.google.cloud.aiplatform.v1beta1.IAssembleDataOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAssembleDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassembledatarequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IAssembleDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassembledataresponse), [protos.google.cloud.aiplatform.v1beta1.IAssembleDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassembledataoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### assembleData(request, callback)
    
    
    assembleData(request: protos.google.cloud.aiplatform.v1beta1.IAssembleDataRequest, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IAssembleDataResponse, protos.google.cloud.aiplatform.v1beta1.IAssembleDataOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAssembleDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassembledatarequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IAssembleDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassembledataresponse), [protos.google.cloud.aiplatform.v1beta1.IAssembleDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassembledataoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### assessData(request, options)
    
    
    assessData(request?: protos.google.cloud.aiplatform.v1beta1.IAssessDataRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.aiplatform.v1beta1.IAssessDataResponse, protos.google.cloud.aiplatform.v1beta1.IAssessDataOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Assesses the state or validity of the dataset with respect to a given use case.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAssessDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassessdatarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.aiplatform.v1beta1.IAssessDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassessdataresponse), [protos.google.cloud.aiplatform.v1beta1.IAssessDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassessdataoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Configuration for the tuning validation assessment.
       */
      // const tuningValidationAssessmentConfig = {}
      /**
       *  Optional. Configuration for the tuning resource usage assessment.
       */
      // const tuningResourceUsageAssessmentConfig = {}
      /**
       *  Optional. Configuration for the batch prediction validation assessment.
       */
      // const batchPredictionValidationAssessmentConfig = {}
      /**
       *  Optional. Configuration for the batch prediction resource usage
       *  assessment.
       */
      // const batchPredictionResourceUsageAssessmentConfig = {}
      /**
       *  Required. The name of the Dataset resource. Used only for MULTIMODAL
       *  datasets. Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}`
       */
      // const name = 'abc123'
      /**
       *  Optional. The Gemini request read config for the dataset.
       */
      // const geminiRequestReadConfig = {}
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callAssessData() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.assessData(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callAssessData();
    
    

### assessData(request, options, callback)
    
    
    assessData(request: protos.google.cloud.aiplatform.v1beta1.IAssessDataRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IAssessDataResponse, protos.google.cloud.aiplatform.v1beta1.IAssessDataOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAssessDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassessdatarequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IAssessDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassessdataresponse), [protos.google.cloud.aiplatform.v1beta1.IAssessDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassessdataoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### assessData(request, callback)
    
    
    assessData(request: protos.google.cloud.aiplatform.v1beta1.IAssessDataRequest, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IAssessDataResponse, protos.google.cloud.aiplatform.v1beta1.IAssessDataOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAssessDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassessdatarequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IAssessDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassessdataresponse), [protos.google.cloud.aiplatform.v1beta1.IAssessDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iassessdataoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchPredictionJobPath(project, location, batchPredictionJob)
    
    
    batchPredictionJobPath(project: string, location: string, batchPredictionJob: string): string;

Return a fully-qualified batchPredictionJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`batchPredictionJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### cachedContentPath(project, location, cachedContent)
    
    
    cachedContentPath(project: string, location: string, cachedContent: string): string;

Return a fully-qualified cachedContent resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`cachedContent` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### cancelOperation(request, optionsOrCallback, callback)
    
    
    cancelOperation(request: protos.google.longrunning.CancelOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>, callback?: Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>): Promise<protos.google.protobuf.Empty>;

Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an value with a of 1, corresponding to `Code.CANCELLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### checkAssembleDataProgress(name)
    
    
    checkAssembleDataProgress(name: string): Promise<LROperation<protos.google.cloud.aiplatform.v1beta1.AssembleDataResponse, protos.google.cloud.aiplatform.v1beta1.AssembleDataOperationMetadata>>;

Check the status of the long running operation returned by `assembleData()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.aiplatform.v1beta1.AssembleDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.assembledataresponse), [protos.google.cloud.aiplatform.v1beta1.AssembleDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.assembledataoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Dataset resource (used only for MULTIMODAL
       *  datasets). Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}`
       */
      // const name = 'abc123'
      /**
       *  Optional. The read config for the dataset.
       */
      // const geminiRequestReadConfig = {}
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callAssembleData() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.assembleData(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callAssembleData();
    
    

### checkAssessDataProgress(name)
    
    
    checkAssessDataProgress(name: string): Promise<LROperation<protos.google.cloud.aiplatform.v1beta1.AssessDataResponse, protos.google.cloud.aiplatform.v1beta1.AssessDataOperationMetadata>>;

Check the status of the long running operation returned by `assessData()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.aiplatform.v1beta1.AssessDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.assessdataresponse-class), [protos.google.cloud.aiplatform.v1beta1.AssessDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.assessdataoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Configuration for the tuning validation assessment.
       */
      // const tuningValidationAssessmentConfig = {}
      /**
       *  Optional. Configuration for the tuning resource usage assessment.
       */
      // const tuningResourceUsageAssessmentConfig = {}
      /**
       *  Optional. Configuration for the batch prediction validation assessment.
       */
      // const batchPredictionValidationAssessmentConfig = {}
      /**
       *  Optional. Configuration for the batch prediction resource usage
       *  assessment.
       */
      // const batchPredictionResourceUsageAssessmentConfig = {}
      /**
       *  Required. The name of the Dataset resource. Used only for MULTIMODAL
       *  datasets. Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}`
       */
      // const name = 'abc123'
      /**
       *  Optional. The Gemini request read config for the dataset.
       */
      // const geminiRequestReadConfig = {}
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callAssessData() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.assessData(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callAssessData();
    
    

### checkCreateDatasetProgress(name)
    
    
    checkCreateDatasetProgress(name: string): Promise<LROperation<protos.google.cloud.aiplatform.v1beta1.Dataset, protos.google.cloud.aiplatform.v1beta1.CreateDatasetOperationMetadata>>;

Check the status of the long running operation returned by `createDataset()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.aiplatform.v1beta1.Dataset](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.dataset), [protos.google.cloud.aiplatform.v1beta1.CreateDatasetOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.createdatasetoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Location to create the Dataset in.
       *  Format: `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The Dataset to create.
       */
      // const dataset = {}
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callCreateDataset() {
        // Construct request
        const request = {
          parent,
          dataset,
        };
    
        // Run request
        const [operation] = await aiplatformClient.createDataset(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateDataset();
    
    

### checkCreateDatasetVersionProgress(name)
    
    
    checkCreateDatasetVersionProgress(name: string): Promise<LROperation<protos.google.cloud.aiplatform.v1beta1.DatasetVersion, protos.google.cloud.aiplatform.v1beta1.CreateDatasetVersionOperationMetadata>>;

Check the status of the long running operation returned by `createDatasetVersion()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.aiplatform.v1beta1.DatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.datasetversion), [protos.google.cloud.aiplatform.v1beta1.CreateDatasetVersionOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.createdatasetversionoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Dataset resource.
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The version to be created. The same CMEK policies with the
       *  original Dataset will be applied the dataset version. So here we don't need
       *  to specify the EncryptionSpecType here.
       */
      // const datasetVersion = {}
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callCreateDatasetVersion() {
        // Construct request
        const request = {
          parent,
          datasetVersion,
        };
    
        // Run request
        const [operation] = await aiplatformClient.createDatasetVersion(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateDatasetVersion();
    
    

### checkDeleteDatasetProgress(name)
    
    
    checkDeleteDatasetProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata>>;

Check the status of the long running operation returned by `deleteDataset()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.empty), [protos.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.deleteoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Dataset to delete.
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteDataset() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.deleteDataset(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteDataset();
    
    

### checkDeleteDatasetVersionProgress(name)
    
    
    checkDeleteDatasetVersionProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata>>;

Check the status of the long running operation returned by `deleteDatasetVersion()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.empty), [protos.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.deleteoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Dataset version to delete.
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}/datasetVersions/{dataset_version}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteDatasetVersion() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.deleteDatasetVersion(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteDatasetVersion();
    
    

### checkDeleteSavedQueryProgress(name)
    
    
    checkDeleteSavedQueryProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata>>;

Check the status of the long running operation returned by `deleteSavedQuery()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.empty), [protos.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.deleteoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the SavedQuery to delete.
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}/savedQueries/{saved_query}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteSavedQuery() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.deleteSavedQuery(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteSavedQuery();
    
    

### checkExportDataProgress(name)
    
    
    checkExportDataProgress(name: string): Promise<LROperation<protos.google.cloud.aiplatform.v1beta1.ExportDataResponse, protos.google.cloud.aiplatform.v1beta1.ExportDataOperationMetadata>>;

Check the status of the long running operation returned by `exportData()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.aiplatform.v1beta1.ExportDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.exportdataresponse), [protos.google.cloud.aiplatform.v1beta1.ExportDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.exportdataoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Dataset resource.
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}`
       */
      // const name = 'abc123'
      /**
       *  Required. The desired output location.
       */
      // const exportConfig = {}
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callExportData() {
        // Construct request
        const request = {
          name,
          exportConfig,
        };
    
        // Run request
        const [operation] = await aiplatformClient.exportData(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportData();
    
    

### checkImportDataProgress(name)
    
    
    checkImportDataProgress(name: string): Promise<LROperation<protos.google.cloud.aiplatform.v1beta1.ImportDataResponse, protos.google.cloud.aiplatform.v1beta1.ImportDataOperationMetadata>>;

Check the status of the long running operation returned by `importData()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.aiplatform.v1beta1.ImportDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.importdataresponse), [protos.google.cloud.aiplatform.v1beta1.ImportDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.importdataoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Dataset resource.
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}`
       */
      // const name = 'abc123'
      /**
       *  Required. The desired input locations. The contents of all input locations
       *  will be imported in one batch.
       */
      // const importConfigs = [1,2,3,4]
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callImportData() {
        // Construct request
        const request = {
          name,
          importConfigs,
        };
    
        // Run request
        const [operation] = await aiplatformClient.importData(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callImportData();
    
    

### checkRestoreDatasetVersionProgress(name)
    
    
    checkRestoreDatasetVersionProgress(name: string): Promise<LROperation<protos.google.cloud.aiplatform.v1beta1.DatasetVersion, protos.google.cloud.aiplatform.v1beta1.RestoreDatasetVersionOperationMetadata>>;

Check the status of the long running operation returned by `restoreDatasetVersion()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.aiplatform.v1beta1.DatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.datasetversion), [protos.google.cloud.aiplatform.v1beta1.RestoreDatasetVersionOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.restoredatasetversionoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the DatasetVersion resource.
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}/datasetVersions/{dataset_version}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callRestoreDatasetVersion() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.restoreDatasetVersion(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callRestoreDatasetVersion();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### contextPath(project, location, metadataStore, context)
    
    
    contextPath(project: string, location: string, metadataStore: string, context: string): string;

Return a fully-qualified context resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`metadataStore` |  `string`   
  
`context` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### createDataset(request, options)
    
    
    createDataset(request?: protos.google.cloud.aiplatform.v1beta1.ICreateDatasetRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.aiplatform.v1beta1.IDataset, protos.google.cloud.aiplatform.v1beta1.ICreateDatasetOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatedatasetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.aiplatform.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idataset), [protos.google.cloud.aiplatform.v1beta1.ICreateDatasetOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatedatasetoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Location to create the Dataset in.
       *  Format: `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The Dataset to create.
       */
      // const dataset = {}
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callCreateDataset() {
        // Construct request
        const request = {
          parent,
          dataset,
        };
    
        // Run request
        const [operation] = await aiplatformClient.createDataset(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateDataset();
    
    

### createDataset(request, options, callback)
    
    
    createDataset(request: protos.google.cloud.aiplatform.v1beta1.ICreateDatasetRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IDataset, protos.google.cloud.aiplatform.v1beta1.ICreateDatasetOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatedatasetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idataset), [protos.google.cloud.aiplatform.v1beta1.ICreateDatasetOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatedatasetoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataset(request, callback)
    
    
    createDataset(request: protos.google.cloud.aiplatform.v1beta1.ICreateDatasetRequest, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IDataset, protos.google.cloud.aiplatform.v1beta1.ICreateDatasetOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatedatasetrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idataset), [protos.google.cloud.aiplatform.v1beta1.ICreateDatasetOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatedatasetoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDatasetVersion(request, options)
    
    
    createDatasetVersion(request?: protos.google.cloud.aiplatform.v1beta1.ICreateDatasetVersionRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.aiplatform.v1beta1.IDatasetVersion, protos.google.cloud.aiplatform.v1beta1.ICreateDatasetVersionOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Create a version from a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatedatasetversionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.aiplatform.v1beta1.IDatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idatasetversion), [protos.google.cloud.aiplatform.v1beta1.ICreateDatasetVersionOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatedatasetversionoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Dataset resource.
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The version to be created. The same CMEK policies with the
       *  original Dataset will be applied the dataset version. So here we don't need
       *  to specify the EncryptionSpecType here.
       */
      // const datasetVersion = {}
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callCreateDatasetVersion() {
        // Construct request
        const request = {
          parent,
          datasetVersion,
        };
    
        // Run request
        const [operation] = await aiplatformClient.createDatasetVersion(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateDatasetVersion();
    
    

### createDatasetVersion(request, options, callback)
    
    
    createDatasetVersion(request: protos.google.cloud.aiplatform.v1beta1.ICreateDatasetVersionRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IDatasetVersion, protos.google.cloud.aiplatform.v1beta1.ICreateDatasetVersionOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatedatasetversionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IDatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idatasetversion), [protos.google.cloud.aiplatform.v1beta1.ICreateDatasetVersionOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatedatasetversionoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDatasetVersion(request, callback)
    
    
    createDatasetVersion(request: protos.google.cloud.aiplatform.v1beta1.ICreateDatasetVersionRequest, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IDatasetVersion, protos.google.cloud.aiplatform.v1beta1.ICreateDatasetVersionOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatedatasetversionrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IDatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idatasetversion), [protos.google.cloud.aiplatform.v1beta1.ICreateDatasetVersionOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatedatasetversionoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### customJobPath(project, location, customJob)
    
    
    customJobPath(project: string, location: string, customJob: string): string;

Return a fully-qualified customJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`customJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### dataItemPath(project, location, dataset, dataItem)
    
    
    dataItemPath(project: string, location: string, dataset: string, dataItem: string): string;

Return a fully-qualified dataItem resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataset` |  `string`   
  
`dataItem` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### dataLabelingJobPath(project, location, dataLabelingJob)
    
    
    dataLabelingJobPath(project: string, location: string, dataLabelingJob: string): string;

Return a fully-qualified dataLabelingJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataLabelingJob` |  `string`   
  
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
  
### datasetVersionPath(project, location, dataset, datasetVersion)
    
    
    datasetVersionPath(project: string, location: string, dataset: string, datasetVersion: string): string;

Return a fully-qualified datasetVersion resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataset` |  `string`   
  
`datasetVersion` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### deleteDataset(request, options)
    
    
    deleteDataset(request?: protos.google.cloud.aiplatform.v1beta1.IDeleteDatasetRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletedatasetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Dataset to delete.
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteDataset() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.deleteDataset(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteDataset();
    
    

### deleteDataset(request, options, callback)
    
    
    deleteDataset(request: protos.google.cloud.aiplatform.v1beta1.IDeleteDatasetRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletedatasetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataset(request, callback)
    
    
    deleteDataset(request: protos.google.cloud.aiplatform.v1beta1.IDeleteDatasetRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletedatasetrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDatasetVersion(request, options)
    
    
    deleteDatasetVersion(request?: protos.google.cloud.aiplatform.v1beta1.IDeleteDatasetVersionRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a Dataset version.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletedatasetversionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Dataset version to delete.
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}/datasetVersions/{dataset_version}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteDatasetVersion() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.deleteDatasetVersion(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteDatasetVersion();
    
    

### deleteDatasetVersion(request, options, callback)
    
    
    deleteDatasetVersion(request: protos.google.cloud.aiplatform.v1beta1.IDeleteDatasetVersionRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletedatasetversionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDatasetVersion(request, callback)
    
    
    deleteDatasetVersion(request: protos.google.cloud.aiplatform.v1beta1.IDeleteDatasetVersionRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletedatasetversionrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteOperation(request, optionsOrCallback, callback)
    
    
    deleteOperation(request: protos.google.longrunning.DeleteOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.protobuf.Empty, protos.google.longrunning.DeleteOperationRequest, {} | null | undefined>, callback?: Callback<protos.google.protobuf.Empty, protos.google.longrunning.DeleteOperationRequest, {} | null | undefined>): Promise<protos.google.protobuf.Empty>;

Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### deleteSavedQuery(request, options)
    
    
    deleteSavedQuery(request?: protos.google.cloud.aiplatform.v1beta1.IDeleteSavedQueryRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a SavedQuery.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSavedQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletesavedqueryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the SavedQuery to delete.
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}/savedQueries/{saved_query}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteSavedQuery() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.deleteSavedQuery(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteSavedQuery();
    
    

### deleteSavedQuery(request, options, callback)
    
    
    deleteSavedQuery(request: protos.google.cloud.aiplatform.v1beta1.IDeleteSavedQueryRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSavedQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletesavedqueryrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSavedQuery(request, callback)
    
    
    deleteSavedQuery(request: protos.google.cloud.aiplatform.v1beta1.IDeleteSavedQueryRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSavedQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletesavedqueryrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deploymentResourcePoolPath(project, location, deploymentResourcePool)
    
    
    deploymentResourcePoolPath(project: string, location: string, deploymentResourcePool: string): string;

Return a fully-qualified deploymentResourcePool resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`deploymentResourcePool` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### entityTypePath(project, location, featurestore, entityType)
    
    
    entityTypePath(project: string, location: string, featurestore: string, entityType: string): string;

Return a fully-qualified entityType resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`featurestore` |  `string`   
  
`entityType` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### exampleStorePath(project, location, exampleStore)
    
    
    exampleStorePath(project: string, location: string, exampleStore: string): string;

Return a fully-qualified exampleStore resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`exampleStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### executionPath(project, location, metadataStore, execution)
    
    
    executionPath(project: string, location: string, metadataStore: string, execution: string): string;

Return a fully-qualified execution resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`metadataStore` |  `string`   
  
`execution` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### exportData(request, options)
    
    
    exportData(request?: protos.google.cloud.aiplatform.v1beta1.IExportDataRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.aiplatform.v1beta1.IExportDataResponse, protos.google.cloud.aiplatform.v1beta1.IExportDataOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Exports data from a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexportdatarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.aiplatform.v1beta1.IExportDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexportdataresponse), [protos.google.cloud.aiplatform.v1beta1.IExportDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexportdataoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Dataset resource.
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}`
       */
      // const name = 'abc123'
      /**
       *  Required. The desired output location.
       */
      // const exportConfig = {}
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callExportData() {
        // Construct request
        const request = {
          name,
          exportConfig,
        };
    
        // Run request
        const [operation] = await aiplatformClient.exportData(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportData();
    
    

### exportData(request, options, callback)
    
    
    exportData(request: protos.google.cloud.aiplatform.v1beta1.IExportDataRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IExportDataResponse, protos.google.cloud.aiplatform.v1beta1.IExportDataOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexportdatarequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IExportDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexportdataresponse), [protos.google.cloud.aiplatform.v1beta1.IExportDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexportdataoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportData(request, callback)
    
    
    exportData(request: protos.google.cloud.aiplatform.v1beta1.IExportDataRequest, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IExportDataResponse, protos.google.cloud.aiplatform.v1beta1.IExportDataOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexportdatarequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IExportDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexportdataresponse), [protos.google.cloud.aiplatform.v1beta1.IExportDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexportdataoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### extensionPath(project, location, extension)
    
    
    extensionPath(project: string, location: string, extension: string): string;

Return a fully-qualified extension resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`extension` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### featureGroupPath(project, location, featureGroup)
    
    
    featureGroupPath(project: string, location: string, featureGroup: string): string;

Return a fully-qualified featureGroup resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`featureGroup` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### featureMonitorJobPath(project, location, featureGroup, featureMonitor, featureMonitorJob)
    
    
    featureMonitorJobPath(project: string, location: string, featureGroup: string, featureMonitor: string, featureMonitorJob: string): string;

Return a fully-qualified featureMonitorJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`featureGroup` |  `string`   
  
`featureMonitor` |  `string`   
  
`featureMonitorJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### featureMonitorPath(project, location, featureGroup, featureMonitor)
    
    
    featureMonitorPath(project: string, location: string, featureGroup: string, featureMonitor: string): string;

Return a fully-qualified featureMonitor resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`featureGroup` |  `string`   
  
`featureMonitor` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### featureOnlineStorePath(project, location, featureOnlineStore)
    
    
    featureOnlineStorePath(project: string, location: string, featureOnlineStore: string): string;

Return a fully-qualified featureOnlineStore resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`featureOnlineStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### featurestorePath(project, location, featurestore)
    
    
    featurestorePath(project: string, location: string, featurestore: string): string;

Return a fully-qualified featurestore resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`featurestore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### featureViewPath(project, location, featureOnlineStore, featureView)
    
    
    featureViewPath(project: string, location: string, featureOnlineStore: string, featureView: string): string;

Return a fully-qualified featureView resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`featureOnlineStore` |  `string`   
  
`featureView` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### featureViewSyncPath(project, location, featureOnlineStore, featureView)
    
    
    featureViewSyncPath(project: string, location: string, featureOnlineStore: string, featureView: string): string;

Return a fully-qualified featureViewSync resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`featureOnlineStore` |  `string`   
  
`featureView` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### getAnnotationSpec(request, options)
    
    
    getAnnotationSpec(request?: protos.google.cloud.aiplatform.v1beta1.IGetAnnotationSpecRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IAnnotationSpec,
            (protos.google.cloud.aiplatform.v1beta1.IGetAnnotationSpecRequest | undefined),
            {} | undefined
        ]>;

Gets an AnnotationSpec.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotationSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetannotationspecrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IAnnotationSpec](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iannotationspec), ([protos.google.cloud.aiplatform.v1beta1.IGetAnnotationSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetannotationspecrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [AnnotationSpec](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.annotationspec). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the AnnotationSpec resource.
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}/annotationSpecs/{annotation_spec}`
       */
      // const name = 'abc123'
      /**
       *  Mask specifying which fields to read.
       */
      // const readMask = {}
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callGetAnnotationSpec() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await aiplatformClient.getAnnotationSpec(request);
        console.log(response);
      }
    
      callGetAnnotationSpec();
    
    

### getAnnotationSpec(request, options, callback)
    
    
    getAnnotationSpec(request: protos.google.cloud.aiplatform.v1beta1.IGetAnnotationSpecRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IAnnotationSpec, protos.google.cloud.aiplatform.v1beta1.IGetAnnotationSpecRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotationSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetannotationspecrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IAnnotationSpec](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iannotationspec), [protos.google.cloud.aiplatform.v1beta1.IGetAnnotationSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetannotationspecrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAnnotationSpec(request, callback)
    
    
    getAnnotationSpec(request: protos.google.cloud.aiplatform.v1beta1.IGetAnnotationSpecRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IAnnotationSpec, protos.google.cloud.aiplatform.v1beta1.IGetAnnotationSpecRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotationSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetannotationspecrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IAnnotationSpec](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iannotationspec), [protos.google.cloud.aiplatform.v1beta1.IGetAnnotationSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetannotationspecrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataset(request, options)
    
    
    getDataset(request?: protos.google.cloud.aiplatform.v1beta1.IGetDatasetRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IDataset,
            protos.google.cloud.aiplatform.v1beta1.IGetDatasetRequest | undefined,
            {} | undefined
        ]>;

Gets a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetdatasetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idataset), [protos.google.cloud.aiplatform.v1beta1.IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetdatasetrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Dataset](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.dataset). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Dataset resource.
       */
      // const name = 'abc123'
      /**
       *  Mask specifying which fields to read.
       */
      // const readMask = {}
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callGetDataset() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await aiplatformClient.getDataset(request);
        console.log(response);
      }
    
      callGetDataset();
    
    

### getDataset(request, options, callback)
    
    
    getDataset(request: protos.google.cloud.aiplatform.v1beta1.IGetDatasetRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IDataset, protos.google.cloud.aiplatform.v1beta1.IGetDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetdatasetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idataset), [protos.google.cloud.aiplatform.v1beta1.IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetdatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataset(request, callback)
    
    
    getDataset(request: protos.google.cloud.aiplatform.v1beta1.IGetDatasetRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IDataset, protos.google.cloud.aiplatform.v1beta1.IGetDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetdatasetrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idataset), [protos.google.cloud.aiplatform.v1beta1.IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetdatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDatasetVersion(request, options)
    
    
    getDatasetVersion(request?: protos.google.cloud.aiplatform.v1beta1.IGetDatasetVersionRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IDatasetVersion,
            (protos.google.cloud.aiplatform.v1beta1.IGetDatasetVersionRequest | undefined),
            {} | undefined
        ]>;

Gets a Dataset version.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetdatasetversionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IDatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idatasetversion), ([protos.google.cloud.aiplatform.v1beta1.IGetDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetdatasetversionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [DatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.datasetversion). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Dataset version to delete.
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}/datasetVersions/{dataset_version}`
       */
      // const name = 'abc123'
      /**
       *  Mask specifying which fields to read.
       */
      // const readMask = {}
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callGetDatasetVersion() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await aiplatformClient.getDatasetVersion(request);
        console.log(response);
      }
    
      callGetDatasetVersion();
    
    

### getDatasetVersion(request, options, callback)
    
    
    getDatasetVersion(request: protos.google.cloud.aiplatform.v1beta1.IGetDatasetVersionRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IDatasetVersion, protos.google.cloud.aiplatform.v1beta1.IGetDatasetVersionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetdatasetversionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IDatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idatasetversion), [protos.google.cloud.aiplatform.v1beta1.IGetDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetdatasetversionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDatasetVersion(request, callback)
    
    
    getDatasetVersion(request: protos.google.cloud.aiplatform.v1beta1.IGetDatasetVersionRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IDatasetVersion, protos.google.cloud.aiplatform.v1beta1.IGetDatasetVersionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetdatasetversionrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IDatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idatasetversion), [protos.google.cloud.aiplatform.v1beta1.IGetDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetdatasetversionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request, options, callback)
    
    
    getIamPolicy(request: IamProtos.google.iam.v1.GetIamPolicyRequest, options?: gax.CallOptions | Callback<IamProtos.google.iam.v1.Policy, IamProtos.google.iam.v1.GetIamPolicyRequest | null | undefined, {} | null | undefined>, callback?: Callback<IamProtos.google.iam.v1.Policy, IamProtos.google.iam.v1.GetIamPolicyRequest | null | undefined, {} | null | undefined>): Promise<[IamProtos.google.iam.v1.Policy]>;

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `IamProtos.google.iam.v1.GetIamPolicyRequest`   
The request object that will be sent.  
`options` |  `CallOptions | Callback<google.iam.v1.Policy, google.iam.v1.GetIamPolicyRequest | null | undefined, {} | null | undefined>`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/interfaces/CallOptions.html) for the details.  
`callback` |  `Callback<google.iam.v1.Policy, google.iam.v1.GetIamPolicyRequest | null | undefined, {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing .  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.Policy]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
  
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
    

### getOperation(request, optionsOrCallback, callback)
    
    
    getOperation(request: protos.google.longrunning.GetOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>, callback?: Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>): Promise<[protos.google.longrunning.Operation]>;

Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)]>` |   
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
  
### hyperparameterTuningJobPath(project, location, hyperparameterTuningJob)
    
    
    hyperparameterTuningJobPath(project: string, location: string, hyperparameterTuningJob: string): string;

Return a fully-qualified hyperparameterTuningJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`hyperparameterTuningJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### importData(request, options)
    
    
    importData(request?: protos.google.cloud.aiplatform.v1beta1.IImportDataRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.aiplatform.v1beta1.IImportDataResponse, protos.google.cloud.aiplatform.v1beta1.IImportDataOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Imports data into a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iimportdatarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.aiplatform.v1beta1.IImportDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iimportdataresponse), [protos.google.cloud.aiplatform.v1beta1.IImportDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iimportdataoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Dataset resource.
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}`
       */
      // const name = 'abc123'
      /**
       *  Required. The desired input locations. The contents of all input locations
       *  will be imported in one batch.
       */
      // const importConfigs = [1,2,3,4]
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callImportData() {
        // Construct request
        const request = {
          name,
          importConfigs,
        };
    
        // Run request
        const [operation] = await aiplatformClient.importData(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callImportData();
    
    

### importData(request, options, callback)
    
    
    importData(request: protos.google.cloud.aiplatform.v1beta1.IImportDataRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IImportDataResponse, protos.google.cloud.aiplatform.v1beta1.IImportDataOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iimportdatarequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IImportDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iimportdataresponse), [protos.google.cloud.aiplatform.v1beta1.IImportDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iimportdataoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importData(request, callback)
    
    
    importData(request: protos.google.cloud.aiplatform.v1beta1.IImportDataRequest, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IImportDataResponse, protos.google.cloud.aiplatform.v1beta1.IImportDataOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iimportdatarequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IImportDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iimportdataresponse), [protos.google.cloud.aiplatform.v1beta1.IImportDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iimportdataoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### indexEndpointPath(project, location, indexEndpoint)
    
    
    indexEndpointPath(project: string, location: string, indexEndpoint: string): string;

Return a fully-qualified indexEndpoint resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`indexEndpoint` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### indexPath(project, location, index)
    
    
    indexPath(project: string, location: string, index: string): string;

Return a fully-qualified index resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`index` |  `string`   
  
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
  
### listAnnotations(request, options)
    
    
    listAnnotations(request?: protos.google.cloud.aiplatform.v1beta1.IListAnnotationsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IAnnotation[],
            protos.google.cloud.aiplatform.v1beta1.IListAnnotationsRequest | null,
            protos.google.cloud.aiplatform.v1beta1.IListAnnotationsResponse
        ]>;

Lists Annotations belongs to a dataitem.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnnotationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistannotationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IAnnotation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iannotation)[], [protos.google.cloud.aiplatform.v1beta1.IListAnnotationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistannotationsrequest) | null, [protos.google.cloud.aiplatform.v1beta1.IListAnnotationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistannotationsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Annotation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.annotation). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listAnnotationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listAnnotations(request, options, callback)
    
    
    listAnnotations(request: protos.google.cloud.aiplatform.v1beta1.IListAnnotationsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListAnnotationsRequest, protos.google.cloud.aiplatform.v1beta1.IListAnnotationsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.IAnnotation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnnotationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistannotationsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListAnnotationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistannotationsrequest), [protos.google.cloud.aiplatform.v1beta1.IListAnnotationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistannotationsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.IAnnotation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iannotation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAnnotations(request, callback)
    
    
    listAnnotations(request: protos.google.cloud.aiplatform.v1beta1.IListAnnotationsRequest, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListAnnotationsRequest, protos.google.cloud.aiplatform.v1beta1.IListAnnotationsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.IAnnotation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnnotationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistannotationsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListAnnotationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistannotationsrequest), [protos.google.cloud.aiplatform.v1beta1.IListAnnotationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistannotationsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.IAnnotation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iannotation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAnnotationsAsync(request, options)
    
    
    listAnnotationsAsync(request?: protos.google.cloud.aiplatform.v1beta1.IListAnnotationsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.aiplatform.v1beta1.IAnnotation>;

Equivalent to `listAnnotations`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnnotationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistannotationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.aiplatform.v1beta1.IAnnotation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iannotation)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Annotation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.annotation). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the DataItem to list Annotations from.
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}/dataItems/{data_item}`
       */
      // const parent = 'abc123'
      /**
       *  The standard list filter.
       */
      // const filter = 'abc123'
      /**
       *  The standard list page size.
       */
      // const pageSize = 1234
      /**
       *  The standard list page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Mask specifying which fields to read.
       */
      // const readMask = {}
      /**
       *  A comma-separated list of fields to order by, sorted in ascending order.
       *  Use "desc" after a field name for descending.
       */
      // const orderBy = 'abc123'
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callListAnnotations() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = aiplatformClient.listAnnotationsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListAnnotations();
    
    

### listAnnotationsStream(request, options)
    
    
    listAnnotationsStream(request?: protos.google.cloud.aiplatform.v1beta1.IListAnnotationsRequest, options?: CallOptions): Transform;

Equivalent to `listAnnotations`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnnotationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistannotationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Annotation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.annotation) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listAnnotationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDataItems(request, options)
    
    
    listDataItems(request?: protos.google.cloud.aiplatform.v1beta1.IListDataItemsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IDataItem[],
            protos.google.cloud.aiplatform.v1beta1.IListDataItemsRequest | null,
            protos.google.cloud.aiplatform.v1beta1.IListDataItemsResponse
        ]>;

Lists DataItems in a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdataitemsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IDataItem](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idataitem)[], [protos.google.cloud.aiplatform.v1beta1.IListDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdataitemsrequest) | null, [protos.google.cloud.aiplatform.v1beta1.IListDataItemsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdataitemsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [DataItem](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.dataitem). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listDataItemsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDataItems(request, options, callback)
    
    
    listDataItems(request: protos.google.cloud.aiplatform.v1beta1.IListDataItemsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListDataItemsRequest, protos.google.cloud.aiplatform.v1beta1.IListDataItemsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.IDataItem>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdataitemsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdataitemsrequest), [protos.google.cloud.aiplatform.v1beta1.IListDataItemsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdataitemsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.IDataItem](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idataitem)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataItems(request, callback)
    
    
    listDataItems(request: protos.google.cloud.aiplatform.v1beta1.IListDataItemsRequest, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListDataItemsRequest, protos.google.cloud.aiplatform.v1beta1.IListDataItemsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.IDataItem>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdataitemsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdataitemsrequest), [protos.google.cloud.aiplatform.v1beta1.IListDataItemsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdataitemsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.IDataItem](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idataitem)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataItemsAsync(request, options)
    
    
    listDataItemsAsync(request?: protos.google.cloud.aiplatform.v1beta1.IListDataItemsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.aiplatform.v1beta1.IDataItem>;

Equivalent to `listDataItems`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdataitemsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.aiplatform.v1beta1.IDataItem](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idataitem)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [DataItem](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.dataitem). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Dataset to list DataItems from.
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}`
       */
      // const parent = 'abc123'
      /**
       *  The standard list filter.
       */
      // const filter = 'abc123'
      /**
       *  The standard list page size.
       */
      // const pageSize = 1234
      /**
       *  The standard list page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Mask specifying which fields to read.
       */
      // const readMask = {}
      /**
       *  A comma-separated list of fields to order by, sorted in ascending order.
       *  Use "desc" after a field name for descending.
       */
      // const orderBy = 'abc123'
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callListDataItems() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = aiplatformClient.listDataItemsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListDataItems();
    
    

### listDataItemsStream(request, options)
    
    
    listDataItemsStream(request?: protos.google.cloud.aiplatform.v1beta1.IListDataItemsRequest, options?: CallOptions): Transform;

Equivalent to `listDataItems`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdataitemsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [DataItem](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.dataitem) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listDataItemsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDatasets(request, options)
    
    
    listDatasets(request?: protos.google.cloud.aiplatform.v1beta1.IListDatasetsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IDataset[],
            protos.google.cloud.aiplatform.v1beta1.IListDatasetsRequest | null,
            protos.google.cloud.aiplatform.v1beta1.IListDatasetsResponse
        ]>;

Lists Datasets in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idataset)[], [protos.google.cloud.aiplatform.v1beta1.IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetsrequest) | null, [protos.google.cloud.aiplatform.v1beta1.IListDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Dataset](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.dataset). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listDatasetsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDatasets(request, options, callback)
    
    
    listDatasets(request: protos.google.cloud.aiplatform.v1beta1.IListDatasetsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListDatasetsRequest, protos.google.cloud.aiplatform.v1beta1.IListDatasetsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.IDataset>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetsrequest), [protos.google.cloud.aiplatform.v1beta1.IListDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idataset)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDatasets(request, callback)
    
    
    listDatasets(request: protos.google.cloud.aiplatform.v1beta1.IListDatasetsRequest, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListDatasetsRequest, protos.google.cloud.aiplatform.v1beta1.IListDatasetsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.IDataset>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetsrequest), [protos.google.cloud.aiplatform.v1beta1.IListDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idataset)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDatasetsAsync(request, options)
    
    
    listDatasetsAsync(request?: protos.google.cloud.aiplatform.v1beta1.IListDatasetsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.aiplatform.v1beta1.IDataset>;

Equivalent to `listDatasets`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.aiplatform.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idataset)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Dataset](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.dataset). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Dataset's parent resource.
       *  Format: `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  An expression for filtering the results of the request. For field names
       *  both snake_case and camelCase are supported.
       *    * `display_name`: supports = and !=
       *    * `metadata_schema_uri`: supports = and !=
       *    * `labels` supports general map functions that is:
       *      * `labels.key=value` - key:value equality
       *      * `labels.key:* or labels:key - key existence
       *      * A key including a space must be quoted. `labels."a key"`.
       *  Some examples:
       *    * `displayName="myDisplayName"`
       *    * `labels.myKey="myValue"`
       */
      // const filter = 'abc123'
      /**
       *  The standard list page size.
       */
      // const pageSize = 1234
      /**
       *  The standard list page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Mask specifying which fields to read.
       */
      // const readMask = {}
      /**
       *  A comma-separated list of fields to order by, sorted in ascending order.
       *  Use "desc" after a field name for descending.
       *  Supported fields:
       *    * `display_name`
       *    * `create_time`
       *    * `update_time`
       */
      // const orderBy = 'abc123'
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callListDatasets() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = aiplatformClient.listDatasetsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListDatasets();
    
    

### listDatasetsStream(request, options)
    
    
    listDatasetsStream(request?: protos.google.cloud.aiplatform.v1beta1.IListDatasetsRequest, options?: CallOptions): Transform;

Equivalent to `listDatasets`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Dataset](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.dataset) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listDatasetsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDatasetVersions(request, options)
    
    
    listDatasetVersions(request?: protos.google.cloud.aiplatform.v1beta1.IListDatasetVersionsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IDatasetVersion[],
            protos.google.cloud.aiplatform.v1beta1.IListDatasetVersionsRequest | null,
            protos.google.cloud.aiplatform.v1beta1.IListDatasetVersionsResponse
        ]>;

Lists DatasetVersions in a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetversionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IDatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idatasetversion)[], [protos.google.cloud.aiplatform.v1beta1.IListDatasetVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetversionsrequest) | null, [protos.google.cloud.aiplatform.v1beta1.IListDatasetVersionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetversionsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [DatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.datasetversion). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listDatasetVersionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDatasetVersions(request, options, callback)
    
    
    listDatasetVersions(request: protos.google.cloud.aiplatform.v1beta1.IListDatasetVersionsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListDatasetVersionsRequest, protos.google.cloud.aiplatform.v1beta1.IListDatasetVersionsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.IDatasetVersion>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetversionsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListDatasetVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetversionsrequest), [protos.google.cloud.aiplatform.v1beta1.IListDatasetVersionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetversionsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.IDatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idatasetversion)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDatasetVersions(request, callback)
    
    
    listDatasetVersions(request: protos.google.cloud.aiplatform.v1beta1.IListDatasetVersionsRequest, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListDatasetVersionsRequest, protos.google.cloud.aiplatform.v1beta1.IListDatasetVersionsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.IDatasetVersion>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetversionsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListDatasetVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetversionsrequest), [protos.google.cloud.aiplatform.v1beta1.IListDatasetVersionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetversionsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.IDatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idatasetversion)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDatasetVersionsAsync(request, options)
    
    
    listDatasetVersionsAsync(request?: protos.google.cloud.aiplatform.v1beta1.IListDatasetVersionsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.aiplatform.v1beta1.IDatasetVersion>;

Equivalent to `listDatasetVersions`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetversionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.aiplatform.v1beta1.IDatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idatasetversion)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [DatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.datasetversion). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Dataset to list DatasetVersions from.
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. The standard list filter.
       */
      // const filter = 'abc123'
      /**
       *  Optional. The standard list page size.
       */
      // const pageSize = 1234
      /**
       *  Optional. The standard list page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Mask specifying which fields to read.
       */
      // const readMask = {}
      /**
       *  Optional. A comma-separated list of fields to order by, sorted in ascending
       *  order. Use "desc" after a field name for descending.
       */
      // const orderBy = 'abc123'
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callListDatasetVersions() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = aiplatformClient.listDatasetVersionsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListDatasetVersions();
    
    

### listDatasetVersionsStream(request, options)
    
    
    listDatasetVersionsStream(request?: protos.google.cloud.aiplatform.v1beta1.IListDatasetVersionsRequest, options?: CallOptions): Transform;

Equivalent to `listDatasetVersions`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistdatasetversionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [DatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.datasetversion) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listDatasetVersionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
    

### listOperationsAsync(request, options)
    
    
    listOperationsAsync(request: protos.google.longrunning.ListOperationsRequest, options?: gax.CallOptions): AsyncIterable<protos.google.longrunning.IOperation>;

Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. Returns an iterable object.

For-await-of syntax is used with the iterable to recursively get response element on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
**Example**
    
    
    const client = longrunning.operationsClient();
    for await (const response of client.listOperationsAsync(request));
    // doThingsWith(response)
    

### listSavedQueries(request, options)
    
    
    listSavedQueries(request?: protos.google.cloud.aiplatform.v1beta1.IListSavedQueriesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ISavedQuery[],
            protos.google.cloud.aiplatform.v1beta1.IListSavedQueriesRequest | null,
            protos.google.cloud.aiplatform.v1beta1.IListSavedQueriesResponse
        ]>;

Lists SavedQueries in a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSavedQueriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistsavedqueriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ISavedQuery](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isavedquery)[], [protos.google.cloud.aiplatform.v1beta1.IListSavedQueriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistsavedqueriesrequest) | null, [protos.google.cloud.aiplatform.v1beta1.IListSavedQueriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistsavedqueriesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [SavedQuery](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.savedquery). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listSavedQueriesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listSavedQueries(request, options, callback)
    
    
    listSavedQueries(request: protos.google.cloud.aiplatform.v1beta1.IListSavedQueriesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListSavedQueriesRequest, protos.google.cloud.aiplatform.v1beta1.IListSavedQueriesResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.ISavedQuery>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSavedQueriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistsavedqueriesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListSavedQueriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistsavedqueriesrequest), [protos.google.cloud.aiplatform.v1beta1.IListSavedQueriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistsavedqueriesresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.ISavedQuery](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isavedquery)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSavedQueries(request, callback)
    
    
    listSavedQueries(request: protos.google.cloud.aiplatform.v1beta1.IListSavedQueriesRequest, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListSavedQueriesRequest, protos.google.cloud.aiplatform.v1beta1.IListSavedQueriesResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.ISavedQuery>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSavedQueriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistsavedqueriesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListSavedQueriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistsavedqueriesrequest), [protos.google.cloud.aiplatform.v1beta1.IListSavedQueriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistsavedqueriesresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.ISavedQuery](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isavedquery)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSavedQueriesAsync(request, options)
    
    
    listSavedQueriesAsync(request?: protos.google.cloud.aiplatform.v1beta1.IListSavedQueriesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.aiplatform.v1beta1.ISavedQuery>;

Equivalent to `listSavedQueries`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSavedQueriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistsavedqueriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.aiplatform.v1beta1.ISavedQuery](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isavedquery)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [SavedQuery](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.savedquery). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Dataset to list SavedQueries from.
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}`
       */
      // const parent = 'abc123'
      /**
       *  The standard list filter.
       */
      // const filter = 'abc123'
      /**
       *  The standard list page size.
       */
      // const pageSize = 1234
      /**
       *  The standard list page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Mask specifying which fields to read.
       */
      // const readMask = {}
      /**
       *  A comma-separated list of fields to order by, sorted in ascending order.
       *  Use "desc" after a field name for descending.
       */
      // const orderBy = 'abc123'
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callListSavedQueries() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = aiplatformClient.listSavedQueriesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListSavedQueries();
    
    

### listSavedQueriesStream(request, options)
    
    
    listSavedQueriesStream(request?: protos.google.cloud.aiplatform.v1beta1.IListSavedQueriesRequest, options?: CallOptions): Transform;

Equivalent to `listSavedQueries`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSavedQueriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistsavedqueriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [SavedQuery](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.savedquery) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listSavedQueriesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### matchAnnotationFromAnnotationName(annotationName)
    
    
    matchAnnotationFromAnnotationName(annotationName: string): string | number;

Parse the annotation from Annotation resource.

**Parameter**  
---  
**Name** | **Description**  
`annotationName` |  `string`   
A fully-qualified path representing Annotation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the annotation.  
  
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
  
### matchArtifactFromArtifactName(artifactName)
    
    
    matchArtifactFromArtifactName(artifactName: string): string | number;

Parse the artifact from Artifact resource.

**Parameter**  
---  
**Name** | **Description**  
`artifactName` |  `string`   
A fully-qualified path representing Artifact resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the artifact.  
  
### matchBatchPredictionJobFromBatchPredictionJobName(batchPredictionJobName)
    
    
    matchBatchPredictionJobFromBatchPredictionJobName(batchPredictionJobName: string): string | number;

Parse the batch_prediction_job from BatchPredictionJob resource.

**Parameter**  
---  
**Name** | **Description**  
`batchPredictionJobName` |  `string`   
A fully-qualified path representing BatchPredictionJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the batch_prediction_job.  
  
### matchCachedContentFromCachedContentName(cachedContentName)
    
    
    matchCachedContentFromCachedContentName(cachedContentName: string): string | number;

Parse the cached_content from CachedContent resource.

**Parameter**  
---  
**Name** | **Description**  
`cachedContentName` |  `string`   
A fully-qualified path representing CachedContent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the cached_content.  
  
### matchContextFromContextName(contextName)
    
    
    matchContextFromContextName(contextName: string): string | number;

Parse the context from Context resource.

**Parameter**  
---  
**Name** | **Description**  
`contextName` |  `string`   
A fully-qualified path representing Context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the context.  
  
### matchCustomJobFromCustomJobName(customJobName)
    
    
    matchCustomJobFromCustomJobName(customJobName: string): string | number;

Parse the custom_job from CustomJob resource.

**Parameter**  
---  
**Name** | **Description**  
`customJobName` |  `string`   
A fully-qualified path representing CustomJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the custom_job.  
  
### matchDataItemFromAnnotationName(annotationName)
    
    
    matchDataItemFromAnnotationName(annotationName: string): string | number;

Parse the data_item from Annotation resource.

**Parameter**  
---  
**Name** | **Description**  
`annotationName` |  `string`   
A fully-qualified path representing Annotation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_item.  
  
### matchDataItemFromDataItemName(dataItemName)
    
    
    matchDataItemFromDataItemName(dataItemName: string): string | number;

Parse the data_item from DataItem resource.

**Parameter**  
---  
**Name** | **Description**  
`dataItemName` |  `string`   
A fully-qualified path representing DataItem resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_item.  
  
### matchDataLabelingJobFromDataLabelingJobName(dataLabelingJobName)
    
    
    matchDataLabelingJobFromDataLabelingJobName(dataLabelingJobName: string): string | number;

Parse the data_labeling_job from DataLabelingJob resource.

**Parameter**  
---  
**Name** | **Description**  
`dataLabelingJobName` |  `string`   
A fully-qualified path representing DataLabelingJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_labeling_job.  
  
### matchDatasetFromAnnotationName(annotationName)
    
    
    matchDatasetFromAnnotationName(annotationName: string): string | number;

Parse the dataset from Annotation resource.

**Parameter**  
---  
**Name** | **Description**  
`annotationName` |  `string`   
A fully-qualified path representing Annotation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the dataset.  
  
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
  
### matchDatasetFromDataItemName(dataItemName)
    
    
    matchDatasetFromDataItemName(dataItemName: string): string | number;

Parse the dataset from DataItem resource.

**Parameter**  
---  
**Name** | **Description**  
`dataItemName` |  `string`   
A fully-qualified path representing DataItem resource.  
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
  
### matchDatasetFromDatasetVersionName(datasetVersionName)
    
    
    matchDatasetFromDatasetVersionName(datasetVersionName: string): string | number;

Parse the dataset from DatasetVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`datasetVersionName` |  `string`   
A fully-qualified path representing DatasetVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the dataset.  
  
### matchDatasetFromSavedQueryName(savedQueryName)
    
    
    matchDatasetFromSavedQueryName(savedQueryName: string): string | number;

Parse the dataset from SavedQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`savedQueryName` |  `string`   
A fully-qualified path representing SavedQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the dataset.  
  
### matchDatasetVersionFromDatasetVersionName(datasetVersionName)
    
    
    matchDatasetVersionFromDatasetVersionName(datasetVersionName: string): string | number;

Parse the dataset_version from DatasetVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`datasetVersionName` |  `string`   
A fully-qualified path representing DatasetVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the dataset_version.  
  
### matchDeploymentResourcePoolFromDeploymentResourcePoolName(deploymentResourcePoolName)
    
    
    matchDeploymentResourcePoolFromDeploymentResourcePoolName(deploymentResourcePoolName: string): string | number;

Parse the deployment_resource_pool from DeploymentResourcePool resource.

**Parameter**  
---  
**Name** | **Description**  
`deploymentResourcePoolName` |  `string`   
A fully-qualified path representing DeploymentResourcePool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the deployment_resource_pool.  
  
### matchEndpointFromProjectLocationEndpointName(projectLocationEndpointName)
    
    
    matchEndpointFromProjectLocationEndpointName(projectLocationEndpointName: string): string | number;

Parse the endpoint from ProjectLocationEndpoint resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationEndpointName` |  `string`   
A fully-qualified path representing project_location_endpoint resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the endpoint.  
  
### matchEntityTypeFromEntityTypeName(entityTypeName)
    
    
    matchEntityTypeFromEntityTypeName(entityTypeName: string): string | number;

Parse the entity_type from EntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`entityTypeName` |  `string`   
A fully-qualified path representing EntityType resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the entity_type.  
  
### matchEntityTypeFromProjectLocationFeaturestoreEntityTypeFeaturesName(projectLocationFeaturestoreEntityTypeFeaturesName)
    
    
    matchEntityTypeFromProjectLocationFeaturestoreEntityTypeFeaturesName(projectLocationFeaturestoreEntityTypeFeaturesName: string): string | number;

Parse the entity_type from ProjectLocationFeaturestoreEntityTypeFeatures resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationFeaturestoreEntityTypeFeaturesName` |  `string`   
A fully-qualified path representing project_location_featurestore_entity_type_features resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the entity_type.  
  
### matchEvaluationFromModelEvaluationName(modelEvaluationName)
    
    
    matchEvaluationFromModelEvaluationName(modelEvaluationName: string): string | number;

Parse the evaluation from ModelEvaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`modelEvaluationName` |  `string`   
A fully-qualified path representing ModelEvaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the evaluation.  
  
### matchEvaluationFromModelEvaluationSliceName(modelEvaluationSliceName)
    
    
    matchEvaluationFromModelEvaluationSliceName(modelEvaluationSliceName: string): string | number;

Parse the evaluation from ModelEvaluationSlice resource.

**Parameter**  
---  
**Name** | **Description**  
`modelEvaluationSliceName` |  `string`   
A fully-qualified path representing ModelEvaluationSlice resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the evaluation.  
  
### matchEventFromSessionEventName(sessionEventName)
    
    
    matchEventFromSessionEventName(sessionEventName: string): string | number;

Parse the event from SessionEvent resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionEventName` |  `string`   
A fully-qualified path representing SessionEvent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the event.  
  
### matchExampleStoreFromExampleStoreName(exampleStoreName)
    
    
    matchExampleStoreFromExampleStoreName(exampleStoreName: string): string | number;

Parse the example_store from ExampleStore resource.

**Parameter**  
---  
**Name** | **Description**  
`exampleStoreName` |  `string`   
A fully-qualified path representing ExampleStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the example_store.  
  
### matchExecutionFromExecutionName(executionName)
    
    
    matchExecutionFromExecutionName(executionName: string): string | number;

Parse the execution from Execution resource.

**Parameter**  
---  
**Name** | **Description**  
`executionName` |  `string`   
A fully-qualified path representing Execution resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the execution.  
  
### matchExperimentFromTensorboardExperimentName(tensorboardExperimentName)
    
    
    matchExperimentFromTensorboardExperimentName(tensorboardExperimentName: string): string | number;

Parse the experiment from TensorboardExperiment resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardExperimentName` |  `string`   
A fully-qualified path representing TensorboardExperiment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the experiment.  
  
### matchExperimentFromTensorboardRunName(tensorboardRunName)
    
    
    matchExperimentFromTensorboardRunName(tensorboardRunName: string): string | number;

Parse the experiment from TensorboardRun resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardRunName` |  `string`   
A fully-qualified path representing TensorboardRun resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the experiment.  
  
### matchExperimentFromTensorboardTimeSeriesName(tensorboardTimeSeriesName)
    
    
    matchExperimentFromTensorboardTimeSeriesName(tensorboardTimeSeriesName: string): string | number;

Parse the experiment from TensorboardTimeSeries resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardTimeSeriesName` |  `string`   
A fully-qualified path representing TensorboardTimeSeries resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the experiment.  
  
### matchExtensionFromExtensionName(extensionName)
    
    
    matchExtensionFromExtensionName(extensionName: string): string | number;

Parse the extension from Extension resource.

**Parameter**  
---  
**Name** | **Description**  
`extensionName` |  `string`   
A fully-qualified path representing Extension resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the extension.  
  
### matchFeatureFromProjectLocationFeatureGroupFeaturesName(projectLocationFeatureGroupFeaturesName)
    
    
    matchFeatureFromProjectLocationFeatureGroupFeaturesName(projectLocationFeatureGroupFeaturesName: string): string | number;

Parse the feature from ProjectLocationFeatureGroupFeatures resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationFeatureGroupFeaturesName` |  `string`   
A fully-qualified path representing project_location_feature_group_features resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature.  
  
### matchFeatureFromProjectLocationFeaturestoreEntityTypeFeaturesName(projectLocationFeaturestoreEntityTypeFeaturesName)
    
    
    matchFeatureFromProjectLocationFeaturestoreEntityTypeFeaturesName(projectLocationFeaturestoreEntityTypeFeaturesName: string): string | number;

Parse the feature from ProjectLocationFeaturestoreEntityTypeFeatures resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationFeaturestoreEntityTypeFeaturesName` |  `string`   
A fully-qualified path representing project_location_featurestore_entity_type_features resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature.  
  
### matchFeatureGroupFromFeatureGroupName(featureGroupName)
    
    
    matchFeatureGroupFromFeatureGroupName(featureGroupName: string): string | number;

Parse the feature_group from FeatureGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`featureGroupName` |  `string`   
A fully-qualified path representing FeatureGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_group.  
  
### matchFeatureGroupFromFeatureMonitorJobName(featureMonitorJobName)
    
    
    matchFeatureGroupFromFeatureMonitorJobName(featureMonitorJobName: string): string | number;

Parse the feature_group from FeatureMonitorJob resource.

**Parameter**  
---  
**Name** | **Description**  
`featureMonitorJobName` |  `string`   
A fully-qualified path representing FeatureMonitorJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_group.  
  
### matchFeatureGroupFromFeatureMonitorName(featureMonitorName)
    
    
    matchFeatureGroupFromFeatureMonitorName(featureMonitorName: string): string | number;

Parse the feature_group from FeatureMonitor resource.

**Parameter**  
---  
**Name** | **Description**  
`featureMonitorName` |  `string`   
A fully-qualified path representing FeatureMonitor resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_group.  
  
### matchFeatureGroupFromProjectLocationFeatureGroupFeaturesName(projectLocationFeatureGroupFeaturesName)
    
    
    matchFeatureGroupFromProjectLocationFeatureGroupFeaturesName(projectLocationFeatureGroupFeaturesName: string): string | number;

Parse the feature_group from ProjectLocationFeatureGroupFeatures resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationFeatureGroupFeaturesName` |  `string`   
A fully-qualified path representing project_location_feature_group_features resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_group.  
  
### matchFeatureMonitorFromFeatureMonitorJobName(featureMonitorJobName)
    
    
    matchFeatureMonitorFromFeatureMonitorJobName(featureMonitorJobName: string): string | number;

Parse the feature_monitor from FeatureMonitorJob resource.

**Parameter**  
---  
**Name** | **Description**  
`featureMonitorJobName` |  `string`   
A fully-qualified path representing FeatureMonitorJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_monitor.  
  
### matchFeatureMonitorFromFeatureMonitorName(featureMonitorName)
    
    
    matchFeatureMonitorFromFeatureMonitorName(featureMonitorName: string): string | number;

Parse the feature_monitor from FeatureMonitor resource.

**Parameter**  
---  
**Name** | **Description**  
`featureMonitorName` |  `string`   
A fully-qualified path representing FeatureMonitor resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_monitor.  
  
### matchFeatureMonitorJobFromFeatureMonitorJobName(featureMonitorJobName)
    
    
    matchFeatureMonitorJobFromFeatureMonitorJobName(featureMonitorJobName: string): string | number;

Parse the feature_monitor_job from FeatureMonitorJob resource.

**Parameter**  
---  
**Name** | **Description**  
`featureMonitorJobName` |  `string`   
A fully-qualified path representing FeatureMonitorJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_monitor_job.  
  
### matchFeatureOnlineStoreFromFeatureOnlineStoreName(featureOnlineStoreName)
    
    
    matchFeatureOnlineStoreFromFeatureOnlineStoreName(featureOnlineStoreName: string): string | number;

Parse the feature_online_store from FeatureOnlineStore resource.

**Parameter**  
---  
**Name** | **Description**  
`featureOnlineStoreName` |  `string`   
A fully-qualified path representing FeatureOnlineStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_online_store.  
  
### matchFeatureOnlineStoreFromFeatureViewName(featureViewName)
    
    
    matchFeatureOnlineStoreFromFeatureViewName(featureViewName: string): string | number;

Parse the feature_online_store from FeatureView resource.

**Parameter**  
---  
**Name** | **Description**  
`featureViewName` |  `string`   
A fully-qualified path representing FeatureView resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_online_store.  
  
### matchFeatureOnlineStoreFromFeatureViewSyncName(featureViewSyncName)
    
    
    matchFeatureOnlineStoreFromFeatureViewSyncName(featureViewSyncName: string): string | number;

Parse the feature_online_store from FeatureViewSync resource.

**Parameter**  
---  
**Name** | **Description**  
`featureViewSyncName` |  `string`   
A fully-qualified path representing FeatureViewSync resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_online_store.  
  
### matchFeaturestoreFromEntityTypeName(entityTypeName)
    
    
    matchFeaturestoreFromEntityTypeName(entityTypeName: string): string | number;

Parse the featurestore from EntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`entityTypeName` |  `string`   
A fully-qualified path representing EntityType resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the featurestore.  
  
### matchFeaturestoreFromFeaturestoreName(featurestoreName)
    
    
    matchFeaturestoreFromFeaturestoreName(featurestoreName: string): string | number;

Parse the featurestore from Featurestore resource.

**Parameter**  
---  
**Name** | **Description**  
`featurestoreName` |  `string`   
A fully-qualified path representing Featurestore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the featurestore.  
  
### matchFeaturestoreFromProjectLocationFeaturestoreEntityTypeFeaturesName(projectLocationFeaturestoreEntityTypeFeaturesName)
    
    
    matchFeaturestoreFromProjectLocationFeaturestoreEntityTypeFeaturesName(projectLocationFeaturestoreEntityTypeFeaturesName: string): string | number;

Parse the featurestore from ProjectLocationFeaturestoreEntityTypeFeatures resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationFeaturestoreEntityTypeFeaturesName` |  `string`   
A fully-qualified path representing project_location_featurestore_entity_type_features resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the featurestore.  
  
### matchFeatureViewFromFeatureViewName(featureViewName)
    
    
    matchFeatureViewFromFeatureViewName(featureViewName: string): string | number;

Parse the feature_view from FeatureView resource.

**Parameter**  
---  
**Name** | **Description**  
`featureViewName` |  `string`   
A fully-qualified path representing FeatureView resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_view.  
  
### matchFeatureViewFromFeatureViewSyncName(featureViewSyncName)
    
    
    matchFeatureViewFromFeatureViewSyncName(featureViewSyncName: string): string | number;

Parse the feature_view from FeatureViewSync resource.

**Parameter**  
---  
**Name** | **Description**  
`featureViewSyncName` |  `string`   
A fully-qualified path representing FeatureViewSync resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_view.  
  
### matchHyperparameterTuningJobFromHyperparameterTuningJobName(hyperparameterTuningJobName)
    
    
    matchHyperparameterTuningJobFromHyperparameterTuningJobName(hyperparameterTuningJobName: string): string | number;

Parse the hyperparameter_tuning_job from HyperparameterTuningJob resource.

**Parameter**  
---  
**Name** | **Description**  
`hyperparameterTuningJobName` |  `string`   
A fully-qualified path representing HyperparameterTuningJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the hyperparameter_tuning_job.  
  
### matchIndexEndpointFromIndexEndpointName(indexEndpointName)
    
    
    matchIndexEndpointFromIndexEndpointName(indexEndpointName: string): string | number;

Parse the index_endpoint from IndexEndpoint resource.

**Parameter**  
---  
**Name** | **Description**  
`indexEndpointName` |  `string`   
A fully-qualified path representing IndexEndpoint resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the index_endpoint.  
  
### matchIndexFromIndexName(indexName)
    
    
    matchIndexFromIndexName(indexName: string): string | number;

Parse the index from Index resource.

**Parameter**  
---  
**Name** | **Description**  
`indexName` |  `string`   
A fully-qualified path representing Index resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the index.  
  
### matchLocationFromAnnotationName(annotationName)
    
    
    matchLocationFromAnnotationName(annotationName: string): string | number;

Parse the location from Annotation resource.

**Parameter**  
---  
**Name** | **Description**  
`annotationName` |  `string`   
A fully-qualified path representing Annotation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
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
  
### matchLocationFromArtifactName(artifactName)
    
    
    matchLocationFromArtifactName(artifactName: string): string | number;

Parse the location from Artifact resource.

**Parameter**  
---  
**Name** | **Description**  
`artifactName` |  `string`   
A fully-qualified path representing Artifact resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromBatchPredictionJobName(batchPredictionJobName)
    
    
    matchLocationFromBatchPredictionJobName(batchPredictionJobName: string): string | number;

Parse the location from BatchPredictionJob resource.

**Parameter**  
---  
**Name** | **Description**  
`batchPredictionJobName` |  `string`   
A fully-qualified path representing BatchPredictionJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromCachedContentName(cachedContentName)
    
    
    matchLocationFromCachedContentName(cachedContentName: string): string | number;

Parse the location from CachedContent resource.

**Parameter**  
---  
**Name** | **Description**  
`cachedContentName` |  `string`   
A fully-qualified path representing CachedContent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromContextName(contextName)
    
    
    matchLocationFromContextName(contextName: string): string | number;

Parse the location from Context resource.

**Parameter**  
---  
**Name** | **Description**  
`contextName` |  `string`   
A fully-qualified path representing Context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromCustomJobName(customJobName)
    
    
    matchLocationFromCustomJobName(customJobName: string): string | number;

Parse the location from CustomJob resource.

**Parameter**  
---  
**Name** | **Description**  
`customJobName` |  `string`   
A fully-qualified path representing CustomJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromDataItemName(dataItemName)
    
    
    matchLocationFromDataItemName(dataItemName: string): string | number;

Parse the location from DataItem resource.

**Parameter**  
---  
**Name** | **Description**  
`dataItemName` |  `string`   
A fully-qualified path representing DataItem resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromDataLabelingJobName(dataLabelingJobName)
    
    
    matchLocationFromDataLabelingJobName(dataLabelingJobName: string): string | number;

Parse the location from DataLabelingJob resource.

**Parameter**  
---  
**Name** | **Description**  
`dataLabelingJobName` |  `string`   
A fully-qualified path representing DataLabelingJob resource.  
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
  
### matchLocationFromDatasetVersionName(datasetVersionName)
    
    
    matchLocationFromDatasetVersionName(datasetVersionName: string): string | number;

Parse the location from DatasetVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`datasetVersionName` |  `string`   
A fully-qualified path representing DatasetVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromDeploymentResourcePoolName(deploymentResourcePoolName)
    
    
    matchLocationFromDeploymentResourcePoolName(deploymentResourcePoolName: string): string | number;

Parse the location from DeploymentResourcePool resource.

**Parameter**  
---  
**Name** | **Description**  
`deploymentResourcePoolName` |  `string`   
A fully-qualified path representing DeploymentResourcePool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromEntityTypeName(entityTypeName)
    
    
    matchLocationFromEntityTypeName(entityTypeName: string): string | number;

Parse the location from EntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`entityTypeName` |  `string`   
A fully-qualified path representing EntityType resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromExampleStoreName(exampleStoreName)
    
    
    matchLocationFromExampleStoreName(exampleStoreName: string): string | number;

Parse the location from ExampleStore resource.

**Parameter**  
---  
**Name** | **Description**  
`exampleStoreName` |  `string`   
A fully-qualified path representing ExampleStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromExecutionName(executionName)
    
    
    matchLocationFromExecutionName(executionName: string): string | number;

Parse the location from Execution resource.

**Parameter**  
---  
**Name** | **Description**  
`executionName` |  `string`   
A fully-qualified path representing Execution resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromExtensionName(extensionName)
    
    
    matchLocationFromExtensionName(extensionName: string): string | number;

Parse the location from Extension resource.

**Parameter**  
---  
**Name** | **Description**  
`extensionName` |  `string`   
A fully-qualified path representing Extension resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromFeatureGroupName(featureGroupName)
    
    
    matchLocationFromFeatureGroupName(featureGroupName: string): string | number;

Parse the location from FeatureGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`featureGroupName` |  `string`   
A fully-qualified path representing FeatureGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromFeatureMonitorJobName(featureMonitorJobName)
    
    
    matchLocationFromFeatureMonitorJobName(featureMonitorJobName: string): string | number;

Parse the location from FeatureMonitorJob resource.

**Parameter**  
---  
**Name** | **Description**  
`featureMonitorJobName` |  `string`   
A fully-qualified path representing FeatureMonitorJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromFeatureMonitorName(featureMonitorName)
    
    
    matchLocationFromFeatureMonitorName(featureMonitorName: string): string | number;

Parse the location from FeatureMonitor resource.

**Parameter**  
---  
**Name** | **Description**  
`featureMonitorName` |  `string`   
A fully-qualified path representing FeatureMonitor resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromFeatureOnlineStoreName(featureOnlineStoreName)
    
    
    matchLocationFromFeatureOnlineStoreName(featureOnlineStoreName: string): string | number;

Parse the location from FeatureOnlineStore resource.

**Parameter**  
---  
**Name** | **Description**  
`featureOnlineStoreName` |  `string`   
A fully-qualified path representing FeatureOnlineStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromFeaturestoreName(featurestoreName)
    
    
    matchLocationFromFeaturestoreName(featurestoreName: string): string | number;

Parse the location from Featurestore resource.

**Parameter**  
---  
**Name** | **Description**  
`featurestoreName` |  `string`   
A fully-qualified path representing Featurestore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromFeatureViewName(featureViewName)
    
    
    matchLocationFromFeatureViewName(featureViewName: string): string | number;

Parse the location from FeatureView resource.

**Parameter**  
---  
**Name** | **Description**  
`featureViewName` |  `string`   
A fully-qualified path representing FeatureView resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromFeatureViewSyncName(featureViewSyncName)
    
    
    matchLocationFromFeatureViewSyncName(featureViewSyncName: string): string | number;

Parse the location from FeatureViewSync resource.

**Parameter**  
---  
**Name** | **Description**  
`featureViewSyncName` |  `string`   
A fully-qualified path representing FeatureViewSync resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromHyperparameterTuningJobName(hyperparameterTuningJobName)
    
    
    matchLocationFromHyperparameterTuningJobName(hyperparameterTuningJobName: string): string | number;

Parse the location from HyperparameterTuningJob resource.

**Parameter**  
---  
**Name** | **Description**  
`hyperparameterTuningJobName` |  `string`   
A fully-qualified path representing HyperparameterTuningJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromIndexEndpointName(indexEndpointName)
    
    
    matchLocationFromIndexEndpointName(indexEndpointName: string): string | number;

Parse the location from IndexEndpoint resource.

**Parameter**  
---  
**Name** | **Description**  
`indexEndpointName` |  `string`   
A fully-qualified path representing IndexEndpoint resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromIndexName(indexName)
    
    
    matchLocationFromIndexName(indexName: string): string | number;

Parse the location from Index resource.

**Parameter**  
---  
**Name** | **Description**  
`indexName` |  `string`   
A fully-qualified path representing Index resource.  
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
  
### matchLocationFromMemoryName(memoryName)
    
    
    matchLocationFromMemoryName(memoryName: string): string | number;

Parse the location from Memory resource.

**Parameter**  
---  
**Name** | **Description**  
`memoryName` |  `string`   
A fully-qualified path representing Memory resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromMetadataSchemaName(metadataSchemaName)
    
    
    matchLocationFromMetadataSchemaName(metadataSchemaName: string): string | number;

Parse the location from MetadataSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`metadataSchemaName` |  `string`   
A fully-qualified path representing MetadataSchema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromMetadataStoreName(metadataStoreName)
    
    
    matchLocationFromMetadataStoreName(metadataStoreName: string): string | number;

Parse the location from MetadataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`metadataStoreName` |  `string`   
A fully-qualified path representing MetadataStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromModelDeploymentMonitoringJobName(modelDeploymentMonitoringJobName)
    
    
    matchLocationFromModelDeploymentMonitoringJobName(modelDeploymentMonitoringJobName: string): string | number;

Parse the location from ModelDeploymentMonitoringJob resource.

**Parameter**  
---  
**Name** | **Description**  
`modelDeploymentMonitoringJobName` |  `string`   
A fully-qualified path representing ModelDeploymentMonitoringJob resource.  
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
  
### matchLocationFromModelEvaluationSliceName(modelEvaluationSliceName)
    
    
    matchLocationFromModelEvaluationSliceName(modelEvaluationSliceName: string): string | number;

Parse the location from ModelEvaluationSlice resource.

**Parameter**  
---  
**Name** | **Description**  
`modelEvaluationSliceName` |  `string`   
A fully-qualified path representing ModelEvaluationSlice resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromModelMonitoringJobName(modelMonitoringJobName)
    
    
    matchLocationFromModelMonitoringJobName(modelMonitoringJobName: string): string | number;

Parse the location from ModelMonitoringJob resource.

**Parameter**  
---  
**Name** | **Description**  
`modelMonitoringJobName` |  `string`   
A fully-qualified path representing ModelMonitoringJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromModelMonitorName(modelMonitorName)
    
    
    matchLocationFromModelMonitorName(modelMonitorName: string): string | number;

Parse the location from ModelMonitor resource.

**Parameter**  
---  
**Name** | **Description**  
`modelMonitorName` |  `string`   
A fully-qualified path representing ModelMonitor resource.  
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
  
### matchLocationFromNasJobName(nasJobName)
    
    
    matchLocationFromNasJobName(nasJobName: string): string | number;

Parse the location from NasJob resource.

**Parameter**  
---  
**Name** | **Description**  
`nasJobName` |  `string`   
A fully-qualified path representing NasJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromNasTrialDetailName(nasTrialDetailName)
    
    
    matchLocationFromNasTrialDetailName(nasTrialDetailName: string): string | number;

Parse the location from NasTrialDetail resource.

**Parameter**  
---  
**Name** | **Description**  
`nasTrialDetailName` |  `string`   
A fully-qualified path representing NasTrialDetail resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromNotebookExecutionJobName(notebookExecutionJobName)
    
    
    matchLocationFromNotebookExecutionJobName(notebookExecutionJobName: string): string | number;

Parse the location from NotebookExecutionJob resource.

**Parameter**  
---  
**Name** | **Description**  
`notebookExecutionJobName` |  `string`   
A fully-qualified path representing NotebookExecutionJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromNotebookRuntimeName(notebookRuntimeName)
    
    
    matchLocationFromNotebookRuntimeName(notebookRuntimeName: string): string | number;

Parse the location from NotebookRuntime resource.

**Parameter**  
---  
**Name** | **Description**  
`notebookRuntimeName` |  `string`   
A fully-qualified path representing NotebookRuntime resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromNotebookRuntimeTemplateName(notebookRuntimeTemplateName)
    
    
    matchLocationFromNotebookRuntimeTemplateName(notebookRuntimeTemplateName: string): string | number;

Parse the location from NotebookRuntimeTemplate resource.

**Parameter**  
---  
**Name** | **Description**  
`notebookRuntimeTemplateName` |  `string`   
A fully-qualified path representing NotebookRuntimeTemplate resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromOnlineEvaluatorName(onlineEvaluatorName)
    
    
    matchLocationFromOnlineEvaluatorName(onlineEvaluatorName: string): string | number;

Parse the location from OnlineEvaluator resource.

**Parameter**  
---  
**Name** | **Description**  
`onlineEvaluatorName` |  `string`   
A fully-qualified path representing OnlineEvaluator resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromPersistentResourceName(persistentResourceName)
    
    
    matchLocationFromPersistentResourceName(persistentResourceName: string): string | number;

Parse the location from PersistentResource resource.

**Parameter**  
---  
**Name** | **Description**  
`persistentResourceName` |  `string`   
A fully-qualified path representing PersistentResource resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromPipelineJobName(pipelineJobName)
    
    
    matchLocationFromPipelineJobName(pipelineJobName: string): string | number;

Parse the location from PipelineJob resource.

**Parameter**  
---  
**Name** | **Description**  
`pipelineJobName` |  `string`   
A fully-qualified path representing PipelineJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationEndpointName(projectLocationEndpointName)
    
    
    matchLocationFromProjectLocationEndpointName(projectLocationEndpointName: string): string | number;

Parse the location from ProjectLocationEndpoint resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationEndpointName` |  `string`   
A fully-qualified path representing project_location_endpoint resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationFeatureGroupFeaturesName(projectLocationFeatureGroupFeaturesName)
    
    
    matchLocationFromProjectLocationFeatureGroupFeaturesName(projectLocationFeatureGroupFeaturesName: string): string | number;

Parse the location from ProjectLocationFeatureGroupFeatures resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationFeatureGroupFeaturesName` |  `string`   
A fully-qualified path representing project_location_feature_group_features resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationFeaturestoreEntityTypeFeaturesName(projectLocationFeaturestoreEntityTypeFeaturesName)
    
    
    matchLocationFromProjectLocationFeaturestoreEntityTypeFeaturesName(projectLocationFeaturestoreEntityTypeFeaturesName: string): string | number;

Parse the location from ProjectLocationFeaturestoreEntityTypeFeatures resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationFeaturestoreEntityTypeFeaturesName` |  `string`   
A fully-qualified path representing project_location_featurestore_entity_type_features resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationPublisherModelName(projectLocationPublisherModelName)
    
    
    matchLocationFromProjectLocationPublisherModelName(projectLocationPublisherModelName: string): string | number;

Parse the location from ProjectLocationPublisherModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationPublisherModelName` |  `string`   
A fully-qualified path representing project_location_publisher_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromRagCorpusName(ragCorpusName)
    
    
    matchLocationFromRagCorpusName(ragCorpusName: string): string | number;

Parse the location from RagCorpus resource.

**Parameter**  
---  
**Name** | **Description**  
`ragCorpusName` |  `string`   
A fully-qualified path representing RagCorpus resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromRagDataSchemaName(ragDataSchemaName)
    
    
    matchLocationFromRagDataSchemaName(ragDataSchemaName: string): string | number;

Parse the location from RagDataSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`ragDataSchemaName` |  `string`   
A fully-qualified path representing RagDataSchema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromRagEngineConfigName(ragEngineConfigName)
    
    
    matchLocationFromRagEngineConfigName(ragEngineConfigName: string): string | number;

Parse the location from RagEngineConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`ragEngineConfigName` |  `string`   
A fully-qualified path representing RagEngineConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromRagFileName(ragFileName)
    
    
    matchLocationFromRagFileName(ragFileName: string): string | number;

Parse the location from RagFile resource.

**Parameter**  
---  
**Name** | **Description**  
`ragFileName` |  `string`   
A fully-qualified path representing RagFile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromRagMetadataName(ragMetadataName)
    
    
    matchLocationFromRagMetadataName(ragMetadataName: string): string | number;

Parse the location from RagMetadata resource.

**Parameter**  
---  
**Name** | **Description**  
`ragMetadataName` |  `string`   
A fully-qualified path representing RagMetadata resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromReasoningEngineName(reasoningEngineName)
    
    
    matchLocationFromReasoningEngineName(reasoningEngineName: string): string | number;

Parse the location from ReasoningEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`reasoningEngineName` |  `string`   
A fully-qualified path representing ReasoningEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromReasoningEngineRuntimeRevisionName(reasoningEngineRuntimeRevisionName)
    
    
    matchLocationFromReasoningEngineRuntimeRevisionName(reasoningEngineRuntimeRevisionName: string): string | number;

Parse the location from ReasoningEngineRuntimeRevision resource.

**Parameter**  
---  
**Name** | **Description**  
`reasoningEngineRuntimeRevisionName` |  `string`   
A fully-qualified path representing ReasoningEngineRuntimeRevision resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSavedQueryName(savedQueryName)
    
    
    matchLocationFromSavedQueryName(savedQueryName: string): string | number;

Parse the location from SavedQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`savedQueryName` |  `string`   
A fully-qualified path representing SavedQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromScheduleName(scheduleName)
    
    
    matchLocationFromScheduleName(scheduleName: string): string | number;

Parse the location from Schedule resource.

**Parameter**  
---  
**Name** | **Description**  
`scheduleName` |  `string`   
A fully-qualified path representing Schedule resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSessionEventName(sessionEventName)
    
    
    matchLocationFromSessionEventName(sessionEventName: string): string | number;

Parse the location from SessionEvent resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionEventName` |  `string`   
A fully-qualified path representing SessionEvent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSessionName(sessionName)
    
    
    matchLocationFromSessionName(sessionName: string): string | number;

Parse the location from Session resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionName` |  `string`   
A fully-qualified path representing Session resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSpecialistPoolName(specialistPoolName)
    
    
    matchLocationFromSpecialistPoolName(specialistPoolName: string): string | number;

Parse the location from SpecialistPool resource.

**Parameter**  
---  
**Name** | **Description**  
`specialistPoolName` |  `string`   
A fully-qualified path representing SpecialistPool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromStudyName(studyName)
    
    
    matchLocationFromStudyName(studyName: string): string | number;

Parse the location from Study resource.

**Parameter**  
---  
**Name** | **Description**  
`studyName` |  `string`   
A fully-qualified path representing Study resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTensorboardExperimentName(tensorboardExperimentName)
    
    
    matchLocationFromTensorboardExperimentName(tensorboardExperimentName: string): string | number;

Parse the location from TensorboardExperiment resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardExperimentName` |  `string`   
A fully-qualified path representing TensorboardExperiment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTensorboardName(tensorboardName)
    
    
    matchLocationFromTensorboardName(tensorboardName: string): string | number;

Parse the location from Tensorboard resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardName` |  `string`   
A fully-qualified path representing Tensorboard resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTensorboardRunName(tensorboardRunName)
    
    
    matchLocationFromTensorboardRunName(tensorboardRunName: string): string | number;

Parse the location from TensorboardRun resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardRunName` |  `string`   
A fully-qualified path representing TensorboardRun resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTensorboardTimeSeriesName(tensorboardTimeSeriesName)
    
    
    matchLocationFromTensorboardTimeSeriesName(tensorboardTimeSeriesName: string): string | number;

Parse the location from TensorboardTimeSeries resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardTimeSeriesName` |  `string`   
A fully-qualified path representing TensorboardTimeSeries resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTrainingPipelineName(trainingPipelineName)
    
    
    matchLocationFromTrainingPipelineName(trainingPipelineName: string): string | number;

Parse the location from TrainingPipeline resource.

**Parameter**  
---  
**Name** | **Description**  
`trainingPipelineName` |  `string`   
A fully-qualified path representing TrainingPipeline resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTrialName(trialName)
    
    
    matchLocationFromTrialName(trialName: string): string | number;

Parse the location from Trial resource.

**Parameter**  
---  
**Name** | **Description**  
`trialName` |  `string`   
A fully-qualified path representing Trial resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTuningJobName(tuningJobName)
    
    
    matchLocationFromTuningJobName(tuningJobName: string): string | number;

Parse the location from TuningJob resource.

**Parameter**  
---  
**Name** | **Description**  
`tuningJobName` |  `string`   
A fully-qualified path representing TuningJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchMemoryFromMemoryName(memoryName)
    
    
    matchMemoryFromMemoryName(memoryName: string): string | number;

Parse the memory from Memory resource.

**Parameter**  
---  
**Name** | **Description**  
`memoryName` |  `string`   
A fully-qualified path representing Memory resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the memory.  
  
### matchMetadataSchemaFromMetadataSchemaName(metadataSchemaName)
    
    
    matchMetadataSchemaFromMetadataSchemaName(metadataSchemaName: string): string | number;

Parse the metadata_schema from MetadataSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`metadataSchemaName` |  `string`   
A fully-qualified path representing MetadataSchema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the metadata_schema.  
  
### matchMetadataStoreFromArtifactName(artifactName)
    
    
    matchMetadataStoreFromArtifactName(artifactName: string): string | number;

Parse the metadata_store from Artifact resource.

**Parameter**  
---  
**Name** | **Description**  
`artifactName` |  `string`   
A fully-qualified path representing Artifact resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the metadata_store.  
  
### matchMetadataStoreFromContextName(contextName)
    
    
    matchMetadataStoreFromContextName(contextName: string): string | number;

Parse the metadata_store from Context resource.

**Parameter**  
---  
**Name** | **Description**  
`contextName` |  `string`   
A fully-qualified path representing Context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the metadata_store.  
  
### matchMetadataStoreFromExecutionName(executionName)
    
    
    matchMetadataStoreFromExecutionName(executionName: string): string | number;

Parse the metadata_store from Execution resource.

**Parameter**  
---  
**Name** | **Description**  
`executionName` |  `string`   
A fully-qualified path representing Execution resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the metadata_store.  
  
### matchMetadataStoreFromMetadataSchemaName(metadataSchemaName)
    
    
    matchMetadataStoreFromMetadataSchemaName(metadataSchemaName: string): string | number;

Parse the metadata_store from MetadataSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`metadataSchemaName` |  `string`   
A fully-qualified path representing MetadataSchema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the metadata_store.  
  
### matchMetadataStoreFromMetadataStoreName(metadataStoreName)
    
    
    matchMetadataStoreFromMetadataStoreName(metadataStoreName: string): string | number;

Parse the metadata_store from MetadataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`metadataStoreName` |  `string`   
A fully-qualified path representing MetadataStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the metadata_store.  
  
### matchModelDeploymentMonitoringJobFromModelDeploymentMonitoringJobName(modelDeploymentMonitoringJobName)
    
    
    matchModelDeploymentMonitoringJobFromModelDeploymentMonitoringJobName(modelDeploymentMonitoringJobName: string): string | number;

Parse the model_deployment_monitoring_job from ModelDeploymentMonitoringJob resource.

**Parameter**  
---  
**Name** | **Description**  
`modelDeploymentMonitoringJobName` |  `string`   
A fully-qualified path representing ModelDeploymentMonitoringJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the model_deployment_monitoring_job.  
  
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
  
### matchModelFromModelEvaluationSliceName(modelEvaluationSliceName)
    
    
    matchModelFromModelEvaluationSliceName(modelEvaluationSliceName: string): string | number;

Parse the model from ModelEvaluationSlice resource.

**Parameter**  
---  
**Name** | **Description**  
`modelEvaluationSliceName` |  `string`   
A fully-qualified path representing ModelEvaluationSlice resource.  
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
  
### matchModelFromProjectLocationPublisherModelName(projectLocationPublisherModelName)
    
    
    matchModelFromProjectLocationPublisherModelName(projectLocationPublisherModelName: string): string | number;

Parse the model from ProjectLocationPublisherModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationPublisherModelName` |  `string`   
A fully-qualified path representing project_location_publisher_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the model.  
  
### matchModelFromPublisherModelName(publisherModelName)
    
    
    matchModelFromPublisherModelName(publisherModelName: string): string | number;

Parse the model from PublisherModel resource.

**Parameter**  
---  
**Name** | **Description**  
`publisherModelName` |  `string`   
A fully-qualified path representing PublisherModel resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the model.  
  
### matchModelMonitorFromModelMonitoringJobName(modelMonitoringJobName)
    
    
    matchModelMonitorFromModelMonitoringJobName(modelMonitoringJobName: string): string | number;

Parse the model_monitor from ModelMonitoringJob resource.

**Parameter**  
---  
**Name** | **Description**  
`modelMonitoringJobName` |  `string`   
A fully-qualified path representing ModelMonitoringJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the model_monitor.  
  
### matchModelMonitorFromModelMonitorName(modelMonitorName)
    
    
    matchModelMonitorFromModelMonitorName(modelMonitorName: string): string | number;

Parse the model_monitor from ModelMonitor resource.

**Parameter**  
---  
**Name** | **Description**  
`modelMonitorName` |  `string`   
A fully-qualified path representing ModelMonitor resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the model_monitor.  
  
### matchModelMonitoringJobFromModelMonitoringJobName(modelMonitoringJobName)
    
    
    matchModelMonitoringJobFromModelMonitoringJobName(modelMonitoringJobName: string): string | number;

Parse the model_monitoring_job from ModelMonitoringJob resource.

**Parameter**  
---  
**Name** | **Description**  
`modelMonitoringJobName` |  `string`   
A fully-qualified path representing ModelMonitoringJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the model_monitoring_job.  
  
### matchNasJobFromNasJobName(nasJobName)
    
    
    matchNasJobFromNasJobName(nasJobName: string): string | number;

Parse the nas_job from NasJob resource.

**Parameter**  
---  
**Name** | **Description**  
`nasJobName` |  `string`   
A fully-qualified path representing NasJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the nas_job.  
  
### matchNasJobFromNasTrialDetailName(nasTrialDetailName)
    
    
    matchNasJobFromNasTrialDetailName(nasTrialDetailName: string): string | number;

Parse the nas_job from NasTrialDetail resource.

**Parameter**  
---  
**Name** | **Description**  
`nasTrialDetailName` |  `string`   
A fully-qualified path representing NasTrialDetail resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the nas_job.  
  
### matchNasTrialDetailFromNasTrialDetailName(nasTrialDetailName)
    
    
    matchNasTrialDetailFromNasTrialDetailName(nasTrialDetailName: string): string | number;

Parse the nas_trial_detail from NasTrialDetail resource.

**Parameter**  
---  
**Name** | **Description**  
`nasTrialDetailName` |  `string`   
A fully-qualified path representing NasTrialDetail resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the nas_trial_detail.  
  
### matchNotebookExecutionJobFromNotebookExecutionJobName(notebookExecutionJobName)
    
    
    matchNotebookExecutionJobFromNotebookExecutionJobName(notebookExecutionJobName: string): string | number;

Parse the notebook_execution_job from NotebookExecutionJob resource.

**Parameter**  
---  
**Name** | **Description**  
`notebookExecutionJobName` |  `string`   
A fully-qualified path representing NotebookExecutionJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the notebook_execution_job.  
  
### matchNotebookRuntimeFromNotebookRuntimeName(notebookRuntimeName)
    
    
    matchNotebookRuntimeFromNotebookRuntimeName(notebookRuntimeName: string): string | number;

Parse the notebook_runtime from NotebookRuntime resource.

**Parameter**  
---  
**Name** | **Description**  
`notebookRuntimeName` |  `string`   
A fully-qualified path representing NotebookRuntime resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the notebook_runtime.  
  
### matchNotebookRuntimeTemplateFromNotebookRuntimeTemplateName(notebookRuntimeTemplateName)
    
    
    matchNotebookRuntimeTemplateFromNotebookRuntimeTemplateName(notebookRuntimeTemplateName: string): string | number;

Parse the notebook_runtime_template from NotebookRuntimeTemplate resource.

**Parameter**  
---  
**Name** | **Description**  
`notebookRuntimeTemplateName` |  `string`   
A fully-qualified path representing NotebookRuntimeTemplate resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the notebook_runtime_template.  
  
### matchOnlineEvaluatorFromOnlineEvaluatorName(onlineEvaluatorName)
    
    
    matchOnlineEvaluatorFromOnlineEvaluatorName(onlineEvaluatorName: string): string | number;

Parse the online_evaluator from OnlineEvaluator resource.

**Parameter**  
---  
**Name** | **Description**  
`onlineEvaluatorName` |  `string`   
A fully-qualified path representing OnlineEvaluator resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the online_evaluator.  
  
### matchPersistentResourceFromPersistentResourceName(persistentResourceName)
    
    
    matchPersistentResourceFromPersistentResourceName(persistentResourceName: string): string | number;

Parse the persistent_resource from PersistentResource resource.

**Parameter**  
---  
**Name** | **Description**  
`persistentResourceName` |  `string`   
A fully-qualified path representing PersistentResource resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the persistent_resource.  
  
### matchPipelineJobFromPipelineJobName(pipelineJobName)
    
    
    matchPipelineJobFromPipelineJobName(pipelineJobName: string): string | number;

Parse the pipeline_job from PipelineJob resource.

**Parameter**  
---  
**Name** | **Description**  
`pipelineJobName` |  `string`   
A fully-qualified path representing PipelineJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the pipeline_job.  
  
### matchProjectFromAnnotationName(annotationName)
    
    
    matchProjectFromAnnotationName(annotationName: string): string | number;

Parse the project from Annotation resource.

**Parameter**  
---  
**Name** | **Description**  
`annotationName` |  `string`   
A fully-qualified path representing Annotation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
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
  
### matchProjectFromArtifactName(artifactName)
    
    
    matchProjectFromArtifactName(artifactName: string): string | number;

Parse the project from Artifact resource.

**Parameter**  
---  
**Name** | **Description**  
`artifactName` |  `string`   
A fully-qualified path representing Artifact resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromBatchPredictionJobName(batchPredictionJobName)
    
    
    matchProjectFromBatchPredictionJobName(batchPredictionJobName: string): string | number;

Parse the project from BatchPredictionJob resource.

**Parameter**  
---  
**Name** | **Description**  
`batchPredictionJobName` |  `string`   
A fully-qualified path representing BatchPredictionJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromCachedContentName(cachedContentName)
    
    
    matchProjectFromCachedContentName(cachedContentName: string): string | number;

Parse the project from CachedContent resource.

**Parameter**  
---  
**Name** | **Description**  
`cachedContentName` |  `string`   
A fully-qualified path representing CachedContent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromContextName(contextName)
    
    
    matchProjectFromContextName(contextName: string): string | number;

Parse the project from Context resource.

**Parameter**  
---  
**Name** | **Description**  
`contextName` |  `string`   
A fully-qualified path representing Context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromCustomJobName(customJobName)
    
    
    matchProjectFromCustomJobName(customJobName: string): string | number;

Parse the project from CustomJob resource.

**Parameter**  
---  
**Name** | **Description**  
`customJobName` |  `string`   
A fully-qualified path representing CustomJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromDataItemName(dataItemName)
    
    
    matchProjectFromDataItemName(dataItemName: string): string | number;

Parse the project from DataItem resource.

**Parameter**  
---  
**Name** | **Description**  
`dataItemName` |  `string`   
A fully-qualified path representing DataItem resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromDataLabelingJobName(dataLabelingJobName)
    
    
    matchProjectFromDataLabelingJobName(dataLabelingJobName: string): string | number;

Parse the project from DataLabelingJob resource.

**Parameter**  
---  
**Name** | **Description**  
`dataLabelingJobName` |  `string`   
A fully-qualified path representing DataLabelingJob resource.  
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
  
### matchProjectFromDatasetVersionName(datasetVersionName)
    
    
    matchProjectFromDatasetVersionName(datasetVersionName: string): string | number;

Parse the project from DatasetVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`datasetVersionName` |  `string`   
A fully-qualified path representing DatasetVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromDeploymentResourcePoolName(deploymentResourcePoolName)
    
    
    matchProjectFromDeploymentResourcePoolName(deploymentResourcePoolName: string): string | number;

Parse the project from DeploymentResourcePool resource.

**Parameter**  
---  
**Name** | **Description**  
`deploymentResourcePoolName` |  `string`   
A fully-qualified path representing DeploymentResourcePool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromEntityTypeName(entityTypeName)
    
    
    matchProjectFromEntityTypeName(entityTypeName: string): string | number;

Parse the project from EntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`entityTypeName` |  `string`   
A fully-qualified path representing EntityType resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromExampleStoreName(exampleStoreName)
    
    
    matchProjectFromExampleStoreName(exampleStoreName: string): string | number;

Parse the project from ExampleStore resource.

**Parameter**  
---  
**Name** | **Description**  
`exampleStoreName` |  `string`   
A fully-qualified path representing ExampleStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromExecutionName(executionName)
    
    
    matchProjectFromExecutionName(executionName: string): string | number;

Parse the project from Execution resource.

**Parameter**  
---  
**Name** | **Description**  
`executionName` |  `string`   
A fully-qualified path representing Execution resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromExtensionName(extensionName)
    
    
    matchProjectFromExtensionName(extensionName: string): string | number;

Parse the project from Extension resource.

**Parameter**  
---  
**Name** | **Description**  
`extensionName` |  `string`   
A fully-qualified path representing Extension resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromFeatureGroupName(featureGroupName)
    
    
    matchProjectFromFeatureGroupName(featureGroupName: string): string | number;

Parse the project from FeatureGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`featureGroupName` |  `string`   
A fully-qualified path representing FeatureGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromFeatureMonitorJobName(featureMonitorJobName)
    
    
    matchProjectFromFeatureMonitorJobName(featureMonitorJobName: string): string | number;

Parse the project from FeatureMonitorJob resource.

**Parameter**  
---  
**Name** | **Description**  
`featureMonitorJobName` |  `string`   
A fully-qualified path representing FeatureMonitorJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromFeatureMonitorName(featureMonitorName)
    
    
    matchProjectFromFeatureMonitorName(featureMonitorName: string): string | number;

Parse the project from FeatureMonitor resource.

**Parameter**  
---  
**Name** | **Description**  
`featureMonitorName` |  `string`   
A fully-qualified path representing FeatureMonitor resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromFeatureOnlineStoreName(featureOnlineStoreName)
    
    
    matchProjectFromFeatureOnlineStoreName(featureOnlineStoreName: string): string | number;

Parse the project from FeatureOnlineStore resource.

**Parameter**  
---  
**Name** | **Description**  
`featureOnlineStoreName` |  `string`   
A fully-qualified path representing FeatureOnlineStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromFeaturestoreName(featurestoreName)
    
    
    matchProjectFromFeaturestoreName(featurestoreName: string): string | number;

Parse the project from Featurestore resource.

**Parameter**  
---  
**Name** | **Description**  
`featurestoreName` |  `string`   
A fully-qualified path representing Featurestore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromFeatureViewName(featureViewName)
    
    
    matchProjectFromFeatureViewName(featureViewName: string): string | number;

Parse the project from FeatureView resource.

**Parameter**  
---  
**Name** | **Description**  
`featureViewName` |  `string`   
A fully-qualified path representing FeatureView resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromFeatureViewSyncName(featureViewSyncName)
    
    
    matchProjectFromFeatureViewSyncName(featureViewSyncName: string): string | number;

Parse the project from FeatureViewSync resource.

**Parameter**  
---  
**Name** | **Description**  
`featureViewSyncName` |  `string`   
A fully-qualified path representing FeatureViewSync resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromHyperparameterTuningJobName(hyperparameterTuningJobName)
    
    
    matchProjectFromHyperparameterTuningJobName(hyperparameterTuningJobName: string): string | number;

Parse the project from HyperparameterTuningJob resource.

**Parameter**  
---  
**Name** | **Description**  
`hyperparameterTuningJobName` |  `string`   
A fully-qualified path representing HyperparameterTuningJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromIndexEndpointName(indexEndpointName)
    
    
    matchProjectFromIndexEndpointName(indexEndpointName: string): string | number;

Parse the project from IndexEndpoint resource.

**Parameter**  
---  
**Name** | **Description**  
`indexEndpointName` |  `string`   
A fully-qualified path representing IndexEndpoint resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromIndexName(indexName)
    
    
    matchProjectFromIndexName(indexName: string): string | number;

Parse the project from Index resource.

**Parameter**  
---  
**Name** | **Description**  
`indexName` |  `string`   
A fully-qualified path representing Index resource.  
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
  
### matchProjectFromMemoryName(memoryName)
    
    
    matchProjectFromMemoryName(memoryName: string): string | number;

Parse the project from Memory resource.

**Parameter**  
---  
**Name** | **Description**  
`memoryName` |  `string`   
A fully-qualified path representing Memory resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromMetadataSchemaName(metadataSchemaName)
    
    
    matchProjectFromMetadataSchemaName(metadataSchemaName: string): string | number;

Parse the project from MetadataSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`metadataSchemaName` |  `string`   
A fully-qualified path representing MetadataSchema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromMetadataStoreName(metadataStoreName)
    
    
    matchProjectFromMetadataStoreName(metadataStoreName: string): string | number;

Parse the project from MetadataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`metadataStoreName` |  `string`   
A fully-qualified path representing MetadataStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromModelDeploymentMonitoringJobName(modelDeploymentMonitoringJobName)
    
    
    matchProjectFromModelDeploymentMonitoringJobName(modelDeploymentMonitoringJobName: string): string | number;

Parse the project from ModelDeploymentMonitoringJob resource.

**Parameter**  
---  
**Name** | **Description**  
`modelDeploymentMonitoringJobName` |  `string`   
A fully-qualified path representing ModelDeploymentMonitoringJob resource.  
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
  
### matchProjectFromModelEvaluationSliceName(modelEvaluationSliceName)
    
    
    matchProjectFromModelEvaluationSliceName(modelEvaluationSliceName: string): string | number;

Parse the project from ModelEvaluationSlice resource.

**Parameter**  
---  
**Name** | **Description**  
`modelEvaluationSliceName` |  `string`   
A fully-qualified path representing ModelEvaluationSlice resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromModelMonitoringJobName(modelMonitoringJobName)
    
    
    matchProjectFromModelMonitoringJobName(modelMonitoringJobName: string): string | number;

Parse the project from ModelMonitoringJob resource.

**Parameter**  
---  
**Name** | **Description**  
`modelMonitoringJobName` |  `string`   
A fully-qualified path representing ModelMonitoringJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromModelMonitorName(modelMonitorName)
    
    
    matchProjectFromModelMonitorName(modelMonitorName: string): string | number;

Parse the project from ModelMonitor resource.

**Parameter**  
---  
**Name** | **Description**  
`modelMonitorName` |  `string`   
A fully-qualified path representing ModelMonitor resource.  
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
  
### matchProjectFromNasJobName(nasJobName)
    
    
    matchProjectFromNasJobName(nasJobName: string): string | number;

Parse the project from NasJob resource.

**Parameter**  
---  
**Name** | **Description**  
`nasJobName` |  `string`   
A fully-qualified path representing NasJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromNasTrialDetailName(nasTrialDetailName)
    
    
    matchProjectFromNasTrialDetailName(nasTrialDetailName: string): string | number;

Parse the project from NasTrialDetail resource.

**Parameter**  
---  
**Name** | **Description**  
`nasTrialDetailName` |  `string`   
A fully-qualified path representing NasTrialDetail resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromNotebookExecutionJobName(notebookExecutionJobName)
    
    
    matchProjectFromNotebookExecutionJobName(notebookExecutionJobName: string): string | number;

Parse the project from NotebookExecutionJob resource.

**Parameter**  
---  
**Name** | **Description**  
`notebookExecutionJobName` |  `string`   
A fully-qualified path representing NotebookExecutionJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromNotebookRuntimeName(notebookRuntimeName)
    
    
    matchProjectFromNotebookRuntimeName(notebookRuntimeName: string): string | number;

Parse the project from NotebookRuntime resource.

**Parameter**  
---  
**Name** | **Description**  
`notebookRuntimeName` |  `string`   
A fully-qualified path representing NotebookRuntime resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromNotebookRuntimeTemplateName(notebookRuntimeTemplateName)
    
    
    matchProjectFromNotebookRuntimeTemplateName(notebookRuntimeTemplateName: string): string | number;

Parse the project from NotebookRuntimeTemplate resource.

**Parameter**  
---  
**Name** | **Description**  
`notebookRuntimeTemplateName` |  `string`   
A fully-qualified path representing NotebookRuntimeTemplate resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromOnlineEvaluatorName(onlineEvaluatorName)
    
    
    matchProjectFromOnlineEvaluatorName(onlineEvaluatorName: string): string | number;

Parse the project from OnlineEvaluator resource.

**Parameter**  
---  
**Name** | **Description**  
`onlineEvaluatorName` |  `string`   
A fully-qualified path representing OnlineEvaluator resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromPersistentResourceName(persistentResourceName)
    
    
    matchProjectFromPersistentResourceName(persistentResourceName: string): string | number;

Parse the project from PersistentResource resource.

**Parameter**  
---  
**Name** | **Description**  
`persistentResourceName` |  `string`   
A fully-qualified path representing PersistentResource resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromPipelineJobName(pipelineJobName)
    
    
    matchProjectFromPipelineJobName(pipelineJobName: string): string | number;

Parse the project from PipelineJob resource.

**Parameter**  
---  
**Name** | **Description**  
`pipelineJobName` |  `string`   
A fully-qualified path representing PipelineJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationEndpointName(projectLocationEndpointName)
    
    
    matchProjectFromProjectLocationEndpointName(projectLocationEndpointName: string): string | number;

Parse the project from ProjectLocationEndpoint resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationEndpointName` |  `string`   
A fully-qualified path representing project_location_endpoint resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationFeatureGroupFeaturesName(projectLocationFeatureGroupFeaturesName)
    
    
    matchProjectFromProjectLocationFeatureGroupFeaturesName(projectLocationFeatureGroupFeaturesName: string): string | number;

Parse the project from ProjectLocationFeatureGroupFeatures resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationFeatureGroupFeaturesName` |  `string`   
A fully-qualified path representing project_location_feature_group_features resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationFeaturestoreEntityTypeFeaturesName(projectLocationFeaturestoreEntityTypeFeaturesName)
    
    
    matchProjectFromProjectLocationFeaturestoreEntityTypeFeaturesName(projectLocationFeaturestoreEntityTypeFeaturesName: string): string | number;

Parse the project from ProjectLocationFeaturestoreEntityTypeFeatures resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationFeaturestoreEntityTypeFeaturesName` |  `string`   
A fully-qualified path representing project_location_featurestore_entity_type_features resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationPublisherModelName(projectLocationPublisherModelName)
    
    
    matchProjectFromProjectLocationPublisherModelName(projectLocationPublisherModelName: string): string | number;

Parse the project from ProjectLocationPublisherModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationPublisherModelName` |  `string`   
A fully-qualified path representing project_location_publisher_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromRagCorpusName(ragCorpusName)
    
    
    matchProjectFromRagCorpusName(ragCorpusName: string): string | number;

Parse the project from RagCorpus resource.

**Parameter**  
---  
**Name** | **Description**  
`ragCorpusName` |  `string`   
A fully-qualified path representing RagCorpus resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromRagDataSchemaName(ragDataSchemaName)
    
    
    matchProjectFromRagDataSchemaName(ragDataSchemaName: string): string | number;

Parse the project from RagDataSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`ragDataSchemaName` |  `string`   
A fully-qualified path representing RagDataSchema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromRagEngineConfigName(ragEngineConfigName)
    
    
    matchProjectFromRagEngineConfigName(ragEngineConfigName: string): string | number;

Parse the project from RagEngineConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`ragEngineConfigName` |  `string`   
A fully-qualified path representing RagEngineConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromRagFileName(ragFileName)
    
    
    matchProjectFromRagFileName(ragFileName: string): string | number;

Parse the project from RagFile resource.

**Parameter**  
---  
**Name** | **Description**  
`ragFileName` |  `string`   
A fully-qualified path representing RagFile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromRagMetadataName(ragMetadataName)
    
    
    matchProjectFromRagMetadataName(ragMetadataName: string): string | number;

Parse the project from RagMetadata resource.

**Parameter**  
---  
**Name** | **Description**  
`ragMetadataName` |  `string`   
A fully-qualified path representing RagMetadata resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromReasoningEngineName(reasoningEngineName)
    
    
    matchProjectFromReasoningEngineName(reasoningEngineName: string): string | number;

Parse the project from ReasoningEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`reasoningEngineName` |  `string`   
A fully-qualified path representing ReasoningEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromReasoningEngineRuntimeRevisionName(reasoningEngineRuntimeRevisionName)
    
    
    matchProjectFromReasoningEngineRuntimeRevisionName(reasoningEngineRuntimeRevisionName: string): string | number;

Parse the project from ReasoningEngineRuntimeRevision resource.

**Parameter**  
---  
**Name** | **Description**  
`reasoningEngineRuntimeRevisionName` |  `string`   
A fully-qualified path representing ReasoningEngineRuntimeRevision resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSavedQueryName(savedQueryName)
    
    
    matchProjectFromSavedQueryName(savedQueryName: string): string | number;

Parse the project from SavedQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`savedQueryName` |  `string`   
A fully-qualified path representing SavedQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromScheduleName(scheduleName)
    
    
    matchProjectFromScheduleName(scheduleName: string): string | number;

Parse the project from Schedule resource.

**Parameter**  
---  
**Name** | **Description**  
`scheduleName` |  `string`   
A fully-qualified path representing Schedule resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSessionEventName(sessionEventName)
    
    
    matchProjectFromSessionEventName(sessionEventName: string): string | number;

Parse the project from SessionEvent resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionEventName` |  `string`   
A fully-qualified path representing SessionEvent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSessionName(sessionName)
    
    
    matchProjectFromSessionName(sessionName: string): string | number;

Parse the project from Session resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionName` |  `string`   
A fully-qualified path representing Session resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSpecialistPoolName(specialistPoolName)
    
    
    matchProjectFromSpecialistPoolName(specialistPoolName: string): string | number;

Parse the project from SpecialistPool resource.

**Parameter**  
---  
**Name** | **Description**  
`specialistPoolName` |  `string`   
A fully-qualified path representing SpecialistPool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromStudyName(studyName)
    
    
    matchProjectFromStudyName(studyName: string): string | number;

Parse the project from Study resource.

**Parameter**  
---  
**Name** | **Description**  
`studyName` |  `string`   
A fully-qualified path representing Study resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTensorboardExperimentName(tensorboardExperimentName)
    
    
    matchProjectFromTensorboardExperimentName(tensorboardExperimentName: string): string | number;

Parse the project from TensorboardExperiment resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardExperimentName` |  `string`   
A fully-qualified path representing TensorboardExperiment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTensorboardName(tensorboardName)
    
    
    matchProjectFromTensorboardName(tensorboardName: string): string | number;

Parse the project from Tensorboard resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardName` |  `string`   
A fully-qualified path representing Tensorboard resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTensorboardRunName(tensorboardRunName)
    
    
    matchProjectFromTensorboardRunName(tensorboardRunName: string): string | number;

Parse the project from TensorboardRun resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardRunName` |  `string`   
A fully-qualified path representing TensorboardRun resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTensorboardTimeSeriesName(tensorboardTimeSeriesName)
    
    
    matchProjectFromTensorboardTimeSeriesName(tensorboardTimeSeriesName: string): string | number;

Parse the project from TensorboardTimeSeries resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardTimeSeriesName` |  `string`   
A fully-qualified path representing TensorboardTimeSeries resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTrainingPipelineName(trainingPipelineName)
    
    
    matchProjectFromTrainingPipelineName(trainingPipelineName: string): string | number;

Parse the project from TrainingPipeline resource.

**Parameter**  
---  
**Name** | **Description**  
`trainingPipelineName` |  `string`   
A fully-qualified path representing TrainingPipeline resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTrialName(trialName)
    
    
    matchProjectFromTrialName(trialName: string): string | number;

Parse the project from Trial resource.

**Parameter**  
---  
**Name** | **Description**  
`trialName` |  `string`   
A fully-qualified path representing Trial resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTuningJobName(tuningJobName)
    
    
    matchProjectFromTuningJobName(tuningJobName: string): string | number;

Parse the project from TuningJob resource.

**Parameter**  
---  
**Name** | **Description**  
`tuningJobName` |  `string`   
A fully-qualified path representing TuningJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchPublisherFromProjectLocationPublisherModelName(projectLocationPublisherModelName)
    
    
    matchPublisherFromProjectLocationPublisherModelName(projectLocationPublisherModelName: string): string | number;

Parse the publisher from ProjectLocationPublisherModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationPublisherModelName` |  `string`   
A fully-qualified path representing project_location_publisher_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the publisher.  
  
### matchPublisherFromPublisherModelName(publisherModelName)
    
    
    matchPublisherFromPublisherModelName(publisherModelName: string): string | number;

Parse the publisher from PublisherModel resource.

**Parameter**  
---  
**Name** | **Description**  
`publisherModelName` |  `string`   
A fully-qualified path representing PublisherModel resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the publisher.  
  
### matchRagCorpusFromRagCorpusName(ragCorpusName)
    
    
    matchRagCorpusFromRagCorpusName(ragCorpusName: string): string | number;

Parse the rag_corpus from RagCorpus resource.

**Parameter**  
---  
**Name** | **Description**  
`ragCorpusName` |  `string`   
A fully-qualified path representing RagCorpus resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the rag_corpus.  
  
### matchRagCorpusFromRagDataSchemaName(ragDataSchemaName)
    
    
    matchRagCorpusFromRagDataSchemaName(ragDataSchemaName: string): string | number;

Parse the rag_corpus from RagDataSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`ragDataSchemaName` |  `string`   
A fully-qualified path representing RagDataSchema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the rag_corpus.  
  
### matchRagCorpusFromRagFileName(ragFileName)
    
    
    matchRagCorpusFromRagFileName(ragFileName: string): string | number;

Parse the rag_corpus from RagFile resource.

**Parameter**  
---  
**Name** | **Description**  
`ragFileName` |  `string`   
A fully-qualified path representing RagFile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the rag_corpus.  
  
### matchRagCorpusFromRagMetadataName(ragMetadataName)
    
    
    matchRagCorpusFromRagMetadataName(ragMetadataName: string): string | number;

Parse the rag_corpus from RagMetadata resource.

**Parameter**  
---  
**Name** | **Description**  
`ragMetadataName` |  `string`   
A fully-qualified path representing RagMetadata resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the rag_corpus.  
  
### matchRagDataSchemaFromRagDataSchemaName(ragDataSchemaName)
    
    
    matchRagDataSchemaFromRagDataSchemaName(ragDataSchemaName: string): string | number;

Parse the rag_data_schema from RagDataSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`ragDataSchemaName` |  `string`   
A fully-qualified path representing RagDataSchema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the rag_data_schema.  
  
### matchRagFileFromRagFileName(ragFileName)
    
    
    matchRagFileFromRagFileName(ragFileName: string): string | number;

Parse the rag_file from RagFile resource.

**Parameter**  
---  
**Name** | **Description**  
`ragFileName` |  `string`   
A fully-qualified path representing RagFile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the rag_file.  
  
### matchRagFileFromRagMetadataName(ragMetadataName)
    
    
    matchRagFileFromRagMetadataName(ragMetadataName: string): string | number;

Parse the rag_file from RagMetadata resource.

**Parameter**  
---  
**Name** | **Description**  
`ragMetadataName` |  `string`   
A fully-qualified path representing RagMetadata resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the rag_file.  
  
### matchRagMetadataFromRagMetadataName(ragMetadataName)
    
    
    matchRagMetadataFromRagMetadataName(ragMetadataName: string): string | number;

Parse the rag_metadata from RagMetadata resource.

**Parameter**  
---  
**Name** | **Description**  
`ragMetadataName` |  `string`   
A fully-qualified path representing RagMetadata resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the rag_metadata.  
  
### matchReasoningEngineFromMemoryName(memoryName)
    
    
    matchReasoningEngineFromMemoryName(memoryName: string): string | number;

Parse the reasoning_engine from Memory resource.

**Parameter**  
---  
**Name** | **Description**  
`memoryName` |  `string`   
A fully-qualified path representing Memory resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the reasoning_engine.  
  
### matchReasoningEngineFromReasoningEngineName(reasoningEngineName)
    
    
    matchReasoningEngineFromReasoningEngineName(reasoningEngineName: string): string | number;

Parse the reasoning_engine from ReasoningEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`reasoningEngineName` |  `string`   
A fully-qualified path representing ReasoningEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the reasoning_engine.  
  
### matchReasoningEngineFromReasoningEngineRuntimeRevisionName(reasoningEngineRuntimeRevisionName)
    
    
    matchReasoningEngineFromReasoningEngineRuntimeRevisionName(reasoningEngineRuntimeRevisionName: string): string | number;

Parse the reasoning_engine from ReasoningEngineRuntimeRevision resource.

**Parameter**  
---  
**Name** | **Description**  
`reasoningEngineRuntimeRevisionName` |  `string`   
A fully-qualified path representing ReasoningEngineRuntimeRevision resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the reasoning_engine.  
  
### matchReasoningEngineFromSessionEventName(sessionEventName)
    
    
    matchReasoningEngineFromSessionEventName(sessionEventName: string): string | number;

Parse the reasoning_engine from SessionEvent resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionEventName` |  `string`   
A fully-qualified path representing SessionEvent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the reasoning_engine.  
  
### matchReasoningEngineFromSessionName(sessionName)
    
    
    matchReasoningEngineFromSessionName(sessionName: string): string | number;

Parse the reasoning_engine from Session resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionName` |  `string`   
A fully-qualified path representing Session resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the reasoning_engine.  
  
### matchRunFromTensorboardRunName(tensorboardRunName)
    
    
    matchRunFromTensorboardRunName(tensorboardRunName: string): string | number;

Parse the run from TensorboardRun resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardRunName` |  `string`   
A fully-qualified path representing TensorboardRun resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the run.  
  
### matchRunFromTensorboardTimeSeriesName(tensorboardTimeSeriesName)
    
    
    matchRunFromTensorboardTimeSeriesName(tensorboardTimeSeriesName: string): string | number;

Parse the run from TensorboardTimeSeries resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardTimeSeriesName` |  `string`   
A fully-qualified path representing TensorboardTimeSeries resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the run.  
  
### matchRuntimeRevisionFromReasoningEngineRuntimeRevisionName(reasoningEngineRuntimeRevisionName)
    
    
    matchRuntimeRevisionFromReasoningEngineRuntimeRevisionName(reasoningEngineRuntimeRevisionName: string): string | number;

Parse the runtime_revision from ReasoningEngineRuntimeRevision resource.

**Parameter**  
---  
**Name** | **Description**  
`reasoningEngineRuntimeRevisionName` |  `string`   
A fully-qualified path representing ReasoningEngineRuntimeRevision resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the runtime_revision.  
  
### matchSavedQueryFromSavedQueryName(savedQueryName)
    
    
    matchSavedQueryFromSavedQueryName(savedQueryName: string): string | number;

Parse the saved_query from SavedQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`savedQueryName` |  `string`   
A fully-qualified path representing SavedQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the saved_query.  
  
### matchScheduleFromScheduleName(scheduleName)
    
    
    matchScheduleFromScheduleName(scheduleName: string): string | number;

Parse the schedule from Schedule resource.

**Parameter**  
---  
**Name** | **Description**  
`scheduleName` |  `string`   
A fully-qualified path representing Schedule resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the schedule.  
  
### matchSessionFromSessionEventName(sessionEventName)
    
    
    matchSessionFromSessionEventName(sessionEventName: string): string | number;

Parse the session from SessionEvent resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionEventName` |  `string`   
A fully-qualified path representing SessionEvent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromSessionName(sessionName)
    
    
    matchSessionFromSessionName(sessionName: string): string | number;

Parse the session from Session resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionName` |  `string`   
A fully-qualified path representing Session resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSliceFromModelEvaluationSliceName(modelEvaluationSliceName)
    
    
    matchSliceFromModelEvaluationSliceName(modelEvaluationSliceName: string): string | number;

Parse the slice from ModelEvaluationSlice resource.

**Parameter**  
---  
**Name** | **Description**  
`modelEvaluationSliceName` |  `string`   
A fully-qualified path representing ModelEvaluationSlice resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the slice.  
  
### matchSpecialistPoolFromSpecialistPoolName(specialistPoolName)
    
    
    matchSpecialistPoolFromSpecialistPoolName(specialistPoolName: string): string | number;

Parse the specialist_pool from SpecialistPool resource.

**Parameter**  
---  
**Name** | **Description**  
`specialistPoolName` |  `string`   
A fully-qualified path representing SpecialistPool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the specialist_pool.  
  
### matchStudyFromStudyName(studyName)
    
    
    matchStudyFromStudyName(studyName: string): string | number;

Parse the study from Study resource.

**Parameter**  
---  
**Name** | **Description**  
`studyName` |  `string`   
A fully-qualified path representing Study resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the study.  
  
### matchStudyFromTrialName(trialName)
    
    
    matchStudyFromTrialName(trialName: string): string | number;

Parse the study from Trial resource.

**Parameter**  
---  
**Name** | **Description**  
`trialName` |  `string`   
A fully-qualified path representing Trial resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the study.  
  
### matchTensorboardFromTensorboardExperimentName(tensorboardExperimentName)
    
    
    matchTensorboardFromTensorboardExperimentName(tensorboardExperimentName: string): string | number;

Parse the tensorboard from TensorboardExperiment resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardExperimentName` |  `string`   
A fully-qualified path representing TensorboardExperiment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tensorboard.  
  
### matchTensorboardFromTensorboardName(tensorboardName)
    
    
    matchTensorboardFromTensorboardName(tensorboardName: string): string | number;

Parse the tensorboard from Tensorboard resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardName` |  `string`   
A fully-qualified path representing Tensorboard resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tensorboard.  
  
### matchTensorboardFromTensorboardRunName(tensorboardRunName)
    
    
    matchTensorboardFromTensorboardRunName(tensorboardRunName: string): string | number;

Parse the tensorboard from TensorboardRun resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardRunName` |  `string`   
A fully-qualified path representing TensorboardRun resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tensorboard.  
  
### matchTensorboardFromTensorboardTimeSeriesName(tensorboardTimeSeriesName)
    
    
    matchTensorboardFromTensorboardTimeSeriesName(tensorboardTimeSeriesName: string): string | number;

Parse the tensorboard from TensorboardTimeSeries resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardTimeSeriesName` |  `string`   
A fully-qualified path representing TensorboardTimeSeries resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tensorboard.  
  
### matchTimeSeriesFromTensorboardTimeSeriesName(tensorboardTimeSeriesName)
    
    
    matchTimeSeriesFromTensorboardTimeSeriesName(tensorboardTimeSeriesName: string): string | number;

Parse the time_series from TensorboardTimeSeries resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardTimeSeriesName` |  `string`   
A fully-qualified path representing TensorboardTimeSeries resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the time_series.  
  
### matchTrainingPipelineFromTrainingPipelineName(trainingPipelineName)
    
    
    matchTrainingPipelineFromTrainingPipelineName(trainingPipelineName: string): string | number;

Parse the training_pipeline from TrainingPipeline resource.

**Parameter**  
---  
**Name** | **Description**  
`trainingPipelineName` |  `string`   
A fully-qualified path representing TrainingPipeline resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the training_pipeline.  
  
### matchTrialFromTrialName(trialName)
    
    
    matchTrialFromTrialName(trialName: string): string | number;

Parse the trial from Trial resource.

**Parameter**  
---  
**Name** | **Description**  
`trialName` |  `string`   
A fully-qualified path representing Trial resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the trial.  
  
### matchTuningJobFromTuningJobName(tuningJobName)
    
    
    matchTuningJobFromTuningJobName(tuningJobName: string): string | number;

Parse the tuning_job from TuningJob resource.

**Parameter**  
---  
**Name** | **Description**  
`tuningJobName` |  `string`   
A fully-qualified path representing TuningJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tuning_job.  
  
### memoryPath(project, location, reasoningEngine, memory)
    
    
    memoryPath(project: string, location: string, reasoningEngine: string, memory: string): string;

Return a fully-qualified memory resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`reasoningEngine` |  `string`   
  
`memory` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### metadataSchemaPath(project, location, metadataStore, metadataSchema)
    
    
    metadataSchemaPath(project: string, location: string, metadataStore: string, metadataSchema: string): string;

Return a fully-qualified metadataSchema resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`metadataStore` |  `string`   
  
`metadataSchema` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### metadataStorePath(project, location, metadataStore)
    
    
    metadataStorePath(project: string, location: string, metadataStore: string): string;

Return a fully-qualified metadataStore resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`metadataStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### modelDeploymentMonitoringJobPath(project, location, modelDeploymentMonitoringJob)
    
    
    modelDeploymentMonitoringJobPath(project: string, location: string, modelDeploymentMonitoringJob: string): string;

Return a fully-qualified modelDeploymentMonitoringJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`modelDeploymentMonitoringJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### modelEvaluationPath(project, location, model, evaluation)
    
    
    modelEvaluationPath(project: string, location: string, model: string, evaluation: string): string;

Return a fully-qualified modelEvaluation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`model` |  `string`   
  
`evaluation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### modelEvaluationSlicePath(project, location, model, evaluation, slice)
    
    
    modelEvaluationSlicePath(project: string, location: string, model: string, evaluation: string, slice: string): string;

Return a fully-qualified modelEvaluationSlice resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`model` |  `string`   
  
`evaluation` |  `string`   
  
`slice` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### modelMonitoringJobPath(project, location, modelMonitor, modelMonitoringJob)
    
    
    modelMonitoringJobPath(project: string, location: string, modelMonitor: string, modelMonitoringJob: string): string;

Return a fully-qualified modelMonitoringJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`modelMonitor` |  `string`   
  
`modelMonitoringJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### modelMonitorPath(project, location, modelMonitor)
    
    
    modelMonitorPath(project: string, location: string, modelMonitor: string): string;

Return a fully-qualified modelMonitor resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`modelMonitor` |  `string`   
  
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
  
### nasJobPath(project, location, nasJob)
    
    
    nasJobPath(project: string, location: string, nasJob: string): string;

Return a fully-qualified nasJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`nasJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### nasTrialDetailPath(project, location, nasJob, nasTrialDetail)
    
    
    nasTrialDetailPath(project: string, location: string, nasJob: string, nasTrialDetail: string): string;

Return a fully-qualified nasTrialDetail resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`nasJob` |  `string`   
  
`nasTrialDetail` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### notebookExecutionJobPath(project, location, notebookExecutionJob)
    
    
    notebookExecutionJobPath(project: string, location: string, notebookExecutionJob: string): string;

Return a fully-qualified notebookExecutionJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`notebookExecutionJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### notebookRuntimePath(project, location, notebookRuntime)
    
    
    notebookRuntimePath(project: string, location: string, notebookRuntime: string): string;

Return a fully-qualified notebookRuntime resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`notebookRuntime` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### notebookRuntimeTemplatePath(project, location, notebookRuntimeTemplate)
    
    
    notebookRuntimeTemplatePath(project: string, location: string, notebookRuntimeTemplate: string): string;

Return a fully-qualified notebookRuntimeTemplate resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`notebookRuntimeTemplate` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### onlineEvaluatorPath(project, location, onlineEvaluator)
    
    
    onlineEvaluatorPath(project: string, location: string, onlineEvaluator: string): string;

Return a fully-qualified onlineEvaluator resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`onlineEvaluator` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### persistentResourcePath(project, location, persistentResource)
    
    
    persistentResourcePath(project: string, location: string, persistentResource: string): string;

Return a fully-qualified persistentResource resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`persistentResource` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### pipelineJobPath(project, location, pipelineJob)
    
    
    pipelineJobPath(project: string, location: string, pipelineJob: string): string;

Return a fully-qualified pipelineJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`pipelineJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationEndpointPath(project, location, endpoint)
    
    
    projectLocationEndpointPath(project: string, location: string, endpoint: string): string;

Return a fully-qualified projectLocationEndpoint resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`endpoint` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationFeatureGroupFeaturesPath(project, location, featureGroup, feature)
    
    
    projectLocationFeatureGroupFeaturesPath(project: string, location: string, featureGroup: string, feature: string): string;

Return a fully-qualified projectLocationFeatureGroupFeatures resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`featureGroup` |  `string`   
  
`feature` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationFeaturestoreEntityTypeFeaturesPath(project, location, featurestore, entityType, feature)
    
    
    projectLocationFeaturestoreEntityTypeFeaturesPath(project: string, location: string, featurestore: string, entityType: string, feature: string): string;

Return a fully-qualified projectLocationFeaturestoreEntityTypeFeatures resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`featurestore` |  `string`   
  
`entityType` |  `string`   
  
`feature` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationPublisherModelPath(project, location, publisher, model)
    
    
    projectLocationPublisherModelPath(project: string, location: string, publisher: string, model: string): string;

Return a fully-qualified projectLocationPublisherModel resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`publisher` |  `string`   
  
`model` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### publisherModelPath(publisher, model)
    
    
    publisherModelPath(publisher: string, model: string): string;

Return a fully-qualified publisherModel resource name string.

**Parameters**  
---  
**Name** | **Description**  
`publisher` |  `string`   
  
`model` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### ragCorpusPath(project, location, ragCorpus)
    
    
    ragCorpusPath(project: string, location: string, ragCorpus: string): string;

Return a fully-qualified ragCorpus resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`ragCorpus` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### ragDataSchemaPath(project, location, ragCorpus, ragDataSchema)
    
    
    ragDataSchemaPath(project: string, location: string, ragCorpus: string, ragDataSchema: string): string;

Return a fully-qualified ragDataSchema resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`ragCorpus` |  `string`   
  
`ragDataSchema` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### ragEngineConfigPath(project, location)
    
    
    ragEngineConfigPath(project: string, location: string): string;

Return a fully-qualified ragEngineConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### ragFilePath(project, location, ragCorpus, ragFile)
    
    
    ragFilePath(project: string, location: string, ragCorpus: string, ragFile: string): string;

Return a fully-qualified ragFile resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`ragCorpus` |  `string`   
  
`ragFile` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### ragMetadataPath(project, location, ragCorpus, ragFile, ragMetadata)
    
    
    ragMetadataPath(project: string, location: string, ragCorpus: string, ragFile: string, ragMetadata: string): string;

Return a fully-qualified ragMetadata resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`ragCorpus` |  `string`   
  
`ragFile` |  `string`   
  
`ragMetadata` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### reasoningEnginePath(project, location, reasoningEngine)
    
    
    reasoningEnginePath(project: string, location: string, reasoningEngine: string): string;

Return a fully-qualified reasoningEngine resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`reasoningEngine` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### reasoningEngineRuntimeRevisionPath(project, location, reasoningEngine, runtimeRevision)
    
    
    reasoningEngineRuntimeRevisionPath(project: string, location: string, reasoningEngine: string, runtimeRevision: string): string;

Return a fully-qualified reasoningEngineRuntimeRevision resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`reasoningEngine` |  `string`   
  
`runtimeRevision` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### restoreDatasetVersion(request, options)
    
    
    restoreDatasetVersion(request?: protos.google.cloud.aiplatform.v1beta1.IRestoreDatasetVersionRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.aiplatform.v1beta1.IDatasetVersion, protos.google.cloud.aiplatform.v1beta1.IRestoreDatasetVersionOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Restores a dataset version.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRestoreDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.irestoredatasetversionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.aiplatform.v1beta1.IDatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idatasetversion), [protos.google.cloud.aiplatform.v1beta1.IRestoreDatasetVersionOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.irestoredatasetversionoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the DatasetVersion resource.
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}/datasetVersions/{dataset_version}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callRestoreDatasetVersion() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.restoreDatasetVersion(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callRestoreDatasetVersion();
    
    

### restoreDatasetVersion(request, options, callback)
    
    
    restoreDatasetVersion(request: protos.google.cloud.aiplatform.v1beta1.IRestoreDatasetVersionRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IDatasetVersion, protos.google.cloud.aiplatform.v1beta1.IRestoreDatasetVersionOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRestoreDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.irestoredatasetversionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IDatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idatasetversion), [protos.google.cloud.aiplatform.v1beta1.IRestoreDatasetVersionOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.irestoredatasetversionoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### restoreDatasetVersion(request, callback)
    
    
    restoreDatasetVersion(request: protos.google.cloud.aiplatform.v1beta1.IRestoreDatasetVersionRequest, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IDatasetVersion, protos.google.cloud.aiplatform.v1beta1.IRestoreDatasetVersionOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRestoreDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.irestoredatasetversionrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IDatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idatasetversion), [protos.google.cloud.aiplatform.v1beta1.IRestoreDatasetVersionOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.irestoredatasetversionoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### savedQueryPath(project, location, dataset, savedQuery)
    
    
    savedQueryPath(project: string, location: string, dataset: string, savedQuery: string): string;

Return a fully-qualified savedQuery resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataset` |  `string`   
  
`savedQuery` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### schedulePath(project, location, schedule)
    
    
    schedulePath(project: string, location: string, schedule: string): string;

Return a fully-qualified schedule resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`schedule` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### searchDataItems(request, options)
    
    
    searchDataItems(request?: protos.google.cloud.aiplatform.v1beta1.ISearchDataItemsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IDataItemView[],
            protos.google.cloud.aiplatform.v1beta1.ISearchDataItemsRequest | null,
            protos.google.cloud.aiplatform.v1beta1.ISearchDataItemsResponse
        ]>;

Searches DataItems in a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isearchdataitemsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IDataItemView](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idataitemview)[], [protos.google.cloud.aiplatform.v1beta1.ISearchDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isearchdataitemsrequest) | null, [protos.google.cloud.aiplatform.v1beta1.ISearchDataItemsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isearchdataitemsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [DataItemView](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.dataitemview). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `searchDataItemsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### searchDataItems(request, options, callback)
    
    
    searchDataItems(request: protos.google.cloud.aiplatform.v1beta1.ISearchDataItemsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.ISearchDataItemsRequest, protos.google.cloud.aiplatform.v1beta1.ISearchDataItemsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.IDataItemView>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isearchdataitemsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.ISearchDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isearchdataitemsrequest), [protos.google.cloud.aiplatform.v1beta1.ISearchDataItemsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isearchdataitemsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.IDataItemView](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idataitemview)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchDataItems(request, callback)
    
    
    searchDataItems(request: protos.google.cloud.aiplatform.v1beta1.ISearchDataItemsRequest, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.ISearchDataItemsRequest, protos.google.cloud.aiplatform.v1beta1.ISearchDataItemsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.IDataItemView>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isearchdataitemsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.ISearchDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isearchdataitemsrequest), [protos.google.cloud.aiplatform.v1beta1.ISearchDataItemsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isearchdataitemsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.IDataItemView](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idataitemview)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchDataItemsAsync(request, options)
    
    
    searchDataItemsAsync(request?: protos.google.cloud.aiplatform.v1beta1.ISearchDataItemsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.aiplatform.v1beta1.IDataItemView>;

Equivalent to `searchDataItems`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isearchdataitemsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.aiplatform.v1beta1.IDataItemView](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idataitemview)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [DataItemView](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.dataitemview). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  A comma-separated list of data item fields to order by, sorted in
       *  ascending order. Use "desc" after a field name for descending.
       */
      // const orderByDataItem = 'abc123'
      /**
       *  Expression that allows ranking results based on annotation's property.
       */
      // const orderByAnnotation = {}
      /**
       *  Required. The resource name of the Dataset from which to search DataItems.
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}`
       */
      // const dataset = 'abc123'
      /**
       *  The resource name of a SavedQuery(annotation set in UI).
       *  Format:
       *  `projects/{project}/locations/{location}/datasets/{dataset}/savedQueries/{saved_query}`
       *  All of the search will be done in the context of this SavedQuery.
       */
      // const savedQuery = 'abc123'
      /**
       *  The resource name of a DataLabelingJob.
       *  Format:
       *  `projects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}`
       *  If this field is set, all of the search will be done in the context of
       *  this DataLabelingJob.
       */
      // const dataLabelingJob = 'abc123'
      /**
       *  An expression for filtering the DataItem that will be returned.
       *    * `data_item_id` - for = or !=.
       *    * `labeled` - for = or !=.
       *    * `has_annotation(ANNOTATION_SPEC_ID)` - true only for DataItem that
       *      have at least one annotation with annotation_spec_id =
       *      `ANNOTATION_SPEC_ID` in the context of SavedQuery or DataLabelingJob.
       *  For example:
       *  * `data_item=1`
       *  * `has_annotation(5)`
       */
      // const dataItemFilter = 'abc123'
      /**
       *  An expression for filtering the Annotations that will be returned per
       *  DataItem.
       *    * `annotation_spec_id` - for = or !=.
       */
      // const annotationsFilter = 'abc123'
      /**
       *  An expression that specifies what Annotations will be returned per
       *  DataItem. Annotations satisfied either of the conditions will be returned.
       *    * `annotation_spec_id` - for = or !=.
       *  Must specify `saved_query_id=` - saved query id that annotations should
       *  belong to.
       */
      // const annotationFilters = ['abc','def']
      /**
       *  Mask specifying which fields of
       *  DataItemView google.cloud.aiplatform.v1beta1.DataItemView  to read.
       */
      // const fieldMask = {}
      /**
       *  If set, only up to this many of Annotations will be returned per
       *  DataItemView. The maximum value is 1000. If not set, the maximum value will
       *  be used.
       */
      // const annotationsLimit = 1234
      /**
       *  Requested page size. Server may return fewer results than requested.
       *  Default and maximum page size is 100.
       */
      // const pageSize = 1234
      /**
       *  A comma-separated list of fields to order by, sorted in ascending order.
       *  Use "desc" after a field name for descending.
       */
      // const orderBy = 'abc123'
      /**
       *  A token identifying a page of results for the server to return
       *  Typically obtained via
       *  SearchDataItemsResponse.next_page_token google.cloud.aiplatform.v1beta1.SearchDataItemsResponse.next_page_token 
       *  of the previous
       *  DatasetService.SearchDataItems google.cloud.aiplatform.v1beta1.DatasetService.SearchDataItems 
       *  call.
       */
      // const pageToken = 'abc123'
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callSearchDataItems() {
        // Construct request
        const request = {
          dataset,
        };
    
        // Run request
        const iterable = aiplatformClient.searchDataItemsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callSearchDataItems();
    
    

### searchDataItemsStream(request, options)
    
    
    searchDataItemsStream(request?: protos.google.cloud.aiplatform.v1beta1.ISearchDataItemsRequest, options?: CallOptions): Transform;

Equivalent to `searchDataItems`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isearchdataitemsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [DataItemView](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.dataitemview) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `searchDataItemsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### sessionEventPath(project, location, reasoningEngine, session, event)
    
    
    sessionEventPath(project: string, location: string, reasoningEngine: string, session: string, event: string): string;

Return a fully-qualified sessionEvent resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`reasoningEngine` |  `string`   
  
`session` |  `string`   
  
`event` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### sessionPath(project, location, reasoningEngine, session)
    
    
    sessionPath(project: string, location: string, reasoningEngine: string, session: string): string;

Return a fully-qualified session resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`reasoningEngine` |  `string`   
  
`session` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### setIamPolicy(request, options, callback)
    
    
    setIamPolicy(request: IamProtos.google.iam.v1.SetIamPolicyRequest, options?: gax.CallOptions | Callback<IamProtos.google.iam.v1.Policy, IamProtos.google.iam.v1.SetIamPolicyRequest | null | undefined, {} | null | undefined>, callback?: Callback<IamProtos.google.iam.v1.Policy, IamProtos.google.iam.v1.SetIamPolicyRequest | null | undefined, {} | null | undefined>): Promise<[IamProtos.google.iam.v1.Policy]>;

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `IamProtos.google.iam.v1.SetIamPolicyRequest`   
The request object that will be sent.  
`options` |  `CallOptions | Callback<google.iam.v1.Policy, google.iam.v1.SetIamPolicyRequest | null | undefined, {} | null | undefined>`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/interfaces/CallOptions.html) for the details.  
`callback` |  `Callback<google.iam.v1.Policy, google.iam.v1.SetIamPolicyRequest | null | undefined, {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing .  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.Policy]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
  
### specialistPoolPath(project, location, specialistPool)
    
    
    specialistPoolPath(project: string, location: string, specialistPool: string): string;

Return a fully-qualified specialistPool resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`specialistPool` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### studyPath(project, location, study)
    
    
    studyPath(project: string, location: string, study: string): string;

Return a fully-qualified study resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`study` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### tensorboardExperimentPath(project, location, tensorboard, experiment)
    
    
    tensorboardExperimentPath(project: string, location: string, tensorboard: string, experiment: string): string;

Return a fully-qualified tensorboardExperiment resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`tensorboard` |  `string`   
  
`experiment` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### tensorboardPath(project, location, tensorboard)
    
    
    tensorboardPath(project: string, location: string, tensorboard: string): string;

Return a fully-qualified tensorboard resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`tensorboard` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### tensorboardRunPath(project, location, tensorboard, experiment, run)
    
    
    tensorboardRunPath(project: string, location: string, tensorboard: string, experiment: string, run: string): string;

Return a fully-qualified tensorboardRun resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`tensorboard` |  `string`   
  
`experiment` |  `string`   
  
`run` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### tensorboardTimeSeriesPath(project, location, tensorboard, experiment, run, timeSeries)
    
    
    tensorboardTimeSeriesPath(project: string, location: string, tensorboard: string, experiment: string, run: string, timeSeries: string): string;

Return a fully-qualified tensorboardTimeSeries resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`tensorboard` |  `string`   
  
`experiment` |  `string`   
  
`run` |  `string`   
  
`timeSeries` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### testIamPermissions(request, options, callback)
    
    
    testIamPermissions(request: IamProtos.google.iam.v1.TestIamPermissionsRequest, options?: gax.CallOptions | Callback<IamProtos.google.iam.v1.TestIamPermissionsResponse, IamProtos.google.iam.v1.TestIamPermissionsRequest | null | undefined, {} | null | undefined>, callback?: Callback<IamProtos.google.iam.v1.TestIamPermissionsResponse, IamProtos.google.iam.v1.TestIamPermissionsRequest | null | undefined, {} | null | undefined>): Promise<[IamProtos.google.iam.v1.TestIamPermissionsResponse]>;

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `IamProtos.google.iam.v1.TestIamPermissionsRequest`   
The request object that will be sent.  
`options` |  `CallOptions | Callback<google.iam.v1.TestIamPermissionsResponse, google.iam.v1.TestIamPermissionsRequest | null | undefined, {} | null | undefined>`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/interfaces/CallOptions.html) for the details.  
`callback` |  `Callback<google.iam.v1.TestIamPermissionsResponse, google.iam.v1.TestIamPermissionsRequest | null | undefined, {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing .  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.TestIamPermissionsResponse]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
  
### trainingPipelinePath(project, location, trainingPipeline)
    
    
    trainingPipelinePath(project: string, location: string, trainingPipeline: string): string;

Return a fully-qualified trainingPipeline resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`trainingPipeline` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### trialPath(project, location, study, trial)
    
    
    trialPath(project: string, location: string, study: string, trial: string): string;

Return a fully-qualified trial resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`study` |  `string`   
  
`trial` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### tuningJobPath(project, location, tuningJob)
    
    
    tuningJobPath(project: string, location: string, tuningJob: string): string;

Return a fully-qualified tuningJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`tuningJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### updateDataset(request, options)
    
    
    updateDataset(request?: protos.google.cloud.aiplatform.v1beta1.IUpdateDatasetRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IDataset,
            protos.google.cloud.aiplatform.v1beta1.IUpdateDatasetRequest | undefined,
            {} | undefined
        ]>;

Updates a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatedatasetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idataset), [protos.google.cloud.aiplatform.v1beta1.IUpdateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatedatasetrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Dataset](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.dataset). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Dataset which replaces the resource on the server.
       */
      // const dataset = {}
      /**
       *  Required. The update mask applies to the resource.
       *  For the `FieldMask` definition, see
       *  google.protobuf.FieldMask google.protobuf.FieldMask. Updatable fields:
       *    * `display_name`
       *    * `description`
       *    * `labels`
       */
      // const updateMask = {}
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callUpdateDataset() {
        // Construct request
        const request = {
          dataset,
          updateMask,
        };
    
        // Run request
        const response = await aiplatformClient.updateDataset(request);
        console.log(response);
      }
    
      callUpdateDataset();
    
    

### updateDataset(request, options, callback)
    
    
    updateDataset(request: protos.google.cloud.aiplatform.v1beta1.IUpdateDatasetRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IDataset, protos.google.cloud.aiplatform.v1beta1.IUpdateDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatedatasetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idataset), [protos.google.cloud.aiplatform.v1beta1.IUpdateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatedatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataset(request, callback)
    
    
    updateDataset(request: protos.google.cloud.aiplatform.v1beta1.IUpdateDatasetRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IDataset, protos.google.cloud.aiplatform.v1beta1.IUpdateDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatedatasetrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idataset), [protos.google.cloud.aiplatform.v1beta1.IUpdateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatedatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDatasetVersion(request, options)
    
    
    updateDatasetVersion(request?: protos.google.cloud.aiplatform.v1beta1.IUpdateDatasetVersionRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IDatasetVersion,
            (protos.google.cloud.aiplatform.v1beta1.IUpdateDatasetVersionRequest | undefined),
            {} | undefined
        ]>;

Updates a DatasetVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatedatasetversionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IDatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idatasetversion), ([protos.google.cloud.aiplatform.v1beta1.IUpdateDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatedatasetversionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [DatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.datasetversion). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The DatasetVersion which replaces the resource on the server.
       */
      // const datasetVersion = {}
      /**
       *  Required. The update mask applies to the resource.
       *  For the `FieldMask` definition, see
       *  google.protobuf.FieldMask google.protobuf.FieldMask. Updatable fields:
       *    * `display_name`
       */
      // const updateMask = {}
    
      // Imports the Aiplatform library
      const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callUpdateDatasetVersion() {
        // Construct request
        const request = {
          datasetVersion,
          updateMask,
        };
    
        // Run request
        const response = await aiplatformClient.updateDatasetVersion(request);
        console.log(response);
      }
    
      callUpdateDatasetVersion();
    
    

### updateDatasetVersion(request, options, callback)
    
    
    updateDatasetVersion(request: protos.google.cloud.aiplatform.v1beta1.IUpdateDatasetVersionRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IDatasetVersion, protos.google.cloud.aiplatform.v1beta1.IUpdateDatasetVersionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatedatasetversionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IDatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idatasetversion), [protos.google.cloud.aiplatform.v1beta1.IUpdateDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatedatasetversionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDatasetVersion(request, callback)
    
    
    updateDatasetVersion(request: protos.google.cloud.aiplatform.v1beta1.IUpdateDatasetVersionRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IDatasetVersion, protos.google.cloud.aiplatform.v1beta1.IUpdateDatasetVersionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatedatasetversionrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IDatasetVersion](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.idatasetversion), [protos.google.cloud.aiplatform.v1beta1.IUpdateDatasetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatedatasetversionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
