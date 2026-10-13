---
url: https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/v1beta.usageserviceclient
title: Class v1beta.UsageServiceClient (0.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:25:07.940843+00:00
---

# Class v1beta.UsageServiceClient (0.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/v1beta.usageserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.UsageServiceClient (0.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.1 (latest)  0.2.0  0.1.2 

Provides access to historical and forecasted usage data. v1beta

## Package

[@google-cloud/capacityplanner](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of UsageServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new UsageServiceClient({fallback: true}, gax); ```  
  
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

### universeDomain
    
    
    get universeDomain(): string;

### usageServiceStub
    
    
    usageServiceStub?: Promise<{
            [name: string]: Function;
        }>;

### warn
    
    
    warn: (code: string, message: string, warnType?: string) => void;

## Methods 

### checkExportForecastsProgress(name)
    
    
    checkExportForecastsProgress(name: string): Promise<LROperation<protos.google.cloud.capacityplanner.v1beta.ExportForecastsResponse, protos.google.cloud.capacityplanner.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `exportForecasts()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.capacityplanner.v1beta.ExportForecastsResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.exportforecastsresponse), [protos.google.cloud.capacityplanner.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The compute engine resource and location for the time series
       *  values to return. The format is:
       *     projects/{project}/locations/{location} or
       *     organizations/{organization}/locations/{location} or
       *     folders/{folder}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Optional. The machine family to use to select the `Forecast` values to
       *  return. Possible values include "n1", and "n2d".
       */
      // const machineFamily = 'abc123'
      /**
       *  Optional. The machine shape for the time series values to export.
       */
      // const machineShape = {}
      /**
       *  Optional. The disk_type for the `Forecast` values to return with request
       *  persistent-disk resource_type.
       */
      // const diskType = 'abc123'
      /**
       *  Optional. The GPU type for the `Forecast` values to return. Sample values
       *  are "nvidia-tesla-t4", and "nvidia-tesla-a100". See
       *  https://cloud.google.com/compute/docs/gpus for a list. Empty gpu_type
       *  will return results matching all GPUs.
       */
      // const gpuType = 'abc123'
      /**
       *  Optional. The TPU type for the `Forecast` values to return. Empty tpu_type
       *  will return results matching all TPUs.
       */
      // const tpuType = 'abc123'
      /**
       *  Required. The resource for the `Forecast` values to return. Possible values
       *  include "gce-vcpus", "gce-ram", "gce-local-ssd", "gce-persistent-disk",
       *  "gce-gpu" and "gce-tpu".
       */
      // const resourceType = 'abc123'
      /**
       *  Optional. The prediction interval to use to select the `Forecast` values to
       *  return. PREDICTION_INTERVAL_UNSPECIFIED will return results matching all
       *  prediction intervals.
       */
      // const predictionInterval = {}
      /**
       *  Optional. Aggregation Method of the historical usage for which the forecast
       *  is generated.
       */
      // const aggregationMethod = {}
      /**
       *  Optional. The start date of forecasts.
       */
      // const startDate = {}
      /**
       *  Optional. The end date of forecasts.
       */
      // const endDate = {}
      /**
       *  Required. Output configuration indicating where the results will be output
       *  to.
       */
      // const outputConfig = {}
    
      // Imports the Capacityplanner library
      const {UsageServiceClient} = require('[@google-cloud/capacityplanner](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const capacityplannerClient = new [UsageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)();
    
      async function callExportForecasts() {
        // Construct request
        const request = {
          parent,
          resourceType,
          outputConfig,
        };
    
        // Run request
        const [operation] = await capacityplannerClient.exportForecasts(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportForecasts();
    
    

### checkExportReservationsUsageProgress(name)
    
    
    checkExportReservationsUsageProgress(name: string): Promise<LROperation<protos.google.cloud.capacityplanner.v1beta.ExportReservationsUsageResponse, protos.google.cloud.capacityplanner.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `exportReservationsUsage()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.capacityplanner.v1beta.ExportReservationsUsageResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.exportreservationsusageresponse), [protos.google.cloud.capacityplanner.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. The machine family to query reservations and usage by. For
       *  example: n1, n2d.
       */
      // const machineFamily = 'abc123'
      /**
       *  Optional. The machine_shape as a filter to select matching reservations
       *  and its usage.
       */
      // const machineShape = {}
      /**
       *  Optional. The GPU type to query reservations and usage  by. For example:
       *  NVIDIA T4.
       */
      // const gpuType = 'abc123'
      /**
       *  Required. The compute engine resource and location of the
       *  reservationsusage. The format is:
       *     projects/{project}/locations/{location} or
       *     organizations/{organization}/locations/{location} or
       *     folders/{folder}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Optional. The location level of the reservations usage timeseries.
       */
      // const locationLevel = {}
      /**
       *  Required. The resource for the `ReservationsUsage` values to return.
       *  Possible values include "gce-vcpus", "gce-ram", "gce-local-ssd", and
       *  "gce-gpu".
       */
      // const cloudResourceType = 'abc123'
      /**
       *  Required. The method that should be used to convert sampled reservations
       *  data to daily usage values.
       */
      // const usageAggregationMethod = {}
      /**
       *  Optional. Type of share settings to filter reservations in response. If
       *  unspecified, all types are included.
       */
      // const shareType = {}
      /**
       *  Optional. The start date of reservations usage.
       */
      // const startDate = {}
      /**
       *  Optional. The end date of reservations usage.
       */
      // const endDate = {}
      /**
       *  Required. Output configuration indicating where the results will be output
       *  to.
       */
      // const outputConfig = {}
    
      // Imports the Capacityplanner library
      const {UsageServiceClient} = require('[@google-cloud/capacityplanner](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const capacityplannerClient = new [UsageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)();
    
      async function callExportReservationsUsage() {
        // Construct request
        const request = {
          parent,
          cloudResourceType,
          usageAggregationMethod,
          outputConfig,
        };
    
        // Run request
        const [operation] = await capacityplannerClient.exportReservationsUsage(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportReservationsUsage();
    
    

### checkExportUsageHistoriesProgress(name)
    
    
    checkExportUsageHistoriesProgress(name: string): Promise<LROperation<protos.google.cloud.capacityplanner.v1beta.ExportUsageHistoriesResponse, protos.google.cloud.capacityplanner.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `exportUsageHistories()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.capacityplanner.v1beta.ExportUsageHistoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.exportusagehistoriesresponse), [protos.google.cloud.capacityplanner.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The compute engine resource and location for the time series
       *  values to return. The format is:
       *     projects/{project}/locations/{location} or
       *     organizations/{organization}/locations/{location} or
       *     folders/{folder}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Optional. Set true to export usage for spot resources.
       */
      // const isSpot = true
      /**
       *  Optional. The machine family for the `UsageHistory` values to return.
       *  Possible values include "n1", and "n2d". See
       *  https://cloud.google.com/compute/docs/machine-types for more examples.
       */
      // const machineFamily = 'abc123'
      /**
       *  Optional. The machine shape for the time series values to export.
       */
      // const machineShape = {}
      /**
       *  Optional. The disk_type for the `UsageHistory` values to return request
       *  with persistent-disk resource_type. Possible values include "pd-ssd",
       *  "pd-standard", "pd-balanced", and "pd-extreme".
       */
      // const diskType = 'abc123'
      /**
       *  Optional. The GPU type for the `UsageHistory` values to return. Sample
       *  values are "nvidia-tesla-t4", and "nvidia-tesla-a100". See
       *  https://cloud.google.com/compute/docs/gpus for a list. Empty gpu_type
       *  will return results matching all GPUs.
       */
      // const gpuType = 'abc123'
      /**
       *  Optional. The TPU type for the `UsageHistory` values to return. Empty
       *  tpu_type will return results matching all TPUs.
       */
      // const tpuType = 'abc123'
      /**
       *  Required. The resource for the `UsageHistory` values to return. Possible
       *  values include "gce-vcpus", "gce-ram", "gce-local-ssd",
       *  "gce-persistent-disk", "gce-gpu" and "gce-tpu".
       */
      // const resourceType = 'abc123'
      /**
       *  Optional. The method that should be used to convert sampled usage data to
       *  daily usage values. AGGREGATION_METHOD_UNSPECIFIED will return results
       *  matching all the aggregation methods.
       */
      // const usageAggregationMethod = {}
      /**
       *  Optional. The start date of usage.
       */
      // const startDate = {}
      /**
       *  Optional. The end date of usage.
       */
      // const endDate = {}
      /**
       *  Required. Output configuration indicating where the results will be output
       *  to.
       */
      // const outputConfig = {}
    
      // Imports the Capacityplanner library
      const {UsageServiceClient} = require('[@google-cloud/capacityplanner](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const capacityplannerClient = new [UsageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)();
    
      async function callExportUsageHistories() {
        // Construct request
        const request = {
          parent,
          resourceType,
          outputConfig,
        };
    
        // Run request
        const [operation] = await capacityplannerClient.exportUsageHistories(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportUsageHistories();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### exportForecasts(request, options)
    
    
    exportForecasts(request?: protos.google.cloud.capacityplanner.v1beta.IExportForecastsRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.capacityplanner.v1beta.IExportForecastsResponse, protos.google.cloud.capacityplanner.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Exports forecasted usage data requested by user into either an existing Cloud Storage bucket or a BigQuery table.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportForecastsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iexportforecastsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.capacityplanner.v1beta.IExportForecastsResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iexportforecastsresponse), [protos.google.cloud.capacityplanner.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The compute engine resource and location for the time series
       *  values to return. The format is:
       *     projects/{project}/locations/{location} or
       *     organizations/{organization}/locations/{location} or
       *     folders/{folder}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Optional. The machine family to use to select the `Forecast` values to
       *  return. Possible values include "n1", and "n2d".
       */
      // const machineFamily = 'abc123'
      /**
       *  Optional. The machine shape for the time series values to export.
       */
      // const machineShape = {}
      /**
       *  Optional. The disk_type for the `Forecast` values to return with request
       *  persistent-disk resource_type.
       */
      // const diskType = 'abc123'
      /**
       *  Optional. The GPU type for the `Forecast` values to return. Sample values
       *  are "nvidia-tesla-t4", and "nvidia-tesla-a100". See
       *  https://cloud.google.com/compute/docs/gpus for a list. Empty gpu_type
       *  will return results matching all GPUs.
       */
      // const gpuType = 'abc123'
      /**
       *  Optional. The TPU type for the `Forecast` values to return. Empty tpu_type
       *  will return results matching all TPUs.
       */
      // const tpuType = 'abc123'
      /**
       *  Required. The resource for the `Forecast` values to return. Possible values
       *  include "gce-vcpus", "gce-ram", "gce-local-ssd", "gce-persistent-disk",
       *  "gce-gpu" and "gce-tpu".
       */
      // const resourceType = 'abc123'
      /**
       *  Optional. The prediction interval to use to select the `Forecast` values to
       *  return. PREDICTION_INTERVAL_UNSPECIFIED will return results matching all
       *  prediction intervals.
       */
      // const predictionInterval = {}
      /**
       *  Optional. Aggregation Method of the historical usage for which the forecast
       *  is generated.
       */
      // const aggregationMethod = {}
      /**
       *  Optional. The start date of forecasts.
       */
      // const startDate = {}
      /**
       *  Optional. The end date of forecasts.
       */
      // const endDate = {}
      /**
       *  Required. Output configuration indicating where the results will be output
       *  to.
       */
      // const outputConfig = {}
    
      // Imports the Capacityplanner library
      const {UsageServiceClient} = require('[@google-cloud/capacityplanner](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const capacityplannerClient = new [UsageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)();
    
      async function callExportForecasts() {
        // Construct request
        const request = {
          parent,
          resourceType,
          outputConfig,
        };
    
        // Run request
        const [operation] = await capacityplannerClient.exportForecasts(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportForecasts();
    
    

### exportForecasts(request, options, callback)
    
    
    exportForecasts(request: protos.google.cloud.capacityplanner.v1beta.IExportForecastsRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.capacityplanner.v1beta.IExportForecastsResponse, protos.google.cloud.capacityplanner.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportForecastsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iexportforecastsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.capacityplanner.v1beta.IExportForecastsResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iexportforecastsresponse), [protos.google.cloud.capacityplanner.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportForecasts(request, callback)
    
    
    exportForecasts(request: protos.google.cloud.capacityplanner.v1beta.IExportForecastsRequest, callback: Callback<LROperation<protos.google.cloud.capacityplanner.v1beta.IExportForecastsResponse, protos.google.cloud.capacityplanner.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportForecastsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iexportforecastsrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.capacityplanner.v1beta.IExportForecastsResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iexportforecastsresponse), [protos.google.cloud.capacityplanner.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportReservationsUsage(request, options)
    
    
    exportReservationsUsage(request?: protos.google.cloud.capacityplanner.v1beta.IExportReservationsUsageRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.capacityplanner.v1beta.IExportReservationsUsageResponse, protos.google.cloud.capacityplanner.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Exports reservations usage data requested by user into either an existing Cloud Storage bucket or a new/existing BigQuery table.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportReservationsUsageRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iexportreservationsusagerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.capacityplanner.v1beta.IExportReservationsUsageResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iexportreservationsusageresponse), [protos.google.cloud.capacityplanner.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. The machine family to query reservations and usage by. For
       *  example: n1, n2d.
       */
      // const machineFamily = 'abc123'
      /**
       *  Optional. The machine_shape as a filter to select matching reservations
       *  and its usage.
       */
      // const machineShape = {}
      /**
       *  Optional. The GPU type to query reservations and usage  by. For example:
       *  NVIDIA T4.
       */
      // const gpuType = 'abc123'
      /**
       *  Required. The compute engine resource and location of the
       *  reservationsusage. The format is:
       *     projects/{project}/locations/{location} or
       *     organizations/{organization}/locations/{location} or
       *     folders/{folder}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Optional. The location level of the reservations usage timeseries.
       */
      // const locationLevel = {}
      /**
       *  Required. The resource for the `ReservationsUsage` values to return.
       *  Possible values include "gce-vcpus", "gce-ram", "gce-local-ssd", and
       *  "gce-gpu".
       */
      // const cloudResourceType = 'abc123'
      /**
       *  Required. The method that should be used to convert sampled reservations
       *  data to daily usage values.
       */
      // const usageAggregationMethod = {}
      /**
       *  Optional. Type of share settings to filter reservations in response. If
       *  unspecified, all types are included.
       */
      // const shareType = {}
      /**
       *  Optional. The start date of reservations usage.
       */
      // const startDate = {}
      /**
       *  Optional. The end date of reservations usage.
       */
      // const endDate = {}
      /**
       *  Required. Output configuration indicating where the results will be output
       *  to.
       */
      // const outputConfig = {}
    
      // Imports the Capacityplanner library
      const {UsageServiceClient} = require('[@google-cloud/capacityplanner](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const capacityplannerClient = new [UsageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)();
    
      async function callExportReservationsUsage() {
        // Construct request
        const request = {
          parent,
          cloudResourceType,
          usageAggregationMethod,
          outputConfig,
        };
    
        // Run request
        const [operation] = await capacityplannerClient.exportReservationsUsage(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportReservationsUsage();
    
    

### exportReservationsUsage(request, options, callback)
    
    
    exportReservationsUsage(request: protos.google.cloud.capacityplanner.v1beta.IExportReservationsUsageRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.capacityplanner.v1beta.IExportReservationsUsageResponse, protos.google.cloud.capacityplanner.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportReservationsUsageRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iexportreservationsusagerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.capacityplanner.v1beta.IExportReservationsUsageResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iexportreservationsusageresponse), [protos.google.cloud.capacityplanner.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportReservationsUsage(request, callback)
    
    
    exportReservationsUsage(request: protos.google.cloud.capacityplanner.v1beta.IExportReservationsUsageRequest, callback: Callback<LROperation<protos.google.cloud.capacityplanner.v1beta.IExportReservationsUsageResponse, protos.google.cloud.capacityplanner.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportReservationsUsageRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iexportreservationsusagerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.capacityplanner.v1beta.IExportReservationsUsageResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iexportreservationsusageresponse), [protos.google.cloud.capacityplanner.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportUsageHistories(request, options)
    
    
    exportUsageHistories(request?: protos.google.cloud.capacityplanner.v1beta.IExportUsageHistoriesRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.capacityplanner.v1beta.IExportUsageHistoriesResponse, protos.google.cloud.capacityplanner.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Exports historical usage data requested by user into either an existing Cloud Storage bucket or a BigQuery table.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportUsageHistoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iexportusagehistoriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.capacityplanner.v1beta.IExportUsageHistoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iexportusagehistoriesresponse), [protos.google.cloud.capacityplanner.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The compute engine resource and location for the time series
       *  values to return. The format is:
       *     projects/{project}/locations/{location} or
       *     organizations/{organization}/locations/{location} or
       *     folders/{folder}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Optional. Set true to export usage for spot resources.
       */
      // const isSpot = true
      /**
       *  Optional. The machine family for the `UsageHistory` values to return.
       *  Possible values include "n1", and "n2d". See
       *  https://cloud.google.com/compute/docs/machine-types for more examples.
       */
      // const machineFamily = 'abc123'
      /**
       *  Optional. The machine shape for the time series values to export.
       */
      // const machineShape = {}
      /**
       *  Optional. The disk_type for the `UsageHistory` values to return request
       *  with persistent-disk resource_type. Possible values include "pd-ssd",
       *  "pd-standard", "pd-balanced", and "pd-extreme".
       */
      // const diskType = 'abc123'
      /**
       *  Optional. The GPU type for the `UsageHistory` values to return. Sample
       *  values are "nvidia-tesla-t4", and "nvidia-tesla-a100". See
       *  https://cloud.google.com/compute/docs/gpus for a list. Empty gpu_type
       *  will return results matching all GPUs.
       */
      // const gpuType = 'abc123'
      /**
       *  Optional. The TPU type for the `UsageHistory` values to return. Empty
       *  tpu_type will return results matching all TPUs.
       */
      // const tpuType = 'abc123'
      /**
       *  Required. The resource for the `UsageHistory` values to return. Possible
       *  values include "gce-vcpus", "gce-ram", "gce-local-ssd",
       *  "gce-persistent-disk", "gce-gpu" and "gce-tpu".
       */
      // const resourceType = 'abc123'
      /**
       *  Optional. The method that should be used to convert sampled usage data to
       *  daily usage values. AGGREGATION_METHOD_UNSPECIFIED will return results
       *  matching all the aggregation methods.
       */
      // const usageAggregationMethod = {}
      /**
       *  Optional. The start date of usage.
       */
      // const startDate = {}
      /**
       *  Optional. The end date of usage.
       */
      // const endDate = {}
      /**
       *  Required. Output configuration indicating where the results will be output
       *  to.
       */
      // const outputConfig = {}
    
      // Imports the Capacityplanner library
      const {UsageServiceClient} = require('[@google-cloud/capacityplanner](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const capacityplannerClient = new [UsageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)();
    
      async function callExportUsageHistories() {
        // Construct request
        const request = {
          parent,
          resourceType,
          outputConfig,
        };
    
        // Run request
        const [operation] = await capacityplannerClient.exportUsageHistories(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportUsageHistories();
    
    

### exportUsageHistories(request, options, callback)
    
    
    exportUsageHistories(request: protos.google.cloud.capacityplanner.v1beta.IExportUsageHistoriesRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.capacityplanner.v1beta.IExportUsageHistoriesResponse, protos.google.cloud.capacityplanner.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportUsageHistoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iexportusagehistoriesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.capacityplanner.v1beta.IExportUsageHistoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iexportusagehistoriesresponse), [protos.google.cloud.capacityplanner.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportUsageHistories(request, callback)
    
    
    exportUsageHistories(request: protos.google.cloud.capacityplanner.v1beta.IExportUsageHistoriesRequest, callback: Callback<LROperation<protos.google.cloud.capacityplanner.v1beta.IExportUsageHistoriesResponse, protos.google.cloud.capacityplanner.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportUsageHistoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iexportusagehistoriesrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.capacityplanner.v1beta.IExportUsageHistoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iexportusagehistoriesresponse), [protos.google.cloud.capacityplanner.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### folderLocationForecastsPath(folder, location, forecast)
    
    
    folderLocationForecastsPath(folder: string, location: string, forecast: string): string;

Return a fully-qualified folderLocationForecasts resource name string.

**Parameters**  
---  
**Name** | **Description**  
`folder` |  `string`   
  
`location` |  `string`   
  
`forecast` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### folderLocationReservationsPath(folder, location, reservation)
    
    
    folderLocationReservationsPath(folder: string, location: string, reservation: string): string;

Return a fully-qualified folderLocationReservations resource name string.

**Parameters**  
---  
**Name** | **Description**  
`folder` |  `string`   
  
`location` |  `string`   
  
`reservation` |  `string`   
  
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
  
### matchFolderFromFolderLocationForecastsName(folderLocationForecastsName)
    
    
    matchFolderFromFolderLocationForecastsName(folderLocationForecastsName: string): string | number;

Parse the folder from FolderLocationForecasts resource.

**Parameter**  
---  
**Name** | **Description**  
`folderLocationForecastsName` |  `string`   
A fully-qualified path representing folder_location_forecasts resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the folder.  
  
### matchFolderFromFolderLocationReservationsName(folderLocationReservationsName)
    
    
    matchFolderFromFolderLocationReservationsName(folderLocationReservationsName: string): string | number;

Parse the folder from FolderLocationReservations resource.

**Parameter**  
---  
**Name** | **Description**  
`folderLocationReservationsName` |  `string`   
A fully-qualified path representing folder_location_reservations resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the folder.  
  
### matchForecastFromFolderLocationForecastsName(folderLocationForecastsName)
    
    
    matchForecastFromFolderLocationForecastsName(folderLocationForecastsName: string): string | number;

Parse the forecast from FolderLocationForecasts resource.

**Parameter**  
---  
**Name** | **Description**  
`folderLocationForecastsName` |  `string`   
A fully-qualified path representing folder_location_forecasts resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the forecast.  
  
### matchForecastFromOrganizationLocationForecastsName(organizationLocationForecastsName)
    
    
    matchForecastFromOrganizationLocationForecastsName(organizationLocationForecastsName: string): string | number;

Parse the forecast from OrganizationLocationForecasts resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationLocationForecastsName` |  `string`   
A fully-qualified path representing organization_location_forecasts resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the forecast.  
  
### matchForecastFromProjectLocationForecastsName(projectLocationForecastsName)
    
    
    matchForecastFromProjectLocationForecastsName(projectLocationForecastsName: string): string | number;

Parse the forecast from ProjectLocationForecasts resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationForecastsName` |  `string`   
A fully-qualified path representing project_location_forecasts resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the forecast.  
  
### matchLocationFromFolderLocationForecastsName(folderLocationForecastsName)
    
    
    matchLocationFromFolderLocationForecastsName(folderLocationForecastsName: string): string | number;

Parse the location from FolderLocationForecasts resource.

**Parameter**  
---  
**Name** | **Description**  
`folderLocationForecastsName` |  `string`   
A fully-qualified path representing folder_location_forecasts resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromFolderLocationReservationsName(folderLocationReservationsName)
    
    
    matchLocationFromFolderLocationReservationsName(folderLocationReservationsName: string): string | number;

Parse the location from FolderLocationReservations resource.

**Parameter**  
---  
**Name** | **Description**  
`folderLocationReservationsName` |  `string`   
A fully-qualified path representing folder_location_reservations resource.  
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
  
### matchLocationFromOrganizationLocationForecastsName(organizationLocationForecastsName)
    
    
    matchLocationFromOrganizationLocationForecastsName(organizationLocationForecastsName: string): string | number;

Parse the location from OrganizationLocationForecasts resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationLocationForecastsName` |  `string`   
A fully-qualified path representing organization_location_forecasts resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromOrganizationLocationReservationsName(organizationLocationReservationsName)
    
    
    matchLocationFromOrganizationLocationReservationsName(organizationLocationReservationsName: string): string | number;

Parse the location from OrganizationLocationReservations resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationLocationReservationsName` |  `string`   
A fully-qualified path representing organization_location_reservations resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationForecastsName(projectLocationForecastsName)
    
    
    matchLocationFromProjectLocationForecastsName(projectLocationForecastsName: string): string | number;

Parse the location from ProjectLocationForecasts resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationForecastsName` |  `string`   
A fully-qualified path representing project_location_forecasts resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationReservationsName(projectLocationReservationsName)
    
    
    matchLocationFromProjectLocationReservationsName(projectLocationReservationsName: string): string | number;

Parse the location from ProjectLocationReservations resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationReservationsName` |  `string`   
A fully-qualified path representing project_location_reservations resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchOrganizationFromOrganizationLocationForecastsName(organizationLocationForecastsName)
    
    
    matchOrganizationFromOrganizationLocationForecastsName(organizationLocationForecastsName: string): string | number;

Parse the organization from OrganizationLocationForecasts resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationLocationForecastsName` |  `string`   
A fully-qualified path representing organization_location_forecasts resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the organization.  
  
### matchOrganizationFromOrganizationLocationReservationsName(organizationLocationReservationsName)
    
    
    matchOrganizationFromOrganizationLocationReservationsName(organizationLocationReservationsName: string): string | number;

Parse the organization from OrganizationLocationReservations resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationLocationReservationsName` |  `string`   
A fully-qualified path representing organization_location_reservations resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the organization.  
  
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
  
### matchProjectFromProjectLocationForecastsName(projectLocationForecastsName)
    
    
    matchProjectFromProjectLocationForecastsName(projectLocationForecastsName: string): string | number;

Parse the project from ProjectLocationForecasts resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationForecastsName` |  `string`   
A fully-qualified path representing project_location_forecasts resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationReservationsName(projectLocationReservationsName)
    
    
    matchProjectFromProjectLocationReservationsName(projectLocationReservationsName: string): string | number;

Parse the project from ProjectLocationReservations resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationReservationsName` |  `string`   
A fully-qualified path representing project_location_reservations resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchReservationFromFolderLocationReservationsName(folderLocationReservationsName)
    
    
    matchReservationFromFolderLocationReservationsName(folderLocationReservationsName: string): string | number;

Parse the reservation from FolderLocationReservations resource.

**Parameter**  
---  
**Name** | **Description**  
`folderLocationReservationsName` |  `string`   
A fully-qualified path representing folder_location_reservations resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the reservation.  
  
### matchReservationFromOrganizationLocationReservationsName(organizationLocationReservationsName)
    
    
    matchReservationFromOrganizationLocationReservationsName(organizationLocationReservationsName: string): string | number;

Parse the reservation from OrganizationLocationReservations resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationLocationReservationsName` |  `string`   
A fully-qualified path representing organization_location_reservations resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the reservation.  
  
### matchReservationFromProjectLocationReservationsName(projectLocationReservationsName)
    
    
    matchReservationFromProjectLocationReservationsName(projectLocationReservationsName: string): string | number;

Parse the reservation from ProjectLocationReservations resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationReservationsName` |  `string`   
A fully-qualified path representing project_location_reservations resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the reservation.  
  
### organizationLocationForecastsPath(organization, location, forecast)
    
    
    organizationLocationForecastsPath(organization: string, location: string, forecast: string): string;

Return a fully-qualified organizationLocationForecasts resource name string.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`location` |  `string`   
  
`forecast` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### organizationLocationReservationsPath(organization, location, reservation)
    
    
    organizationLocationReservationsPath(organization: string, location: string, reservation: string): string;

Return a fully-qualified organizationLocationReservations resource name string.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`location` |  `string`   
  
`reservation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationForecastsPath(project, location, forecast)
    
    
    projectLocationForecastsPath(project: string, location: string, forecast: string): string;

Return a fully-qualified projectLocationForecasts resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`forecast` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationReservationsPath(project, location, reservation)
    
    
    projectLocationReservationsPath(project: string, location: string, reservation: string): string;

Return a fully-qualified projectLocationReservations resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`reservation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### queryForecasts(request, options)
    
    
    queryForecasts(request?: protos.google.cloud.capacityplanner.v1beta.IQueryForecastsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.capacityplanner.v1beta.IQueryForecastsResponse,
            (protos.google.cloud.capacityplanner.v1beta.IQueryForecastsRequest | undefined),
            {} | undefined
        ]>;

Returns a list of the forecasts that are in the parent parameter and match your specified filters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryForecastsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryforecastsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.capacityplanner.v1beta.IQueryForecastsResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryforecastsresponse), ([protos.google.cloud.capacityplanner.v1beta.IQueryForecastsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryforecastsrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [QueryForecastsResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.queryforecastsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The compute engine resource and location for the time series
       *  values to return. The format is:
       *  projects/{project}/locations/{location} or
       *  organizations/{organization}/locations/{location} or
       *  folders/{folder}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  The machine family to use to select the `Forecast` values to return.
       *  Possible values include "n1", and "n2d".
       *  Empty machine_family will return results matching all machine families.
       */
      // const machineFamily = 'abc123'
      /**
       *  Optional. The machine shape for the time series values to return.
       */
      // const machineShape = {}
      /**
       *  Optional. The disk_type for the `Forecast` values to return with request
       *  persistent-disk cloud_resource_type.
       *  Empty disk_type will return results matching all disk types.
       */
      // const diskType = 'abc123'
      /**
       *  Optional. Whether the persistent disk is in confidential mode.
       */
      // const confidentialMode = true
      /**
       *  Optional. The GPU type for the `Forecast` values to return. Sample values
       *  are "nvidia-tesla-t4", and "nvidia-tesla-a100". See
       *  https://cloud.google.com/compute/docs/gpus for a list. Empty gpu_type
       *  will return results matching all GPUs.
       */
      // const gpuType = 'abc123'
      /**
       *  Optional. The TPU type for the `Forecast` values to return. Empty tpu_type
       *  will return results matching all TPUs.
       */
      // const tpuType = 'abc123'
      /**
       *  Required. The resource for the `Forecast` values to return. Possible values
       *  include "gce-vcpus", "gce-ram", "gce-local-ssd", "gce-persistent-disk",
       *  "gce-gpu" and "gce-tpu". Empty cloud_resource_type will return results
       *  matching all resources.
       */
      // const cloudResourceType = 'abc123'
      /**
       *  The type of forecast to use to select the `Forecast` values to return.
       *  FORECAST_TYPE_UNSPECIFIED will return results matching all the forecast
       *  types.
       */
      // const forecastType = {}
      /**
       *  The prediction interval to use to select the `Forecast` values to return.
       *  PREDICTION_INTERVAL_UNSPECIFIED will return results matching all prediction
       *  intervals.
       */
      // const predictionInterval = {}
      /**
       *  Aggregation Method of the historical usage for which the forecast is
       *  generated
       */
      // const aggregationMethod = {}
    
      // Imports the Capacityplanner library
      const {UsageServiceClient} = require('[@google-cloud/capacityplanner](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const capacityplannerClient = new [UsageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)();
    
      async function callQueryForecasts() {
        // Construct request
        const request = {
          parent,
          cloudResourceType,
        };
    
        // Run request
        const response = await capacityplannerClient.queryForecasts(request);
        console.log(response);
      }
    
      callQueryForecasts();
    
    

### queryForecasts(request, options, callback)
    
    
    queryForecasts(request: protos.google.cloud.capacityplanner.v1beta.IQueryForecastsRequest, options: CallOptions, callback: Callback<protos.google.cloud.capacityplanner.v1beta.IQueryForecastsResponse, protos.google.cloud.capacityplanner.v1beta.IQueryForecastsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryForecastsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryforecastsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.capacityplanner.v1beta.IQueryForecastsResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryforecastsresponse), [protos.google.cloud.capacityplanner.v1beta.IQueryForecastsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryforecastsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryForecasts(request, callback)
    
    
    queryForecasts(request: protos.google.cloud.capacityplanner.v1beta.IQueryForecastsRequest, callback: Callback<protos.google.cloud.capacityplanner.v1beta.IQueryForecastsResponse, protos.google.cloud.capacityplanner.v1beta.IQueryForecastsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryForecastsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryforecastsrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.capacityplanner.v1beta.IQueryForecastsResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryforecastsresponse), [protos.google.cloud.capacityplanner.v1beta.IQueryForecastsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryforecastsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryReservations(request, options)
    
    
    queryReservations(request?: protos.google.cloud.capacityplanner.v1beta.IQueryReservationsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.capacityplanner.v1beta.IQueryReservationsResponse,
            (protos.google.cloud.capacityplanner.v1beta.IQueryReservationsRequest | undefined),
            {} | undefined
        ]>;

Returns a list of the reservations that are in the parent parameter and match your specified filters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryReservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryreservationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.capacityplanner.v1beta.IQueryReservationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryreservationsresponse), ([protos.google.cloud.capacityplanner.v1beta.IQueryReservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryreservationsrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [QueryReservationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.queryreservationsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The compute engine resource and location for the time series
       *  values to return. The format is:
       *  projects/{project}/locations/{location} or
       *  organizations/{organization}/locations/{location} or
       *  folders/{folder}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Optional. The location level of the reservations usage timeseries.
       */
      // const locationLevel = {}
      /**
       *  Optional. The machine family to use to select the aggregate reserved values
       *  to return. Possible values include "n1", and "n2d" etc. Empty
       *  machine_family will return results matching all machine families.
       */
      // const machineFamily = 'abc123'
      /**
       *  Optional. The machine_shape as a filter to select matching reservations.
       */
      // const machineShape = {}
      /**
       *  Optional. The GPU type for the reserved values to return. Sample values
       *  are "nvidia-tesla-t4", and "nvidia-tesla-a100". See
       *  https://cloud.google.com/compute/docs/gpus for a list. Empty gpu_type
       *  will return results matching all GPUs.
       */
      // const gpuType = 'abc123'
      /**
       *  Required. The resource for the reserved values to return. Possible values
       *  include "gce-vcpus", "gce-ram", "gce-local-ssd", "gce-gpu" and "gce-vm".
       */
      // const cloudResourceType = 'abc123'
      /**
       *  Required. The Reservation type for example, future reservation request and
       *  allocation. If unspecified, all types are
       *  included.
       */
      // const reservationType = {}
      /**
       *  Optional. Types of share settings to filter reservations in response. If
       *  unspecified, all types are included.
       */
      // const shareType = {}
      /**
       *  Optional. Types of ownerships to filter reservations based on.
       *  In case of OWNED, it filters reservations which are owned by selected
       *  parent project/folder/organization. If unspecified, all types are
       *  included.
       */
      // const ownershipType = {}
      /**
       *  Required. Reservations output data format.
       */
      // const reservationDataLevel = {}
      /**
       *  Optional. Whether to include pending for approval reservations in the
       *  response. This field is only applicable for future reservations.
       */
      // const includeUnapprovedReservations = true
      /**
       *  Optional. Aggregation Method of the historical reservation usage
       */
      // const aggregationMethod = {}
      /**
       *  Optional. The start date of reservations usage.
       */
      // const startDate = {}
      /**
       *  Optional. The end date of reservations usage.
       */
      // const endDate = {}
    
      // Imports the Capacityplanner library
      const {UsageServiceClient} = require('[@google-cloud/capacityplanner](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const capacityplannerClient = new [UsageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)();
    
      async function callQueryReservations() {
        // Construct request
        const request = {
          parent,
          cloudResourceType,
          reservationType,
          reservationDataLevel,
        };
    
        // Run request
        const response = await capacityplannerClient.queryReservations(request);
        console.log(response);
      }
    
      callQueryReservations();
    
    

### queryReservations(request, options, callback)
    
    
    queryReservations(request: protos.google.cloud.capacityplanner.v1beta.IQueryReservationsRequest, options: CallOptions, callback: Callback<protos.google.cloud.capacityplanner.v1beta.IQueryReservationsResponse, protos.google.cloud.capacityplanner.v1beta.IQueryReservationsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryReservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryreservationsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.capacityplanner.v1beta.IQueryReservationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryreservationsresponse), [protos.google.cloud.capacityplanner.v1beta.IQueryReservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryreservationsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryReservations(request, callback)
    
    
    queryReservations(request: protos.google.cloud.capacityplanner.v1beta.IQueryReservationsRequest, callback: Callback<protos.google.cloud.capacityplanner.v1beta.IQueryReservationsResponse, protos.google.cloud.capacityplanner.v1beta.IQueryReservationsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryReservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryreservationsrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.capacityplanner.v1beta.IQueryReservationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryreservationsresponse), [protos.google.cloud.capacityplanner.v1beta.IQueryReservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryreservationsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryUsageHistories(request, options)
    
    
    queryUsageHistories(request?: protos.google.cloud.capacityplanner.v1beta.IQueryUsageHistoriesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.capacityplanner.v1beta.IQueryUsageHistoriesResponse,
            (protos.google.cloud.capacityplanner.v1beta.IQueryUsageHistoriesRequest | undefined),
            {} | undefined
        ]>;

Returns a list of the usage histories that are in the parent parameter and match your specified filters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryUsageHistoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryusagehistoriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.capacityplanner.v1beta.IQueryUsageHistoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryusagehistoriesresponse), ([protos.google.cloud.capacityplanner.v1beta.IQueryUsageHistoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryusagehistoriesrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [QueryUsageHistoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.queryusagehistoriesresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The compute engine resource and location for the time series
       *  values to return. The format is:
       *      projects/{project}/locations/{location} or
       *      organizations/{organization}/locations/{location} or
       *      folders/{folder}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Optional. The location level of the reservations usage timeseries.
       */
      // const locationLevel = {}
      /**
       *  Optional. The is_spot flag is used to fetch the usage data for preemptible
       *  Resources.
       */
      // const isSpot = true
      /**
       *  The machine family for the `UsageHistory` values to return. Possible values
       *  include "n1", and "n2d". See
       *  https://cloud.google.com/compute/docs/machine-types for more examples.
       *  Empty machine_family will return results matching all machine families.
       */
      // const machineFamily = 'abc123'
      /**
       *  Optional. The machine shape for the `UsageHistory` values to return.
       */
      // const machineShape = {}
      /**
       *  Optional. The disk_type for the `UsageHistory` values to return request
       *  with persistent-disk cloud_resource_type. Empty disk_type will return
       *  results matching all disk types.
       */
      // const diskType = 'abc123'
      /**
       *  Optional. Whether the persistent disk is in confidential mode.
       */
      // const confidentialMode = true
      /**
       *  Optional. The GPU type for the `UsageHistory` values to return. Sample
       *  values are "nvidia-tesla-t4", and "nvidia-tesla-a100". See
       *  https://cloud.google.com/compute/docs/gpus for a list. Empty gpu_type
       *  will return results matching all GPUs.
       */
      // const gpuType = 'abc123'
      /**
       *  Optional. The TPU type for the `UsageHistory` values to return. Empty
       *  tpu_type will return results matching all TPUs.
       */
      // const tpuType = 'abc123'
      /**
       *  Required. The resource for the `UsageHistory` values to return. Possible
       *  values include "gce-vcpus", "gce-ram", "gce-local-ssd",
       *  "gce-persistent-disk", "gce-gpu" and "gce-tpu". Empty cloud_resource_type
       *  will return results matching all resources.
       */
      // const cloudResourceType = 'abc123'
      /**
       *  The method that should be used to convert sampled usage data to daily
       *  usage values.
       *  AGGREGATION_METHOD_UNSPECIFIED will return results matching all the
       *  aggregation methods.
       */
      // const usageAggregationMethod = {}
      /**
       *  Optional. The start date of reservations usage.
       */
      // const startDate = {}
      /**
       *  Optional. The end date of reservations usage.
       */
      // const endDate = {}
    
      // Imports the Capacityplanner library
      const {UsageServiceClient} = require('[@google-cloud/capacityplanner](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const capacityplannerClient = new [UsageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)();
    
      async function callQueryUsageHistories() {
        // Construct request
        const request = {
          parent,
          cloudResourceType,
        };
    
        // Run request
        const response = await capacityplannerClient.queryUsageHistories(request);
        console.log(response);
      }
    
      callQueryUsageHistories();
    
    

### queryUsageHistories(request, options, callback)
    
    
    queryUsageHistories(request: protos.google.cloud.capacityplanner.v1beta.IQueryUsageHistoriesRequest, options: CallOptions, callback: Callback<protos.google.cloud.capacityplanner.v1beta.IQueryUsageHistoriesResponse, protos.google.cloud.capacityplanner.v1beta.IQueryUsageHistoriesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryUsageHistoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryusagehistoriesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.capacityplanner.v1beta.IQueryUsageHistoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryusagehistoriesresponse), [protos.google.cloud.capacityplanner.v1beta.IQueryUsageHistoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryusagehistoriesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryUsageHistories(request, callback)
    
    
    queryUsageHistories(request: protos.google.cloud.capacityplanner.v1beta.IQueryUsageHistoriesRequest, callback: Callback<protos.google.cloud.capacityplanner.v1beta.IQueryUsageHistoriesResponse, protos.google.cloud.capacityplanner.v1beta.IQueryUsageHistoriesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryUsageHistoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryusagehistoriesrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.capacityplanner.v1beta.IQueryUsageHistoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryusagehistoriesresponse), [protos.google.cloud.capacityplanner.v1beta.IQueryUsageHistoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryusagehistoriesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
