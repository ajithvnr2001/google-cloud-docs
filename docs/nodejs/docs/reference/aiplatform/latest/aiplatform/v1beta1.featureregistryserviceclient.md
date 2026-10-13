---
url: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/v1beta1.featureregistryserviceclient
title: Class v1beta1.FeatureRegistryServiceClient (7.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:12:45.462147+00:00
---

# Class v1beta1.FeatureRegistryServiceClient (7.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/v1beta1.featureregistryserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.FeatureRegistryServiceClient (7.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.4.1 (latest)  7.3.0  6.10.0  6.9.0  6.8.1  6.6.0  6.4.0  6.3.0  6.2.0  6.1.0  6.0.0  5.14.0  5.13.0  3.15.0  3.13.0  3.11.0  3.10.1  3.9.0  3.7.0  3.6.0  3.4.0  3.3.0  3.0.0  2.12.0  2.11.0  2.10.0  2.7.0  2.6.1  2.5.0  2.3.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0  1.11.0  1.7.2 

The service that handles CRUD and List for resources for FeatureRegistry. v1beta1

## Package

[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of FeatureRegistryServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new FeatureRegistryServiceClient({fallback: true}, gax); ```  
  
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

### featureRegistryServiceStub
    
    
    featureRegistryServiceStub?: Promise<{
            [name: string]: Function;
        }>;

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
  
### batchCreateFeatures(request, options)
    
    
    batchCreateFeatures(request?: protos.google.cloud.aiplatform.v1beta1.IBatchCreateFeaturesRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.aiplatform.v1beta1.IBatchCreateFeaturesResponse, protos.google.cloud.aiplatform.v1beta1.IBatchCreateFeaturesOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a batch of Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatefeaturesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.aiplatform.v1beta1.IBatchCreateFeaturesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatefeaturesresponse), [protos.google.cloud.aiplatform.v1beta1.IBatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatefeaturesoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the EntityType/FeatureGroup to create the
       *  batch of Features under. Format:
       *  `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}`
       *  `projects/{project}/locations/{location}/featureGroups/{feature_group}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The request message specifying the Features to create. All
       *  Features must be created under the same parent EntityType / FeatureGroup.
       *  The `parent` field in each child request message can be omitted. If
       *  `parent` is set in a child request, then the value must match the `parent`
       *  value in this request message.
       */
      // const requests = [1,2,3,4]
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callBatchCreateFeatures() {
        // Construct request
        const request = {
          parent,
          requests,
        };
    
        // Run request
        const [operation] = await aiplatformClient.batchCreateFeatures(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callBatchCreateFeatures();
    
    

### batchCreateFeatures(request, options, callback)
    
    
    batchCreateFeatures(request: protos.google.cloud.aiplatform.v1beta1.IBatchCreateFeaturesRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IBatchCreateFeaturesResponse, protos.google.cloud.aiplatform.v1beta1.IBatchCreateFeaturesOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatefeaturesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IBatchCreateFeaturesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatefeaturesresponse), [protos.google.cloud.aiplatform.v1beta1.IBatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatefeaturesoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateFeatures(request, callback)
    
    
    batchCreateFeatures(request: protos.google.cloud.aiplatform.v1beta1.IBatchCreateFeaturesRequest, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IBatchCreateFeaturesResponse, protos.google.cloud.aiplatform.v1beta1.IBatchCreateFeaturesOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatefeaturesrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IBatchCreateFeaturesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatefeaturesresponse), [protos.google.cloud.aiplatform.v1beta1.IBatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ibatchcreatefeaturesoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
    

### checkBatchCreateFeaturesProgress(name)
    
    
    checkBatchCreateFeaturesProgress(name: string): Promise<LROperation<protos.google.cloud.aiplatform.v1beta1.BatchCreateFeaturesResponse, protos.google.cloud.aiplatform.v1beta1.BatchCreateFeaturesOperationMetadata>>;

Check the status of the long running operation returned by `batchCreateFeatures()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.aiplatform.v1beta1.BatchCreateFeaturesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.batchcreatefeaturesresponse), [protos.google.cloud.aiplatform.v1beta1.BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.batchcreatefeaturesoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the EntityType/FeatureGroup to create the
       *  batch of Features under. Format:
       *  `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}`
       *  `projects/{project}/locations/{location}/featureGroups/{feature_group}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The request message specifying the Features to create. All
       *  Features must be created under the same parent EntityType / FeatureGroup.
       *  The `parent` field in each child request message can be omitted. If
       *  `parent` is set in a child request, then the value must match the `parent`
       *  value in this request message.
       */
      // const requests = [1,2,3,4]
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callBatchCreateFeatures() {
        // Construct request
        const request = {
          parent,
          requests,
        };
    
        // Run request
        const [operation] = await aiplatformClient.batchCreateFeatures(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callBatchCreateFeatures();
    
    

### checkCreateFeatureGroupProgress(name)
    
    
    checkCreateFeatureGroupProgress(name: string): Promise<LROperation<protos.google.cloud.aiplatform.v1beta1.FeatureGroup, protos.google.cloud.aiplatform.v1beta1.CreateFeatureGroupOperationMetadata>>;

Check the status of the long running operation returned by `createFeatureGroup()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.aiplatform.v1beta1.FeatureGroup](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featuregroup-class), [protos.google.cloud.aiplatform.v1beta1.CreateFeatureGroupOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.createfeaturegroupoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Location to create FeatureGroups.
       *  Format:
       *  `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The FeatureGroup to create.
       */
      // const featureGroup = {}
      /**
       *  Required. The ID to use for this FeatureGroup, which will become the final
       *  component of the FeatureGroup's resource name.
       *  This value may be up to 128 characters, and valid characters are
       *  `[a-z0-9_]`. The first character cannot be a number.
       *  The value must be unique within the project and location.
       */
      // const featureGroupId = 'abc123'
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callCreateFeatureGroup() {
        // Construct request
        const request = {
          parent,
          featureGroup,
          featureGroupId,
        };
    
        // Run request
        const [operation] = await aiplatformClient.createFeatureGroup(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateFeatureGroup();
    
    

### checkCreateFeatureMonitorProgress(name)
    
    
    checkCreateFeatureMonitorProgress(name: string): Promise<LROperation<protos.google.cloud.aiplatform.v1beta1.FeatureMonitor, protos.google.cloud.aiplatform.v1beta1.CreateFeatureMonitorOperationMetadata>>;

Check the status of the long running operation returned by `createFeatureMonitor()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.aiplatform.v1beta1.FeatureMonitor](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featuremonitor), [protos.google.cloud.aiplatform.v1beta1.CreateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.createfeaturemonitoroperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of FeatureGroup to create FeatureMonitor.
       *  Format:
       *  `projects/{project}/locations/{location}/featureGroups/{featuregroup}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The Monitor to create.
       */
      // const featureMonitor = {}
      /**
       *  Required. The ID to use for this FeatureMonitor, which will become the
       *  final component of the FeatureGroup's resource name.
       *  This value may be up to 60 characters, and valid characters are
       *  `[a-z0-9_]`. The first character cannot be a number.
       *  The value must be unique within the FeatureGroup.
       */
      // const featureMonitorId = 'abc123'
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callCreateFeatureMonitor() {
        // Construct request
        const request = {
          parent,
          featureMonitor,
          featureMonitorId,
        };
    
        // Run request
        const [operation] = await aiplatformClient.createFeatureMonitor(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateFeatureMonitor();
    
    

### checkCreateFeatureProgress(name)
    
    
    checkCreateFeatureProgress(name: string): Promise<LROperation<protos.google.cloud.aiplatform.v1beta1.Feature, protos.google.cloud.aiplatform.v1beta1.CreateFeatureOperationMetadata>>;

Check the status of the long running operation returned by `createFeature()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.aiplatform.v1beta1.Feature](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.feature-class), [protos.google.cloud.aiplatform.v1beta1.CreateFeatureOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.createfeatureoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the EntityType or FeatureGroup to create a
       *  Feature. Format for entity_type as parent:
       *  `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}`
       *  Format for feature_group as parent:
       *  `projects/{project}/locations/{location}/featureGroups/{feature_group}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The Feature to create.
       */
      // const feature = {}
      /**
       *  Required. The ID to use for the Feature, which will become the final
       *  component of the Feature's resource name.
       *  This value may be up to 128 characters, and valid characters are
       *  `[a-z0-9_]`. The first character cannot be a number.
       *  The value must be unique within an EntityType/FeatureGroup.
       */
      // const featureId = 'abc123'
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callCreateFeature() {
        // Construct request
        const request = {
          parent,
          feature,
          featureId,
        };
    
        // Run request
        const [operation] = await aiplatformClient.createFeature(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateFeature();
    
    

### checkDeleteFeatureGroupProgress(name)
    
    
    checkDeleteFeatureGroupProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata>>;

Check the status of the long running operation returned by `deleteFeatureGroup()`.

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
       *  Required. The name of the FeatureGroup to be deleted.
       *  Format:
       *  `projects/{project}/locations/{location}/featureGroups/{feature_group}`
       */
      // const name = 'abc123'
      /**
       *  If set to true, any Features under this FeatureGroup
       *  will also be deleted. (Otherwise, the request will only work if the
       *  FeatureGroup has no Features.)
       */
      // const force = true
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteFeatureGroup() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.deleteFeatureGroup(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteFeatureGroup();
    
    

### checkDeleteFeatureMonitorProgress(name)
    
    
    checkDeleteFeatureMonitorProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata>>;

Check the status of the long running operation returned by `deleteFeatureMonitor()`.

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
       *  Required. The name of the FeatureMonitor to be deleted.
       *  Format:
       *  `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteFeatureMonitor() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.deleteFeatureMonitor(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteFeatureMonitor();
    
    

### checkDeleteFeatureProgress(name)
    
    
    checkDeleteFeatureProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.aiplatform.v1beta1.DeleteOperationMetadata>>;

Check the status of the long running operation returned by `deleteFeature()`.

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
       *  Required. The name of the Features to be deleted.
       *  Format:
       *  `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}`
       *  `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteFeature() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.deleteFeature(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteFeature();
    
    

### checkUpdateFeatureGroupProgress(name)
    
    
    checkUpdateFeatureGroupProgress(name: string): Promise<LROperation<protos.google.cloud.aiplatform.v1beta1.FeatureGroup, protos.google.cloud.aiplatform.v1beta1.UpdateFeatureGroupOperationMetadata>>;

Check the status of the long running operation returned by `updateFeatureGroup()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.aiplatform.v1beta1.FeatureGroup](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featuregroup-class), [protos.google.cloud.aiplatform.v1beta1.UpdateFeatureGroupOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.updatefeaturegroupoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The FeatureGroup's `name` field is used to identify the
       *  FeatureGroup to be updated. Format:
       *  `projects/{project}/locations/{location}/featureGroups/{feature_group}`
       */
      // const featureGroup = {}
      /**
       *  Field mask is used to specify the fields to be overwritten in the
       *  FeatureGroup resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then only the non-empty fields present in the
       *  request will be overwritten. Set the update_mask to `*` to override all
       *  fields.
       *  Updatable fields:
       *    * `labels`
       *    * `description`
       *    * `big_query`
       *    * `big_query.entity_id_columns`
       */
      // const updateMask = {}
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callUpdateFeatureGroup() {
        // Construct request
        const request = {
          featureGroup,
        };
    
        // Run request
        const [operation] = await aiplatformClient.updateFeatureGroup(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateFeatureGroup();
    
    

### checkUpdateFeatureMonitorProgress(name)
    
    
    checkUpdateFeatureMonitorProgress(name: string): Promise<LROperation<protos.google.cloud.aiplatform.v1beta1.FeatureMonitor, protos.google.cloud.aiplatform.v1beta1.UpdateFeatureMonitorOperationMetadata>>;

Check the status of the long running operation returned by `updateFeatureMonitor()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.aiplatform.v1beta1.FeatureMonitor](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featuremonitor), [protos.google.cloud.aiplatform.v1beta1.UpdateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.updatefeaturemonitoroperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The FeatureMonitor's `name` field is used to identify the
       *  FeatureMonitor to be updated. Format:
       *  `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`
       */
      // const featureMonitor = {}
      /**
       *  Optional. Field mask is used to specify the fields to be overwritten in the
       *  FeatureMonitor resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then only the non-empty fields present in the
       *  request will be overwritten. Set the update_mask to `*` to override all
       *  fields.
       *  Updatable fields:
       *    * `labels`
       */
      // const updateMask = {}
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callUpdateFeatureMonitor() {
        // Construct request
        const request = {
          featureMonitor,
        };
    
        // Run request
        const [operation] = await aiplatformClient.updateFeatureMonitor(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateFeatureMonitor();
    
    

### checkUpdateFeatureProgress(name)
    
    
    checkUpdateFeatureProgress(name: string): Promise<LROperation<protos.google.cloud.aiplatform.v1beta1.Feature, protos.google.cloud.aiplatform.v1beta1.UpdateFeatureOperationMetadata>>;

Check the status of the long running operation returned by `updateFeature()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.aiplatform.v1beta1.Feature](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.feature-class), [protos.google.cloud.aiplatform.v1beta1.UpdateFeatureOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.updatefeatureoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Feature's `name` field is used to identify the Feature to be
       *  updated.
       *  Format:
       *  `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}`
       *  `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}`
       */
      // const feature = {}
      /**
       *  Field mask is used to specify the fields to be overwritten in the
       *  Features resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then only the non-empty fields present in the
       *  request will be overwritten. Set the update_mask to `*` to override all
       *  fields.
       *  Updatable fields:
       *    * `description`
       *    * `labels`
       *    * `disable_monitoring` (Not supported for FeatureRegistryService Feature)
       *    * `point_of_contact` (Not supported for FeaturestoreService FeatureStore)
       */
      // const updateMask = {}
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callUpdateFeature() {
        // Construct request
        const request = {
          feature,
        };
    
        // Run request
        const [operation] = await aiplatformClient.updateFeature(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateFeature();
    
    

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
  
### createFeature(request, options)
    
    
    createFeature(request?: protos.google.cloud.aiplatform.v1beta1.ICreateFeatureRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.aiplatform.v1beta1.IFeature, protos.google.cloud.aiplatform.v1beta1.ICreateFeatureOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new Feature in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.aiplatform.v1beta1.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeature), [protos.google.cloud.aiplatform.v1beta1.ICreateFeatureOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeatureoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the EntityType or FeatureGroup to create a
       *  Feature. Format for entity_type as parent:
       *  `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}`
       *  Format for feature_group as parent:
       *  `projects/{project}/locations/{location}/featureGroups/{feature_group}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The Feature to create.
       */
      // const feature = {}
      /**
       *  Required. The ID to use for the Feature, which will become the final
       *  component of the Feature's resource name.
       *  This value may be up to 128 characters, and valid characters are
       *  `[a-z0-9_]`. The first character cannot be a number.
       *  The value must be unique within an EntityType/FeatureGroup.
       */
      // const featureId = 'abc123'
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callCreateFeature() {
        // Construct request
        const request = {
          parent,
          feature,
          featureId,
        };
    
        // Run request
        const [operation] = await aiplatformClient.createFeature(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateFeature();
    
    

### createFeature(request, options, callback)
    
    
    createFeature(request: protos.google.cloud.aiplatform.v1beta1.ICreateFeatureRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IFeature, protos.google.cloud.aiplatform.v1beta1.ICreateFeatureOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeature), [protos.google.cloud.aiplatform.v1beta1.ICreateFeatureOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeatureoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFeature(request, callback)
    
    
    createFeature(request: protos.google.cloud.aiplatform.v1beta1.ICreateFeatureRequest, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IFeature, protos.google.cloud.aiplatform.v1beta1.ICreateFeatureOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeature), [protos.google.cloud.aiplatform.v1beta1.ICreateFeatureOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeatureoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFeatureGroup(request, options)
    
    
    createFeatureGroup(request?: protos.google.cloud.aiplatform.v1beta1.ICreateFeatureGroupRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.aiplatform.v1beta1.IFeatureGroup, protos.google.cloud.aiplatform.v1beta1.ICreateFeatureGroupOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new FeatureGroup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeatureGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturegrouprequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.aiplatform.v1beta1.IFeatureGroup](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturegroup), [protos.google.cloud.aiplatform.v1beta1.ICreateFeatureGroupOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturegroupoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Location to create FeatureGroups.
       *  Format:
       *  `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The FeatureGroup to create.
       */
      // const featureGroup = {}
      /**
       *  Required. The ID to use for this FeatureGroup, which will become the final
       *  component of the FeatureGroup's resource name.
       *  This value may be up to 128 characters, and valid characters are
       *  `[a-z0-9_]`. The first character cannot be a number.
       *  The value must be unique within the project and location.
       */
      // const featureGroupId = 'abc123'
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callCreateFeatureGroup() {
        // Construct request
        const request = {
          parent,
          featureGroup,
          featureGroupId,
        };
    
        // Run request
        const [operation] = await aiplatformClient.createFeatureGroup(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateFeatureGroup();
    
    

### createFeatureGroup(request, options, callback)
    
    
    createFeatureGroup(request: protos.google.cloud.aiplatform.v1beta1.ICreateFeatureGroupRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IFeatureGroup, protos.google.cloud.aiplatform.v1beta1.ICreateFeatureGroupOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeatureGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturegrouprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IFeatureGroup](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturegroup), [protos.google.cloud.aiplatform.v1beta1.ICreateFeatureGroupOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturegroupoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFeatureGroup(request, callback)
    
    
    createFeatureGroup(request: protos.google.cloud.aiplatform.v1beta1.ICreateFeatureGroupRequest, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IFeatureGroup, protos.google.cloud.aiplatform.v1beta1.ICreateFeatureGroupOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeatureGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturegrouprequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IFeatureGroup](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturegroup), [protos.google.cloud.aiplatform.v1beta1.ICreateFeatureGroupOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturegroupoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFeatureMonitor(request, options)
    
    
    createFeatureMonitor(request?: protos.google.cloud.aiplatform.v1beta1.ICreateFeatureMonitorRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor, protos.google.cloud.aiplatform.v1beta1.ICreateFeatureMonitorOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new FeatureMonitor in a given project, location and FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeatureMonitorRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturemonitorrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitor), [protos.google.cloud.aiplatform.v1beta1.ICreateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturemonitoroperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of FeatureGroup to create FeatureMonitor.
       *  Format:
       *  `projects/{project}/locations/{location}/featureGroups/{featuregroup}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The Monitor to create.
       */
      // const featureMonitor = {}
      /**
       *  Required. The ID to use for this FeatureMonitor, which will become the
       *  final component of the FeatureGroup's resource name.
       *  This value may be up to 60 characters, and valid characters are
       *  `[a-z0-9_]`. The first character cannot be a number.
       *  The value must be unique within the FeatureGroup.
       */
      // const featureMonitorId = 'abc123'
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callCreateFeatureMonitor() {
        // Construct request
        const request = {
          parent,
          featureMonitor,
          featureMonitorId,
        };
    
        // Run request
        const [operation] = await aiplatformClient.createFeatureMonitor(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateFeatureMonitor();
    
    

### createFeatureMonitor(request, options, callback)
    
    
    createFeatureMonitor(request: protos.google.cloud.aiplatform.v1beta1.ICreateFeatureMonitorRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor, protos.google.cloud.aiplatform.v1beta1.ICreateFeatureMonitorOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeatureMonitorRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturemonitorrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitor), [protos.google.cloud.aiplatform.v1beta1.ICreateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturemonitoroperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFeatureMonitor(request, callback)
    
    
    createFeatureMonitor(request: protos.google.cloud.aiplatform.v1beta1.ICreateFeatureMonitorRequest, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor, protos.google.cloud.aiplatform.v1beta1.ICreateFeatureMonitorOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeatureMonitorRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturemonitorrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitor), [protos.google.cloud.aiplatform.v1beta1.ICreateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturemonitoroperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFeatureMonitorJob(request, options)
    
    
    createFeatureMonitorJob(request?: protos.google.cloud.aiplatform.v1beta1.ICreateFeatureMonitorJobRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IFeatureMonitorJob,
            (protos.google.cloud.aiplatform.v1beta1.ICreateFeatureMonitorJobRequest | undefined),
            {} | undefined
        ]>;

Creates a new feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeatureMonitorJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturemonitorjobrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IFeatureMonitorJob](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitorjob), ([protos.google.cloud.aiplatform.v1beta1.ICreateFeatureMonitorJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturemonitorjobrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of FeatureMonitor to create FeatureMonitorJob.
       *  Format:
       *  `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The Monitor to create.
       */
      // const featureMonitorJob = {}
      /**
       *  Optional. Output only. System-generated ID for feature monitor job.
       */
      // const featureMonitorJobId = 1234
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callCreateFeatureMonitorJob() {
        // Construct request
        const request = {
          parent,
          featureMonitorJob,
        };
    
        // Run request
        const response = await aiplatformClient.createFeatureMonitorJob(request);
        console.log(response);
      }
    
      callCreateFeatureMonitorJob();
    
    

### createFeatureMonitorJob(request, options, callback)
    
    
    createFeatureMonitorJob(request: protos.google.cloud.aiplatform.v1beta1.ICreateFeatureMonitorJobRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IFeatureMonitorJob, protos.google.cloud.aiplatform.v1beta1.ICreateFeatureMonitorJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeatureMonitorJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturemonitorjobrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IFeatureMonitorJob](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitorjob), [protos.google.cloud.aiplatform.v1beta1.ICreateFeatureMonitorJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturemonitorjobrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFeatureMonitorJob(request, callback)
    
    
    createFeatureMonitorJob(request: protos.google.cloud.aiplatform.v1beta1.ICreateFeatureMonitorJobRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IFeatureMonitorJob, protos.google.cloud.aiplatform.v1beta1.ICreateFeatureMonitorJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeatureMonitorJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturemonitorjobrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IFeatureMonitorJob](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitorjob), [protos.google.cloud.aiplatform.v1beta1.ICreateFeatureMonitorJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatefeaturemonitorjobrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### deleteFeature(request, options)
    
    
    deleteFeature(request?: protos.google.cloud.aiplatform.v1beta1.IDeleteFeatureRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletefeaturerequest)`   
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
       *  Required. The name of the Features to be deleted.
       *  Format:
       *  `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}`
       *  `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteFeature() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.deleteFeature(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteFeature();
    
    

### deleteFeature(request, options, callback)
    
    
    deleteFeature(request: protos.google.cloud.aiplatform.v1beta1.IDeleteFeatureRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletefeaturerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFeature(request, callback)
    
    
    deleteFeature(request: protos.google.cloud.aiplatform.v1beta1.IDeleteFeatureRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletefeaturerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFeatureGroup(request, options)
    
    
    deleteFeatureGroup(request?: protos.google.cloud.aiplatform.v1beta1.IDeleteFeatureGroupRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeatureGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletefeaturegrouprequest)`   
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
       *  Required. The name of the FeatureGroup to be deleted.
       *  Format:
       *  `projects/{project}/locations/{location}/featureGroups/{feature_group}`
       */
      // const name = 'abc123'
      /**
       *  If set to true, any Features under this FeatureGroup
       *  will also be deleted. (Otherwise, the request will only work if the
       *  FeatureGroup has no Features.)
       */
      // const force = true
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteFeatureGroup() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.deleteFeatureGroup(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteFeatureGroup();
    
    

### deleteFeatureGroup(request, options, callback)
    
    
    deleteFeatureGroup(request: protos.google.cloud.aiplatform.v1beta1.IDeleteFeatureGroupRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeatureGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletefeaturegrouprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFeatureGroup(request, callback)
    
    
    deleteFeatureGroup(request: protos.google.cloud.aiplatform.v1beta1.IDeleteFeatureGroupRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeatureGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletefeaturegrouprequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFeatureMonitor(request, options)
    
    
    deleteFeatureMonitor(request?: protos.google.cloud.aiplatform.v1beta1.IDeleteFeatureMonitorRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeatureMonitorRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletefeaturemonitorrequest)`   
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
       *  Required. The name of the FeatureMonitor to be deleted.
       *  Format:
       *  `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteFeatureMonitor() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await aiplatformClient.deleteFeatureMonitor(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteFeatureMonitor();
    
    

### deleteFeatureMonitor(request, options, callback)
    
    
    deleteFeatureMonitor(request: protos.google.cloud.aiplatform.v1beta1.IDeleteFeatureMonitorRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeatureMonitorRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletefeaturemonitorrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideleteoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFeatureMonitor(request, callback)
    
    
    deleteFeatureMonitor(request: protos.google.cloud.aiplatform.v1beta1.IDeleteFeatureMonitorRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeatureMonitorRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletefeaturemonitorrequest)`   
  
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
  
### getFeature(request, options)
    
    
    getFeature(request?: protos.google.cloud.aiplatform.v1beta1.IGetFeatureRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IFeature,
            protos.google.cloud.aiplatform.v1beta1.IGetFeatureRequest | undefined,
            {} | undefined
        ]>;

Gets details of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeature), [protos.google.cloud.aiplatform.v1beta1.IGetFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Feature resource.
       *  Format for entity_type as parent:
       *  `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}`
       *  Format for feature_group as parent:
       *  `projects/{project}/locations/{location}/featureGroups/{feature_group}`
       */
      // const name = 'abc123'
      /**
       *  Optional. Only applicable for Vertex AI Feature Store.
       *  If set, retrieves FeatureStatsAndAnomaly generated by FeatureMonitors based
       *  on this spec.
       */
      // const featureStatsAndAnomalySpec = {}
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callGetFeature() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await aiplatformClient.getFeature(request);
        console.log(response);
      }
    
      callGetFeature();
    
    

### getFeature(request, options, callback)
    
    
    getFeature(request: protos.google.cloud.aiplatform.v1beta1.IGetFeatureRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IFeature, protos.google.cloud.aiplatform.v1beta1.IGetFeatureRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeature), [protos.google.cloud.aiplatform.v1beta1.IGetFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFeature(request, callback)
    
    
    getFeature(request: protos.google.cloud.aiplatform.v1beta1.IGetFeatureRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IFeature, protos.google.cloud.aiplatform.v1beta1.IGetFeatureRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeature), [protos.google.cloud.aiplatform.v1beta1.IGetFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFeatureGroup(request, options)
    
    
    getFeatureGroup(request?: protos.google.cloud.aiplatform.v1beta1.IGetFeatureGroupRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IFeatureGroup,
            (protos.google.cloud.aiplatform.v1beta1.IGetFeatureGroupRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturegrouprequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IFeatureGroup](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturegroup), ([protos.google.cloud.aiplatform.v1beta1.IGetFeatureGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturegrouprequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the FeatureGroup resource.
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callGetFeatureGroup() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await aiplatformClient.getFeatureGroup(request);
        console.log(response);
      }
    
      callGetFeatureGroup();
    
    

### getFeatureGroup(request, options, callback)
    
    
    getFeatureGroup(request: protos.google.cloud.aiplatform.v1beta1.IGetFeatureGroupRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IFeatureGroup, protos.google.cloud.aiplatform.v1beta1.IGetFeatureGroupRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturegrouprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IFeatureGroup](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturegroup), [protos.google.cloud.aiplatform.v1beta1.IGetFeatureGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturegrouprequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFeatureGroup(request, callback)
    
    
    getFeatureGroup(request: protos.google.cloud.aiplatform.v1beta1.IGetFeatureGroupRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IFeatureGroup, protos.google.cloud.aiplatform.v1beta1.IGetFeatureGroupRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturegrouprequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IFeatureGroup](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturegroup), [protos.google.cloud.aiplatform.v1beta1.IGetFeatureGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturegrouprequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFeatureMonitor(request, options)
    
    
    getFeatureMonitor(request?: protos.google.cloud.aiplatform.v1beta1.IGetFeatureMonitorRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor,
            (protos.google.cloud.aiplatform.v1beta1.IGetFeatureMonitorRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureMonitorRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturemonitorrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitor), ([protos.google.cloud.aiplatform.v1beta1.IGetFeatureMonitorRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturemonitorrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [FeatureMonitor](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featuremonitor). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the FeatureMonitor resource.
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callGetFeatureMonitor() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await aiplatformClient.getFeatureMonitor(request);
        console.log(response);
      }
    
      callGetFeatureMonitor();
    
    

### getFeatureMonitor(request, options, callback)
    
    
    getFeatureMonitor(request: protos.google.cloud.aiplatform.v1beta1.IGetFeatureMonitorRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor, protos.google.cloud.aiplatform.v1beta1.IGetFeatureMonitorRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureMonitorRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturemonitorrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitor), [protos.google.cloud.aiplatform.v1beta1.IGetFeatureMonitorRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturemonitorrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFeatureMonitor(request, callback)
    
    
    getFeatureMonitor(request: protos.google.cloud.aiplatform.v1beta1.IGetFeatureMonitorRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor, protos.google.cloud.aiplatform.v1beta1.IGetFeatureMonitorRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureMonitorRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturemonitorrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitor), [protos.google.cloud.aiplatform.v1beta1.IGetFeatureMonitorRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturemonitorrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFeatureMonitorJob(request, options)
    
    
    getFeatureMonitorJob(request?: protos.google.cloud.aiplatform.v1beta1.IGetFeatureMonitorJobRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IFeatureMonitorJob,
            (protos.google.cloud.aiplatform.v1beta1.IGetFeatureMonitorJobRequest | undefined),
            {} | undefined
        ]>;

Get a feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureMonitorJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturemonitorjobrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IFeatureMonitorJob](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitorjob), ([protos.google.cloud.aiplatform.v1beta1.IGetFeatureMonitorJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturemonitorjobrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the FeatureMonitorJob resource.
       *  Format:
       *  `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}/featureMonitorJobs/{feature_monitor_job}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callGetFeatureMonitorJob() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await aiplatformClient.getFeatureMonitorJob(request);
        console.log(response);
      }
    
      callGetFeatureMonitorJob();
    
    

### getFeatureMonitorJob(request, options, callback)
    
    
    getFeatureMonitorJob(request: protos.google.cloud.aiplatform.v1beta1.IGetFeatureMonitorJobRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IFeatureMonitorJob, protos.google.cloud.aiplatform.v1beta1.IGetFeatureMonitorJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureMonitorJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturemonitorjobrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IFeatureMonitorJob](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitorjob), [protos.google.cloud.aiplatform.v1beta1.IGetFeatureMonitorJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturemonitorjobrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFeatureMonitorJob(request, callback)
    
    
    getFeatureMonitorJob(request: protos.google.cloud.aiplatform.v1beta1.IGetFeatureMonitorJobRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IFeatureMonitorJob, protos.google.cloud.aiplatform.v1beta1.IGetFeatureMonitorJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeatureMonitorJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturemonitorjobrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IFeatureMonitorJob](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitorjob), [protos.google.cloud.aiplatform.v1beta1.IGetFeatureMonitorJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetfeaturemonitorjobrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listFeatureGroups(request, options)
    
    
    listFeatureGroups(request?: protos.google.cloud.aiplatform.v1beta1.IListFeatureGroupsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IFeatureGroup[],
            protos.google.cloud.aiplatform.v1beta1.IListFeatureGroupsRequest | null,
            protos.google.cloud.aiplatform.v1beta1.IListFeatureGroupsResponse
        ]>;

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeatureGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturegroupsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IFeatureGroup](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturegroup)[], [protos.google.cloud.aiplatform.v1beta1.IListFeatureGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturegroupsrequest) | null, [protos.google.cloud.aiplatform.v1beta1.IListFeatureGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturegroupsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listFeatureGroupsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listFeatureGroups(request, options, callback)
    
    
    listFeatureGroups(request: protos.google.cloud.aiplatform.v1beta1.IListFeatureGroupsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListFeatureGroupsRequest, protos.google.cloud.aiplatform.v1beta1.IListFeatureGroupsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.IFeatureGroup>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeatureGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturegroupsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListFeatureGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturegroupsrequest), [protos.google.cloud.aiplatform.v1beta1.IListFeatureGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturegroupsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.IFeatureGroup](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturegroup)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFeatureGroups(request, callback)
    
    
    listFeatureGroups(request: protos.google.cloud.aiplatform.v1beta1.IListFeatureGroupsRequest, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListFeatureGroupsRequest, protos.google.cloud.aiplatform.v1beta1.IListFeatureGroupsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.IFeatureGroup>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeatureGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturegroupsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListFeatureGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturegroupsrequest), [protos.google.cloud.aiplatform.v1beta1.IListFeatureGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturegroupsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.IFeatureGroup](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturegroup)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFeatureGroupsAsync(request, options)
    
    
    listFeatureGroupsAsync(request?: protos.google.cloud.aiplatform.v1beta1.IListFeatureGroupsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.aiplatform.v1beta1.IFeatureGroup>;

Equivalent to `listFeatureGroups`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeatureGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturegroupsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.aiplatform.v1beta1.IFeatureGroup](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturegroup)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Location to list FeatureGroups.
       *  Format:
       *  `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Lists the FeatureGroups that match the filter expression. The
       *  following fields are supported:
       *  * `create_time`: Supports `=`, `!=`, `<`, `="">`, `<=`, and="" `="">=` comparisons.
       *  Values must be
       *    in RFC 3339 format.
       *  * `update_time`: Supports `=`, `!=`, `<`, `="">`, `<=`, and="" `="">=` comparisons.
       *  Values must be
       *    in RFC 3339 format.
       *  * `labels`: Supports key-value equality and key presence.
       *  Examples:
       *  * `create_time > "2020-01-01" OR update_time > "2020-01-01"`
       *     FeatureGroups created or updated after 2020-01-01.
       *  * `labels.env = "prod"`
       *     FeatureGroups with label "env" set to "prod".
       */
      // const filter = 'abc123'
      /**
       *  The maximum number of FeatureGroups to return. The service may return
       *  fewer than this value. If unspecified, at most 100 FeatureGroups will
       *  be returned. The maximum value is 100; any value greater than 100 will be
       *  coerced to 100.
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous
       *  FeatureGroupAdminService.ListFeatureGroups   call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  FeatureGroupAdminService.ListFeatureGroups   must
       *  match the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  A comma-separated list of fields to order by, sorted in ascending order.
       *  Use "desc" after a field name for descending.
       *  Supported Fields:
       *    * `create_time`
       *    * `update_time`
       */
      // const orderBy = 'abc123'
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callListFeatureGroups() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = aiplatformClient.listFeatureGroupsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListFeatureGroups();
    
    

### listFeatureGroupsStream(request, options)
    
    
    listFeatureGroupsStream(request?: protos.google.cloud.aiplatform.v1beta1.IListFeatureGroupsRequest, options?: CallOptions): Transform;

Equivalent to `listFeatureGroups`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeatureGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturegroupsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listFeatureGroupsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listFeatureMonitorJobs(request, options)
    
    
    listFeatureMonitorJobs(request?: protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorJobsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IFeatureMonitorJob[],
            protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorJobsRequest | null,
            protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorJobsResponse
        ]>;

List feature monitor jobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeatureMonitorJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorjobsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IFeatureMonitorJob](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitorjob)[], [protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorjobsrequest) | null, [protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorjobsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listFeatureMonitorJobsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listFeatureMonitorJobs(request, options, callback)
    
    
    listFeatureMonitorJobs(request: protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorJobsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorJobsRequest, protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorJobsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.IFeatureMonitorJob>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeatureMonitorJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorjobsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorjobsrequest), [protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorjobsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.IFeatureMonitorJob](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitorjob)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFeatureMonitorJobs(request, callback)
    
    
    listFeatureMonitorJobs(request: protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorJobsRequest, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorJobsRequest, protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorJobsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.IFeatureMonitorJob>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeatureMonitorJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorjobsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorjobsrequest), [protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorjobsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.IFeatureMonitorJob](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitorjob)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFeatureMonitorJobsAsync(request, options)
    
    
    listFeatureMonitorJobsAsync(request?: protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorJobsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.aiplatform.v1beta1.IFeatureMonitorJob>;

Equivalent to `listFeatureMonitorJobs`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeatureMonitorJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorjobsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.aiplatform.v1beta1.IFeatureMonitorJob](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitorjob)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the FeatureMonitor to list
       *  FeatureMonitorJobs. Format:
       *  `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. Lists the FeatureMonitorJobs that match the filter expression.
       *  The following fields are supported:
       *  * `create_time`: Supports `=`, `!=`, `<`, `="">`, `<=`, and="" `="">=` comparisons.
       *  Values must be
       *  Examples:
       *  * `create_time > "2020-01-01"`
       *     FeatureMonitorJobs created after 2020-01-01.
       */
      // const filter = 'abc123'
      /**
       *  Optional. The maximum number of FeatureMonitorJobs to return. The service
       *  may return fewer than this value. If unspecified, at most 100
       *  FeatureMonitorJobs will be returned. The maximum value is 100; any value
       *  greater than 100 will be coerced to 100.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous
       *  FeatureRegistryService.ListFeatureMonitorJobs google.cloud.aiplatform.v1beta1.FeatureRegistryService.ListFeatureMonitorJobs 
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  FeatureRegistryService.ListFeatureMonitorJobs google.cloud.aiplatform.v1beta1.FeatureRegistryService.ListFeatureMonitorJobs 
       *  must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. A comma-separated list of fields to order by, sorted in ascending
       *  order. Use "desc" after a field name for descending. Supported Fields:
       *    * `create_time`
       */
      // const orderBy = 'abc123'
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callListFeatureMonitorJobs() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = aiplatformClient.[listFeatureMonitorJobsAsync](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/v1beta1.featureregistryserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListFeatureMonitorJobs();
    
    

### listFeatureMonitorJobsStream(request, options)
    
    
    listFeatureMonitorJobsStream(request?: protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorJobsRequest, options?: CallOptions): Transform;

Equivalent to `listFeatureMonitorJobs`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeatureMonitorJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorjobsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listFeatureMonitorJobsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listFeatureMonitors(request, options)
    
    
    listFeatureMonitors(request?: protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor[],
            protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorsRequest | null,
            protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorsResponse
        ]>;

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeatureMonitorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitor)[], [protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorsrequest) | null, [protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [FeatureMonitor](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featuremonitor). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listFeatureMonitorsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listFeatureMonitors(request, options, callback)
    
    
    listFeatureMonitors(request: protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorsRequest, protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeatureMonitorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorsrequest), [protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitor)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFeatureMonitors(request, callback)
    
    
    listFeatureMonitors(request: protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorsRequest, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorsRequest, protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeatureMonitorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorsrequest), [protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitor)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFeatureMonitorsAsync(request, options)
    
    
    listFeatureMonitorsAsync(request?: protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor>;

Equivalent to `listFeatureMonitors`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeatureMonitorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitor)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [FeatureMonitor](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featuremonitor). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the FeatureGroup to list FeatureMonitors.
       *  Format:
       *  `projects/{project}/locations/{location}/featureGroups/{featureGroup}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. Lists the FeatureMonitors that match the filter expression. The
       *  following fields are supported:
       *  * `create_time`: Supports `=`, `!=`, `<`, `="">`, `<=`, and="" `="">=` comparisons.
       *  Values must be
       *    in RFC 3339 format.
       *  * `update_time`: Supports `=`, `!=`, `<`, `="">`, `<=`, and="" `="">=` comparisons.
       *  Values must be
       *    in RFC 3339 format.
       *  * `labels`: Supports key-value equality and key presence.
       *  Examples:
       *  * `create_time > "2020-01-01" OR update_time > "2020-01-01"`
       *     FeatureMonitors created or updated after 2020-01-01.
       *  * `labels.env = "prod"`
       *     FeatureGroups with label "env" set to "prod".
       */
      // const filter = 'abc123'
      /**
       *  Optional. The maximum number of FeatureGroups to return. The service may
       *  return fewer than this value. If unspecified, at most 100 FeatureMonitors
       *  will be returned. The maximum value is 100; any value greater than 100 will
       *  be coerced to 100.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous
       *  FeatureRegistryService.ListFeatureMonitors google.cloud.aiplatform.v1beta1.FeatureRegistryService.ListFeatureMonitors 
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  FeatureRegistryService.ListFeatureMonitors google.cloud.aiplatform.v1beta1.FeatureRegistryService.ListFeatureMonitors 
       *  must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. A comma-separated list of fields to order by, sorted in ascending
       *  order. Use "desc" after a field name for descending. Supported Fields:
       *    * `create_time`
       *    * `update_time`
       */
      // const orderBy = 'abc123'
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callListFeatureMonitors() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = aiplatformClient.[listFeatureMonitorsAsync](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/v1beta1.featureregistryserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListFeatureMonitors();
    
    

### listFeatureMonitorsStream(request, options)
    
    
    listFeatureMonitorsStream(request?: protos.google.cloud.aiplatform.v1beta1.IListFeatureMonitorsRequest, options?: CallOptions): Transform;

Equivalent to `listFeatureMonitors`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeatureMonitorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturemonitorsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [FeatureMonitor](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featuremonitor) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listFeatureMonitorsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listFeatures(request, options)
    
    
    listFeatures(request?: protos.google.cloud.aiplatform.v1beta1.IListFeaturesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IFeature[],
            protos.google.cloud.aiplatform.v1beta1.IListFeaturesRequest | null,
            protos.google.cloud.aiplatform.v1beta1.IListFeaturesResponse
        ]>;

Lists Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeature)[], [protos.google.cloud.aiplatform.v1beta1.IListFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturesrequest) | null, [protos.google.cloud.aiplatform.v1beta1.IListFeaturesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listFeaturesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listFeatures(request, options, callback)
    
    
    listFeatures(request: protos.google.cloud.aiplatform.v1beta1.IListFeaturesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListFeaturesRequest, protos.google.cloud.aiplatform.v1beta1.IListFeaturesResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.IFeature>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturesrequest), [protos.google.cloud.aiplatform.v1beta1.IListFeaturesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturesresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeature)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFeatures(request, callback)
    
    
    listFeatures(request: protos.google.cloud.aiplatform.v1beta1.IListFeaturesRequest, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListFeaturesRequest, protos.google.cloud.aiplatform.v1beta1.IListFeaturesResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.IFeature>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturesrequest), [protos.google.cloud.aiplatform.v1beta1.IListFeaturesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturesresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeature)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFeaturesAsync(request, options)
    
    
    listFeaturesAsync(request?: protos.google.cloud.aiplatform.v1beta1.IListFeaturesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.aiplatform.v1beta1.IFeature>;

Equivalent to `listFeatures`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.aiplatform.v1beta1.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeature)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Location to list Features.
       *  Format for entity_type as parent:
       *  `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}`
       *  Format for feature_group as parent:
       *  `projects/{project}/locations/{location}/featureGroups/{feature_group}`
       */
      // const parent = 'abc123'
      /**
       *  Lists the Features that match the filter expression. The following
       *  filters are supported:
       *  * `value_type`: Supports = and != comparisons.
       *  * `create_time`: Supports =, !=, <,>, >=, and <= comparisons.="" values="" must="" *="" be="" in="" rfc="" 3339="" format.="" *="" *="" `update_time`:="" supports="," !=","><,>, >=, and <= comparisons.="" values="" must="" *="" be="" in="" rfc="" 3339="" format.="" *="" *="" `labels`:="" supports="" key-value="" equality="" as="" well="" as="" key="" presence.="" *="" examples:="" *="" *="" `value_type="DOUBLE`" --=""> Features whose type is DOUBLE.
       *  * `create_time > \"2020-01-31T15:30:00.000000Z\" OR
       *       update_time > \"2020-01-31T15:30:00.000000Z\"` --> EntityTypes created
       *       or updated after 2020-01-31T15:30:00.000000Z.
       *  * `labels.active = yes AND labels.env = prod` --> Features having both
       *      (active: yes) and (env: prod) labels.
       *  * `labels.env: *` --> Any Feature which has a label with 'env' as the
       *    key.
       */
      // const filter = 'abc123'
      /**
       *  The maximum number of Features to return. The service may return fewer
       *  than this value. If unspecified, at most 1000 Features will be returned.
       *  The maximum value is 1000; any value greater than 1000 will be coerced to
       *  1000.
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous
       *  FeaturestoreService.ListFeatures google.cloud.aiplatform.v1beta1.FeaturestoreService.ListFeatures 
       *  call or
       *  FeatureRegistryService.ListFeatures google.cloud.aiplatform.v1beta1.FeatureRegistryService.ListFeatures 
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  FeaturestoreService.ListFeatures google.cloud.aiplatform.v1beta1.FeaturestoreService.ListFeatures 
       *  or
       *  FeatureRegistryService.ListFeatures google.cloud.aiplatform.v1beta1.FeatureRegistryService.ListFeatures 
       *  must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  A comma-separated list of fields to order by, sorted in ascending order.
       *  Use "desc" after a field name for descending.
       *  Supported fields:
       *    * `feature_id`
       *    * `value_type` (Not supported for FeatureRegistry Feature)
       *    * `create_time`
       *    * `update_time`
       */
      // const orderBy = 'abc123'
      /**
       *  Mask specifying which fields to read.
       */
      // const readMask = {}
      /**
       *  Only applicable for Vertex AI Feature Store (Legacy).
       *  If set, return the most recent
       *  ListFeaturesRequest.latest_stats_count google.cloud.aiplatform.v1beta1.ListFeaturesRequest.latest_stats_count 
       *  of stats for each Feature in response. Valid value is 0, 10. If number of
       *  stats exists < *="" listfeaturesrequest.latest_stats_count="" google.cloud.aiplatform.v1beta1.listfeaturesrequest.latest_stats_count,="" *="" return="" all="" existing="" stats.="" */="" const="" lateststatscount="1234" imports="" the="" aiplatform="" library="" const="" {featureregistryserviceclient}="require('@google-cloud/aiplatform').v1beta1;" instantiates="" a="" client="" const="" aiplatformclient="new" featureregistryserviceclient();="" async="" function="" calllistfeatures()="" {="" construct="" request="" const="" request="{" parent,="" };="" run="" request="" const="" iterable="aiplatformClient.listFeaturesAsync(request);" for="" await="" (const="" response="" of="" iterable)="" {="" console.log(response);="" }="" }="" calllistfeatures();="">

### listFeaturesStream(request, options)
    
    
    listFeaturesStream(request?: protos.google.cloud.aiplatform.v1beta1.IListFeaturesRequest, options?: CallOptions): Transform;

Equivalent to `listFeatures`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeaturesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistfeaturesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listFeaturesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### updateFeature(request, options)
    
    
    updateFeature(request?: protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.aiplatform.v1beta1.IFeature, protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the parameters of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeaturerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.aiplatform.v1beta1.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeature), [protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeatureoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Feature's `name` field is used to identify the Feature to be
       *  updated.
       *  Format:
       *  `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}`
       *  `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}`
       */
      // const feature = {}
      /**
       *  Field mask is used to specify the fields to be overwritten in the
       *  Features resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then only the non-empty fields present in the
       *  request will be overwritten. Set the update_mask to `*` to override all
       *  fields.
       *  Updatable fields:
       *    * `description`
       *    * `labels`
       *    * `disable_monitoring` (Not supported for FeatureRegistryService Feature)
       *    * `point_of_contact` (Not supported for FeaturestoreService FeatureStore)
       */
      // const updateMask = {}
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callUpdateFeature() {
        // Construct request
        const request = {
          feature,
        };
    
        // Run request
        const [operation] = await aiplatformClient.updateFeature(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateFeature();
    
    

### updateFeature(request, options, callback)
    
    
    updateFeature(request: protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IFeature, protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeaturerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeature), [protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeatureoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFeature(request, callback)
    
    
    updateFeature(request: protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureRequest, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IFeature, protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeatureRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeaturerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IFeature](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeature), [protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeatureoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFeatureGroup(request, options)
    
    
    updateFeatureGroup(request?: protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureGroupRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.aiplatform.v1beta1.IFeatureGroup, protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureGroupOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the parameters of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeatureGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeaturegrouprequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.aiplatform.v1beta1.IFeatureGroup](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturegroup), [protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureGroupOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeaturegroupoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The FeatureGroup's `name` field is used to identify the
       *  FeatureGroup to be updated. Format:
       *  `projects/{project}/locations/{location}/featureGroups/{feature_group}`
       */
      // const featureGroup = {}
      /**
       *  Field mask is used to specify the fields to be overwritten in the
       *  FeatureGroup resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then only the non-empty fields present in the
       *  request will be overwritten. Set the update_mask to `*` to override all
       *  fields.
       *  Updatable fields:
       *    * `labels`
       *    * `description`
       *    * `big_query`
       *    * `big_query.entity_id_columns`
       */
      // const updateMask = {}
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callUpdateFeatureGroup() {
        // Construct request
        const request = {
          featureGroup,
        };
    
        // Run request
        const [operation] = await aiplatformClient.updateFeatureGroup(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateFeatureGroup();
    
    

### updateFeatureGroup(request, options, callback)
    
    
    updateFeatureGroup(request: protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureGroupRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IFeatureGroup, protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureGroupOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeatureGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeaturegrouprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IFeatureGroup](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturegroup), [protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureGroupOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeaturegroupoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFeatureGroup(request, callback)
    
    
    updateFeatureGroup(request: protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureGroupRequest, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IFeatureGroup, protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureGroupOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeatureGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeaturegrouprequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IFeatureGroup](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturegroup), [protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureGroupOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeaturegroupoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFeatureMonitor(request, options)
    
    
    updateFeatureMonitor(request?: protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureMonitorRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor, protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureMonitorOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the parameters of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeatureMonitorRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeaturemonitorrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitor), [protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeaturemonitoroperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The FeatureMonitor's `name` field is used to identify the
       *  FeatureMonitor to be updated. Format:
       *  `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`
       */
      // const featureMonitor = {}
      /**
       *  Optional. Field mask is used to specify the fields to be overwritten in the
       *  FeatureMonitor resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then only the non-empty fields present in the
       *  request will be overwritten. Set the update_mask to `*` to override all
       *  fields.
       *  Updatable fields:
       *    * `labels`
       */
      // const updateMask = {}
    
      // Imports the Aiplatform library
      const {FeatureRegistryServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [FeatureRegistryServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callUpdateFeatureMonitor() {
        // Construct request
        const request = {
          featureMonitor,
        };
    
        // Run request
        const [operation] = await aiplatformClient.updateFeatureMonitor(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateFeatureMonitor();
    
    

### updateFeatureMonitor(request, options, callback)
    
    
    updateFeatureMonitor(request: protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureMonitorRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor, protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureMonitorOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeatureMonitorRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeaturemonitorrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitor), [protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeaturemonitoroperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFeatureMonitor(request, callback)
    
    
    updateFeatureMonitor(request: protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureMonitorRequest, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor, protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureMonitorOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeatureMonitorRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeaturemonitorrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.IFeatureMonitor](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ifeaturemonitor), [protos.google.cloud.aiplatform.v1beta1.IUpdateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iupdatefeaturemonitoroperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
