---
url: https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/v1beta1.automlclient
title: Class v1beta1.AutoMlClient (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:28.637560+00:00
---

# Class v1beta1.AutoMlClient (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/v1beta1.automlclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.AutoMlClient (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.1.3  4.0.1  3.1.2  2.5.2  2.4.5 

AutoML Server API.

The resource names are assigned by the server. The server never reuses names that it has created after the resources with those names are deleted.

An ID of a resource is the last element of the item's resource name. For `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}`, then the id for the item is `{dataset_id}`.

Currently the only supported `location_id` is "us-central1".

On any input that is documented to expect a string parameter in snake_case or kebab-case, either of those cases is accepted. v1beta1

## Package

[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of AutoMlClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new AutoMlClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### autoMlStub
    
    
    autoMlStub?: Promise<{
            [name: string]: Function;
        }>;

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
  
### checkCreateModelProgress(name)
    
    
    checkCreateModelProgress(name: string): Promise<LROperation<protos.google.cloud.automl.v1beta1.Model, protos.google.cloud.automl.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `createModel()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.automl.v1beta1.Model](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.model-class), [protos.google.cloud.automl.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name of the parent project where the model is being created.
       */
      // const parent = 'abc123'
      /**
       *  Required. The model to create.
       */
      // const model = {}
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callCreateModel() {
        // Construct request
        const request = {
          parent,
          model,
        };
    
        // Run request
        const [operation] = await automlClient.createModel(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateModel();
    
    

### checkDeleteDatasetProgress(name)
    
    
    checkDeleteDatasetProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.automl.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `deleteDataset()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.empty), [protos.google.cloud.automl.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the dataset to delete.
       */
      // const name = 'abc123'
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callDeleteDataset() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await automlClient.deleteDataset(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteDataset();
    
    

### checkDeleteModelProgress(name)
    
    
    checkDeleteModelProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.automl.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `deleteModel()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.empty), [protos.google.cloud.automl.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name of the model being deleted.
       */
      // const name = 'abc123'
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callDeleteModel() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await automlClient.deleteModel(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteModel();
    
    

### checkDeployModelProgress(name)
    
    
    checkDeployModelProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.automl.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `deployModel()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.empty), [protos.google.cloud.automl.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Model deployment metadata specific to Image Object Detection.
       */
      // const imageObjectDetectionModelDeploymentMetadata = {}
      /**
       *  Model deployment metadata specific to Image Classification.
       */
      // const imageClassificationModelDeploymentMetadata = {}
      /**
       *  Required. Resource name of the model to deploy.
       */
      // const name = 'abc123'
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callDeployModel() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await automlClient.deployModel(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeployModel();
    
    

### checkExportDataProgress(name)
    
    
    checkExportDataProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.automl.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `exportData()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.empty), [protos.google.cloud.automl.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the dataset.
       */
      // const name = 'abc123'
      /**
       *  Required. The desired output location.
       */
      // const outputConfig = {}
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callExportData() {
        // Construct request
        const request = {
          name,
          outputConfig,
        };
    
        // Run request
        const [operation] = await automlClient.exportData(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportData();
    
    

### checkExportEvaluatedExamplesProgress(name)
    
    
    checkExportEvaluatedExamplesProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.automl.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `exportEvaluatedExamples()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.empty), [protos.google.cloud.automl.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the model whose evaluated examples are to
       *  be exported.
       */
      // const name = 'abc123'
      /**
       *  Required. The desired output location and configuration.
       */
      // const outputConfig = {}
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callExportEvaluatedExamples() {
        // Construct request
        const request = {
          name,
          outputConfig,
        };
    
        // Run request
        const [operation] = await automlClient.exportEvaluatedExamples(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportEvaluatedExamples();
    
    

### checkExportModelProgress(name)
    
    
    checkExportModelProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.automl.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `exportModel()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.empty), [protos.google.cloud.automl.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the model to export.
       */
      // const name = 'abc123'
      /**
       *  Required. The desired output location and configuration.
       */
      // const outputConfig = {}
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callExportModel() {
        // Construct request
        const request = {
          name,
          outputConfig,
        };
    
        // Run request
        const [operation] = await automlClient.exportModel(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportModel();
    
    

### checkImportDataProgress(name)
    
    
    checkImportDataProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.automl.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `importData()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.empty), [protos.google.cloud.automl.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Dataset name. Dataset must already exist. All imported
       *  annotations and examples will be added.
       */
      // const name = 'abc123'
      /**
       *  Required. The desired input location and its domain specific semantics,
       *  if any.
       */
      // const inputConfig = {}
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callImportData() {
        // Construct request
        const request = {
          name,
          inputConfig,
        };
    
        // Run request
        const [operation] = await automlClient.importData(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callImportData();
    
    

### checkUndeployModelProgress(name)
    
    
    checkUndeployModelProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.automl.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `undeployModel()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.empty), [protos.google.cloud.automl.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name of the model to undeploy.
       */
      // const name = 'abc123'
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callUndeployModel() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await automlClient.undeployModel(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUndeployModel();
    
    

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
  
### createDataset(request, options)
    
    
    createDataset(request?: protos.google.cloud.automl.v1beta1.ICreateDatasetRequest, options?: CallOptions): Promise<[
            protos.google.cloud.automl.v1beta1.IDataset,
            protos.google.cloud.automl.v1beta1.ICreateDatasetRequest | undefined,
            {} | undefined
        ]>;

Creates a dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icreatedatasetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.automl.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.idataset), [protos.google.cloud.automl.v1beta1.ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icreatedatasetrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Dataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.dataset). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the project to create the dataset for.
       */
      // const parent = 'abc123'
      /**
       *  Required. The dataset to create.
       */
      // const dataset = {}
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callCreateDataset() {
        // Construct request
        const request = {
          parent,
          dataset,
        };
    
        // Run request
        const response = await automlClient.createDataset(request);
        console.log(response);
      }
    
      callCreateDataset();
    
    

### createDataset(request, options, callback)
    
    
    createDataset(request: protos.google.cloud.automl.v1beta1.ICreateDatasetRequest, options: CallOptions, callback: Callback<protos.google.cloud.automl.v1beta1.IDataset, protos.google.cloud.automl.v1beta1.ICreateDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icreatedatasetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.idataset), [protos.google.cloud.automl.v1beta1.ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icreatedatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataset(request, callback)
    
    
    createDataset(request: protos.google.cloud.automl.v1beta1.ICreateDatasetRequest, callback: Callback<protos.google.cloud.automl.v1beta1.IDataset, protos.google.cloud.automl.v1beta1.ICreateDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icreatedatasetrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.idataset), [protos.google.cloud.automl.v1beta1.ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icreatedatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createModel(request, options)
    
    
    createModel(request?: protos.google.cloud.automl.v1beta1.ICreateModelRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.automl.v1beta1.IModel, protos.google.cloud.automl.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a model. Returns a Model in the [response](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation) field when it completes. When you create a model, several model evaluations are created for it: a global evaluation, and one evaluation for each annotation spec.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icreatemodelrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.automl.v1beta1.IModel](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodel), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name of the parent project where the model is being created.
       */
      // const parent = 'abc123'
      /**
       *  Required. The model to create.
       */
      // const model = {}
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callCreateModel() {
        // Construct request
        const request = {
          parent,
          model,
        };
    
        // Run request
        const [operation] = await automlClient.createModel(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateModel();
    
    

### createModel(request, options, callback)
    
    
    createModel(request: protos.google.cloud.automl.v1beta1.ICreateModelRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.automl.v1beta1.IModel, protos.google.cloud.automl.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icreatemodelrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.automl.v1beta1.IModel](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodel), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createModel(request, callback)
    
    
    createModel(request: protos.google.cloud.automl.v1beta1.ICreateModelRequest, callback: Callback<LROperation<protos.google.cloud.automl.v1beta1.IModel, protos.google.cloud.automl.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icreatemodelrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.automl.v1beta1.IModel](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodel), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
  
### deleteDataset(request, options)
    
    
    deleteDataset(request?: protos.google.cloud.automl.v1beta1.IDeleteDatasetRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a dataset and all of its contents. Returns empty response in the [response](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation) field when it completes, and `delete_details` in the [metadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation) field.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ideletedatasetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the dataset to delete.
       */
      // const name = 'abc123'
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callDeleteDataset() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await automlClient.deleteDataset(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteDataset();
    
    

### deleteDataset(request, options, callback)
    
    
    deleteDataset(request: protos.google.cloud.automl.v1beta1.IDeleteDatasetRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ideletedatasetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataset(request, callback)
    
    
    deleteDataset(request: protos.google.cloud.automl.v1beta1.IDeleteDatasetRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ideletedatasetrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteModel(request, options)
    
    
    deleteModel(request?: protos.google.cloud.automl.v1beta1.IDeleteModelRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a model. Returns `google.protobuf.Empty` in the [response](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation) field when it completes, and `delete_details` in the [metadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation) field.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ideletemodelrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name of the model being deleted.
       */
      // const name = 'abc123'
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callDeleteModel() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await automlClient.deleteModel(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteModel();
    
    

### deleteModel(request, options, callback)
    
    
    deleteModel(request: protos.google.cloud.automl.v1beta1.IDeleteModelRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ideletemodelrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteModel(request, callback)
    
    
    deleteModel(request: protos.google.cloud.automl.v1beta1.IDeleteModelRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ideletemodelrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deployModel(request, options)
    
    
    deployModel(request?: protos.google.cloud.automl.v1beta1.IDeployModelRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deploys a model. If a model is already deployed, deploying it with the same parameters has no effect. Deploying with different parametrs (as e.g. changing

) will reset the deployment state without pausing the model's availability.

Only applicable for Text Classification, Image Object Detection , Tables, and Image Segmentation; all other domains manage deployment automatically.

Returns an empty response in the [response](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation) field when it completes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeployModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ideploymodelrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Model deployment metadata specific to Image Object Detection.
       */
      // const imageObjectDetectionModelDeploymentMetadata = {}
      /**
       *  Model deployment metadata specific to Image Classification.
       */
      // const imageClassificationModelDeploymentMetadata = {}
      /**
       *  Required. Resource name of the model to deploy.
       */
      // const name = 'abc123'
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callDeployModel() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await automlClient.deployModel(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeployModel();
    
    

### deployModel(request, options, callback)
    
    
    deployModel(request: protos.google.cloud.automl.v1beta1.IDeployModelRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeployModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ideploymodelrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deployModel(request, callback)
    
    
    deployModel(request: protos.google.cloud.automl.v1beta1.IDeployModelRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeployModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ideploymodelrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportData(request, options)
    
    
    exportData(request?: protos.google.cloud.automl.v1beta1.IExportDataRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Exports dataset's data to the provided output location. Returns an empty response in the [response](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation) field when it completes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iexportdatarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the dataset.
       */
      // const name = 'abc123'
      /**
       *  Required. The desired output location.
       */
      // const outputConfig = {}
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callExportData() {
        // Construct request
        const request = {
          name,
          outputConfig,
        };
    
        // Run request
        const [operation] = await automlClient.exportData(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportData();
    
    

### exportData(request, options, callback)
    
    
    exportData(request: protos.google.cloud.automl.v1beta1.IExportDataRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iexportdatarequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportData(request, callback)
    
    
    exportData(request: protos.google.cloud.automl.v1beta1.IExportDataRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iexportdatarequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportEvaluatedExamples(request, options)
    
    
    exportEvaluatedExamples(request?: protos.google.cloud.automl.v1beta1.IExportEvaluatedExamplesRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Exports examples on which the model was evaluated (i.e. which were in the TEST set of the dataset the model was created from), together with their ground truth annotations and the annotations created (predicted) by the model. The examples, ground truth and predictions are exported in the state they were at the moment the model was evaluated.

This export is available only for 30 days since the model evaluation is created.

Currently only available for Tables.

Returns an empty response in the [response](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation) field when it completes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportEvaluatedExamplesRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iexportevaluatedexamplesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the model whose evaluated examples are to
       *  be exported.
       */
      // const name = 'abc123'
      /**
       *  Required. The desired output location and configuration.
       */
      // const outputConfig = {}
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callExportEvaluatedExamples() {
        // Construct request
        const request = {
          name,
          outputConfig,
        };
    
        // Run request
        const [operation] = await automlClient.exportEvaluatedExamples(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportEvaluatedExamples();
    
    

### exportEvaluatedExamples(request, options, callback)
    
    
    exportEvaluatedExamples(request: protos.google.cloud.automl.v1beta1.IExportEvaluatedExamplesRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportEvaluatedExamplesRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iexportevaluatedexamplesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportEvaluatedExamples(request, callback)
    
    
    exportEvaluatedExamples(request: protos.google.cloud.automl.v1beta1.IExportEvaluatedExamplesRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportEvaluatedExamplesRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iexportevaluatedexamplesrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportModel(request, options)
    
    
    exportModel(request?: protos.google.cloud.automl.v1beta1.IExportModelRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Exports a trained, "export-able", model to a user specified Google Cloud Storage location. A model is considered export-able if and only if it has an export format defined for it in

[ModelExportOutputConfig](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.modelexportoutputconfig).

Returns an empty response in the [response](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation) field when it completes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iexportmodelrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the model to export.
       */
      // const name = 'abc123'
      /**
       *  Required. The desired output location and configuration.
       */
      // const outputConfig = {}
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callExportModel() {
        // Construct request
        const request = {
          name,
          outputConfig,
        };
    
        // Run request
        const [operation] = await automlClient.exportModel(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportModel();
    
    

### exportModel(request, options, callback)
    
    
    exportModel(request: protos.google.cloud.automl.v1beta1.IExportModelRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iexportmodelrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportModel(request, callback)
    
    
    exportModel(request: protos.google.cloud.automl.v1beta1.IExportModelRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iexportmodelrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAnnotationSpec(request, options)
    
    
    getAnnotationSpec(request?: protos.google.cloud.automl.v1beta1.IGetAnnotationSpecRequest, options?: CallOptions): Promise<[
            protos.google.cloud.automl.v1beta1.IAnnotationSpec,
            protos.google.cloud.automl.v1beta1.IGetAnnotationSpecRequest | undefined,
            {} | undefined
        ]>;

Gets an annotation spec.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotationSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetannotationspecrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.automl.v1beta1.IAnnotationSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iannotationspec), [protos.google.cloud.automl.v1beta1.IGetAnnotationSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetannotationspecrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [AnnotationSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.annotationspec). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the annotation spec to retrieve.
       */
      // const name = 'abc123'
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callGetAnnotationSpec() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await automlClient.getAnnotationSpec(request);
        console.log(response);
      }
    
      callGetAnnotationSpec();
    
    

### getAnnotationSpec(request, options, callback)
    
    
    getAnnotationSpec(request: protos.google.cloud.automl.v1beta1.IGetAnnotationSpecRequest, options: CallOptions, callback: Callback<protos.google.cloud.automl.v1beta1.IAnnotationSpec, protos.google.cloud.automl.v1beta1.IGetAnnotationSpecRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotationSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetannotationspecrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.IAnnotationSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iannotationspec), [protos.google.cloud.automl.v1beta1.IGetAnnotationSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetannotationspecrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAnnotationSpec(request, callback)
    
    
    getAnnotationSpec(request: protos.google.cloud.automl.v1beta1.IGetAnnotationSpecRequest, callback: Callback<protos.google.cloud.automl.v1beta1.IAnnotationSpec, protos.google.cloud.automl.v1beta1.IGetAnnotationSpecRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotationSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetannotationspecrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.IAnnotationSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iannotationspec), [protos.google.cloud.automl.v1beta1.IGetAnnotationSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetannotationspecrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getColumnSpec(request, options)
    
    
    getColumnSpec(request?: protos.google.cloud.automl.v1beta1.IGetColumnSpecRequest, options?: CallOptions): Promise<[
            protos.google.cloud.automl.v1beta1.IColumnSpec,
            protos.google.cloud.automl.v1beta1.IGetColumnSpecRequest | undefined,
            {} | undefined
        ]>;

Gets a column spec.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetColumnSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetcolumnspecrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.automl.v1beta1.IColumnSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icolumnspec), [protos.google.cloud.automl.v1beta1.IGetColumnSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetcolumnspecrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the column spec to retrieve.
       */
      // const name = 'abc123'
      /**
       *  Mask specifying which fields to read.
       */
      // const fieldMask = {}
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callGetColumnSpec() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await automlClient.getColumnSpec(request);
        console.log(response);
      }
    
      callGetColumnSpec();
    
    

### getColumnSpec(request, options, callback)
    
    
    getColumnSpec(request: protos.google.cloud.automl.v1beta1.IGetColumnSpecRequest, options: CallOptions, callback: Callback<protos.google.cloud.automl.v1beta1.IColumnSpec, protos.google.cloud.automl.v1beta1.IGetColumnSpecRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetColumnSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetcolumnspecrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.IColumnSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icolumnspec), [protos.google.cloud.automl.v1beta1.IGetColumnSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetcolumnspecrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getColumnSpec(request, callback)
    
    
    getColumnSpec(request: protos.google.cloud.automl.v1beta1.IGetColumnSpecRequest, callback: Callback<protos.google.cloud.automl.v1beta1.IColumnSpec, protos.google.cloud.automl.v1beta1.IGetColumnSpecRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetColumnSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetcolumnspecrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.IColumnSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icolumnspec), [protos.google.cloud.automl.v1beta1.IGetColumnSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetcolumnspecrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataset(request, options)
    
    
    getDataset(request?: protos.google.cloud.automl.v1beta1.IGetDatasetRequest, options?: CallOptions): Promise<[
            protos.google.cloud.automl.v1beta1.IDataset,
            protos.google.cloud.automl.v1beta1.IGetDatasetRequest | undefined,
            {} | undefined
        ]>;

Gets a dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetdatasetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.automl.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.idataset), [protos.google.cloud.automl.v1beta1.IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetdatasetrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Dataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.dataset). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the dataset to retrieve.
       */
      // const name = 'abc123'
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callGetDataset() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await automlClient.getDataset(request);
        console.log(response);
      }
    
      callGetDataset();
    
    

### getDataset(request, options, callback)
    
    
    getDataset(request: protos.google.cloud.automl.v1beta1.IGetDatasetRequest, options: CallOptions, callback: Callback<protos.google.cloud.automl.v1beta1.IDataset, protos.google.cloud.automl.v1beta1.IGetDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetdatasetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.idataset), [protos.google.cloud.automl.v1beta1.IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetdatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataset(request, callback)
    
    
    getDataset(request: protos.google.cloud.automl.v1beta1.IGetDatasetRequest, callback: Callback<protos.google.cloud.automl.v1beta1.IDataset, protos.google.cloud.automl.v1beta1.IGetDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetdatasetrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.idataset), [protos.google.cloud.automl.v1beta1.IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetdatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getModel(request, options)
    
    
    getModel(request?: protos.google.cloud.automl.v1beta1.IGetModelRequest, options?: CallOptions): Promise<[
            protos.google.cloud.automl.v1beta1.IModel,
            protos.google.cloud.automl.v1beta1.IGetModelRequest | undefined,
            {} | undefined
        ]>;

Gets a model.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetmodelrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.automl.v1beta1.IModel](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodel), [protos.google.cloud.automl.v1beta1.IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetmodelrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name of the model.
       */
      // const name = 'abc123'
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callGetModel() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await automlClient.getModel(request);
        console.log(response);
      }
    
      callGetModel();
    
    

### getModel(request, options, callback)
    
    
    getModel(request: protos.google.cloud.automl.v1beta1.IGetModelRequest, options: CallOptions, callback: Callback<protos.google.cloud.automl.v1beta1.IModel, protos.google.cloud.automl.v1beta1.IGetModelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetmodelrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.IModel](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodel), [protos.google.cloud.automl.v1beta1.IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetmodelrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getModel(request, callback)
    
    
    getModel(request: protos.google.cloud.automl.v1beta1.IGetModelRequest, callback: Callback<protos.google.cloud.automl.v1beta1.IModel, protos.google.cloud.automl.v1beta1.IGetModelRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetmodelrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.IModel](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodel), [protos.google.cloud.automl.v1beta1.IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetmodelrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getModelEvaluation(request, options)
    
    
    getModelEvaluation(request?: protos.google.cloud.automl.v1beta1.IGetModelEvaluationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.automl.v1beta1.IModelEvaluation,
            protos.google.cloud.automl.v1beta1.IGetModelEvaluationRequest | undefined,
            {} | undefined
        ]>;

Gets a model evaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetModelEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetmodelevaluationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.automl.v1beta1.IModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodelevaluation), [protos.google.cloud.automl.v1beta1.IGetModelEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetmodelevaluationrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.modelevaluation). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name for the model evaluation.
       */
      // const name = 'abc123'
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callGetModelEvaluation() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await automlClient.getModelEvaluation(request);
        console.log(response);
      }
    
      callGetModelEvaluation();
    
    

### getModelEvaluation(request, options, callback)
    
    
    getModelEvaluation(request: protos.google.cloud.automl.v1beta1.IGetModelEvaluationRequest, options: CallOptions, callback: Callback<protos.google.cloud.automl.v1beta1.IModelEvaluation, protos.google.cloud.automl.v1beta1.IGetModelEvaluationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetModelEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetmodelevaluationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.IModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodelevaluation), [protos.google.cloud.automl.v1beta1.IGetModelEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetmodelevaluationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getModelEvaluation(request, callback)
    
    
    getModelEvaluation(request: protos.google.cloud.automl.v1beta1.IGetModelEvaluationRequest, callback: Callback<protos.google.cloud.automl.v1beta1.IModelEvaluation, protos.google.cloud.automl.v1beta1.IGetModelEvaluationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetModelEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetmodelevaluationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.IModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodelevaluation), [protos.google.cloud.automl.v1beta1.IGetModelEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igetmodelevaluationrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### getTableSpec(request, options)
    
    
    getTableSpec(request?: protos.google.cloud.automl.v1beta1.IGetTableSpecRequest, options?: CallOptions): Promise<[
            protos.google.cloud.automl.v1beta1.ITableSpec,
            protos.google.cloud.automl.v1beta1.IGetTableSpecRequest | undefined,
            {} | undefined
        ]>;

Gets a table spec.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTableSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igettablespecrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.automl.v1beta1.ITableSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.itablespec), [protos.google.cloud.automl.v1beta1.IGetTableSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igettablespecrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [TableSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.tablespec). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the table spec to retrieve.
       */
      // const name = 'abc123'
      /**
       *  Mask specifying which fields to read.
       */
      // const fieldMask = {}
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callGetTableSpec() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await automlClient.getTableSpec(request);
        console.log(response);
      }
    
      callGetTableSpec();
    
    

### getTableSpec(request, options, callback)
    
    
    getTableSpec(request: protos.google.cloud.automl.v1beta1.IGetTableSpecRequest, options: CallOptions, callback: Callback<protos.google.cloud.automl.v1beta1.ITableSpec, protos.google.cloud.automl.v1beta1.IGetTableSpecRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTableSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igettablespecrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.ITableSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.itablespec), [protos.google.cloud.automl.v1beta1.IGetTableSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igettablespecrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTableSpec(request, callback)
    
    
    getTableSpec(request: protos.google.cloud.automl.v1beta1.IGetTableSpecRequest, callback: Callback<protos.google.cloud.automl.v1beta1.ITableSpec, protos.google.cloud.automl.v1beta1.IGetTableSpecRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTableSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igettablespecrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.ITableSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.itablespec), [protos.google.cloud.automl.v1beta1.IGetTableSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.igettablespecrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importData(request, options)
    
    
    importData(request?: protos.google.cloud.automl.v1beta1.IImportDataRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Imports data into a dataset. For Tables this method can only be called on an empty Dataset.

For Tables: * A [schema_inference_version](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.inputconfig) parameter must be explicitly set. Returns an empty response in the [response](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation) field when it completes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iimportdatarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Dataset name. Dataset must already exist. All imported
       *  annotations and examples will be added.
       */
      // const name = 'abc123'
      /**
       *  Required. The desired input location and its domain specific semantics,
       *  if any.
       */
      // const inputConfig = {}
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callImportData() {
        // Construct request
        const request = {
          name,
          inputConfig,
        };
    
        // Run request
        const [operation] = await automlClient.importData(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callImportData();
    
    

### importData(request, options, callback)
    
    
    importData(request: protos.google.cloud.automl.v1beta1.IImportDataRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iimportdatarequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importData(request, callback)
    
    
    importData(request: protos.google.cloud.automl.v1beta1.IImportDataRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iimportdatarequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
  
### listColumnSpecs(request, options)
    
    
    listColumnSpecs(request?: protos.google.cloud.automl.v1beta1.IListColumnSpecsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.automl.v1beta1.IColumnSpec[],
            protos.google.cloud.automl.v1beta1.IListColumnSpecsRequest | null,
            protos.google.cloud.automl.v1beta1.IListColumnSpecsResponse
        ]>;

Lists column specs in a table spec.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListColumnSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistcolumnspecsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.automl.v1beta1.IColumnSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icolumnspec)[], [protos.google.cloud.automl.v1beta1.IListColumnSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistcolumnspecsrequest) | null, [protos.google.cloud.automl.v1beta1.IListColumnSpecsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistcolumnspecsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listColumnSpecsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listColumnSpecs(request, options, callback)
    
    
    listColumnSpecs(request: protos.google.cloud.automl.v1beta1.IListColumnSpecsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.automl.v1beta1.IListColumnSpecsRequest, protos.google.cloud.automl.v1beta1.IListColumnSpecsResponse | null | undefined, protos.google.cloud.automl.v1beta1.IColumnSpec>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListColumnSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistcolumnspecsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.automl.v1beta1.IListColumnSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistcolumnspecsrequest), [protos.google.cloud.automl.v1beta1.IListColumnSpecsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistcolumnspecsresponse) | null | undefined, [protos.google.cloud.automl.v1beta1.IColumnSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icolumnspec)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listColumnSpecs(request, callback)
    
    
    listColumnSpecs(request: protos.google.cloud.automl.v1beta1.IListColumnSpecsRequest, callback: PaginationCallback<protos.google.cloud.automl.v1beta1.IListColumnSpecsRequest, protos.google.cloud.automl.v1beta1.IListColumnSpecsResponse | null | undefined, protos.google.cloud.automl.v1beta1.IColumnSpec>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListColumnSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistcolumnspecsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.automl.v1beta1.IListColumnSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistcolumnspecsrequest), [protos.google.cloud.automl.v1beta1.IListColumnSpecsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistcolumnspecsresponse) | null | undefined, [protos.google.cloud.automl.v1beta1.IColumnSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icolumnspec)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listColumnSpecsAsync(request, options)
    
    
    listColumnSpecsAsync(request?: protos.google.cloud.automl.v1beta1.IListColumnSpecsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.automl.v1beta1.IColumnSpec>;

Equivalent to `listColumnSpecs`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListColumnSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistcolumnspecsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.automl.v1beta1.IColumnSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icolumnspec)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the table spec to list column specs from.
       */
      // const parent = 'abc123'
      /**
       *  Mask specifying which fields to read.
       */
      // const fieldMask = {}
      /**
       *  Filter expression, see go/filtering.
       */
      // const filter = 'abc123'
      /**
       *  Requested page size. The server can return fewer results than requested.
       *  If unspecified, the server will pick a default size.
       */
      // const pageSize = 1234
      /**
       *  A token identifying a page of results for the server to return.
       *  Typically obtained from the
       *  ListColumnSpecsResponse.next_page_token google.cloud.automl.v1beta1.ListColumnSpecsResponse.next_page_token  field of the previous
       *  AutoMl.ListColumnSpecs google.cloud.automl.v1beta1.AutoMl.ListColumnSpecs  call.
       */
      // const pageToken = 'abc123'
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callListColumnSpecs() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = automlClient.[listColumnSpecsAsync](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/v1beta1.automlclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListColumnSpecs();
    
    

### listColumnSpecsStream(request, options)
    
    
    listColumnSpecsStream(request?: protos.google.cloud.automl.v1beta1.IListColumnSpecsRequest, options?: CallOptions): Transform;

Equivalent to `listColumnSpecs`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListColumnSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistcolumnspecsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listColumnSpecsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDatasets(request, options)
    
    
    listDatasets(request?: protos.google.cloud.automl.v1beta1.IListDatasetsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.automl.v1beta1.IDataset[],
            protos.google.cloud.automl.v1beta1.IListDatasetsRequest | null,
            protos.google.cloud.automl.v1beta1.IListDatasetsResponse
        ]>;

Lists datasets in a project.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistdatasetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.automl.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.idataset)[], [protos.google.cloud.automl.v1beta1.IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistdatasetsrequest) | null, [protos.google.cloud.automl.v1beta1.IListDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistdatasetsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Dataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.dataset). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listDatasetsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDatasets(request, options, callback)
    
    
    listDatasets(request: protos.google.cloud.automl.v1beta1.IListDatasetsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.automl.v1beta1.IListDatasetsRequest, protos.google.cloud.automl.v1beta1.IListDatasetsResponse | null | undefined, protos.google.cloud.automl.v1beta1.IDataset>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistdatasetsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.automl.v1beta1.IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistdatasetsrequest), [protos.google.cloud.automl.v1beta1.IListDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistdatasetsresponse) | null | undefined, [protos.google.cloud.automl.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.idataset)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDatasets(request, callback)
    
    
    listDatasets(request: protos.google.cloud.automl.v1beta1.IListDatasetsRequest, callback: PaginationCallback<protos.google.cloud.automl.v1beta1.IListDatasetsRequest, protos.google.cloud.automl.v1beta1.IListDatasetsResponse | null | undefined, protos.google.cloud.automl.v1beta1.IDataset>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistdatasetsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.automl.v1beta1.IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistdatasetsrequest), [protos.google.cloud.automl.v1beta1.IListDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistdatasetsresponse) | null | undefined, [protos.google.cloud.automl.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.idataset)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDatasetsAsync(request, options)
    
    
    listDatasetsAsync(request?: protos.google.cloud.automl.v1beta1.IListDatasetsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.automl.v1beta1.IDataset>;

Equivalent to `listDatasets`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistdatasetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.automl.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.idataset)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Dataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.dataset). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the project from which to list datasets.
       */
      // const parent = 'abc123'
      /**
       *  An expression for filtering the results of the request.
       *    * `dataset_metadata` - for existence of the case (e.g.
       *              `image_classification_dataset_metadata:*`). Some examples of
       *              using the filter are:
       *    * `translation_dataset_metadata:*` --> The dataset has
       *                                           `translation_dataset_metadata`.
       */
      // const filter = 'abc123'
      /**
       *  Requested page size. Server may return fewer results than requested.
       *  If unspecified, server will pick a default size.
       */
      // const pageSize = 1234
      /**
       *  A token identifying a page of results for the server to return
       *  Typically obtained via
       *  ListDatasetsResponse.next_page_token google.cloud.automl.v1beta1.ListDatasetsResponse.next_page_token  of the previous
       *  AutoMl.ListDatasets google.cloud.automl.v1beta1.AutoMl.ListDatasets  call.
       */
      // const pageToken = 'abc123'
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callListDatasets() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = automlClient.listDatasetsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListDatasets();
    
    

### listDatasetsStream(request, options)
    
    
    listDatasetsStream(request?: protos.google.cloud.automl.v1beta1.IListDatasetsRequest, options?: CallOptions): Transform;

Equivalent to `listDatasets`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistdatasetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Dataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.dataset) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listDatasetsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listModelEvaluations(request, options)
    
    
    listModelEvaluations(request?: protos.google.cloud.automl.v1beta1.IListModelEvaluationsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.automl.v1beta1.IModelEvaluation[],
            protos.google.cloud.automl.v1beta1.IListModelEvaluationsRequest | null,
            protos.google.cloud.automl.v1beta1.IListModelEvaluationsResponse
        ]>;

Lists model evaluations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelevaluationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.automl.v1beta1.IModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodelevaluation)[], [protos.google.cloud.automl.v1beta1.IListModelEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelevaluationsrequest) | null, [protos.google.cloud.automl.v1beta1.IListModelEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelevaluationsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [ModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.modelevaluation). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listModelEvaluationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listModelEvaluations(request, options, callback)
    
    
    listModelEvaluations(request: protos.google.cloud.automl.v1beta1.IListModelEvaluationsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.automl.v1beta1.IListModelEvaluationsRequest, protos.google.cloud.automl.v1beta1.IListModelEvaluationsResponse | null | undefined, protos.google.cloud.automl.v1beta1.IModelEvaluation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelevaluationsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.automl.v1beta1.IListModelEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelevaluationsrequest), [protos.google.cloud.automl.v1beta1.IListModelEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelevaluationsresponse) | null | undefined, [protos.google.cloud.automl.v1beta1.IModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodelevaluation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listModelEvaluations(request, callback)
    
    
    listModelEvaluations(request: protos.google.cloud.automl.v1beta1.IListModelEvaluationsRequest, callback: PaginationCallback<protos.google.cloud.automl.v1beta1.IListModelEvaluationsRequest, protos.google.cloud.automl.v1beta1.IListModelEvaluationsResponse | null | undefined, protos.google.cloud.automl.v1beta1.IModelEvaluation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelevaluationsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.automl.v1beta1.IListModelEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelevaluationsrequest), [protos.google.cloud.automl.v1beta1.IListModelEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelevaluationsresponse) | null | undefined, [protos.google.cloud.automl.v1beta1.IModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodelevaluation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listModelEvaluationsAsync(request, options)
    
    
    listModelEvaluationsAsync(request?: protos.google.cloud.automl.v1beta1.IListModelEvaluationsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.automl.v1beta1.IModelEvaluation>;

Equivalent to `listModelEvaluations`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelevaluationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.automl.v1beta1.IModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodelevaluation)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [ModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.modelevaluation). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name of the model to list the model evaluations for.
       *  If modelId is set as "-", this will list model evaluations from across all
       *  models of the parent location.
       */
      // const parent = 'abc123'
      /**
       *  An expression for filtering the results of the request.
       *    * `annotation_spec_id` - for =, !=  or existence. See example below for
       *                           the last.
       *  Some examples of using the filter are:
       *    * `annotation_spec_id!=4` --> The model evaluation was done for
       *                              annotation spec with ID different than 4.
       *    * `NOT annotation_spec_id:*` --> The model evaluation was done for
       *                                 aggregate of all annotation specs.
       */
      // const filter = 'abc123'
      /**
       *  Requested page size.
       */
      // const pageSize = 1234
      /**
       *  A token identifying a page of results for the server to return.
       *  Typically obtained via
       *  ListModelEvaluationsResponse.next_page_token google.cloud.automl.v1beta1.ListModelEvaluationsResponse.next_page_token  of the previous
       *  AutoMl.ListModelEvaluations google.cloud.automl.v1beta1.AutoMl.ListModelEvaluations  call.
       */
      // const pageToken = 'abc123'
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callListModelEvaluations() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = automlClient.listModelEvaluationsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListModelEvaluations();
    
    

### listModelEvaluationsStream(request, options)
    
    
    listModelEvaluationsStream(request?: protos.google.cloud.automl.v1beta1.IListModelEvaluationsRequest, options?: CallOptions): Transform;

Equivalent to `listModelEvaluations`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelevaluationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [ModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.modelevaluation) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listModelEvaluationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listModels(request, options)
    
    
    listModels(request?: protos.google.cloud.automl.v1beta1.IListModelsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.automl.v1beta1.IModel[],
            protos.google.cloud.automl.v1beta1.IListModelsRequest | null,
            protos.google.cloud.automl.v1beta1.IListModelsResponse
        ]>;

Lists models.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.automl.v1beta1.IModel](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodel)[], [protos.google.cloud.automl.v1beta1.IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelsrequest) | null, [protos.google.cloud.automl.v1beta1.IListModelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listModelsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listModels(request, options, callback)
    
    
    listModels(request: protos.google.cloud.automl.v1beta1.IListModelsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.automl.v1beta1.IListModelsRequest, protos.google.cloud.automl.v1beta1.IListModelsResponse | null | undefined, protos.google.cloud.automl.v1beta1.IModel>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.automl.v1beta1.IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelsrequest), [protos.google.cloud.automl.v1beta1.IListModelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelsresponse) | null | undefined, [protos.google.cloud.automl.v1beta1.IModel](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodel)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listModels(request, callback)
    
    
    listModels(request: protos.google.cloud.automl.v1beta1.IListModelsRequest, callback: PaginationCallback<protos.google.cloud.automl.v1beta1.IListModelsRequest, protos.google.cloud.automl.v1beta1.IListModelsResponse | null | undefined, protos.google.cloud.automl.v1beta1.IModel>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.automl.v1beta1.IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelsrequest), [protos.google.cloud.automl.v1beta1.IListModelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelsresponse) | null | undefined, [protos.google.cloud.automl.v1beta1.IModel](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodel)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listModelsAsync(request, options)
    
    
    listModelsAsync(request?: protos.google.cloud.automl.v1beta1.IListModelsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.automl.v1beta1.IModel>;

Equivalent to `listModels`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.automl.v1beta1.IModel](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodel)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name of the project, from which to list the models.
       */
      // const parent = 'abc123'
      /**
       *  An expression for filtering the results of the request.
       *    * `model_metadata` - for existence of the case (e.g.
       *              `video_classification_model_metadata:*`).
       *    * `dataset_id` - for = or !=. Some examples of using the filter are:
       *    * `image_classification_model_metadata:*` --> The model has
       *                                       `image_classification_model_metadata`.
       *    * `dataset_id=5` --> The model was created from a dataset with ID 5.
       */
      // const filter = 'abc123'
      /**
       *  Requested page size.
       */
      // const pageSize = 1234
      /**
       *  A token identifying a page of results for the server to return
       *  Typically obtained via
       *  ListModelsResponse.next_page_token google.cloud.automl.v1beta1.ListModelsResponse.next_page_token  of the previous
       *  AutoMl.ListModels google.cloud.automl.v1beta1.AutoMl.ListModels  call.
       */
      // const pageToken = 'abc123'
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callListModels() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = automlClient.listModelsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListModels();
    
    

### listModelsStream(request, options)
    
    
    listModelsStream(request?: protos.google.cloud.automl.v1beta1.IListModelsRequest, options?: CallOptions): Transform;

Equivalent to `listModels`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilistmodelsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listModelsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listTableSpecs(request, options)
    
    
    listTableSpecs(request?: protos.google.cloud.automl.v1beta1.IListTableSpecsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.automl.v1beta1.ITableSpec[],
            protos.google.cloud.automl.v1beta1.IListTableSpecsRequest | null,
            protos.google.cloud.automl.v1beta1.IListTableSpecsResponse
        ]>;

Lists table specs in a dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTableSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilisttablespecsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.automl.v1beta1.ITableSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.itablespec)[], [protos.google.cloud.automl.v1beta1.IListTableSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilisttablespecsrequest) | null, [protos.google.cloud.automl.v1beta1.IListTableSpecsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilisttablespecsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [TableSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.tablespec). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listTableSpecsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listTableSpecs(request, options, callback)
    
    
    listTableSpecs(request: protos.google.cloud.automl.v1beta1.IListTableSpecsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.automl.v1beta1.IListTableSpecsRequest, protos.google.cloud.automl.v1beta1.IListTableSpecsResponse | null | undefined, protos.google.cloud.automl.v1beta1.ITableSpec>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTableSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilisttablespecsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.automl.v1beta1.IListTableSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilisttablespecsrequest), [protos.google.cloud.automl.v1beta1.IListTableSpecsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilisttablespecsresponse) | null | undefined, [protos.google.cloud.automl.v1beta1.ITableSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.itablespec)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTableSpecs(request, callback)
    
    
    listTableSpecs(request: protos.google.cloud.automl.v1beta1.IListTableSpecsRequest, callback: PaginationCallback<protos.google.cloud.automl.v1beta1.IListTableSpecsRequest, protos.google.cloud.automl.v1beta1.IListTableSpecsResponse | null | undefined, protos.google.cloud.automl.v1beta1.ITableSpec>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTableSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilisttablespecsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.automl.v1beta1.IListTableSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilisttablespecsrequest), [protos.google.cloud.automl.v1beta1.IListTableSpecsResponse](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilisttablespecsresponse) | null | undefined, [protos.google.cloud.automl.v1beta1.ITableSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.itablespec)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTableSpecsAsync(request, options)
    
    
    listTableSpecsAsync(request?: protos.google.cloud.automl.v1beta1.IListTableSpecsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.automl.v1beta1.ITableSpec>;

Equivalent to `listTableSpecs`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTableSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilisttablespecsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.automl.v1beta1.ITableSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.itablespec)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [TableSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.tablespec). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the dataset to list table specs from.
       */
      // const parent = 'abc123'
      /**
       *  Mask specifying which fields to read.
       */
      // const fieldMask = {}
      /**
       *  Filter expression, see go/filtering.
       */
      // const filter = 'abc123'
      /**
       *  Requested page size. The server can return fewer results than requested.
       *  If unspecified, the server will pick a default size.
       */
      // const pageSize = 1234
      /**
       *  A token identifying a page of results for the server to return.
       *  Typically obtained from the
       *  ListTableSpecsResponse.next_page_token google.cloud.automl.v1beta1.ListTableSpecsResponse.next_page_token  field of the previous
       *  AutoMl.ListTableSpecs google.cloud.automl.v1beta1.AutoMl.ListTableSpecs  call.
       */
      // const pageToken = 'abc123'
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callListTableSpecs() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = automlClient.[listTableSpecsAsync](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/v1beta1.automlclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListTableSpecs();
    
    

### listTableSpecsStream(request, options)
    
    
    listTableSpecsStream(request?: protos.google.cloud.automl.v1beta1.IListTableSpecsRequest, options?: CallOptions): Transform;

Equivalent to `listTableSpecs`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTableSpecsRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ilisttablespecsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [TableSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.tablespec) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listTableSpecsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### undeployModel(request, options)
    
    
    undeployModel(request?: protos.google.cloud.automl.v1beta1.IUndeployModelRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Undeploys a model. If the model is not deployed this method has no effect.

Only applicable for Text Classification, Image Object Detection and Tables; all other domains manage deployment automatically.

Returns an empty response in the [response](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.operation) field when it completes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUndeployModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iundeploymodelrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name of the model to undeploy.
       */
      // const name = 'abc123'
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callUndeployModel() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await automlClient.undeployModel(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUndeployModel();
    
    

### undeployModel(request, options, callback)
    
    
    undeployModel(request: protos.google.cloud.automl.v1beta1.IUndeployModelRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUndeployModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iundeploymodelrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### undeployModel(request, callback)
    
    
    undeployModel(request: protos.google.cloud.automl.v1beta1.IUndeployModelRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.automl.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUndeployModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iundeploymodelrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.protobuf.iempty), [protos.google.cloud.automl.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateColumnSpec(request, options)
    
    
    updateColumnSpec(request?: protos.google.cloud.automl.v1beta1.IUpdateColumnSpecRequest, options?: CallOptions): Promise<[
            protos.google.cloud.automl.v1beta1.IColumnSpec,
            protos.google.cloud.automl.v1beta1.IUpdateColumnSpecRequest | undefined,
            {} | undefined
        ]>;

Updates a column spec.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateColumnSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatecolumnspecrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.automl.v1beta1.IColumnSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icolumnspec), [protos.google.cloud.automl.v1beta1.IUpdateColumnSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatecolumnspecrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The column spec which replaces the resource on the server.
       */
      // const columnSpec = {}
      /**
       *  The update mask applies to the resource.
       */
      // const updateMask = {}
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callUpdateColumnSpec() {
        // Construct request
        const request = {
          columnSpec,
        };
    
        // Run request
        const response = await automlClient.updateColumnSpec(request);
        console.log(response);
      }
    
      callUpdateColumnSpec();
    
    

### updateColumnSpec(request, options, callback)
    
    
    updateColumnSpec(request: protos.google.cloud.automl.v1beta1.IUpdateColumnSpecRequest, options: CallOptions, callback: Callback<protos.google.cloud.automl.v1beta1.IColumnSpec, protos.google.cloud.automl.v1beta1.IUpdateColumnSpecRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateColumnSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatecolumnspecrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.IColumnSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icolumnspec), [protos.google.cloud.automl.v1beta1.IUpdateColumnSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatecolumnspecrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateColumnSpec(request, callback)
    
    
    updateColumnSpec(request: protos.google.cloud.automl.v1beta1.IUpdateColumnSpecRequest, callback: Callback<protos.google.cloud.automl.v1beta1.IColumnSpec, protos.google.cloud.automl.v1beta1.IUpdateColumnSpecRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateColumnSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatecolumnspecrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.IColumnSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.icolumnspec), [protos.google.cloud.automl.v1beta1.IUpdateColumnSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatecolumnspecrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataset(request, options)
    
    
    updateDataset(request?: protos.google.cloud.automl.v1beta1.IUpdateDatasetRequest, options?: CallOptions): Promise<[
            protos.google.cloud.automl.v1beta1.IDataset,
            protos.google.cloud.automl.v1beta1.IUpdateDatasetRequest | undefined,
            {} | undefined
        ]>;

Updates a dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatedatasetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.automl.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.idataset), [protos.google.cloud.automl.v1beta1.IUpdateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatedatasetrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Dataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.dataset). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The dataset which replaces the resource on the server.
       */
      // const dataset = {}
      /**
       *  The update mask applies to the resource.
       */
      // const updateMask = {}
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callUpdateDataset() {
        // Construct request
        const request = {
          dataset,
        };
    
        // Run request
        const response = await automlClient.updateDataset(request);
        console.log(response);
      }
    
      callUpdateDataset();
    
    

### updateDataset(request, options, callback)
    
    
    updateDataset(request: protos.google.cloud.automl.v1beta1.IUpdateDatasetRequest, options: CallOptions, callback: Callback<protos.google.cloud.automl.v1beta1.IDataset, protos.google.cloud.automl.v1beta1.IUpdateDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatedatasetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.idataset), [protos.google.cloud.automl.v1beta1.IUpdateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatedatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataset(request, callback)
    
    
    updateDataset(request: protos.google.cloud.automl.v1beta1.IUpdateDatasetRequest, callback: Callback<protos.google.cloud.automl.v1beta1.IDataset, protos.google.cloud.automl.v1beta1.IUpdateDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatedatasetrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.idataset), [protos.google.cloud.automl.v1beta1.IUpdateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatedatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTableSpec(request, options)
    
    
    updateTableSpec(request?: protos.google.cloud.automl.v1beta1.IUpdateTableSpecRequest, options?: CallOptions): Promise<[
            protos.google.cloud.automl.v1beta1.ITableSpec,
            protos.google.cloud.automl.v1beta1.IUpdateTableSpecRequest | undefined,
            {} | undefined
        ]>;

Updates a table spec.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTableSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatetablespecrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.automl.v1beta1.ITableSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.itablespec), [protos.google.cloud.automl.v1beta1.IUpdateTableSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatetablespecrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [TableSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.tablespec). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The table spec which replaces the resource on the server.
       */
      // const tableSpec = {}
      /**
       *  The update mask applies to the resource.
       */
      // const updateMask = {}
    
      // Imports the Automl library
      const {AutoMlClient} = require('[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const automlClient = new [AutoMlClient](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)();
    
      async function callUpdateTableSpec() {
        // Construct request
        const request = {
          tableSpec,
        };
    
        // Run request
        const response = await automlClient.updateTableSpec(request);
        console.log(response);
      }
    
      callUpdateTableSpec();
    
    

### updateTableSpec(request, options, callback)
    
    
    updateTableSpec(request: protos.google.cloud.automl.v1beta1.IUpdateTableSpecRequest, options: CallOptions, callback: Callback<protos.google.cloud.automl.v1beta1.ITableSpec, protos.google.cloud.automl.v1beta1.IUpdateTableSpecRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTableSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatetablespecrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.ITableSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.itablespec), [protos.google.cloud.automl.v1beta1.IUpdateTableSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatetablespecrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTableSpec(request, callback)
    
    
    updateTableSpec(request: protos.google.cloud.automl.v1beta1.IUpdateTableSpecRequest, callback: Callback<protos.google.cloud.automl.v1beta1.ITableSpec, protos.google.cloud.automl.v1beta1.IUpdateTableSpecRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTableSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatetablespecrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.automl.v1beta1.ITableSpec](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.itablespec), [protos.google.cloud.automl.v1beta1.IUpdateTableSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.iupdatetablespecrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
