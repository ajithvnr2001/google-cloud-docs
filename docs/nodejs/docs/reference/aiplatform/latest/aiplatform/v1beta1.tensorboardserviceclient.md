---
url: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/v1beta1.tensorboardserviceclient
title: Class v1beta1.TensorboardServiceClient (7.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:14:33.744911+00:00
---

# Class v1beta1.TensorboardServiceClient (7.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/v1beta1.tensorboardserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.TensorboardServiceClient (7.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.4.1 (latest)  7.3.0  6.10.0  6.9.0  6.8.1  6.6.0  6.4.0  6.3.0  6.2.0  6.1.0  6.0.0  5.14.0  5.13.0  3.15.0  3.13.0  3.11.0  3.10.1  3.9.0  3.7.0  3.6.0  3.4.0  3.3.0  3.0.0  2.12.0  2.11.0  2.10.0  2.7.0  2.6.1  2.5.0  2.3.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0  1.11.0  1.7.2 

TensorboardService v1beta1

## Package

[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of TensorboardServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new TensorboardServiceClient({fallback: true}, gax); ```  
  
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

### tensorboardServiceStub
    
    
    tensorboardServiceStub?: Promise<{
            [name: string]: Function;
        }>;

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
  
### batchCreateTensorboardRuns(request, options)
    
    
    batchCreateTensorboardRuns(request?: protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardRunsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardRunsResponse,
            (protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardRunsRequest | undefined),
            {} | undefined
        ]>;

Batch create TensorboardRuns.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateTensorboardRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatetensorboardrunsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatetensorboardrunsresponse), ([protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatetensorboardrunsrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [BatchCreateTensorboardRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.batchcreatetensorboardrunsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the TensorboardExperiment to create the
       *  TensorboardRuns in. Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`
       *  The parent field in the CreateTensorboardRunRequest messages must match
       *  this field.
       */
      // const parent = 'abc123'
      /**
       *  Required. The request message specifying the TensorboardRuns to create.
       *  A maximum of 1000 TensorboardRuns can be created in a batch.
       */
      // const requests = [1,2,3,4]
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callBatchCreateTensorboardRuns() {
        // Construct request
        const request = {
          parent,
          requests,
        };
    
        // Run request
        const response = await aiplatformClient.batchCreateTensorboardRuns(request);
        console.log(response);
      }
    
      callBatchCreateTensorboardRuns();
    
    

### batchCreateTensorboardRuns(request, options, callback)
    
    
    batchCreateTensorboardRuns(request: protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardRunsRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardRunsResponse, protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardRunsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateTensorboardRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatetensorboardrunsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatetensorboardrunsresponse), [protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatetensorboardrunsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateTensorboardRuns(request, callback)
    
    
    batchCreateTensorboardRuns(request: protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardRunsRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardRunsResponse, protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardRunsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateTensorboardRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatetensorboardrunsrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatetensorboardrunsresponse), [protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatetensorboardrunsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateTensorboardTimeSeries(request, options)
    
    
    batchCreateTensorboardTimeSeries(request?: protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardTimeSeriesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardTimeSeriesResponse,
            (protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardTimeSeriesRequest | undefined),
            {} | undefined
        ]>;

Batch create TensorboardTimeSeries that belong to a TensorboardExperiment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatetensorboardtimeseriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardTimeSeriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatetensorboardtimeseriesresponse), ([protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatetensorboardtimeseriesrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [BatchCreateTensorboardTimeSeriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.batchcreatetensorboardtimeseriesresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the TensorboardExperiment to create the
       *  TensorboardTimeSeries in.
       *  Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`
       *  The TensorboardRuns referenced by the parent fields in the
       *  CreateTensorboardTimeSeriesRequest messages must be sub resources of this
       *  TensorboardExperiment.
       */
      // const parent = 'abc123'
      /**
       *  Required. The request message specifying the TensorboardTimeSeries to
       *  create. A maximum of 1000 TensorboardTimeSeries can be created in a batch.
       */
      // const requests = [1,2,3,4]
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callBatchCreateTensorboardTimeSeries() {
        // Construct request
        const request = {
          parent,
          requests,
        };
    
        // Run request
        const response = await aiplatformClient.batchCreateTensorboardTimeSeries(request);
        console.log(response);
      }
    
      callBatchCreateTensorboardTimeSeries();
    
    

### batchCreateTensorboardTimeSeries(request, options, callback)
    
    
    batchCreateTensorboardTimeSeries(request: protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardTimeSeriesRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardTimeSeriesResponse, protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardTimeSeriesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatetensorboardtimeseriesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardTimeSeriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatetensorboardtimeseriesresponse), [protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatetensorboardtimeseriesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateTensorboardTimeSeries(request, callback)
    
    
    batchCreateTensorboardTimeSeries(request: protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardTimeSeriesRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardTimeSeriesResponse, protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardTimeSeriesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatetensorboardtimeseriesrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardTimeSeriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatetensorboardtimeseriesresponse), [protos.google.cloud.aiplatform.v1beta1.IBatchCreateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatetensorboardtimeseriesrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### batchReadTensorboardTimeSeriesData(request, options)
    
    
    batchReadTensorboardTimeSeriesData(request?: protos.google.cloud.aiplatform.v1beta1.IBatchReadTensorboardTimeSeriesDataRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IBatchReadTensorboardTimeSeriesDataResponse,
            (protos.google.cloud.aiplatform.v1beta1.IBatchReadTensorboardTimeSeriesDataRequest | undefined),
            {} | undefined
        ]>;

Reads multiple TensorboardTimeSeries' data. The data point number limit is 1000 for scalars, 100 for tensors and blob references. If the number of data points stored is less than the limit, all data is returned. Otherwise, the number limit of data points is randomly selected from this time series and returned.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchReadTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchreadtensorboardtimeseriesdatarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IBatchReadTensorboardTimeSeriesDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchreadtensorboardtimeseriesdataresponse), ([protos.google.cloud.aiplatform.v1beta1.IBatchReadTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchreadtensorboardtimeseriesdatarequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [BatchReadTensorboardTimeSeriesDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.batchreadtensorboardtimeseriesdataresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Tensorboard containing
       *  TensorboardTimeSeries to read data from. Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}`.
       *  The TensorboardTimeSeries referenced by
       *  time_series google.cloud.aiplatform.v1beta1.BatchReadTensorboardTimeSeriesDataRequest.time_series 
       *  must be sub resources of this Tensorboard.
       */
      // const tensorboard = 'abc123'
      /**
       *  Required. The resource names of the TensorboardTimeSeries to read data
       *  from. Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`
       */
      // const timeSeries = ['abc','def']
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callBatchReadTensorboardTimeSeriesData() {
        // Construct request
        const request = {
          tensorboard,
          timeSeries,
        };
    
        // Run request
        const response = await aiplatformClient.batchReadTensorboardTimeSeriesData(request);
        console.log(response);
      }
    
      callBatchReadTensorboardTimeSeriesData();
    
    

### batchReadTensorboardTimeSeriesData(request, options, callback)
    
    
    batchReadTensorboardTimeSeriesData(request: protos.google.cloud.aiplatform.v1beta1.IBatchReadTensorboardTimeSeriesDataRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IBatchReadTensorboardTimeSeriesDataResponse, protos.google.cloud.aiplatform.v1beta1.IBatchReadTensorboardTimeSeriesDataRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchReadTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchreadtensorboardtimeseriesdatarequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IBatchReadTensorboardTimeSeriesDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchreadtensorboardtimeseriesdataresponse), [protos.google.cloud.aiplatform.v1beta1.IBatchReadTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchreadtensorboardtimeseriesdatarequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchReadTensorboardTimeSeriesData(request, callback)
    
    
    batchReadTensorboardTimeSeriesData(request: protos.google.cloud.aiplatform.v1beta1.IBatchReadTensorboardTimeSeriesDataRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IBatchReadTensorboardTimeSeriesDataResponse, protos.google.cloud.aiplatform.v1beta1.IBatchReadTensorboardTimeSeriesDataRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchReadTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchreadtensorboardtimeseriesdatarequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IBatchReadTensorboardTimeSeriesDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchreadtensorboardtimeseriesdataresponse), [protos.google.cloud.aiplatform.v1beta1.IBatchReadTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchreadtensorboardtimeseriesdatarequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
    

### checkCreateTensorboardProgress(name)
    
    
    checkCreateTensorboardProgress(name: string): Promise<LROperation<protos.google.cloud.aiplatform.v1beta1.Tensorboard, protos.google.cloud.aiplatform.v1beta1.CreateTensorboardOperationMetadata>>;

Check the status of the long running operation returned by `createTensorboard()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.aiplatform.v1beta1.Tensorboard](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.tensorboard), [protos.google.cloud.aiplatform.v1beta1.CreateTensorboardOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.createtensorboardoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Location to create the Tensorboard in.
       *  Format: `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The Tensorboard to create.
       */
      // const tensorboard = {}
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callCreateTensorboard() {
        // Construct request
        const request = {
          parent,
          tensorboard,
        };
    
        // Run request
        const [operation] = await aiplatformClient.createTensorboard(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateTensorboard();
    
    

### checkDeleteTensorboardExperimentProgress(name)
    
    
    checkDeleteTensorboardExperimentProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata>>;

Check the status of the long running operation returned by `deleteTensorboardExperiment()`.

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
       *  Required. The name of the TensorboardExperiment to be deleted.
       *  Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteTensorboardExperiment() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.deleteTensorboardExperiment(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteTensorboardExperiment();
    
    

### checkDeleteTensorboardProgress(name)
    
    
    checkDeleteTensorboardProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata>>;

Check the status of the long running operation returned by `deleteTensorboard()`.

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
       *  Required. The name of the Tensorboard to be deleted.
       *  Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteTensorboard() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.deleteTensorboard(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteTensorboard();
    
    

### checkDeleteTensorboardRunProgress(name)
    
    
    checkDeleteTensorboardRunProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata>>;

Check the status of the long running operation returned by `deleteTensorboardRun()`.

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
       *  Required. The name of the TensorboardRun to be deleted.
       *  Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteTensorboardRun() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.deleteTensorboardRun(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteTensorboardRun();
    
    

### checkDeleteTensorboardTimeSeriesProgress(name)
    
    
    checkDeleteTensorboardTimeSeriesProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata>>;

Check the status of the long running operation returned by `deleteTensorboardTimeSeries()`.

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
       *  Required. The name of the TensorboardTimeSeries to be deleted.
       *  Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteTensorboardTimeSeries() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.deleteTensorboardTimeSeries(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteTensorboardTimeSeries();
    
    

### checkUpdateTensorboardProgress(name)
    
    
    checkUpdateTensorboardProgress(name: string): Promise<LROperation<protos.google.cloud.aiplatform.v1beta1.Tensorboard, protos.google.cloud.aiplatform.v1beta1.UpdateTensorboardOperationMetadata>>;

Check the status of the long running operation returned by `updateTensorboard()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.aiplatform.v1beta1.Tensorboard](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.tensorboard), [protos.google.cloud.aiplatform.v1beta1.UpdateTensorboardOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.updatetensorboardoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Field mask is used to specify the fields to be overwritten in the
       *  Tensorboard resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field is overwritten if it's in the mask. If the
       *  user does not provide a mask then all fields are overwritten if new
       *  values are specified.
       */
      // const updateMask = {}
      /**
       *  Required. The Tensorboard's `name` field is used to identify the
       *  Tensorboard to be updated. Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}`
       */
      // const tensorboard = {}
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callUpdateTensorboard() {
        // Construct request
        const request = {
          updateMask,
          tensorboard,
        };
    
        // Run request
        const [operation] = await aiplatformClient.updateTensorboard(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateTensorboard();
    
    

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
  
### createTensorboard(request, options)
    
    
    createTensorboard(request?: protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.aiplatform.v1beta1.ITensorboard, protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a Tensorboard.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTensorboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.aiplatform.v1beta1.ITensorboard](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboard), [protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Location to create the Tensorboard in.
       *  Format: `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The Tensorboard to create.
       */
      // const tensorboard = {}
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callCreateTensorboard() {
        // Construct request
        const request = {
          parent,
          tensorboard,
        };
    
        // Run request
        const [operation] = await aiplatformClient.createTensorboard(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateTensorboard();
    
    

### createTensorboard(request, options, callback)
    
    
    createTensorboard(request: protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.ITensorboard, protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTensorboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.ITensorboard](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboard), [protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTensorboard(request, callback)
    
    
    createTensorboard(request: protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardRequest, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.ITensorboard, protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTensorboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.ITensorboard](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboard), [protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTensorboardExperiment(request, options)
    
    
    createTensorboardExperiment(request?: protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardExperimentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment,
            (protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardExperimentRequest | undefined),
            {} | undefined
        ]>;

Creates a TensorboardExperiment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTensorboardExperimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardexperimentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardexperiment), ([protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardExperimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardexperimentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [TensorboardExperiment](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.tensorboardexperiment). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Tensorboard to create the
       *  TensorboardExperiment in. Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}`
       */
      // const parent = 'abc123'
      /**
       *  The TensorboardExperiment to create.
       */
      // const tensorboardExperiment = {}
      /**
       *  Required. The ID to use for the Tensorboard experiment, which becomes the
       *  final component of the Tensorboard experiment's resource name.
       *  This value should be 1-128 characters, and valid characters
       *  are `/[a-z][0-9]-/`.
       */
      // const tensorboardExperimentId = 'abc123'
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callCreateTensorboardExperiment() {
        // Construct request
        const request = {
          parent,
          tensorboardExperimentId,
        };
    
        // Run request
        const response = await aiplatformClient.createTensorboardExperiment(request);
        console.log(response);
      }
    
      callCreateTensorboardExperiment();
    
    

### createTensorboardExperiment(request, options, callback)
    
    
    createTensorboardExperiment(request: protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardExperimentRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment, protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardExperimentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTensorboardExperimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardexperimentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardexperiment), [protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardExperimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardexperimentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTensorboardExperiment(request, callback)
    
    
    createTensorboardExperiment(request: protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardExperimentRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment, protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardExperimentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTensorboardExperimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardexperimentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardexperiment), [protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardExperimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardexperimentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTensorboardRun(request, options)
    
    
    createTensorboardRun(request?: protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardRunRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ITensorboardRun,
            (protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardRunRequest | undefined),
            {} | undefined
        ]>;

Creates a TensorboardRun.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTensorboardRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardrunrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ITensorboardRun](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardrun), ([protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardrunrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [TensorboardRun](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.tensorboardrun). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the TensorboardExperiment to create the
       *  TensorboardRun in. Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The TensorboardRun to create.
       */
      // const tensorboardRun = {}
      /**
       *  Required. The ID to use for the Tensorboard run, which becomes the final
       *  component of the Tensorboard run's resource name.
       *  This value should be 1-128 characters, and valid characters
       *  are `/[a-z][0-9]-/`.
       */
      // const tensorboardRunId = 'abc123'
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callCreateTensorboardRun() {
        // Construct request
        const request = {
          parent,
          tensorboardRun,
          tensorboardRunId,
        };
    
        // Run request
        const response = await aiplatformClient.createTensorboardRun(request);
        console.log(response);
      }
    
      callCreateTensorboardRun();
    
    

### createTensorboardRun(request, options, callback)
    
    
    createTensorboardRun(request: protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardRunRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITensorboardRun, protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardRunRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTensorboardRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardrunrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITensorboardRun](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardrun), [protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardrunrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTensorboardRun(request, callback)
    
    
    createTensorboardRun(request: protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardRunRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITensorboardRun, protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardRunRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTensorboardRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardrunrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITensorboardRun](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardrun), [protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardrunrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTensorboardTimeSeries(request, options)
    
    
    createTensorboardTimeSeries(request?: protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardTimeSeriesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries,
            (protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardTimeSeriesRequest | undefined),
            {} | undefined
        ]>;

Creates a TensorboardTimeSeries.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardtimeseriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardtimeseries), ([protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardtimeseriesrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the TensorboardRun to create the
       *  TensorboardTimeSeries in.
       *  Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. The user specified unique ID to use for the
       *  TensorboardTimeSeries, which becomes the final component of the
       *  TensorboardTimeSeries's resource name. This value should match
       *  "[a-z0-9][a-z0-9-]{0, 127}"
       */
      // const tensorboardTimeSeriesId = 'abc123'
      /**
       *  Required. The TensorboardTimeSeries to create.
       */
      // const tensorboardTimeSeries = {}
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callCreateTensorboardTimeSeries() {
        // Construct request
        const request = {
          parent,
          tensorboardTimeSeries,
        };
    
        // Run request
        const response = await aiplatformClient.createTensorboardTimeSeries(request);
        console.log(response);
      }
    
      callCreateTensorboardTimeSeries();
    
    

### createTensorboardTimeSeries(request, options, callback)
    
    
    createTensorboardTimeSeries(request: protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardTimeSeriesRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries, protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardTimeSeriesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardtimeseriesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardtimeseries), [protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardtimeseriesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTensorboardTimeSeries(request, callback)
    
    
    createTensorboardTimeSeries(request: protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardTimeSeriesRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries, protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardTimeSeriesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardtimeseriesrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardtimeseries), [protos.google.cloud.aiplatform.v1beta1.ICreateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetensorboardtimeseriesrequest) | null | undefined, {} | null | undefined>`   
  
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
    

### deleteTensorboard(request, options)
    
    
    deleteTensorboard(request?: protos.google.cloud.aiplatform.v1beta1.IDeleteTensorboardRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a Tensorboard.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTensorboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletetensorboardrequest)`   
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
       *  Required. The name of the Tensorboard to be deleted.
       *  Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteTensorboard() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.deleteTensorboard(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteTensorboard();
    
    

### deleteTensorboard(request, options, callback)
    
    
    deleteTensorboard(request: protos.google.cloud.aiplatform.v1beta1.IDeleteTensorboardRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTensorboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletetensorboardrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTensorboard(request, callback)
    
    
    deleteTensorboard(request: protos.google.cloud.aiplatform.v1beta1.IDeleteTensorboardRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTensorboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletetensorboardrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTensorboardExperiment(request, options)
    
    
    deleteTensorboardExperiment(request?: protos.google.cloud.aiplatform.v1beta1.IDeleteTensorboardExperimentRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a TensorboardExperiment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTensorboardExperimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletetensorboardexperimentrequest)`   
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
       *  Required. The name of the TensorboardExperiment to be deleted.
       *  Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteTensorboardExperiment() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.deleteTensorboardExperiment(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteTensorboardExperiment();
    
    

### deleteTensorboardExperiment(request, options, callback)
    
    
    deleteTensorboardExperiment(request: protos.google.cloud.aiplatform.v1beta1.IDeleteTensorboardExperimentRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTensorboardExperimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletetensorboardexperimentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTensorboardExperiment(request, callback)
    
    
    deleteTensorboardExperiment(request: protos.google.cloud.aiplatform.v1beta1.IDeleteTensorboardExperimentRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTensorboardExperimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletetensorboardexperimentrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTensorboardRun(request, options)
    
    
    deleteTensorboardRun(request?: protos.google.cloud.aiplatform.v1beta1.IDeleteTensorboardRunRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a TensorboardRun.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTensorboardRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletetensorboardrunrequest)`   
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
       *  Required. The name of the TensorboardRun to be deleted.
       *  Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteTensorboardRun() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.deleteTensorboardRun(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteTensorboardRun();
    
    

### deleteTensorboardRun(request, options, callback)
    
    
    deleteTensorboardRun(request: protos.google.cloud.aiplatform.v1beta1.IDeleteTensorboardRunRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTensorboardRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletetensorboardrunrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTensorboardRun(request, callback)
    
    
    deleteTensorboardRun(request: protos.google.cloud.aiplatform.v1beta1.IDeleteTensorboardRunRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTensorboardRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletetensorboardrunrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTensorboardTimeSeries(request, options)
    
    
    deleteTensorboardTimeSeries(request?: protos.google.cloud.aiplatform.v1beta1.IDeleteTensorboardTimeSeriesRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a TensorboardTimeSeries.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletetensorboardtimeseriesrequest)`   
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
       *  Required. The name of the TensorboardTimeSeries to be deleted.
       *  Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteTensorboardTimeSeries() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.deleteTensorboardTimeSeries(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteTensorboardTimeSeries();
    
    

### deleteTensorboardTimeSeries(request, options, callback)
    
    
    deleteTensorboardTimeSeries(request: protos.google.cloud.aiplatform.v1beta1.IDeleteTensorboardTimeSeriesRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletetensorboardtimeseriesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTensorboardTimeSeries(request, callback)
    
    
    deleteTensorboardTimeSeries(request: protos.google.cloud.aiplatform.v1beta1.IDeleteTensorboardTimeSeriesRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletetensorboardtimeseriesrequest)`   
  
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
  
### exportTensorboardTimeSeriesData(request, options)
    
    
    exportTensorboardTimeSeriesData(request?: protos.google.cloud.aiplatform.v1beta1.IExportTensorboardTimeSeriesDataRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ITimeSeriesDataPoint[],
            protos.google.cloud.aiplatform.v1beta1.IExportTensorboardTimeSeriesDataRequest | null,
            protos.google.cloud.aiplatform.v1beta1.IExportTensorboardTimeSeriesDataResponse
        ]>;

Exports a TensorboardTimeSeries' data. Data is returned in paginated responses.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexporttensorboardtimeseriesdatarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ITimeSeriesDataPoint](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itimeseriesdatapoint)[], [protos.google.cloud.aiplatform.v1beta1.IExportTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexporttensorboardtimeseriesdatarequest) | null, [protos.google.cloud.aiplatform.v1beta1.IExportTensorboardTimeSeriesDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexporttensorboardtimeseriesdataresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [TimeSeriesDataPoint](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.timeseriesdatapoint). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `exportTensorboardTimeSeriesDataAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### exportTensorboardTimeSeriesData(request, options, callback)
    
    
    exportTensorboardTimeSeriesData(request: protos.google.cloud.aiplatform.v1beta1.IExportTensorboardTimeSeriesDataRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IExportTensorboardTimeSeriesDataRequest, protos.google.cloud.aiplatform.v1beta1.IExportTensorboardTimeSeriesDataResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.ITimeSeriesDataPoint>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexporttensorboardtimeseriesdatarequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IExportTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexporttensorboardtimeseriesdatarequest), [protos.google.cloud.aiplatform.v1beta1.IExportTensorboardTimeSeriesDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexporttensorboardtimeseriesdataresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.ITimeSeriesDataPoint](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itimeseriesdatapoint)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportTensorboardTimeSeriesData(request, callback)
    
    
    exportTensorboardTimeSeriesData(request: protos.google.cloud.aiplatform.v1beta1.IExportTensorboardTimeSeriesDataRequest, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IExportTensorboardTimeSeriesDataRequest, protos.google.cloud.aiplatform.v1beta1.IExportTensorboardTimeSeriesDataResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.ITimeSeriesDataPoint>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexporttensorboardtimeseriesdatarequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IExportTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexporttensorboardtimeseriesdatarequest), [protos.google.cloud.aiplatform.v1beta1.IExportTensorboardTimeSeriesDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexporttensorboardtimeseriesdataresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.ITimeSeriesDataPoint](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itimeseriesdatapoint)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportTensorboardTimeSeriesDataAsync(request, options)
    
    
    exportTensorboardTimeSeriesDataAsync(request?: protos.google.cloud.aiplatform.v1beta1.IExportTensorboardTimeSeriesDataRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.aiplatform.v1beta1.ITimeSeriesDataPoint>;

Equivalent to `exportTensorboardTimeSeriesData`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexporttensorboardtimeseriesdatarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.aiplatform.v1beta1.ITimeSeriesDataPoint](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itimeseriesdatapoint)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [TimeSeriesDataPoint](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.timeseriesdatapoint). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the TensorboardTimeSeries to export data
       *  from. Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`
       */
      // const tensorboardTimeSeries = 'abc123'
      /**
       *  Exports the TensorboardTimeSeries' data that match the filter expression.
       */
      // const filter = 'abc123'
      /**
       *  The maximum number of data points to return per page.
       *  The default page_size is 1000. Values must be between 1 and 10000.
       *  Values above 10000 are coerced to 10000.
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous
       *  ExportTensorboardTimeSeriesData google.cloud.aiplatform.v1beta1.TensorboardService.ExportTensorboardTimeSeriesData 
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  ExportTensorboardTimeSeriesData google.cloud.aiplatform.v1beta1.TensorboardService.ExportTensorboardTimeSeriesData 
       *  must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Field to use to sort the TensorboardTimeSeries' data.
       *  By default, TensorboardTimeSeries' data is returned in a pseudo random
       *  order.
       */
      // const orderBy = 'abc123'
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callExportTensorboardTimeSeriesData() {
        // Construct request
        const request = {
          tensorboardTimeSeries,
        };
    
        // Run request
        const iterable = aiplatformClient.exportTensorboardTimeSeriesDataAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callExportTensorboardTimeSeriesData();
    
    

### exportTensorboardTimeSeriesDataStream(request, options)
    
    
    exportTensorboardTimeSeriesDataStream(request?: protos.google.cloud.aiplatform.v1beta1.IExportTensorboardTimeSeriesDataRequest, options?: CallOptions): Transform;

Equivalent to `exportTensorboardTimeSeriesData`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iexporttensorboardtimeseriesdatarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [TimeSeriesDataPoint](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.timeseriesdatapoint) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `exportTensorboardTimeSeriesDataAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### getTensorboard(request, options)
    
    
    getTensorboard(request?: protos.google.cloud.aiplatform.v1beta1.IGetTensorboardRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ITensorboard,
            protos.google.cloud.aiplatform.v1beta1.IGetTensorboardRequest | undefined,
            {} | undefined
        ]>;

Gets a Tensorboard.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTensorboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ITensorboard](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboard), [protos.google.cloud.aiplatform.v1beta1.IGetTensorboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Tensorboard](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.tensorboard). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Tensorboard resource.
       *  Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callGetTensorboard() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await aiplatformClient.getTensorboard(request);
        console.log(response);
      }
    
      callGetTensorboard();
    
    

### getTensorboard(request, options, callback)
    
    
    getTensorboard(request: protos.google.cloud.aiplatform.v1beta1.IGetTensorboardRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITensorboard, protos.google.cloud.aiplatform.v1beta1.IGetTensorboardRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTensorboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITensorboard](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboard), [protos.google.cloud.aiplatform.v1beta1.IGetTensorboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTensorboard(request, callback)
    
    
    getTensorboard(request: protos.google.cloud.aiplatform.v1beta1.IGetTensorboardRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITensorboard, protos.google.cloud.aiplatform.v1beta1.IGetTensorboardRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTensorboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITensorboard](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboard), [protos.google.cloud.aiplatform.v1beta1.IGetTensorboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTensorboardExperiment(request, options)
    
    
    getTensorboardExperiment(request?: protos.google.cloud.aiplatform.v1beta1.IGetTensorboardExperimentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment,
            (protos.google.cloud.aiplatform.v1beta1.IGetTensorboardExperimentRequest | undefined),
            {} | undefined
        ]>;

Gets a TensorboardExperiment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTensorboardExperimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardexperimentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardexperiment), ([protos.google.cloud.aiplatform.v1beta1.IGetTensorboardExperimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardexperimentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [TensorboardExperiment](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.tensorboardexperiment). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the TensorboardExperiment resource.
       *  Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callGetTensorboardExperiment() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await aiplatformClient.getTensorboardExperiment(request);
        console.log(response);
      }
    
      callGetTensorboardExperiment();
    
    

### getTensorboardExperiment(request, options, callback)
    
    
    getTensorboardExperiment(request: protos.google.cloud.aiplatform.v1beta1.IGetTensorboardExperimentRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment, protos.google.cloud.aiplatform.v1beta1.IGetTensorboardExperimentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTensorboardExperimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardexperimentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardexperiment), [protos.google.cloud.aiplatform.v1beta1.IGetTensorboardExperimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardexperimentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTensorboardExperiment(request, callback)
    
    
    getTensorboardExperiment(request: protos.google.cloud.aiplatform.v1beta1.IGetTensorboardExperimentRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment, protos.google.cloud.aiplatform.v1beta1.IGetTensorboardExperimentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTensorboardExperimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardexperimentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardexperiment), [protos.google.cloud.aiplatform.v1beta1.IGetTensorboardExperimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardexperimentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTensorboardRun(request, options)
    
    
    getTensorboardRun(request?: protos.google.cloud.aiplatform.v1beta1.IGetTensorboardRunRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ITensorboardRun,
            (protos.google.cloud.aiplatform.v1beta1.IGetTensorboardRunRequest | undefined),
            {} | undefined
        ]>;

Gets a TensorboardRun.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTensorboardRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardrunrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ITensorboardRun](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardrun), ([protos.google.cloud.aiplatform.v1beta1.IGetTensorboardRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardrunrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [TensorboardRun](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.tensorboardrun). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the TensorboardRun resource.
       *  Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callGetTensorboardRun() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await aiplatformClient.getTensorboardRun(request);
        console.log(response);
      }
    
      callGetTensorboardRun();
    
    

### getTensorboardRun(request, options, callback)
    
    
    getTensorboardRun(request: protos.google.cloud.aiplatform.v1beta1.IGetTensorboardRunRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITensorboardRun, protos.google.cloud.aiplatform.v1beta1.IGetTensorboardRunRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTensorboardRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardrunrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITensorboardRun](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardrun), [protos.google.cloud.aiplatform.v1beta1.IGetTensorboardRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardrunrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTensorboardRun(request, callback)
    
    
    getTensorboardRun(request: protos.google.cloud.aiplatform.v1beta1.IGetTensorboardRunRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITensorboardRun, protos.google.cloud.aiplatform.v1beta1.IGetTensorboardRunRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTensorboardRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardrunrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITensorboardRun](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardrun), [protos.google.cloud.aiplatform.v1beta1.IGetTensorboardRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardrunrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTensorboardTimeSeries(request, options)
    
    
    getTensorboardTimeSeries(request?: protos.google.cloud.aiplatform.v1beta1.IGetTensorboardTimeSeriesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries,
            (protos.google.cloud.aiplatform.v1beta1.IGetTensorboardTimeSeriesRequest | undefined),
            {} | undefined
        ]>;

Gets a TensorboardTimeSeries.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardtimeseriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardtimeseries), ([protos.google.cloud.aiplatform.v1beta1.IGetTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardtimeseriesrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the TensorboardTimeSeries resource.
       *  Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callGetTensorboardTimeSeries() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await aiplatformClient.getTensorboardTimeSeries(request);
        console.log(response);
      }
    
      callGetTensorboardTimeSeries();
    
    

### getTensorboardTimeSeries(request, options, callback)
    
    
    getTensorboardTimeSeries(request: protos.google.cloud.aiplatform.v1beta1.IGetTensorboardTimeSeriesRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries, protos.google.cloud.aiplatform.v1beta1.IGetTensorboardTimeSeriesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardtimeseriesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardtimeseries), [protos.google.cloud.aiplatform.v1beta1.IGetTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardtimeseriesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTensorboardTimeSeries(request, callback)
    
    
    getTensorboardTimeSeries(request: protos.google.cloud.aiplatform.v1beta1.IGetTensorboardTimeSeriesRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries, protos.google.cloud.aiplatform.v1beta1.IGetTensorboardTimeSeriesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardtimeseriesrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardtimeseries), [protos.google.cloud.aiplatform.v1beta1.IGetTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettensorboardtimeseriesrequest) | null | undefined, {} | null | undefined>`   
  
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
    

### listTensorboardExperiments(request, options)
    
    
    listTensorboardExperiments(request?: protos.google.cloud.aiplatform.v1beta1.IListTensorboardExperimentsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment[],
            protos.google.cloud.aiplatform.v1beta1.IListTensorboardExperimentsRequest | null,
            protos.google.cloud.aiplatform.v1beta1.IListTensorboardExperimentsResponse
        ]>;

Lists TensorboardExperiments in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTensorboardExperimentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardexperimentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardexperiment)[], [protos.google.cloud.aiplatform.v1beta1.IListTensorboardExperimentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardexperimentsrequest) | null, [protos.google.cloud.aiplatform.v1beta1.IListTensorboardExperimentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardexperimentsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [TensorboardExperiment](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.tensorboardexperiment). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listTensorboardExperimentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listTensorboardExperiments(request, options, callback)
    
    
    listTensorboardExperiments(request: protos.google.cloud.aiplatform.v1beta1.IListTensorboardExperimentsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListTensorboardExperimentsRequest, protos.google.cloud.aiplatform.v1beta1.IListTensorboardExperimentsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTensorboardExperimentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardexperimentsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListTensorboardExperimentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardexperimentsrequest), [protos.google.cloud.aiplatform.v1beta1.IListTensorboardExperimentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardexperimentsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardexperiment)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTensorboardExperiments(request, callback)
    
    
    listTensorboardExperiments(request: protos.google.cloud.aiplatform.v1beta1.IListTensorboardExperimentsRequest, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListTensorboardExperimentsRequest, protos.google.cloud.aiplatform.v1beta1.IListTensorboardExperimentsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTensorboardExperimentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardexperimentsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListTensorboardExperimentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardexperimentsrequest), [protos.google.cloud.aiplatform.v1beta1.IListTensorboardExperimentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardexperimentsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardexperiment)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTensorboardExperimentsAsync(request, options)
    
    
    listTensorboardExperimentsAsync(request?: protos.google.cloud.aiplatform.v1beta1.IListTensorboardExperimentsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment>;

Equivalent to `listTensorboardExperiments`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTensorboardExperimentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardexperimentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardexperiment)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [TensorboardExperiment](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.tensorboardexperiment). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Tensorboard to list
       *  TensorboardExperiments. Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}`
       */
      // const parent = 'abc123'
      /**
       *  Lists the TensorboardExperiments that match the filter expression.
       */
      // const filter = 'abc123'
      /**
       *  The maximum number of TensorboardExperiments to return. The service may
       *  return fewer than this value. If unspecified, at most 50
       *  TensorboardExperiments are returned. The maximum value is 1000; values
       *  above 1000 are coerced to 1000.
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous
       *  TensorboardService.ListTensorboardExperiments google.cloud.aiplatform.v1beta1.TensorboardService.ListTensorboardExperiments 
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  TensorboardService.ListTensorboardExperiments google.cloud.aiplatform.v1beta1.TensorboardService.ListTensorboardExperiments 
       *  must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Field to use to sort the list.
       */
      // const orderBy = 'abc123'
      /**
       *  Mask specifying which fields to read.
       */
      // const readMask = {}
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callListTensorboardExperiments() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = aiplatformClient.listTensorboardExperimentsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListTensorboardExperiments();
    
    

### listTensorboardExperimentsStream(request, options)
    
    
    listTensorboardExperimentsStream(request?: protos.google.cloud.aiplatform.v1beta1.IListTensorboardExperimentsRequest, options?: CallOptions): Transform;

Equivalent to `listTensorboardExperiments`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTensorboardExperimentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardexperimentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [TensorboardExperiment](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.tensorboardexperiment) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listTensorboardExperimentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listTensorboardRuns(request, options)
    
    
    listTensorboardRuns(request?: protos.google.cloud.aiplatform.v1beta1.IListTensorboardRunsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ITensorboardRun[],
            protos.google.cloud.aiplatform.v1beta1.IListTensorboardRunsRequest | null,
            protos.google.cloud.aiplatform.v1beta1.IListTensorboardRunsResponse
        ]>;

Lists TensorboardRuns in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTensorboardRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardrunsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ITensorboardRun](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardrun)[], [protos.google.cloud.aiplatform.v1beta1.IListTensorboardRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardrunsrequest) | null, [protos.google.cloud.aiplatform.v1beta1.IListTensorboardRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardrunsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [TensorboardRun](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.tensorboardrun). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listTensorboardRunsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listTensorboardRuns(request, options, callback)
    
    
    listTensorboardRuns(request: protos.google.cloud.aiplatform.v1beta1.IListTensorboardRunsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListTensorboardRunsRequest, protos.google.cloud.aiplatform.v1beta1.IListTensorboardRunsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.ITensorboardRun>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTensorboardRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardrunsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListTensorboardRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardrunsrequest), [protos.google.cloud.aiplatform.v1beta1.IListTensorboardRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardrunsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.ITensorboardRun](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardrun)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTensorboardRuns(request, callback)
    
    
    listTensorboardRuns(request: protos.google.cloud.aiplatform.v1beta1.IListTensorboardRunsRequest, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListTensorboardRunsRequest, protos.google.cloud.aiplatform.v1beta1.IListTensorboardRunsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.ITensorboardRun>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTensorboardRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardrunsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListTensorboardRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardrunsrequest), [protos.google.cloud.aiplatform.v1beta1.IListTensorboardRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardrunsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.ITensorboardRun](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardrun)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTensorboardRunsAsync(request, options)
    
    
    listTensorboardRunsAsync(request?: protos.google.cloud.aiplatform.v1beta1.IListTensorboardRunsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.aiplatform.v1beta1.ITensorboardRun>;

Equivalent to `listTensorboardRuns`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTensorboardRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardrunsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.aiplatform.v1beta1.ITensorboardRun](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardrun)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [TensorboardRun](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.tensorboardrun). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the TensorboardExperiment to list
       *  TensorboardRuns. Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`
       */
      // const parent = 'abc123'
      /**
       *  Lists the TensorboardRuns that match the filter expression.
       */
      // const filter = 'abc123'
      /**
       *  The maximum number of TensorboardRuns to return. The service may return
       *  fewer than this value. If unspecified, at most 50 TensorboardRuns are
       *  returned. The maximum value is 1000; values above 1000 are coerced to
       *  1000.
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous
       *  TensorboardService.ListTensorboardRuns google.cloud.aiplatform.v1beta1.TensorboardService.ListTensorboardRuns 
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  TensorboardService.ListTensorboardRuns google.cloud.aiplatform.v1beta1.TensorboardService.ListTensorboardRuns 
       *  must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Field to use to sort the list.
       */
      // const orderBy = 'abc123'
      /**
       *  Mask specifying which fields to read.
       */
      // const readMask = {}
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callListTensorboardRuns() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = aiplatformClient.listTensorboardRunsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListTensorboardRuns();
    
    

### listTensorboardRunsStream(request, options)
    
    
    listTensorboardRunsStream(request?: protos.google.cloud.aiplatform.v1beta1.IListTensorboardRunsRequest, options?: CallOptions): Transform;

Equivalent to `listTensorboardRuns`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTensorboardRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardrunsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [TensorboardRun](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.tensorboardrun) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listTensorboardRunsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listTensorboards(request, options)
    
    
    listTensorboards(request?: protos.google.cloud.aiplatform.v1beta1.IListTensorboardsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ITensorboard[],
            protos.google.cloud.aiplatform.v1beta1.IListTensorboardsRequest | null,
            protos.google.cloud.aiplatform.v1beta1.IListTensorboardsResponse
        ]>;

Lists Tensorboards in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTensorboardsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ITensorboard](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboard)[], [protos.google.cloud.aiplatform.v1beta1.IListTensorboardsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardsrequest) | null, [protos.google.cloud.aiplatform.v1beta1.IListTensorboardsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Tensorboard](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.tensorboard). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listTensorboardsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listTensorboards(request, options, callback)
    
    
    listTensorboards(request: protos.google.cloud.aiplatform.v1beta1.IListTensorboardsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListTensorboardsRequest, protos.google.cloud.aiplatform.v1beta1.IListTensorboardsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.ITensorboard>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTensorboardsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListTensorboardsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardsrequest), [protos.google.cloud.aiplatform.v1beta1.IListTensorboardsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.ITensorboard](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboard)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTensorboards(request, callback)
    
    
    listTensorboards(request: protos.google.cloud.aiplatform.v1beta1.IListTensorboardsRequest, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListTensorboardsRequest, protos.google.cloud.aiplatform.v1beta1.IListTensorboardsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.ITensorboard>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTensorboardsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListTensorboardsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardsrequest), [protos.google.cloud.aiplatform.v1beta1.IListTensorboardsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.ITensorboard](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboard)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTensorboardsAsync(request, options)
    
    
    listTensorboardsAsync(request?: protos.google.cloud.aiplatform.v1beta1.IListTensorboardsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.aiplatform.v1beta1.ITensorboard>;

Equivalent to `listTensorboards`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTensorboardsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.aiplatform.v1beta1.ITensorboard](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboard)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Tensorboard](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.tensorboard). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Location to list Tensorboards.
       *  Format:
       *  `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Lists the Tensorboards that match the filter expression.
       */
      // const filter = 'abc123'
      /**
       *  The maximum number of Tensorboards to return. The service may return
       *  fewer than this value. If unspecified, at most 100 Tensorboards are
       *  returned. The maximum value is 100; values above 100 are coerced to
       *  100.
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous
       *  TensorboardService.ListTensorboards google.cloud.aiplatform.v1beta1.TensorboardService.ListTensorboards 
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  TensorboardService.ListTensorboards google.cloud.aiplatform.v1beta1.TensorboardService.ListTensorboards 
       *  must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Field to use to sort the list.
       */
      // const orderBy = 'abc123'
      /**
       *  Mask specifying which fields to read.
       */
      // const readMask = {}
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callListTensorboards() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = aiplatformClient.listTensorboardsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListTensorboards();
    
    

### listTensorboardsStream(request, options)
    
    
    listTensorboardsStream(request?: protos.google.cloud.aiplatform.v1beta1.IListTensorboardsRequest, options?: CallOptions): Transform;

Equivalent to `listTensorboards`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTensorboardsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Tensorboard](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.tensorboard) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listTensorboardsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listTensorboardTimeSeries(request, options)
    
    
    listTensorboardTimeSeries(request?: protos.google.cloud.aiplatform.v1beta1.IListTensorboardTimeSeriesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries[],
            protos.google.cloud.aiplatform.v1beta1.IListTensorboardTimeSeriesRequest | null,
            protos.google.cloud.aiplatform.v1beta1.IListTensorboardTimeSeriesResponse
        ]>;

Lists TensorboardTimeSeries in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardtimeseriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardtimeseries)[], [protos.google.cloud.aiplatform.v1beta1.IListTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardtimeseriesrequest) | null, [protos.google.cloud.aiplatform.v1beta1.IListTensorboardTimeSeriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardtimeseriesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listTensorboardTimeSeriesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listTensorboardTimeSeries(request, options, callback)
    
    
    listTensorboardTimeSeries(request: protos.google.cloud.aiplatform.v1beta1.IListTensorboardTimeSeriesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListTensorboardTimeSeriesRequest, protos.google.cloud.aiplatform.v1beta1.IListTensorboardTimeSeriesResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardtimeseriesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardtimeseriesrequest), [protos.google.cloud.aiplatform.v1beta1.IListTensorboardTimeSeriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardtimeseriesresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardtimeseries)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTensorboardTimeSeries(request, callback)
    
    
    listTensorboardTimeSeries(request: protos.google.cloud.aiplatform.v1beta1.IListTensorboardTimeSeriesRequest, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListTensorboardTimeSeriesRequest, protos.google.cloud.aiplatform.v1beta1.IListTensorboardTimeSeriesResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardtimeseriesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardtimeseriesrequest), [protos.google.cloud.aiplatform.v1beta1.IListTensorboardTimeSeriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardtimeseriesresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardtimeseries)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTensorboardTimeSeriesAsync(request, options)
    
    
    listTensorboardTimeSeriesAsync(request?: protos.google.cloud.aiplatform.v1beta1.IListTensorboardTimeSeriesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries>;

Equivalent to `listTensorboardTimeSeries`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardtimeseriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardtimeseries)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the TensorboardRun to list
       *  TensorboardTimeSeries. Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}`
       */
      // const parent = 'abc123'
      /**
       *  Lists the TensorboardTimeSeries that match the filter expression.
       */
      // const filter = 'abc123'
      /**
       *  The maximum number of TensorboardTimeSeries to return. The service may
       *  return fewer than this value. If unspecified, at most 50
       *  TensorboardTimeSeries are returned. The maximum value is 1000; values
       *  above 1000 are coerced to 1000.
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous
       *  TensorboardService.ListTensorboardTimeSeries google.cloud.aiplatform.v1beta1.TensorboardService.ListTensorboardTimeSeries 
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  TensorboardService.ListTensorboardTimeSeries google.cloud.aiplatform.v1beta1.TensorboardService.ListTensorboardTimeSeries 
       *  must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Field to use to sort the list.
       */
      // const orderBy = 'abc123'
      /**
       *  Mask specifying which fields to read.
       */
      // const readMask = {}
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callListTensorboardTimeSeries() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = aiplatformClient.listTensorboardTimeSeriesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListTensorboardTimeSeries();
    
    

### listTensorboardTimeSeriesStream(request, options)
    
    
    listTensorboardTimeSeriesStream(request?: protos.google.cloud.aiplatform.v1beta1.IListTensorboardTimeSeriesRequest, options?: CallOptions): Transform;

Equivalent to `listTensorboardTimeSeries`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttensorboardtimeseriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listTensorboardTimeSeriesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### readTensorboardBlobData(request, options)
    
    
    readTensorboardBlobData(request?: protos.google.cloud.aiplatform.v1beta1.IReadTensorboardBlobDataRequest, options?: CallOptions): gax.CancellableStream;

Gets bytes of TensorboardBlobs. This is to allow reading blob data stored in consumer project's Cloud Storage bucket without users having to obtain Cloud Storage access permission.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReadTensorboardBlobDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardblobdatarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`gax.CancellableStream` | {Stream} An object stream which emits [ReadTensorboardBlobDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.readtensorboardblobdataresponse) on 'data' event. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#server-streaming) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the TensorboardTimeSeries to list Blobs.
       *  Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`
       */
      // const timeSeries = 'abc123'
      /**
       *  IDs of the blobs to read.
       */
      // const blobIds = ['abc','def']
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callReadTensorboardBlobData() {
        // Construct request
        const request = {
          timeSeries,
        };
    
        // Run request
        const stream = await aiplatformClient.readTensorboardBlobData(request);
        stream.on('data', (response) => { console.log(response) });
        stream.on('error', (err) => { throw(err) });
        stream.on('end', () => { /* API call completed */ });
      }
    
      callReadTensorboardBlobData();
    
    

### readTensorboardSize(request, options)
    
    
    readTensorboardSize(request?: protos.google.cloud.aiplatform.v1beta1.IReadTensorboardSizeRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IReadTensorboardSizeResponse,
            (protos.google.cloud.aiplatform.v1beta1.IReadTensorboardSizeRequest | undefined),
            {} | undefined
        ]>;

Returns the storage size for a given TensorBoard instance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReadTensorboardSizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardsizerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IReadTensorboardSizeResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardsizeresponse), ([protos.google.cloud.aiplatform.v1beta1.IReadTensorboardSizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardsizerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ReadTensorboardSizeResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.readtensorboardsizeresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Tensorboard resource.
       *  Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}`
       */
      // const tensorboard = 'abc123'
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callReadTensorboardSize() {
        // Construct request
        const request = {
          tensorboard,
        };
    
        // Run request
        const response = await aiplatformClient.readTensorboardSize(request);
        console.log(response);
      }
    
      callReadTensorboardSize();
    
    

### readTensorboardSize(request, options, callback)
    
    
    readTensorboardSize(request: protos.google.cloud.aiplatform.v1beta1.IReadTensorboardSizeRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IReadTensorboardSizeResponse, protos.google.cloud.aiplatform.v1beta1.IReadTensorboardSizeRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReadTensorboardSizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardsizerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IReadTensorboardSizeResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardsizeresponse), [protos.google.cloud.aiplatform.v1beta1.IReadTensorboardSizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardsizerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### readTensorboardSize(request, callback)
    
    
    readTensorboardSize(request: protos.google.cloud.aiplatform.v1beta1.IReadTensorboardSizeRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IReadTensorboardSizeResponse, protos.google.cloud.aiplatform.v1beta1.IReadTensorboardSizeRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReadTensorboardSizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardsizerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IReadTensorboardSizeResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardsizeresponse), [protos.google.cloud.aiplatform.v1beta1.IReadTensorboardSizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardsizerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### readTensorboardTimeSeriesData(request, options)
    
    
    readTensorboardTimeSeriesData(request?: protos.google.cloud.aiplatform.v1beta1.IReadTensorboardTimeSeriesDataRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IReadTensorboardTimeSeriesDataResponse,
            (protos.google.cloud.aiplatform.v1beta1.IReadTensorboardTimeSeriesDataRequest | undefined),
            {} | undefined
        ]>;

Reads a TensorboardTimeSeries' data. By default, if the number of data points stored is less than 1000, all data is returned. Otherwise, 1000 data points is randomly selected from this time series and returned. This value can be changed by changing max_data_points, which can't be greater than 10k.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReadTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardtimeseriesdatarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IReadTensorboardTimeSeriesDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardtimeseriesdataresponse), ([protos.google.cloud.aiplatform.v1beta1.IReadTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardtimeseriesdatarequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ReadTensorboardTimeSeriesDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.readtensorboardtimeseriesdataresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the TensorboardTimeSeries to read data from.
       *  Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`
       */
      // const tensorboardTimeSeries = 'abc123'
      /**
       *  The maximum number of TensorboardTimeSeries' data to return.
       *  This value should be a positive integer.
       *  This value can be set to -1 to return all data.
       */
      // const maxDataPoints = 1234
      /**
       *  Reads the TensorboardTimeSeries' data that match the filter expression.
       */
      // const filter = 'abc123'
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callReadTensorboardTimeSeriesData() {
        // Construct request
        const request = {
          tensorboardTimeSeries,
        };
    
        // Run request
        const response = await aiplatformClient.readTensorboardTimeSeriesData(request);
        console.log(response);
      }
    
      callReadTensorboardTimeSeriesData();
    
    

### readTensorboardTimeSeriesData(request, options, callback)
    
    
    readTensorboardTimeSeriesData(request: protos.google.cloud.aiplatform.v1beta1.IReadTensorboardTimeSeriesDataRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IReadTensorboardTimeSeriesDataResponse, protos.google.cloud.aiplatform.v1beta1.IReadTensorboardTimeSeriesDataRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReadTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardtimeseriesdatarequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IReadTensorboardTimeSeriesDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardtimeseriesdataresponse), [protos.google.cloud.aiplatform.v1beta1.IReadTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardtimeseriesdatarequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### readTensorboardTimeSeriesData(request, callback)
    
    
    readTensorboardTimeSeriesData(request: protos.google.cloud.aiplatform.v1beta1.IReadTensorboardTimeSeriesDataRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IReadTensorboardTimeSeriesDataResponse, protos.google.cloud.aiplatform.v1beta1.IReadTensorboardTimeSeriesDataRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReadTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardtimeseriesdatarequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IReadTensorboardTimeSeriesDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardtimeseriesdataresponse), [protos.google.cloud.aiplatform.v1beta1.IReadTensorboardTimeSeriesDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardtimeseriesdatarequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### readTensorboardUsage(request, options)
    
    
    readTensorboardUsage(request?: protos.google.cloud.aiplatform.v1beta1.IReadTensorboardUsageRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IReadTensorboardUsageResponse,
            (protos.google.cloud.aiplatform.v1beta1.IReadTensorboardUsageRequest | undefined),
            {} | undefined
        ]>;

Returns a list of monthly active users for a given TensorBoard instance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReadTensorboardUsageRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardusagerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IReadTensorboardUsageResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardusageresponse), ([protos.google.cloud.aiplatform.v1beta1.IReadTensorboardUsageRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardusagerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Tensorboard resource.
       *  Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}`
       */
      // const tensorboard = 'abc123'
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callReadTensorboardUsage() {
        // Construct request
        const request = {
          tensorboard,
        };
    
        // Run request
        const response = await aiplatformClient.readTensorboardUsage(request);
        console.log(response);
      }
    
      callReadTensorboardUsage();
    
    

### readTensorboardUsage(request, options, callback)
    
    
    readTensorboardUsage(request: protos.google.cloud.aiplatform.v1beta1.IReadTensorboardUsageRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IReadTensorboardUsageResponse, protos.google.cloud.aiplatform.v1beta1.IReadTensorboardUsageRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReadTensorboardUsageRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardusagerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IReadTensorboardUsageResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardusageresponse), [protos.google.cloud.aiplatform.v1beta1.IReadTensorboardUsageRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardusagerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### readTensorboardUsage(request, callback)
    
    
    readTensorboardUsage(request: protos.google.cloud.aiplatform.v1beta1.IReadTensorboardUsageRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IReadTensorboardUsageResponse, protos.google.cloud.aiplatform.v1beta1.IReadTensorboardUsageRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReadTensorboardUsageRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardusagerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IReadTensorboardUsageResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardusageresponse), [protos.google.cloud.aiplatform.v1beta1.IReadTensorboardUsageRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadtensorboardusagerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
  
### updateTensorboard(request, options)
    
    
    updateTensorboard(request?: protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.aiplatform.v1beta1.ITensorboard, protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates a Tensorboard.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTensorboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.aiplatform.v1beta1.ITensorboard](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboard), [protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Field mask is used to specify the fields to be overwritten in the
       *  Tensorboard resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field is overwritten if it's in the mask. If the
       *  user does not provide a mask then all fields are overwritten if new
       *  values are specified.
       */
      // const updateMask = {}
      /**
       *  Required. The Tensorboard's `name` field is used to identify the
       *  Tensorboard to be updated. Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}`
       */
      // const tensorboard = {}
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callUpdateTensorboard() {
        // Construct request
        const request = {
          updateMask,
          tensorboard,
        };
    
        // Run request
        const [operation] = await aiplatformClient.updateTensorboard(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateTensorboard();
    
    

### updateTensorboard(request, options, callback)
    
    
    updateTensorboard(request: protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.ITensorboard, protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTensorboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.ITensorboard](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboard), [protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTensorboard(request, callback)
    
    
    updateTensorboard(request: protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardRequest, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.ITensorboard, protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTensorboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.ITensorboard](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboard), [protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTensorboardExperiment(request, options)
    
    
    updateTensorboardExperiment(request?: protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardExperimentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment,
            (protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardExperimentRequest | undefined),
            {} | undefined
        ]>;

Updates a TensorboardExperiment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTensorboardExperimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardexperimentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardexperiment), ([protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardExperimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardexperimentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [TensorboardExperiment](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.tensorboardexperiment). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Field mask is used to specify the fields to be overwritten in the
       *  TensorboardExperiment resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field is overwritten if it's in the mask. If the
       *  user does not provide a mask then all fields are overwritten if new
       *  values are specified.
       */
      // const updateMask = {}
      /**
       *  Required. The TensorboardExperiment's `name` field is used to identify the
       *  TensorboardExperiment to be updated. Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`
       */
      // const tensorboardExperiment = {}
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callUpdateTensorboardExperiment() {
        // Construct request
        const request = {
          updateMask,
          tensorboardExperiment,
        };
    
        // Run request
        const response = await aiplatformClient.updateTensorboardExperiment(request);
        console.log(response);
      }
    
      callUpdateTensorboardExperiment();
    
    

### updateTensorboardExperiment(request, options, callback)
    
    
    updateTensorboardExperiment(request: protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardExperimentRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment, protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardExperimentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTensorboardExperimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardexperimentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardexperiment), [protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardExperimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardexperimentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTensorboardExperiment(request, callback)
    
    
    updateTensorboardExperiment(request: protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardExperimentRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment, protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardExperimentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTensorboardExperimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardexperimentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITensorboardExperiment](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardexperiment), [protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardExperimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardexperimentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTensorboardRun(request, options)
    
    
    updateTensorboardRun(request?: protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardRunRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ITensorboardRun,
            (protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardRunRequest | undefined),
            {} | undefined
        ]>;

Updates a TensorboardRun.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTensorboardRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardrunrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ITensorboardRun](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardrun), ([protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardrunrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [TensorboardRun](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.tensorboardrun). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Field mask is used to specify the fields to be overwritten in the
       *  TensorboardRun resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field is overwritten if it's in the mask. If the
       *  user does not provide a mask then all fields are overwritten if new
       *  values are specified.
       */
      // const updateMask = {}
      /**
       *  Required. The TensorboardRun's `name` field is used to identify the
       *  TensorboardRun to be updated. Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}`
       */
      // const tensorboardRun = {}
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callUpdateTensorboardRun() {
        // Construct request
        const request = {
          updateMask,
          tensorboardRun,
        };
    
        // Run request
        const response = await aiplatformClient.updateTensorboardRun(request);
        console.log(response);
      }
    
      callUpdateTensorboardRun();
    
    

### updateTensorboardRun(request, options, callback)
    
    
    updateTensorboardRun(request: protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardRunRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITensorboardRun, protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardRunRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTensorboardRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardrunrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITensorboardRun](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardrun), [protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardrunrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTensorboardRun(request, callback)
    
    
    updateTensorboardRun(request: protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardRunRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITensorboardRun, protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardRunRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTensorboardRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardrunrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITensorboardRun](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardrun), [protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardrunrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTensorboardTimeSeries(request, options)
    
    
    updateTensorboardTimeSeries(request?: protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardTimeSeriesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries,
            (protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardTimeSeriesRequest | undefined),
            {} | undefined
        ]>;

Updates a TensorboardTimeSeries.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardtimeseriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardtimeseries), ([protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardtimeseriesrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Field mask is used to specify the fields to be overwritten in the
       *  TensorboardTimeSeries resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field is overwritten if it's in the mask. If the
       *  user does not provide a mask then all fields are overwritten if new
       *  values are specified.
       */
      // const updateMask = {}
      /**
       *  Required. The TensorboardTimeSeries' `name` field is used to identify the
       *  TensorboardTimeSeries to be updated.
       *  Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}`
       */
      // const tensorboardTimeSeries = {}
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callUpdateTensorboardTimeSeries() {
        // Construct request
        const request = {
          updateMask,
          tensorboardTimeSeries,
        };
    
        // Run request
        const response = await aiplatformClient.updateTensorboardTimeSeries(request);
        console.log(response);
      }
    
      callUpdateTensorboardTimeSeries();
    
    

### updateTensorboardTimeSeries(request, options, callback)
    
    
    updateTensorboardTimeSeries(request: protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardTimeSeriesRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries, protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardTimeSeriesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardtimeseriesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardtimeseries), [protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardtimeseriesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTensorboardTimeSeries(request, callback)
    
    
    updateTensorboardTimeSeries(request: protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardTimeSeriesRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries, protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardTimeSeriesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardtimeseriesrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITensorboardTimeSeries](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itensorboardtimeseries), [protos.google.cloud.aiplatform.v1beta1.IUpdateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatetensorboardtimeseriesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### writeTensorboardExperimentData(request, options)
    
    
    writeTensorboardExperimentData(request?: protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardExperimentDataRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardExperimentDataResponse,
            (protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardExperimentDataRequest | undefined),
            {} | undefined
        ]>;

Write time series data points of multiple TensorboardTimeSeries in multiple TensorboardRun's. If any data fail to be ingested, an error is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IWriteTensorboardExperimentDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iwritetensorboardexperimentdatarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardExperimentDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iwritetensorboardexperimentdataresponse), ([protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardExperimentDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iwritetensorboardexperimentdatarequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [WriteTensorboardExperimentDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.writetensorboardexperimentdataresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the TensorboardExperiment to write data to.
       *  Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}`
       */
      // const tensorboardExperiment = 'abc123'
      /**
       *  Required. Requests containing per-run TensorboardTimeSeries data to write.
       */
      // const writeRunDataRequests = [1,2,3,4]
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callWriteTensorboardExperimentData() {
        // Construct request
        const request = {
          tensorboardExperiment,
          writeRunDataRequests,
        };
    
        // Run request
        const response = await aiplatformClient.writeTensorboardExperimentData(request);
        console.log(response);
      }
    
      callWriteTensorboardExperimentData();
    
    

### writeTensorboardExperimentData(request, options, callback)
    
    
    writeTensorboardExperimentData(request: protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardExperimentDataRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardExperimentDataResponse, protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardExperimentDataRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IWriteTensorboardExperimentDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iwritetensorboardexperimentdatarequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardExperimentDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iwritetensorboardexperimentdataresponse), [protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardExperimentDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iwritetensorboardexperimentdatarequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### writeTensorboardExperimentData(request, callback)
    
    
    writeTensorboardExperimentData(request: protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardExperimentDataRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardExperimentDataResponse, protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardExperimentDataRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IWriteTensorboardExperimentDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iwritetensorboardexperimentdatarequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardExperimentDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iwritetensorboardexperimentdataresponse), [protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardExperimentDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iwritetensorboardexperimentdatarequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### writeTensorboardRunData(request, options)
    
    
    writeTensorboardRunData(request?: protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardRunDataRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardRunDataResponse,
            (protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardRunDataRequest | undefined),
            {} | undefined
        ]>;

Write time series data points into multiple TensorboardTimeSeries under a TensorboardRun. If any data fail to be ingested, an error is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IWriteTensorboardRunDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iwritetensorboardrundatarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardRunDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iwritetensorboardrundataresponse), ([protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardRunDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iwritetensorboardrundatarequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [WriteTensorboardRunDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.writetensorboardrundataresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the TensorboardRun to write data to.
       *  Format:
       *  `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}`
       */
      // const tensorboardRun = 'abc123'
      /**
       *  Required. The TensorboardTimeSeries data to write.
       *  Values with in a time series are indexed by their step value.
       *  Repeated writes to the same step will overwrite the existing value for that
       *  step.
       *  The upper limit of data points per write request is 5000.
       */
      // const timeSeriesData = [1,2,3,4]
    
      // Imports the Aiplatform library
      const {TensorboardServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [TensorboardServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callWriteTensorboardRunData() {
        // Construct request
        const request = {
          tensorboardRun,
          timeSeriesData,
        };
    
        // Run request
        const response = await aiplatformClient.writeTensorboardRunData(request);
        console.log(response);
      }
    
      callWriteTensorboardRunData();
    
    

### writeTensorboardRunData(request, options, callback)
    
    
    writeTensorboardRunData(request: protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardRunDataRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardRunDataResponse, protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardRunDataRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IWriteTensorboardRunDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iwritetensorboardrundatarequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardRunDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iwritetensorboardrundataresponse), [protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardRunDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iwritetensorboardrundatarequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### writeTensorboardRunData(request, callback)
    
    
    writeTensorboardRunData(request: protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardRunDataRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardRunDataResponse, protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardRunDataRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IWriteTensorboardRunDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iwritetensorboardrundatarequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardRunDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iwritetensorboardrundataresponse), [protos.google.cloud.aiplatform.v1beta1.IWriteTensorboardRunDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iwritetensorboardrundatarequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
